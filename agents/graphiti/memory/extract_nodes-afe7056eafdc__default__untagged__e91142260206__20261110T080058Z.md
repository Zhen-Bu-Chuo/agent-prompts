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
source_commit: e911422602068a0dc28e72a1961698269e9aefb2
source_path: graphiti_core/prompts/extract_nodes.py
source_symbol: module.classify_nodes.sys_prompt.1
source_lines:
- 350
- 351
source_permalink: https://github.com/getzep/graphiti/blob/e911422602068a0dc28e72a1961698269e9aefb2/graphiti_core/prompts/extract_nodes.py#L350-L351
source_committed_at: '2026-11-09T09:35:22Z'
release_published_at: null
fetched_at: '2026-11-10T08:00:58Z'
extractor_version: 1.0.3
content_sha256: 9f56342aa97bdab6f73110311b964e08746d0cb83b8332938cd090ce9f32cd86
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are an entity classification specialist. NEVER assign types not listed in ENTITY TYPES.