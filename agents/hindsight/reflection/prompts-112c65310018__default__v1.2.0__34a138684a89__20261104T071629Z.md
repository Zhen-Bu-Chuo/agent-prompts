---
agent: hindsight
prompt_id: prompts-112c65310018
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.2.0
package_name: null
package_version: null
source_ref: v1.2.0
source_commit: 34a138684a899b6ec34175f7a2b633860466d289
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_structured_delta_prompt.1
source_lines:
- 1641
- 1646
source_permalink: https://github.com/vectorize-io/hindsight/blob/34a138684a899b6ec34175f7a2b633860466d289/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1641-L1646
source_committed_at: '2026-11-03T11:05:49Z'
release_published_at: '2026-11-03T11:38:19Z'
fetched_at: '2026-11-04T07:16:29Z'
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