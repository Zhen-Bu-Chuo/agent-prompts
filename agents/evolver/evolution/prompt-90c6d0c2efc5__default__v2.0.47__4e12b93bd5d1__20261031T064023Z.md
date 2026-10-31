---
agent: evolver
prompt_id: prompt-90c6d0c2efc5
module: evolution
variant: default
upstream_repository: EvoMap/evolver
upstream_version: v2.0.47
package_name: null
package_version: null
source_ref: v2.0.47
source_commit: 4e12b93bd5d1173ee0c3bd2ae72de8030f82db7a
source_path: packages/evolver-core/dist/exec/prompt.js
source_symbol: lines.10
source_lines:
- 35
- 35
source_permalink: https://github.com/EvoMap/evolver/blob/4e12b93bd5d1173ee0c3bd2ae72de8030f82db7a/packages/evolver-core/dist/exec/prompt.js#L35-L35
source_committed_at: '2026-10-30T12:01:35Z'
release_published_at: '2026-10-30T12:03:00Z'
fetched_at: '2026-10-31T06:40:23Z'
extractor_version: 1.0.3
content_sha256: 5b0411a8c12993e2fcf8cb4ce7ab5e1f6796ef36af10430ed2402df1a3d23ff4
license: GPL-3.0-or-later
source_kind: dynamic_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---
   Trigger: ${sanitize(warning.trigger.join(', '), 240)}