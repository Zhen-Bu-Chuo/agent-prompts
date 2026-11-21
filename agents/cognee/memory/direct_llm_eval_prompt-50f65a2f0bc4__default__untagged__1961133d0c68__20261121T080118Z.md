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
source_commit: 1961133d0c68b450fe8e71941a756371e94f7c04
source_path: cognee/infrastructure/llm/prompts/direct_llm_eval_prompt.txt
source_symbol: document
source_lines:
- 1
- 3
source_permalink: https://github.com/topoteretes/cognee/blob/1961133d0c68b450fe8e71941a756371e94f7c04/cognee/infrastructure/llm/prompts/direct_llm_eval_prompt.txt#L1-L3
source_committed_at: '2026-11-20T09:41:35Z'
release_published_at: null
fetched_at: '2026-11-21T08:01:18Z'
extractor_version: 1.0.3
content_sha256: aa499d6882e21e58fd896a44db7f404adccca3532673fbc973d3e49c6ce4a15b
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Question: {{question}}
Provided Answer: {{answer}}
Golden Answer: {{golden_answer}}
