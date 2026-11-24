---
agent: hindsight
prompt_id: prompts-aad6564bca91
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: fa2b4a8c444cb73630859bdbba8b4e6c26bd80c1
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_structured_delta_prompt.document_hint.2
source_lines:
- 1611
- 1614
source_permalink: https://github.com/vectorize-io/hindsight/blob/fa2b4a8c444cb73630859bdbba8b4e6c26bd80c1/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1611-L1614
source_committed_at: '2026-11-24T10:34:27Z'
release_published_at: null
fetched_at: '2026-11-24T10:42:28Z'
extractor_version: 1.0.3
content_sha256: 9b673b631ec56a420d696467efb74dd5bef6e2a393cd0c147a92d93628461435
license: MIT
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---
\n\n## Document budget\n"
                f"The document is ~{document_tokens} tokens against a budget of {document_budget}. "
                "It is close to the limit, so prefer replacing stale blocks over appending new ones "
                "where the new facts update something the document already covers.