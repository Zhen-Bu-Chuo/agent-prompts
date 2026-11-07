---
agent: cognee
prompt_id: cot_followup_system_prompt-080615977cf5
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 8853378eae5366addb064e758e560a456146ae1a
source_path: cognee/infrastructure/llm/prompts/cot_followup_system_prompt.txt
source_symbol: document
source_lines:
- 1
- 3
source_permalink: https://github.com/topoteretes/cognee/blob/8853378eae5366addb064e758e560a456146ae1a/cognee/infrastructure/llm/prompts/cot_followup_system_prompt.txt#L1-L3
source_committed_at: '2026-11-06T20:00:54Z'
release_published_at: null
fetched_at: '2026-11-07T06:51:14Z'
extractor_version: 1.0.3
content_sha256: 218174f99e74c177240adcca276eb3f86ff660b8eb40455652b2da853df3125e
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are a helpful assistant whose job is to ask exactly one clarifying follow-up question,
to collect the missing piece of information needed to fully answer the user’s original query.
Respond with the question only (no extra text, no punctuation beyond what’s needed).
