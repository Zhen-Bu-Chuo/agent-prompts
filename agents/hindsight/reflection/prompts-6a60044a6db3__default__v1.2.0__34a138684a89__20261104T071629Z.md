---
agent: hindsight
prompt_id: prompts-6a60044a6db3
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.2.0
package_name: null
package_version: null
source_ref: v1.2.0
source_commit: 34a138684a899b6ec34175f7a2b633860466d289
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.7
source_lines:
- 301
- 301
source_permalink: https://github.com/vectorize-io/hindsight/blob/34a138684a899b6ec34175f7a2b633860466d289/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L301-L301
source_committed_at: '2026-11-03T11:05:49Z'
release_published_at: '2026-11-03T11:38:19Z'
fetched_at: '2026-11-04T07:16:29Z'
extractor_version: 1.0.3
content_sha256: 7e345d4995fe6e70d2238d6af8b83d9264b4819f4d158f602bbc68d6ea754034
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
For reconstructing a TIMELINE of events, order by `occurred_start` / `occurred_end` (when things happened), not `mentioned_at` (when they were retained).