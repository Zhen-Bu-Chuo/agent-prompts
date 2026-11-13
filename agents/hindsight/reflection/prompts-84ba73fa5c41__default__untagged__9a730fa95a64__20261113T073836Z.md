---
agent: hindsight
prompt_id: prompts-84ba73fa5c41
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 9a730fa95a6453785341adaa436a9453ed5ebf7e
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.42
source_lines:
- 549
- 550
source_permalink: https://github.com/vectorize-io/hindsight/blob/9a730fa95a6453785341adaa436a9453ed5ebf7e/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L549-L550
source_committed_at: '2026-11-12T19:42:59Z'
release_published_at: null
fetched_at: '2026-11-13T07:38:36Z'
extractor_version: 1.0.3
content_sha256: 0dae602618910c18d21796e7b537e2a175c88eef53a69a041a1df0779a75d24b
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
If search_observations returns 0 results, is stale, OR does not state the answer, you MUST call recall() for raw facts