---
agent: evolver
prompt_id: prompt-3ffcfbaa97ee
module: evolution
variant: default
upstream_repository: EvoMap/evolver
upstream_version: v2.0.51
package_name: null
package_version: null
source_ref: v2.0.51
source_commit: 3c6a933ba9b97309d35c4d1dcb88e30856dcee53
source_path: packages/evolver-core/dist/exec/prompt.js
source_symbol: steps.25
source_lines:
- 72
- 72
source_permalink: https://github.com/EvoMap/evolver/blob/3c6a933ba9b97309d35c4d1dcb88e30856dcee53/packages/evolver-core/dist/exec/prompt.js#L72-L72
source_committed_at: '2026-11-12T06:38:46Z'
release_published_at: '2026-11-12T06:40:08Z'
fetched_at: '2026-11-12T07:58:25Z'
extractor_version: 1.0.3
content_sha256: f5fbb24250c3deac65c0eb62a99c70ab9de1646bd7fb87c94eb130970b617306
license: GPL-3.0-or-later
source_kind: dynamic_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---
Preconditions: ${s(gene.preconditions.join('; '))}