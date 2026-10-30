---
agent: cognee
prompt_id: detect_pii-70c26911de9f
module: memory
variant: default
upstream_repository: topoteretes/cognee
upstream_version: v1.6.6
package_name: null
package_version: null
source_ref: v1.6.6
source_commit: df2b4facd7c1d73b59376fd251fb93674a9d60a3
source_path: cognee/infrastructure/llm/prompts/detect_pii.txt
source_symbol: document
source_lines:
- 1
- 12
source_permalink: https://github.com/topoteretes/cognee/blob/df2b4facd7c1d73b59376fd251fb93674a9d60a3/cognee/infrastructure/llm/prompts/detect_pii.txt#L1-L12
source_committed_at: '2026-10-29T21:29:40Z'
release_published_at: '2026-10-29T21:33:43Z'
fetched_at: '2026-10-30T05:29:25Z'
extractor_version: 1.0.3
content_sha256: 70ea0227598a6b1447ca540ae5ce674664cfd1fb2dc71a1fdb048af81ab18052
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
You are a privacy reviewer. You will be given a text sample from the file named "{{ file_name }}".

Decide whether the text contains personal data about identifiable people — for example: identity or government documents, financial records (statements, payslips, tax filings), medical information, home addresses, dates of birth, credentials, or private correspondence.

Rules:
- Judge only what is present in the sample; do not speculate about the rest of the file.
- Company or public information (published articles, documentation, marketing text) is NOT personal data.
- Categories must be short snake_case labels, e.g. "medical_document", "financial_document", "identity_document", "private_correspondence", "home_address", "credential".
- Severity: "high" for identity/government/financial/medical data and credentials, "medium" for private correspondence and resumes, "low" for incidental contact details.
- NEVER quote or repeat the personal data itself in your rationale — describe it generically ("contains a date of birth"), do not restate it.

Return your structured assessment.
