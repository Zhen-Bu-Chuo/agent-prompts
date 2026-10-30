---
agent: graphiti
prompt_id: extract_nodes_and_edges-ae62eacd2875
module: memory
variant: default
upstream_repository: getzep/graphiti
upstream_version: v0.31.2
package_name: null
package_version: null
source_ref: v0.31.2
source_commit: d72407dcedac911e1be9fc15b55e8c05a3efcc36
source_path: graphiti_core/prompts/extract_nodes_and_edges.py
source_symbol: module._C2_INSTRUCTION_TEXT.1
source_lines:
- 126
- 152
source_permalink: https://github.com/getzep/graphiti/blob/d72407dcedac911e1be9fc15b55e8c05a3efcc36/graphiti_core/prompts/extract_nodes_and_edges.py#L126-L152
source_committed_at: '2026-10-20T17:23:18Z'
release_published_at: '2026-10-20T17:25:21Z'
fetched_at: '2026-10-30T05:29:43Z'
extractor_version: 1.0.3
content_sha256: 808e046c7b9f21e845cf58b1e9ad5d37b9ad0d55bd683f739c380883e2e40d1d
license: Apache-2.0
source_kind: static_template
extraction_notes: Python string decoded by the AST parser; upstream code was not executed.
---
# Goal
Turn CURRENT MESSAGES into a knowledge graph: a list of entities and a list of facts (edges) between them. A good result lets an agent answer "who said, did, wants, owns, plans, feels, recommends, or knows what" without the source text.

# What good output looks like
- Complete: every episode, post, and speaker with real content is covered, including the later ones in a long input. Preferences, opinions, plans, commitments, requests, questions, emotions, experiences, advice, and results all count. Skip only content-free turns ("Hi!", "Thanks!", "Bye!").
- Attributed: when a named person, author, account, or organization states, recommends, or does something, that actor is the source entity, and the fact text names the actor.
- Self-contained: each fact is one plain sentence that uses entity names (no pronouns), keeps the specific details (numbers, dates, prices, versions, names), and makes sense with no other context.
- Compact: one fact for one statement. Keep a list of items from one statement in one fact ("Marina plans to change into a sweater and trousers."), unless each item has its own details. Do not make a fact or an entity for each list item. Not redundant: If the same fact appears in more than one episode, emit it once and list all of its episode indices.

# Entities
- Speakers. Name each speaker with the most complete name available. When a message header has profile fields (first_name and last_name, given_name and family_name, user_alias, screen_name), use the full personal name, for example "Marisol Beckett". Use "User" only when no name is available.
- Other entities: named people, organizations, places, products, files, tickets, projects, events, documents, and named or described objects, plus hobbies and activities that someone does ("road cycling", "watercolor painting"). Use the most specific form mentioned, at most 5 words, as a noun phrase. For a person's possession, pet, project, or creation, use a possessive name ("Calvin's guitar", "Marina's sweater"), not the bare noun.
- Do not make entities from: pronouns or unresolved references ("the city", "this issue"); vague abstractions ("growth", "life", "time"); clock times, dates, quantities, prices, durations, measurements, or coordinates (keep these in the fact text, unless the value is itself an edge endpoint such as a version string); answer options or template tokens ("Agree", "Strongly disagree"); imperative tips ("Buy in bulk" becomes the topic "bulk buying"); quoted slogans or idioms; tutorial example values ("/path/to/source", "file.txt").
- Each entity appears once. Classify it with an entity_type_id from ENTITY TYPES. Extract entities only from CURRENT MESSAGES; use PREVIOUS MESSAGES and [CONTEXT EPISODE] messages only to resolve references.

# Facts
- source_entity_name and target_entity_name must be names from extracted_entities. If an endpoint is a value such as a version, add it as an entity.
- Connect the actor directly to the thing: "Calvin -> PERFORMED_IN -> Tokyo", "Mira Sen -> RECOMMENDS_METRICS_FOR -> Ember & Oak". Do not route a relationship through descriptive nouns ("city lights -> LOCATED_IN -> Tokyo"), and do not turn an actor's claim into a fact between two nouns that the actor mentioned.
- Use a self-referencing fact (source and target are the same entity) only when a statement is about one entity and no other extracted entity fits, for example a routine, a feeling, or a health state ("Evan has a knee injury.").
- When a fact involves two extracted entities, use both as source and target.
- Use PREVIOUS MESSAGES and [CONTEXT EPISODE] messages to resolve what the current message refers to, and write the resolved fact ("all the hard work paid off" becomes what paid off). [CONTEXT EPISODE] messages are conversation turns between the numbered episodes, shown so you can read the conversation in order.
- Set episode_indices to the 0-based [Episode N] numbers that the fact comes from. Messages headed [CONTEXT EPISODE] are not numbered episodes: do not extract facts from them and do not give them an episode index.
- Write each entity name and each fact in the dominant language of its source episode. Keep proper names as written. Write relation_type as an English SCREAMING_SNAKE_CASE label.
- A fact states what the source says. Do not add reasoning, hedges ("appears to", "suggests"), or commentary.

# Output
Return only the JSON object: {"extracted_entities":[{"name":"...","entity_type_id":0}],"edges":[{"source_entity_name":"...","target_entity_name":"...","relation_type":"...","fact":"...","episode_indices":[0]}]}.