"""Keep source mechanism notes pinned to each agent's current archive snapshot."""
import fnmatch
import json
from pathlib import Path

from .archive import source_link, write_if_changed


def sync_mechanism_docs(root, adapters, catalog):
    root = Path(root)
    catalog_rows = {}
    for item in catalog.get("agents", []):
        catalog_rows.setdefault(item["agent"], []).append(item)
    changed = 0
    for adapter in adapters:
        slug = adapter["slug"]
        repository = adapter["repository"]
        manifest_path = root / "indexes" / f"{slug}.json"
        source_path = root / "indexes" / f"{slug}-source.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else None
        source = json.loads(source_path.read_text(encoding="utf-8")) if source_path.exists() else {}
        snapshot = None
        if manifest and manifest.get("snapshots"):
            preferred_id = manifest.get("current", {}).get("release") or manifest.get("current", {}).get("default-branch")
            snapshot = next((x for x in manifest["snapshots"] if x["id"] == preferred_id), manifest["snapshots"][-1])
        rows = catalog_rows.get(slug, [])
        preferred = next((x for x in rows if x.get("ref_kind") == "release"), None)
        preferred = preferred or next(iter(rows), {})
        source_ref = (snapshot or {}).get("source_ref") or preferred.get("ref") or source.get("source_ref")
        source_commit = (snapshot or {}).get("source_commit") or preferred.get("commit") or source.get("source_commit")
        if not source_ref or not source_commit:
            source_ref = source_ref or preferred.get("ref") or "unresolved"
            source_commit = source_commit or preferred.get("commit") or "unresolved"
        version = (snapshot or {}).get("upstream_version") or preferred.get("version") or source.get("upstream_version") or source_ref
        license_id = source.get("license") or "not granted or undetermined"
        coverage = (manifest or {}).get("coverage") or adapter.get("coverage", "supported")
        entries = (snapshot or {}).get("entries", [])
        source_files = {}
        for entry in entries:
            source_files.setdefault(entry["source_path"], set()).add(entry["module"])

        table = ["| Module | Extractor | Pinned source |", "| --- | --- | --- |"]
        if source_files:
            for path, modules in sorted(source_files.items()):
                formats = sorted({rule["format"] for rule in adapter.get("rules", [])
                                  if rule.get("module") in modules and fnmatch.fnmatchcase(path, rule["glob"])})
                label = ", ".join(f"`{module}`" for module in sorted(modules))
                extractor = ", ".join(f"`{fmt}`" for fmt in formats) or "static source"
                permalink = source_link(repository, source_commit, path)
                table.append(f"| {label} | {extractor} | [`{path}`]({permalink}) |")
        else:
            table.append("| — | metadata only | No prompt text is copied from this pinned source. |")

        limitations = adapter.get("limitations", [])
        coverage_lines = [f"- Coverage: `{coverage}`.", f"- Pinned upstream version: `{version}` at commit `{source_commit}`."]
        coverage_lines.extend(f"- {item}" for item in limitations)
        content = (f"# {adapter['name']} prompt and mechanism sources\n\n"
                   f"- Repository: [`{repository}`](https://github.com/{repository})\n"
                   f"- Selected release/branch: `{source_ref}`\n"
                   f"- Commit: `{source_commit}`\n"
                   f"- SPDX metadata: `{license_id}`\n"
                   f"- Collection status: `{coverage}`\n\n"
                   "## Selected source files\n\n" + "\n".join(table) +
                   "\n\n## Current coverage\n\n" + "\n".join(coverage_lines) + "\n\n")

        path = root / "docs" / "mechanisms" / f"{slug}.md"
        if path.exists():
            old = path.read_text(encoding="utf-8")
            marker = "## Collection notes\n"
            notes = old.split(marker, 1)[1] if marker in old else "\nSource paths and release metadata are maintained from the pinned archive index.\n"
            content += marker + notes.strip() + "\n"
        else:
            content += "## Collection notes\n\nThe collector reads pinned public source files as data.\n"
        changed += write_if_changed(path, content)
    return changed
