---
agent: gemini-cli
prompt_id: snippets-bb2803cf0ec8
module: context
variant: default
upstream_repository: google-gemini/gemini-cli
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 0ac57c029b848d109eef940afe0db4b5a0c3dad0
source_path: packages/core/src/prompts/snippets.ts
source_symbol: globalMemoryBullet.113
source_lines:
- 864
- 865
source_permalink: https://github.com/google-gemini/gemini-cli/blob/0ac57c029b848d109eef940afe0db4b5a0c3dad0/packages/core/src/prompts/snippets.ts#L864-L865
source_committed_at: '2026-11-02T19:18:51Z'
release_published_at: null
fetched_at: '2026-11-03T07:37:34Z'
extractor_version: 1.0.3
content_sha256: 4999b518625acd9831231173a8aecfdef1ca5db29ba068e366812bddebad9683
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---

  - **Global Personal Memory** (\`${options.globalMemoryPath}\`): Cross-project personal preferences and facts about the user that should follow them into every workspace (e.g. preferred testing framework across all projects, language preferences, coding-style defaults). Loaded automatically in every session. Keep entries concise and durable — never workspace-specific.