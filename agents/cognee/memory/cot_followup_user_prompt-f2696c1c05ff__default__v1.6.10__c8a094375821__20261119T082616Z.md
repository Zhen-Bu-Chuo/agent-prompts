---
agent: cognee
prompt_id: cot_followup_user_prompt-f2696c1c05ff
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.10
package_name: null
package_version: null
source_ref: v1.6.10
source_commit: c8a094375821f2d8c7c4945d3b2202e2e5d6603e
source_path: cognee/infrastructure/llm/prompts/cot_followup_user_prompt.txt
source_symbol: document
source_lines:
- 1
- 14
source_permalink: https://github.com/topoteretes/cognee/blob/c8a094375821f2d8c7c4945d3b2202e2e5d6603e/cognee/infrastructure/llm/prompts/cot_followup_user_prompt.txt#L1-L14
source_committed_at: '2026-11-18T21:40:46Z'
release_published_at: '2026-11-18T21:42:57Z'
fetched_at: '2026-11-19T08:26:16Z'
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
