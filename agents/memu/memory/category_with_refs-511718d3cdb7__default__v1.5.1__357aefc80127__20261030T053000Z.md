---
agent: memu
prompt_id: category_with_refs-511718d3cdb7
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/category_summary/category_with_refs.py
source_symbol: module.PROMPT_BLOCK_EXAMPLES.1
source_lines:
- 78
- 106
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/category_summary/category_with_refs.py#L78-L106
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: a6b8177f52e3cb2fc1cf979c27b1f306b8822c78f8bb44bc986000ffd89d7124
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Examples (Input / Output)

Topic:
Personal Basic Information

Original content:
<content>
# Personal Basic Information
## Basic Information
- The user is 28 years old
- The user currently lives in Beijing
</content>

New memory items with IDs:
<items>
- [item_a1b2c3] The user is 30 years old
- [item_d4e5f6] The user currently lives in Shanghai
- [item_g7h8i9] The user prefers Sichuan-style spicy food
</items>

Output:
# Personal Basic Information
## Basic Information
- The user is 30 years old [ref:item_a1b2c3]
- The user currently lives in Shanghai [ref:item_d4e5f6]
## Basic Preferences
- The user prefers Sichuan-style spicy food [ref:item_g7h8i9]
