---
agent: dgm
prompt_id: testrepo_prompt-80c03195bf38
module: evaluation
variant: default
upstream_repository: jennyzzt/dgm
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
source_path: prompts/testrepo_prompt.py
source_symbol: module.get_test_description.description.2
source_lines:
- 28
- 28
source_permalink: https://github.com/jennyzzt/dgm/blob/a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/prompts/testrepo_prompt.py#L28-L28
source_committed_at: '2025-08-13T10:40:14Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:27Z'
extractor_version: 1.0.3
content_sha256: 0f50ce8cf556f084e1c807c4b3415d6f234e03f4fd3696c203d0179ef72eb0ed
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
The tests in the repository can be run with the bash command `cd /dgm/ && pytest -rA <specific test files>`. If no specific test files are provided, all tests will be run. The given command-line options must be used EXACTLY as specified. Do not use any other command-line options. ONLY test tools and utils. NEVER try to test or run agentic_system.forward().