---
agent: evoagentx
prompt_id: graph_synonym-4dd9b304b4c4
module: planning
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: e3df900662443e94dd92141be5633b040a69a70a
source_path: evoagentx/prompts/rag/graph_synonym.py
source_symbol: module.DEFAULT_SYNONYM_EXPAND_TEMPLATE.1
source_lines:
- 3
- 10
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/e3df900662443e94dd92141be5633b040a69a70a/evoagentx/prompts/rag/graph_synonym.py#L3-L10
source_committed_at: '2026-10-31T01:49:52Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:23Z'
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