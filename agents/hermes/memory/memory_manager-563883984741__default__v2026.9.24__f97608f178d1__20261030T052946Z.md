---
agent: hermes
prompt_id: memory_manager-563883984741
module: memory
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: v2026.9.24
package_name: null
package_version: null
source_ref: v2026.9.24
source_commit: f97608f178d1ffeca59860195ab7da295f7c8e5f
source_path: agent/memory_manager.py
source_symbol: module.MemoryManager._drain_sync_executor.1
source_lines:
- 891
- 892
source_permalink: https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/memory_manager.py#L891-L892
source_committed_at: '2026-09-24T10:08:47Z'
release_published_at: '2026-09-24T10:09:38Z'
fetched_at: '2026-10-30T05:29:46Z'
extractor_version: 1.0.3
content_sha256: e4c3748513ddfcd42622e969c9062d64766161f9747b3f914e8e09b6dda75dab
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Memory shutdown drain timed out after %.2fs; abandoning %d queued memory write(s) and %d queued prefetch(es); %d active task(s) remain detached