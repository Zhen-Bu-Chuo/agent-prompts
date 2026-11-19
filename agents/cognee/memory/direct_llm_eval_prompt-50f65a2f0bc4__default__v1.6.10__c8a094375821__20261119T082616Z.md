---
agent: cognee
prompt_id: direct_llm_eval_prompt-50f65a2f0bc4
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.10
package_name: null
package_version: null
source_ref: v1.6.10
source_commit: c8a094375821f2d8c7c4945d3b2202e2e5d6603e
source_path: cognee/infrastructure/llm/prompts/direct_llm_eval_prompt.txt
source_symbol: document
source_lines:
- 1
- 3
source_permalink: https://github.com/topoteretes/cognee/blob/c8a094375821f2d8c7c4945d3b2202e2e5d6603e/cognee/infrastructure/llm/prompts/direct_llm_eval_prompt.txt#L1-L3
source_committed_at: '2026-11-18T21:40:46Z'
release_published_at: '2026-11-18T21:42:57Z'
fetched_at: '2026-11-19T08:26:16Z'
extractor_version: 1.0.3
content_sha256: aa499d6882e21e58fd896a44db7f404adccca3532673fbc973d3e49c6ce4a15b
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Question: {{question}}
Provided Answer: {{answer}}
Golden Answer: {{golden_answer}}
