---
agent: codex
prompt_id: models-d2ad9c53c2ba
module: system
variant: per-model-message-variants
upstream_repository: openai/codex
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: b9559ff737000a4fcf7a0e12c3353cca1ea4d008
source_path: codex-rs/models-manager/models.json
source_symbol: models.7.model_messages.token_budget.reminder_message_template
source_lines:
- 1
- 2124
source_permalink: https://github.com/openai/codex/blob/b9559ff737000a4fcf7a0e12c3353cca1ea4d008/codex-rs/models-manager/models.json#L1-L2124
source_committed_at: '2026-11-19T06:34:53Z'
release_published_at: null
fetched_at: '2026-11-19T08:26:15Z'
extractor_version: 1.0.3
content_sha256: 840af84260ef8d951f5fc7e4cef7e3bb61b2b063621b117f0a2604aba9a60bf1
license: Apache-2.0
source_kind: structured_template
extraction_notes: Value selected from a structured configuration; line range cites the complete file.
---
<context_window_reminder>
Your current context window is nearly exhausted; only {n_remaining} tokens remain. Before starting a new context window, save concise progress notes with the `notes` tool with the goal, decisions, progress, learnings, next steps, and the window ID and item ID of every relevant user request still being solved, as well as important actions/tool calls for future reference. Note that every non-assistant item, such as user, developer, tool response, has an item id `[id: ...]` that is immediately after its item content. You should write or append notes in a way to best help you recover in a new context window. It is also a good idea to clean up your old notes if they become obsolete or irrelevant. Future context windows will not automatically include the current conversation. After saving your state, call `functions.new_context` to continue in a fresh context window.
</context_window_reminder>