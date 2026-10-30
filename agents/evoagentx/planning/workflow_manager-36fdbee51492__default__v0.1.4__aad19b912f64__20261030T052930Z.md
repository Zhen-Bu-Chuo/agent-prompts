---
agent: evoagentx
prompt_id: workflow_manager-36fdbee51492
module: planning
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: v0.1.4
package_name: null
package_version: null
source_ref: v0.1.4
source_commit: aad19b912f640161ea07e8904d9237cd34fde5f1
source_path: evoagentx/prompts/workflow/workflow_manager.py
source_symbol: module.DEFAULT_ACTION_SCHEDULER_PROMPT.1
source_lines:
- 113
- 166
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/workflow/workflow_manager.py#L113-L166
source_committed_at: '2026-06-28T10:20:05Z'
release_published_at: '2026-06-28T10:24:06Z'
fetched_at: '2026-10-30T05:29:30Z'
extractor_version: 1.0.3
content_sha256: d46a7030a64e80bfbf4a693f1870688fdcec91e287c481c44e78f27a361cfaeb
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

### Objective
Your task is to analyze the given subtask, its input data, execution history, and the available agents with their actions to **determine the next action to be executed**. Since completing this subtask requires multiple actions, you should select only **one** action at a time that logically continues the execution process.

### Instructions
1. Review the Subtask Information to understand its requirements, dependencies, and expected outcomes.
2. Analyze the Subtask Input Data to determine what information is already available for execution.
3. Check the Subtask Execution History to evaluate:
   - Which actions have already been executed.
   - Whether any errors or missing information exist.
   - What the next logical step should be.
4. Evaluate the Available Agents and Their Actions to identify the most suitable action by considering:
   - Whether an agent has the necessary capabilities to perform the next step.
   - Whether an agent has successfully performed a similar action before.
   - Whether selecting this action helps in progressing toward subtask completion.
5. Select the Best Agent and Action for the next execution step.
6. Output the decision in the required format.

### Output Format
Your final output should ALWAYS be in the following format:

## Thought  
Provide a brief explanation of your reasoning for selecting the agent and action.

## Scheduled Execution  
Produce your answer in valid JSON with the following structure:
```json
{{
    "agent": "name of the selected agent, should be EXACTLY the same as the provided agent name",
    "action": "name of the selected action, should be EXACTLY the same as the provided action name",
    "reason": "the reasoning for selecting this agent and action"
}}
```
Note that the `action` field of the output should be chosen from the provided action names. DON'T generate your own action name.

-----
lets' begin 

Here is the information for your decision:

### SubTask Information 
{task_info}

### SubTask Input data 
{task_inputs}

### SubTask Execution History 
{task_execution_history}

### Available Agents and Actions 
{agent_action_list}

Output:
