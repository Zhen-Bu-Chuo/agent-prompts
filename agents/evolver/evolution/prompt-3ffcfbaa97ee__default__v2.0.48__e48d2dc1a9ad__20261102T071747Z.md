---
agent: evolver
prompt_id: prompt-3ffcfbaa97ee
module: evolution
variant: default
upstream_repository: EvoMap/evolver
upstream_version: v2.0.48
package_name: null
package_version: null
source_ref: v2.0.48
source_commit: e48d2dc1a9ad11210ede367f4fbadcbf0b539f18
source_path: packages/evolver-core/dist/exec/prompt.js
source_symbol: steps.25
source_lines:
- 72
- 72
source_permalink: https://github.com/EvoMap/evolver/blob/e48d2dc1a9ad11210ede367f4fbadcbf0b539f18/packages/evolver-core/dist/exec/prompt.js#L72-L72
source_committed_at: '2026-11-01T08:57:13Z'
release_published_at: '2026-11-01T09:58:31Z'
fetched_at: '2026-11-02T07:17:47Z'
extractor_version: 1.0.3
content_sha256: f5fbb24250c3deac65c0eb62a99c70ab9de1646bd7fb87c94eb130970b617306
license: GPL-3.0-or-later
source_kind: dynamic_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---
Preconditions: ${s(gene.preconditions.join('; '))}