---
agent: codex
prompt_id: realtime_end-319b689d82c5
module: modes
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.167.2
package_name: null
package_version: null
source_ref: rust-v0.167.2
source_commit: ce21072c90d32c40af7a55b60b2fb35c84a43a6a
source_path: codex-rs/prompts/templates/realtime/realtime_end.md
source_symbol: document
source_lines:
- 1
- 3
source_permalink: https://github.com/openai/codex/blob/ce21072c90d32c40af7a55b60b2fb35c84a43a6a/codex-rs/prompts/templates/realtime/realtime_end.md#L1-L3
source_committed_at: '2026-11-11T20:03:56Z'
release_published_at: '2026-11-11T22:44:46Z'
fetched_at: '2026-11-12T07:58:20Z'
extractor_version: 1.0.3
content_sha256: 95dbde1501871117f96d45f95cb501abbbc25464eab1ae5ed689e110e1849036
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Realtime conversation ended.

Subsequent user input will return to typed text rather than transcript-style text. Do not assume recognition errors or missing punctuation once realtime has ended. Resume normal chat behavior.
