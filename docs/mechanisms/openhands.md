# OpenHands prompt and mechanism sources

- Repository: [`OpenHands/software-agent-sdk`](https://github.com/OpenHands/software-agent-sdk)
- Selected release/branch: `v1.62.0`
- Commit: `504a88cab0fb48ee5226238ad7b8f1d865fa84a8`
- SPDX metadata: `MIT`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `system` | `python` | [`openhands-sdk/openhands/sdk/context/prompts/sections/static.py`](https://github.com/OpenHands/software-agent-sdk/blob/504a88cab0fb48ee5226238ad7b8f1d865fa84a8/openhands-sdk/openhands/sdk/context/prompts/sections/static.py) |
| `system` | `raw` | [`openhands-sdk/openhands/sdk/context/prompts/templates/ask_agent_template.j2`](https://github.com/OpenHands/software-agent-sdk/blob/504a88cab0fb48ee5226238ad7b8f1d865fa84a8/openhands-sdk/openhands/sdk/context/prompts/templates/ask_agent_template.j2) |
| `system` | `raw` | [`openhands-sdk/openhands/sdk/context/prompts/templates/skill_knowledge_info.j2`](https://github.com/OpenHands/software-agent-sdk/blob/504a88cab0fb48ee5226238ad7b8f1d865fa84a8/openhands-sdk/openhands/sdk/context/prompts/templates/skill_knowledge_info.j2) |
| `planning` | `python` | [`openhands-sdk/openhands/sdk/conversation/goal/prompts.py`](https://github.com/OpenHands/software-agent-sdk/blob/504a88cab0fb48ee5226238ad7b8f1d865fa84a8/openhands-sdk/openhands/sdk/conversation/goal/prompts.py) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `v1.62.0` at commit `504a88cab0fb48ee5226238ad7b8f1d865fa84a8`.
- OpenHands/OpenHands UI 仓库已将运行时 agent 移至 OpenHands/software-agent-sdk；采集该 SDK，并在机制文档记录迁移依据。
- 工具环境、事件流和执行反馈由运行时注入，模板仅代表静态片段。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- OpenHands/OpenHands UI 仓库已将运行时 agent 移至 OpenHands/software-agent-sdk；采集该 SDK，并在机制文档记录迁移依据。
- 工具环境、事件流和执行反馈由运行时注入，模板仅代表静态片段。

Product lineage noted in the adapter: [`OpenHands/OpenHands`](https://github.com/OpenHands/OpenHands); the source files above come from `OpenHands/software-agent-sdk`.
