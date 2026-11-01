---
agent: graphiti
prompt_id: eval-cdb2a85f9e14
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 16bf514380de4e44884aed6779bece220e6fe470
source_path: graphiti_core/prompts/eval.py
source_symbol: module.qa_prompt.user_prompt.1
source_lines:
- 84
- 96
source_permalink: https://github.com/getzep/graphiti/blob/16bf514380de4e44884aed6779bece220e6fe470/graphiti_core/prompts/eval.py#L84-L96
source_committed_at: '2026-11-01T01:04:59Z'
release_published_at: null
fetched_at: '2026-11-01T07:10:11Z'
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
    