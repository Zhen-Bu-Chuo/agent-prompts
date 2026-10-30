---
agent: graphiti
prompt_id: eval-cdb2a85f9e14
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: v0.31.2
package_name: null
package_version: null
source_ref: v0.31.2
source_commit: d72407dcedac911e1be9fc15b55e8c05a3efcc36
source_path: graphiti_core/prompts/eval.py
source_symbol: module.qa_prompt.user_prompt.1
source_lines:
- 84
- 96
source_permalink: https://github.com/getzep/graphiti/blob/d72407dcedac911e1be9fc15b55e8c05a3efcc36/graphiti_core/prompts/eval.py#L84-L96
source_committed_at: '2026-10-20T17:23:18Z'
release_published_at: '2026-10-20T17:25:21Z'
fetched_at: '2026-10-30T05:29:43Z'
extractor_version: 1.0.3
content_sha256: abf5668f119285b343b16d865e05d3f86c09fefa90da68874765468e068ab0f3
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---

    Your task is to briefly answer the question in the way that you think Alice would answer the question.
    You are given the following entity summaries and facts to help you determine the answer to your question.
    <ENTITY_SUMMARIES>
    {to_prompt_json(context['entity_summaries'])}
    </ENTITY_SUMMARIES>
    <FACTS>
    {to_prompt_json(context['facts'])}
    </FACTS>
    <QUESTION>
    {context['query']}
    </QUESTION>
    