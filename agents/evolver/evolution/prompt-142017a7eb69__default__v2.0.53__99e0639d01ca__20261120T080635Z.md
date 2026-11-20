---
agent: evolver
prompt_id: prompt-142017a7eb69
module: evolution
variant: default
upstream_repository: EvoMap/evolver
upstream_version: v2.0.53
package_name: null
package_version: null
source_ref: v2.0.53
source_commit: 99e0639d01ca7b264e54803f72fb02324837cc5a
source_path: packages/evolver-core/dist/exec/prompt.js
source_symbol: evidence.33
source_lines:
- 85
- 85
source_permalink: https://github.com/EvoMap/evolver/blob/99e0639d01ca7b264e54803f72fb02324837cc5a/packages/evolver-core/dist/exec/prompt.js#L85-L85
source_committed_at: '2026-11-19T16:28:50Z'
release_published_at: '2026-11-19T16:30:05Z'
fetched_at: '2026-11-20T08:06:35Z'
extractor_version: 1.0.3
content_sha256: d6a3f2061338e30235344d60c045babee529cf6f010f5ff10c0ab852b5330c21
license: GPL-3.0-or-later
source_kind: dynamic_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---
- gene=${s(evidence.geneId, 240)} successes=${evidence.successCount} failures=${evidence.failCount} expected_success=${evidence.expectedSuccess.toFixed(2)} similarity=${evidence.similarity.toFixed(2)}