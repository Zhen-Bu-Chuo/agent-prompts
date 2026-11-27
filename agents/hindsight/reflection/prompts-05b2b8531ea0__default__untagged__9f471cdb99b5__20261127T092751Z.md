---
agent: hindsight
prompt_id: prompts-05b2b8531ea0
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 9f471cdb99b5de4a87cc279b39eb97ec4d4545a9
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.33
source_lines:
- 472
- 472
source_permalink: https://github.com/vectorize-io/hindsight/blob/9f471cdb99b5de4a87cc279b39eb97ec4d4545a9/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L472-L472
source_committed_at: '2026-11-26T22:41:54Z'
release_published_at: null
fetched_at: '2026-11-27T09:27:51Z'
extractor_version: 1.0.3
content_sha256: 4179abd5977d6e20a6ee9f831a8ec98508446267a716ae35a7a0119ee47ff627
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
recall() uses semantic search. NEVER just echo the user's question - decompose it into targeted searches: