---
agent: cognee
prompt_id: session_distillation_merge_system-c171b9a2b05f
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.10
package_name: null
package_version: null
source_ref: v1.6.10
source_commit: c8a094375821f2d8c7c4945d3b2202e2e5d6603e
source_path: cognee/infrastructure/llm/prompts/coding/session_distillation_merge_system.txt
source_symbol: document
source_lines:
- 1
- 13
source_permalink: https://github.com/topoteretes/cognee/blob/c8a094375821f2d8c7c4945d3b2202e2e5d6603e/cognee/infrastructure/llm/prompts/coding/session_distillation_merge_system.txt#L1-L13
source_committed_at: '2026-11-18T21:40:46Z'
release_published_at: '2026-11-18T21:42:57Z'
fetched_at: '2026-11-19T08:26:16Z'
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
