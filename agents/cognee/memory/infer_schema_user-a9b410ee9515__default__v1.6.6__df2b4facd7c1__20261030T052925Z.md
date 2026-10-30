---
agent: cognee
prompt_id: infer_schema_user-a9b410ee9515
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.6
package_name: null
package_version: null
source_ref: v1.6.6
source_commit: df2b4facd7c1d73b59376fd251fb93674a9d60a3
source_path: cognee/infrastructure/llm/prompts/infer_schema_user.txt
source_symbol: document
source_lines:
- 1
- 3
source_permalink: https://github.com/topoteretes/cognee/blob/df2b4facd7c1d73b59376fd251fb93674a9d60a3/cognee/infrastructure/llm/prompts/infer_schema_user.txt#L1-L3
source_committed_at: '2026-10-29T21:29:40Z'
release_published_at: '2026-10-29T21:33:43Z'
fetched_at: '2026-10-30T05:29:25Z'
extractor_version: 1.0.3
content_sha256: b0cdfac8aa85580341cfa3c4cb3f3fa379ef217ac9fa124ce4e7facaf9adf0c7
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Analyze the following text and propose a graph schema (JSON Schema) that captures the entity types and relationships present:

{{SAMPLE_TEXT}}
