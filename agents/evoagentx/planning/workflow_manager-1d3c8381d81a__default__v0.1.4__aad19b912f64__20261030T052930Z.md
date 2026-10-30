---
agent: evoagentx
prompt_id: workflow_manager-1d3c8381d81a
module: planning
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: v0.1.4
package_name: null
package_version: null
source_ref: v0.1.4
source_commit: aad19b912f640161ea07e8904d9237cd34fde5f1
source_path: evoagentx/prompts/workflow/workflow_manager.py
source_symbol: module.WORKFLOW_OUTPUT_EXTRACTION_PROMPT.1
source_lines:
- 175
- 204
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/workflow/workflow_manager.py#L175-L204
source_committed_at: '2026-06-28T10:20:05Z'
release_published_at: '2026-06-28T10:24:06Z'
fetched_at: '2026-10-30T05:29:30Z'
extractor_version: 1.0.3
content_sha256: 4ec36be37bf4f65ea1f45b476f4934be3054f85bc057e14a1b03188774a56717
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

### Objective 
Your goal is to read the Workflow Goal, the WorkFlow Information, and the WorkFlow Execution Results from the provided input. Then, based on those details, extract and present ONLY the FINAL output data that meets the Workflow Goal.

### Instructions 
1. Carefully analyze the Workflow Goal to understand the specific objective.
2. Review the WorkFlow Information (including the workflow graph and any steps or dependencies) to see how tasks are organized or connected.
3. Inspect the WorkFlow Execution Results to determine which parts directly contribute to the final required output.
4. Ignore any information that does not help fulfill the stated Workflow Goal (such as intermediate debug logs, partial results not relevant to the final outcome, or any extraneous details).
5. Provide your extracted final output in a concise and clear form that directly meets the Workflow Goal.

### Note
1. If you need to extract generated code, DO NOT change the provided code. 

--- 
lets' begin 

Here is your information for extracting the workflow output: 

### Workflow Goal:
{goal}

### WorkFlow Information:
{workflow_graph_representation}

### WorkFlow Execution Results:
{workflow_execution_results}

Now, based on the workflow information and execution results, provide your extracted output.
