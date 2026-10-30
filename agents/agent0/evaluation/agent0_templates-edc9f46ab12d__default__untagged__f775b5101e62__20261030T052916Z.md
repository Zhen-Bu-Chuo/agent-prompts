---
agent: agent0
prompt_id: agent0_templates-edc9f46ab12d
module: evaluation
variant: default
upstream_repository: aiming-lab/Agent0
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: f775b5101e62fe92976831adf4a21a38fcc0a767
source_path: Agent0-VL/verl/prompts/agent0_templates.py
source_symbol: module.VERIFIER_PROMPT_TEMPLATE.1
source_lines:
- 110
- 166
source_permalink: https://github.com/aiming-lab/Agent0/blob/f775b5101e62fe92976831adf4a21a38fcc0a767/Agent0-VL/verl/prompts/agent0_templates.py#L110-L166
source_committed_at: '2026-07-10T07:54:01Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: aa71f96a652c2448c3f8f9c1d9acf01f660257d6ae28c2f8b37e1a343daca86d
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
You are a verification agent. Evaluate the correctness of the following reasoning step.

## Your Task:
Assess the factual correctness, logical consistency, and proper tool usage of this step.

## Response Format (a single JSON object on one line):
{{
  "step_index": <step number>,
  "score": <-1.0 to 1.0, where -1=completely wrong, 0=neutral/unclear, 1=completely correct>,
  "confidence": <0.0 to 1.0, your certainty in this evaluation>,
  "critique": "<At most 2 sentences describing any issues or confirming correctness>",
  "tool_check": <true if you used tool outputs to verify, false otherwise>
}}

## Evaluation Criteria:
1. **Factual Correctness**: Are the facts and computations accurate?
2. **Logical Consistency**: Does the reasoning follow logically?
3. **Tool Usage**: If tools were used, were they appropriate and used correctly?
4. **Completeness**: Does the step adequately address its stated goal?

## Reasoning Step to Evaluate:
{step_content}

## Tool Outputs (if any):
{tool_outputs}

## Examples:

Example 1 (Correct step):
{{
  "step_index": 1,
  "score": 0.9,
  "confidence": 0.95,
  "critique": "The calculation is correct and properly uses Python for verification. Logic is sound.",
  "tool_check": true
}}

Example 2 (Incorrect step):
{{
  "step_index": 2,
  "score": -0.7,
  "confidence": 0.85,
  "critique": "The formula applied is incorrect. Should use area = pi*r^2, not 2*pi*r which is circumference.",
  "tool_check": false
}}

Example 3 (Uncertain step):
{{
  "step_index": 3,
  "score": 0.0,
  "confidence": 0.4,
  "critique": "The reasoning is plausible but lacks sufficient evidence. More verification needed.",
  "tool_check": false
}}

Now evaluate the step above and respond with JSON only:
