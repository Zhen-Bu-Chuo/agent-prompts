---
agent: memu
prompt_id: category_with_refs-1bd1b25bde56
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/category_summary/category_with_refs.py
source_symbol: module.PROMPT_BLOCK_WORKFLOW.1
source_lines:
- 16
- 50
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/category_summary/category_with_refs.py#L16-L50
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 538e0f60a1d0c6d4401f5fc68af6233c8d072cbc921986c573408efe4af5fd2d
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Workflow
## Step 1: Preprocessing & Parsing
- Input sources:
  - User Initial Profile: structured, categorized, confirmed long-term user information.
  - Newly Extracted User Information Items: each item has an ID that MUST be referenced.
- Structure parsing:
  - Initial profile: extract categories and core content; preserve original wording style and format.
  - New items: note the item ID for each piece of information to include as [ref:ID].

## Step 2: Core Operations (Update / Add)
A. Update
- When updating existing information with new data, add the reference: "User is 30 years old [ref:item_abc123]"
- If multiple items support the same fact, include multiple refs: [ref:id1,id2]

B. Add
- When adding new information, always include the source reference
- Format: "User enjoys hiking on weekends [ref:item_xyz789]"

## Step 3: Merge & Formatting
- Structured ordering: present content by category order; omit empty categories.
- Formatting rules: strictly use Markdown (# for main title, ## for category titles).
- References: ensure every new or updated fact has at least one [ref:ITEM_ID] citation.

## Step 4: Summarize
Target length: {target_length}
- Summarize the updated user markdown profile to the target length.
- PRESERVE all [ref:ITEM_ID] citations in the summary.
- Use Markdown hierarchy.

## Step 5: Output
- Output only the updated user markdown profile with inline references.
- Use Markdown hierarchy.
- Do not include explanations, operation traces, or meta text.
