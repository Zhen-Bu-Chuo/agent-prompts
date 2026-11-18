---
agent: cline
prompt_id: prompts-d6095c2a1be7
module: tools
variant: default
upstream_repository: cline/cline
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: eff43e19b267e171f597ab03733bfed25090f72d
source_path: apps/cli/src/connectors/adapters/prompts.ts
source_symbol: CONNECTOR_SYSTEM_RULES.2
source_lines:
- 16
- 16
source_permalink: https://github.com/cline/cline/blob/eff43e19b267e171f597ab03733bfed25090f72d/apps/cli/src/connectors/adapters/prompts.ts#L16-L16
source_committed_at: '2026-11-17T13:18:29Z'
release_published_at: null
fetched_at: '2026-11-18T08:14:22Z'
extractor_version: 1.0.3
content_sha256: 64adf655c87f650735962b1d4e32ed25c46f261d701adf43a2f88f8f50a588b1
license: Apache-2.0
source_kind: source_string_fragment
extraction_notes: Raw JavaScript quoted string body; source escapes and separate concatenation/array fragments are preserved without evaluation.
---
Keep answers compact and optimized for this {{CONNECTOR_ID}} integration unless the user asks for detail.