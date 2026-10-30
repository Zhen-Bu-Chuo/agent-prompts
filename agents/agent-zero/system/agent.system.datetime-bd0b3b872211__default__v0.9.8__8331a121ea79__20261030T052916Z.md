---
agent: agent-zero
prompt_id: agent.system.datetime-bd0b3b872211
module: system
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.datetime.md
source_symbol: document
source_lines:
- 1
- 3
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.datetime.md#L1-L3
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: ec4710a9d9c24a378558deae0f8d0686ee3ac74ed30cd5ad9651331bfe9d8dcc
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
# Current system date and time of user
- current datetime: {{date_time}}
- rely on this info always up to date
