---
agent: graphiti
prompt_id: eval-d25d0f69da0a
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: null
package_name: null
package_version: null
source_ref: main
source_commit: 72b5c59c06607e09ea855be61b6ff5a3446fc951
source_path: graphiti_core/prompts/eval.py
source_symbol: module.eval_add_episode_results.user_prompt.1
source_lines:
- 132
- 153
source_permalink: https://github.com/getzep/graphiti/blob/72b5c59c06607e09ea855be61b6ff5a3446fc951/graphiti_core/prompts/eval.py#L132-L153
source_committed_at: '2026-10-28T23:22:49Z'
release_published_at: null
fetched_at: '2026-10-31T06:40:29Z'
extractor_version: 1.0.3
content_sha256: eba70b539fc61298b7efebdd2daa0c32367502d7f1ad96b1159473b5a530e05c
license: Apache-2.0
source_kind: dynamic_template
extraction_notes: Static Python f-string source; expressions are preserved and have not been evaluated.
---

    Given the following PREVIOUS MESSAGES and MESSAGE, determine if the BASELINE graph data extracted from the 
    conversation is higher quality than the CANDIDATE graph data extracted from the conversation.
    
    Return False if the BASELINE extraction is better, and True otherwise. If the CANDIDATE extraction and
    BASELINE extraction are nearly identical in quality, return True. Add your reasoning for your decision to the reasoning field
    
    <PREVIOUS MESSAGES>
    {context['previous_messages']}
    </PREVIOUS MESSAGES>
    <MESSAGE>
    {context['message']}
    </MESSAGE>
    
    <BASELINE>
    {context['baseline']}
    </BASELINE>
    
    <CANDIDATE>
    {context['candidate']}
    </CANDIDATE>
    