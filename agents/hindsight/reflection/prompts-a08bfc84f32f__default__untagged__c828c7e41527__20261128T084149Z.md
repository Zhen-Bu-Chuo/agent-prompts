---
agent: hindsight
prompt_id: prompts-a08bfc84f32f
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: c828c7e41527d0c4916cac0ba2b56334fed4a79d
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.9
source_lines:
- 318
- 318
source_permalink: https://github.com/vectorize-io/hindsight/blob/c828c7e41527d0c4916cac0ba2b56334fed4a79d/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L318-L318
source_committed_at: '2026-11-27T17:40:16Z'
release_published_at: null
fetched_at: '2026-11-28T08:41:49Z'
extractor_version: 1.0.3
content_sha256: df743806892a4439091ac1da19a56d04ff8e709400d4c400b98e61b3cd89fb21
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
- UNRESOLVABLE ambiguity — the data is internally inconsistent in a way the temporal rule does NOT settle. Examples: a recent aggregate (count, total) is incompatible with the individual entities you can enumerate; two equally-recent facts disagree and no later fact resolves them; events are described but their relative order is unclear; the user's own statements contradict each other and nothing later reconciles them.