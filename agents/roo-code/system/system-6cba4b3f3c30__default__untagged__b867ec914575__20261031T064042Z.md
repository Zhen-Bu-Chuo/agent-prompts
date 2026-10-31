---
agent: roo-code
prompt_id: system-6cba4b3f3c30
module: system
variant: default
upstream_repository: RooCodeInc/Roo-Code
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: b867ec9145750d0ae1ff7f02d35406e9bf2a0b16
source_path: src/core/prompts/system.ts
source_symbol: basePrompt.16
source_lines:
- 85
- 107
source_permalink: https://github.com/RooCodeInc/Roo-Code/blob/b867ec9145750d0ae1ff7f02d35406e9bf2a0b16/src/core/prompts/system.ts#L85-L107
source_committed_at: '2026-05-15T18:04:45Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:42Z'
extractor_version: 1.0.3
content_sha256: 4527b3575a434d74392302904e7ef981a95b3ed135ec6f8cfcc2c8eece50a3c2
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Raw JavaScript template body; escapes, expressions and nested templates are preserved without evaluation.
---
${roleDefinition}

${markdownFormattingSection()}

${getSharedToolUseSection()}${toolsCatalog}

	${getToolUseGuidelinesSection()}

${getCapabilitiesSection(cwd, shouldIncludeMcp ? mcpHub : undefined)}

${modesSection}
${skillsSection ? `\n${skillsSection}` : ""}
${getRulesSection(cwd, settings)}

${getSystemInfoSection(cwd)}

${getObjectiveSection()}

${await addCustomInstructions(baseInstructions, globalCustomInstructions || "", cwd, mode, {
	language: language ?? formatLanguage(vscode.env.language),
	rooIgnoreInstructions,
	settings,
})}