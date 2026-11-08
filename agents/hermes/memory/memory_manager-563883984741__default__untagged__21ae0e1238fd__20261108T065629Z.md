---
agent: hermes
prompt_id: memory_manager-563883984741
module: memory
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 21ae0e1238fdf466fa52a85a6ebf75d6899e49da
source_path: agent/memory_manager.py
source_symbol: module.MemoryManager._drain_sync_executor.1
source_lines:
- 931
- 932
source_permalink: https://github.com/NousResearch/hermes-agent/blob/21ae0e1238fdf466fa52a85a6ebf75d6899e49da/agent/memory_manager.py#L931-L932
source_committed_at: '2026-11-08T03:38:20Z'
release_published_at: null
fetched_at: '2026-11-08T06:56:29Z'
extractor_version: 1.0.3
content_sha256: e4c3748513ddfcd42622e969c9062d64766161f9747b3f914e8e09b6dda75dab
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Memory shutdown drain timed out after %.2fs; abandoning %d queued memory write(s) and %d queued prefetch(es); %d active task(s) remain detached