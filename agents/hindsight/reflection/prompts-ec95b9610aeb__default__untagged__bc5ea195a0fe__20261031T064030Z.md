---
agent: hindsight
prompt_id: prompts-ec95b9610aeb
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: bc5ea195a0fed1346ff171a5780bbb72a38c89c8
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_chunk_claims_prompt.1
source_lines:
- 1048
- 1051
source_permalink: https://github.com/vectorize-io/hindsight/blob/bc5ea195a0fed1346ff171a5780bbb72a38c89c8/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1048-L1051
source_committed_at: '2026-10-30T23:40:41Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:30Z'
extractor_version: 1.0.3
content_sha256: 9d26a76c942bbb77089037d99a8b093bd73582917d0cad638bd25ca26e3d4cb0
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

## Instructions
List every claim in the retrieved data relevant to the question, one bullet per claim, each with its (mentioned_at: ...; occurred: ...; memory_ids: ...) provenance. Do not answer the question.