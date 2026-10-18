# DeepSeek V4.1 Flash 1017 对比 Claude Opus 5.5、GPT-6 和 Gemini 4 Argon

[English](../model-comparison.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

两类证据，分开呈现：

1. **我们实测的。** Lab [Evals 榜单][evals] 展示 Artificial Analysis 的数据；Lab [Pelican Test][pelican] 对每个模型使用同一个固定提示词并打分。样本小，但所有模型条件相同。
2. **创作者报告的。** 创作者在 X 上发布的同提示词对比，提示词、成本和耗时都是他们自己的。可作参考，我们没有核实。

DeepSeek-V4.1-Flash-1017 于 2026 年 10 月 17 日以同一个名称替换了 9 月版 V4.1 Flash（[这次更新改了什么][update]）。标注为 "DeepSeek V4.1 Flash" 的分数，只有在这一天或之后测得，才能代表 1017，所以下面每一节都会说明它对应的是哪个版本。

## 我们实测的：Lab Evals 榜单

以下为 2026-10-17 Lab 榜单上的数据（快照抓取于 17:33 UTC）。数据来源：[Artificial Analysis][aa]。排名按该榜单的全部行计算。

| 模型（榜单上的行） | [智能指数][b-intel] | [输出速度][b-speed] | [单任务成本][b-cost] |
|---|---|---|---|
| Claude Opus 5.5 (Max, Default Fallback) | 57.6（694 行中第 1） | 97 tok/s（373 行中第 181） | $5.98（189 行中第 187） |
| GPT-6 Astra (Max) | 52.7（第 8） | 57 tok/s（第 280） | $3.26（第 173） |
| Gemini 4 Argon (High) | 52.6（第 9） | 不在榜单上 | $1.99（第 157） |
| GPT-6.1 Sol (Max) | 51.8（第 13） | 66 tok/s（第 257） | $0.724（第 112） |
| **DeepSeek V4.1 Flash (Max)** | **39.5（第 67）** | **180 tok/s（第 62）** | **$0.265（第 74）** |
| GPT-6 Luna (Max) | 38.1（第 77） | 121 tok/s（第 133） | $0.068（第 35） |
| DeepSeek V4.1 Flash (Non-reasoning) | 24.7（第 172） | 171 tok/s（第 70） | $0.147（第 58） |

能说明什么，不能说明什么：

- **这些多半还不是 1017 的数字。** 两行 DeepSeek 的智能指数和单任务成本都与上一期快照相同，而上一期快照日期是 2026-10-14，比 1017 发布早三天。在 Artificial Analysis 重新测量之前，应把它们看作 9 月版的数据。
- **比前沿模型便宜、更快，但智能指数差得多。** 按这几行数据，V4.1 Flash 的单任务成本约为 Opus 5.5 的二十分之一，速度接近两倍，但智能指数比 Opus 5.5、GPT-6 Astra、Gemini 4 Argon 和 GPT-6.1 Sol 低 12 到 18 分。
- **没有编程或 Agent 榜单的行。** DeepSeek V4.1 Flash、Opus 5.5、Argon、GPT-6.1 Sol 和 GPT-6 Luna 在 [编程][b-coding] 和 [Agent][b-agentic] 榜单上都没有对应的行，只有 GPT-6 Astra 有。而 DeepSeek 自己公布的 1017 基准里，变化最大的正是这两类（见 [更多实测](#更多实测)）。

## 我们实测的：Lab Pelican Test

[Pelican Test][pelican] 让每个模型画一张"鹈鹕骑自行车"的 SVG，静态一次、动画一次（轮子转、腿踩踏板，只能用 CSS/SMIL）。页面渲染成 PNG 后，由 `google/gemini-3.8-flash` 按四项打 0 到 5 分：认得出、真的在骑、车结构合理、好看。成本是 SandBase 上的实际扣费。

以下为本页涉及模型在 2026-10-18 [实时榜单][pelican] 上的行（共 20 个模型、102 条结果）：

| 排名 | 模型 | 结果数 | 得分 | 能渲染 | 动画真的在动 | 平均成本 |
|---|---|---|---|---|---|---|
| 1 | openai/gpt-6.1-sol | 6 | 3.79 | 100% | 100% | $0.026 |
| 2 | google/gemini-4-argon | 4 | 3.75 | 100% | 100% | $0.150 |
| 4 | anthropic/claude-opus-5.5 | 6 | 3.42 | 100% | 100% | $0.223 |
| 5 | **deepseek/deepseek-v4.1-flash** | 6 | **3.29** | 100% | 100% | $0.017 |
| 6 | openai/gpt-6-luna | 2 | 3.25 | 100% | 100% | $0.006 |
| 8 | openai/gpt-6-astra | 6 | 3.08 | 83% | 67% | $0.102 |

DeepSeek 这一行混合了 2026-10-06（9 月版）和 2026-10-17 的运行，因此不是 1017 的分数。2026-10-17 的结果都晚于当天早上 X 上第一批 1017 帖子（07:13 UTC）。以下是 1017 版本的 [打分结果][pelican-ds]：

| 时间（UTC） | 类型 | 得分 | 认得出 / 在骑 / 车 / 好看 | 输出 token | 耗时 | 成本 | 评委点评 |
|---|---|---|---|---|---|---|---|
| 09:14 | 静态 | 3.25 | 4 / 3 / 3 / 3 | 12,076 | 67 秒 | $0.016 | "This snappy pelican pedals smoothly into the wind, though its bike could use a proper saddle." |
| 09:14 | 动画 | 3.25 | 4 / 3 / 3 / 3 | 15,272 | 81 秒 | $0.017 | "…the bird is coasting without any legs." |
| 11:25 | 静态 | 3.25 | 4 / 3 / 3 / 3 | 14,419 | 75 秒 | $0.017 | "…it is missing a saddle to sit on and wings on the handlebars." |
| 11:29 | 静态 | 3.5 | 4 / 3 / 3 / 4 | 14,350 | 70 秒 | $0.017 | "A stylish pelican catches a ride, though it seems to have forgotten its bike saddle." |
| 12:33 | 动画 | 3.5 | 4 / 3 / 3 / 4 | 17,530 | 87 秒 | — | "…it's gliding on the handlebars rather than pedaling." |
| 13:06 | 动画 | 3.0 | 4 / 2 / 3 / 3 | 15,805 | 81 秒 | — | "…it mostly hovers above the bike rather than pedaling it." |
| 13:28 | 动画 | 3.5 | 4 / 3 / 3 / 4 | 18,527 | 92 秒 | $0.020 | "…the bicycle frame geometry is slightly distorted." |

当天另有五次动画运行以 "failed" 状态结束，没有得分。

结论：

- **每次都认得出，但从没真正骑起来。** 七张图在"认得出"上都是 4 分，"在骑"和"车"都没有超过 3 分。评委点评反复提到没画车座，鹈鹕在滑行或悬空，而不是在踩踏板。
- **质量中游，价格很低。** 七条 1017 结果平均 3.32 分，与上面混合版本的榜单行接近，每张约 2 美分：大约是 Opus 5.5 或 Argon 平均成本的十分之一，也低于得分更高的 GPT-6.1 Sol。
- **很费 token。** 每张 SVG 输出中位数 15,272 个 token，中位耗时 81 秒。
- **样本量。** 只有一天内的七条打分结果。欢迎 [自己跑一次][pelican-run] 补充结果。

Lab 其他代码测试还没有 1017 的结果：[Endless Runner][runner]（Canvas 游戏）没有 V4.1 Flash 的结果，V4.1 Flash 在 [Watermelon Test][watermelon] 上的最好结果来自 2026-10-12，早于 1017。

## 创作者报告的结果

以下是创作者在 X 上发布的同提示词对比。数字均按作者原话：使用的工具不同（DeepSeek Harness、API、OpenRouter、转售平台），推理设置不同，有高峰和低谷时段价格，通常只跑了一次。点击链接可以观看两边的结果。

| 作者 | 任务 | V4.1 Flash 1017 | 对比模型 | 作者结论 |
|---|---|---|---|---|
| [@marcthecreatorr][marc-opus] | 同一提示词 | 约 1 小时，$0.23 | Opus 5.5：20 分钟，约 $6 | Opus 在动画、音效和细节上更好；DeepSeek "pretty close"，有几处错误 |
| [@ItsWonda_][wonda] | 与上一行相同的测试 | 1 小时，$0.23 | Opus 5.5：20 分钟，$6 | Opus 在打磨和操控上胜出；DeepSeek 很接近，"for 26x less" |
| [@wquguru][gummy] | 可以抓、拉、扔的软糖熊 | 约 $0.32（低谷时段），54 分钟 | Opus 5.5 + Fable 5.1 作顾问：约 $7.8（API 标价），61 分钟 | 静止时不相上下；一碰之后 DeepSeek 的熊会撕裂，眼睛会漂移 |
| [@aGim_asf][showreel] | 15 秒动效 showreel | 约 6800 万 token | Opus 5.5：26 分钟，$5.75 | "Opus cooked"，DeepSeek "a lot cheaper" |
| [@kepochnik][fnaf] | 《Five Nights at Freddy's》游戏 | 24 分钟 | Opus 5.5：38 分钟 | 让观众评判 |
| [@Bhavani_00007][rocket] | 火箭发射场景 | $0.78，3 分钟 | GPT-6.1 Sol：$6.10，5 分钟 | DeepSeek "absolutely cooked" |
| [@SPAC89][sol] | 同一测试，Max 对比 Sol Ultra | API 成本 "0.44 cents" | GPT-6.1 Sol Ultra：耗时差不多 | 就这个价格而言，DeepSeek 的质量 "incredible" |
| [@thehypedotnews][parkour] | 第一人称跑酷，单 HTML，四个 flash 模型 | $0.141，1 小时 27 分 | Claude Haiku 5.5：$0.08，23 分 33 秒 · GPT-6 Luna：$0.036，8 分 07 秒 · Qwen3.8 Flash：$0.227，2 小时 04 分 | DeepSeek 的特效 "the best effects of the four" |
| [@atomic_chat_hq][roadster] | 3D 体素风 Tesla Roadster 发布会 | $0.89 | GPT-6 Luna：$1.07 | — |
| [@VulKan42069][vpelican] | 体素鹈鹕，两边都用 Max | — | GPT-6 Luna | — |
| [@Bhavani_00007][whale] | 鲸鱼跃出水面测试 | 一次生成的结果 "blown out"；之后限额 $2.50 | Kimi K3：$2.50，一次生成 | Kimi 更好；DeepSeek "not on par with Opus 5 or Kimi in frontend and 3D" |
| [@wikiwayne][seven] | 同样的 7 个游戏提示词 | 9 分 30 秒，$0.21，343,227 输出 token | Gemini 4 Argon：$1.34 · Beam：免费，3 分 45 秒 | 7 个都能正常加载；价格上 "crushed Argon" |

没有并排视频的评价：[@GeekCatX][mower] 认为它的 3D 作品达到 Opus 5.5 的水平，与 Gemini 4 Argon 相当，但更慢；[@aibuilderclub_][globe] 认为它在审美和细节上与 Opus 5.5 相当；[@YifeiZhou][fps] 说它 "seems the same level as Gemini 4 and better than Chatgpt 6.1 sol"；[@UFO2002616][pelican-voxel] 指出 Gemini 4 和 GPT-6 Astra 发现了提示词里的一个错别字，DeepSeek 没有发现。

与 9 月版 V4.1 Flash 在同一提示词下的对比：

- [@NFT_Chen][rain-1]、[@karanC_12][rain-2] 和 [@AndyL5cc][rain-3] 展示了同一个雨夜便利店场景，左边是旧版本，右边是 1017，光线、氛围和细节明显更好。
- [@leo114119][old-3d] 认为 1017 的 Three.js 建模比旧版本强得多。
- [@teortaxesTex][turtle] 在同一个海龟提示词上发现 1017 "massively faster"，"but only up until it does 90% of the job"；之后 "you've got to handhold it"。

只跑 1017 并报告了成本的作品：

| 作者 | 任务 | 报告数据 |
|---|---|---|
| [@wikiwayne][tour] | 24 秒 Three.js 导览，一个提示词 | 194.2 秒，$0.0334（API 报告） |
| [@alohaproxy][robo] | 机器人组装与发射测试，Three.js | $0.04 |
| [@YifeiZhou][fps] | 一句话生成 FPS 游戏 | 37 分钟，$0.1 |
| [@hqmank][browser-skill] | 为一个开源项目做的动效视频 | $0.25 |
| [@SahilPanhotra][peacock] | 孔雀测试：先一次生成，再用递归循环 | $0.53，之后约 $1.50（[第二次运行][peacock-loop]） |
| [@notjazii][frieren] | 带背景音乐的 SVG 绘图 | 1 小时 15 分，6570 万 token，$0.70 |
| [@vincent_ddup][tokyo] | 3D 东京塔场景 | 27 分钟，¥1.5，没有返工 |
| [@GKev1n][svg-gkev] | 在 Harness 中由 Codex 驱动画 SVG 鹈鹕 | 15 分 47 秒，约 287 万 token（缓存命中 92%），1 元多一点 |
| [@hiwise_aigc][whale-promo] | 在 Harness 中做鲸鱼宣传视频 | 18 分 34 秒，247 tok/s，4940 万 token（缓存命中 99%），¥2.17 |
| [@UFO2002616][pelican-voxel] | 骑独轮车的体素鹈鹕，Max | 37 分钟，¥2.7 |
| [@marcthecreatorr][medieval] | 中世纪体素世界，超过 200 万个体素，max 推理 | 约 25 分钟，约 $5 |

两类数据呈现的规律：V4.1 Flash 1017 一次生成一个页面只要几美分，较长的 Harness 运行从 1 美元左右到 $5 不等。与 Opus 5.5 相比，创作者大多仍更喜欢 Opus 的打磨程度，但要多付约 24 到 26 倍的费用，而且 DeepSeek 也并不总是更快。与 GPT-6.1 Sol 和 GPT-6 Luna 相比，更多创作者更喜欢 DeepSeek 的结果。

## 相信对比之前，先自己跑一遍

结果受配置影响很大。[@Bhavani_00007][whale] 一次生成的鲸鱼 "completely blown out"，之后才做了第二次限额运行；[@SahilPanhotra][peacock-loop] 加了一个递归循环、在提示词里多加一个词，孔雀就好了很多；[@YxzRainy][four-demos] 和 [@AndyL5cc][four-demos-2] 追问 DeepSeek 官方展示的演示跑了多久、用了几轮，普通用户能不能复现。请自己跑一遍：把提示词贴进 [Lab 文本竞技场][arena]，同时选两三个模型，或参考 [教程](tutorial.md)。

## 更多实测

- [DeepSeek V4.1-Flash-1017：10 月更新改了什么](https://blog.sandbase.ai/zh-CN/deepseek-v4-1-flash-1017-update-2026/?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=reading)：DeepSeek 官方基准表，把 1017 与 9 月版、Claude Opus 5、GPT-5.6 Sol、Kimi K3 和 GLM-5.3 对比（厂商自报，不含 Opus 5.5、GPT-6 或 Argon）。
- [DeepSeek V4.1 Flash 对比 V4 Pro：价格、视觉能力与 Pro 的现状](https://blog.sandbase.ai/zh-CN/deepseek-v4-1-flash-vs-v4-flash-pro-2026/?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=reading)。
- Gemini 4 Argon 的同类合集：[awesome-gemini4-argon](https://github.com/sandbase-lab/awesome-gemini4-argon)。

---

Lab 数据：[Evals 榜单][evals]（Artificial Analysis，2026-10-17 快照）和 [Pelican Test][pelican]（2026-10-18 快照）。创作者数据：见各自帖子链接，未经独立核实。

[evals]: https://www.sandbase.ai/lab/evals?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[b-intel]: https://www.sandbase.ai/lab/evals/llm-intelligence?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[b-coding]: https://www.sandbase.ai/lab/evals/llm-coding?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[b-agentic]: https://www.sandbase.ai/lab/evals/llm-agentic?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[b-speed]: https://www.sandbase.ai/lab/evals/llm-speed?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[b-cost]: https://www.sandbase.ai/lab/evals/llm-cost?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[aa]: https://artificialanalysis.ai/
[update]: https://blog.sandbase.ai/zh-CN/deepseek-v4-1-flash-1017-update-2026/?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=reading
[pelican]: https://www.sandbase.ai/lab/pelican-test?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[pelican-ds]: https://www.sandbase.ai/lab/pelican-test/m/deepseek--deepseek-v4.1-flash?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[pelican-run]: https://www.sandbase.ai/lab/pelican-test?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=run
[runner]: https://www.sandbase.ai/lab/endless-runner?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[watermelon]: https://www.sandbase.ai/lab/watermelon-test?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=deepseek%2Fdeepseek-v4.1-flash&lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[marc-opus]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111427716142571554?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[wonda]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111440074831536446?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[gummy]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111440154078703961?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[showreel]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111466670405599370?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[fnaf]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111421758691827905?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[rocket]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111501438564331534?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[sol]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111413922989224089?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[parkour]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111472170190684243?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[roadster]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111474429410566422?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[vpelican]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111476518694384061?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[whale]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111417280366031318?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[seven]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111426732217532722?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[mower]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111487932515410366?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[globe]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111453908002562494?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[fps]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111410853522129220?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[pelican-voxel]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111426130549117402?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[rain-1]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111354975213519082?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[rain-2]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111371468399689740?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[rain-3]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111397507674857813?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[old-3d]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111466664613269898?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[turtle]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111394568725774765?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[tour]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111459465472176150?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[robo]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111466763959271873?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[browser-skill]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111470277309997492?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[peacock]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111415760681849025?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[peacock-loop]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111454840337600839?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[frieren]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111476965429645706?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[tokyo]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111438861318418817?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[svg-gkev]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111392745155936690?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[whale-promo]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111402753566310600?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[medieval]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111401362713968942?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[four-demos]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111388754573398252?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[four-demos-2]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111395155505033338?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
