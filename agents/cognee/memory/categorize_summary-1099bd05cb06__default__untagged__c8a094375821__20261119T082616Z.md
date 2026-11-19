---
agent: cognee
prompt_id: categorize_summary-1099bd05cb06
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: c8a094375821f2d8c7c4945d3b2202e2e5d6603e
source_path: cognee/infrastructure/llm/prompts/categorize_summary.txt
source_symbol: document
source_lines:
- 1
- 2
source_permalink: https://github.com/topoteretes/cognee/blob/c8a094375821f2d8c7c4945d3b2202e2e5d6603e/cognee/infrastructure/llm/prompts/categorize_summary.txt#L1-L2
source_committed_at: '2026-11-18T21:40:46Z'
release_published_at: null
fetched_at: '2026-11-19T08:26:16Z'
extractor_version: 1.0.3
content_sha256: fcd1aba55bb375bdabf90f0f8356db187459288de2a5533d146505177fa8dd0f
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Chose the summaries that are relevant to the following query: `{{ query }}`
Here are the all summaries: `{{ summaries }}`
