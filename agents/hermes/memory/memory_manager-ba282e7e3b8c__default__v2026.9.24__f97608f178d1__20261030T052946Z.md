---
agent: hermes
prompt_id: memory_manager-ba282e7e3b8c
module: memory
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: v2026.9.24
package_name: null
package_version: null
source_ref: v2026.9.24
source_commit: f97608f178d1ffeca59860195ab7da295f7c8e5f
source_path: agent/memory_manager.py
source_symbol: module.MemoryManager.add_provider.2
source_lines:
- 416
- 418
source_permalink: https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/memory_manager.py#L416-L418
source_committed_at: '2026-09-24T10:08:47Z'
release_published_at: '2026-09-24T10:09:38Z'
fetched_at: '2026-10-30T05:29:46Z'
extractor_version: 1.0.3
content_sha256: d0dd7a0b6b9a6e63b32f5ad9da00de2717bb53ea3bb20fed789de4b26e74a321
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Memory provider '%s' tool '%s' shadows a reserved core tool name; registration ignored. Core tools always win — rename the provider's tool to something unique.