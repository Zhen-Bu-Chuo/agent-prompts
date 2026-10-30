---
agent: codex
prompt_id: read_only-9ae12216082e
module: modes
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.166.0
package_name: null
package_version: null
source_ref: rust-v0.166.0
source_commit: 6ff1e1ca3b30fc8b914720681fcf5fe62e95f856
source_path: codex-rs/prompts/templates/permissions/sandbox_mode/read_only.md
source_symbol: document
source_lines:
- 1
- 1
source_permalink: https://github.com/openai/codex/blob/6ff1e1ca3b30fc8b914720681fcf5fe62e95f856/codex-rs/prompts/templates/permissions/sandbox_mode/read_only.md#L1-L1
source_committed_at: '2026-10-29T17:44:30Z'
release_published_at: '2026-10-29T19:47:53Z'
fetched_at: '2026-10-30T05:29:24Z'
extractor_version: 1.0.3
content_sha256: 509b39f88e6a4f5cb36485ea8b340680c03f27175ba20200b823ec07bc79668d
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Filesystem sandboxing defines which files can be read or written. `sandbox_mode` is `read-only`: The sandbox only permits reading files. Network access is {{ network_access }}.
