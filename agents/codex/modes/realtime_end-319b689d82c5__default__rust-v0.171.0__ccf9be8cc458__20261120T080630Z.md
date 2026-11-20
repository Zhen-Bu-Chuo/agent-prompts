---
agent: codex
prompt_id: realtime_end-319b689d82c5
module: modes
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.171.0
package_name: null
package_version: null
source_ref: rust-v0.171.0
source_commit: ccf9be8cc458bd6b8336fe84d68d8893f2691a5e
source_path: codex-rs/prompts/templates/realtime/realtime_end.md
source_symbol: document
source_lines:
- 1
- 3
source_permalink: https://github.com/openai/codex/blob/ccf9be8cc458bd6b8336fe84d68d8893f2691a5e/codex-rs/prompts/templates/realtime/realtime_end.md#L1-L3
source_committed_at: '2026-11-19T23:07:36Z'
release_published_at: '2026-11-20T00:44:47Z'
fetched_at: '2026-11-20T08:06:30Z'
extractor_version: 1.0.3
content_sha256: 95dbde1501871117f96d45f95cb501abbbc25464eab1ae5ed689e110e1849036
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Realtime conversation ended.

Subsequent user input will return to typed text rather than transcript-style text. Do not assume recognition errors or missing punctuation once realtime has ended. Resume normal chat behavior.
