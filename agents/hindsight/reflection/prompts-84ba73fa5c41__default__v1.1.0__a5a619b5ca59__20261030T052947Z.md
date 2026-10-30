---
agent: hindsight
prompt_id: prompts-84ba73fa5c41
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.1.0
package_name: null
package_version: null
source_ref: v1.1.0
source_commit: a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.42
source_lines:
- 551
- 552
source_permalink: https://github.com/vectorize-io/hindsight/blob/a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L551-L552
source_committed_at: '2026-10-21T16:16:23Z'
release_published_at: '2026-10-21T16:41:42Z'
fetched_at: '2026-10-30T05:29:47Z'
extractor_version: 1.0.3
content_sha256: 0badb5e827c9ffe187f01ab6bb711925981b9d12ef4140f592c3a0697671b3ac
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
If there is no mental model, it's stale, OR it does not state the answer, use recall() for raw facts. Reporting that nothing is known requires recall() first