---
agent: dgm
prompt_id: diagnose_improvement_prompt-26a0836e0c9b
module: reflection
variant: default
upstream_repository: jennyzzt/dgm
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
source_path: prompts/diagnose_improvement_prompt.py
source_symbol: module.diagnose_improvement_system_message.1
source_lines:
- 5
- 37
source_permalink: https://github.com/jennyzzt/dgm/blob/a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/prompts/diagnose_improvement_prompt.py#L5-L37
source_committed_at: '2025-08-13T10:40:14Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:27Z'
extractor_version: 1.0.3
content_sha256: 191f31bf0392c642abeaa83170c709f2848b9bb443639bd59577f53434a0e6ff
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Here is the relevant code for the LLM Coding agent with the model patch applied.

# LLM Coding Agent Code
The current code of LLM coding agent.
----- LLM Coding Agent Code Start -----
{code}
----- LLM Coding Agent Code End -----

# LLM Coding Agent Code Patch
The edits of LLM coding agent from the previous improvement.
----- LLM Coding Agent Code Patch Start -----
{model_patch_text}
----- LLM Coding Agent Code Patch End -----

# Test Patch
SWE-bench's official private tests to detect whether the issue is solved.
----- Test Patch Start -----
{test_patch}
----- Test Patch End -----

# Answer Patch
SWE-bench's official answer patch to the issue.
----- Answer Patch Start -----
{answer_patch}
----- Answer Patch End -----

# Your Task
Your task is to identify:
1. If the model patch has improved the agent's coding capabilities.
2. If the model patch has introduced any new issues or regressions.

Give a detailed analysis of the agent's performance before and after applying the model patch. Focus on the impact of the patch on the agent's problem-solving capabilities and general performance.
