---
agent: agent-zero
prompt_id: agent.system.secrets-c46287903e66
module: system
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.secrets.md
source_symbol: document
source_lines:
- 1
- 20
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.secrets.md#L1-L20
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: 807f6092caab51af7823057a157b43127082ef81007b38f29361507282d08fe7
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
# Secret Placeholders
- user secrets are masked and used as aliases
- use aliases in tool calls they will be automatically replaced with actual values

You have access to the following secrets:
<secrets>
{{secrets}}
</secrets>

## Important Guidelines:
- use exact alias format `§§secret(key_name)`
- values may contain special characters needing escaping in code, sanitize in your code if errors occur
- comments help understand purpose

# Additional variables
- use these non-sensitive variables as they are when needed
- use plain text values without placeholder format
<variables>
{{vars}}
</variables>
