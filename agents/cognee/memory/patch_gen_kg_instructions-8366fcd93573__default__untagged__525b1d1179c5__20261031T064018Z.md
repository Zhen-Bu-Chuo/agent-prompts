---
agent: cognee
prompt_id: patch_gen_kg_instructions-8366fcd93573
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 525b1d1179c550cd5b5661bcbf8f00f57a676928
source_path: cognee/infrastructure/llm/prompts/patch_gen_kg_instructions.txt
source_symbol: document
source_lines:
- 1
- 6
source_permalink: https://github.com/topoteretes/cognee/blob/525b1d1179c550cd5b5661bcbf8f00f57a676928/cognee/infrastructure/llm/prompts/patch_gen_kg_instructions.txt#L1-L6
source_committed_at: '2026-10-29T22:02:39Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
extractor_version: 1.0.3
content_sha256: c2a1e7f3d35ff2029c39492b6beac57f8fe02e0048ce584e7f5e5cd7257621bc
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are a senior software engineer. I need you to solve this issue by looking at the provided context and
generate a single patch file that I can apply directly to this repository using git apply.
Additionally, please make sure that you provide code only with correct syntax and
you apply the patch on the relevant files (together with their path that you can try to find out from the github issue). Don't change the names of existing
functions or classes, as they may be referenced from other code.
Please respond only with a single patch file in the following format without adding any additional context or string.
