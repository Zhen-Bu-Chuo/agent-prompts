---
agent: evoagentx
prompt_id: workflow_manager-da2ae87bfa9c
module: planning
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: v0.1.4
package_name: null
package_version: null
source_ref: v0.1.4
source_commit: aad19b912f640161ea07e8904d9237cd34fde5f1
source_path: evoagentx/prompts/workflow/workflow_manager.py
source_symbol: module.OLD_DEFAULT_TASK_SCHEDULER_PROMPT.1
source_lines:
- 52
- 101
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/workflow/workflow_manager.py#L52-L101
source_committed_at: '2026-06-28T10:20:05Z'
release_published_at: '2026-06-28T10:24:06Z'
fetched_at: '2026-10-30T05:29:30Z'
extractor_version: 1.0.3
content_sha256: af191d6b62158985e79cddeca50bce2f321b364b31821bd6cb0d780328bb7cf4
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

### objective
Your task is to analyze the given workflow graph, current execution information, and candidate subtasks to decide one of the following actions:
- Re-execute a previous subtask to correct errors or gather missing information (if a previous subtask's result is erroneous or incomplete). You may only re-execute each task up to {max_num_turns} times, based on the `Workflow Execution History`. 
- Select a subtask for iterative execution (if there is a loop or iterative context in the workflow). You may only iterate on each task up to {max_num_turns} times, also determined by the `Workflow Execution History`. 
- Select a new subtask from the candidates to move the workflow forward (if the workflow should proceed without re-executing or iterating).

### Instructions
1. Review the Workflow Information for the structure and details of the tasks and any potential loops or iterative sections.
2. Check the Current Execution Information for evidence of errors or missing data from previously executed subtasks.
3. If you identify a past subtask with clear errors or missing data, propose a re-execute decision on that subtask.
4. If the workflow graph indicates there is a loop or iterative context, select a subtask from the Candidate Subtasks that aligns with that iterative or looping goal.
5. Otherwise, select a subtask from the Candidate Subtasks that best moves the workflow forward.
6. Finally, output the decision in the required format.

### Output Format
Your final output should ALWAYS in the following format:

## Thought 
Provide a brief explanation of your reasoning for scheduling the next task.

## Scheduled Subtask 
Produce your answer in valid JSON with the following structure: 
```json
{{
    "decision": "re-execute | iterate | forward",
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
