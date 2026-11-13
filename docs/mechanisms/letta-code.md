# Letta Code prompt and mechanism sources

- Repository: [`letta-ai/letta-code`](https://github.com/letta-ai/letta-code)
- Selected release/branch: `v0.34.59`
- Commit: `9c3cdb590fe2d1ff7512c3d77f24487a2023802f`
- SPDX metadata: `Apache-2.0`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `system` | `raw` | [`src/agent/prompts/letta.md`](https://github.com/letta-ai/letta-code/blob/9c3cdb590fe2d1ff7512c3d77f24487a2023802f/src/agent/prompts/letta.md) |
| `system` | `raw` | [`src/agent/prompts/letta_local_memfs.md`](https://github.com/letta-ai/letta-code/blob/9c3cdb590fe2d1ff7512c3d77f24487a2023802f/src/agent/prompts/letta_local_memfs.md) |
| `system` | `raw` | [`src/agent/prompts/letta_no_memfs.md`](https://github.com/letta-ai/letta-code/blob/9c3cdb590fe2d1ff7512c3d77f24487a2023802f/src/agent/prompts/letta_no_memfs.md) |
| `system` | `raw` | [`src/agent/prompts/letta_root_memfs.md`](https://github.com/letta-ai/letta-code/blob/9c3cdb590fe2d1ff7512c3d77f24487a2023802f/src/agent/prompts/letta_root_memfs.md) |
| `memory` | `raw` | [`src/agent/prompts/memory_filesystem.mdx`](https://github.com/letta-ai/letta-code/blob/9c3cdb590fe2d1ff7512c3d77f24487a2023802f/src/agent/prompts/memory_filesystem.mdx) |
| `memory` | `raw` | [`src/agent/prompts/recall_subagent.md`](https://github.com/letta-ai/letta-code/blob/9c3cdb590fe2d1ff7512c3d77f24487a2023802f/src/agent/prompts/recall_subagent.md) |
| `memory` | `raw` | [`src/agent/prompts/recall_subagent_local.md`](https://github.com/letta-ai/letta-code/blob/9c3cdb590fe2d1ff7512c3d77f24487a2023802f/src/agent/prompts/recall_subagent_local.md) |
| `memory` | `raw` | [`src/agent/subagents/builtin/memory.md`](https://github.com/letta-ai/letta-code/blob/9c3cdb590fe2d1ff7512c3d77f24487a2023802f/src/agent/subagents/builtin/memory.md) |
| `reflection` | `raw` | [`src/agent/subagents/builtin/reflection-v2.md`](https://github.com/letta-ai/letta-code/blob/9c3cdb590fe2d1ff7512c3d77f24487a2023802f/src/agent/subagents/builtin/reflection-v2.md) |
| `reflection` | `raw` | [`src/agent/subagents/builtin/reflection.md`](https://github.com/letta-ai/letta-code/blob/9c3cdb590fe2d1ff7512c3d77f24487a2023802f/src/agent/subagents/builtin/reflection.md) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `v0.34.59` at commit `9c3cdb590fe2d1ff7512c3d77f24487a2023802f`.
- source_claude.md、source_codex.md 等声明从其他产品预设或社区渠道导入的提示词不纳入 Letta Code 官方内容；核心 Memory Filesystem 和反思 Agent 模板取自 Letta Code 自有路径。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- source_claude.md、source_codex.md 等声明从其他产品预设或社区渠道导入的提示词不纳入 Letta Code 官方内容；核心 Memory Filesystem 和反思 Agent 模板取自 Letta Code 自有路径。
