---
agent: aider
prompt_id: patch_prompts-d5bba0d58894
module: editing
variant: patch
upstream_repository: Aider-AI/aider
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 5dc9490bb35f9729ef2c95d00a19ccd30c26339c
source_path: aider/coders/patch_prompts.py
source_symbol: module.PatchPrompts.example_messages.2
source_lines:
- 46
- 78
source_permalink: https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/aider/coders/patch_prompts.py#L46-L78
source_committed_at: '2026-05-22T14:02:20Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:15Z'
extractor_version: 1.0.3
content_sha256: 840f99be7825a1485515aef5915967da58fd6f4607ae565493010deed6dfc5e4
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
To make this change we need to modify `mathweb/flask/app.py`:

1. Import the `math` module.
2. Replace the custom recursive `factorial()` helper with `math.factorial`.
3. Update `get_factorial()` to call `math.factorial`.

Here is the patch:

*** Begin Patch
*** Update File: mathweb/flask/app.py
@@
-from flask import Flask
-
-from flask import Flask
+from flask import Flask
+import math
@@
-def factorial(n):
-    "compute factorial"
-
-    if n == 0:
-        return 1
-    else:
-        return n * factorial(n-1)
+def factorial(n):
+    "compute factorial"
+
+    return math.factorial(n)
@@     def get_factorial(self, n):
-    return str(factorial(n))
+    return str(math.factorial(n))
*** End Patch
