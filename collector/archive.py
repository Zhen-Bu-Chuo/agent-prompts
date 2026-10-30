"""Immutable prompt records, deterministic indexes and change tracking."""
import hashlib
import json
import re
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import yaml

from . import __version__


def safe_relative(value):
    if not value or "\\" in value or re.match(r"^[A-Za-z]:", value):
        raise ValueError(f"Unsafe relative path: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Unsafe relative path: {value!r}")
    return path


def write_if_changed(path, content):
    encoded = content.encode("utf-8") if isinstance(content, str) else content
    if path.exists() and path.read_bytes() == encoded:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(encoded)
    return True


def write_json(path, value):
    return write_if_changed(path, json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def read_manifest(root, slug):
    path = root / "indexes" / f"{slug}.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def _name(value, length=60):
    result = re.sub(r"[^a-zA-Z0-9._-]+", "-", str(value)).strip(".-")[:length] or "default"
    if result.lower() in {"con", "prn", "aux", "nul", *(f"com{i}" for i in range(1, 10)), *(f"lpt{i}" for i in range(1, 10))}:
        result = "_" + result
    return result


def source_link(repository, commit, path, start=None, end=None):
    link = f"https://github.com/{repository}/blob/{commit}/{quote(path, safe='/')}"
    return link + (f"#L{start}-L{end}" if start else "")


def _changes(previous, entries):
    old = {x["prompt_id"]: x for x in previous}
    new = {x["prompt_id"]: x for x in entries}
    added = [x for k, x in new.items() if k not in old]
    removed = [x for k, x in old.items() if k not in new]
    changed = [dict(prompt_id=k, before=old[k]["archive_path"], after=x["archive_path"])
               for k, x in new.items() if k in old and old[k]["content_sha256"] != x["content_sha256"]]
    moved = []
    for item in list(added):
        match = next((x for x in removed if (x["content_sha256"], x["module"], x["variant"]) ==
                      (item["content_sha256"], item["module"], item["variant"])), None)
        if match:
            moved.append(dict(before=match["source_path"], after=item["source_path"], archive_path=item["archive_path"]))
            added.remove(item)
            removed.remove(match)
    return dict(added=[x["prompt_id"] for x in added], changed=changed, moved=moved,
                removed=[x["prompt_id"] for x in removed])


def archive_snapshot(root, adapter, snapshot, records, collected_at, only_latest=False):
    root = Path(root)
    slug = str(safe_relative(adapter["slug"]))
    manifest = read_manifest(root, slug) or dict(schema_version=1, agent=slug, name=adapter["name"], snapshots=[], current={})
    manifest.update(repository=adapter["repository"], coverage=adapter.get("coverage", "supported"),
                    limitations=adapter.get("limitations", []), license=snapshot.get("license"),
                    status="ok", last_error=None)
    identity = ":".join(str(snapshot.get(k, "")) for k in
                        ("ref_kind", "source_ref", "source_commit", "adapter_sha256", "extractor_version"))
    # A successful identical snapshot is immutable, including its observation time.
    if any(x["id"] == identity for x in manifest["snapshots"]):
        if only_latest:
            retained = [x for x in manifest["snapshots"] if x["id"] == identity]
            protected = {item["archive_path"] for x in retained for item in x["entries"]}
            old = [x for x in manifest["snapshots"] if x["id"] != identity]
            manifest["snapshots"] = retained
            manifest["current"] = {snapshot["ref_kind"]: identity}
            for previous in old:
                for item in previous["entries"]:
                    rel = str(safe_relative(item["archive_path"]))
                    if rel in protected or safe_relative(rel).parts[:2] != ("agents", slug):
                        continue
                    path = root.joinpath(*safe_relative(rel).parts)
                    if path.is_file() and not path.is_symlink():
                        path.unlink()
        changed = write_json(root / "indexes" / f"{slug}.json", manifest)
        return dict(new_files=0, changed=changed, snapshot_id=identity, entries=len(records), changes={})
    superseded = [old for old in manifest["snapshots"] if only_latest or (
                  old.get("ref_kind") == snapshot.get("ref_kind") and
                  old.get("source_ref") == snapshot.get("source_ref") and
                  old.get("source_commit") == snapshot.get("source_commit"))]
    superseded_ids = {old["id"] for old in superseded}
    existing = {}
    for old in manifest["snapshots"]:
        if old["id"] in superseded_ids:
            continue
        for item in old["entries"]:
            existing.setdefault((item["content_sha256"], item["module"], item["variant"],
                                 old.get("source_ref"), old.get("source_commit"),
                                 item["prompt_id"], item["source_path"]), item["archive_path"])
    entries, new_files = [], 0
    for item in records:
        path = str(safe_relative(item["source_path"]))
        module = str(safe_relative(item["module"]))
        variant = item.get("variant", "default")
        fragment = item["fragment"]
        content_hash = hashlib.sha256(fragment.content.encode("utf-8")).hexdigest()
        prompt_key = f"{path}::{module}::{fragment.key}::{variant}"
        prompt_id = _name(PurePosixPath(path).stem, 35) + "-" + hashlib.sha256(prompt_key.encode()).hexdigest()[:12]
        lookup = (content_hash, module, variant, snapshot.get("source_ref"), snapshot.get("source_commit"),
                  prompt_id, path)
        archive_path = existing.get(lookup)
        permalink = source_link(adapter["repository"], snapshot["source_commit"], path, fragment.start_line, fragment.end_line)
        if archive_path is None:
            stamp = collected_at.replace("-", "").replace(":", "")
            filename = f"{prompt_id}__{_name(variant, 28)}__{_name(snapshot.get('upstream_version') or 'untagged', 28)}__{snapshot['source_commit'][:12]}__{stamp}.md"
            archive_path = str(PurePosixPath("agents", slug, module, filename))
            metadata = dict(agent=slug, prompt_id=prompt_id, module=module, variant=variant,
                            upstream_repository=adapter["repository"], upstream_version=snapshot.get("upstream_version"),
                            package_name=adapter.get("package_name"), package_version=snapshot.get("package_version"),
                            source_ref=snapshot["source_ref"], source_commit=snapshot["source_commit"],
                            source_path=path, source_symbol=fragment.key, source_lines=[fragment.start_line, fragment.end_line],
                            source_permalink=permalink, source_committed_at=snapshot.get("source_committed_at"),
                            release_published_at=snapshot.get("release_published_at"), fetched_at=collected_at,
                            extractor_version=__version__, content_sha256=content_hash, license=snapshot.get("license"),
                            source_kind=fragment.kind, extraction_notes=fragment.notes)
            text = "---\n" + yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False, width=1000) + "---\n" + fragment.content
            destination = root.joinpath(*safe_relative(archive_path).parts)
            if destination.exists() and destination.read_bytes() != text.encode("utf-8"):
                # Distinct contents can be observed at the same second and source ref after extractor changes.
                archive_path = str(PurePosixPath(archive_path).with_name(filename[:-3] + "__" + content_hash[:12] + ".md"))
                destination = root.joinpath(*safe_relative(archive_path).parts)
            new_files += write_if_changed(destination, text)
            existing[lookup] = archive_path
        entries.append(dict(prompt_id=prompt_id, source_path=path, source_symbol=fragment.key,
                            source_lines=[fragment.start_line, fragment.end_line], source_permalink=permalink,
                            module=module, variant=variant, content_sha256=content_hash, archive_path=archive_path))
    entries.sort(key=lambda x: (x["module"], x["source_path"], x["source_symbol"], x["variant"]))
    previous_id = manifest["current"].get(snapshot["ref_kind"])
    previous = next((x["entries"] for x in manifest["snapshots"] if x["id"] == previous_id), [])
    delta = _changes(previous, entries)
    entry = dict(snapshot, id=identity, observed_at=collected_at, entries=entries, changes=delta)
    manifest["snapshots"] = [old for old in manifest["snapshots"] if old["id"] not in superseded_ids]
    manifest["snapshots"].append(entry)
    manifest["current"][snapshot["ref_kind"]] = identity
    referenced = {item["archive_path"] for old in manifest["snapshots"] for item in old["entries"]}
    for old in superseded:
        for item in old["entries"]:
            old_path = str(safe_relative(item["archive_path"]))
            if old_path in referenced or safe_relative(old_path).parts[:2] != ("agents", slug):
                continue
            obsolete = root.joinpath(*safe_relative(old_path).parts)
            if obsolete.is_file() and not obsolete.is_symlink():
                obsolete.unlink()
    write_json(root / "indexes" / f"{slug}.json", manifest)
    return dict(new_files=new_files, changed=True, snapshot_id=identity, entries=len(entries), changes=delta)
