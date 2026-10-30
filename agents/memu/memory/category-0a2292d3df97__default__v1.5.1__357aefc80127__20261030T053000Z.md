---
agent: memu
prompt_id: category-0a2292d3df97
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/category_summary/category.py
source_symbol: module.PROMPT_BLOCK_INPUT.1
source_lines:
- 264
- 278
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/category_summary/category.py#L264-L278
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 08d045d47231771d2baab7d8a42d271574e5a991cdf3d61515046900e42c589c
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Input
Topic:
{category}

Original content:
<content>
{original_content}
</content>

New memory items:
<item>
{new_memory_items_text}
</item>
