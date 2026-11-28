---
agent: hindsight
prompt_id: prompts-bb075917ca8e
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: c828c7e41527d0c4916cac0ba2b56334fed4a79d
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.20
source_lines:
- 354
- 356
source_permalink: https://github.com/vectorize-io/hindsight/blob/c828c7e41527d0c4916cac0ba2b56334fed4a79d/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L354-L356
source_committed_at: '2026-11-27T17:40:16Z'
release_published_at: null
fetched_at: '2026-11-28T08:41:49Z'
extractor_version: 1.0.3
content_sha256: d6c7bbd36dbef6f2252a48a4d2b9b8ad967d6245aa610e916e058c76ede20b86
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
- Search returns the best matches in full (`content`) and a SNIPPET of the others (`snippet`, only the page opening); call read_mental_models on any id whose snippet looks like it answers the question, and read it before answering from it