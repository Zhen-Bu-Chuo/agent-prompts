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
source_commit: bc5ea195a0fed1346ff171a5780bbb72a38c89c8
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.9
source_lines:
- 307
- 307
source_permalink: https://github.com/vectorize-io/hindsight/blob/bc5ea195a0fed1346ff171a5780bbb72a38c89c8/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L307-L307
source_committed_at: '2026-10-30T23:40:41Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:30Z'
extractor_version: 1.0.3
content_sha256: df743806892a4439091ac1da19a56d04ff8e709400d4c400b98e61b3cd89fb21
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
- UNRESOLVABLE ambiguity — the data is internally inconsistent in a way the temporal rule does NOT settle. Examples: a recent aggregate (count, total) is incompatible with the individual entities you can enumerate; two equally-recent facts disagree and no later fact resolves them; events are described but their relative order is unclear; the user's own statements contradict each other and nothing later reconciles them.