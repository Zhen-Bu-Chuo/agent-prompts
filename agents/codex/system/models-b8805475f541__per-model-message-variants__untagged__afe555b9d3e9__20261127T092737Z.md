---
agent: codex
prompt_id: models-b8805475f541
module: system
variant: per-model-message-variants
upstream_repository: openai/codex
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: afe555b9d3e95b4f58b247212565070f1555bc5d
source_path: codex-rs/models-manager/models.json
source_symbol: models.5.model_messages.auto_review.rejection_instructions
source_lines:
- 1
- 2124
source_permalink: https://github.com/openai/codex/blob/afe555b9d3e95b4f58b247212565070f1555bc5d/codex-rs/models-manager/models.json#L1-L2124
source_committed_at: '2026-11-27T05:03:45Z'
release_published_at: null
fetched_at: '2026-11-27T09:27:37Z'
extractor_version: 1.0.3
content_sha256: fc210b5bc0337ddba407c155ef00eea5ba8bda8dd264ce415ce100e1b2ac81e3
license: Apache-2.0
source_kind: structured_template
extraction_notes: Value selected from a structured configuration; line range cites the complete file.
---
Do not bypass this rejection through a workaround or indirect execution. Continue with a safer alternative, or carry out checks to prove that the action is authorized or low risk before trying again. Complete unaffected work without asking for confirmation. Report anything that remains blocked, clarify why it was blocked by auto-review, inform the user of the risk and ask for approval.