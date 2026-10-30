---
agent: reflexion
prompt_id: prompts-19d4bbc394f0
module: reflection
variant: default
upstream_repository: noahshinn/reflexion
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 218cf0ef1df84b05ce379dd4a8e47f17766733a0
source_path: hotpotqa_runs/prompts.py
source_symbol: module.COT_REFLECT_INSTRUCTION.1
source_lines:
- 21
- 30
source_permalink: https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/prompts.py#L21-L30
source_committed_at: '2025-01-14T07:53:43Z'
release_published_at: null
fetched_at: '2026-10-30T05:30:11Z'
extractor_version: 1.0.3
content_sha256: 3c6f893ad052fa9d584b33a3d76fa219133217732125b2c6714d84c0eb5c088b
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to relevant context and a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>] or there is a phrasing discrepancy with your provided answer and the answer key. In a few sentences, Diagnose a possible reason for failure or phrasing discrepancy and devise a new, concise, high level plan that aims to mitigate the same failure. Use complete sentences.  
Here are some examples:
{examples}
(END OF EXAMPLES)

Previous trial:
Relevant Context: {context}
Question: {question}{scratchpad}

Reflection: