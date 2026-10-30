---
agent: cline
prompt_id: prompts-d6095c2a1be7
module: tools
variant: default
upstream_repository: cline/cline
upstream_version: v4.1.26
package_name: null
package_version: null
source_ref: v4.1.26
source_commit: a459f1d04dea030833b558be645011ab739c463b
source_path: apps/cli/src/connectors/adapters/prompts.ts
source_symbol: CONNECTOR_SYSTEM_RULES.2
source_lines:
- 16
- 16
source_permalink: https://github.com/cline/cline/blob/a459f1d04dea030833b558be645011ab739c463b/apps/cli/src/connectors/adapters/prompts.ts#L16-L16
source_committed_at: '2026-10-26T04:37:15Z'
release_published_at: '2026-10-26T09:06:50Z'
fetched_at: '2026-10-30T05:29:22Z'
extractor_version: 1.0.3
content_sha256: 64adf655c87f650735962b1d4e32ed25c46f261d701adf43a2f88f8f50a588b1
license: Apache-2.0
source_kind: source_string_fragment
extraction_notes: Raw JavaScript quoted string body; source escapes and separate concatenation/array fragments are preserved without evaluation.
---
Keep answers compact and optimized for this {{CONNECTOR_ID}} integration unless the user asks for detail.