---
agent: codex
prompt_id: history_message_interrupted-eb5052683d66
module: review
variant: default
upstream_repository: openai/codex
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: c320b5c69e74755a6efd4075ff01d4524ad6a4bf
source_path: codex-rs/core/templates/review/history_message_interrupted.md
source_symbol: document
source_lines:
- 1
- 8
source_permalink: https://github.com/openai/codex/blob/c320b5c69e74755a6efd4075ff01d4524ad6a4bf/codex-rs/core/templates/review/history_message_interrupted.md#L1-L8
source_committed_at: '2026-11-11T07:24:38Z'
release_published_at: null
fetched_at: '2026-11-11T07:30:25Z'
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

