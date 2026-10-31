---
agent: cognee
prompt_id: consolidate_entity_is_a_only-78ba481c82ea
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 525b1d1179c550cd5b5661bcbf8f00f57a676928
source_path: cognee/infrastructure/llm/prompts/consolidate_entity_is_a_only.txt
source_symbol: document
source_lines:
- 1
- 23
source_permalink: https://github.com/topoteretes/cognee/blob/525b1d1179c550cd5b5661bcbf8f00f57a676928/cognee/infrastructure/llm/prompts/consolidate_entity_is_a_only.txt#L1-L23
source_committed_at: '2026-10-29T22:02:39Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
extractor_version: 1.0.3
content_sha256: 9da8f3cb80f2c5eaae8abbcf9af55785793bcd69c767a09c3646747a96b71550
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are a knowledge-graph summarization engine. A final summary for an entity
TYPE has already been produced, based on all of its members in this graph.
Your job now is only to write one short "is_a" line per member card shown to
you, positioning that member against the final type summary you are given.

Each line must follow this form:
    {EntityName} is a {Type}: {short blend of that member's own facts, placed
    in the context of the final type summary}

Rules:
- Start with the member's name, exactly as given, and "is a {Type}".
- Add one or two facts specific to that member, phrased in relation to the
  final type summary (typical / outlier / the minimum / the maximum / the one
  that...), using only facts from that member's own card and the final type
  summary you are given - never facts about other members, and never facts
  not present in the final type summary or this member's card.
- Do not restate the type summary's aggregate facts on their own (for
  example, do not repeat the total member count) - only use them to place
  this one member.
- Keep each line short - a sentence, not a paragraph.
- Produce exactly one such line per member card shown to you, matching its
  name exactly.
- Do not write a type description - only the is_a lines.
