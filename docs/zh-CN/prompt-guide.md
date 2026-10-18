# DeepSeek V4.1 Flash 1017 提示词写法：如何让 V4.1 Flash 写出能做视频的页面

[English](../prompt-guide.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

DeepSeek V4.1 Flash 1017 并不直接输出视频。它写的是代码（用 Three.js、Canvas 或 SVG 做的 HTML 页面），作者再把页面播放的过程录下来。在 DeepSeek 的 Harness 里，它还能操控 Blender。下面的写法来自创作者随视频公开的提示词，以及 SandBase Lab 测试模型时使用的固定提示词。每个例子都链接到它生成的视频。

## 1. 先说清要什么文件

写明格式和运行环境。公开出来、效果好的提示词几乎都在第一行就这样写：

- "用 Three.js 写一个**可直接打开的单文件 index.html**"（[@zmdsb259414][isaac]）
- "a first-person parkour run **in a single html file**"（[@thehypedotnews][parkour]）
- "使用svg画一个鹈鹕骑车的html。"（[@aizhibeibei][svg-pelican]）
- 单独做 SVG 时禁用脚本，这样放进 `<img>` 也能播放："Use **CSS or SMIL animation only, no JavaScript**. The animation loops seamlessly."（Lab [Pelican Test][pelican]）

## 2. 一句话的愿望也能撑起整部作品

V4.1 Flash 1017 能从很短的描述里补全大量细节，好几位作者只写一行就拿到了完整的游戏或场景：

- "build a call of duty 23 fps game use three js."（[@YifeiZhou][fps]）：作者报告用时 37 分钟、花费 $0.1，得到一个有五波敌人、三名干员和三档难度的游戏。
- "设计一个3D的东京塔的场景。"（[@vincent_ddup][tokyo]）：用时 27 分钟，花费 ¥1.5，没有返工。
- 开放式的描述在 Harness 里会跑很久。"尽你最大的能力…交付一个高水准的宣传视频"用了 18 分 34 秒、4,940 万 token（[@hiwise_aigc][whale-promo]）；让它为一段 15 秒的作品集短片"go all out"，用了约 6,800 万 token（[@aGim_asf][showreel]）。

短提示词得到的是模型的选择，不是你的，而且它不一定会纠正你的错误。[@UFO2002616][pelican-voxel] 把"鹈鹕"打成了"醍醐"，并说模型没有发现。写完先校对主体。

## 3. 写清每个操作和每条规则

列出每种操作以及它的作用，并给出游戏必须遵守的数字。这份列表里最长的公开提示词就是这样写的：

- "WASD 移动，方向键/鼠标射泪；每局随机生成 5–9 个连通房间…3 颗红心，清房开门"（[@zmdsb259414][isaac]）。后面还要求至少六个被动道具和一个两阶段 Boss。
- 游戏要写明按键："Space or swipe up = jump. Down arrow or swipe down = slide."（Lab [Endless Runner][runner]）

## 4. 把硬性约束放在前面

长输出的失败方式很固定：CDN 没加载、文件写到一半被截断、代码只能在服务器上跑。先把这些排除掉：

- "美术全部程序化…无外部素材"（[@zmdsb259414][isaac]）
- "Everything inline: no external files, fonts, images, libraries or CDNs. The file must work when opened from disk with no network connection."（Lab [Endless Runner][runner]）
- "Return ONLY the complete HTML code. No markdown fences, no explanation."（同上）
- 纹理用代码生成，声音用 Web Audio API 合成，不需要加载任何文件。（Lab [Watermelon Test][watermelon]）

作者们反复提到，效果最好的作品完全不用素材："all in code without any external assets, just Three.js"（[@ItsmeAjayKV][oneshot-3d]）。

## 5. 让它自己检查结果

[@MaxForAI][maxforai] 发现 1017 会主动跑很多冒烟测试和确认关卡。把这一点用起来，在提示词里写明要做什么测试：

- 以撒提示词的最后一句是"自动瞄准清图到通关的 Playwright 自测，最终零控制台错误"（[@zmdsb259414][isaac]）。
- [@thehypedotnews][parkour] 给四个 flash 模型同一份描述，并要求"four stages and one fix round"。

还要给它一个终点。[@teortaxesTex][turtle] 发现 1017 比之前的 V4.1 Flash 快得多，"up until it does 90% of the job"，之后它可能会"rabbithole into some oracle theater or microscopic polish"。一个必须通过的测试，就是自然的收尾点。

## 6. 给它一个参考

V4.1 Flash 能读图，一张参考图往往比一长段描述更管用：

- "添付画像を参考にBlenderで3Dモデルを作成して"（"参考附图，用 Blender 做一个 3D 模型"）（[@npaka123][blender-ref]）
- 用"one prompt + one reference image"复刻一个 3D 地球仪数据面板（[@aibuilderclub_][globe]）。作者说模型还自己加上了日间模式和夜间模式。
- [@GeekCatX][mower] 让它复刻另一位作者用 Opus 5.5 做的视频，报告结果非常接近。

## 7. 提前为录屏做准备

想最后得到视频，就在提示词里要求：

- 固定的镜头运动或自动播放的导览，不用鼠标也能播放。[@wikiwayne][tour] 用一条提示词拿到了"a 24-second Three.js tour"。东京塔那条帖子把"加一段自动巡游镜头"列为建议的下一步（[@vincent_ddup][tokyo]）。
- 时长确定的循环。[@GKev1n][svg-gkev] 让它写了一段原生 SVG 动画（车轮转动、脚踩在踏板上），再做成 11 秒的视频。
- 可检查的状态。Lab 的西瓜提示词要求页面设置 `document.body.dataset.bands` 和 `dataset.state = "burst"`，脚本据此知道精彩部分何时发生。

然后用 [`scripts/record.mjs`](../../scripts/record.mjs) 录制（见 [教程](tutorial.md#4-把页面录成视频)）。

## 可以直接套用的模板

```text
用一个独立的 HTML 文件做出 [主体]，要能直接从本地磁盘打开。

外观：[风格，如体素风 / 低多边形 / 电影感 PBR]，[氛围、光照、配色]。
运动：[哪些东西怎么动]。页面加载后自动播放 [10] 秒镜头导览，然后循环。
交互：[拖动 = …，滚轮 = …，点击 = …，按键 = …]。
规则：[必须遵守的数字：房间数、生命数、敌人波数、齿轮传动比、碰撞]。

技术要求：
- 通过 CDN import map 以 ES 模块方式引入 Three.js，不使用其他库。
- 不加载外部图片、模型、字体或音频：纹理用代码生成，声音用 Web Audio。
- 铺满视口，不出现滚动条，在笔记本上保持 60 fps。
- 完成之前，检查页面加载后控制台零错误，并且每个操作都能用。
- 只返回完整 HTML，从 <!DOCTYPE html> 到 </html>，不要省略任何部分。
```

可以在 [Lab 文本竞技场][arena] 里让 V4.1 Flash 1017 和其他模型并排运行，或按 [教程](tutorial.md) 用 API 调用。

## 参数设置

- **输出预算。** 模型先推理再回答，这些看不到的 token 也计入 `max_tokens`，并按输出计费。SandBase 自己测试时，`max_tokens: 300` 拿回的是空答案（[Python 教程][py]）。在 Lab Pelican Test 中，10 月 17 日的运行生成一张 SVG 用了 12,076 到 18,527 个 completion token（见 [模型对比](model-comparison.md#我们实测的lab-pelican-test)）；[@wikiwayne][seven] 报告七个游戏共用了 343,227 个输出 token，其中 250,426 个是推理。把 `max_tokens` 设为 32,000 以上（SandBase 最高接受 384,000）。
- **推理强度。** 公开了设置的创作者大多在 DeepSeek 的 Harness 里用 Max（[@marcthecreatorr][medieval]、[@zmdsb259414][isaac]、[@UFO2002616][pelican-voxel]）。[@UFO2002616][pelican-voxel] 也提醒 Max 要慎用，因为它会花很多力气反复折腾；[@GKev1n][svg-gkev] 先用 Max，最后改用 High 完成。通过 API 调用时，对应的参数是 `reasoning_effort`（[Python 教程][py]）。
- **一次生成还是多轮迭代。** 这里很多视频是一次生成。迭代成本更高，但可能值得：[@SahilPanhotra][peacock] 报告一次生成的孔雀花了 $0.53，加上递归循环后花了约 $1.50，腿和脚好了很多（[第二次运行][peacock-loop]）。

带工具调用、JSON 输出和推理控制、附 token 数和成本的实测代码，见 SandBase 博客的 [DeepSeek V4.1-Flash-1017 Python 实测](https://blog.sandbase.ai/zh-CN/deepseek-v4-1-flash-1017-api-python-tutorial-2026/?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=reading)。

---

引用均为简短摘录并注明作者，完整提示词和视频请点链接查看。英文和中文提示词保留原文，日文引用的中文译文由我们提供。

[isaac]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111477584924209246?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[parkour]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111472170190684243?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[svg-pelican]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111460614656913914?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[fps]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111410853522129220?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[tokyo]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111438861318418817?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[whale-promo]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111402753566310600?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[showreel]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111466670405599370?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[pelican-voxel]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111426130549117402?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[oneshot-3d]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111434381323907105?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[maxforai]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111440821484667343?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[turtle]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111394568725774765?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[blender-ref]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111454710498766979?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[globe]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111453908002562494?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[mower]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111487932515410366?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[tour]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111459465472176150?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[svg-gkev]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111392745155936690?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[seven]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111426732217532722?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[medieval]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111401362713968942?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[peacock]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111415760681849025?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[peacock-loop]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111454840337600839?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[pelican]: https://www.sandbase.ai/lab/pelican-test?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[runner]: https://www.sandbase.ai/lab/endless-runner?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[watermelon]: https://www.sandbase.ai/lab/watermelon-test?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=deepseek%2Fdeepseek-v4.1-flash&lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[py]: https://blog.sandbase.ai/zh-CN/deepseek-v4-1-flash-1017-api-python-tutorial-2026/?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=reading
