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
source_commit: 5318be8ea572aa00ceae636c71c1d8d334f805b6
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.27
source_lines:
- 395
- 397
source_permalink: https://github.com/vectorize-io/hindsight/blob/5318be8ea572aa00ceae636c71c1d8d334f805b6/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L395-L397
source_committed_at: '2026-11-14T09:16:49Z'
release_published_at: null
fetched_at: '2026-11-15T07:36:26Z'
extractor_version: 1.0.3
content_sha256: 31e36ce18ccbfe489bc1b7bacff71a243f59cfdfd95e3d9b609aab7340ac730e
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
- MANDATORY: If search_observations returns 0 results or count=0, OR returns observations that do not STATE the answer, you MUST call recall() before giving up. Never report that the bank holds nothing about something until recall() has run with the question's key terms verbatim