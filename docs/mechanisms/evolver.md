# EvoMap Evolver prompt and mechanism sources

- Repository: [`EvoMap/evolver`](https://github.com/EvoMap/evolver)
- Selected release/branch: `v2.0.47`
- Commit: `4e12b93bd5d1173ee0c3bd2ae72de8030f82db7a`
- SPDX metadata: `GPL-3.0-or-later`
- Collection status: `partial`

## Selected source files

| Module | Extractor | Pinned source |
| --- | --- | --- |
| `evolution` | `js-strings` | [`packages/evolver-core/dist/exec/prompt.js`](https://github.com/EvoMap/evolver/blob/4e12b93bd5d1173ee0c3bd2ae72de8030f82db7a/packages/evolver-core/dist/exec/prompt.js) |

## Current coverage

- Coverage: `partial`.
- Pinned upstream version: `v2.0.47` at commit `4e12b93bd5d1173ee0c3bd2ae72de8030f82db7a`.
- v2.0.46 只提供 transpiled dist 源码；README 标注 GPL-3.0-or-later，没有独立根 LICENSE 文件。保留 README license 声明与源码链接。
- personality/prompt.js 已混淆并排除；exec/prompt.js 中仅保存静态可读字符串片段，标记为片段而非重建完整运行时 prompt。

## Collection notes
The collector reads only these configured file paths from the pinned commit. It parses structured strings and templates as data and does not run the upstream agent. A source entry is a static template fragment; values supplied at runtime remain unresolved.

- v2.0.46 只提供 transpiled dist 源码；README 标注 GPL-3.0-or-later，没有独立根 LICENSE 文件。保留 README license 声明与源码链接。
- personality/prompt.js 已混淆并排除；exec/prompt.js 中仅保存静态可读字符串片段，标记为片段而非重建完整运行时 prompt。
