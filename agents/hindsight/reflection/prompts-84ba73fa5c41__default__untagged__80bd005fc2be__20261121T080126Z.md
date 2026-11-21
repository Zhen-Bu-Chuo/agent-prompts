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
source_commit: 80bd005fc2be5c9604a1a0c9741ea93d5ac85156
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.42
source_lines:
- 549
- 550
source_permalink: https://github.com/vectorize-io/hindsight/blob/80bd005fc2be5c9604a1a0c9741ea93d5ac85156/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L549-L550
source_committed_at: '2026-11-20T21:45:57Z'
release_published_at: null
fetched_at: '2026-11-21T08:01:26Z'
extractor_version: 1.0.3
content_sha256: 0dae602618910c18d21796e7b537e2a175c88eef53a69a041a1df0779a75d24b
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
If search_observations returns 0 results, is stale, OR does not state the answer, you MUST call recall() for raw facts