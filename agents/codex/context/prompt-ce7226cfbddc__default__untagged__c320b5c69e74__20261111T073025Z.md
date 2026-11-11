---
agent: codex
prompt_id: prompt-ce7226cfbddc
module: context
variant: default
upstream_repository: openai/codex
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: c320b5c69e74755a6efd4075ff01d4524ad6a4bf
source_path: codex-rs/prompts/templates/compact/prompt.md
source_symbol: document
source_lines:
- 1
- 9
source_permalink: https://github.com/openai/codex/blob/c320b5c69e74755a6efd4075ff01d4524ad6a4bf/codex-rs/prompts/templates/compact/prompt.md#L1-L9
source_committed_at: '2026-11-11T07:24:38Z'
release_published_at: null
fetched_at: '2026-11-11T07:30:25Z'
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
