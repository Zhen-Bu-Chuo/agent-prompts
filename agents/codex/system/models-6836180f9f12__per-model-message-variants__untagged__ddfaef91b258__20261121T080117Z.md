---
agent: codex
prompt_id: models-6836180f9f12
module: system
variant: per-model-message-variants
upstream_repository: openai/codex
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: ddfaef91b258da5a0217951ed5f6e0039add5e02
source_path: codex-rs/models-manager/models.json
source_symbol: models.6.model_messages.approvals.on_request_auto_review
source_lines:
- 1
- 2124
source_permalink: https://github.com/openai/codex/blob/ddfaef91b258da5a0217951ed5f6e0039add5e02/codex-rs/models-manager/models.json#L1-L2124
source_committed_at: '2026-11-21T05:57:16Z'
release_published_at: null
fetched_at: '2026-11-21T08:01:17Z'
extractor_version: 1.0.3
content_sha256: 65dddb8b4bb89a74889c0b62e8f6620fe88f11b210d63637088c9535935f30f8
license: Apache-2.0
source_kind: structured_template
extraction_notes: Value selected from a structured configuration; line range cites the complete file.
---

`approvals_reviewer` is `auto_review`: Sandbox escalations with require_escalated will be reviewed for compliance with the policy.
If a rejection happens, you can continue with a safer alternative, or carry out checks to prove that the action is authorized or low risk before trying again. Complete unaffected work without asking for confirmation. Report anything that remains blocked, clarify why it was blocked by auto-review, inform the user of the risk and ask for approval.