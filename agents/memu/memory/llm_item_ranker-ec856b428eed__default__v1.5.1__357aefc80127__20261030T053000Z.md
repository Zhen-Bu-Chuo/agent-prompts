---
agent: memu
prompt_id: llm_item_ranker-ec856b428eed
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/retrieve/llm_item_ranker.py
source_symbol: module.PROMPT.1
source_lines:
- 1
- 40
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/retrieve/llm_item_ranker.py#L1-L40
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 20782ce5c2239b206f47825bd31d00acf40645a18e688dfaa0c52d3c8623bef9
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Task Objective
Search through the provided memory items and identify the most relevant ones for the given query, based on the already identified relevant categories, then rank them by relevance.

# Workflow
1. Analyze the **Query** to understand intent and key information needs.
2. Review the **Relevant Categories** provided to understand the scope.
3. Examine all **Available Memory Items** within those categories.
4. Identify which memory items are truly relevant to the query.
5. Select up to **top_k** most relevant items.
6. Rank the selected items from most to least relevant.

# Rules
- Only consider memory items that belong to the provided relevant categories.
- Only include items that are actually relevant to the query.
- Include **at most** {top_k} items.
- Order matters: the first item must be the most relevant.
- Do not invent, modify, or infer item IDs.
- If no relevant items are found, return an empty array.

# Output Format
Return the result as a JSON object in the following format:

```json
{{
  "analysis": "your analysis process",
  "items": ["item_id_1", "item_id_2", "item_id_3"]
}}
```

# Input
Query:
{query}

Available Memory Items:
{items_data}

These memory items belong to the following relevant categories that were already identified:
{relevant_categories}
