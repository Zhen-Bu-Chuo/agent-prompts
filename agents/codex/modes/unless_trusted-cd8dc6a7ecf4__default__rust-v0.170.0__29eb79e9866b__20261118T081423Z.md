---
agent: codex
prompt_id: unless_trusted-cd8dc6a7ecf4
module: modes
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.170.0
package_name: null
package_version: null
source_ref: rust-v0.170.0
source_commit: 29eb79e9866b3262a777fdf8195c1b9e63684c91
source_path: codex-rs/prompts/templates/permissions/approval_policy/unless_trusted.md
source_symbol: document
source_lines:
- 1
- 1
source_permalink: https://github.com/openai/codex/blob/29eb79e9866b3262a777fdf8195c1b9e63684c91/codex-rs/prompts/templates/permissions/approval_policy/unless_trusted.md#L1-L1
source_committed_at: '2026-11-18T02:28:28Z'
release_published_at: '2026-11-18T03:40:48Z'
fetched_at: '2026-11-18T08:14:23Z'
extractor_version: 1.0.3
content_sha256: fadec1a060a758b805f227bc5715c7dd3d7d7e2015bd5020c386eca0f3293d10
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
 `approval_policy` is `unless-trusted`: The harness will require user approval before running commands unless an explicit exec policy rule allows them.
