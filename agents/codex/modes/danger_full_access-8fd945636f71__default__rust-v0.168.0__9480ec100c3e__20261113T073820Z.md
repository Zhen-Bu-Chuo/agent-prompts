---
agent: codex
prompt_id: danger_full_access-8fd945636f71
module: modes
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.168.0
package_name: null
package_version: null
source_ref: rust-v0.168.0
source_commit: 9480ec100c3edee9fc69172e8e80a4730444094d
source_path: codex-rs/prompts/templates/permissions/sandbox_mode/danger_full_access.md
source_symbol: document
source_lines:
- 1
- 1
source_permalink: https://github.com/openai/codex/blob/9480ec100c3edee9fc69172e8e80a4730444094d/codex-rs/prompts/templates/permissions/sandbox_mode/danger_full_access.md#L1-L1
source_committed_at: '2026-11-12T21:29:06Z'
release_published_at: '2026-11-13T03:54:29Z'
fetched_at: '2026-11-13T07:38:20Z'
extractor_version: 1.0.3
content_sha256: 0d887cb1eaba21a6cade67ab958a6ffee00f671c46f8cf29c83706e397942dbf
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Filesystem sandboxing defines which files can be read or written. `sandbox_mode` is `danger-full-access`: No filesystem sandboxing - all commands are permitted. Network access is {{ network_access }}.
