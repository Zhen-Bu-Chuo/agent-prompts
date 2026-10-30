---
agent: hindsight
prompt_id: prompts-7ac8fd048734
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.1.0
package_name: null
package_version: null
source_ref: v1.1.0
source_commit: a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.11
source_lines:
- 310
- 310
source_permalink: https://github.com/vectorize-io/hindsight/blob/a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L310-L310
source_committed_at: '2026-10-21T16:16:23Z'
release_published_at: '2026-10-21T16:41:42Z'
fetched_at: '2026-10-30T05:29:47Z'
extractor_version: 1.0.3
content_sha256: f00ec3a08f4725a7b41d3695f8a5e7c71d52ca809810cf567f788fb24469b74b
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
An honest 'the data is inconsistent about X' beats a confident wrong answer. Do NOT pick a value arbitrarily, average conflicting values, or smooth over gaps in confident prose. Acknowledging ambiguity is a successful answer, not a failure mode.