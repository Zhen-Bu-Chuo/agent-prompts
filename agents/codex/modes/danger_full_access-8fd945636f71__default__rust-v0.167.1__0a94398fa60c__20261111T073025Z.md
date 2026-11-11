---
agent: codex
prompt_id: danger_full_access-8fd945636f71
module: modes
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.167.1
package_name: null
package_version: null
source_ref: rust-v0.167.1
source_commit: 0a94398fa60c4fac0e7659e4213a0a36e613dd46
source_path: codex-rs/prompts/templates/permissions/sandbox_mode/danger_full_access.md
source_symbol: document
source_lines:
- 1
- 1
source_permalink: https://github.com/openai/codex/blob/0a94398fa60c4fac0e7659e4213a0a36e613dd46/codex-rs/prompts/templates/permissions/sandbox_mode/danger_full_access.md#L1-L1
source_committed_at: '2026-11-10T18:02:25Z'
release_published_at: '2026-11-10T21:32:01Z'
fetched_at: '2026-11-11T07:30:25Z'
extractor_version: 1.0.3
content_sha256: 0d887cb1eaba21a6cade67ab958a6ffee00f671c46f8cf29c83706e397942dbf
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Filesystem sandboxing defines which files can be read or written. `sandbox_mode` is `danger-full-access`: No filesystem sandboxing - all commands are permitted. Network access is {{ network_access }}.
