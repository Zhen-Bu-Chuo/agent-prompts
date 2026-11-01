---
agent: graphiti
prompt_id: eval-cd331fec6964
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 16bf514380de4e44884aed6779bece220e6fe470
source_path: graphiti_core/prompts/eval.py
source_symbol: module.eval_prompt.user_prompt.1
source_lines:
- 108
- 121
source_permalink: https://github.com/getzep/graphiti/blob/16bf514380de4e44884aed6779bece220e6fe470/graphiti_core/prompts/eval.py#L108-L121
source_committed_at: '2026-11-01T01:04:59Z'
release_published_at: null
fetched_at: '2026-11-01T07:10:11Z'
extractor_version: 1.0.3
content_sha256: 0f05cf21fa486653462a0c553ae253319ed4f133b4cd2572fdf5d0551caee088
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---

    Given the QUESTION and the gold standard ANSWER determine if the RESPONSE to the question is correct or incorrect.
    Although the RESPONSE may be more verbose, mark it as correct as long as it references the same topic 
    as the gold standard ANSWER. Also include your reasoning for the grade.
    <QUESTION>
    {context['query']}
    </QUESTION>
    <ANSWER>
    {context['answer']}
    </ANSWER>
    <RESPONSE>
    {context['response']}
    </RESPONSE>
    