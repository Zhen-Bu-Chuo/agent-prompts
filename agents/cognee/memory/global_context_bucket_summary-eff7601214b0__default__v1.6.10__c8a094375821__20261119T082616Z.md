---
agent: cognee
prompt_id: global_context_bucket_summary-eff7601214b0
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.10
package_name: null
package_version: null
source_ref: v1.6.10
source_commit: c8a094375821f2d8c7c4945d3b2202e2e5d6603e
source_path: cognee/infrastructure/llm/prompts/global_context_bucket_summary.txt
source_symbol: document
source_lines:
- 1
- 29
source_permalink: https://github.com/topoteretes/cognee/blob/c8a094375821f2d8c7c4945d3b2202e2e5d6603e/cognee/infrastructure/llm/prompts/global_context_bucket_summary.txt#L1-L29
source_committed_at: '2026-11-18T21:40:46Z'
release_published_at: '2026-11-18T21:42:57Z'
fetched_at: '2026-11-19T08:26:16Z'
extractor_version: 1.0.3
content_sha256: a57f176205013eafa4121284e03cfb4f488361dc4a1899bec453b1f8c992463a
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Compress the input summaries into one retrieval-ready area summary.

Output two sections only.

First section:
This area of the dataset is about:
- <Category>: <names or topics>
- <Category>: <names or topics>

First-section rules:
1. List entity/topic categories that define this area. Do not list facts here.
2. Use only useful categories present in the inputs.
3. Good categories include People, Companies, Organizations, Places, Roles, Projects, Products, Systems, Concepts, Events, and Topics; prefer recurring concrete names.
4. Keep category lines short. Do not include weak or generic words.

Second section:
Facts:
- <self-contained fact or tight fact group>
- <self-contained fact or tight fact group>

Second-section rules:
1. Write compressed complete sentences with clear subjects.
2. Each fact must stand alone without the input summaries or the other facts.
3. Order facts by: time first, category second, entity/topic third.
4. Do not group all facts about one entity if that makes the facts jump backward or forward in time.
5. Make sure the facts cover the important content of the input summaries.
6. Do not invent.

Max 300 tokens.
