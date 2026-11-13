---
agent: cognee
prompt_id: hybrid_context_for_question-3743ac86e88f
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.8
package_name: null
package_version: null
source_ref: v1.6.8
source_commit: 069f3cc119bdf5628be054bb915992b2fc78cfc5
source_path: cognee/infrastructure/llm/prompts/hybrid_context_for_question.txt
source_symbol: document
source_lines:
- 1
- 5
source_permalink: https://github.com/topoteretes/cognee/blob/069f3cc119bdf5628be054bb915992b2fc78cfc5/cognee/infrastructure/llm/prompts/hybrid_context_for_question.txt#L1-L5
source_committed_at: '2026-11-12T22:26:02Z'
release_published_at: '2026-11-12T22:31:22Z'
fetched_at: '2026-11-13T07:38:22Z'
extractor_version: 1.0.3
content_sha256: d31a6948d3390f208d6fa7488f7be487de4b61b5f9cca3e7652183b5e7ff4241
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
The question is: `{{ question }}`
Answer using this sectioned context. Keep the answer brief and do not use information outside the context.

Context:
`{{ context }}`
