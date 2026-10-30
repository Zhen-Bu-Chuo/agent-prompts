---
agent: agent-zero
prompt_id: agent.system.main-4c77dea6cebb
module: system
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.main.md
source_symbol: document
source_lines:
- 1
- 11
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.main.md#L1-L11
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: a6d59b4285be57a60a6e70c3a2694b02b92c783f610d6daf0a2b086aef3a0577
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
# Agent Zero System Manual

{{ include "agent.system.main.role.md" }}

{{ include "agent.system.main.environment.md" }}

{{ include "agent.system.main.communication.md" }}

{{ include "agent.system.main.solving.md" }}

{{ include "agent.system.main.tips.md" }}
