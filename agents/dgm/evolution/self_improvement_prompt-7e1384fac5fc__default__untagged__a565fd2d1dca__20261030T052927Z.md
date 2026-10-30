---
agent: dgm
prompt_id: self_improvement_prompt-7e1384fac5fc
module: evolution
variant: default
upstream_repository: jennyzzt/dgm
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
source_path: prompts/self_improvement_prompt.py
source_symbol: module.diagnose_prompt_emptypatches_polyglot.1
source_lines:
- 254
- 275
source_permalink: https://github.com/jennyzzt/dgm/blob/a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/prompts/self_improvement_prompt.py#L254-L275
source_committed_at: '2025-08-13T10:40:14Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:27Z'
extractor_version: 1.0.3
content_sha256: bf45b59cbafadf62370d8f2a4039d01f7bdf3f1175506e6fd0dcd4acab85e074
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
There are some empty patches when attempting to solve GitHub issues. Since the coding agent is stochastic, it may not always produce a patch. Handle cases where the coding agent fails to generate a patch or generates one that only modifies the test cases without editing the primary source code. For example, the simplest solution is to change the prompt to specifically make sure it called the edit tool.

Please analyze the log below to identify why no code edits were made.

# Agent Running Log
----- Agent Running Log Start -----
{md_log}
----- Agent Running Log End -----

Respond precisely in the following format including the JSON start and end markers:

```json
<JSON>
```

In <JSON>, provide a JSON response with the following fields:
- "potential_improvements": Identify potential improvements to the coding agent's system. All necessary dependencies and environment setup have already been handled, so do not focus on these aspects.
- "improvement_proposal": Choose ONE high-impact improvement from the identified potential improvements and describe it in detail. This should be a focused and comprehensive plan to enhance the agent's overall coding ability.
- "implementation_suggestion": Referring to the coding agent's summary and implementation, think critically about what feature could be added or improved to best implement the proposed improvement.
- "problem_description": Phrase the improvement proposal and implementation suggestion as a GitHub issue description. It should clearly describe the feature so that a software engineer viewing the issue and the repository can implement it.

Your response will be automatically parsed, so ensure that the string response is precisely in the correct format. Do NOT include the `<JSON>` tag in your output.