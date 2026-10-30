---
agent: aider
prompt_id: editblock_fenced_prompts-703cdc3358b4
module: editing
variant: editblock_fenced
upstream_repository: Aider-AI/aider
upstream_version: v0.86.0
package_name: null
package_version: null
source_ref: v0.86.0
source_commit: a4be6ccd87ebaa59b361f3f028d116ce1761b626
source_path: aider/coders/editblock_fenced_prompts.py
source_symbol: module.EditBlockFencedPrompts.example_messages.2
source_lines:
- 14
- 56
source_permalink: https://github.com/Aider-AI/aider/blob/a4be6ccd87ebaa59b361f3f028d116ce1761b626/aider/coders/editblock_fenced_prompts.py#L14-L56
source_committed_at: '2025-08-09T15:54:51Z'
release_published_at: '2025-08-09T17:42:19Z'
fetched_at: '2026-10-30T05:29:16Z'
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
