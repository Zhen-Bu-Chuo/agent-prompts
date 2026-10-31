---
agent: evoagentx
prompt_id: workflow_manager-c39813834c44
module: planning
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: e3df900662443e94dd92141be5633b040a69a70a
source_path: evoagentx/prompts/workflow/workflow_manager.py
source_symbol: module.DEFAULT_TASK_SCHEDULER_PROMPT.1
source_lines:
- 3
- 50
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/e3df900662443e94dd92141be5633b040a69a70a/evoagentx/prompts/workflow/workflow_manager.py#L3-L50
source_committed_at: '2026-10-31T01:49:52Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:23Z'
extractor_version: 1.0.3
content_sha256: 0733c5f41afaf0d68f2cc61838dbf0efc26bcaf99f73460c49797edb4c087f73
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

### objective
Your task is to analyze the given workflow graph, current execution information, and candidate subtasks to decide one of the following actions:
- Select a subtask for iterative execution (if there is a loop or iterative context in the workflow). You may only iterate on each task up to {max_num_turns} times, also determined by the `Workflow Execution History`. 
- Select a new subtask from the candidates to move the workflow forward (if the workflow should proceed without re-executing or iterating).

### Instructions
1. Review the Workflow Information for the structure and details of the tasks and any potential loops or iterative sections.
2. Check the Current Execution Information for evidence of errors or missing data from previously executed subtasks.
3. If the workflow graph indicates there is a loop or iterative context, select a subtask from the Candidate Subtasks that aligns with that iterative or looping goal.
4. Otherwise, select a subtask from the Candidate Subtasks that best moves the workflow forward.
5. Finally, output the decision in the required format.

### Output Format
Your final output should ALWAYS in the following format:

## Thought 
Provide a brief explanation of your reasoning for scheduling the next task.

## Scheduled Subtask 
Produce your answer in valid JSON with the following structure: 
```json
{{
    "decision": "iterate | forward",
    "task_name": "name of the scheduled subtask",
    "reason": "the reasoning for scheduling this subtask"
}}
```

-----
lets' begin 

Here is the information for your decision:

### Workflow Information:
{workflow_graph_representation}

### Workflow Execution History:
{execution_history}

### Workflow Execution Outputs:
{execution_outputs}

### Candidate Subtasks:
{candidate_tasks}

Output:
