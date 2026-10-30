# Agent Prompts

Agent Prompts is a source-linked collection of prompt templates and the mechanisms that assemble them. Every extracted record identifies the upstream repository, release, immutable commit, source file and lines, collection time, extractor version, license, and SHA-256 of the stored text.

Initial history depth is **one latest stable release per source**. When a repository has no usable stable release, its current default-branch commit is collected. The `--initial-latest` option rebuilds that single-snapshot baseline; daily runs preserve history and follow both the newest stable release and the default branch. Repeating a run at the same commit creates no source change or timestamp-only commit.

The maintained set covers **33 unique upstream projects** across coding and general agents, memory frameworks, and self-evolving agents. A-MEM and memU are relevant to both memory and self-evolution. Each source has a YAML configuration in [`adapters/`](adapters/) and source-selection notes in [`docs/mechanisms/`](docs/mechanisms/). The checked-in [`indexes/catalog.json`](indexes/catalog.json) lists collected versions and refs; projects without redistributable prompt text or a verified static prompt source remain prompt-metadata-only.

## Archive layout

```text
agents/<agent>/<module>/<prompt-id>__<variant>__<release>__<commit>__<first-seen-utc>.md
indexes/<agent>.json                   Immutable version and content index
indexes/<agent>-source.json            Pinned source and license record
licenses/<agent>/<commit>.<ext>        Upstream license text where available
docs/mechanisms/<agent>.md             Source-cited assembly and lifecycle notes
adapters/<agent>.yaml                  Version filter, rules, and source scope
```

Prompt modules include `system`, `memory`, `context`, `tools`, `planning`, `execution`, `editing`, `review`, `subagents`, `modes`, `skills`, `reflection`, `evolution`, `evaluation`, `curriculum`, and `other`. A source template that interpolates runtime state retains its original variables and is labeled as a static template. The collector does not execute source code, templates, prompts, tools, or repository scripts.

The root MIT license applies to the collector, adapter configuration, tests, and original mechanism notes. Prompt text under `agents/` retains the upstream license named in its metadata; the corresponding upstream license text and pinned source link are stored where redistribution is permitted. When permission cannot be verified, the catalog stores source and version metadata without copying prompt text.

## Run

Python 3.11 or later is required. The collector only reads public GitHub repositories. For an authenticated local run, set `GH_TOKEN` to a GitHub token with public repository read access; on Windows it can reuse the logged-in Git Credential Manager. The token is never stored in the repository.

```powershell
python -m pip install -r requirements.txt
python -m collector collect --initial-latest
python -m collector validate
python -m unittest discover -s tests -v
```

Use `python -m collector collect` for normal daily behavior. It checks both the latest stable release and default branch. To refresh selected sources, add `--agents mem0 letta-code voyager` (use the slugs listed by `Get-ChildItem adapters`).

## Daily updates

GitHub Actions runs `.github/workflows/collect.yml` every day at 01:00 UTC (09:00 Asia/Shanghai) and also supports a manual run. It tests the collector, records a run summary, validates prompt hashes, and commits only changed source records, mechanism notes, or indexes. GitHub Actions must be enabled for the repository; the workflow uses `GITHUB_TOKEN` with repository content-write permission.

To synchronize a remote update locally:

```powershell
git pull --ff-only
```

If a run fails, check the Actions run summary for the affected source, tag filter, license decision, API error, or source-path drift. A successful follow-up clears the persisted error record.

## Add an agent

1. Verify its canonical upstream repository, package scope, license, latest stable release tag, and prompt source paths.
2. Add `adapters/<slug>.yaml`. Use narrow source globs and one of `raw`, `python`, `js-strings`, `js-templates`, `rust-strings`, `yaml`, or `json`; use `key_pattern` and `min_chars` to select intended string fields.
3. Add `docs/mechanisms/<slug>.md` with commit-pinned source links and coverage limitations.
4. Run the collector for the new slug and inspect source paths, prompt variants, metadata, and generated license notices before publishing.
