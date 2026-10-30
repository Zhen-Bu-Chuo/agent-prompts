---
agent: agent-zero
prompt_id: agent.system.tool.browser-bb8b314a1758
module: system
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.tool.browser.md
source_symbol: document
source_lines:
- 1
- 36
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.tool.browser.md#L1-L36
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: 8ff07181170e42a9b3000d1e7c1db59541c63e3fefceece2345a5772033720da
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
### browser_agent:

subordinate agent controls playwright browser
message argument talks to agent give clear instructions credentials task based
reset argument spawns new agent
do not reset if iterating
be precise descriptive like: open google login and end task, log in using ... and end task
when following up start: considering open pages
dont use phrase wait for instructions use end task
downloads default in /a0/tmp/downloads
pass secrets and variables in message when needed

usage:
```json
{
  "thoughts": ["I need to log in to..."],
  "headline": "Opening new browser session for login",
  "tool_name": "browser_agent",
  "tool_args": {
    "message": "Open and log me into...",
    "reset": "true"
  }
}
```

```json
{
  "thoughts": ["I need to log in to..."],
  "headline": "Continuing with existing browser session",
  "tool_name": "browser_agent",
  "tool_args": {
    "message": "Considering open pages, click...",
    "reset": "false"
  }
}
```
