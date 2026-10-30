---
agent: cognee
prompt_id: answer_hotpot_question-922f91e9b0b6
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.6
package_name: null
package_version: null
source_ref: v1.6.6
source_commit: df2b4facd7c1d73b59376fd251fb93674a9d60a3
source_path: cognee/infrastructure/llm/prompts/answer_hotpot_question.txt
source_symbol: document
source_lines:
- 1
- 2
source_permalink: https://github.com/topoteretes/cognee/blob/df2b4facd7c1d73b59376fd251fb93674a9d60a3/cognee/infrastructure/llm/prompts/answer_hotpot_question.txt#L1-L2
source_committed_at: '2026-10-29T21:29:40Z'
release_published_at: '2026-10-29T21:33:43Z'
fetched_at: '2026-10-30T05:29:25Z'
extractor_version: 1.0.3
content_sha256: 25eec1a4aa96fa171e1ea07b682cb4c051e1740aae364b2790cc702f68696fc8
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Answer the question using the provided context. Be as brief as possible.
Each entry in the context is a paragraph, which is represented as a list with two elements [title, sentences] and sentences is a list of strings.
