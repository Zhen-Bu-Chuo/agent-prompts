---
agent: roo-code
prompt_id: responses-19df54b29767
module: tools
variant: default
upstream_repository: RooCodeInc/Roo-Code
upstream_version: v3.54.0
package_name: null
package_version: null
source_ref: v3.54.0
source_commit: 27001b2b5aa47b65e8a6ba1914e0f4216be0ebb0
source_path: src/core/prompts/responses.ts
source_symbol: toolUseInstructionsReminderNative.52
source_lines:
- 219
- 223
source_permalink: https://github.com/RooCodeInc/Roo-Code/blob/27001b2b5aa47b65e8a6ba1914e0f4216be0ebb0/src/core/prompts/responses.ts#L219-L223
source_committed_at: '2026-05-15T17:43:39Z'
release_published_at: '2026-05-15T17:52:24Z'
fetched_at: '2026-10-30T05:30:13Z'
extractor_version: 1.0.3
content_sha256: 0ed9ba97690c41ad00e471105c1453a7f9a412bb12f8d2bcc2fa220480dd0c1a
license: Apache-2.0
source_kind: static_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---
# Reminder: Instructions for Tool Use

Tools are invoked using the platform's native tool calling mechanism. Each tool requires specific parameters as defined in the tool descriptions. Refer to the tool definitions provided in your system instructions for the correct parameter structure and usage examples.

Always ensure you provide all required parameters for the tool you wish to use.