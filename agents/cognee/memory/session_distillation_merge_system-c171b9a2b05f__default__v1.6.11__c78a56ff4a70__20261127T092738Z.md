---
agent: cognee
prompt_id: session_distillation_merge_system-c171b9a2b05f
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.11
package_name: null
package_version: null
source_ref: v1.6.11
source_commit: c78a56ff4a705a6f46090a1fe6a3a9737f45e17b
source_path: cognee/infrastructure/llm/prompts/coding/session_distillation_merge_system.txt
source_symbol: document
source_lines:
- 1
- 13
source_permalink: https://github.com/topoteretes/cognee/blob/c78a56ff4a705a6f46090a1fe6a3a9737f45e17b/cognee/infrastructure/llm/prompts/coding/session_distillation_merge_system.txt#L1-L13
source_committed_at: '2026-11-26T16:54:44Z'
release_published_at: '2026-11-26T17:05:51Z'
fetched_at: '2026-11-27T09:27:38Z'
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
