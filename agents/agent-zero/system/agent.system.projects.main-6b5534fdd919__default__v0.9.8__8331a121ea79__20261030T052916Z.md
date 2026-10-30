---
agent: agent-zero
prompt_id: agent.system.projects.main-6b5534fdd919
module: system
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.projects.main.md
source_symbol: document
source_lines:
- 1
- 5
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.projects.main.md#L1-L5
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: 60a6dceb9b89a39fe6499c2460bfd72367c626a2b8a0518e570f211b7e5996ad
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
# Projects
- user can create and activate projects
- projects have work folder in /usr/projects/<name> and instructions and config in /usr/projects/<name>/.a0proj
- when activated agent works in project follows project instructions
- agent cannot manipulate or switch projects