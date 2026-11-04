---
agent: hindsight
prompt_id: prompts-9963e852d3f3
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: f14cc1eb5624b0374cb4d82768eb2e0b9c21ae24
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.18
source_lines:
- 322
- 322
source_permalink: https://github.com/vectorize-io/hindsight/blob/f14cc1eb5624b0374cb4d82768eb2e0b9c21ae24/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L322-L322
source_committed_at: '2026-11-03T15:26:23Z'
release_published_at: null
fetched_at: '2026-11-04T07:16:29Z'
extractor_version: 1.0.3
content_sha256: 2fd0dd6328b9444648b28b76b0ac4f199d9c9a508565290b9557e0c3d968b9c0
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
6. If step 2 or 3 cannot be done cleanly (no clear winner, overlapping timestamps, unclear event order), STOP and surface this as an UNRESOLVABLE ambiguity per the section above — do not fabricate a derivation.