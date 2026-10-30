---
agent: swe-agent
prompt_id: default_backticks-f13ecabafbe5
module: system
variant: default
upstream_repository: SWE-agent/SWE-agent
upstream_version: v1.1.0
package_name: null
package_version: null
source_ref: v1.1.0
source_commit: 0f3acafacabc0def8cc76b4e48acb4b6cf302cb9
source_path: config/default_backticks.yaml
source_symbol: agent.templates.instance_template
source_lines:
- 1
- 63
source_permalink: https://github.com/SWE-agent/SWE-agent/blob/0f3acafacabc0def8cc76b4e48acb4b6cf302cb9/config/default_backticks.yaml#L1-L63
source_committed_at: '2025-05-22T16:10:41Z'
release_published_at: '2025-05-22T16:11:39Z'
fetched_at: '2026-10-30T05:30:13Z'
extractor_version: 1.0.3
content_sha256: 10de1455c0139004a0bee751fcd2bda2e44b97abe3ba8454a71b0b49d3678e98
license: MIT
source_kind: structured_template
extraction_notes: Value selected from a structured configuration; line range cites the complete file.
---
<uploaded_files>
{{working_dir}}
</uploaded_files>
I've uploaded a python code repository in the directory {{working_dir}}. Consider the following PR description:

<pr_description>
{{problem_statement}}
</pr_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <pr_description> are met?
I've already taken care of all changes to any of the test files described in the <pr_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-tests files in the {{working_dir}} directory to ensure the <pr_description> is satisfied.
Follow these steps to resolve the issue:
1. As a first step, it might be a good idea to find and read code relevant to the <pr_description>
2. Create a script to reproduce the error and execute it with `python <filename.py>` using the bash tool, to confirm the error
3. Edit the sourcecode of the repo to resolve the issue
4. Rerun your reproduce script and confirm that the error is fixed!
5. Think about edgecases and make sure your fix handles them as well
Your thinking should be thorough and so it's fine if it's very long.