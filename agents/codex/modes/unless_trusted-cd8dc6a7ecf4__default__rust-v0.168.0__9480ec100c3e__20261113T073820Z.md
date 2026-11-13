---
agent: codex
prompt_id: unless_trusted-cd8dc6a7ecf4
module: modes
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.168.0
package_name: null
package_version: null
source_ref: rust-v0.168.0
source_commit: 9480ec100c3edee9fc69172e8e80a4730444094d
source_path: codex-rs/prompts/templates/permissions/approval_policy/unless_trusted.md
source_symbol: document
source_lines:
- 1
- 1
source_permalink: https://github.com/openai/codex/blob/9480ec100c3edee9fc69172e8e80a4730444094d/codex-rs/prompts/templates/permissions/approval_policy/unless_trusted.md#L1-L1
source_committed_at: '2026-11-12T21:29:06Z'
release_published_at: '2026-11-13T03:54:29Z'
fetched_at: '2026-11-13T07:38:20Z'
extractor_version: 1.0.3
content_sha256: fadec1a060a758b805f227bc5715c7dd3d7d7e2015bd5020c386eca0f3293d10
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
 `approval_policy` is `unless-trusted`: The harness will require user approval before running commands unless an explicit exec policy rule allows them.
