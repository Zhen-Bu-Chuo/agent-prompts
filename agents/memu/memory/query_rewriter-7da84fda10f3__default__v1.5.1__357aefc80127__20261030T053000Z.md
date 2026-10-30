---
agent: memu
prompt_id: query_rewriter-7da84fda10f3
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/retrieve/query_rewriter.py
source_symbol: module.PROMPT.1
source_lines:
- 1
- 44
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/retrieve/query_rewriter.py#L1-L44
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 4e8b9819febd9d33356583bbaf046562b8eb03b69b71d8b4d737a8d1a3514c65
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Task Objective
Rewrite a user query to make it self-contained and explicit by resolving references and ambiguities using the conversation history.

# Workflow
1. Review the **Conversation History** to identify relevant entities, topics, and context.
2. Analyze the **Current Query**.
3. Determine whether the query contains:
   - Pronouns (e.g., “they”, “it”, “their”, “his”, “her”)
   - Referential expressions (e.g., “that”, “those”, “the same”)
   - Implicit context (e.g., “what about…”, “and also…”)
   - Incomplete information that can be inferred from the conversation history
4. If rewriting is needed:
   - Replace pronouns with specific entities mentioned in the conversation
   - Add necessary background from the conversation history
   - Make implicit references explicit
   - Ensure the rewritten query is understandable on its own
5. If the query is already clear and self-contained, keep it unchanged.

# Rules
- Preserve the original intent of the user query.
- Only use information explicitly available in the conversation history.
- Do not introduce new assumptions or external knowledge.
- Keep the rewritten query concise but fully explicit.

# Output Format
Use the following structure:

<analysis>
Brief analysis of whether the query needs rewriting and why.
</analysis>

<rewritten_query>
The rewritten query that is self-contained and explicit if no rewrite is needed).
</rewritten_query>


# Input
Query Context:
{conversation_history}

Current Query:
{query}
