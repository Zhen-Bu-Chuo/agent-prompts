---
agent: hermes
prompt_id: plan_prompt-2ff535c40991
module: planning
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 90d6b98fd86d20981ee06ddd5b7d93e4320f26a4
source_path: agent/plan_prompt.py
source_symbol: module._PLAN_MODE_RULES.1
source_lines:
- 11
- 26
source_permalink: https://github.com/NousResearch/hermes-agent/blob/90d6b98fd86d20981ee06ddd5b7d93e4320f26a4/agent/plan_prompt.py#L11-L26
source_committed_at: '2026-11-06T07:12:42Z'
release_published_at: null
fetched_at: '2026-11-06T07:42:00Z'
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
