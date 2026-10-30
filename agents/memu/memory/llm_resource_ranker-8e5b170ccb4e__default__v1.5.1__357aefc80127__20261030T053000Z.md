---
agent: memu
prompt_id: llm_resource_ranker-8e5b170ccb4e
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/retrieve/llm_resource_ranker.py
source_symbol: module.PROMPT.1
source_lines:
- 1
- 40
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/retrieve/llm_resource_ranker.py#L1-L40
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 376c4740d241021bc30883f70ff50200464997eb8e6a378b07e2ed8440468a9b
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Task Objective
Search through the provided resources and identify the most relevant ones for the given query, then rank them by relevance.

# Workflow
1. Analyze the **Query**  to understand its intent and key information needs.
2. Review the provided **Context Info** , which contains already-identified categories and items, to guide relevance.
3. Examine all **Available Resources**.
4. Determine which resources are actually relevant to the query.
5. Select up to {top_k} most relevant resources.
6. Rank the selected resources from most to least relevant.

# Rules
- Only include resources that are actually relevant to the query.
- Include **at most {top_k}** resources.
- Ranking matters: the first resource must be the most relevant.
- Do not invent, modify, or infer resource IDs.
- If no resources are relevant, return an empty array.

# Output Format
Return the result as a JSON object in the following format:

```json
{{
  "analysis": "your analysis process",
  "resources": ["resource_id_1", "resource_id_2", "resource_id_3"]
}}
```

# Input
Query:
{query}

Context Info:
{context_info}

Available Resources:
{resources_data}

