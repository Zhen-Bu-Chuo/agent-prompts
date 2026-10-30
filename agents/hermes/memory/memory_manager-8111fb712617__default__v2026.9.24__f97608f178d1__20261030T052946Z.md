---
agent: hermes
prompt_id: memory_manager-8111fb712617
module: memory
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: v2026.9.24
package_name: null
package_version: null
source_ref: v2026.9.24
source_commit: f97608f178d1ffeca59860195ab7da295f7c8e5f
source_path: agent/memory_manager.py
source_symbol: module.inject_memory_provider_tools.1
source_lines:
- 130
- 133
source_permalink: https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/memory_manager.py#L130-L133
source_committed_at: '2026-09-24T10:08:47Z'
release_published_at: '2026-09-24T10:09:38Z'
fetched_at: '2026-10-30T05:29:46Z'
extractor_version: 1.0.3
content_sha256: 4bd3a7ed4198cf978fa56262c7979bf9a45d15a5a3c5da959c1cc74fd177ccb7
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Memory provider(s) %s configured but the 'memory' toolset is gated off for this session (platform_toolsets / agent.disabled_toolsets) — provider tools and system-prompt block are both withheld.