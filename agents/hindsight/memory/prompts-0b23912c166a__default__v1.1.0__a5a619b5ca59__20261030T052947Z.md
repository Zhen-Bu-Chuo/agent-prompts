---
agent: hindsight
prompt_id: prompts-0b23912c166a
module: memory
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.1.0
package_name: null
package_version: null
source_ref: v1.1.0
source_commit: a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5
source_path: hindsight-api-slim/hindsight_api/engine/consolidation/prompts.py
source_symbol: module.build_consolidation_system_prompt.template.1
source_lines:
- 204
- 211
source_permalink: https://github.com/vectorize-io/hindsight/blob/a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5/hindsight-api-slim/hindsight_api/engine/consolidation/prompts.py#L204-L211
source_committed_at: '2026-10-21T16:16:23Z'
release_published_at: '2026-10-21T16:41:42Z'
fetched_at: '2026-10-30T05:29:47Z'
extractor_version: 1.0.3
content_sha256: 6f13b361f6c47eda6a4c0c03ec8aa73c63b4d0986bda265195d0f99cf10277d0
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
You are a memory consolidation system. Synthesize new facts into "
        "observations, merging with existing observations when appropriate.\n\n"
        f"{_MISSION_PRIORITY_NOTE}\n\n"
        f"{language_section}"
        f"{_PROCESSING_RULES}\n\n"
        f"{_INPUT_FORMAT_NOTE}\n\n"
        f"{_DECISION_GUIDE}\n\n"
        f"{_OUTPUT_SECTION}