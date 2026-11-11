---
agent: hindsight
prompt_id: prompts-84ba73fa5c41
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 289fb421bdb438861480720e947874551ac42ff7
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.42
source_lines:
- 552
- 553
source_permalink: https://github.com/vectorize-io/hindsight/blob/289fb421bdb438861480720e947874551ac42ff7/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L552-L553
source_committed_at: '2026-11-10T17:14:29Z'
release_published_at: null
fetched_at: '2026-11-11T07:30:35Z'
extractor_version: 1.0.3
content_sha256: 0badb5e827c9ffe187f01ab6bb711925981b9d12ef4140f592c3a0697671b3ac
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
If there is no mental model, it's stale, OR it does not state the answer, use recall() for raw facts. Reporting that nothing is known requires recall() first