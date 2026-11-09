---
agent: hermes
prompt_id: memory_manager-92d5ed0ed51f
module: memory
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: e3b63d99ef01fb7363807f4c51e81536ad2b42b3
source_path: agent/memory_manager.py
source_symbol: module.MemoryManager.add_provider.1
source_lines:
- 288
- 291
source_permalink: https://github.com/NousResearch/hermes-agent/blob/e3b63d99ef01fb7363807f4c51e81536ad2b42b3/agent/memory_manager.py#L288-L291
source_committed_at: '2026-11-09T07:35:04Z'
release_published_at: null
fetched_at: '2026-11-09T07:40:45Z'
extractor_version: 1.0.3
content_sha256: 34b0662d168a5aa2c5d99b7aa24241668a45e97bad410001a58dd88f5d3a8a96
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Rejected memory provider '%s' — external provider '%s' is already registered. Only one external memory provider is allowed at a time. Configure which one via memory.provider in config.yaml.