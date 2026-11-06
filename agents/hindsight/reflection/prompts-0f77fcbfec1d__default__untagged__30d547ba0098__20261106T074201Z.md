---
agent: hindsight
prompt_id: prompts-0f77fcbfec1d
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 30d547ba00989297057a9679f2d59f30a554b240
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.32
source_lines:
- 459
- 459
source_permalink: https://github.com/vectorize-io/hindsight/blob/30d547ba00989297057a9679f2d59f30a554b240/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L459-L459
source_committed_at: '2026-11-05T14:20:11Z'
release_published_at: null
fetched_at: '2026-11-06T07:42:01Z'
extractor_version: 1.0.3
content_sha256: 4179abd5977d6e20a6ee9f831a8ec98508446267a716ae35a7a0119ee47ff627
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
recall() uses semantic search. NEVER just echo the user's question - decompose it into targeted searches: