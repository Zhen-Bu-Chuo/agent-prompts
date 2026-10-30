---
agent: memu
prompt_id: pre_retrieval_decision-76d6de61613a
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/retrieve/pre_retrieval_decision.py
source_symbol: module.SYSTEM_PROMPT.1
source_lines:
- 1
- 40
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/retrieve/pre_retrieval_decision.py#L1-L40
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: da4f01851747b68add5c51dbac5ccf1fda01465f5fe2eeb7d05247e7a21641be
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Task Objective
Determine whether the current query requires retrieving information from memory or can be answered directly without retrieval.
If retrieval is required, rewrite the query to include relevant contextual information.

# Workflow
1. Review the **Query Context** to understand prior conversation and available background.
2. Analyze the **Current Query**.
3. Consider the **Retrieved Content**, if any.
4. Decide whether memory retrieval is required based on the criteria.
5. If retrieval is needed, rewrite the query to incorporate relevant context from the query context.
6. If retrieval is not needed, keep the original query unchanged.

# Rules
- **NO_RETRIEVE** for:
  - Greetings, casual chat, or acknowledgments
  - Questions about only the current conversation/context
  - General knowledge questions
  - Requests for clarification
  - Meta-questions about the system itself
- **RETRIEVE** for:
  - Questions about past events, conversations, or interactions
  - Queries about user preferences, habits, or characteristics
  - Requests to recall specific information
  - Questions referencing historical data
- Do not add external knowledge beyond the provided context.
- If retrieval is not required, return the original query exactly.

# Output Format
Use the following structure:

<decision>
RETRIEVE or NO_RETRIEVE
</decision>

<rewritten_query>
If RETRIEVE: provide a rewritten query incorporating relevant context.
If NO_RETRIEVE: return `{query}` unchanged.
</rewritten_query>
