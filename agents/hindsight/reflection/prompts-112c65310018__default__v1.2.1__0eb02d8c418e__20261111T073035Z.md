---
agent: hindsight
prompt_id: prompts-112c65310018
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.2.1
package_name: null
package_version: null
source_ref: v1.2.1
source_commit: 0eb02d8c418eac6b489bc63883c993b2257dfac4
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_structured_delta_prompt.1
source_lines:
- 1642
- 1647
source_permalink: https://github.com/vectorize-io/hindsight/blob/0eb02d8c418eac6b489bc63883c993b2257dfac4/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1642-L1647
source_committed_at: '2026-11-10T14:02:17Z'
release_published_at: '2026-11-10T14:34:26Z'
fetched_at: '2026-11-11T07:30:35Z'
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