---
agent: cognee
prompt_id: extract_presort_relation-350abf181eba
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.6
package_name: null
package_version: null
source_ref: v1.6.6
source_commit: df2b4facd7c1d73b59376fd251fb93674a9d60a3
source_path: cognee/infrastructure/llm/prompts/extract_presort_relation.txt
source_symbol: document
source_lines:
- 1
- 14
source_permalink: https://github.com/topoteretes/cognee/blob/df2b4facd7c1d73b59376fd251fb93674a9d60a3/cognee/infrastructure/llm/prompts/extract_presort_relation.txt#L1-L14
source_committed_at: '2026-10-29T21:29:40Z'
release_published_at: '2026-10-29T21:33:43Z'
fetched_at: '2026-10-30T05:29:25Z'
extractor_version: 1.0.3
content_sha256: 36c503a3755c36984a725402c631696f37353ea8201a35245ed821b50591ba8d
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are analyzing one file from a folder scan to compute instances of the relationship "{{ relation_name }}".
{% if relation_description %}Relationship meaning: {{ relation_description }}{% endif %}

The relationship points from the file to entities of type "{{ target_entity }}".
{% if target_description %}Target entity meaning: {{ target_description }}{% endif %}

You will be given the file's name and a text sample of its content. Identify every "{{ target_entity }}" this file has the "{{ relation_name }}" relationship with, based only on what the sample shows.

Rules:
- Return one instance per distinct target, with a short human-readable target_name.
- Set confidence in [0, 1]; use low confidence when the evidence is indirect.
- Do not invent targets that are not supported by the sample.
- The rationale must be one short sentence and must NOT quote personal data verbatim.
- If the file has no such relationship, return an empty list.
