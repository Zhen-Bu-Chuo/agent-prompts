---
agent: memu
prompt_id: tool-a90fe195cfe2
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/tool.py
source_symbol: module.PROMPT_BLOCK_WORKFLOW.1
source_lines:
- 6
- 17
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/tool.py#L6-L17
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: ace885eb68de1b56840f026f25a9970a0d8abb2bc0395355a65039b2f5413387
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Workflow
Read the full resource content to understand tool execution context.
## Extract tool memories
Identify tool calls, their inputs, outputs, success/failure status, and any patterns.
## Create tool memory entries
For each significant tool usage, create a memory entry with when_to_use hints.
## Review & validate
Ensure each tool memory is actionable and helps future tool selection.
## Final output
Output Tool Memory entries.
