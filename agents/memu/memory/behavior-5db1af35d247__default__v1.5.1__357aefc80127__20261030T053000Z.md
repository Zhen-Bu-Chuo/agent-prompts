---
agent: memu
prompt_id: behavior-5db1af35d247
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/behavior.py
source_symbol: module.PROMPT_BLOCK_WORKFLOW.1
source_lines:
- 50
- 60
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/behavior.py#L50-L60
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: c5d20d86514faa3b5473aa0979d393b774119e1a8cb87b4b102ca479b4f83d9b
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Workflow
Read the full conversation to understand topics and meanings.
## Extract memories
Select turns that contain valuable Behavior Information and extract behavioral memory items.
## Review & validate
Merge semantically similar items.
Resolve contradictions by keeping the latest / most certain item.
## Final output
Output Behavior Information.
