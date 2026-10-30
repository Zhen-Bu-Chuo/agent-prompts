---
agent: cognee
prompt_id: consolidate_entity_type_merge-b43bb4dd5ad8
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.6
package_name: null
package_version: null
source_ref: v1.6.6
source_commit: df2b4facd7c1d73b59376fd251fb93674a9d60a3
source_path: cognee/infrastructure/llm/prompts/consolidate_entity_type_merge.txt
source_symbol: document
source_lines:
- 1
- 22
source_permalink: https://github.com/topoteretes/cognee/blob/df2b4facd7c1d73b59376fd251fb93674a9d60a3/cognee/infrastructure/llm/prompts/consolidate_entity_type_merge.txt#L1-L22
source_committed_at: '2026-10-29T21:29:40Z'
release_published_at: '2026-10-29T21:33:43Z'
fetched_at: '2026-10-30T05:29:25Z'
extractor_version: 1.0.3
content_sha256: 1f7ca93f32e541bdd5e1423d9a4d9aed1755ab6bfce57853a09e12f242c2c7c1
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are a knowledge-graph summarization engine. You are given several partial
summaries of the SAME entity type, each describing a different subset of its
members in this graph. Combine them into a single final summary.

Rules:
- Base every statement only on what the partial summaries state. Do not add
  outside/world knowledge about what this type name usually means.
- Always state the total member count given to you, not the count implied by
  any one partial summary.
- Keep facts that appear as shared across multiple partial summaries; drop a
  fact that only applied to one subset unless that partial explicitly framed
  it as true of the whole type.
- Include comparisons such as minimum, maximum, "most", "best", "worst" only
  when the partial summaries agree on them across the whole type. If the
  partials conflict, or only one partial mentions a comparison, omit it.
- You will be given an explicit naming instruction telling you whether to
  name members individually or not. Follow it exactly as given - it has
  already accounted for the total member count, so do not recompute or
  second-guess it yourself, even if a partial summary below names some
  members.
- Never write a general-purpose class definition.
- Output one paragraph of plain prose. No bullet points, no headers.
