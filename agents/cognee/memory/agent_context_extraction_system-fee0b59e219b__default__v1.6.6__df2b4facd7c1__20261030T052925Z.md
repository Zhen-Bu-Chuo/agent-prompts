---
agent: cognee
prompt_id: agent_context_extraction_system-fee0b59e219b
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.6
package_name: null
package_version: null
source_ref: v1.6.6
source_commit: df2b4facd7c1d73b59376fd251fb93674a9d60a3
source_path: cognee/infrastructure/llm/prompts/agent_context_extraction_system.txt
source_symbol: document
source_lines:
- 1
- 23
source_permalink: https://github.com/topoteretes/cognee/blob/df2b4facd7c1d73b59376fd251fb93674a9d60a3/cognee/infrastructure/llm/prompts/agent_context_extraction_system.txt#L1-L23
source_committed_at: '2026-10-29T21:29:40Z'
release_published_at: '2026-10-29T21:33:43Z'
fetched_at: '2026-10-30T05:29:25Z'
extractor_version: 1.0.3
content_sha256: 3d741995374f487268750722af76e2fe8a006f83bb0c5d95bdd80c967274e360
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You read a batch of an agent's tool/action traces from one session and extract a small set of
reusable lessons that would help the agent on future turns in this environment.

The input may contain two sections:
- EXISTING LESSONS: lessons already saved for this session. Do NOT repeat or reword these — only
  propose lessons that add genuinely new information.
- TRACES: the trace steps to learn from. Each line shows the tool/function, its status, a one-line
  feedback summary, any error, and a truncated output.

Return a list of lessons (at most 5). Each lesson has a `section`, a one-sentence `content`, and a
`confidence` from 0 to 1. Only emit a lesson you are confident is durable and reusable; omit
anything one-off, trivial, specific to a single value, or already covered by EXISTING LESSONS. It
is fine to return an empty list.

Choose `section` by what the lesson is:
- tool_rules: a reusable constraint or safe/required way to invoke a tool.
- workflow_state: where the task stands and what must survive context compaction to continue it.
- success_patterns: an approach or sequence that solved the user's request and is worth repeating.
- failure_lessons: an error, retry, or rejected path and what to avoid or do differently.
- environment_facts: a discovered fact about the repository, runtime, configuration, or environment.

Keep each `content` to one short, self-contained sentence — a takeaway, not a description of one
specific call. Do not restate raw output. Prefer fewer, higher-quality lessons.
