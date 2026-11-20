---
agent: codex
prompt_id: exit_interrupted-54cc0e164ea3
module: review
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.171.0
package_name: null
package_version: null
source_ref: rust-v0.171.0
source_commit: ccf9be8cc458bd6b8336fe84d68d8893f2691a5e
source_path: codex-rs/prompts/templates/review/exit_interrupted.xml
source_symbol: document
source_lines:
- 1
- 8
source_permalink: https://github.com/openai/codex/blob/ccf9be8cc458bd6b8336fe84d68d8893f2691a5e/codex-rs/prompts/templates/review/exit_interrupted.xml#L1-L8
source_committed_at: '2026-11-19T23:07:36Z'
release_published_at: '2026-11-20T00:44:47Z'
fetched_at: '2026-11-20T08:06:30Z'
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

