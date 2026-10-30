---
agent: memu
prompt_id: judger-d85dfe115a24
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/retrieve/judger.py
source_symbol: module.PROMPT.1
source_lines:
- 1
- 39
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/retrieve/judger.py#L1-L39
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 1661e360bad429a68ba188526ac5e18f9a0b4aa9f23d41e99033e32a03af02a9
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Task Objective
Judge whether the retrieved content is sufficient to answer the user's query.

# Workflow
1. Analyze the **Query** to understand what the user is asking.
2. Review the **Retrieved Content** carefully.
3. Evaluate the retrieved content against the following criteria:
   - Does it directly address the user's question?
   - Is the information specific and detailed enough?
   - Are there obvious gaps or missing details?
   - Did the user explicitly ask to recall or remember more information?
4. Based on this evaluation, decide whether the information is sufficient or more is needed.

# Rules
- Base your judgement **only** on the provided query and retrieved content.
- Do not assume or add external knowledge.
- Do not provide additional explanations beyond the required sections.
- The final judgement must be **one word only**.

# Output Format
Use the following structure:

<consideration>
Explain your reasoning for how you made the judgement.
</consideration>

<judgement>
ENOUGH or MORE
</judgement>


# Input
Query:
{query}

Retrieved Content:
{content}
