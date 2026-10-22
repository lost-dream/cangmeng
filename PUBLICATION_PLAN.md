# cangmeng 公开发布方案

## 建议路线：公开核心＋本地扩展

公开一个能独立运行基本功能的核心，而不是上传完整私人整合包。用户调用 cangmeng 后，内置流程直接执行，可选流程读取用户本机已合法安装的原技能。

| 原模块 | 当前公开基础包 | 后续可行路线 |
|---|---|---|
| gc-minimal-zine-poster-v0-1 | 内置原指南，保留 MIT 与原作者 | 可继续维护整合，记录修改 |
| neil-quentin | 内置原指南，保留 MIT 与原作者 | 同上 |
| xxd-panel-224 / 100 / 028 | 当前作为本地可选扩展 | PolyForm Noncommercial 1.0.0 允许按条款非商用分发；可以另做明确标注非商用、保留全部许可与通知的扩展包，不能重标 MIT |
| scene-to-art-lab | 不复制指南或素材 | 本机使用仍受个人非商用许可约束。公开分发需先取得作者书面授权；不通过改名、改写、自动下载来替代授权 |
| scene-distillation-zine-v1-3 / CRT / culture / flipbook / remove-ai-watermarks 原指南 | 不随公开包分发；仅检测本地安装 | 本地未找到技能整体明确分发许可。核实上游许可或获得作者授权后再决定是否内置；不要把仓库可见当成可任意再分发 |
| 新增 PNG 元数据工具 | 内置自主新增代码 | 与原 remove-ai-watermarks 外部 CLI 区分，诚实说明有限处理范围 |

## 保留完整功能的另一条路线

逐个联系受限／许可不明模块的权利人，说明仓库公开、修改整合、是否商业、是否允许再分发与示例图展示。保留书面授权范围。获得授权后才把相应内容纳入公开包。此方案没有代你联系任何作者。

## 图片处理

私人包的 11 组对照图全部留在本地。公开基础包不含这些图片，也不含使用受限指南生成的宣传素材。公开画廊后续采用自己拍摄或有明确展示授权的输入图，再制作对应结果；记录每组来源、许可和是否 AI 生成。不要先提交受限图片再删除，因为 Git 历史仍可能保留。

## 你的贡献怎么写

推荐项目定位：

> cangmeng：面向照片视觉创作的模块化 Skill 工作台。实现按用途路由、本地扩展发现、第三方许可隔离，以及保持像素不变的 PNG 来源元数据处理；集成公开许可的上游海报流程并保留来源。

不要写成“独立原创 11 种视觉引擎”。如果扩展需要额外安装，在 README 和演示中明确标注。提交历史体现你在整合架构、工具与文档上的实际工作，不替代原作者署名。

## 具体发布步骤

1. 只把当前 cangmeng-public 目录作为仓库根目录；不要使用上层 github 目录或完整 cangmeng 私人包。
2. 阅读 README、LICENSE、THIRD_PARTY_NOTICES 与 publication-manifest，确认是公开基础版。
3. 在当前目录初始化全新 Git 历史，创建有意义的首个提交；不要复制私人版的历史。
4. 检查 Git 暂存文件，确保没有私有扩展、原图、生成缓存、凭据或私人包 ZIP。
5. 创建 GitHub 仓库，lost-dream/cangmeng，推送此公开基础版。
6. 发布说明写“2 个内置海报模块＋PNG 元数据工具＋可选本地扩展”，不写“11 模块开箱即用”。

当前发布目标为 https://github.com/lost-dream/cangmeng 。这份方案说明仓库的内容边界；完整私人版不进入公开 Git 历史。

## 核对依据

- [GitHub 官方：Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
- [PolyForm Noncommercial 1.0.0 正文](https://polyformproject.org/licenses/noncommercial/1.0.0)
- [GC Minimal Zine Poster 的 MIT 许可](https://github.com/LiamGvchi/gc-minimal-zine-poster/blob/main/LICENSE)
- Neil Quentin：本机安装副本的 LICENSE 为 MIT，版权行为 2026 Nealsun1993；原文随包保存。线上许可证页面本次读取超时，不据此声称已核实最新版。
- Scene to Art Lab：本机安装副本 LICENSE.txt 明确禁止未经书面授权的再分发，版权人为 2026 Niko；原受限文件未复制到此公开包。

核对日期：2026-10-22。方案依据所读取文本做发布范围整理，不代表代替权利人的额外授权。
