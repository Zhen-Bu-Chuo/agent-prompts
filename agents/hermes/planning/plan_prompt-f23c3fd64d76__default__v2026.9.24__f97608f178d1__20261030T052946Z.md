---
agent: hermes
prompt_id: plan_prompt-f23c3fd64d76
module: planning
variant: default
upstream_repository: NousResearch/hermes-agent
upstream_version: v2026.9.24
package_name: null
package_version: null
source_ref: v2026.9.24
source_commit: f97608f178d1ffeca59860195ab7da295f7c8e5f
source_path: agent/plan_prompt.py
source_symbol: module._PLAN_CRAFT.1
source_lines:
- 28
- 57
source_permalink: https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/plan_prompt.py#L28-L57
source_committed_at: '2026-09-24T10:08:47Z'
release_published_at: '2026-09-24T10:09:38Z'
fetched_at: '2026-10-30T05:29:46Z'
extractor_version: 1.0.3
content_sha256: a407672126643b1545ddfb2d45eb2f67cad8e278c204c4265036c5d96ce6eeb9
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Write the plan for an implementer with zero context for the codebase and
questionable taste. A good plan makes implementation obvious — if someone has
to guess, the plan is incomplete.

Structure (include the sections that are relevant):
- Goal — one sentence.
- Current context / assumptions.
- Architecture / proposed approach — 2-3 sentences.
- Step-by-step tasks. Each task is bite-sized (2-5 minutes of focused work),
  names exact file paths (`src/models/user.py`, not "the model file"),
  includes complete copy-pasteable code where code is needed, and exact
  commands with expected output for verification.
- Tests / validation — for code tasks, follow the TDD cycle per task: write
  the failing test, run it to verify failure, implement minimally, run to
  verify pass, commit.
- Risks, tradeoffs, and open questions.

Principles: DRY, YAGNI, TDD, frequent commits. Avoid vague tasks ("add
authentication"), incomplete code ("add validation here"), and unverifiable
steps ("test it works" — instead: the exact command and its expected output).

Interaction style:
- If the request is clear enough, write the plan directly.
- If it is genuinely underspecified, ask a brief clarifying question instead
  of guessing.
- After saving the plan, reply briefly with what you planned and the saved
  path, and offer to execute it (e.g. via subagent-driven development) —
  but do not start executing in this turn.
