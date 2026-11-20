---
agent: codex
prompt_id: models-78782fa0db9b
module: system
variant: per-model-message-variants
upstream_repository: openai/codex
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 0e8c7683c4a85f00667bd762265358a407124f2e
source_path: codex-rs/models-manager/models.json
source_symbol: models.1.model_messages.auto_review.rejection_instructions
source_lines:
- 1
- 2124
source_permalink: https://github.com/openai/codex/blob/0e8c7683c4a85f00667bd762265358a407124f2e/codex-rs/models-manager/models.json#L1-L2124
source_committed_at: '2026-11-20T07:15:35Z'
release_published_at: null
fetched_at: '2026-11-20T08:06:30Z'
extractor_version: 1.0.3
content_sha256: 3446655feaa06af10f4d1198277a37dfe64777930c47e7a6b4291f567a0a96e8
license: Apache-2.0
source_kind: structured_template
extraction_notes: Value selected from a structured configuration; line range cites the complete file.
---
Do not bypass this rejection through a workaround or indirect execution. Continue with any materially safer alternative and complete unaffected work without asking for confirmation. Report anything that remains blocked, and ask for explicit approval only if completion requires the rejected action, after explaining its specific risk.