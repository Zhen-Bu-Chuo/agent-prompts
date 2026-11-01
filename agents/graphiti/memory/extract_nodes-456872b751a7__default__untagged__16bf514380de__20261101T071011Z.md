---
agent: graphiti
prompt_id: extract_nodes-456872b751a7
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 16bf514380de4e44884aed6779bece220e6fe470
source_path: graphiti_core/prompts/extract_nodes.py
source_symbol: module.extract_json.sys_prompt.1
source_lines:
- 216
- 217
source_permalink: https://github.com/getzep/graphiti/blob/16bf514380de4e44884aed6779bece220e6fe470/graphiti_core/prompts/extract_nodes.py#L216-L217
source_committed_at: '2026-11-01T01:04:59Z'
release_published_at: null
fetched_at: '2026-11-01T07:10:11Z'
extractor_version: 1.0.3
content_sha256: a7b4765e61d25b2c32ec503fb7f25212f90aec0e31e56d6e52addc60f37cceda
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are an entity extraction specialist for JSON data. NEVER extract abstract concepts, dates, or generic field values.