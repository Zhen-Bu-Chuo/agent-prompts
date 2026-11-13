---
agent: hindsight
prompt_id: prompts-17953ad4f5f1
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 9a730fa95a6453785341adaa436a9453ed5ebf7e
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_reduce_prompt.2
source_lines:
- 1092
- 1096
source_permalink: https://github.com/vectorize-io/hindsight/blob/9a730fa95a6453785341adaa436a9453ed5ebf7e/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1092-L1096
source_committed_at: '2026-11-12T19:42:59Z'
release_published_at: null
fetched_at: '2026-11-13T07:38:36Z'
extractor_version: 1.0.3
content_sha256: c20a02ab0508c0c8ad14a658078dc04263c5f2e0226c5daa4c728dea9d1dee67
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

## Instructions
When claims about the same fact conflict, the claim with the LATEST mentioned_at date is authoritative — later statements supersede earlier ones, regardless of which section they appear in. If equally-recent claims disagree and nothing resolves them, say so explicitly rather than picking one.

