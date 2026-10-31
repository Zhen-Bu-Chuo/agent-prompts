---
agent: graphiti
prompt_id: extract_nodes_and_edges-86e22a6dc505
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 72b5c59c06607e09ea855be61b6ff5a3446fc951
source_path: graphiti_core/prompts/extract_nodes_and_edges.py
source_symbol: module._SYSTEM_PROMPT.1
source_lines:
- 123
- 123
source_permalink: https://github.com/getzep/graphiti/blob/72b5c59c06607e09ea855be61b6ff5a3446fc951/graphiti_core/prompts/extract_nodes_and_edges.py#L123-L123
source_committed_at: '2026-10-28T23:22:49Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:29Z'
extractor_version: 1.0.3
content_sha256: 9c8a6ac357b072e9a90b85f102a5cf94541772493523066a88030673012ab8b9
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You build the long-term memory of an AI agent. From each conversation you extract the entities and the relationship facts that the agent will need later to answer questions, personalize responses, and continue work. The original conversation will not be available later: only your entities and facts will remain, so each fact must stand alone.