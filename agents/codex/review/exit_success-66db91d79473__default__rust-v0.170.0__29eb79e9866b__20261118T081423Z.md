---
agent: codex
prompt_id: exit_success-66db91d79473
module: review
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.170.0
package_name: null
package_version: null
source_ref: rust-v0.170.0
source_commit: 29eb79e9866b3262a777fdf8195c1b9e63684c91
source_path: codex-rs/prompts/templates/review/exit_success.xml
source_symbol: document
source_lines:
- 1
- 7
source_permalink: https://github.com/openai/codex/blob/29eb79e9866b3262a777fdf8195c1b9e63684c91/codex-rs/prompts/templates/review/exit_success.xml#L1-L7
source_committed_at: '2026-11-18T02:28:28Z'
release_published_at: '2026-11-18T03:40:48Z'
fetched_at: '2026-11-18T08:14:23Z'
extractor_version: 1.0.3
content_sha256: 87ce1bcbc0f1aee3fcba4fedd35775eccf4a640352b071ead206d0b4ff286559
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
<user_action>
  <context>User initiated a review task. Here's the full review output from reviewer model. User may select one or more comments to resolve.</context>
  <action>review</action>
  <results>
  {{results}}
  </results>
  </user_action>
