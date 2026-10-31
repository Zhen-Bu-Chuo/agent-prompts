---
agent: evoagentx
prompt_id: workflow_editor-1bb1274f321b
module: planning
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: e3df900662443e94dd92141be5633b040a69a70a
source_path: evoagentx/prompts/workflow/workflow_editor.py
source_symbol: module.PROMPT_BASE.1
source_lines:
- 1
- 15
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/e3df900662443e94dd92141be5633b040a69a70a/evoagentx/prompts/workflow/workflow_editor.py#L1-L15
source_committed_at: '2026-10-31T01:49:52Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:23Z'
extractor_version: 1.0.3
content_sha256: 1a545cd29cf080353dc6ecc97b4f878759b36e28375c633cf9a82f92ce0222e2
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

analyze the workflow and optimize it according to the user's advice and make it more reasonable and efficient, make sure to keep the original key of the json dict,and the original structure of the json dict:

current workflow structure:
{current_workflow_json}

user's advice:
{user_advice}

after the user's advice, please consider the following rules:
1. the description of the node is clear
2. the input and output parameters are reasonable
3. the dependency relationship between the nodes is correct
4. whether some nodes can be merged or split
