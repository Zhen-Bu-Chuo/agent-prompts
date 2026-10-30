---
agent: memu
prompt_id: llm_category_ranker-86c4e0d6f62b
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/retrieve/llm_category_ranker.py
source_symbol: module.PROMPT.1
source_lines:
- 1
- 35
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/retrieve/llm_category_ranker.py#L1-L35
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: fddeded89eb8095aaf3795ba4c83854d3a71c319d5c751fe70aee1bb32d9f6f5
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Task Objective
Search through the provided categories and identify the most relevant ones for the given query, then rank them by relevance.

# Workflow
1. Analyze the **Query** to understand its intent and key topics.
2. Review all **Available Categories**.
3. Determine which categories are relevant to the query.
4. Select up to **{top_k}** most relevant categories.
5. Rank the selected categories from most to least relevant.

# Rules
- Only include categories that are actually relevant to the query.
- Include **at most** {top_k} categories.
- Ranking matters: the first category must be the most relevant.
- Do not invent or modify category IDs.
- If no categories are relevant, return an empty array.

# Output Format
Return the result as a JSON object in the following format:

```json
{{
  "analysis": "your analysis process",
  "categories": ["category_id_1", "category_id_2", "category_id_3"]
}}
```

# Input
Query:
{query}

Available Categories:
{categories_data}
