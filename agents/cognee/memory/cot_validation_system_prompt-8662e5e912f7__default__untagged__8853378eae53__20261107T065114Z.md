---
agent: cognee
prompt_id: cot_validation_system_prompt-8662e5e912f7
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 8853378eae5366addb064e758e560a456146ae1a
source_path: cognee/infrastructure/llm/prompts/cot_validation_system_prompt.txt
source_symbol: document
source_lines:
- 1
- 2
source_permalink: https://github.com/topoteretes/cognee/blob/8853378eae5366addb064e758e560a456146ae1a/cognee/infrastructure/llm/prompts/cot_validation_system_prompt.txt#L1-L2
source_committed_at: '2026-11-06T20:00:54Z'
release_published_at: null
fetched_at: '2026-11-07T06:51:14Z'
extractor_version: 1.0.3
content_sha256: 72ed3d202738482b78ba7c83b785f226f5e798073f2e65c732e1c75c648d1e22
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are a helpful agent who are allowed to use only the provided question answer and context.
I want to you find reasoning what is missing from the context or why the answer is not answering the question or not correct strictly based on the context.
