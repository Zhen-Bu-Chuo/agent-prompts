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
source_commit: 343a7bb1fa950946a3c43ebbdf5bffeb00ff843e
source_path: graphiti_core/prompts/extract_nodes.py
source_symbol: module.extract_json.sys_prompt.1
source_lines:
- 216
- 217
source_permalink: https://github.com/getzep/graphiti/blob/343a7bb1fa950946a3c43ebbdf5bffeb00ff843e/graphiti_core/prompts/extract_nodes.py#L216-L217
source_committed_at: '2026-11-27T13:54:10Z'
release_published_at: null
fetched_at: '2026-11-28T08:41:48Z'
extractor_version: 1.0.3
content_sha256: a7b4765e61d25b2c32ec503fb7f25212f90aec0e31e56d6e52addc60f37cceda
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are an entity extraction specialist for JSON data. NEVER extract abstract concepts, dates, or generic field values.