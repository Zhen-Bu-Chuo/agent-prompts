---
agent: aider
prompt_id: editblock_fenced_prompts-703cdc3358b4
module: editing
variant: editblock_fenced
upstream_repository: Aider-AI/aider
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 5dc9490bb35f9729ef2c95d00a19ccd30c26339c
source_path: aider/coders/editblock_fenced_prompts.py
source_symbol: module.EditBlockFencedPrompts.example_messages.2
source_lines:
- 14
- 56
source_permalink: https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/aider/coders/editblock_fenced_prompts.py#L14-L56
source_committed_at: '2026-05-22T14:02:20Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:15Z'
extractor_version: 1.0.3
content_sha256: 13dbad1a5a4246546a9eaef1895c4aa62633cf7f7c32096b6816d2828ea06a8e
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
To make this change we need to modify `mathweb/flask/app.py` to:

1. Import the math package.
2. Remove the existing factorial() function.
3. Update get_factorial() to call math.factorial instead.

Here are the *SEARCH/REPLACE* blocks:

{fence[0]}python
mathweb/flask/app.py
<<<<<<< SEARCH
from flask import Flask
=======
import math
from flask import Flask
>>>>>>> REPLACE
{fence[1]}

{fence[0]}python
mathweb/flask/app.py
<<<<<<< SEARCH
def factorial(n):
    "compute factorial"

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
>>>>>>> REPLACE
{fence[1]}

{fence[0]}python
mathweb/flask/app.py
<<<<<<< SEARCH
    return str(factorial(n))
=======
    return str(math.factorial(n))
>>>>>>> REPLACE
{fence[1]}
<<<<<<< HEAD
