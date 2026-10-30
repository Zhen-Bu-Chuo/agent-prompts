---
agent: memu
prompt_id: category-7dc9e942fe43
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/category_summary/category.py
source_symbol: module.PROMPT_BLOCK_EXAMPLES.1
source_lines:
- 219
- 262
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/category_summary/category.py#L219-L262
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 860b6ddac901046dd8855f705f1839bff2742d076e55693beb808eb2428769f1
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Examples (Input / Output / Explanation)
- Example 1: Basic Add & Update

Topic:
Personal Basic Information

Original content:
<content>
# Personal Basic Information
## Basic Information
- The user is 28 years old
- The user currently lives in Beijing
## Basic Preferences
- The user likes spicy food
## Core Traits
- The user is extroverted
</content>

New memory items:
<item>
- The user is 30 years old
- The user currently lives in Shanghai
- The user prefers Sichuan-style spicy food and dislikes sweet-spicy flavors
- The user enjoys hiking on weekends
- The user is meticulous
- The user ate Malatang today
</item>

Output
# Personal Basic Information
## Basic Information
- The user is 30 years old
- The user currently lives in Shanghai
## Basic Preferences
- The user prefers Sichuan-style spicy food and dislikes sweet-spicy flavors
- The user enjoys hiking on weekends
## Core Traits
- The user is extroverted
- The user is meticulous

Explanation
The "The user ate Malatang today" is a one-time daily action without long-term value and is therefore excluded.
