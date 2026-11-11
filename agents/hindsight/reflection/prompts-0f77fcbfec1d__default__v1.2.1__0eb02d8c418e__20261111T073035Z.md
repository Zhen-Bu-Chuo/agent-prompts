---
agent: hindsight
prompt_id: prompts-0f77fcbfec1d
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.2.1
package_name: null
package_version: null
source_ref: v1.2.1
source_commit: 0eb02d8c418eac6b489bc63883c993b2257dfac4
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.32
source_lines:
- 459
- 459
source_permalink: https://github.com/vectorize-io/hindsight/blob/0eb02d8c418eac6b489bc63883c993b2257dfac4/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L459-L459
source_committed_at: '2026-11-10T14:02:17Z'
release_published_at: '2026-11-10T14:34:26Z'
fetched_at: '2026-11-11T07:30:35Z'
extractor_version: 1.0.3
content_sha256: 4179abd5977d6e20a6ee9f831a8ec98508446267a716ae35a7a0119ee47ff627
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
recall() uses semantic search. NEVER just echo the user's question - decompose it into targeted searches: