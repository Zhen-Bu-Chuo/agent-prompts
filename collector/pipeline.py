"""Resolve immutable versions, select prompt sources, and update indexes."""
import fnmatch
import hashlib
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import yaml

from . import __version__
from .archive import archive_snapshot, read_manifest, source_link, write_if_changed, write_json
from .extract import extract
from .sources import choose_release

LICENSE_PATTERNS = {
    "MIT": r"(?i)\bMIT License\b|Permission is hereby granted, free of charge",
    "Apache-2.0": r"(?i)Apache License.*Version 2\.0",
    "BSD-2-Clause": r"(?i)Redistribution and use in source and binary forms.*retain the copyright notice",
    "BSD-3-Clause": r"(?i)Redistribution and use in source and binary forms.*Neither the name",
    "ISC": r"(?i)Permission to use, copy, modify, and/or distribute this software",
    "MPL-2.0": r"(?i)Mozilla Public License.*2\.0",
    "GPL-3.0-only": r"(?i)GNU GENERAL PUBLIC LICENSE.*Version 3",
    "GPL-3.0-or-later": r"(?i)GNU GENERAL PUBLIC LICENSE.*Version 3",
    "AGPL-3.0-only": r"(?i)GNU AFFERO GENERAL PUBLIC LICENSE.*Version 3",
    "AGPL-3.0-or-later": r"(?i)GNU AFFERO GENERAL PUBLIC LICENSE.*Version 3",
    "EPL-2.0": r"(?i)Eclipse Public License.*2\.0",
    "Unlicense": r"(?i)This is free and unencumbered software released into the public domain",
}


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _adapter_files(root):
    directory = Path(root) / "adapters"
    return [yaml.safe_load(path.read_text(encoding="utf-8")) for path in sorted(directory.glob("*.yaml"))]


def _license(repo_info, tree, client, repo, commit, adapter):
    spdx = adapter.get("license_override") or ((repo_info.get("license") or {}).get("spdx_id"))
    license_file = adapter.get("license_path")
    if not license_file:
        license_file = next((path for path in tree if Path(path).name.lower() in
                             {"license", "license.md", "license.txt", "copying"}), None)
    text = client.file(repo, commit, license_file) if license_file and spdx in (None, "NOASSERTION", "OTHER") else None
    if not spdx or spdx in ("NOASSERTION", "OTHER"):
        for candidate, pattern in LICENSE_PATTERNS.items():
            if text and re.search(pattern, text[:12000], re.S):
                spdx = candidate
                break
    # A SPDX identifier is useful only when its redistribution terms are known here.
    if spdx not in LICENSE_PATTERNS:
        return dict(spdx=spdx, file=license_file, text=text, allowed=False,
                    reason=adapter.get("license_notes") or "Could not verify a redistributable license from the pinned source.")
    if text is None and license_file:
        text = client.file(repo, commit, license_file)
    return dict(spdx=spdx, file=license_file, text=text, allowed=True, reason=None)


def _snapshot_for(client, repo_info, repo, ref, ref_kind, release=None):
    commit = client.commit(repo, ref)
    result = dict(repository=repo_info["full_name"], ref_kind=ref_kind, source_ref=ref,
                  source_commit=commit["sha"], source_committed_at=commit["commit"]["committer"]["date"],
                  upstream_version=release["tag_name"] if release else None,
                  release_published_at=release.get("published_at") if release else None,
                  package_version=None)
    return result


def _license_record(root, adapter, snapshot, license_info, observed_at, only_latest=False):
    slug = adapter["slug"]
    value = dict(agent=slug, repository=adapter["repository"], source_commit=snapshot["source_commit"],
                 source_ref=snapshot.get("source_ref"), ref_kind=snapshot.get("ref_kind"),
                 upstream_version=snapshot.get("upstream_version"),
                 source_committed_at=snapshot.get("source_committed_at"),
                 release_published_at=snapshot.get("release_published_at"),
                 collected_at=observed_at,
                 source_path=license_info["file"], license=license_info["spdx"],
                 license_permalink=source_link(adapter["repository"], snapshot["source_commit"], license_info["file"])
                 if license_info["file"] else None,
                 redistribution_allowed=license_info["allowed"],
                 limitations=[license_info["reason"]] if license_info["reason"] else [])
    if license_info["text"] and license_info["allowed"]:
        ext = Path(license_info["file"] or "LICENSE.txt").suffix or ".txt"
        rel = Path("licenses") / slug / (snapshot["source_commit"][:12] + ext)
        write_if_changed(Path(root) / rel, license_info["text"])
        value["license_text_path"] = rel.as_posix()
        if only_latest:
            license_dir = Path(root) / "licenses" / slug
            for old in license_dir.glob("*"):
                if old != Path(root) / rel and old.is_file() and not old.is_symlink():
                    old.unlink()
    index_path = Path(root) / "indexes" / f"{slug}-source.json"
    if index_path.exists():
        previous = json.loads(index_path.read_text(encoding="utf-8"))
        current_state = {key: item for key, item in value.items() if key != "collected_at"}
        previous_state = {key: item for key, item in previous.items() if key != "collected_at"}
        if current_state == previous_state:
            value["collected_at"] = previous.get("collected_at", observed_at)
    write_json(index_path, value)


def _match_paths(paths, rule):
    pattern = rule["glob"].replace("\\", "/")
    return [p for p in paths if fnmatch.fnmatchcase(p, pattern) and not any(
        part.lower() in {"tests", "test", "fixtures", "examples", "example", "node_modules", "vendor", "dist-info", "__pycache__"}
        for part in Path(p).parts)]


def _collect_snapshot(root, adapter, client, snapshot, paths, license_info, observed_at, only_latest=False):
    repo = adapter["repository"]
    slug = adapter["slug"]
    if not license_info["allowed"]:
        reason = "; ".join(adapter.get("limitations", [])) or license_info["reason"]
        license_info = dict(license_info, reason=reason)
        _license_record(root, adapter, snapshot, license_info, observed_at, only_latest)
        return dict(status="unavailable", agent=slug, files=0, prompts=0, new_files=0,
                    repository=repo, version=snapshot.get("upstream_version"),
                    ref=snapshot.get("source_ref"), commit=snapshot.get("source_commit"),
                    ref_kind=snapshot.get("ref_kind"), reason=reason)
    if adapter.get("coverage") == "unavailable":
        reason = "; ".join(adapter.get("limitations", [])) or "No static prompt source configured."
        _license_record(root, adapter, snapshot, license_info, observed_at, only_latest)
        return dict(status="unavailable", agent=slug, files=0, prompts=0, new_files=0,
                    repository=repo, version=snapshot.get("upstream_version"),
                    ref=snapshot.get("source_ref"), commit=snapshot.get("source_commit"),
                    ref_kind=snapshot.get("ref_kind"), reason=reason)
    snapshot["license"] = license_info["spdx"]
    snapshot["adapter_sha256"] = hashlib.sha256(json.dumps(adapter, sort_keys=True).encode()).hexdigest()
    snapshot["extractor_version"] = __version__
    _license_record(root, adapter, snapshot, license_info, observed_at, only_latest)
    manifest = read_manifest(Path(root), slug)
    identity = ":".join(str(snapshot.get(k, "")) for k in
                        ("ref_kind", "source_ref", "source_commit", "adapter_sha256", "extractor_version"))
    if manifest and any(item["id"] == identity for item in manifest["snapshots"]):
        previous = next(item for item in manifest["snapshots"] if item["id"] == identity)
        return dict(status=manifest.get("coverage", "supported"), agent=slug, repository=repo,
                    version=previous.get("upstream_version"), ref=previous.get("source_ref"), commit=previous.get("source_commit"),
                    ref_kind=snapshot.get("ref_kind"),
                    files=0, prompts=len(previous["entries"]), new_files=0,
                    changes={}, snapshot_id=previous["id"], unchanged=True)
    records, checked = [], 0
    rule_results = []
    for rule in adapter.get("rules", []):
        matches = _match_paths(paths, rule)
        extracted = 0
        rule_error = None
        for source_path in matches:
            try:
                source = client.file(repo, snapshot["source_commit"], source_path)
                fragments = extract(source, rule["format"], min_chars=int(rule.get("min_chars", 80)),
                                    key_pattern=rule.get("key_pattern"))
                checked += 1
                for fragment in fragments:
                    records.append(dict(source_path=source_path, module=rule["module"],
                                        variant=rule.get("variant", "default"), fragment=fragment))
                    extracted += 1
            except (UnicodeDecodeError, ValueError, yaml.YAMLError, json.JSONDecodeError) as exc:
                rule_error = f"{source_path}: {exc}"
        rule_results.append(dict(pattern=rule["glob"], matched=len(matches), fragments=extracted,
                                 error=rule_error, required=rule.get("required", True)))
    required_misses = [x for x in rule_results if x["required"] and (x["matched"] == 0 or x["error"])]
    if required_misses or not records:
        raise RuntimeError(f"No complete prompt extraction for {slug}; required rule results: {json.dumps(required_misses or rule_results,ensure_ascii=False)}")
    unique = {}
    for record in records:
        item = record["fragment"]
        key = (record["source_path"], record["module"], record["variant"], item.key, item.content)
        unique.setdefault(key, record)
    result = archive_snapshot(root, adapter, snapshot, list(unique.values()), observed_at, only_latest)
    return dict(status=adapter.get("coverage", "supported"), agent=slug,
                repository=repo, version=snapshot.get("upstream_version"), ref=snapshot["source_ref"],
                commit=snapshot["source_commit"], ref_kind=snapshot.get("ref_kind"),
                files=checked, prompts=result["entries"],
                new_files=result["new_files"], changes=result["changes"],
                rules=rule_results, unchanged=result.get("unchanged", False),
                warnings=[x["error"] for x in rule_results if x["error"]])


def collect_one(root, adapter, client, initial_latest=False):
    observed_at = _now()
    slug = adapter["slug"]
    repo = adapter["repository"]
    try:
        repo_info = client.repository(repo)
        if repo_info.get("archived"):
            adapter["limitations"] = list(adapter.get("limitations", [])) + ["Upstream repository is archived."]
        if hasattr(client, "latest_release"):
            release = client.latest_release(repo, adapter.get("tag_pattern"))
        else:
            release = choose_release(client.releases(repo), adapter.get("tag_pattern"))
        refs = []
        if release:
            refs.append(_snapshot_for(client, repo_info, repo, release["tag_name"], "release", release))
        else:
            refs.append(_snapshot_for(client, repo_info, repo, repo_info["default_branch"], "default-branch"))
        if not initial_latest and release:
            refs.append(_snapshot_for(client, repo_info, repo, repo_info["default_branch"], "default-branch"))
        reports = []
        for snapshot in refs:
            if adapter.get("tree_strategy") == "git":
                paths = client.git_tree(repo, snapshot["source_commit"])
            else:
                paths = client.tree(repo, snapshot["source_commit"])
            license_info = _license(repo_info, paths, client, repo, snapshot["source_commit"], adapter)
            reports.append(_collect_snapshot(root, adapter, client, snapshot, paths, license_info, observed_at,
                                             only_latest=initial_latest))
        _write_status(root, adapter, None, observed_at, reports)
        return reports
    except Exception as exc:
        _write_status(root, adapter, exc, observed_at)
        return [dict(status="error", agent=slug, repository=repo, error=f"{type(exc).__name__}: {exc}")]


def _write_status(root, adapter, error, observed_at, reports=None):
    path = Path(root) / "indexes" / f"{adapter['slug']}-status.json"
    if not error:
        if path.exists():
            path.unlink()
        return
    value = dict(agent=adapter["slug"], repository=adapter["repository"])
    previous = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    message = f"{type(error).__name__}: {error}"
    value["last_error"] = previous.get("last_error") if previous.get("last_error", {}).get("message") == message else dict(message=message, first_observed_at=observed_at)
    write_json(path, value)


def collect_sources(root, adapters=None, client=None, initial_latest=False, workers=4):
    root = Path(root)
    if adapters is None:
        adapters = _adapter_files(root)
    if client is None:
        from .sources import GitHub
        client = GitHub(root / "work" / "github-cache")
    slugset = [str(x["slug"]) for x in adapters]
    if len(slugset) != len(set(slugset)):
        raise ValueError("Adapter slugs must be unique")
    reports = []
    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        futures = [pool.submit(collect_one, root, adapter, client, initial_latest) for adapter in adapters]
        for future in as_completed(futures):
            reports.extend(future.result())
    reports.sort(key=lambda x: (x["agent"], x.get("ref", ""), x.get("commit", "")))
    catalog_path = root / "indexes" / "catalog.json"
    previous = json.loads(catalog_path.read_text(encoding="utf-8")) if catalog_path.exists() else {"agents": []}
    stable = {(item["agent"], item.get("ref_kind", ""), item.get("ref", "")): item
              for item in previous.get("agents", [])}
    for report in reports:
        key = (report["agent"], report.get("ref_kind", ""), report.get("ref", ""))
        if report.get("status") == "error":
            if not any(item["agent"] == report["agent"] for item in stable.values()):
                stable[key] = {k: report.get(k) for k in
                               ("agent", "status", "repository", "version", "ref", "commit", "prompts", "error", "reason")
                               if k in report}
            continue
        for old_key, old_item in list(stable.items()):
            if old_item["agent"] == report["agent"] and (
                    old_item.get("status") == "error" or old_item.get("ref") == report.get("ref")):
                stable.pop(old_key)
        stable[key] = {k: report.get(k) for k in
                       ("agent", "status", "repository", "version", "ref", "commit", "ref_kind", "prompts", "error", "reason")
                       if k in report}
    write_json(catalog_path, dict(agents=sorted(stable.values(), key=lambda x: (x["agent"], x.get("ref_kind", "")))))
    from .docs import sync_mechanism_docs
    changed_docs = sync_mechanism_docs(root, adapters, json.loads(catalog_path.read_text(encoding="utf-8")))
    _write_run_summary(root, reports)
    for report in reports:
        report["changed_mechanism_docs"] = changed_docs
    return reports


def _write_run_summary(root, reports):
    def cell(value):
        return str(value or "").replace("|", "\\|").replace("\n", " ")
    lines = ["# Source collection report", "", "| Agent | Status | Version / ref | Prompts | New files | Result |",
             "| --- | --- | --- | ---: | ---: | --- |"]
    for report in reports:
        lines.append("| " + " | ".join(cell(x) for x in (report["agent"], report["status"], report.get("version") or report.get("ref"), report.get("prompts", 0), report.get("new_files", 0), report.get("error") or report.get("reason") or "ok")) + " |")
    write_if_changed(Path(root) / "work" / "latest-run.md", "\n".join(lines) + "\n")


def validate_archive(root):
    root = Path(root)
    errors = []
    for manifest_path in sorted((root / "indexes").glob("*.json")):
        if manifest_path.name in {"catalog.json"} or manifest_path.name.endswith("-source.json") or manifest_path.name.endswith("-status.json"):
            continue
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            slug = manifest["agent"]
            for snapshot in manifest["snapshots"]:
                seen = set()
                for item in snapshot["entries"]:
                    p = str(safe_path(item["archive_path"]))
                    if p in seen:
                        continue
                    seen.add(p)
                    full = root.joinpath(*Path(p).parts)
                    if not full.is_file():
                        errors.append(f"{slug}: missing archive {p}")
                        continue
                    text = full.read_text(encoding="utf-8")
                    try:
                        _, header, body = text.split("---\n", 2)
                        meta = yaml.safe_load(header)
                    except (ValueError, yaml.YAMLError) as exc:
                        errors.append(f"{slug}: malformed archive {p}: {exc}")
                        continue
                    digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
                    if digest != meta.get("content_sha256") or digest != item.get("content_sha256"):
                        errors.append(f"{slug}: hash mismatch for {p}")
                    if meta.get("source_commit") not in (snap for snap in [x.get("source_commit") for x in manifest["snapshots"]]):
                        # Content deduplicated across releases keeps its first-seen commit.
                        if not meta.get("source_permalink", "").startswith("https://github.com/"):
                            errors.append(f"{slug}: missing pinned GitHub provenance for {p}")
                    if not meta.get("source_permalink", "").startswith("https://github.com/"):
                        errors.append(f"{slug}: invalid source permalink for {p}")
        except (KeyError, ValueError, OSError, json.JSONDecodeError) as exc:
            errors.append(f"{manifest_path.name}: {exc}")
    return errors


def safe_path(value):
    from .archive import safe_relative
    return safe_relative(value)
