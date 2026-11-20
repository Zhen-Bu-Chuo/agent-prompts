---
agent: hindsight
prompt_id: prompts-8848e8eb34af
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.2.3
package_name: null
package_version: null
source_ref: v1.2.3
source_commit: bd230e8bb40e768bf69f266f1dd3c9ae03e22fe3
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.28
source_lines:
- 400
- 400
source_permalink: https://github.com/vectorize-io/hindsight/blob/bd230e8bb40e768bf69f266f1dd3c9ae03e22fe3/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L400-L400
source_committed_at: '2026-11-19T22:21:53Z'
release_published_at: '2026-11-19T22:48:28Z'
fetched_at: '2026-11-20T08:06:42Z'
extractor_version: 1.0.3
content_sha256: df50ae871f43d83fb524c90bfd9ffd5bd65f5bc811ab44f664df31da6080b874
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
**Tool result ordering:** `recall()` and `search_observations()` return their `memories` / `observations` arrays sorted by SEMANTIC RELEVANCE to the query, NOT by time. The POSITION of an entry tells you nothing about when it was retained. For any temporal reasoning — recency, supersession, applying events on top of a state — IGNORE the position and read the per-entry `mentioned_at` field (and `occurred_start` / `occurred_end` for events).