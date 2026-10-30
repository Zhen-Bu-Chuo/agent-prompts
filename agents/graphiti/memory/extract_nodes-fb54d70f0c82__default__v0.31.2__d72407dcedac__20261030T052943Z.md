---
agent: graphiti
prompt_id: extract_nodes-fb54d70f0c82
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: v0.31.2
package_name: null
package_version: null
source_ref: v0.31.2
source_commit: d72407dcedac911e1be9fc15b55e8c05a3efcc36
source_path: graphiti_core/prompts/extract_nodes.py
source_symbol: module.extract_message.sys_prompt.1
source_lines:
- 86
- 87
source_permalink: https://github.com/getzep/graphiti/blob/d72407dcedac911e1be9fc15b55e8c05a3efcc36/graphiti_core/prompts/extract_nodes.py#L86-L87
source_committed_at: '2026-10-20T17:23:18Z'
release_published_at: '2026-10-20T17:25:21Z'
fetched_at: '2026-10-30T05:29:43Z'
extractor_version: 1.0.3
content_sha256: 9fca5886992309bcd80ebb907254ef6c630af03581254fdeecc825c0bbe0a657
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are an entity extraction specialist for conversational messages. NEVER extract abstract concepts, feelings, or generic words.