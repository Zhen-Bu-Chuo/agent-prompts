---
agent: openhands
prompt_id: skill_knowledge_info-ea3bd251d83b
module: system
variant: default
upstream_repository: OpenHands/software-agent-sdk
upstream_version: v1.59.0
package_name: openhands-sdk
package_version: null
source_ref: v1.59.0
source_commit: ccae18cb897bef7960f210aa3f380b577a84be7c
source_path: openhands-sdk/openhands/sdk/context/prompts/templates/skill_knowledge_info.j2
source_symbol: document
source_lines:
- 1
- 12
source_permalink: https://github.com/OpenHands/software-agent-sdk/blob/ccae18cb897bef7960f210aa3f380b577a84be7c/openhands-sdk/openhands/sdk/context/prompts/templates/skill_knowledge_info.j2#L1-L12
source_committed_at: '2026-10-28T14:34:29Z'
release_published_at: '2026-10-28T14:34:44Z'
fetched_at: '2026-10-30T05:30:04Z'
extractor_version: 1.0.3
content_sha256: 6e8a84b0022ccc9d82cbb65ced47c52dbc125e01726d9e2653c602096fb35d87
license: MIT
source_kind: template_document
extraction_notes: Original standalone template; runtime placeholders are preserved.
---
{% for agent_info in triggered_agents %}
<EXTRA_INFO>
The following information has been included based on a keyword match for "{{ agent_info.trigger }}".
It may or may not be relevant to the user's request.
{% if agent_info.location %}
Skill location: {{ agent_info.location }}
(Use this path to resolve relative file references in the skill content below)
{% endif %}

{{ agent_info.content }}
</EXTRA_INFO>
{% endfor %}
