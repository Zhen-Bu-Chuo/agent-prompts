---
agent: hindsight
prompt_id: prompts-7a4aa2c3e9ba
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 7cec128b8fdb0a696366d888e63be71fe1d52338
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.16
source_lines:
- 320
- 320
source_permalink: https://github.com/vectorize-io/hindsight/blob/7cec128b8fdb0a696366d888e63be71fe1d52338/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L320-L320
source_committed_at: '2026-11-11T17:59:36Z'
release_published_at: null
fetched_at: '2026-11-12T07:58:32Z'
extractor_version: 1.0.3
content_sha256: 9a6f413e64aca5a989aa4c0ef4e48249058e44f78978b0e118f9df647243e7db
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
4. **Sanity-check each candidate event against the authoritative date** — for EVERY event from step 3, write a one-line check in the form `<event> (<event_date>) vs authoritative (<authoritative_date>) → BEFORE/AFTER → KEEP/DROP`. If the event is BEFORE or EQUAL to the authoritative date, DROP it: it is already reflected in the authoritative fact, and applying it again is double-counting. This is the single most common mistake — do not skip this step even if you feel confident.