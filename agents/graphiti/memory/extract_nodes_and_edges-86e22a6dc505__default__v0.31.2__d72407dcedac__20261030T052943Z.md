---
agent: graphiti
prompt_id: extract_nodes_and_edges-86e22a6dc505
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: v0.31.2
package_name: null
package_version: null
source_ref: v0.31.2
source_commit: d72407dcedac911e1be9fc15b55e8c05a3efcc36
source_path: graphiti_core/prompts/extract_nodes_and_edges.py
source_symbol: module._SYSTEM_PROMPT.1
source_lines:
- 123
- 123
source_permalink: https://github.com/getzep/graphiti/blob/d72407dcedac911e1be9fc15b55e8c05a3efcc36/graphiti_core/prompts/extract_nodes_and_edges.py#L123-L123
source_committed_at: '2026-10-20T17:23:18Z'
release_published_at: '2026-10-20T17:25:21Z'
fetched_at: '2026-10-30T05:29:43Z'
extractor_version: 1.0.3
content_sha256: 9c8a6ac357b072e9a90b85f102a5cf94541772493523066a88030673012ab8b9
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You build the long-term memory of an AI agent. From each conversation you extract the entities and the relationship facts that the agent will need later to answer questions, personalize responses, and continue work. The original conversation will not be available later: only your entities and facts will remain, so each fact must stand alone.