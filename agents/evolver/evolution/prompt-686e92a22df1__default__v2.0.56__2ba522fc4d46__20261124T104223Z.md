---
agent: evolver
prompt_id: prompt-686e92a22df1
module: evolution
variant: default
upstream_repository: EvoMap/evolver
upstream_version: v2.0.56
package_name: null
package_version: null
source_ref: v2.0.56
source_commit: 2ba522fc4d46b63cf2ebf4661376002ea084cfdf
source_path: packages/evolver-core/dist/exec/prompt.js
source_symbol: head.8
source_lines:
- 32
- 32
source_permalink: https://github.com/EvoMap/evolver/blob/2ba522fc4d46b63cf2ebf4661376002ea084cfdf/packages/evolver-core/dist/exec/prompt.js#L32-L32
source_committed_at: '2026-11-24T02:41:18Z'
release_published_at: '2026-11-24T02:42:35Z'
fetched_at: '2026-11-24T10:42:23Z'
extractor_version: 1.0.3
content_sha256: 205638d69e442b43667b32e6f3e8782da074f21c1c6e920e0c27ccf96a3ad938
license: GPL-3.0-or-later
source_kind: dynamic_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---
- ${sanitize(warning.summary, 240)}