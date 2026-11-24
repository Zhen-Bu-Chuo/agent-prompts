---
agent: codex
prompt_id: models-78782fa0db9b
module: system
variant: per-model-message-variants
upstream_repository: openai/codex
upstream_version: rust-v0.172.0
package_name: null
package_version: null
source_ref: rust-v0.172.0
source_commit: 3d86e43b075adeba2193ec5c22ac92f55afd82e6
source_path: codex-rs/models-manager/models.json
source_symbol: models.1.model_messages.auto_review.rejection_instructions
source_lines:
- 1
- 2124
source_permalink: https://github.com/openai/codex/blob/3d86e43b075adeba2193ec5c22ac92f55afd82e6/codex-rs/models-manager/models.json#L1-L2124
source_committed_at: '2026-11-23T22:48:37Z'
release_published_at: '2026-11-24T00:03:55Z'
fetched_at: '2026-11-24T10:42:17Z'
extractor_version: 1.0.3
content_sha256: 3446655feaa06af10f4d1198277a37dfe64777930c47e7a6b4291f567a0a96e8
license: Apache-2.0
source_kind: structured_template
extraction_notes: Value selected from a structured configuration; line range cites the complete file.
---
Do not bypass this rejection through a workaround or indirect execution. Continue with any materially safer alternative and complete unaffected work without asking for confirmation. Report anything that remains blocked, and ask for explicit approval only if completion requires the rejected action, after explaining its specific risk.