# OpenCode prompt and mechanism sources

- Repository: [`anomalyco/opencode`](https://github.com/anomalyco/opencode)
- Selected release/branch: `v2.2.5`
- Commit: `9bbb8ce18c80f099e0e448775f59d965ead40a21`
- SPDX metadata: `MIT`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `system` | `raw` | [`packages/core/src/plugin/system-prompt/anthropic.txt`](https://github.com/anomalyco/opencode/blob/9bbb8ce18c80f099e0e448775f59d965ead40a21/packages/core/src/plugin/system-prompt/anthropic.txt) |
| `system` | `raw` | [`packages/core/src/plugin/system-prompt/gpt-astra.txt`](https://github.com/anomalyco/opencode/blob/9bbb8ce18c80f099e0e448775f59d965ead40a21/packages/core/src/plugin/system-prompt/gpt-astra.txt) |
| `system` | `raw` | [`packages/core/src/plugin/system-prompt/gpt.txt`](https://github.com/anomalyco/opencode/blob/9bbb8ce18c80f099e0e448775f59d965ead40a21/packages/core/src/plugin/system-prompt/gpt.txt) |
| `system` | `raw` | [`packages/core/src/plugin/system-prompt/kimi.txt`](https://github.com/anomalyco/opencode/blob/9bbb8ce18c80f099e0e448775f59d965ead40a21/packages/core/src/plugin/system-prompt/kimi.txt) |
| `system` | `raw` | [`packages/core/src/plugin/system-prompt/meta.txt`](https://github.com/anomalyco/opencode/blob/9bbb8ce18c80f099e0e448775f59d965ead40a21/packages/core/src/plugin/system-prompt/meta.txt) |
| `system` | `raw` | [`packages/core/src/plugin/system-prompt/trinity.txt`](https://github.com/anomalyco/opencode/blob/9bbb8ce18c80f099e0e448775f59d965ead40a21/packages/core/src/plugin/system-prompt/trinity.txt) |
| `system` | `raw` | [`packages/core/src/session/runner/prompt/system.txt`](https://github.com/anomalyco/opencode/blob/9bbb8ce18c80f099e0e448775f59d965ead40a21/packages/core/src/session/runner/prompt/system.txt) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `v2.2.5` at commit `9bbb8ce18c80f099e0e448775f59d965ead40a21`.
- 模型专属 system prompt 按上游模型文件独立保存；会话消息、工具可用性和运行时上下文仍由调度代码动态组装。
- 只选择固定 system prompt 和 session prompt 构造模块，TUI 用户输入占位不作为 agent system prompt。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 模型专属 system prompt 按上游模型文件独立保存；会话消息、工具可用性和运行时上下文仍由调度代码动态组装。
- 只选择固定 system prompt 和 session prompt 构造模块，TUI 用户输入占位不作为 agent system prompt。
