---
agent: codex
prompt_id: tool_description-e0a100bac5a5
module: tools
variant: default
upstream_repository: openai/codex
upstream_version: rust-v0.167.2
package_name: null
package_version: null
source_ref: rust-v0.167.2
source_commit: ce21072c90d32c40af7a55b60b2fb35c84a43a6a
source_path: codex-rs/core/templates/search_tool/tool_description.md
source_symbol: document
source_lines:
- 1
- 7
source_permalink: https://github.com/openai/codex/blob/ce21072c90d32c40af7a55b60b2fb35c84a43a6a/codex-rs/core/templates/search_tool/tool_description.md#L1-L7
source_committed_at: '2026-11-11T20:03:56Z'
release_published_at: '2026-11-11T22:44:46Z'
fetched_at: '2026-11-12T07:58:20Z'
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
