---
agent: hindsight
prompt_id: prompts-224f7b732724
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.1.0
package_name: null
package_version: null
source_ref: v1.1.0
source_commit: a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_system_prompt_for_tools.44
source_lines:
- 582
- 584
source_permalink: https://github.com/vectorize-io/hindsight/blob/a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L582-L584
source_committed_at: '2026-10-21T16:16:23Z'
release_published_at: '2026-10-21T16:41:42Z'
fetched_at: '2026-10-30T05:29:47Z'
extractor_version: 1.0.3
content_sha256: 0dec92ad3afea91901c7d96fb434a6f0d98bc4fdefd709a037f921f7e22f38df
license: MIT
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
- 'document' holds a 'sections' array — one entry per section, in order. Shape: {"sections": [{"heading": "Overview", "level": 2, "blocks": ["First paragraph.", "- a list item\n- another"]}]}