---
agent: memu
prompt_id: event-e55281432445
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/event.py
source_symbol: module.PROMPT_BLOCK_WORKFLOW.1
source_lines:
- 62
- 72
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/event.py#L62-L72
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: aa8ed10ee33d2932d1743aef7132bce9f955deb2b35b3f029cd57a81363a5e45
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Workflow
Read the full conversation to understand topics and meanings.
## Extract memories
Select turns that contain valuable Event Information and extract event memory items.
## Review & validate
Merge semantically similar items.
Resolve contradictions by keeping the latest / most certain item.
## Final output
Output Event Information.
