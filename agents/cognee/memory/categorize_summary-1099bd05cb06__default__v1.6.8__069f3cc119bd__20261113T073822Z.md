---
agent: cognee
prompt_id: categorize_summary-1099bd05cb06
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.8
package_name: null
package_version: null
source_ref: v1.6.8
source_commit: 069f3cc119bdf5628be054bb915992b2fc78cfc5
source_path: cognee/infrastructure/llm/prompts/categorize_summary.txt
source_symbol: document
source_lines:
- 1
- 2
source_permalink: https://github.com/topoteretes/cognee/blob/069f3cc119bdf5628be054bb915992b2fc78cfc5/cognee/infrastructure/llm/prompts/categorize_summary.txt#L1-L2
source_committed_at: '2026-11-12T22:26:02Z'
release_published_at: '2026-11-12T22:31:22Z'
fetched_at: '2026-11-13T07:38:22Z'
extractor_version: 1.0.3
content_sha256: fcd1aba55bb375bdabf90f0f8356db187459288de2a5533d146505177fa8dd0f
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Chose the summaries that are relevant to the following query: `{{ query }}`
Here are the all summaries: `{{ summaries }}`
