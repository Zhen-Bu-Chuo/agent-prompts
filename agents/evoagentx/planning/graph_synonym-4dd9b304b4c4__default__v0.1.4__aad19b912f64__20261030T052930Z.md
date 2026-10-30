---
agent: evoagentx
prompt_id: graph_synonym-4dd9b304b4c4
module: planning
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: v0.1.4
package_name: null
package_version: null
source_ref: v0.1.4
source_commit: aad19b912f640161ea07e8904d9237cd34fde5f1
source_path: evoagentx/prompts/rag/graph_synonym.py
source_symbol: module.DEFAULT_SYNONYM_EXPAND_TEMPLATE.1
source_lines:
- 3
- 10
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/rag/graph_synonym.py#L3-L10
source_committed_at: '2026-06-28T10:20:05Z'
release_published_at: '2026-06-28T10:24:06Z'
fetched_at: '2026-10-30T05:29:30Z'
extractor_version: 1.0.3
content_sha256: 7341c1c870bc37ad6b0a2b9ae6f0b4dfc70fa05e7da4e06fe572616d1dca14f3
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Given some initial query, generate synonyms or related keywords up to {max_keywords} in total, considering possible cases of capitalization, pluralization, common expressions, etc.
Provide all synonyms/keywords separated by '^' symbols: 'keyword1^keyword2^...'
Note, result should be in one-line, separated by '^' symbols.----
QUERY: {query_str}
----
KEYWORDS: 