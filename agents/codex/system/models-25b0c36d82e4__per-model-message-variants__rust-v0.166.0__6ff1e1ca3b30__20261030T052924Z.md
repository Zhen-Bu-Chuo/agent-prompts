---
agent: codex
prompt_id: models-25b0c36d82e4
module: system
variant: per-model-message-variants
upstream_repository: openai/codex
upstream_version: rust-v0.166.0
package_name: null
package_version: null
source_ref: rust-v0.166.0
source_commit: 6ff1e1ca3b30fc8b914720681fcf5fe62e95f856
source_path: codex-rs/models-manager/models.json
source_symbol: models.2.model_messages.auto_review.rejection_instructions
source_lines:
- 1
- 1779
source_permalink: https://github.com/openai/codex/blob/6ff1e1ca3b30fc8b914720681fcf5fe62e95f856/codex-rs/models-manager/models.json#L1-L1779
source_committed_at: '2026-10-29T17:44:30Z'
release_published_at: '2026-10-29T19:47:53Z'
fetched_at: '2026-10-30T05:29:24Z'
extractor_version: 1.0.3
content_sha256: fc210b5bc0337ddba407c155ef00eea5ba8bda8dd264ce415ce100e1b2ac81e3
license: Apache-2.0
source_kind: structured_template
extraction_notes: Value selected from a structured configuration; line range cites the complete file.
---
Do not bypass this rejection through a workaround or indirect execution. Continue with a safer alternative, or carry out checks to prove that the action is authorized or low risk before trying again. Complete unaffected work without asking for confirmation. Report anything that remains blocked, clarify why it was blocked by auto-review, inform the user of the risk and ask for approval.