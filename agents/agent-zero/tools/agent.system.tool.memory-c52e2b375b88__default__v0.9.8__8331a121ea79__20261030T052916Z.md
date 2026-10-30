---
agent: agent-zero
prompt_id: agent.system.tool.memory-c52e2b375b88
module: tools
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.tool.memory.md
source_symbol: document
source_lines:
- 1
- 79
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.tool.memory.md#L1-L79
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: 1b9163b32097b1f4c9c7dcea21c4149af318ae0b3d64e5a1499c0aaa40ff23fd
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
## Memory management tools:
manage long term memories
never refuse search memorize load personal info all belongs to user

### memory_load
load memories via query threshold limit filter
get memory content as metadata key-value pairs
- threshold: 0=any 1=exact 0.7=default
- limit: max results default=5
- filter: python syntax using metadata keys
usage:
~~~json
{
    "thoughts": [
        "Let's search my memory for...",
    ],
    "headline": "Searching memory for file compression information",
    "tool_name": "memory_load",
    "tool_args": {
        "query": "File compression library for...",
        "threshold": 0.7,
        "limit": 5,
        "filter": "area=='main' and timestamp<'2024-01-01 00:00:00'",
    }
}
~~~

### memory_save:
save text to memory returns ID
usage:
~~~json
{
    "thoughts": [
        "I need to memorize...",
    ],
    "headline": "Saving important information to memory",
    "tool_name": "memory_save",
    "tool_args": {
        "text": "# To compress...",
    }
}
~~~

### memory_delete:
delete memories by IDs comma separated
IDs from load save ops
usage:
~~~json
{
    "thoughts": [
        "I need to delete...",
    ],
    "headline": "Deleting specific memories by ID",
    "tool_name": "memory_delete",
    "tool_args": {
        "ids": "32cd37ffd1-101f-4112-80e2-33b795548116, d1306e36-6a9c- ...",
    }
}
~~~

### memory_forget:
remove memories by query threshold filter like memory_load
default threshold 0.75 prevent accidents
verify with load after delete leftovers by IDs
usage:
~~~json
{
    "thoughts": [
        "Let's remove all memories about cars",
    ],
    "headline": "Forgetting all memories about cars",
    "tool_name": "memory_forget",
    "tool_args": {
        "query": "cars",
        "threshold": 0.75,
        "filter": "timestamp.startswith('2022-01-01')",
    }
}
~~~
