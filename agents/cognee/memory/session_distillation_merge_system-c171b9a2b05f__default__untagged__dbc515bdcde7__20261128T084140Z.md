---
agent: cognee
prompt_id: session_distillation_merge_system-c171b9a2b05f
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: dbc515bdcde72691c1880978407ac1e5829bbc25
source_path: cognee/infrastructure/llm/prompts/coding/session_distillation_merge_system.txt
source_symbol: document
source_lines:
- 1
- 13
source_permalink: https://github.com/topoteretes/cognee/blob/dbc515bdcde72691c1880978407ac1e5829bbc25/cognee/infrastructure/llm/prompts/coding/session_distillation_merge_system.txt#L1-L13
source_committed_at: '2026-11-27T15:10:07Z'
release_published_at: null
fetched_at: '2026-11-28T08:41:40Z'
extractor_version: 1.0.3
content_sha256: aaece133ebf1cf23b3a2924f26570c8b3dcff3714796784099dd2d29cdcad3ea
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You receive a numbered list of lessons proposed from one coding session. Some were proposed
more than once, in different words. Find the lessons that state the same fact.

Two lessons are duplicates only when they say the same thing about the same files, symbols,
commands or tests, so that keeping one loses nothing the other says. Lessons that differ in a
name, a number, an outcome or a reason are not duplicates, even when they are worded alike.
Lessons about the same subject that state different facts are not duplicates. When unsure,
do not group them.

Return groups: each group is the list of the numbers of lessons that are duplicates of each
other, two or more numbers per group. A number appears in at most one group. Leave out every
lesson that has no duplicate. Return no groups when there are no duplicates. Do not rewrite,
judge or drop any lesson.
