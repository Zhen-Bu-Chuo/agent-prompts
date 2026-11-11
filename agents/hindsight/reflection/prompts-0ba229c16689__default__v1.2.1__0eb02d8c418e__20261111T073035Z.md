---
agent: hindsight
prompt_id: prompts-0ba229c16689
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.2.1
package_name: null
package_version: null
source_ref: v1.2.1
source_commit: 0eb02d8c418eac6b489bc63883c993b2257dfac4
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.25
source_lines:
- 383
- 385
source_permalink: https://github.com/vectorize-io/hindsight/blob/0eb02d8c418eac6b489bc63883c993b2257dfac4/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L383-L385
source_committed_at: '2026-11-10T14:02:17Z'
release_published_at: '2026-11-10T14:34:26Z'
fetched_at: '2026-11-11T07:30:35Z'
extractor_version: 1.0.3
content_sha256: 7d2227440838d05b3202169c9c0672fc5b4ae738c5dab5ecc402b9444eb29f36
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
- MANDATORY: If search_mental_models returns 0 results, OR returns a model that does not STATE the answer, you MUST call recall() before giving up. Never report that the bank holds nothing about something until recall() has run with the question's key terms verbatim