---
agent: hindsight
prompt_id: prompts-5d552214cfc9
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 289fb421bdb438861480720e947874551ac42ff7
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.4
source_lines:
- 291
- 291
source_permalink: https://github.com/vectorize-io/hindsight/blob/289fb421bdb438861480720e947874551ac42ff7/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L291-L291
source_committed_at: '2026-11-10T17:14:29Z'
release_published_at: null
fetched_at: '2026-11-11T07:30:35Z'
extractor_version: 1.0.3
content_sha256: 395aa20cbf62501e06d2ef66d61281bbf0ebebfd0de85f7ba555f053efdc0d97
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
When facts about the SAME facet conflict — counts, statuses, ownership, location, presence, etc. — the fact with the LATEST `mentioned_at` is authoritative. Later statements SUPERSEDE earlier ones. Do NOT average, sum, or favor an explicitly-dated fact over a more recent one. The one exception is a DECISION, below.