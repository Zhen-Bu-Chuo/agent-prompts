---
agent: codex
prompt_id: read_only-9ae12216082e
module: modes
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.167.2
package_name: null
package_version: null
source_ref: rust-v0.167.2
source_commit: ce21072c90d32c40af7a55b60b2fb35c84a43a6a
source_path: codex-rs/prompts/templates/permissions/sandbox_mode/read_only.md
source_symbol: document
source_lines:
- 1
- 1
source_permalink: https://github.com/openai/codex/blob/ce21072c90d32c40af7a55b60b2fb35c84a43a6a/codex-rs/prompts/templates/permissions/sandbox_mode/read_only.md#L1-L1
source_committed_at: '2026-11-11T20:03:56Z'
release_published_at: '2026-11-11T22:44:46Z'
fetched_at: '2026-11-12T07:58:20Z'
extractor_version: 1.0.3
content_sha256: 509b39f88e6a4f5cb36485ea8b340680c03f27175ba20200b823ec07bc79668d
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Filesystem sandboxing defines which files can be read or written. `sandbox_mode` is `read-only`: The sandbox only permits reading files. Network access is {{ network_access }}.
