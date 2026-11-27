---
agent: cognee
prompt_id: cot_validation_system_prompt-8662e5e912f7
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.11
package_name: null
package_version: null
source_ref: v1.6.11
source_commit: c78a56ff4a705a6f46090a1fe6a3a9737f45e17b
source_path: cognee/infrastructure/llm/prompts/cot_validation_system_prompt.txt
source_symbol: document
source_lines:
- 1
- 2
source_permalink: https://github.com/topoteretes/cognee/blob/c78a56ff4a705a6f46090a1fe6a3a9737f45e17b/cognee/infrastructure/llm/prompts/cot_validation_system_prompt.txt#L1-L2
source_committed_at: '2026-11-26T16:54:44Z'
release_published_at: '2026-11-26T17:05:51Z'
fetched_at: '2026-11-27T09:27:38Z'
extractor_version: 1.0.3
content_sha256: 72ed3d202738482b78ba7c83b785f226f5e798073f2e65c732e1c75c648d1e22
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are a helpful agent who are allowed to use only the provided question answer and context.
I want to you find reasoning what is missing from the context or why the answer is not answering the question or not correct strictly based on the context.
