---
agent: hermes
prompt_id: memory_manager-ba282e7e3b8c
module: memory
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: e3b63d99ef01fb7363807f4c51e81536ad2b42b3
source_path: agent/memory_manager.py
source_symbol: module.MemoryManager.add_provider.2
source_lines:
- 329
- 331
source_permalink: https://github.com/NousResearch/hermes-agent/blob/e3b63d99ef01fb7363807f4c51e81536ad2b42b3/agent/memory_manager.py#L329-L331
source_committed_at: '2026-11-09T07:35:04Z'
release_published_at: null
fetched_at: '2026-11-09T07:40:45Z'
extractor_version: 1.0.3
content_sha256: d0dd7a0b6b9a6e63b32f5ad9da00de2717bb53ea3bb20fed789de4b26e74a321
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Memory provider '%s' tool '%s' shadows a reserved core tool name; registration ignored. Core tools always win — rename the provider's tool to something unique.