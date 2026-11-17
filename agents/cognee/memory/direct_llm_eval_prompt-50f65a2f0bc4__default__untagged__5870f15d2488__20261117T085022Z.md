---
agent: cognee
prompt_id: direct_llm_eval_prompt-50f65a2f0bc4
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 5870f15d2488b99e80f71dd6e8e146b228749356
source_path: cognee/infrastructure/llm/prompts/direct_llm_eval_prompt.txt
source_symbol: document
source_lines:
- 1
- 3
source_permalink: https://github.com/topoteretes/cognee/blob/5870f15d2488b99e80f71dd6e8e146b228749356/cognee/infrastructure/llm/prompts/direct_llm_eval_prompt.txt#L1-L3
source_committed_at: '2026-11-16T08:47:14Z'
release_published_at: null
fetched_at: '2026-11-17T08:50:22Z'
extractor_version: 1.0.3
content_sha256: aa499d6882e21e58fd896a44db7f404adccca3532673fbc973d3e49c6ce4a15b
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Question: {{question}}
Provided Answer: {{answer}}
Golden Answer: {{golden_answer}}
