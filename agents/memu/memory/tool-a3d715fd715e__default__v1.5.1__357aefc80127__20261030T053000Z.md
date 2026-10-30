---
agent: memu
prompt_id: tool-a3d715fd715e
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/tool.py
source_symbol: module.PROMPT_BLOCK_OBJECTIVE.1
source_lines:
- 1
- 4
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/tool.py#L1-L4
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: cccbe0fe23f30bae556c32171fd9f43e34a1b5d989d42c08702d24937571cdde
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Task Objective
You are a professional Tool Memory Extractor. Your core task is to extract tool usage patterns, execution results, and learnings from agent logs or tool execution traces. This enables agents to learn from their tool usage history.
