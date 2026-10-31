---
agent: cognee
prompt_id: feedback_detection_rating_section-4fb227bad834
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 525b1d1179c550cd5b5661bcbf8f00f57a676928
source_path: cognee/infrastructure/llm/prompts/feedback_detection_rating_section.txt
source_symbol: document
source_lines:
- 1
- 16
source_permalink: https://github.com/topoteretes/cognee/blob/525b1d1179c550cd5b5661bcbf8f00f57a676928/cognee/infrastructure/llm/prompts/feedback_detection_rating_section.txt#L1-L16
source_committed_at: '2026-10-29T22:02:39Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
extractor_version: 1.0.3
content_sha256: 6c32889b1e128f47ce0820cd75714a582daa3da5b178aea76a3ec25b2d7f106e
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
## 4. Previous answer rating

A fourth independent signal, in addition to the ones above.

Rate the previous answer 1-5 only when this message gives clear evidence
about its quality. Otherwise return null.

5 - the user confirms it solved their problem, or acts on it directly.
4 - the user accepts it and builds on it, with a minor correction or caveat.
3 - the user's reaction is genuinely mixed: the answer clearly helped in
    part and clearly fell short in part.
2 - the user repeats the question, redirects, or corrects a substantive part.
1 - the user says it was wrong, unusable, or ignored what they asked for.

A new question on the same topic is not evidence. Politeness is not evidence.
Most turns should return null.
