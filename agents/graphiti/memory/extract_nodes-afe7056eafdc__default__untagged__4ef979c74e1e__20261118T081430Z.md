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
source_commit: 4ef979c74e1e68d08217cf0af4022ddbc89c257f
source_path: graphiti_core/prompts/extract_nodes.py
source_symbol: module.classify_nodes.sys_prompt.1
source_lines:
- 350
- 351
source_permalink: https://github.com/getzep/graphiti/blob/4ef979c74e1e68d08217cf0af4022ddbc89c257f/graphiti_core/prompts/extract_nodes.py#L350-L351
source_committed_at: '2026-11-17T18:27:23Z'
release_published_at: null
fetched_at: '2026-11-18T08:14:30Z'
extractor_version: 1.0.3
content_sha256: 9f56342aa97bdab6f73110311b964e08746d0cb83b8332938cd090ce9f32cd86
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are an entity classification specialist. NEVER assign types not listed in ENTITY TYPES.