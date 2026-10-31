---
agent: cognee
prompt_id: summarize_content-262476a842f8
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 525b1d1179c550cd5b5661bcbf8f00f57a676928
source_path: cognee/infrastructure/llm/prompts/summarize_content.txt
source_symbol: document
source_lines:
- 1
- 29
source_permalink: https://github.com/topoteretes/cognee/blob/525b1d1179c550cd5b5661bcbf8f00f57a676928/cognee/infrastructure/llm/prompts/summarize_content.txt#L1-L29
source_committed_at: '2026-10-29T22:02:39Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
extractor_version: 1.0.3
content_sha256: 863cff087d1264884008ac5e12a87b845809124a73debd5b7fdaa685a9f475a2
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Summarize the chunk for retrieval.

Output two sections only.

First section:
This chunk is about:
- <Category>: <names or topics>
- <Category>: <names or topics>

First-section rules:
1. List entity/topic categories. Do not list facts here.
2. Use only clear, useful categories.
3. Good categories include People, Companies, Organizations, Places, Roles, Projects, Products, Systems, Concepts, Events, and Topics.
4. Keep category lines short.

Second section:
Facts:
- <self-contained fact>
- <self-contained fact>

Second-section rules:
1. Write complete sentences with clear subjects from the first section.
2. Each fact must stand alone without the chunk or the other facts.
3. Order facts by: time first, category second, entity/topic third.
4. Do not group all facts about one entity if that makes the facts jump backward or forward in time.
5. Make sure the facts cover the full content of the chunk.
6. Do not invent.

Max 200 tokens.
