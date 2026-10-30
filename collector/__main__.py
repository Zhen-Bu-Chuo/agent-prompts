"""Command-line entry points for local and scheduled collection."""
import argparse
import json
import sys
from pathlib import Path

from .archive import write_if_changed
from .pipeline import collect_sources, validate_archive


def main(argv=None):
    parser = argparse.ArgumentParser(prog="agent-prompts", description="Collect public, source-pinned AI agent prompts")
    parser.add_argument("command", choices=["collect", "validate"], nargs="?", default="collect")
    parser.add_argument("--root", default=None, help="Repository root (defaults to the project root)")
    parser.add_argument("--initial-latest", action="store_true", help="Collect only the latest stable release per source")
    parser.add_argument("--agents", nargs="+", help="Limit collection to these adapter slugs")
    parser.add_argument("--workers", type=int, default=4, help="Maximum source repositories processed concurrently")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]
    if args.command == "validate":
        errors = validate_archive(root)
        for error in errors:
            print(error)
        if not errors:
            print("Archive validation passed.")
        return 1 if errors else 0
    from .pipeline import _adapter_files
    adapters = _adapter_files(root)
    if args.agents:
        wanted = set(args.agents)
        known = {item["slug"] for item in adapters}
        missing = wanted - known
        if missing:
            parser.error("Unknown agent slugs: " + ", ".join(sorted(missing)))
        adapters = [item for item in adapters if item["slug"] in wanted]
    reports = collect_sources(root, adapters=adapters, initial_latest=args.initial_latest, workers=args.workers)
    report_path = root / "work" / "latest-run.md"
    print(report_path.read_text(encoding="utf-8"))
    if "GITHUB_STEP_SUMMARY" in __import__("os").environ:
        with open(__import__("os").environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as stream:
            stream.write(report_path.read_text(encoding="utf-8"))
    for report in reports:
        print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 1 if any(report["status"] == "error" for report in reports) else 0


if __name__ == "__main__":
    sys.exit(main())
