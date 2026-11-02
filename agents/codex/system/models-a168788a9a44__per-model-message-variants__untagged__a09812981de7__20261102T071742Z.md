---
agent: codex
prompt_id: models-a168788a9a44
module: system
variant: per-model-message-variants
upstream_repository: openai/codex
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: a09812981de703f18f38015cd5d500ab373f616c
source_path: codex-rs/models-manager/models.json
source_symbol: models.0.model_messages.token_budget.auto_compact_fallback_prompt
source_lines:
- 1
- 1779
source_permalink: https://github.com/openai/codex/blob/a09812981de703f18f38015cd5d500ab373f616c/codex-rs/models-manager/models.json#L1-L1779
source_committed_at: '2026-11-01T23:27:06Z'
release_published_at: null
fetched_at: '2026-11-02T07:17:42Z'
extractor_version: 1.0.3
content_sha256: 2c97b42df753cbd6075c2d562744b15197fdb909201b155ce39e33fe179a8a8f
license: Apache-2.0
source_kind: structured_template
extraction_notes: Value selected from a structured configuration; line range cites the complete file.
---
<context_window_reminder>
The current context window is exhausted. Do not continue the task or give a final answer in this window. The next window will not automatically include this conversation. Make exactly one write or append call to `notes` now to save a concise checkpoint with the goal, decisions, progress, learnings, next steps, and the window ID and item ID of every relevant user request still being solved, as well as important actions/tool calls for future reference. Note that every non-assistant item, such as user, developer, tool response, has an item id `[id: ...]` that is immediately after its item content. After the notes result returns, call `functions.new_context`; do not use any tools other than `notes` and `functions.new_context`.
</context_window_reminder>