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
source_commit: 4053f6cc5536757f26a3665eed95c50088e6dc0b
source_path: cognee/infrastructure/llm/prompts/cot_validation_user_prompt.txt
source_symbol: document
source_lines:
- 1
- 11
source_permalink: https://github.com/topoteretes/cognee/blob/4053f6cc5536757f26a3665eed95c50088e6dc0b/cognee/infrastructure/llm/prompts/cot_validation_user_prompt.txt#L1-L11
source_committed_at: '2026-11-13T00:23:56Z'
release_published_at: null
fetched_at: '2026-11-13T07:38:22Z'
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
