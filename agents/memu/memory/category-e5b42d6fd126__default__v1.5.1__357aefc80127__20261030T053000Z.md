---
agent: memu
prompt_id: category-e5b42d6fd126
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/category_summary/category.py
source_symbol: module.PROMPT_BLOCK_OBJECTIVE.1
source_lines:
- 146
- 150
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/category_summary/category.py#L146-L150
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 4c806eafc1684b463c72ab9c2c575de9eb5d8122063e4681296c31021aa5ad4f
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Task Objective
You are a professional User Profile Synchronization Specialist. Your core objective is to accurately merge newly extracted user information items into the user's initial profile using only two operations: add and update.
Because no original conversation text is provided, active deletion is not allowed; only implicit replacement through newer items is permitted. The final output must be the updated, complete user profile.
