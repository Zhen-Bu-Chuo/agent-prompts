---
agent: codex
prompt_id: unless_trusted-cd8dc6a7ecf4
module: modes
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.171.0
package_name: null
package_version: null
source_ref: rust-v0.171.0
source_commit: ccf9be8cc458bd6b8336fe84d68d8893f2691a5e
source_path: codex-rs/prompts/templates/permissions/approval_policy/unless_trusted.md
source_symbol: document
source_lines:
- 1
- 1
source_permalink: https://github.com/openai/codex/blob/ccf9be8cc458bd6b8336fe84d68d8893f2691a5e/codex-rs/prompts/templates/permissions/approval_policy/unless_trusted.md#L1-L1
source_committed_at: '2026-11-19T23:07:36Z'
release_published_at: '2026-11-20T00:44:47Z'
fetched_at: '2026-11-20T08:06:30Z'
extractor_version: 1.0.3
content_sha256: fadec1a060a758b805f227bc5715c7dd3d7d7e2015bd5020c386eca0f3293d10
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
 `approval_policy` is `unless-trusted`: The harness will require user approval before running commands unless an explicit exec policy rule allows them.
