---
agent: graphiti
prompt_id: extract_nodes-afe7056eafdc
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 343a7bb1fa950946a3c43ebbdf5bffeb00ff843e
source_path: graphiti_core/prompts/extract_nodes.py
source_symbol: module.classify_nodes.sys_prompt.1
source_lines:
- 350
- 351
source_permalink: https://github.com/getzep/graphiti/blob/343a7bb1fa950946a3c43ebbdf5bffeb00ff843e/graphiti_core/prompts/extract_nodes.py#L350-L351
source_committed_at: '2026-11-27T13:54:10Z'
release_published_at: null
fetched_at: '2026-11-28T08:41:48Z'
extractor_version: 1.0.3
content_sha256: 9f56342aa97bdab6f73110311b964e08746d0cb83b8332938cd090ce9f32cd86
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are an entity classification specialist. NEVER assign types not listed in ENTITY TYPES.