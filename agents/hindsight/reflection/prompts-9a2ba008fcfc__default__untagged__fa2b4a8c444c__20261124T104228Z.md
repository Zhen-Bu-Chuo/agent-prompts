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
source_commit: fa2b4a8c444cb73630859bdbba8b4e6c26bd80c1
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.24
source_lines:
- 382
- 385
source_permalink: https://github.com/vectorize-io/hindsight/blob/fa2b4a8c444cb73630859bdbba8b4e6c26bd80c1/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L382-L385
source_committed_at: '2026-11-24T10:34:27Z'
release_published_at: null
fetched_at: '2026-11-24T10:42:28Z'
extractor_version: 1.0.3
content_sha256: c275df7b182276a95c4670807c7ab3b8b8ac35e178ea51e8f822f092fe737d5c
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
- MANDATORY: If search_mental_models and search_observations return 0 results, OR return results that do not STATE the answer, you MUST call recall() before giving up. Never report that the bank holds nothing about something until recall() has run with the question's key terms (an issue key, name or identifier) verbatim