---
agent: agent-zero
prompt_id: agent.system.projects.active-e9c7189f7000
module: system
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.projects.active.md
source_symbol: document
source_lines:
- 1
- 13
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.projects.active.md#L1-L13
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: 91700f9558bd0f719b0dfdbc68b17bd12aebc5d5846db8bd39fb48126d4f92c1
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
## Active project
Path: {{project_path}}
Title: {{project_name}}
Description: {{project_description}}
{% if project_git_url %}Git URL: {{project_git_url}}{% endif %}


### Important project instructions MUST follow
- always work inside {{project_path}} directory
- do not rename project directory do not change meta files in .a0proj folder
- cleanup when code accidentaly creates files outside move them

{{project_instructions}}