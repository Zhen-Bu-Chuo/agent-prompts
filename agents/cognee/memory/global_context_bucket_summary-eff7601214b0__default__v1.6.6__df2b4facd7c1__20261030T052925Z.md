---
agent: cognee
prompt_id: global_context_bucket_summary-eff7601214b0
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.6
package_name: null
package_version: null
source_ref: v1.6.6
source_commit: df2b4facd7c1d73b59376fd251fb93674a9d60a3
source_path: cognee/infrastructure/llm/prompts/global_context_bucket_summary.txt
source_symbol: document
source_lines:
- 1
- 29
source_permalink: https://github.com/topoteretes/cognee/blob/df2b4facd7c1d73b59376fd251fb93674a9d60a3/cognee/infrastructure/llm/prompts/global_context_bucket_summary.txt#L1-L29
source_committed_at: '2026-10-29T21:29:40Z'
release_published_at: '2026-10-29T21:33:43Z'
fetched_at: '2026-10-30T05:29:25Z'
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
