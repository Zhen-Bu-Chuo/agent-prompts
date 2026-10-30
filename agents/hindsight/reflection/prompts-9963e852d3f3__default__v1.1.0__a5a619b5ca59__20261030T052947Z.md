---
agent: hindsight
prompt_id: prompts-9963e852d3f3
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.1.0
package_name: null
package_version: null
source_ref: v1.1.0
source_commit: a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.18
source_lines:
- 321
- 321
source_permalink: https://github.com/vectorize-io/hindsight/blob/a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L321-L321
source_committed_at: '2026-10-21T16:16:23Z'
release_published_at: '2026-10-21T16:41:42Z'
fetched_at: '2026-10-30T05:29:47Z'
extractor_version: 1.0.3
content_sha256: 2fd0dd6328b9444648b28b76b0ac4f199d9c9a508565290b9557e0c3d968b9c0
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
6. If step 2 or 3 cannot be done cleanly (no clear winner, overlapping timestamps, unclear event order), STOP and surface this as an UNRESOLVABLE ambiguity per the section above — do not fabricate a derivation.