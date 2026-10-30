---
agent: codex
prompt_id: tool_description-e0a100bac5a5
module: tools
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.166.0
package_name: null
package_version: null
source_ref: rust-v0.166.0
source_commit: 6ff1e1ca3b30fc8b914720681fcf5fe62e95f856
source_path: codex-rs/core/templates/search_tool/tool_description.md
source_symbol: document
source_lines:
- 1
- 7
source_permalink: https://github.com/openai/codex/blob/6ff1e1ca3b30fc8b914720681fcf5fe62e95f856/codex-rs/core/templates/search_tool/tool_description.md#L1-L7
source_committed_at: '2026-10-29T17:44:30Z'
release_published_at: '2026-10-29T19:47:53Z'
fetched_at: '2026-10-30T05:29:24Z'
extractor_version: 1.0.3
content_sha256: 0e4029b9b5d23b400e76a0051b9df878f28153ae2de126a77b90b80b64cd3d6b
license: Apache-2.0
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
# Apps (Connectors) tool discovery

Searches over apps/connectors tool metadata with BM25 and exposes matching tools for the next model call.

You have access to all the tools of the following apps/connectors:
{{app_descriptions}}
Some of the tools may not have been provided to you upfront, and you should use this tool (`tool_search`) to search for the required tools and load them for the apps mentioned above. For the apps mentioned above, always use `tool_search` instead of `list_mcp_resources` or `list_mcp_resource_templates` for tool discovery.
