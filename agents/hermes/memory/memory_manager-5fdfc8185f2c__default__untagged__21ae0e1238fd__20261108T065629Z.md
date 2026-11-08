---
agent: hermes
prompt_id: memory_manager-5fdfc8185f2c
module: memory
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 21ae0e1238fdf466fa52a85a6ebf75d6899e49da
source_path: agent/memory_manager.py
source_symbol: module.MemoryManager.initialize_for_agent.message.1
source_lines:
- 943
- 945
source_permalink: https://github.com/NousResearch/hermes-agent/blob/21ae0e1238fdf466fa52a85a6ebf75d6899e49da/agent/memory_manager.py#L943-L945
source_committed_at: '2026-11-08T03:38:20Z'
release_published_at: null
fetched_at: '2026-11-08T06:56:29Z'
extractor_version: 1.0.3
content_sha256: a510e35a8e5c3358ddcb23dcd7ae84dca527045635bb4144ac4c5cda85c5a5aa
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
⚠ Memory provider {provider.name!r} is disabled for this profile: it handed out the "
                       "provider instance another profile already uses. Built-in memory still works; the "
                       "operator can see why with `hermes logs errors`.