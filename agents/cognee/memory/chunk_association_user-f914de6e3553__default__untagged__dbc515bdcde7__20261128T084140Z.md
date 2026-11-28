---
agent: cognee
prompt_id: chunk_association_user-f914de6e3553
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: dbc515bdcde72691c1880978407ac1e5829bbc25
source_path: cognee/infrastructure/llm/prompts/chunk_association_user.txt
source_symbol: document
source_lines:
- 1
- 13
source_permalink: https://github.com/topoteretes/cognee/blob/dbc515bdcde72691c1880978407ac1e5829bbc25/cognee/infrastructure/llm/prompts/chunk_association_user.txt#L1-L13
source_committed_at: '2026-11-27T15:10:07Z'
release_published_at: null
fetched_at: '2026-11-28T08:41:40Z'
extractor_version: 1.0.3
content_sha256: e2a62d53cd70d4242712316eb0582ef833c94630c1d08b83bedbfeb32d8dd3a8
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Compare these two text chunks and determine their semantic similarity:

**Chunk 1:**
```
{{ chunk_1 }}
```

**Chunk 2:**
```
{{ chunk_2 }}
```

Analyze their relationship and provide your assessment.
