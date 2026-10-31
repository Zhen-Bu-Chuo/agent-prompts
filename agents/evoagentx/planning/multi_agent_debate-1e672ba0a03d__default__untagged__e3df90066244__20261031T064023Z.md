---
agent: evoagentx
prompt_id: multi_agent_debate-1e672ba0a03d
module: planning
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: e3df900662443e94dd92141be5633b040a69a70a
source_path: evoagentx/prompts/workflow/multi_agent_debate.py
source_symbol: module.JUDGE_AGENT_PROMPT.1
source_lines:
- 46
- 64
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/e3df900662443e94dd92141be5633b040a69a70a/evoagentx/prompts/workflow/multi_agent_debate.py#L46-L64
source_committed_at: '2026-10-31T01:49:52Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:23Z'
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
