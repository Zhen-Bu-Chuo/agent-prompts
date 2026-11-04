---
agent: hindsight
prompt_id: prompts-aad6564bca91
module: reflection
variant: default
upstream_repository: vectorize-io/hindsight
upstream_version: v1.2.0
package_name: null
package_version: null
source_ref: v1.2.0
source_commit: 34a138684a899b6ec34175f7a2b633860466d289
source_path: hindsight-api-slim/hindsight_api/engine/reflect/prompts.py
source_symbol: module.build_structured_delta_prompt.document_hint.2
source_lines:
- 1590
- 1593
source_permalink: https://github.com/vectorize-io/hindsight/blob/34a138684a899b6ec34175f7a2b633860466d289/hindsight-api-slim/hindsight_api/engine/reflect/prompts.py#L1590-L1593
source_committed_at: '2026-11-03T11:05:49Z'
release_published_at: '2026-11-03T11:38:19Z'
fetched_at: '2026-11-04T07:16:29Z'
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