---
agent: hindsight
prompt_id: prompts-e0fd9756943d
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 1a37e009cbe9b8cd76b2c5d5b6c5745374e19507
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.2
source_lines:
- 282
- 282
source_permalink: https://github.com/vectorize-io/hindsight/blob/1a37e009cbe9b8cd76b2c5d5b6c5745374e19507/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L282-L282
source_committed_at: '2026-11-04T16:28:01Z'
release_published_at: null
fetched_at: '2026-11-05T07:44:11Z'
extractor_version: 1.0.3
content_sha256: 81d7f2378266250343a1ba8b80194e0304bec26423123e786171130f154c2e8d
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
- When the exact answer isn't stated, use what IS stated to give a best-effort answer AND surface any uncertainty — never invent confidence the data doesn't support.