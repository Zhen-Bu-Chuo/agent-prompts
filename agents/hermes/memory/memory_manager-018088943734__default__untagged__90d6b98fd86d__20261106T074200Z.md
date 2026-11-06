---
agent: hermes
prompt_id: memory_manager-018088943734
module: memory
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 90d6b98fd86d20981ee06ddd5b7d93e4320f26a4
source_path: agent/memory_manager.py
source_symbol: module.MemoryManager._prefetch_provider.1
source_lines:
- 407
- 408
source_permalink: https://github.com/NousResearch/hermes-agent/blob/90d6b98fd86d20981ee06ddd5b7d93e4320f26a4/agent/memory_manager.py#L407-L408
source_committed_at: '2026-11-06T07:12:42Z'
release_published_at: null
fetched_at: '2026-11-06T07:42:00Z'
extractor_version: 1.0.3
content_sha256: aa1c48940a7a460afa552261e59b1dd0485a50d6a91d6e6bc3d7e000e1a9e5fa
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Memory provider '%s' prefetch timed out after %.1fs; the call keeps running in the background (later turns may skip it while the provider stays stuck)