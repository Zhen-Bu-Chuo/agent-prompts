---
agent: hindsight
prompt_id: prompts-30e8bf6ef945
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.2.3
package_name: null
package_version: null
source_ref: v1.2.3
source_commit: bd230e8bb40e768bf69f266f1dd3c9ae03e22fe3
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module._fit_structured_delta_prompt_parts.fixed.1
source_lines:
- 1455
- 1461
source_permalink: https://github.com/vectorize-io/hindsight/blob/bd230e8bb40e768bf69f266f1dd3c9ae03e22fe3/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1455-L1461
source_committed_at: '2026-11-19T22:21:53Z'
release_published_at: '2026-11-19T22:48:28Z'
fetched_at: '2026-11-20T08:06:42Z'
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