---
agent: cognee
prompt_id: graph_completion_decomposition_syst-a59c9ce8b4af
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.7
package_name: null
package_version: null
source_ref: v1.6.7
source_commit: eaa33be5c58cd14584e64e3e0ed2e1479472ee09
source_path: cognee/infrastructure/llm/prompts/graph_completion_decomposition_system_prompt.txt
source_symbol: document
source_lines:
- 1
- 10
source_permalink: https://github.com/topoteretes/cognee/blob/eaa33be5c58cd14584e64e3e0ed2e1479472ee09/cognee/infrastructure/llm/prompts/graph_completion_decomposition_system_prompt.txt#L1-L10
source_committed_at: '2026-11-06T17:10:58Z'
release_published_at: '2026-11-06T17:15:07Z'
fetched_at: '2026-11-07T06:51:14Z'
extractor_version: 1.0.3
content_sha256: 3c8436fa03ff446e520344b04372907d4407727e585a5e97920f0a29a983a16b
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Decompose the user's question into 1 to 5 focused retrieval subqueries.

Rules:
- Return only subqueries that help retrieve graph context for the original question.
- Preserve the original order of reasoning from broadest to most specific when possible.
- Keep each subquery concise and self-contained.
- Do not answer the question.
- Do not include explanations or metadata.
- Avoid duplicates or near-duplicates.
- If the original question is already focused, return it as a single subquery.
