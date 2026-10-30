---
agent: dgm
prompt_id: testrepo_prompt-7c35f389aa3e
module: evaluation
variant: default
upstream_repository: jennyzzt/dgm
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
source_path: prompts/testrepo_prompt.py
source_symbol: module.get_test_description.swe_prompt.1
source_lines:
- 22
- 22
source_permalink: https://github.com/jennyzzt/dgm/blob/a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/prompts/testrepo_prompt.py#L22-L22
source_committed_at: '2025-08-13T10:40:14Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:27Z'
extractor_version: 1.0.3
content_sha256: f1bfaf212f3aa940d60affb94bcbb1faa3ab3e680af747c68c0a423340b31e5e
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
The tests in the repository can be run with the bash command `{test_command}`. If no specific test files are provided, all tests will be run. The given command-line options must be used EXACTLY as specified. Do not use any other command-line options. {test_hint}