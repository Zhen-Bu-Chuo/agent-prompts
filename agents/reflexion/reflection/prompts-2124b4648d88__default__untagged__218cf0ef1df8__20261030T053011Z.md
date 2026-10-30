---
agent: reflexion
prompt_id: prompts-2124b4648d88
module: reflection
variant: default
upstream_repository: noahshinn/reflexion
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 218cf0ef1df84b05ce379dd4a8e47f17766733a0
source_path: hotpotqa_runs/prompts.py
source_symbol: module.REACT_INSTRUCTION.1
source_lines:
- 90
- 98
source_permalink: https://github.com/noahshinn/reflexion/blob/218cf0ef1df84b05ce379dd4a8e47f17766733a0/hotpotqa_runs/prompts.py#L90-L98
source_committed_at: '2025-01-14T07:53:43Z'
release_published_at: null
fetched_at: '2026-10-30T05:30:11Z'
extractor_version: 1.0.3
content_sha256: 76e85198e85e25c703b7dc79f65fb274a24e1e123fc040cd2710b784160035f6
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the last passage successfully found by Search.
(3) Finish[answer], which returns the answer and finishes the task.
You may take as many steps as necessary.
Here are some examples:
{examples}
(END OF EXAMPLES)
Question: {question}{scratchpad}