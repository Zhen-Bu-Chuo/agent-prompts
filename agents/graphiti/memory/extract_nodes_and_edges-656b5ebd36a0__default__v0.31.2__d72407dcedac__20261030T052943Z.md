---
agent: graphiti
prompt_id: extract_nodes_and_edges-656b5ebd36a0
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: v0.31.2
package_name: null
package_version: null
source_ref: v0.31.2
source_commit: d72407dcedac911e1be9fc15b55e8c05a3efcc36
source_path: graphiti_core/prompts/extract_nodes_and_edges.py
source_symbol: module._build_extract_user_prompt.1
source_lines:
- 156
- 170
source_permalink: https://github.com/getzep/graphiti/blob/d72407dcedac911e1be9fc15b55e8c05a3efcc36/graphiti_core/prompts/extract_nodes_and_edges.py#L156-L170
source_committed_at: '2026-10-20T17:23:18Z'
release_published_at: '2026-10-20T17:25:21Z'
fetched_at: '2026-10-30T05:29:43Z'
extractor_version: 1.0.3
content_sha256: de711e0bc36a766d0980922fe9c2de46fc7529e65ce4a439d8d1afc307a4c5ec
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
{_C2_INSTRUCTION_TEXT}

<ENTITY TYPES>
{context['entity_types']}
</ENTITY TYPES>
{_build_edge_types_section(context.get('edge_types'), context.get('strict_edge_types', False))}
{_build_custom_instructions_section(context.get('custom_extraction_instructions'))}
<PREVIOUS MESSAGES>
{to_prompt_json([ep for ep in context['previous_episodes']])}
</PREVIOUS MESSAGES>

<CURRENT MESSAGES>
{context['episode_content']}
</CURRENT MESSAGES>
