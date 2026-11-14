---
agent: codex
prompt_id: prompt-ce7226cfbddc
module: context
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.169.0
package_name: null
package_version: null
source_ref: rust-v0.169.0
source_commit: d32063f96c2dff1dc96af839b3952abb6acfeda4
source_path: codex-rs/prompts/templates/compact/prompt.md
source_symbol: document
source_lines:
- 1
- 9
source_permalink: https://github.com/openai/codex/blob/d32063f96c2dff1dc96af839b3952abb6acfeda4/codex-rs/prompts/templates/compact/prompt.md#L1-L9
source_committed_at: '2026-11-13T04:48:19Z'
release_published_at: '2026-11-13T08:37:05Z'
fetched_at: '2026-11-14T07:23:29Z'
extractor_version: 1.0.3
content_sha256: ab0c334d4faca17e3afbb9b16967c1b2fdcc7242a9a0880af57949fa236d6d07
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are performing a CONTEXT CHECKPOINT COMPACTION. Create a handoff summary for another LLM that will resume the task.

Include:
- Current progress and key decisions made
- Important context, constraints, or user preferences
- What remains to be done (clear next steps)
- Any critical data, examples, or references needed to continue

Be concise, structured, and focused on helping the next LLM seamlessly continue the work.
