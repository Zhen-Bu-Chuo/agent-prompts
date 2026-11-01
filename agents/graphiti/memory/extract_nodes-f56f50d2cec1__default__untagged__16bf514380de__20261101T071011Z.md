---
agent: graphiti
prompt_id: extract_nodes-f56f50d2cec1
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 16bf514380de4e44884aed6779bece220e6fe470
source_path: graphiti_core/prompts/extract_nodes.py
source_symbol: module.classify_nodes.user_prompt.1
source_lines:
- 354
- 377
source_permalink: https://github.com/getzep/graphiti/blob/16bf514380de4e44884aed6779bece220e6fe470/graphiti_core/prompts/extract_nodes.py#L354-L377
source_committed_at: '2026-11-01T01:04:59Z'
release_published_at: null
fetched_at: '2026-11-01T07:10:11Z'
extractor_version: 1.0.3
content_sha256: a87ed86d5e6746c6782eaa4e9d30d584543220be1a7a875692b44be07d05d960
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---

<PREVIOUS MESSAGES>
{to_prompt_json([ep for ep in context['previous_episodes']])}
</PREVIOUS MESSAGES>

<CURRENT MESSAGE>
{context['episode_content']}
</CURRENT MESSAGE>

<EXTRACTED ENTITIES>
{context['extracted_entities']}
</EXTRACTED ENTITIES>

<ENTITY TYPES>
{context['entity_types']}
</ENTITY TYPES>

Given the above conversation, extracted entities, and provided entity types and their descriptions, classify the extracted entities.

Guidelines:
1. Each entity must have exactly one type.
2. NEVER use types not listed in ENTITY TYPES.
3. If none of the provided entity types accurately classify an extracted entity, the type should be set to None.
