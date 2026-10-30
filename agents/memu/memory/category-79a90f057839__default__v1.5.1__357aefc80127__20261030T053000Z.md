---
agent: memu
prompt_id: category-79a90f057839
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/category_patch/category.py
source_symbol: module.PROMPT.1
source_lines:
- 1
- 45
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/category_patch/category.py#L1-L45
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: efc67a2b8ef259319a5a21ef989f6da439711f42ce6dc84778638d288c23620e
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Task Objective
Your task is to read an existing user profile and an update related to a specific memory topic, then determine whether the profile needs to be updated.
If an update is required, you must generate the updated version of the profile based on the rules below.

# Workflow
1. Understand the Topic
Focus only on memories relevant to the specified Topic.

2. Analyze Original Content
Review the existing profile content enclosed in <content>...</content>.

3. Analyze Update
Determine whether the update represents:
- A new memory
- A variation of an existing memory
- A discarded (invalidated) memory

4. Decision Making
Judge whether the profile requires modification based on relevance and importance.

5. Generate Output
- If an update is required, produce the revised profile content.
- If not, explicitly indicate that no update is needed.


# Response Format (JSON):
{{
    "need_update": [bool, whether the profile needs to be updated]
    "updated_content": [str, the updated content of the profile if need_update is true, otherwise empty]
}}


# Input
Topic:
{category}

Original content:
<content>
{original_content}
</content>

Update:
{update_content}
