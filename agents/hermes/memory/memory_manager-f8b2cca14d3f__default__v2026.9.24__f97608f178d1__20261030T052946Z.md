---
agent: hermes
prompt_id: memory_manager-f8b2cca14d3f
module: memory
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: v2026.9.24
package_name: null
package_version: null
source_ref: v2026.9.24
source_commit: f97608f178d1ffeca59860195ab7da295f7c8e5f
source_path: agent/memory_manager.py
source_symbol: module.inject_memory_provider_tools.2
source_lines:
- 150
- 151
source_permalink: https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/memory_manager.py#L150-L151
source_committed_at: '2026-09-24T10:08:47Z'
release_published_at: '2026-09-24T10:09:38Z'
fetched_at: '2026-10-30T05:29:46Z'
extractor_version: 1.0.3
content_sha256: 99e6ea2283fc11579267ed5fc09da9c777d85690cc61a0589dd01af6a88fd3c2
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Memory provider returned a tool schema with no resolvable name; skipping to avoid poisoning the request (%r)