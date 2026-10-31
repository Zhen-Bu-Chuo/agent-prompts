---
agent: cognee
prompt_id: transcribe_image_prompt-e97059aa05f8
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 525b1d1179c550cd5b5661bcbf8f00f57a676928
source_path: cognee/infrastructure/llm/prompts/transcribe_image_prompt.txt
source_symbol: document
source_lines:
- 1
- 11
source_permalink: https://github.com/topoteretes/cognee/blob/525b1d1179c550cd5b5661bcbf8f00f57a676928/cognee/infrastructure/llm/prompts/transcribe_image_prompt.txt#L1-L11
source_committed_at: '2026-10-29T22:02:39Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
extractor_version: 1.0.3
content_sha256: 1ac594dc873eda6f31bd3603668c4d0559b6df1b5b690c1b1d5ff2e969fb3780
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Describe this image as concise, factual text for knowledge extraction.

Capture:
- The entities shown (people, organizations, objects, places, concepts) and their attributes.
- The relationships and connections between them.
- All visible text, numbers, dates, and labels, transcribed verbatim.
- Structured content: tables as rows with their values, charts as their series and data points,
  diagrams as how the elements connect.

Keep it factual and to the point. Include only what is visible; do not guess or add outside
knowledge.
