---
agent: codex
prompt_id: history_message_completed-c076738890a0
module: review
variant: default
upstream_repository: openai/codex
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: a09812981de703f18f38015cd5d500ab373f616c
source_path: codex-rs/core/templates/review/history_message_completed.md
source_symbol: document
source_lines:
- 1
- 8
source_permalink: https://github.com/openai/codex/blob/a09812981de703f18f38015cd5d500ab373f616c/codex-rs/core/templates/review/history_message_completed.md#L1-L8
source_committed_at: '2026-11-01T23:27:06Z'
release_published_at: null
fetched_at: '2026-11-02T07:17:42Z'
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

