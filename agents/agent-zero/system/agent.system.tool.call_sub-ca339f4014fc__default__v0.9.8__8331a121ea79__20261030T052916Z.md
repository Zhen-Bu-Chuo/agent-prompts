---
agent: agent-zero
prompt_id: agent.system.tool.call_sub-ca339f4014fc
module: system
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.tool.call_sub.md
source_symbol: document
source_lines:
- 1
- 36
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.tool.call_sub.md#L1-L36
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: 76047af0d8a39e08fb4b456f27950e0e1e2af26f320f6517ce17a9a2d37f5929
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
{{if agent_profiles}}
### call_subordinate

you can use subordinates for subtasks
subordinates can be scientist coder engineer etc
message field: always describe role, task details goal overview for new subordinate
delegate specific subtasks not entire task
reset arg usage:
  "true": spawn new subordinate
  "false": continue existing subordinate
if superior, orchestrate
respond to existing subordinates using call_subordinate tool with reset false
profile arg usage: select from available profiles for specialized subordinates, leave empty for default

example usage
~~~json
{
    "thoughts": [
        "The result seems to be ok but...",
        "I will ask a coder subordinate to fix...",
    ],
    "tool_name": "call_subordinate",
    "tool_args": {
        "profile": "",
        "message": "...",
        "reset": "true"
    }
}
~~~

**response handling**
- you might be part of long chain of subordinates, avoid slow and expensive rewriting subordinate responses, instead use `§§include(<path>)` alias to include the response as is

**available profiles:**
{{agent_profiles}}
{{endif}}