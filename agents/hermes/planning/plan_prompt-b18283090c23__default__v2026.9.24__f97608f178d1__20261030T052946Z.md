---
agent: hermes
prompt_id: plan_prompt-b18283090c23
module: planning
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: v2026.9.24
package_name: null
package_version: null
source_ref: v2026.9.24
source_commit: f97608f178d1ffeca59860195ab7da295f7c8e5f
source_path: agent/plan_prompt.py
source_symbol: module.build_plan_prompt.task_block.1
source_lines:
- 67
- 69
source_permalink: https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/plan_prompt.py#L67-L69
source_committed_at: '2026-09-24T10:08:47Z'
release_published_at: '2026-09-24T10:09:38Z'
fetched_at: '2026-10-30T05:29:46Z'
extractor_version: 1.0.3
content_sha256: 5be4e2796570818e6a28b95582954fc5190a7f5e0874228058af46f3a9ee00cf
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
No explicit task was given with /plan — infer the task from the current conversation context (the thing we have been discussing or working toward). If the conversation does not imply a task, ask a brief clarifying question.
