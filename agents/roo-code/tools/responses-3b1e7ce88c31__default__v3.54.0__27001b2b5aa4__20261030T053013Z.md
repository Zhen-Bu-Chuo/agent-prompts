---
agent: roo-code
prompt_id: responses-3b1e7ce88c31
module: tools
variant: default
upstream_repository: RooCodeInc/Roo-Code
upstream_version: v3.54.0
package_name: null
package_version: null
source_ref: v3.54.0
source_commit: 27001b2b5aa47b65e8a6ba1914e0f4216be0ebb0
source_path: src/core/prompts/responses.ts
source_symbol: instructions.16
source_lines:
- 45
- 54
source_permalink: https://github.com/RooCodeInc/Roo-Code/blob/27001b2b5aa47b65e8a6ba1914e0f4216be0ebb0/src/core/prompts/responses.ts#L45-L54
source_committed_at: '2026-05-15T17:43:39Z'
release_published_at: '2026-05-15T17:52:24Z'
fetched_at: '2026-10-30T05:30:13Z'
extractor_version: 1.0.3
content_sha256: 1edb48993f3cb8b11dd7ca134eba44e877e3c9ff9c5f85c6b2275853e115cf9d
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---
[ERROR] You did not use a tool in your previous response! Please retry with a tool use.

${instructions}

# Next Steps

If you have completed the user's task, use the attempt_completion tool.
If you require additional information from the user, use the ask_followup_question tool.
Otherwise, if you have not completed the task and do not need additional information, then proceed with the next step of the task.
(This is an automated message, so do not respond to it conversationally.)