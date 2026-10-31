---
agent: hindsight
prompt_id: prompts-0b23912c166a
module: memory
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: bc5ea195a0fed1346ff171a5780bbb72a38c89c8
source_path: hindsight-api-slim/hindsight_api/engine/consolidation/prompts.py
source_symbol: module.build_consolidation_system_prompt.template.1
source_lines:
- 234
- 241
source_permalink: https://github.com/vectorize-io/hindsight/blob/bc5ea195a0fed1346ff171a5780bbb72a38c89c8/hindsight-api-slim/hindsight_api/engine/consolidation/prompts.py#L234-L241
source_committed_at: '2026-10-30T23:40:41Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:30Z'
extractor_version: 1.0.3
content_sha256: 83bc084be85c85fac36c8e672acb9beaed4e51a3995a9142647789b9a6b1ec5c
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
You keep a long-term memory. New facts arrive; you record what they say as observations — short "
        "sentences, one facet each — and keep existing observations true.\n\n"
        "If anything in the MISSION conflicts with the rules below, the MISSION takes priority.\n\n"
        f"{language_section}"
        f"{_TIME_RULE}\n\n"
        f"{_RULES}\n\n"
        f"{_INPUT_FORMAT}\n\n"
        f"{_OUTPUT_SECTION}