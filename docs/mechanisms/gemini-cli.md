# Gemini CLI prompt and mechanism sources

- Repository: [`google-gemini/gemini-cli`](https://github.com/google-gemini/gemini-cli)
- Selected release/branch: `v0.68.0`
- Commit: `5a5c7180ff3f0a02511f54b54db7f228d4982a30`
- SPDX metadata: `Apache-2.0`
- Collection status: `supported`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `context` | `js-strings` | [`packages/core/src/prompts/snippets.ts`](https://github.com/google-gemini/gemini-cli/blob/5a5c7180ff3f0a02511f54b54db7f228d4982a30/packages/core/src/prompts/snippets.ts) |

## Current coverage

- Coverage: `supported`.
- Pinned upstream version: `v0.68.0` at commit `5a5c7180ff3f0a02511f54b54db7f228d4982a30`.
- 按核心提示词模块筛选；项目/会话配置、用户规则、动态 MCP 工具清单和实际子代理消息取决于运行时。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 按核心提示词模块筛选；项目/会话配置、用户规则、动态 MCP 工具清单和实际子代理消息取决于运行时。
