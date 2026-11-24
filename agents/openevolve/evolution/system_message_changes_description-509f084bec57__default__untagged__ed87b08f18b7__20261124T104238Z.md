---
agent: openevolve
prompt_id: system_message_changes_description-509f084bec57
module: evolution
variant: default
upstream_repository: algorithmicsuperintelligence/openevolve
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: ed87b08f18b70a19762f75c372a750f0fa00bc9f
source_path: openevolve/prompts/defaults/system_message_changes_description.txt
source_symbol: document
source_lines:
- 1
- 2
source_permalink: https://github.com/algorithmicsuperintelligence/openevolve/blob/ed87b08f18b70a19762f75c372a750f0fa00bc9f/openevolve/prompts/defaults/system_message_changes_description.txt#L1-L2
source_committed_at: '2026-11-24T10:33:08Z'
release_published_at: null
fetched_at: '2026-11-24T10:42:38Z'
extractor_version: 1.0.3
content_sha256: a1d66563b1f5c5c80f0d737959e9474a21a7fdf54cadab4bbd39df03da95d8bd
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
Important: Describe your changes and any new methods in the "Changes Description" field, replacing the previous description first (as usual, using SEARCH & REPLACE blocks). If you skip this step, all proposed changes will be discarded because our evolution algorithm depends on it.
It is recommended to write the description in plain language as a short numbered list (avoid long paragraphs and complex symbols), since a different LLM model (or you later) will need to update this text in future calls.