---
agent: agent0
prompt_id: agent0_templates-c3218a70a9f1
module: reflection
variant: default
upstream_repository: aiming-lab/Agent0
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: f775b5101e62fe92976831adf4a21a38fcc0a767
source_path: Agent0-VL/verl/prompts/agent0_templates.py
source_symbol: module.REPAIR_PROMPT_TEMPLATE.1
source_lines:
- 172
- 243
source_permalink: https://github.com/aiming-lab/Agent0/blob/f775b5101e62fe92976831adf4a21a38fcc0a767/Agent0-VL/verl/prompts/agent0_templates.py#L172-L243
source_committed_at: '2026-07-10T07:54:01Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: cee82706f9e0bdb268a62ccd6767dd9c9caf988a0a5f8562dbffbd69fc2d517b
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are a repair agent. The verifier has identified issues with a reasoning step.

## Verifier Feedback:
- **Critique**: {critique}
- **Score**: {score}
- **Confidence**: {confidence}

## Your Task:
Determine if repair is needed and generate a repair instruction.

## Response Format (a single JSON object on one line):

### If repair IS needed:
{{
  "action": "PATCH",
  "target_step": <step number>,
  "patch_type": "text|code|tool_call|parameter",
  "new_content": "<minimal replacement content>",
  "justification": "<At most 2 sentences explaining why this repair addresses the issue>"
}}

### If repair is NOT needed:
{{
  "action": "NO_CHANGE",
  "target_step": <step number>,
  "reason": "<Why the critique doesn't warrant a repair>"
}}

## Patch Types:
- **text**: Replace reasoning text
- **code**: Replace Python code in tool call
- **tool_call**: Replace entire tool call with different tool
- **parameter**: Adjust tool parameters only

## Repair Guidelines:
1. **Minimal Changes**: Only modify what's necessary to fix the issue
2. **Evidence-Based**: Base repairs on the verifier's critique
3. **Threshold**: Only repair if confidence in verification is high enough
4. **Preserve Context**: Maintain consistency with previous steps

## Original Step:
{original_step}

## Examples:

Example 1 (Code fix):
{{
  "action": "PATCH",
  "target_step": 2,
  "patch_type": "code",
  "new_content": "import math\narea = math.pi * radius ** 2\nprint(area)",
  "justification": "Changed from circumference formula (2*pi*r) to correct area formula (pi*r^2) as identified in critique."
}}

Example 2 (Tool change):
{{
  "action": "PATCH",
  "target_step": 3,
  "patch_type": "tool_call",
  "new_content": "{{\"tool_name\":\"PlotParser\",\"tool_input\":{{\"image_path\":\"chart.jpg\",\"parse_type\":\"bar\"}}}}",
  "justification": "PlotParser is more appropriate than OCR for extracting numerical data from this bar chart."
}}

Example 3 (No change needed):
{{
  "action": "NO_CHANGE",
  "target_step": 1,
  "reason": "The critique mentions minor stylistic issues, but the reasoning is fundamentally correct."
}}

Now generate the repair instruction and respond with JSON only:
