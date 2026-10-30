---
agent: memu
prompt_id: query_rewriter_judger-23e4bd6f22b4
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/retrieve/query_rewriter_judger.py
source_symbol: module.USER_PROMPT.1
source_lines:
- 38
- 48
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/retrieve/query_rewriter_judger.py#L38-L48
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: b15a6766a201b3f7a4101f4fe8af997788b91c1b199d6c675c52da5ae59ed915
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

Input:
Query Context:
{conversation_history}

Original Query:
{original_query}

Retrieved Content So Far:
{retrieved_content}
