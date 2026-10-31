---
agent: cognee
prompt_id: direct_llm_eval_system-dd491ea74b77
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 525b1d1179c550cd5b5661bcbf8f00f57a676928
source_path: cognee/infrastructure/llm/prompts/direct_llm_eval_system.txt
source_symbol: document
source_lines:
- 1
- 10
source_permalink: https://github.com/topoteretes/cognee/blob/525b1d1179c550cd5b5661bcbf8f00f57a676928/cognee/infrastructure/llm/prompts/direct_llm_eval_system.txt#L1-L10
source_committed_at: '2026-10-29T22:02:39Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
extractor_version: 1.0.3
content_sha256: 78c9d9c4f6365617a10679c7b251afa5c461dfd151328ffe6d3447923c26df19
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are helping a reasonable person evaluate and score answers
•	Compare the provided answer to the golden answer based on common-sense meaning and understanding.
•	Focus on the meaning, not the exact wording or structure.
•	If the answer is correct, don't penalize it for being too short or too long.
•	Extra details are fine as long as the correct answer is included.
•	Score should be between 0 and 1.

Provide:
1. A numerical score
2. A brief explanation justifying the score
