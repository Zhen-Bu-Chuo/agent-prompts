---
agent: gemini-cli
prompt_id: snippets-f4c35538ff07
module: context
variant: default
upstream_repository: google-gemini/gemini-cli
upstream_version: v0.66.0
package_name: null
package_version: null
source_ref: v0.66.0
source_commit: 970413207732f5d4d8c50540c7fc359c44fdaaf2
source_path: packages/core/src/prompts/snippets.ts
source_symbol: getCoreSystemPrompt.8
source_lines:
- 137
- 163
source_permalink: https://github.com/google-gemini/gemini-cli/blob/970413207732f5d4d8c50540c7fc359c44fdaaf2/packages/core/src/prompts/snippets.ts#L137-L163
source_committed_at: '2026-10-27T20:19:20Z'
release_published_at: '2026-10-27T20:26:28Z'
fetched_at: '2026-10-30T05:29:35Z'
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
