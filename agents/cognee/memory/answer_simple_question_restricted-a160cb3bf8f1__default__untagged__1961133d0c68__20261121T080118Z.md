---
agent: cognee
prompt_id: answer_simple_question_restricted-a160cb3bf8f1
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 1961133d0c68b450fe8e71941a756371e94f7c04
source_path: cognee/infrastructure/llm/prompts/answer_simple_question_restricted.txt
source_symbol: document
source_lines:
- 1
- 1
source_permalink: https://github.com/topoteretes/cognee/blob/1961133d0c68b450fe8e71941a756371e94f7c04/cognee/infrastructure/llm/prompts/answer_simple_question_restricted.txt#L1-L1
source_committed_at: '2026-11-20T09:41:35Z'
release_published_at: null
fetched_at: '2026-11-21T08:01:18Z'
extractor_version: 1.0.3
content_sha256: 67b0eb3b24add37ebfddb60030d87743f7d78c7522d38aa2b8d4bb47c106f61e
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Answer the question using the provided context. If the provided context is not connected to the question, just answer "The provided knowledge base does not contain the answer to the question". Be as brief as possible.
