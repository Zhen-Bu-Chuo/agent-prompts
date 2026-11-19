---
agent: cognee
prompt_id: hybrid_context_for_question-3743ac86e88f
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: c8a094375821f2d8c7c4945d3b2202e2e5d6603e
source_path: cognee/infrastructure/llm/prompts/hybrid_context_for_question.txt
source_symbol: document
source_lines:
- 1
- 5
source_permalink: https://github.com/topoteretes/cognee/blob/c8a094375821f2d8c7c4945d3b2202e2e5d6603e/cognee/infrastructure/llm/prompts/hybrid_context_for_question.txt#L1-L5
source_committed_at: '2026-11-18T21:40:46Z'
release_published_at: null
fetched_at: '2026-11-19T08:26:16Z'
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
