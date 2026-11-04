---
agent: hindsight
prompt_id: prompts-99c40c4919eb
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.2.0
package_name: null
package_version: null
source_ref: v1.2.0
source_commit: 34a138684a899b6ec34175f7a2b633860466d289
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.30
source_lines:
- 447
- 448
source_permalink: https://github.com/vectorize-io/hindsight/blob/34a138684a899b6ec34175f7a2b633860466d289/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L447-L448
source_committed_at: '2026-11-03T11:05:49Z'
release_published_at: '2026-11-03T11:38:19Z'
fetched_at: '2026-11-04T07:16:29Z'
extractor_version: 1.0.3
content_sha256: f740f7890076d05fabf1f38d8ba723ad2f85a68cc2bb53025ae73a162f8a1f95
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
- Call `answer_ready` once you have the evidence; you are then asked for the answer. Do not write the answer before that.