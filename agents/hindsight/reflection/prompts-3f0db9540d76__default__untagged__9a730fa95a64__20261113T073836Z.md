---
agent: hindsight
prompt_id: prompts-3f0db9540d76
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 9a730fa95a6453785341adaa436a9453ed5ebf7e
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.26
source_lines:
- 385
- 387
source_permalink: https://github.com/vectorize-io/hindsight/blob/9a730fa95a6453785341adaa436a9453ed5ebf7e/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L385-L387
source_committed_at: '2026-11-12T19:42:59Z'
release_published_at: null
fetched_at: '2026-11-13T07:38:36Z'
extractor_version: 1.0.3
content_sha256: 7d2227440838d05b3202169c9c0672fc5b4ae738c5dab5ecc402b9444eb29f36
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
- MANDATORY: If search_mental_models returns 0 results, OR returns a model that does not STATE the answer, you MUST call recall() before giving up. Never report that the bank holds nothing about something until recall() has run with the question's key terms verbatim