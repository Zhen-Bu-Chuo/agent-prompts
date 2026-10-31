---
agent: qwen-code
prompt_id: live-backend-instructions-cdd617dbae37
module: context
variant: default
upstream_repository: QwenLM/qwen-code
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: bc8ad53f9559c9c27cb182da55727d8ed524804b
source_path: packages/cli/src/acp-integration/live/live-backend-instructions.ts
source_symbol: LIVE_BACKEND_END_INSTRUCTIONS.2
source_lines:
- 23
- 29
source_permalink: https://github.com/QwenLM/qwen-code/blob/bc8ad53f9559c9c27cb182da55727d8ed524804b/packages/cli/src/acp-integration/live/live-backend-instructions.ts#L23-L29
source_committed_at: '2026-10-31T05:36:12Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:40Z'
extractor_version: 1.0.3
content_sha256: 7808d1d5221be504b7a9dfe06a5b2070816768fac4fb946edd9db7f7ff6b5203
license: Apache-2.0
source_kind: static_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---
<realtime_conversation>
Realtime conversation ended.

Subsequent user input will return to typed text rather than transcript-style text. Do not assume recognition errors or missing punctuation once realtime has ended. Resume normal chat behavior.

Reason: inactive
</realtime_conversation>