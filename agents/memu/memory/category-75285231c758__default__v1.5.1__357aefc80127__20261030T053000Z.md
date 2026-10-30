---
agent: memu
prompt_id: category-75285231c758
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/category_summary/category.py
source_symbol: module.PROMPT_BLOCK_WORKFLOW.1
source_lines:
- 152
- 197
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/category_summary/category.py#L152-L197
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 0eebbaecb00320fecac2e3d878ed9fb82300ad7c1a6065ac81a0073396c023c8
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Workflow
## Step 1: Preprocessing & Parsing
- Input sources
User Initial Profile: structured, categorized, confirmed long-term user information.
Newly Extracted User Information Items.
- Structure parsing
Initial profile: extract categories and core content; preserve original wording style and format; build a category-content mapping.
New items: validate completeness and category correctness; mark each as Add or Update; distinguish stable facts from event-type information; extract dates/times (events only).
- Pre-validation
Verify subject accuracy: clearly distinguish the user from related persons (family, friends, etc.).
Remove invalid items: vague, miscategorized, or non-user-information items.
Remove one-off events: temporary actions without long-term relevance (e.g., what the user ate today).

## Step 2: Core Operations (Update / Add)
A. Update
Conflict detection: compare new items with existing ones in the same category for semantic overlap (e.g., age update).
Validity priority: retain information that is more specific, clearer, and more certain.
Overwrite / supplement: replace outdated entries with new ones, ensuring no loss of core information.
Time integration (events only): retain dates/times and integrate them naturally; multiple events at the same time may be layered, but each entry must remain independently understandable.
B. Add
Deduplication check: ensure the new item is not identical or semantically similar to existing or updated items.
Category matching: place the item into the correct predefined category.
Insertion: add the item following the original profile's language and formatting style, concise and clear.

## Step 3: Merge & Formatting
Structured ordering: present content by category order; omit empty categories.
Formatting rules: strictly use Markdown (# for main title, ## for category titles).
Final validation
Consistency: no contradictions or duplicates.
Compliance: correct categories only; no explanatory or operational text.
Accuracy: subject clarity; natural time embedding; proper format.


## Step 4: Summarize
Target length: {target_length}
Summarize the updated user markdown profile to the target length.
Use Markdown hierarchy.
Cluster the memory items and update the <category name>.

## Step 5: Output
Output only the updated user markdown profile.
Use Markdown hierarchy.
Do not include explanations, operation traces, or meta text.
Control item length strictly; prioritize core information if needed.
