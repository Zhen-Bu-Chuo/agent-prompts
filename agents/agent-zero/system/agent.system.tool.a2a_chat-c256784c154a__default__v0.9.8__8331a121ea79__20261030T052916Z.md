---
agent: agent-zero
prompt_id: agent.system.tool.a2a_chat-c256784c154a
module: system
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.tool.a2a_chat.md
source_symbol: document
source_lines:
- 1
- 73
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.tool.a2a_chat.md#L1-L73
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: c1a50ac67ed8bbebb39b50d5e2ba3c8dcc68e731626b6782ad7e663eebe33ef8
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
### a2a_chat:
This tool lets Agent Zero chat with any other FastA2A-compatible agent.
It automatically keeps conversation **context** (so each subsequent call
continues the same dialogue) and supports optional file attachments.

#### What the tool can do
* Start a brand-new conversation with a remote agent.
* Continue an existing conversation transparently (context handled for you).
* Send text plus optional file URIs (images, docs, etc.).
* Receive the assistant’s reply as plain text.

#### Arguments
* `agent_url` (string, required) – Base URL of the *remote* agent.
  • Accepts `host:port`, `http://host:port`, or full path ending in `/a2a`.
* `message` (string, required) – The text you want to send.
* `attachments` (list[string], optional) – URIs pointing to files you want
  to send along with the message (can be http(s):// or file path).
* `reset` (boolean, optional) – Set to `true` to start a **new** conversation
  with the same `agent_url` (clears stored context). Default `false`.

> Leave **context_id** out – the tool handles it internally.

#### Usage – first message
##### Request
```json
{
  "thoughts": [
    "I want to ask the weather-bot for today’s forecast."
  ],
  "headline": "Ask remote agent (weather-bot)",
  "tool_name": "a2a_chat",
  "tool_args": {
    "agent_url": "http://weather.example.com:8000/a2a",
    "message": "Hello! What’s the forecast for Berlin today?",
    "attachments": [],
    "reset": false
  }
}
```
##### Response (assistant-side)
```plaintext
☀️ It will be sunny with a high of 22 °C.
```

#### Usage – follow-up (context automatically preserved)
##### Request
```json
{
  "thoughts": [
    "Need tomorrow’s forecast too."
  ],
  "headline": "Follow-up question",
  "tool_name": "a2a_chat",
  "tool_args": {
    "agent_url": "http://weather.example.com:8000/a2a",
    "message": "And tomorrow?",
    "attachments": [],
    "reset": false
  }
}
```
##### Response
```plaintext
🌦️ Partly cloudy with showers, high 18 °C.
```

#### Notes
1. **New conversation** – omit previous `agent_url` or use a *different* URL.
2. **Attachments** – supply absolute URIs ("http://…", "file:/…").
3. The tool stores session IDs per `agent_url` inside the current
   `AgentContext` – no manual handling required.
4. Use `"reset": true` to forget previous context and start a new chat.
5. The remote agent must implement FastA2A v0.2+ protocol.
