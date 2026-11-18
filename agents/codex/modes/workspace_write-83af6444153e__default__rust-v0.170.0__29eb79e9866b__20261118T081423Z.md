---
agent: codex
prompt_id: workspace_write-83af6444153e
module: modes
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.170.0
package_name: null
package_version: null
source_ref: rust-v0.170.0
source_commit: 29eb79e9866b3262a777fdf8195c1b9e63684c91
source_path: codex-rs/prompts/templates/permissions/sandbox_mode/workspace_write.md
source_symbol: document
source_lines:
- 1
- 1
source_permalink: https://github.com/openai/codex/blob/29eb79e9866b3262a777fdf8195c1b9e63684c91/codex-rs/prompts/templates/permissions/sandbox_mode/workspace_write.md#L1-L1
source_committed_at: '2026-11-18T02:28:28Z'
release_published_at: '2026-11-18T03:40:48Z'
fetched_at: '2026-11-18T08:14:23Z'
extractor_version: 1.0.3
content_sha256: 763661195d613a48173638af6227d480d70ab0a6898d3a81ff075155e82f7555
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Filesystem sandboxing defines which files can be read or written. `sandbox_mode` is `workspace-write`: The sandbox permits reading files, and editing files in `cwd` and `writable_roots`. Editing files in other directories requires approval. Network access is {{ network_access }}.
