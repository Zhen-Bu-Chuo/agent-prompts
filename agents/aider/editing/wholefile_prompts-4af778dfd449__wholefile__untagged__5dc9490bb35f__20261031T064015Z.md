---
agent: aider
prompt_id: wholefile_prompts-4af778dfd449
module: editing
variant: wholefile
upstream_repository: Aider-AI/aider
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 5dc9490bb35f9729ef2c95d00a19ccd30c26339c
source_path: aider/coders/wholefile_prompts.py
source_symbol: module.WholeFilePrompts.example_messages.1
source_lines:
- 24
- 38
source_permalink: https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/aider/coders/wholefile_prompts.py#L24-L38
source_committed_at: '2026-05-22T14:02:20Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:15Z'
extractor_version: 1.0.3
content_sha256: b7f2f6195e1ebe946208a9d383d3bad6563d1d6e56764d7716a179db752fe8e1
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
Ok, I will:

1. Switch the greeting text from "Hello" to "Hey".

show_greeting.py
{fence[0]}
import sys

def greeting(name):
    print(f"Hey {{name}}")

if __name__ == '__main__':
    greeting(sys.argv[1])
{fence[1]}
