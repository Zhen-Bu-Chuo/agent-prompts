---
agent: gemini-cli
prompt_id: snippets-f4c35538ff07
module: context
variant: default
upstream_repository: google-gemini/gemini-cli
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 6814e00d6b148c3a1d57244d5d7040f7c541009d
source_path: packages/core/src/prompts/snippets.ts
source_symbol: getCoreSystemPrompt.8
source_lines:
- 137
- 163
source_permalink: https://github.com/google-gemini/gemini-cli/blob/6814e00d6b148c3a1d57244d5d7040f7c541009d/packages/core/src/prompts/snippets.ts#L137-L163
source_committed_at: '2026-10-30T21:38:47Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:26Z'
extractor_version: 1.0.3
content_sha256: d6ae54c29768ebc5eb519f5f36edf6b8637a3032e4065420208caa6abff04c00
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---

${renderPreamble(options.preamble)}

${renderCoreMandates(options.coreMandates)}

${renderSubAgents(options.subAgents)}

${renderAgentSkills(options.agentSkills)}

${renderHookContext(options.hookContext)}

${
  options.planningWorkflow
    ? renderPlanningWorkflow(options.planningWorkflow)
    : renderPrimaryWorkflows(options.primaryWorkflows)
}

${options.taskTracker ? renderTaskTracker(options.taskTracker) : ''}

${renderOperationalGuidelines(options.operationalGuidelines)}

${renderInteractiveYoloMode(options.interactiveYoloMode)}

${renderSandbox(options.sandbox)}

${renderGitRepo(options.gitRepo)}
