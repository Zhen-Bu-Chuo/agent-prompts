---
agent: graphiti
prompt_id: eval-0e250a941641
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: v0.31.2
package_name: null
package_version: null
source_ref: v0.31.2
source_commit: d72407dcedac911e1be9fc15b55e8c05a3efcc36
source_path: graphiti_core/prompts/eval.py
source_symbol: module.query_expansion.user_prompt.1
source_lines:
- 68
- 74
source_permalink: https://github.com/getzep/graphiti/blob/d72407dcedac911e1be9fc15b55e8c05a3efcc36/graphiti_core/prompts/eval.py#L68-L74
source_committed_at: '2026-10-20T17:23:18Z'
release_published_at: '2026-10-20T17:25:21Z'
fetched_at: '2026-10-30T05:29:43Z'
extractor_version: 1.0.3
content_sha256: 38dd8d06bd4de9eee3a1da5c39a8716f33dd676022ba1490012fa044511f0f4a
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---

    Bob is asking Alice a question, are you able to rephrase the question into a simpler one about Alice in the third person
    that maintains the relevant context?
    <QUESTION>
    {to_prompt_json(context['query'])}
    </QUESTION>
    