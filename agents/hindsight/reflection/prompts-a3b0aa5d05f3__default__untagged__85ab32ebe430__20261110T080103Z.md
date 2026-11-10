---
agent: hindsight
prompt_id: prompts-a3b0aa5d05f3
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 85ab32ebe4301e59c173c4dc775e01b1e6d43a71
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.6
source_lines:
- 299
- 299
source_permalink: https://github.com/vectorize-io/hindsight/blob/85ab32ebe4301e59c173c4dc775e01b1e6d43a71/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L299-L299
source_committed_at: '2026-11-10T00:55:00Z'
release_published_at: null
fetched_at: '2026-11-10T08:01:03Z'
extractor_version: 1.0.3
content_sha256: e8c953fde6830ee6a2f8c60b45fbf0225009eb796a9e2d60e8e06163e7652c05
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
with T1 < T2 < T3. The current size is 5, not 1. Then apply later events (e.g. someone leaving after T3) on top of that.