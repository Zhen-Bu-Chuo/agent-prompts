---
agent: dgm
prompt_id: self_improvement_prompt-6f71597a3b0b
module: evolution
variant: default
upstream_repository: jennyzzt/dgm
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
source_path: prompts/self_improvement_prompt.py
source_symbol: module.diagnose_prompt_stochasticity.1
source_lines:
- 138
- 152
source_permalink: https://github.com/jennyzzt/dgm/blob/a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/prompts/self_improvement_prompt.py#L138-L152
source_committed_at: '2025-08-13T10:40:14Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:27Z'
extractor_version: 1.0.3
content_sha256: 9485cded6202f330a201ab51d2fb7fc57ccc415e656bab0aa3f78f60017dcbd8
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Since the coding agent is stochastic, it may not produce the correct patch for the given problem statement on the first try. Take into account the agent's stochastic nature and provide a solution to handle such cases. For example, one solution could be to ask the agent to try multiple times and select the best patch. The file `utils/eval_utils.py` contains helper functions to evaluate the generated patches. Giving previous attempts as context to the agent may also help.

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