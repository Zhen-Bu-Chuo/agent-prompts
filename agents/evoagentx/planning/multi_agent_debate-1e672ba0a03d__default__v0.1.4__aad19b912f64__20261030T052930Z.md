---
agent: evoagentx
prompt_id: multi_agent_debate-1e672ba0a03d
module: planning
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: v0.1.4
package_name: null
package_version: null
source_ref: v0.1.4
source_commit: aad19b912f640161ea07e8904d9237cd34fde5f1
source_path: evoagentx/prompts/workflow/multi_agent_debate.py
source_symbol: module.JUDGE_AGENT_PROMPT.1
source_lines:
- 46
- 64
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/prompts/workflow/multi_agent_debate.py#L46-L64
source_committed_at: '2026-06-28T10:20:05Z'
release_published_at: '2026-06-28T10:24:06Z'
fetched_at: '2026-10-30T05:29:30Z'
extractor_version: 1.0.3
content_sha256: c176a5d3d943c578eeb6bcddde803209e76b65dd3db38773d820efe8fd0d5882
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

You are the judge. Based on the multi-round debate, deliver a final decision and answer.

Problem:
{problem}

Debater roles:
{roles_text}

Debate transcript:
{transcript_text}

Return the following XML:
<response>
  <rationale>Your judging rationale</rationale>
  <winning_agent_id>Winning debater ID (integer)</winning_agent_id>
  <final_answer>The final answer</final_answer>
</response>
