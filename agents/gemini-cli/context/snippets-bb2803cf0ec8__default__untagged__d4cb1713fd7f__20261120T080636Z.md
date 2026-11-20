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
source_commit: d4cb1713fd7fc30f1c03f9ca7cbfed341c97dffd
source_path: packages/core/src/prompts/snippets.ts
source_symbol: globalMemoryBullet.113
source_lines:
- 864
- 865
source_permalink: https://github.com/google-gemini/gemini-cli/blob/d4cb1713fd7fc30f1c03f9ca7cbfed341c97dffd/packages/core/src/prompts/snippets.ts#L864-L865
source_committed_at: '2026-11-19T21:45:31Z'
release_published_at: null
fetched_at: '2026-11-20T08:06:36Z'
extractor_version: 1.0.3
content_sha256: 4999b518625acd9831231173a8aecfdef1ca5db29ba068e366812bddebad9683
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---

  - **Global Personal Memory** (\`${options.globalMemoryPath}\`): Cross-project personal preferences and facts about the user that should follow them into every workspace (e.g. preferred testing framework across all projects, language preferences, coding-style defaults). Loaded automatically in every session. Keep entries concise and durable — never workspace-specific.