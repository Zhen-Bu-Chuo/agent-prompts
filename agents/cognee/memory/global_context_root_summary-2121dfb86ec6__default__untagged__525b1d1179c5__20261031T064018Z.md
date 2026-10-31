---
agent: cognee
prompt_id: global_context_root_summary-2121dfb86ec6
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 525b1d1179c550cd5b5661bcbf8f00f57a676928
source_path: cognee/infrastructure/llm/prompts/global_context_root_summary.txt
source_symbol: document
source_lines:
- 1
- 29
source_permalink: https://github.com/topoteretes/cognee/blob/525b1d1179c550cd5b5661bcbf8f00f57a676928/cognee/infrastructure/llm/prompts/global_context_root_summary.txt#L1-L29
source_committed_at: '2026-10-29T22:02:39Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
extractor_version: 1.0.3
content_sha256: 80ef1c2fb7b4f4186a960f75026f681ac27cac4fbc2ff91dc2d1da9dbfa7d551
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Compress the top-level summaries into one retrieval-ready dataset summary.

Output two sections only.

First section:
This dataset is about:
- <Category>: <names or topics>
- <Category>: <names or topics>

First-section rules:
1. List entity/topic categories that define the dataset. Do not list facts here.
2. Use only useful categories present in the inputs.
3. Good categories include People, Companies, Organizations, Places, Roles, Projects, Products, Systems, Concepts, Events, and Topics; prefer central concrete names.
4. Keep category lines short. Do not include weak or generic words.

Second section:
Facts:
- <high-level self-contained fact or tight fact group>
- <high-level self-contained fact or tight fact group>

Second-section rules:
1. Write high-level complete sentences with clear subjects.
2. Each fact must stand alone without the input summaries or the other facts.
3. Order facts by: time first, category second, entity/topic third.
4. Do not group all facts about one entity if that makes the facts jump backward or forward in time.
5. Make sure the facts cover the important dataset-level content of the input summaries.
6. Do not invent.

Max 500 tokens.
