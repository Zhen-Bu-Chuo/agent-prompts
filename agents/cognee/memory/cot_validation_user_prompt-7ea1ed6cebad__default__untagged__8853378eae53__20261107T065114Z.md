---
agent: cognee
prompt_id: cot_validation_user_prompt-7ea1ed6cebad
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 8853378eae5366addb064e758e560a456146ae1a
source_path: cognee/infrastructure/llm/prompts/cot_validation_user_prompt.txt
source_symbol: document
source_lines:
- 1
- 11
source_permalink: https://github.com/topoteretes/cognee/blob/8853378eae5366addb064e758e560a456146ae1a/cognee/infrastructure/llm/prompts/cot_validation_user_prompt.txt#L1-L11
source_committed_at: '2026-11-06T20:00:54Z'
release_published_at: null
fetched_at: '2026-11-07T06:51:14Z'
extractor_version: 1.0.3
content_sha256: d690f8661816b19e09fd909f73faaf1126148a68ed7b6f7282febbafc30661b9
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
<QUESTION>
`{{ query}}`
</QUESTION>

<ANSWER>
`{{ answer }}`
</ANSWER>

<CONTEXT>
`{{ context }}`
</CONTEXT>
