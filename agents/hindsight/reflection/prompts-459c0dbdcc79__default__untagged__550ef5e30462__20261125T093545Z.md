---
agent: hindsight
prompt_id: prompts-459c0dbdcc79
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 550ef5e304623be2a456913acbac1b1a834fb2c3
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_structured_retraction_prompt.1
source_lines:
- 1818
- 1826
source_permalink: https://github.com/vectorize-io/hindsight/blob/550ef5e304623be2a456913acbac1b1a834fb2c3/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1818-L1826
source_committed_at: '2026-11-24T16:29:36Z'
release_published_at: null
fetched_at: '2026-11-25T09:35:45Z'
extractor_version: 1.0.3
content_sha256: 9af2d8c3e888fe42ad2e511cd27f1641a24dc910fc0006254667b329551f4c1c
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
## Topic\n{source_query}\n\n"
        f"## CURRENT DOCUMENT (apply ops to this; reference section ids as listed)\n"
        f"```json\n{fitted.document_json}\n```\n\n"
        f"## STILL-SUPPORTED FACTS (these remain valid — do not remove content resting on them)\n"
        f"{fitted.candidate}\n\n"
        f"## RETRACTED FACTS (no longer in the memory bank — remove content resting on these)\n"
        f"{fitted.facts}"
        f"{budget_hint}{truncation_note}\n\n"
        f"{task_footer}