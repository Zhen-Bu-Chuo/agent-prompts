---
agent: hermes
prompt_id: memory_manager-018088943734
module: memory
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: v2026.9.24
package_name: null
package_version: null
source_ref: v2026.9.24
source_commit: f97608f178d1ffeca59860195ab7da295f7c8e5f
source_path: agent/memory_manager.py
source_symbol: module.MemoryManager._prefetch_provider.1
source_lines:
- 483
- 484
source_permalink: https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/memory_manager.py#L483-L484
source_committed_at: '2026-09-24T10:08:47Z'
release_published_at: '2026-09-24T10:09:38Z'
fetched_at: '2026-10-30T05:29:46Z'
extractor_version: 1.0.3
content_sha256: e1105097931396184f6f9ef522fef556bae999b50dcf75ac940bd72761d5e9df
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Memory provider '%s' prefetch timed out after %.1fs; skipping it until the stuck call returns