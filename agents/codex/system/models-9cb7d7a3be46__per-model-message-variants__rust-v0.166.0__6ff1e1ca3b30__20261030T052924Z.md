---
agent: codex
prompt_id: models-9cb7d7a3be46
module: system
variant: per-model-message-variants
upstream_repository: openai/codex
upstream_version: rust-v0.166.0
package_name: null
package_version: null
source_ref: rust-v0.166.0
source_commit: 6ff1e1ca3b30fc8b914720681fcf5fe62e95f856
source_path: codex-rs/models-manager/models.json
source_symbol: models.8.model_messages.token_budget.auto_compact_fallback_prompt
source_lines:
- 1
- 1779
source_permalink: https://github.com/openai/codex/blob/6ff1e1ca3b30fc8b914720681fcf5fe62e95f856/codex-rs/models-manager/models.json#L1-L1779
source_committed_at: '2026-10-29T17:44:30Z'
release_published_at: '2026-10-29T19:47:53Z'
fetched_at: '2026-10-30T05:29:24Z'
extractor_version: 1.0.3
content_sha256: 2c97b42df753cbd6075c2d562744b15197fdb909201b155ce39e33fe179a8a8f
license: Apache-2.0
source_kind: structured_template
extraction_notes: Value selected from a structured configuration; line range cites the complete file.
---
<context_window_reminder>
The current context window is exhausted. Do not continue the task or give a final answer in this window. The next window will not automatically include this conversation. Make exactly one write or append call to `notes` now to save a concise checkpoint with the goal, decisions, progress, learnings, next steps, and the window ID and item ID of every relevant user request still being solved, as well as important actions/tool calls for future reference. Note that every non-assistant item, such as user, developer, tool response, has an item id `[id: ...]` that is immediately after its item content. After the notes result returns, call `functions.new_context`; do not use any tools other than `notes` and `functions.new_context`.
</context_window_reminder>