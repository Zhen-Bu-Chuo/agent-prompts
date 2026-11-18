---
agent: codex
prompt_id: history_message_completed-c076738890a0
module: review
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.170.0
package_name: null
package_version: null
source_ref: rust-v0.170.0
source_commit: 29eb79e9866b3262a777fdf8195c1b9e63684c91
source_path: codex-rs/core/templates/review/history_message_completed.md
source_symbol: document
source_lines:
- 1
- 8
source_permalink: https://github.com/openai/codex/blob/29eb79e9866b3262a777fdf8195c1b9e63684c91/codex-rs/core/templates/review/history_message_completed.md#L1-L8
source_committed_at: '2026-11-18T02:28:28Z'
release_published_at: '2026-11-18T03:40:48Z'
fetched_at: '2026-11-18T08:14:23Z'
extractor_version: 1.0.3
content_sha256: ba3815d1787697a682253f1c18d4618210732abb64263d633b903955ca838d53
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
<user_action>
  <context>User initiated a review task. Here's the full review output from reviewer model. User may select one or more comments to resolve.</context>
  <action>review</action>
  <results>
  {findings}
  </results>
</user_action>

