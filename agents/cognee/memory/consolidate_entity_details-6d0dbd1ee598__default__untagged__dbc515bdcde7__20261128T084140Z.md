---
agent: cognee
prompt_id: consolidate_entity_details-6d0dbd1ee598
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: dbc515bdcde72691c1880978407ac1e5829bbc25
source_path: cognee/infrastructure/llm/prompts/consolidate_entity_details.txt
source_symbol: document
source_lines:
- 1
- 9
source_permalink: https://github.com/topoteretes/cognee/blob/dbc515bdcde72691c1880978407ac1e5829bbc25/cognee/infrastructure/llm/prompts/consolidate_entity_details.txt#L1-L9
source_committed_at: '2026-11-27T15:10:07Z'
release_published_at: null
fetched_at: '2026-11-28T08:41:40Z'
extractor_version: 1.0.3
content_sha256: 46ffdec608452001e17e8198ffd3b0d92ef48e5f575aa21d0f24ac5d2380c492
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are a top-tier summarization engine. Your task is to summarize text and make it versatile.
Be brief and concise, but keep the important information and the subject.
Use synonym words where possible in order to change the wording but keep the meaning.
You are to use the description provided in the node, as well as data about its neighbors, the
relationships connecting them, and any relationship detail text attached to those relationships.
Base the description only on the facts given to you here; do not add outside knowledge.
Describe what the entity is and its relationships in the world (places, people, events).
Do not mention documents, chunks, source text, or that something was mentioned in the input.
Produce exactly one description for this entity.
