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
source_commit: aeb5a071069dbd85d85f2c8d44337f16df29d475
source_path: agent/memory_manager.py
source_symbol: module.MemoryManager.initialize_for_agent.message.1
source_lines:
- 945
- 947
source_permalink: https://github.com/NousResearch/hermes-agent/blob/aeb5a071069dbd85d85f2c8d44337f16df29d475/agent/memory_manager.py#L945-L947
source_committed_at: '2026-11-21T07:30:48Z'
release_published_at: null
fetched_at: '2026-11-21T08:01:25Z'
extractor_version: 1.0.3
content_sha256: a510e35a8e5c3358ddcb23dcd7ae84dca527045635bb4144ac4c5cda85c5a5aa
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
⚠ Memory provider {provider.name!r} is disabled for this profile: it handed out the "
                       "provider instance another profile already uses. Built-in memory still works; the "
                       "operator can see why with `hermes logs errors`.