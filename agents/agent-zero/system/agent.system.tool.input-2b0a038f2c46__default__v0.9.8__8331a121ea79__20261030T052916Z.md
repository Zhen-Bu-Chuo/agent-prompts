---
agent: agent-zero
prompt_id: agent.system.tool.input-2b0a038f2c46
module: system
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.tool.input.md
source_symbol: document
source_lines:
- 1
- 19
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.tool.input.md#L1-L19
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: 6ed84ad8a01177d24b4cdcaee7d5033a1c4598ee0c159af642de1f0dfa28ed8d
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
### input:
use keyboard arg for terminal program input
use session arg for terminal session number
answer dialogues enter passwords etc
not for browser
usage:
~~~json
{
    "thoughts": [
        "The program asks for Y/N...",
    ],
    "headline": "Responding to terminal program prompt",
    "tool_name": "input",
    "tool_args": {
        "keyboard": "Y",
        "session": 0
    }
}
~~~
