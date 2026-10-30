---
agent: memu
prompt_id: pre_retrieval_decision-4812308e913e
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/retrieve/pre_retrieval_decision.py
source_symbol: module.USER_PROMPT.1
source_lines:
- 43
- 53
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/retrieve/pre_retrieval_decision.py#L43-L53
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: f55e88fa5d272f705ca5c55f2edbd8b79296375b0f8fa937ac5d0956bb8870d5
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Input
Query Context:
{conversation_history}

Current Query:
{query}

Retrieved Content:
{retrieved_content}
