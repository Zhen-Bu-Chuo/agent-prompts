---
agent: hindsight
prompt_id: prompts-07f4e1d0ca4d
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.1.0
package_name: null
package_version: null
source_ref: v1.1.0
source_commit: a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.23
source_lines:
- 368
- 371
source_permalink: https://github.com/vectorize-io/hindsight/blob/a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L368-L371
source_committed_at: '2026-10-21T16:16:23Z'
release_published_at: '2026-10-21T16:41:42Z'
fetched_at: '2026-10-30T05:29:47Z'
extractor_version: 1.0.3
content_sha256: c275df7b182276a95c4670807c7ab3b8b8ac35e178ea51e8f822f092fe737d5c
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
- MANDATORY: If search_mental_models and search_observations return 0 results, OR return results that do not STATE the answer, you MUST call recall() before giving up. Never report that the bank holds nothing about something until recall() has run with the question's key terms (an issue key, name or identifier) verbatim