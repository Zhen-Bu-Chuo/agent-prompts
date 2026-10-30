---
agent: reflexion
prompt_id: prompts-c7b3fce8a462
module: reflection
variant: default
upstream_repository: noahshinn/reflexion
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 218cf0ef1df84b05ce379dd4a8e47f17766733a0
source_path: hotpotqa_runs/prompts.py
source_symbol: module.COT_SIMPLE_INSTRUCTION.1
source_lines:
- 47
- 53
source_permalink: https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/prompts.py#L47-L53
source_committed_at: '2025-01-14T07:53:43Z'
release_published_at: null
fetched_at: '2026-10-30T05:30:11Z'
extractor_version: 1.0.3
content_sha256: 8d803ff05704b65acf71d5077f28f24246564a3ab159adc4af4e02a2a630a3ea
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Solve a question answering task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task.
Here are some examples:
{examples}
(END OF EXAMPLES)
{reflections}
{context}
Question: {question}{scratchpad}