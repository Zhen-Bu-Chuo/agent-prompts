---
agent: hindsight
prompt_id: prompts-ee565eea4ce2
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.2.3
package_name: null
package_version: null
source_ref: v1.2.3
source_commit: bd230e8bb40e768bf69f266f1dd3c9ae03e22fe3
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.27
source_lines:
- 395
- 397
source_permalink: https://github.com/vectorize-io/hindsight/blob/bd230e8bb40e768bf69f266f1dd3c9ae03e22fe3/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L395-L397
source_committed_at: '2026-11-19T22:21:53Z'
release_published_at: '2026-11-19T22:48:28Z'
fetched_at: '2026-11-20T08:06:42Z'
extractor_version: 1.0.3
content_sha256: 31e36ce18ccbfe489bc1b7bacff71a243f59cfdfd95e3d9b609aab7340ac730e
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
- MANDATORY: If search_observations returns 0 results or count=0, OR returns observations that do not STATE the answer, you MUST call recall() before giving up. Never report that the bank holds nothing about something until recall() has run with the question's key terms verbatim