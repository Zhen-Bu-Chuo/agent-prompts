---
agent: graphiti
prompt_id: extract_nodes-99b651c1124c
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: v0.31.2
package_name: null
package_version: null
source_ref: v0.31.2
source_commit: d72407dcedac911e1be9fc15b55e8c05a3efcc36
source_path: graphiti_core/prompts/extract_nodes.py
source_symbol: module.extract_json.user_prompt.1
source_lines:
- 220
- 272
source_permalink: https://github.com/getzep/graphiti/blob/d72407dcedac911e1be9fc15b55e8c05a3efcc36/graphiti_core/prompts/extract_nodes.py#L220-L272
source_committed_at: '2026-10-20T17:23:18Z'
release_published_at: '2026-10-20T17:25:21Z'
fetched_at: '2026-10-30T05:29:43Z'
extractor_version: 1.0.3
content_sha256: 94523e762c83fbae28b20b7f52c5ee9cd5dbc9e20091f2efde428e5bbb64dedc
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---

NEVER extract:
- Date, time, or timestamp values
- Abstract concepts or generic field values (e.g., "true", "active", "pending")
- Numeric IDs or codes that are not meaningful entity names
- Bare relational or kinship terms (e.g., "spouse", "parent", "pet") — only extract if qualified
  with a possessor name
- Bare generic objects or common nouns (e.g., "supplies", "tickets", "gear") — only extract if
  qualified with a distinguishing detail
- Generic media/content nouns unless uniquely identified in the value itself (photo, pic, picture,
  image, video, post, story)
- Generic event/activity nouns unless uniquely identified in the value itself (event, game, meeting,
  class, workshop, competition)
- Broad institutional nouns unless explicitly named or uniquely qualified (government, school, company,
  team, office)
- Ambiguous bare nouns whose meaning depends on surrounding text rather than the extracted value itself

Extract entities from the JSON and classify each using the ENTITY TYPES above.

<ENTITY TYPES>
{context['entity_types']}
</ENTITY TYPES>

<SOURCE DESCRIPTION>
{context['source_description']}
</SOURCE DESCRIPTION>

<JSON>
{context['episode_content']}
</JSON>

Guidelines:
1. Extract the primary entity the JSON represents (e.g., a "name" or "user" field).
2. Extract named entities referenced in other properties throughout the JSON structure.
3. Only extract entities specific enough to be uniquely identifiable.
4. Be explicit in naming entities — use full names when available.
5. Use the most specific form present in the data (e.g., "road cycling" not "cycling").
6. If a value would not be meaningful and distinguishable when read alone later, do NOT extract it.

{context['custom_extraction_instructions']}

<EXAMPLE>
JSON: {{"user": "Jordan Lee", "company": "Acme Corp", "role": "engineer", "start_date": "2024-01-15", "location": "Denver", "active": true}}
Good extractions: "Jordan Lee" (Person), "Acme Corp" (Organization), "Denver" (Location)
Do NOT extract: "engineer" (role, not an entity), "2024-01-15" (date), "true" (field value)
</EXAMPLE>

<EXAMPLE>
JSON: {{"author": "Alex", "attachment_type": "photo", "event_name": "event", "agency": "government"}}
Good extractions: "Alex" (Person)
Do NOT extract: "photo" (generic media noun), "event" (generic event noun), "government" (broad institutional noun)
</EXAMPLE>
