---
agent: evoagentx
prompt_id: evoprompt_optimizer-b0ce2655057e
module: evolution
variant: default
upstream_repository: ANative-Lab/EvoAgentX
upstream_version: v0.1.4
package_name: null
package_version: null
source_ref: v0.1.4
source_commit: aad19b912f640161ea07e8904d9237cd34fde5f1
source_path: evoagentx/optimizers/evoprompt_optimizer.py
source_symbol: module.EvopromptOptimizer.__init__.self.paraphrase_agent.1
source_lines:
- 106
- 114
source_permalink: https://github.com/ANative-Lab/EvoAgentX/blob/aad19b912f640161ea07e8904d9237cd34fde5f1/evoagentx/optimizers/evoprompt_optimizer.py#L106-L114
source_committed_at: '2026-06-28T10:20:05Z'
release_published_at: '2026-06-28T10:24:06Z'
fetched_at: '2026-10-30T05:29:30Z'
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