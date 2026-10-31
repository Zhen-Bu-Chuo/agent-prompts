---
agent: codex
prompt_id: danger_full_access-8fd945636f71
module: modes
variant: default
upstream_repository: openai/codex
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 67f0994b532b8740f14b5b738af7b7b2a915b1d6
source_path: codex-rs/prompts/templates/permissions/sandbox_mode/danger_full_access.md
source_symbol: document
source_lines:
- 1
- 1
source_permalink: https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/codex-rs/prompts/templates/permissions/sandbox_mode/danger_full_access.md#L1-L1
source_committed_at: '2026-10-31T00:12:17Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
extractor_version: 1.0.3
content_sha256: 0d887cb1eaba21a6cade67ab958a6ffee00f671c46f8cf29c83706e397942dbf
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Filesystem sandboxing defines which files can be read or written. `sandbox_mode` is `danger-full-access`: No filesystem sandboxing - all commands are permitted. Network access is {{ network_access }}.
