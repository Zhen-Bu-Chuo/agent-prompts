# Kilo Code prompt and mechanism sources

- Repository: [`Kilo-Org/kilocode`](https://github.com/Kilo-Org/kilocode)
- Selected release/branch: `v7.8.18`
- Commit: `b81761530650f8ec7b071441f4f54d2514f1a244`
- SPDX metadata: `MIT`
- Collection status: `unavailable`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| — | metadata only | No prompt text is copied from this pinned source. |

## Current coverage

- Coverage: `unavailable`.
- Pinned upstream version: `v7.8.18` at commit `b81761530650f8ec7b071441f4f54d2514f1a244`.
- 已核对稳定版本中 core 的 prompt.ts 仅导出上游 schema，instruction-context.ts 仅定义上下文数据结构；当前仓库未找到可归属于 Kilo 的静态模型提示词模板，因此只记录版本、提交与来源。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- 按 Kilo core 包定向采集；捆绑的 OpenCode CLI 通用实现不重复归类为 Kilo 专有提示词。
