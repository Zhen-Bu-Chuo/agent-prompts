---
agent: agent-zero
prompt_id: agent.system.tool.notify_user-d7f1cdf015b4
module: tools
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.tool.notify_user.md
source_symbol: document
source_lines:
- 1
- 43
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.tool.notify_user.md#L1-L43
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: 5aa49bfa79abfb4b18b6981e7d5056cac199acad09030d88736c68a6f00b6926
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
### notify_user:
This tool can be used to notify the user of a message independent of the current task.

!!! This is a universal notification tool
!!! Supported notification types: info, success, warning, error, progress

#### Arguments:
 *  "message" (string) : The message to be displayed to the user.
 *  "title" (Optional, string) : The title of the notification.
 *  "detail" (Optional, string) : The detail of the notification. May contain html tags.
 *  "type" (Optional, string) : The type of the notification. Can be "info", "success", "warning", "error", "progress".

#### Usage examples:
##### 1: Success notification
```json
{
    "thoughts": [
        "...",
    ],
    "tool_name": "notify_user",
    "tool_args": {
        "message": "Important notification: task xyz is completed succesfully",
        "title": "Task Completed",
        "detail": "This is a test notification detail with <a href='https://www.google.com'>link</a>",
        "type": "success"
    }
}
```
##### 2: Error notification
```json
{
    "thoughts": [
        "...",
    ],
    "tool_name": "notify_user",
    "tool_args": {
        "message": "Important notification: task xyz is failed",
        "title": "Task Failed",
        "detail": "This is a test notification detail with <a href='https://www.google.com'>link</a> and <img src='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'>",
        "type": "error"
    }
}
```
