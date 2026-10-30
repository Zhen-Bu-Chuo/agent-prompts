---
agent: agent-zero
prompt_id: agent.system.tool.document_query-b6efcc0a64a7
module: tools
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.tool.document_query.md
source_symbol: document
source_lines:
- 1
- 62
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.tool.document_query.md#L1-L62
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: f9838259739b2d91e89e2009597691f3c6deb329579cfb6ca8bce108bbf36ee3
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
### document_query
read and analyze remote/local documents get text content or answer questions
pass a single url/path or a list for multiple documents in "document"
for web documents use "http://" or "https://"" prefix
for local files "file://" prefix is optional but full path is required
if "queries" is empty tool returns document content
if "queries" is a list of strings tool returns answers
supports various formats HTML PDF Office Text etc
usage:

1 get content
~~~json
{
    "thoughts": [
        "I need to read..."
    ],
    "headline": "...",
    "tool_name": "document_query",
    "tool_args": {
        "document": "https://.../document"
    }
}
~~~

2 query document
~~~json
{
    "thoughts": [
        "I need to answer..."
    ],
    "headline": "...",
    "tool_name": "document_query",
    "tool_args": {
        "document": "https://.../document",
        "queries": [
            "What is...",
            "Who is..."
        ]
    }
}
~~~

3 query multiple documents
~~~json
{
    "thoughts": [
        "I need to compare..."
    ],
    "headline": "...",
    "tool_name": "document_query",
    "tool_args": {
        "document": [
            "https://.../document-one",
            "file:///path/to/document-two"
        ],
        "queries": [
            "Compare the main conclusions...",
            "What are the key differences..."
        ]
    }
}
~~~
