---
agent: hindsight
prompt_id: prompts-5d552214cfc9
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.2.0
package_name: null
package_version: null
source_ref: v1.2.0
source_commit: 34a138684a899b6ec34175f7a2b633860466d289
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.4
source_lines:
- 291
- 291
source_permalink: https://github.com/vectorize-io/hindsight/blob/34a138684a899b6ec34175f7a2b633860466d289/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L291-L291
source_committed_at: '2026-11-03T11:05:49Z'
release_published_at: '2026-11-03T11:38:19Z'
fetched_at: '2026-11-04T07:16:29Z'
extractor_version: 1.0.3
content_sha256: 395aa20cbf62501e06d2ef66d61281bbf0ebebfd0de85f7ba555f053efdc0d97
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
When facts about the SAME facet conflict — counts, statuses, ownership, location, presence, etc. — the fact with the LATEST `mentioned_at` is authoritative. Later statements SUPERSEDE earlier ones. Do NOT average, sum, or favor an explicitly-dated fact over a more recent one. The one exception is a DECISION, below.