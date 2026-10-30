---
agent: memu
prompt_id: skill-8f77ed75a6b4
module: memory
variant: default
upstream_repository: NevaMind-AI/memU
upstream_version: v1.5.1
package_name: null
package_version: null
source_ref: v1.5.1
source_commit: 357aefc8012705bfde723f141d52f675fe712bed
source_path: src/memu/prompts/memory_type/skill.py
source_symbol: module.PROMPT_BLOCK_RULES.1
source_lines:
- 370
- 427
source_permalink: https://github.com/NevaMind-AI/memU/blob/357aefc8012705bfde723f141d52f675fe712bed/src/memu/prompts/memory_type/skill.py#L370-L427
source_committed_at: '2026-03-23T07:38:14Z'
release_published_at: '2026-03-23T07:38:28Z'
fetched_at: '2026-10-30T05:30:00Z'
extractor_version: 1.0.3
content_sha256: 2ea92abfeba1d73e8ecd769e76c670d1a65802421b6c683d9262517ab3b7668b
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---

# Rules
## General requirements (must satisfy all)
- Each skill must be formatted as a comprehensive skill profile with frontmatter and all required sections.
- Each skill profile must capture not just WHAT was done, but HOW and WHY it works.
- Be specific and concrete - include technology names, version numbers, metrics, and outcomes.
- Each skill should be comprehensive enough to be referenced and applied independently.
- Minimum 300 words per skill to ensure depth and actionability.
Important: Extract only skills that are clearly demonstrated or described in the resource. No guesses or fabricated details.

## Skill Profile Structure (must include all sections)
1. Frontmatter: name, description, category, demonstrated-in
2. Introduction paragraph
3. Core Principles
4. When to Use This Skill
5. Implementation Guide (Prerequisites, Techniques and Approaches, Example from Resource)
6. Success Patterns
7. Common Pitfalls
8. Key Takeaways

## Special rules for Skill Information
- Generic statements without concrete approaches are forbidden (e.g., "Used Docker", "Good at programming").
- Opinions without demonstrated practice are forbidden (e.g., "I think microservices are better").
- Theory without practice belongs to knowledge type, not skill type.
- One-time luck without a replicable approach is not a skill.
- Trivial actions are not skills (e.g., "Using email", "Reading docs").

## What TO Extract
- Concrete approaches with context, tools, metrics, and outcomes.
- Deployment strategies with specific techniques (canary, blue-green, etc.).
- Incident response procedures with detection, response, and recovery steps.
- Problem-solving approaches with tool orchestration patterns.
- Multi-step workflows with reasoning steps and validation approaches.

## Resource Type Guidelines
### For Deployment Logs:
- Extract each significant deployment (success or failure) as a separate skill.
- Success: Focus on techniques that worked.
- Failure: Focus on incident response, root cause analysis, recovery procedures.
- Include metrics: deployment time, error rates, response times, recovery time.

### For Workflow Documentation:
- Extract major workflow stages as skills.
- Include tool chains and technology stacks.
- Document step-by-step procedures.
- Note success metrics and KPIs.

### For Agent Execution Logs:
- Extract problem-solving approaches as skills.
- Include tool orchestration patterns.
- Document reasoning steps and validation approaches.
- Capture multi-step workflows.

## Review & validation rules
- Ensure all required sections are present in each skill profile.
- Verify minimum 300 words per skill.
- Final check: every skill profile must be actionable and replicable.
