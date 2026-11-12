---
agent: codex
prompt_id: history_message_interrupted-eb5052683d66
module: review
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.167.2
package_name: null
package_version: null
source_ref: rust-v0.167.2
source_commit: ce21072c90d32c40af7a55b60b2fb35c84a43a6a
source_path: codex-rs/core/templates/review/history_message_interrupted.md
source_symbol: document
source_lines:
- 1
- 8
source_permalink: https://github.com/openai/codex/blob/ce21072c90d32c40af7a55b60b2fb35c84a43a6a/codex-rs/core/templates/review/history_message_interrupted.md#L1-L8
source_committed_at: '2026-11-11T20:03:56Z'
release_published_at: '2026-11-11T22:44:46Z'
fetched_at: '2026-11-12T07:58:20Z'
extractor_version: 1.0.3
content_sha256: 034191c75f15338861ce0be2fcf28855833fc5f601b387cbc3c764032507dc86
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
<user_action>
  <context>User initiated a review task, but was interrupted. If user asks about this, tell them to re-initiate a review with `/review` and wait for it to complete.</context>
  <action>review</action>
  <results>
  None.
  </results>
</user_action>

