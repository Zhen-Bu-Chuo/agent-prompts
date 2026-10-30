---
agent: memu
prompt_id: category_with_refs-381184006185
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/category_summary/category_with_refs.py
source_symbol: module.PROMPT_BLOCK_RULES.1
source_lines:
- 52
- 59
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/category_summary/category_with_refs.py#L52-L59
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 4f441edd79e4e8ca10ce827fcc8f2d617f51596184c660de5a6a9e1ecb94ff16
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Reference Rules
1. Every piece of information from new memory items MUST have a [ref:ITEM_ID] citation
2. Use the exact item ID provided in the input
3. Place references immediately after the relevant statement
4. Multiple sources can be cited: [ref:id1,id2]
5. Existing information without new updates does not need references
