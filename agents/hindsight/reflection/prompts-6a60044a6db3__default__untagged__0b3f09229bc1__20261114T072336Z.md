---
agent: hindsight
prompt_id: prompts-6a60044a6db3
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 0b3f09229bc13820f961244238ca885fda674076
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.7
source_lines:
- 301
- 301
source_permalink: https://github.com/vectorize-io/hindsight/blob/0b3f09229bc13820f961244238ca885fda674076/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L301-L301
source_committed_at: '2026-11-13T15:54:06Z'
release_published_at: null
fetched_at: '2026-11-14T07:23:36Z'
extractor_version: 1.0.3
content_sha256: 7e345d4995fe6e70d2238d6af8b83d9264b4819f4d158f602bbc68d6ea754034
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
For reconstructing a TIMELINE of events, order by `occurred_start` / `occurred_end` (when things happened), not `mentioned_at` (when they were retained).