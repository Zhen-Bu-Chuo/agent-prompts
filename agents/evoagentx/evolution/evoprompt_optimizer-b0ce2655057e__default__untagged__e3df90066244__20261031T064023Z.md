---
agent: evoagentx
prompt_id: evoprompt_optimizer-b0ce2655057e
module: evolution
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: e3df900662443e94dd92141be5633b040a69a70a
source_path: evoagentx/optimizers/evoprompt_optimizer.py
source_symbol: module.EvopromptOptimizer.__init__.self.paraphrase_agent.1
source_lines:
- 110
- 118
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/e3df900662443e94dd92141be5633b040a69a70a/evoagentx/optimizers/evoprompt_optimizer.py#L110-L118
source_committed_at: '2026-10-31T01:49:52Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:23Z'
extractor_version: 1.0.3
content_sha256: bd7e4fdb2e573cfad1d93eac064dcb09d12cb377f1ca33ab3eb8731903dbe394
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Task: Generate a semantically equivalent but differently worded version of the user-provided instruction.
                    
Now, please process the following instruction:
Input: {instruction}

Please provide the paraphrased version in the following format:

## paraphrased_instruction
[Your paraphrased version here]