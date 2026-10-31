---
agent: evoagentx
prompt_id: multi_agent_debate-c1180c5ec309
module: planning
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: e3df900662443e94dd92141be5633b040a69a70a
source_path: evoagentx/prompts/workflow/multi_agent_debate.py
source_symbol: module.DEBATER_AGENT_PROMPT.1
source_lines:
- 24
- 43
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/e3df900662443e94dd92141be5633b040a69a70a/evoagentx/prompts/workflow/multi_agent_debate.py#L24-L43
source_committed_at: '2026-10-31T01:49:52Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:23Z'
extractor_version: 1.0.3
content_sha256: 27c74bd0e641226981463925fce52f3f9feda1fd8d0fb92a0e342cfff568e43a
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

You are debater #{agent_id} (role: {role}). This is round {round_index} of {total_rounds}.

Problem:
{problem}

Conversation so far:
{transcript_text}

Instructions:
- Think briefly (<= 120 words), then present your argument or rebuttal.
- If confident, provide your current answer for this round.
- Your output MUST follow this XML template:

<response>
  <thought>Your brief reasoning</thought>
  <argument>Your argument or rebuttal</argument>
  <answer>Optional current answer; leave empty if uncertain</answer>
</response>
