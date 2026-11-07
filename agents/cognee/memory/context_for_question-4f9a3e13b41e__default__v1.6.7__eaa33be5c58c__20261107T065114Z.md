---
agent: cognee
prompt_id: context_for_question-4f9a3e13b41e
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.7
package_name: null
package_version: null
source_ref: v1.6.7
source_commit: eaa33be5c58cd14584e64e3e0ed2e1479472ee09
source_path: cognee/infrastructure/llm/prompts/context_for_question.txt
source_symbol: document
source_lines:
- 1
- 2
source_permalink: https://github.com/topoteretes/cognee/blob/eaa33be5c58cd14584e64e3e0ed2e1479472ee09/cognee/infrastructure/llm/prompts/context_for_question.txt#L1-L2
source_committed_at: '2026-11-06T17:10:58Z'
release_published_at: '2026-11-06T17:15:07Z'
fetched_at: '2026-11-07T06:51:14Z'
extractor_version: 1.0.3
content_sha256: 5266f6608b552e729fe873bd61880d2d89401896f1107fc54834b52b83b29802
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
The question is: `{{ question }}`
And here is the context: `{{ context }}`
