---
agent: hindsight
prompt_id: prompts-112c65310018
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.1.0
package_name: null
package_version: null
source_ref: v1.1.0
source_commit: a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_structured_delta_prompt.1
source_lines:
- 1575
- 1580
source_permalink: https://github.com/vectorize-io/hindsight/blob/a5a619b5ca59c5c39e0f96be6f7a31fabd136bd5/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1575-L1580
source_committed_at: '2026-10-21T16:16:23Z'
release_published_at: '2026-10-21T16:41:42Z'
fetched_at: '2026-10-30T05:29:47Z'
extractor_version: 1.0.3
content_sha256: 4c916b90cd9518f84346c04c07e1f2b28f84a5faf73b3f12ad6f380df0552738
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
## Topic\n{source_query}\n\n"
        f"## CURRENT DOCUMENT (apply ops to this; copy section and block ids from it verbatim)\n"
        f"```json\n{fitted.document_json}\n```\n\n"
        f"## SUPPORTING FACTS (new since last refresh — integrate these)\n{fitted.facts}"
        f"{document_hint}{budget_hint}{truncation_note}\n\n"
        f"{task_footer}