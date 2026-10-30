---
agent: dgm
prompt_id: self_improvement_prompt-5c9a1aaaf2fb
module: evolution
variant: default
upstream_repository: jennyzzt/dgm
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
source_path: prompts/self_improvement_prompt.py
source_symbol: module.diagnose_prompt_contextlength.1
source_lines:
- 154
- 172
source_permalink: https://github.com/jennyzzt/dgm/blob/a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/prompts/self_improvement_prompt.py#L154-L172
source_committed_at: '2025-08-13T10:40:14Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:27Z'
extractor_version: 1.0.3
content_sha256: cb434fb60fa9b3ff6bea922e219b6233ec69fd409a03b603286a00fc9c7def0e
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
While the coding agent is attempting to solve GitHub issues, it encounters an error due to the input being too long for the requested model. This error is likely due to the context length exceeding the model's maximum input size. Handle cases where the input is too long for the model. The coding agent is mainly using the file `llm_withtools.py`. LLMs typically have a context window of 200k tokens. Handle context length only if the context window limit is reached and caught as an exception; otherwise, it is okay to leave it as is.

<error_message>
Error in get_response_withtools: Error code: 400 - {'message': 'Input is too long for requested model.'}
</error_message>

Respond precisely in the following format including the JSON start and end markers:

```json
<JSON>
```

In <JSON>, provide a JSON response with the following fields:
- "potential_improvements": Identify potential improvements to the coding agent's system. All necessary dependencies and environment setup have already been handled, so do not focus on these aspects.
- "improvement_proposal": Choose ONE high-impact improvement from the identified potential improvements and describe it in detail. This should be a focused and comprehensive plan to enhance the agent's overall coding ability.
- "implementation_suggestion": Referring to the coding agent's summary and implementation, think critically about what feature could be added or improved to best implement the proposed improvement.
- "problem_description": Phrase the improvement proposal and implementation suggestion as a GitHub issue description. It should clearly describe the feature and details so that a software engineer viewing the issue and the repository can implement it.

Your response will be automatically parsed, so ensure that the string response is precisely in the correct format. Do NOT include the `<JSON>` tag in your output.