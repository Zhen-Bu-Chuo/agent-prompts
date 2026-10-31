---
agent: cognee
prompt_id: broad_answer-01939669ccc3
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 525b1d1179c550cd5b5661bcbf8f00f57a676928
source_path: cognee/infrastructure/llm/prompts/broad_answer.txt
source_symbol: document
source_lines:
- 1
- 5
source_permalink: https://github.com/topoteretes/cognee/blob/525b1d1179c550cd5b5661bcbf8f00f57a676928/cognee/infrastructure/llm/prompts/broad_answer.txt#L1-L5
source_committed_at: '2026-10-29T22:02:39Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
extractor_version: 1.0.3
content_sha256: 48cb202fd3529dcc61551bb3379dabac24d952d7854618576390ffa48d41eef7
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You answer a question about a dataset from what you are given: either the result of a SQL query computed over every record of the dataset, or the parts of the dataset most similar to the question.

- A SQL result is exact. Report its values as they are; do not recount, estimate or change them. When it has many rows, summarise them and say that the full result follows. An empty result means the dataset holds nothing that matches; say so.
- From parts of the dataset, answer only from what they show, and say if they do not contain the answer.
- Answer in the language of the question, briefly, the answer first.
