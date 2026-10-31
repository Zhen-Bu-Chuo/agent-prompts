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
source_commit: adecc4024456b387b1518813b90bd60c82b51287
source_path: agent/memory_manager.py
source_symbol: module.MemoryManager._prefetch_provider.1
source_lines:
- 391
- 392
source_permalink: https://github.com/NousResearch/hermes-agent/blob/adecc4024456b387b1518813b90bd60c82b51287/agent/memory_manager.py#L391-L392
source_committed_at: '2026-10-31T06:03:57Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:29Z'
extractor_version: 1.0.3
content_sha256: aa1c48940a7a460afa552261e59b1dd0485a50d6a91d6e6bc3d7e000e1a9e5fa
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Memory provider '%s' prefetch timed out after %.1fs; the call keeps running in the background (later turns may skip it while the provider stays stuck)