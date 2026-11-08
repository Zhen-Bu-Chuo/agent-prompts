---
agent: hermes
prompt_id: plan_prompt-b18283090c23
module: planning
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 21ae0e1238fdf466fa52a85a6ebf75d6899e49da
source_path: agent/plan_prompt.py
source_symbol: module.build_plan_prompt.task_block.1
source_lines:
- 67
- 69
source_permalink: https://github.com/NousResearch/hermes-agent/blob/21ae0e1238fdf466fa52a85a6ebf75d6899e49da/agent/plan_prompt.py#L67-L69
source_committed_at: '2026-11-08T03:38:20Z'
release_published_at: null
fetched_at: '2026-11-08T06:56:29Z'
extractor_version: 1.0.3
content_sha256: 5be4e2796570818e6a28b95582954fc5190a7f5e0874228058af46f3a9ee00cf
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
No explicit task was given with /plan — infer the task from the current conversation context (the thing we have been discussing or working toward). If the conversation does not imply a task, ask a brief clarifying question.
