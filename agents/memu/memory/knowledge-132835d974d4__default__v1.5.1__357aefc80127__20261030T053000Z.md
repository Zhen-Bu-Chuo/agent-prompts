---
agent: memu
prompt_id: knowledge-132835d974d4
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/knowledge.py
source_symbol: module.PROMPT_BLOCK_WORKFLOW.1
source_lines:
- 52
- 62
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/knowledge.py#L52-L62
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 96174204ddba4363184d51f0a65d3da1dde751cccea6372fba814e2f5a826ba1
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Workflow
Read the full conversation to understand topics and meanings.
## Extract memories
Select turns that contain valuable Knowledge Information and extract knowledge memory items.
## Review & validate
Merge semantically similar items.
Resolve contradictions by keeping the latest / most certain item.
## Final output
Output Knowledge Information.
