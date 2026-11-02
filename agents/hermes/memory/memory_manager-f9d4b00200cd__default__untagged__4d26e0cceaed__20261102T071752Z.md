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
source_commit: 4d26e0cceaed0a08ede833caec0ec6d6ca77a4b8
source_path: agent/memory_manager.py
source_symbol: module.MemoryManager._call_unless_stalled.1
source_lines:
- 530
- 531
source_permalink: https://github.com/NousResearch/hermes-agent/blob/4d26e0cceaed0a08ede833caec0ec6d6ca77a4b8/agent/memory_manager.py#L530-L531
source_committed_at: '2026-11-02T06:36:15Z'
release_published_at: null
fetched_at: '2026-11-02T07:17:52Z'
extractor_version: 1.0.3
content_sha256: 1ec89c0b8bec3968c08b1c6f7a51bba343e4ad05fb0dbd30524fa4bafb14710e
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Memory provider '%s' has %d background calls stuck for over %.0fs (%d in flight); skipping its sync/prefetch until it recovers (%d skipped)