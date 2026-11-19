---
agent: cognee
prompt_id: cot_validation_system_prompt-8662e5e912f7
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.10
package_name: null
package_version: null
source_ref: v1.6.10
source_commit: c8a094375821f2d8c7c4945d3b2202e2e5d6603e
source_path: cognee/infrastructure/llm/prompts/cot_validation_system_prompt.txt
source_symbol: document
source_lines:
- 1
- 2
source_permalink: https://github.com/topoteretes/cognee/blob/c8a094375821f2d8c7c4945d3b2202e2e5d6603e/cognee/infrastructure/llm/prompts/cot_validation_system_prompt.txt#L1-L2
source_committed_at: '2026-11-18T21:40:46Z'
release_published_at: '2026-11-18T21:42:57Z'
fetched_at: '2026-11-19T08:26:16Z'
extractor_version: 1.0.3
content_sha256: 72ed3d202738482b78ba7c83b785f226f5e798073f2e65c732e1c75c648d1e22
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are a helpful agent who are allowed to use only the provided question answer and context.
I want to you find reasoning what is missing from the context or why the answer is not answering the question or not correct strictly based on the context.
