---
agent: evoagentx
prompt_id: evoprompt_optimizer-1c29a49eb141
module: evolution
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: e3df900662443e94dd92141be5633b040a69a70a
source_path: evoagentx/optimizers/evoprompt_optimizer.py
source_symbol: module.DEOptimizer.__init__.self.de_agent.1
source_lines:
- 1009
- 1026
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/e3df900662443e94dd92141be5633b040a69a70a/evoagentx/optimizers/evoprompt_optimizer.py#L1009-L1026
source_committed_at: '2026-10-31T01:49:52Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:23Z'
extractor_version: 1.0.3
content_sha256: 99694f87e260425f8273a1bdf82875425841b6977264e2a371c3307bc825da61
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Please follow the instructions step-by-step to generate a better prompt using Differential Evolution strategy.

1. Identify the different parts between these two donor prompts:
Donor Prompt 1: {donor1}
Donor Prompt 2: {donor2}

2. Randomly mutate the different parts identified above.

3. Combine the mutated parts with the best prompt, selectively replacing its content:
Best Prompt: {best_prompt}

4. Crossover the result from Step 3 with the current prompt to generate the final evolved prompt. Strictly preserve the original XML tags structure:
Current Prompt: {current_prompt}

Please provide the final evolved prompt in the following format:

## evolved_prompt
[Your evolved prompt here]