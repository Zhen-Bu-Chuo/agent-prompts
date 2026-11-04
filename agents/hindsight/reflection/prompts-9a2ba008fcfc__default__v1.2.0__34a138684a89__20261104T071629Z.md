---
agent: hindsight
prompt_id: prompts-9a2ba008fcfc
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.2.0
package_name: null
package_version: null
source_ref: v1.2.0
source_commit: 34a138684a899b6ec34175f7a2b633860466d289
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.24
source_lines:
- 375
- 375
source_permalink: https://github.com/vectorize-io/hindsight/blob/34a138684a899b6ec34175f7a2b633860466d289/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L375-L375
source_committed_at: '2026-11-03T11:05:49Z'
release_published_at: '2026-11-03T11:38:19Z'
fetched_at: '2026-11-04T07:16:29Z'
extractor_version: 1.0.3
content_sha256: df50ae871f43d83fb524c90bfd9ffd5bd65f5bc811ab44f664df31da6080b874
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
**Tool result ordering:** `recall()` and `search_observations()` return their `memories` / `observations` arrays sorted by SEMANTIC RELEVANCE to the query, NOT by time. The POSITION of an entry tells you nothing about when it was retained. For any temporal reasoning — recency, supersession, applying events on top of a state — IGNORE the position and read the per-entry `mentioned_at` field (and `occurred_start` / `occurred_end` for events).