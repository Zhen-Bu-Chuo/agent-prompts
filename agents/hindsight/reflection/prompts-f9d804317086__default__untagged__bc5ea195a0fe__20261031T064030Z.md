---
agent: hindsight
prompt_id: prompts-f9d804317086
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: bc5ea195a0fed1346ff171a5780bbb72a38c89c8
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_structured_retraction_prompt.task_footer.1
source_lines:
- 1768
- 1771
source_permalink: https://github.com/vectorize-io/hindsight/blob/bc5ea195a0fed1346ff171a5780bbb72a38c89c8/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1768-L1771
source_committed_at: '2026-10-30T23:40:41Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:30Z'
extractor_version: 1.0.3
content_sha256: ad5ae1cd2f7830bf577c06d9363245c5c80654bfef868158d271f5449f6cf348
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
## Task
Output a JSON object matching the operations schema, removing content that rests on the RETRACTED FACTS. Leave everything else untouched. Emit ``{"operations": []}`` if nothing in the document rests on them.