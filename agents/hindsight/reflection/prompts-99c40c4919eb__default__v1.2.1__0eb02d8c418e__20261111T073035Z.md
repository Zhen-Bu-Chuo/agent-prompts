---
agent: hindsight
prompt_id: prompts-99c40c4919eb
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.2.1
package_name: null
package_version: null
source_ref: v1.2.1
source_commit: 0eb02d8c418eac6b489bc63883c993b2257dfac4
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.30
source_lines:
- 447
- 448
source_permalink: https://github.com/vectorize-io/hindsight/blob/0eb02d8c418eac6b489bc63883c993b2257dfac4/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L447-L448
source_committed_at: '2026-11-10T14:02:17Z'
release_published_at: '2026-11-10T14:34:26Z'
fetched_at: '2026-11-11T07:30:35Z'
extractor_version: 1.0.3
content_sha256: f740f7890076d05fabf1f38d8ba723ad2f85a68cc2bb53025ae73a162f8a1f95
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
- Call `answer_ready` once you have the evidence; you are then asked for the answer. Do not write the answer before that.