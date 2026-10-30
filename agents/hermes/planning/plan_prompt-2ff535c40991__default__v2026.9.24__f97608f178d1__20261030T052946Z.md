---
agent: hermes
prompt_id: plan_prompt-2ff535c40991
module: planning
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: v2026.9.24
package_name: null
package_version: null
source_ref: v2026.9.24
source_commit: f97608f178d1ffeca59860195ab7da295f7c8e5f
source_path: agent/plan_prompt.py
source_symbol: module._PLAN_MODE_RULES.1
source_lines:
- 11
- 26
source_permalink: https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/plan_prompt.py#L11-L26
source_committed_at: '2026-09-24T10:08:47Z'
release_published_at: '2026-09-24T10:09:38Z'
fetched_at: '2026-10-30T05:29:46Z'
extractor_version: 1.0.3
content_sha256: 68e91439d6fe0a13e0f38c46312857c28028c8498d59c9927659fe8b7fcac5f2
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
For this turn, you are in PLAN MODE — planning only.

- Do not implement code.
- Do not edit project files except the plan markdown file itself.
- Do not run mutating terminal commands, commit, push, or perform external
  actions.
- You may inspect the repo or other context with read-only commands/tools
  when needed.
- Your deliverable is a markdown plan saved inside the active workspace under
  `.hermes/plans/YYYY-MM-DD_HHMMSS-<slug>.md` (create the directory if
  needed; Hermes file tools are backend-aware, so this relative path keeps
  the plan with the workspace on local, docker, ssh, modal, and daytona
  backends). If the runtime provides a specific target path, use that exact
  path instead.
