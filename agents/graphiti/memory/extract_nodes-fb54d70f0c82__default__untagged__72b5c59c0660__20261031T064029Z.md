---
agent: graphiti
prompt_id: extract_nodes-fb54d70f0c82
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 72b5c59c06607e09ea855be61b6ff5a3446fc951
source_path: graphiti_core/prompts/extract_nodes.py
source_symbol: module.extract_message.sys_prompt.1
source_lines:
- 86
- 87
source_permalink: https://github.com/getzep/graphiti/blob/72b5c59c06607e09ea855be61b6ff5a3446fc951/graphiti_core/prompts/extract_nodes.py#L86-L87
source_committed_at: '2026-10-28T23:22:49Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:29Z'
extractor_version: 1.0.3
content_sha256: 9fca5886992309bcd80ebb907254ef6c630af03581254fdeecc825c0bbe0a657
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are an entity extraction specialist for conversational messages. NEVER extract abstract concepts, feelings, or generic words.