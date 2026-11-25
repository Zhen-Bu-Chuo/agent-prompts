---
agent: hindsight
prompt_id: prompts-05b2b8531ea0
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.3.0
package_name: null
package_version: null
source_ref: v1.3.0
source_commit: 937886199e0e3443f41f4d8180a16b12cc95c547
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.33
source_lines:
- 472
- 472
source_permalink: https://github.com/vectorize-io/hindsight/blob/937886199e0e3443f41f4d8180a16b12cc95c547/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L472-L472
source_committed_at: '2026-11-24T13:04:19Z'
release_published_at: '2026-11-24T14:20:19Z'
fetched_at: '2026-11-25T09:35:45Z'
extractor_version: 1.0.3
content_sha256: 4179abd5977d6e20a6ee9f831a8ec98508446267a716ae35a7a0119ee47ff627
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
recall() uses semantic search. NEVER just echo the user's question - decompose it into targeted searches: