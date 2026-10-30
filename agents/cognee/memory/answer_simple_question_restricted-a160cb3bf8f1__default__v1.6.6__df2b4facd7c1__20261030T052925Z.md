---
agent: cognee
prompt_id: answer_simple_question_restricted-a160cb3bf8f1
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.6
package_name: null
package_version: null
source_ref: v1.6.6
source_commit: df2b4facd7c1d73b59376fd251fb93674a9d60a3
source_path: cognee/infrastructure/llm/prompts/answer_simple_question_restricted.txt
source_symbol: document
source_lines:
- 1
- 1
source_permalink: https://github.com/topoteretes/cognee/blob/df2b4facd7c1d73b59376fd251fb93674a9d60a3/cognee/infrastructure/llm/prompts/answer_simple_question_restricted.txt#L1-L1
source_committed_at: '2026-10-29T21:29:40Z'
release_published_at: '2026-10-29T21:33:43Z'
fetched_at: '2026-10-30T05:29:25Z'
extractor_version: 1.0.3
content_sha256: 67b0eb3b24add37ebfddb60030d87743f7d78c7522d38aa2b8d4bb47c106f61e
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Answer the question using the provided context. If the provided context is not connected to the question, just answer "The provided knowledge base does not contain the answer to the question". Be as brief as possible.
