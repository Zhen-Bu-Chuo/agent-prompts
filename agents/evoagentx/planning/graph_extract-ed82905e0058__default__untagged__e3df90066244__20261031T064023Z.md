---
agent: evoagentx
prompt_id: graph_extract-ed82905e0058
module: planning
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: e3df900662443e94dd92141be5633b040a69a70a
source_path: evoagentx/prompts/rag/graph_extract.py
source_symbol: module.RELATION_EXTRACT_PROMPT.1
source_lines:
- 35
- 51
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/e3df900662443e94dd92141be5633b040a69a70a/evoagentx/prompts/rag/graph_extract.py#L35-L51
source_committed_at: '2026-10-31T01:49:52Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:23Z'
extractor_version: 1.0.3
content_sha256: da5a4107089030441d7e319a2db7bb5b7099b3e808113888a61ce879abb3868b
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

Given the following text and a list of extracted entities, identify explicit, directed relationships between pairs of entities. A relationship should describe a clear, meaningful connection (e.g., "works_for", "located_in", "founded"). Return the results in JSON format as a list of triplets, each with 'source', 'target', and 'relation' fields. The 'source' and 'target' must match entity names from the provided list. 
Ensure relationships are specific and grounded in the text.

***DO NOT*** answer the question itself if the given text is a question.

Text:
{text}

Entities:
{entities_json}

Output JSON:
```json
{"graph": [{"source": "entity1", "target": "entity2", "relation": "relationship_label"}, ...]}
```
