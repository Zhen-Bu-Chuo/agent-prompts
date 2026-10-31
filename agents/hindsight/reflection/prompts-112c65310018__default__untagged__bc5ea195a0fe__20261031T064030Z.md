---
agent: hindsight
prompt_id: prompts-112c65310018
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: bc5ea195a0fed1346ff171a5780bbb72a38c89c8
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_structured_delta_prompt.1
source_lines:
- 1641
- 1646
source_permalink: https://github.com/vectorize-io/hindsight/blob/bc5ea195a0fed1346ff171a5780bbb72a38c89c8/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1641-L1646
source_committed_at: '2026-10-30T23:40:41Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:30Z'
extractor_version: 1.0.3
content_sha256: a69e22cc47e31c5bfb0a47494426285ade493daac899bb60cc70fbd893c369cf
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
## Topic\n{source_query}\n\n"
        f"## CURRENT DOCUMENT (apply ops to this; copy section and block ids from it verbatim)\n"
        f"```json\n{fitted.document_json}\n```\n\n"
        f"## SUPPORTING FACTS (recorded since last refresh — integrate what the document does not already say)\n{fitted.facts}"
        f"{document_hint}{budget_hint}{truncation_note}\n\n"
        f"{task_footer}