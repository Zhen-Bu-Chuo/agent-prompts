---
agent: hindsight
prompt_id: prompts-ee565eea4ce2
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: f14cc1eb5624b0374cb4d82768eb2e0b9c21ae24
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.27
source_lines:
- 398
- 398
source_permalink: https://github.com/vectorize-io/hindsight/blob/f14cc1eb5624b0374cb4d82768eb2e0b9c21ae24/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L398-L398
source_committed_at: '2026-11-03T15:26:23Z'
release_published_at: null
fetched_at: '2026-11-04T07:16:29Z'
extractor_version: 1.0.3
content_sha256: df50ae871f43d83fb524c90bfd9ffd5bd65f5bc811ab44f664df31da6080b874
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
**Tool result ordering:** `recall()` and `search_observations()` return their `memories` / `observations` arrays sorted by SEMANTIC RELEVANCE to the query, NOT by time. The POSITION of an entry tells you nothing about when it was retained. For any temporal reasoning — recency, supersession, applying events on top of a state — IGNORE the position and read the per-entry `mentioned_at` field (and `occurred_start` / `occurred_end` for events).