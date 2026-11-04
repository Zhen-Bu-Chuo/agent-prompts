---
agent: hindsight
prompt_id: prompts-30e8bf6ef945
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: f14cc1eb5624b0374cb4d82768eb2e0b9c21ae24
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module._fit_structured_delta_prompt_parts.fixed.1
source_lines:
- 1447
- 1453
source_permalink: https://github.com/vectorize-io/hindsight/blob/f14cc1eb5624b0374cb4d82768eb2e0b9c21ae24/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1447-L1453
source_committed_at: '2026-11-03T15:26:23Z'
release_published_at: null
fetched_at: '2026-11-04T07:16:29Z'
extractor_version: 1.0.3
content_sha256: 71e2793e0388c4a7e041c88d0f8032d3f9185e1f8e0a1e0a575028ec56a78d68
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
## Topic\n{source_query}\n\n"
        f"## CURRENT DOCUMENT (apply ops to this; copy section and block ids from it verbatim)\n"
        f"```json\n\n```\n\n"
        f"## CANDIDATE SLOT (the retraction prompt's still-supported facts)\n\n"
        f"## SUPPORTING FACTS (recorded since last refresh — integrate what the document does not already say)\n"
        f"{budget_hint}\n\n"
        f"{task_footer}