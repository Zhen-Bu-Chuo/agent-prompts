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
source_commit: 39ca68b38f96b006ea62dcb196cabcd70d2da509
source_path: agent/memory_manager.py
source_symbol: module.MemoryManager.add_provider.1
source_lines:
- 290
- 293
source_permalink: https://github.com/NousResearch/hermes-agent/blob/39ca68b38f96b006ea62dcb196cabcd70d2da509/agent/memory_manager.py#L290-L293
source_committed_at: '2026-11-24T10:24:57Z'
release_published_at: null
fetched_at: '2026-11-24T10:42:27Z'
extractor_version: 1.0.3
content_sha256: 34b0662d168a5aa2c5d99b7aa24241668a45e97bad410001a58dd88f5d3a8a96
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Rejected memory provider '%s' — external provider '%s' is already registered. Only one external memory provider is allowed at a time. Configure which one via memory.provider in config.yaml.