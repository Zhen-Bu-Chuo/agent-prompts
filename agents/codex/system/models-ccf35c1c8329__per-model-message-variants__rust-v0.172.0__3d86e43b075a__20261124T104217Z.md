---
agent: codex
prompt_id: models-ccf35c1c8329
module: system
variant: per-model-message-variants
upstream_repository: openai/codex
upstream_version: rust-v0.172.0
package_name: null
package_version: null
source_ref: rust-v0.172.0
source_commit: 3d86e43b075adeba2193ec5c22ac92f55afd82e6
source_path: codex-rs/models-manager/models.json
source_symbol: models.6.model_messages.auto_review.rejection_instructions
source_lines:
- 1
- 2124
source_permalink: https://github.com/openai/codex/blob/3d86e43b075adeba2193ec5c22ac92f55afd82e6/codex-rs/models-manager/models.json#L1-L2124
source_committed_at: '2026-11-23T22:48:37Z'
release_published_at: '2026-11-24T00:03:55Z'
fetched_at: '2026-11-24T10:42:17Z'
extractor_version: 1.0.3
content_sha256: fc210b5bc0337ddba407c155ef00eea5ba8bda8dd264ce415ce100e1b2ac81e3
license: Apache-2.0
source_kind: structured_template
extraction_notes: Value selected from a structured configuration; line range cites the complete file.
---
Do not bypass this rejection through a workaround or indirect execution. Continue with a safer alternative, or carry out checks to prove that the action is authorized or low risk before trying again. Complete unaffected work without asking for confirmation. Report anything that remains blocked, clarify why it was blocked by auto-review, inform the user of the risk and ask for approval.