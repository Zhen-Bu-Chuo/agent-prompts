---
agent: codex
prompt_id: read_only-9ae12216082e
module: modes
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.170.0
package_name: null
package_version: null
source_ref: rust-v0.170.0
source_commit: 29eb79e9866b3262a777fdf8195c1b9e63684c91
source_path: codex-rs/prompts/templates/permissions/sandbox_mode/read_only.md
source_symbol: document
source_lines:
- 1
- 1
source_permalink: https://github.com/openai/codex/blob/29eb79e9866b3262a777fdf8195c1b9e63684c91/codex-rs/prompts/templates/permissions/sandbox_mode/read_only.md#L1-L1
source_committed_at: '2026-11-18T02:28:28Z'
release_published_at: '2026-11-18T03:40:48Z'
fetched_at: '2026-11-18T08:14:23Z'
extractor_version: 1.0.3
content_sha256: 509b39f88e6a4f5cb36485ea8b340680c03f27175ba20200b823ec07bc79668d
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Filesystem sandboxing defines which files can be read or written. `sandbox_mode` is `read-only`: The sandbox only permits reading files. Network access is {{ network_access }}.
