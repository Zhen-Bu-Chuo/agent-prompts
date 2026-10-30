---
agent: evoagentx
prompt_id: graph_extract-84d03cd3fc7d
module: planning
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: v0.1.4
package_name: null
package_version: null
source_ref: v0.1.4
source_commit: aad19b912f640161ea07e8904d9237cd34fde5f1
source_path: evoagentx/prompts/rag/graph_extract.py
source_symbol: module.ENTITY_EXTRACT_PROMPT.1
source_lines:
- 1
- 33
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/rag/graph_extract.py#L1-L33
source_committed_at: '2026-06-28T10:20:05Z'
release_published_at: '2026-06-28T10:24:06Z'
fetched_at: '2026-10-30T05:29:30Z'
extractor_version: 1.0.3
content_sha256: e1587330b03af1743e7c1d401a666104491bb1439224b6d61c02caa2ef727b5e
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

Extract entities and their types from the following text. An entity is a specific, named object, such as a person, organization, location, or concept. The type should be a concise category (e.g., Person, Organization, Location, Concept). 
Return the results in JSON format as a list of objects, each with 'name' and 'type' fields.
Ensure the entities are distinct and relevant to the text's main topics.

***DO NOT*** answer the question itself if the given text is a question.

Text:
{text}

----------------
EXAMPLE:
Text: Tim Cook, CEO of Apple Inc., announced the new Apple Watch that monitors heart health. 
"UC Berkeley researchers studied the benefits of apples.
"

Output:
```json
{"entities":[
    {'name': 'Tim Cook', 'type': 'PERSON',},
    {'name': 'Apple Inc.', 'type': 'COMPANY'},
    {'name': 'Apple Watch', 'type': 'PRODUCT'},
    {'name': 'heart health', 'type': 'HEALTH_METRIC'},
    {'name': 'UC Berkeley', 'type': 'UNIVERSITY'},
    {'name': 'benefits of apples', 'type': 'RESEARCH_TOPIC'}]
}
```
----------------

Output JSON:
```json
{"entities": [{"name": "entity_name", "type": "entity_type"}, ...]}
```
