---
agent: cognee
prompt_id: cot_followup_user_prompt-f2696c1c05ff
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.6
package_name: null
package_version: null
source_ref: v1.6.6
source_commit: df2b4facd7c1d73b59376fd251fb93674a9d60a3
source_path: cognee/infrastructure/llm/prompts/cot_followup_user_prompt.txt
source_symbol: document
source_lines:
- 1
- 14
source_permalink: https://github.com/topoteretes/cognee/blob/df2b4facd7c1d73b59376fd251fb93674a9d60a3/cognee/infrastructure/llm/prompts/cot_followup_user_prompt.txt#L1-L14
source_committed_at: '2026-10-29T21:29:40Z'
release_published_at: '2026-10-29T21:33:43Z'
fetched_at: '2026-10-30T05:29:25Z'
extractor_version: 1.0.3
content_sha256: b0603b582a91e8ac8ee7d1eeb1522f64cad22406ff7ea50ec2134b6438072aaf
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Based on the following, ask exactly one question that would directly resolve the gap identified in the validation reasoning and allow a valid answer.
Think in a way that with the followup question you are exploring a knowledge graph which contains entities, entity types and document chunks

<QUERY>
`{{ query}}`
</QUERY>

<ANSWER>
`{{ answer }}`
</ANSWER>

<REASONING>
`{{ reasoning }}`
</REASONING>
