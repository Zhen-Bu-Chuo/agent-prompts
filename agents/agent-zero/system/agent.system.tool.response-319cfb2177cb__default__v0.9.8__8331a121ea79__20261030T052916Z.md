---
agent: agent-zero
prompt_id: agent.system.tool.response-319cfb2177cb
module: system
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.tool.response.md
source_symbol: document
source_lines:
- 1
- 19
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.tool.response.md#L1-L19
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: cba534c378e2215528a068d5969a11caadf8b5b97b3cf1f62bb6f9c566a91c7e
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
### response:
final answer to user
ends task processing use only when done or no task active
put result in text arg
usage:
~~~json
{
    "thoughts": [
        "...",
    ],
    "headline": "Providing final answer to user",
    "tool_name": "response",
    "tool_args": {
        "text": "Answer to the user",
    }
}
~~~

{{ include "agent.system.response_tool_tips.md" }}