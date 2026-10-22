# cangmeng · 苍梦

**一个入口，按用途调用照片海报与本地视觉技能。**

维护：[@lost-dream](https://github.com/lost-dream)。本项目的新增贡献是统一任务路由、本地扩展发现、PNG 来源元数据处理及整合文档。两份内置海报指南来自上游 MIT 项目，原作者和许可已保留。

## 公开版实际包含什么

- 极简纸张 Zine 海报：内置 gc-minimal-zine-poster-v0-1 指南。
- Pulp 印刷海报：内置 neil-quentin 指南。
- PNG 来源元数据工具：识别／移除受支持的 AI 来源块，保留压缩像素数据与色彩配置，输出独立报告。
- 可选本地扩展：检查并调用用户自行合法安装的其他视觉技能。未安装时会说明，不冒充内置功能。

**它不是完整 11 模块私人包的公开镜像。** 其他艺术媒介、CRT、文化视觉、XXD、照片书等功能需要用户本机另有对应技能。没有预装图像模型或生成额度。

## 安装与使用

可以让支持技能安装的助手执行：

```text
请安装 https://github.com/lost-dream/cangmeng 仓库中 skills/cangmeng 目录下的 skill。
```

也可以将本仓库 `skills/cangmeng` 文件夹放入你的技能目录后调用 `$cangmeng`。同一环境只安装一个同名 cangmeng；安装前检查是否已有私人完整版，不覆盖而不知情。

```text
使用 $cangmeng，把这张照片做成极简纸张 zine 海报。
使用 $cangmeng，把这张图做成 pulp 印刷海报，标题 NIGHT WALK。
使用 $cangmeng，清理这张我拥有的 PNG 的 AI 来源元数据，保留原文件和像素。
使用 $cangmeng，检查我本机有没有照片翻页书扩展。
```

实际生图仍使用用户选定的 Image2 API 或内置 image_gen；一批选择一次。纯扩展检查与元数据处理无需生图。

```text
<python> skills/cangmeng/scripts/list_extensions.py --json
<python> skills/cangmeng/scripts/png_provenance.py identify input.png
<python> skills/cangmeng/scripts/png_provenance.py clean input.png --output clean.png --report clean-report.json
```

`<python>` 表示本机可用 Python。两个脚本仅使用标准库。扩展检查只查看已知技能目录，不联网、不安装、不上传素材。元数据工具不去除可见版权水印，也不能证明作品不是 AI 生成，不能声称移除了所有隐形信号。

## 图片与示例

此公开基础包没有附带原私人画廊或上游样例照片。公开示例应使用维护者自己拍摄或有明确展示授权的素材；如果是生成图，说明其来源与 AI 生成事实。模块／提示词许可不自动解决每张照片和素材的展示权问题。

## 许可与来源

新增核心与两个随附海报指南按各自 MIT 条款使用，保留 [第三方署名](THIRD_PARTY_NOTICES.md)。可选扩展不随包分发，不受本项目 MIT 覆盖。

发布策略、扩展范围与完整私人版差异见 [PUBLICATION_PLAN.md](PUBLICATION_PLAN.md)。本仓库只发布公开基础版；私人完整版、私人画廊及其完整 ZIP 不属于仓库内容。
