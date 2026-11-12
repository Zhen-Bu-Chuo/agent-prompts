---
agent: evolver
prompt_id: prompt-90c6d0c2efc5
module: evolution
variant: default
upstream_repository: EvoMap/evolver
upstream_version: v2.0.51
package_name: null
package_version: null
source_ref: v2.0.51
source_commit: 3c6a933ba9b97309d35c4d1dcb88e30856dcee53
source_path: packages/evolver-core/dist/exec/prompt.js
source_symbol: lines.10
source_lines:
- 35
- 35
source_permalink: https://github.com/EvoMap/evolver/blob/3c6a933ba9b97309d35c4d1dcb88e30856dcee53/packages/evolver-core/dist/exec/prompt.js#L35-L35
source_committed_at: '2026-11-12T06:38:46Z'
release_published_at: '2026-11-12T06:40:08Z'
fetched_at: '2026-11-12T07:58:25Z'
extractor_version: 1.0.3
content_sha256: 5b0411a8c12993e2fcf8cb4ce7ab5e1f6796ef36af10430ed2402df1a3d23ff4
license: GPL-3.0-or-later
source_kind: dynamic_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---
   Trigger: ${sanitize(warning.trigger.join(', '), 240)}