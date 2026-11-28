---
agent: cognee
prompt_id: graph_completion_decomposition_syst-a59c9ce8b4af
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: dbc515bdcde72691c1880978407ac1e5829bbc25
source_path: cognee/infrastructure/llm/prompts/graph_completion_decomposition_system_prompt.txt
source_symbol: document
source_lines:
- 1
- 10
source_permalink: https://github.com/topoteretes/cognee/blob/dbc515bdcde72691c1880978407ac1e5829bbc25/cognee/infrastructure/llm/prompts/graph_completion_decomposition_system_prompt.txt#L1-L10
source_committed_at: '2026-11-27T15:10:07Z'
release_published_at: null
fetched_at: '2026-11-28T08:41:40Z'
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
