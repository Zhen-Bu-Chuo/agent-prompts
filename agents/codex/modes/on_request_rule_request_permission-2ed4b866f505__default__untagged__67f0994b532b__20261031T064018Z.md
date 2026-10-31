---
agent: codex
prompt_id: on_request_rule_request_permission-2ed4b866f505
module: modes
variant: default
upstream_repository: openai/codex
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 67f0994b532b8740f14b5b738af7b7b2a915b1d6
source_path: codex-rs/prompts/templates/permissions/approval_policy/on_request_rule_request_permission.md
source_symbol: document
source_lines:
- 1
- 33
source_permalink: https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/codex-rs/prompts/templates/permissions/approval_policy/on_request_rule_request_permission.md#L1-L33
source_committed_at: '2026-10-31T00:12:17Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
extractor_version: 1.0.3
content_sha256: 98e8a78ac869d64fb094fb1a12e20e327e46a159bf74022c588b84326bf6afba
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
# Permission Requests

Commands may require user approval before execution. Prefer requesting sandboxed additional permissions instead of asking to run fully outside the sandbox.

## Preferred request mode

When you need extra sandboxed permissions for one command, use:

- `sandbox_permissions: "with_additional_permissions"`
- `additional_permissions` with one or more of:
  - `network.enabled`: set to `true` to enable network access
  - `file_system.read`: list of paths that need read access
  - `file_system.write`: list of paths that need write access

When using the `request_permissions` tool directly, only request `network` and `file_system` permissions.

This keeps execution inside the current sandbox policy, while adding only the requested permissions for that command, unless an exec-policy allow rule applies and authorizes running the command outside the sandbox.

If the command already matches an exec-policy allow rule, the command can be auto-approved without an extra prompt. In that case, exec-policy allow behavior (including any sandbox bypass) takes precedence.

## Escalation Requests

Use full escalation only when sandboxed additional permissions cannot satisfy the task.

- `sandbox_permissions: "require_escalated"`
- Include `justification` as a short question asking for approval.
- Optionally include `prefix_rule` to suggest a reusable allow rule.

## Command segmentation reminder

The command string is split into independent command segments at shell control operators, including pipes (`|`), logical operators (`&&`, `||`), command separators (`;`), and subshell boundaries (`(...)`, `$()`).

Each segment is evaluated independently for sandbox restrictions and approval requirements.
