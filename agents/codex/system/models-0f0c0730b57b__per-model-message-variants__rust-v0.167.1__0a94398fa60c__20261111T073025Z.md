---
agent: codex
prompt_id: models-0f0c0730b57b
module: system
variant: per-model-message-variants
upstream_repository: openai/codex
upstream_version: rust-v0.167.1
package_name: null
package_version: null
source_ref: rust-v0.167.1
source_commit: 0a94398fa60c4fac0e7659e4213a0a36e613dd46
source_path: codex-rs/models-manager/models.json
source_symbol: models.3.model_messages.approvals.on_request_auto_review
source_lines:
- 1
- 1779
source_permalink: https://github.com/openai/codex/blob/0a94398fa60c4fac0e7659e4213a0a36e613dd46/codex-rs/models-manager/models.json#L1-L1779
source_committed_at: '2026-11-10T18:02:25Z'
release_published_at: '2026-11-10T21:32:01Z'
fetched_at: '2026-11-11T07:30:25Z'
extractor_version: 1.0.3
content_sha256: 65dddb8b4bb89a74889c0b62e8f6620fe88f11b210d63637088c9535935f30f8
license: Apache-2.0
source_kind: structured_template
extraction_notes: Value selected from a structured configuration; line range cites the complete file.
---

`approvals_reviewer` is `auto_review`: Sandbox escalations with require_escalated will be reviewed for compliance with the policy.
If a rejection happens, you can continue with a safer alternative, or carry out checks to prove that the action is authorized or low risk before trying again. Complete unaffected work without asking for confirmation. Report anything that remains blocked, clarify why it was blocked by auto-review, inform the user of the risk and ask for approval.