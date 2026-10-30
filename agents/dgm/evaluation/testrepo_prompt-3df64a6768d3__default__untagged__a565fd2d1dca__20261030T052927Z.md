---
agent: dgm
prompt_id: testrepo_prompt-3df64a6768d3
module: evaluation
variant: default
upstream_repository: jennyzzt/dgm
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
source_path: prompts/testrepo_prompt.py
source_symbol: module.get_test_command.test_hint.1
source_lines:
- 12
- 12
source_permalink: https://github.com/jennyzzt/dgm/blob/a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/prompts/testrepo_prompt.py#L12-L12
source_committed_at: '2025-08-13T10:40:14Z'
release_published_at: null
fetched_at: '2026-10-30T05:29:27Z'
extractor_version: 1.0.3
content_sha256: 18c7383628c0a08449f550ee3204370957449999de82888de303dd5502ed166d
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
If the target test file path is tests/some_folder/some_file.py, then <specific test files> should be `some_folder.some_file`.