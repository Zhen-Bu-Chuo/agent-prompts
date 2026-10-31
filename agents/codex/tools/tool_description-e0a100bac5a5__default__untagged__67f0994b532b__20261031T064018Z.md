---
agent: codex
prompt_id: tool_description-e0a100bac5a5
module: tools
variant: default
upstream_repository: openai/codex
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 67f0994b532b8740f14b5b738af7b7b2a915b1d6
source_path: codex-rs/core/templates/search_tool/tool_description.md
source_symbol: document
source_lines:
- 1
- 7
source_permalink: https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/codex-rs/core/templates/search_tool/tool_description.md#L1-L7
source_committed_at: '2026-10-31T00:12:17Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:18Z'
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
