---
agent: codex
prompt_id: realtime_end-319b689d82c5
module: modes
variant: default
upstream_repository: openai/codex
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 748ab55ca7de0b647d9a7a9d9a8e70e00f28666d
source_path: codex-rs/prompts/templates/realtime/realtime_end.md
source_symbol: document
source_lines:
- 1
- 3
source_permalink: https://github.com/openai/codex/blob/748ab55ca7de0b647d9a7a9d9a8e70e00f28666d/codex-rs/prompts/templates/realtime/realtime_end.md#L1-L3
source_committed_at: '2026-11-08T05:59:11Z'
release_published_at: null
fetched_at: '2026-11-08T06:56:22Z'
extractor_version: 1.0.3
content_sha256: 95dbde1501871117f96d45f95cb501abbbc25464eab1ae5ed689e110e1849036
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Realtime conversation ended.

Subsequent user input will return to typed text rather than transcript-style text. Do not assume recognition errors or missing punctuation once realtime has ended. Resume normal chat behavior.
