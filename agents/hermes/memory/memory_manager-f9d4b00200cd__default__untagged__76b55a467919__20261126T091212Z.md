---
agent: hermes
prompt_id: memory_manager-f9d4b00200cd
module: memory
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 76b55a46791914921da552c91a2264569dca2055
source_path: agent/memory_manager.py
source_symbol: module.MemoryManager._call_unless_stalled.1
source_lines:
- 549
- 550
source_permalink: https://github.com/NousResearch/hermes-agent/blob/76b55a46791914921da552c91a2264569dca2055/agent/memory_manager.py#L549-L550
source_committed_at: '2026-11-26T08:37:23Z'
release_published_at: null
fetched_at: '2026-11-26T09:12:12Z'
extractor_version: 1.0.3
content_sha256: 1ec89c0b8bec3968c08b1c6f7a51bba343e4ad05fb0dbd30524fa4bafb14710e
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Memory provider '%s' has %d background calls stuck for over %.0fs (%d in flight); skipping its sync/prefetch until it recovers (%d skipped)