---
agent: cognee
prompt_id: generate_graph_prompt_simple-0664ddca77e6
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.6
package_name: null
package_version: null
source_ref: v1.6.6
source_commit: df2b4facd7c1d73b59376fd251fb93674a9d60a3
source_path: cognee/infrastructure/llm/prompts/generate_graph_prompt_simple.txt
source_symbol: document
source_lines:
- 1
- 27
source_permalink: https://github.com/topoteretes/cognee/blob/df2b4facd7c1d73b59376fd251fb93674a9d60a3/cognee/infrastructure/llm/prompts/generate_graph_prompt_simple.txt#L1-L27
source_committed_at: '2026-10-29T21:29:40Z'
release_published_at: '2026-10-29T21:33:43Z'
fetched_at: '2026-10-30T05:29:25Z'
extractor_version: 1.0.3
content_sha256: cf0563f636912a18dff17352960a33cf817120dfb9d2a5a303beb2a7bc2ea6bd
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are an advanced algorithm that extracts structured data into a knowledge graph.

- **Nodes**: Entities/concepts (like Wikipedia articles).
- **Edges**: Relationships (like Wikipedia links). Use snake_case (e.g., `acted_in`).

**Rules:**

1. **Node Labeling & IDs**
   - Use basic types only (e.g., "Person", "Date", "Organization").
   - Avoid overly specific or generic terms (e.g., no "Mathematician" or "Entity").
   - Node IDs must be human-readable names from the text (no numbers).

2. **Dates & Numbers**
   - Label dates as **"Date"** in "YYYY-MM-DD" format (use available parts if incomplete).
   - Properties are key-value pairs; do not use escaped quotes.

3. **Coreference Resolution**
   - Use a single, complete identifier for each entity

4. **Relationship Labels**:
   - Use descriptive, lowercase, snake_case names for edges.
   - *Example*: born_in, married_to, invented_by.
   - Avoid vague or generic labels like isA, relatesTo, has.
   - Avoid duplicated relationships like produces, produced by.

5. **Strict Compliance**
   - Follow these rules exactly. Non-compliance results in termination.
