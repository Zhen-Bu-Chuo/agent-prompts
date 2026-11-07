---
agent: codex
prompt_id: unless_trusted-cd8dc6a7ecf4
module: modes
variant: default
upstream_repository: openai/codex
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: f4275a2a2e6a50d030280439ba161305b324c851
source_path: codex-rs/prompts/templates/permissions/approval_policy/unless_trusted.md
source_symbol: document
source_lines:
- 1
- 1
source_permalink: https://github.com/openai/codex/blob/f4275a2a2e6a50d030280439ba161305b324c851/codex-rs/prompts/templates/permissions/approval_policy/unless_trusted.md#L1-L1
source_committed_at: '2026-11-07T06:32:12Z'
release_published_at: null
fetched_at: '2026-11-07T06:51:14Z'
extractor_version: 1.0.3
content_sha256: fadec1a060a758b805f227bc5715c7dd3d7d7e2015bd5020c386eca0f3293d10
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
 `approval_policy` is `unless-trusted`: The harness will require user approval before running commands unless an explicit exec policy rule allows them.
