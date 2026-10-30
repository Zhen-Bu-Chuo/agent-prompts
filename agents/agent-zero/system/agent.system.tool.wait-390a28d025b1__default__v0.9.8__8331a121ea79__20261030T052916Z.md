---
agent: agent-zero
prompt_id: agent.system.tool.wait-390a28d025b1
module: system
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.tool.wait.md
source_symbol: document
source_lines:
- 1
- 34
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.tool.wait.md#L1-L34
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: 44cd336adb659656b2e7e2ac9c81ba1c42dd57e125fd4a4b563b7020a000e8cc
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
### wait
pause execution for a set time or until a timestamp
use args "seconds" "minutes" "hours" "days" for duration
use "until" with ISO timestamp for a specific time
usage:

1 wait duration
~~~json
{
    "thoughts": [
        "I need to wait..."
    ],
    "headline": "...",
    "tool_name": "wait",
    "tool_args": { 
        "minutes": 1, 
        "seconds": 30 
    }
}
~~~

2 wait timestamp
~~~json
{
    "thoughts": [
        "I will wait until..."
    ],
    "headline": "...",
    "tool_name": "wait",
    "tool_args": { 
        "until": "2025-10-20T10:00:00Z" 
    }
}
~~~
