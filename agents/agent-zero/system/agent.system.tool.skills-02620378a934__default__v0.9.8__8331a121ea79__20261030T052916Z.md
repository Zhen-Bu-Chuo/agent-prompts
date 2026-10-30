---
agent: agent-zero
prompt_id: agent.system.tool.skills-02620378a934
module: system
variant: default
upstream_repository: agent0ai/agent-zero
upstream_version: v0.9.8
package_name: null
package_version: null
source_ref: v0.9.8
source_commit: 8331a121ea795b099953206ffc6b663ba5080e04
source_path: prompts/agent.system.tool.skills.md
source_symbol: document
source_lines:
- 1
- 82
source_permalink: https://github.com/agent0ai/agent-zero/blob/8331a121ea795b099953206ffc6b663ba5080e04/prompts/agent.system.tool.skills.md#L1-L82
source_committed_at: '2026-02-10T17:47:21Z'
release_published_at: '2026-02-10T18:25:22Z'
fetched_at: '2026-10-30T05:29:16Z'
extractor_version: 1.0.3
content_sha256: 87c0d01851b432f09ced7401ff6c0755414bd2af21a183294d4de4643d597911
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
### skills_tool

#### overview

skills are folders with instructions scripts files
give agent extra capabilities
agentskills.io standard

#### workflow
1. skill list titles descriptions in system prompt section available skills
2. use skills_tool:load to get full skill instructions and context
4. use code_execution_tool to run scripts or read files

#### examples

##### skills_tool:list

list all skills with metadata name version description tags author
only use when details needed

~~~json
{
    "thoughts": [
        "Need find skills of certain properties...",
    ],
    "headline": "Listing all available skills",
    "tool_name": "skills_tool:list",
}
~~~

##### skills_tool:load

loads complete SKILL.md content instructions procedures
returns metadata content file tree
use when potential skill identified and want usage instructions
use again when no longer in history

~~~json
{
    "thoughts": [
        "User needs PDF form extraction",
        "pdf_editing skill will provide procedures",
        "Loading full skill content"
    ],
    "headline": "Loading PDF editing skill",
    "tool_name": "skills_tool:load",
    "tool_args": {
        "skill_name": "pdf_editing"
    }
}
~~~

##### executing skill scripts

use skills_tool:load identify skill script files and instructions
use code_execution_tool runtime terminal to execute
write command and parameters as instructed
use full paths or cd to skill directory

~~~json
{
    "thoughts": [
        "Need to convert PDF to images",
        "Skill provides convert_pdf_to_images.py at scripts/convert_pdf_to_images.py",
        "Using code_execution_tool to run it directly"
    ],
    "headline": "Converting PDF to images",
    "tool_name": "code_execution_tool",
    "tool_args": {
        "runtime": "terminal",
        "code": "python /path/to/skill/scripts/convert_pdf_to_images.py /path/to/document.pdf /tmp/images"
    }
}
~~~

#### skills guide
use skills when relevant for task
load skill before use
read / execute files with code_execution_tool
follow instructions in skill
mind relative paths
conversation history discards old messages use skills_tool:load again when lost