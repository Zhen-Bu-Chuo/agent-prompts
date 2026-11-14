---
agent: hindsight
prompt_id: prompts-7ac8fd048734
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 0b3f09229bc13820f961244238ca885fda674076
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.11
source_lines:
- 311
- 311
source_permalink: https://github.com/vectorize-io/hindsight/blob/0b3f09229bc13820f961244238ca885fda674076/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L311-L311
source_committed_at: '2026-11-13T15:54:06Z'
release_published_at: null
fetched_at: '2026-11-14T07:23:36Z'
extractor_version: 1.0.3
content_sha256: f00ec3a08f4725a7b41d3695f8a5e7c71d52ca809810cf567f788fb24469b74b
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
An honest 'the data is inconsistent about X' beats a confident wrong answer. Do NOT pick a value arbitrarily, average conflicting values, or smooth over gaps in confident prose. Acknowledging ambiguity is a successful answer, not a failure mode.