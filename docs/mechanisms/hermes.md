# Hermes Agent prompt and mechanism sources

- Repository: [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent)
- Selected release/branch: `v2026.9.24`
- Commit: `f97608f178d1ffeca59860195ab7da295f7c8e5f`
- SPDX metadata: `MIT`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `skills` | `python` | [`agent/learn_prompt.py`](https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/learn_prompt.py) |
| `memory` | `python` | [`agent/memory_manager.py`](https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/memory_manager.py) |
| `planning` | `python` | [`agent/plan_prompt.py`](https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/plan_prompt.py) |
| `context` | `python` | [`agent/prompt_builder.py`](https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/prompt_builder.py) |
| `system` | `python` | [`agent/system_prompt.py`](https://github.com/NousResearch/hermes-agent/blob/f97608f178d1ffeca59860195ab7da295f7c8e5f/agent/system_prompt.py) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `v2026.9.24` at commit `f97608f178d1ffeca59860195ab7da295f7c8e5f`.
- 第三方 optional-skills prompts 不自动归属于 Hermes 官方内置系统，仅采集 agent 核心源码。
- 静态 AST 提取提示词常量，无法重构后端、工具、运行态 memory 和配置条件共同生成的最终消息。
- 最新稳定版已将旧版 memory_context.py 与 memory_manager_tools.py 删除；记忆上下文模板改从 memory_manager.py 中仍存在的核心消息构造提取。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 第三方 optional-skills prompts 不自动归属于 Hermes 官方内置系统，仅采集 agent 核心源码。
- 静态 AST 提取提示词常量，无法重构后端、工具、运行态 memory 和配置条件共同生成的最终消息。
