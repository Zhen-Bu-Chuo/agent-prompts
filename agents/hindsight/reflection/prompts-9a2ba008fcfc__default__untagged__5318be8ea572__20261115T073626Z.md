---
agent: hindsight
prompt_id: prompts-9a2ba008fcfc
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 5318be8ea572aa00ceae636c71c1d8d334f805b6
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.24
source_lines:
- 371
- 374
source_permalink: https://github.com/vectorize-io/hindsight/blob/5318be8ea572aa00ceae636c71c1d8d334f805b6/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L371-L374
source_committed_at: '2026-11-14T09:16:49Z'
release_published_at: null
fetched_at: '2026-11-15T07:36:26Z'
extractor_version: 1.0.3
content_sha256: c275df7b182276a95c4670807c7ab3b8b8ac35e178ea51e8f822f092fe737d5c
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
- MANDATORY: If search_mental_models and search_observations return 0 results, OR return results that do not STATE the answer, you MUST call recall() before giving up. Never report that the bank holds nothing about something until recall() has run with the question's key terms (an issue key, name or identifier) verbatim