---
agent: codex
prompt_id: exit_success-66db91d79473
module: review
variant: default
upstream_repository: openai/codex
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: c320b5c69e74755a6efd4075ff01d4524ad6a4bf
source_path: codex-rs/prompts/templates/review/exit_success.xml
source_symbol: document
source_lines:
- 1
- 7
source_permalink: https://github.com/openai/codex/blob/c320b5c69e74755a6efd4075ff01d4524ad6a4bf/codex-rs/prompts/templates/review/exit_success.xml#L1-L7
source_committed_at: '2026-11-11T07:24:38Z'
release_published_at: null
fetched_at: '2026-11-11T07:30:25Z'
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
