---
agent: graphiti
prompt_id: extract_nodes_and_edges-656b5ebd36a0
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 45fdf546c74da5586e8242fd6588a0801e641e16
source_path: graphiti_core/prompts/extract_nodes_and_edges.py
source_symbol: module._build_extract_user_prompt.1
source_lines:
- 156
- 170
source_permalink: https://github.com/getzep/graphiti/blob/45fdf546c74da5586e8242fd6588a0801e641e16/graphiti_core/prompts/extract_nodes_and_edges.py#L156-L170
source_committed_at: '2026-11-23T03:22:04Z'
release_published_at: null
fetched_at: '2026-11-23T08:37:24Z'
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
