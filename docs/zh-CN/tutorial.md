# DeepSeek V4.1 Flash 1017 教程：从提示词到视频

[English](../tutorial.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

从提示词到 MP4，四步。V4.1 Flash 1017 写出网页，你负责播放和录制。

## 1. 从喜欢的视频开始

在 [合集](../../README.zh-CN.md) 里点任意标题，进入它在 [SandBase Lab][lab] 的页面：视频、原帖，以及作者公开的提示词（如果有）。点 **复刻**，Lab 会打开文本竞技场，自动填好帖子内容并选中 DeepSeek V4.1 Flash。登录后运行，就能拿到 HTML，并带实时预览。

作者没公开提示词？参考 [提示词写法](prompt-guide.md) 自己写一个，里面有可以直接填空的模板。

## 2. 同一提示词对比多个模型

在 [文本竞技场][arena] 里，在 V4.1 Flash 旁边再加一两个模型（例如 `anthropic/claude-opus-5.5`、`openai/gpt-6.1-sol` 或 `google/gemini-4-argon`），运行一次。每个模型拿到的提示词完全相同，每条结果都会显示成本和耗时。想在自己的任务上验证 [模型对比](model-comparison.md) 里的说法，这是最快的方式。

## 3. 或者调用 API

DeepSeek V4.1 Flash 1017 在 SandBase 上的模型 ID 是 `deepseek/deepseek-v4.1-flash`，兼容 OpenAI 接口。这个 ID 已于 2026 年 10 月 17 日切换到 1017 版本，所以不需要另选单独的 1017 ID（[这次更新改了什么][update]）。

1. 在 [控制台][keys] 创建 Key 并导出：`export SANDBASE_API_KEY=sk-sb-...`
2. 把提示词保存为 `prompt.txt`。
3. 运行：

```bash
jq -n --rawfile prompt prompt.txt '{
  model: "deepseek/deepseek-v4.1-flash",
  max_tokens: 32000,
  messages: [{role: "user", content: $prompt}]
}' |
curl -sS --max-time 900 https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- > response.json

jq -r '.choices[0].message.content' response.json | sed '/^```/d' > deepseek.html
jq '.usage' response.json
```

- `max_tokens: 32000`：模型会先推理再输出，隐藏的推理 token 也占用同一个额度。上限太低时，可能拿到空回答，token 却照样计费（[Python 教程][py]）。SandBase 最高支持 384,000。
- `--max-time 900`：生成一个长页面可能要几分钟。
- `sed '/^```/d'`：去掉模型可能加上的 Markdown 代码围栏。
- `usage`：本次计费的 token 数，包括 `completion_tokens_details.reasoning_tokens`。推理 token 按输出价格计费。价格见 [模型页][model]。
- 可选：加上 `reasoning_effort`，用思考深度换速度。[Python 教程][py] 实测了它的效果，并提到传入无效值会返回错误。

用浏览器打开 `deepseek.html`。如果是空白页，打开开发者控制台看报错：常见原因是文件被截断（调高 `max_tokens`），或 CDN 没加载上（在提示词里要求全部内联）。

### 使用 SandBase CLI

通过 [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli) 做同样的调用，它同样读取 `SANDBASE_API_KEY`：

```bash
npx -y @sandbaseai/cli@latest inspect deepseek/deepseek-v4.1-flash   # input fields and price, free
jq -n --rawfile prompt prompt.txt '{max_tokens: 32000, messages: [{role: "user", content: $prompt}]}' > input.json
npx -y @sandbaseai/cli@latest run sandbase_deepseek_deepseek_v4_1_flash -f input.json --timeout 900 -o result.json
```

`-o result.json` 会保存响应；页面内容和 API 调用一样，在 assistant 消息里。

## 4. 把页面录成视频

大多数作者是直接录屏。想每次得到一样的片段，可以用 [`scripts/record.mjs`](../../scripts/record.mjs) 无头录制：

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # 或使用本机已安装的 Chrome：export RECORD_CHANNEL=chrome
node scripts/record.mjs deepseek.html deepseek.mp4 12 1920 1080   # 录 12 秒，1080p
```

脚本按指定尺寸打开页面，录制指定秒数，再用 ffmpeg 转成 H.264 MP4。想要干净的画面，就在提示词里要求自动播放的镜头导览或固定时长的循环（见 [提示词写法第 7 节](prompt-guide.md#7-提前为录屏做准备)），不依赖鼠标操作。

想加声音？录制结果只有画面，音频要在剪辑时加。这里有几位作者提到，模型直接把背景音乐写进了页面里（[@hqmank][browser-skill]、[@UFO2002616][pelican-voxel]）。

这个列表里的不少视频是在 DeepSeek 自家的 Harness 里做的，而不是单次 API 调用；作者反馈 Harness 一次运行约 15 到 37 分钟（[@GKev1n][svg-gkev]、[@UFO2002616][pelican-voxel]），模型还能操作 Blender（[@Yunn260414][coaster]）。配置方法见 [DeepSeek V4.1 Flash API：预览访问与 Harness 配置](https://blog.sandbase.ai/zh-CN/deepseek-v4-1-flash-api-harness-preview-2026/?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=reading)。完整的 Python 教程（流式、工具调用、JSON 输出）见 [DeepSeek V4.1-Flash-1017 Python 调用教程][py]。

## 安全运行生成的代码

这些 HTML 是你没读过的代码。单文件页面从本地打开通常没问题，但它仍然可以加载脚本、发起网络请求。对不信任的代码，或者需要批量自动运行时，请使用 [SandBase Sandbox][sandbox]：隔离的运行环境，有时间限制，无法访问你的文件和密钥。

## 分享

把视频连同提示词发到 X，并注明 DeepSeek V4.1 Flash 1017。想收录到这里，请 [提交作品](https://github.com/sandbase-lab/awesome-deepseek-v4.1-flash-1017/issues/new?template=submit-video.yml)；通过审核的作品会加入 Lab 合集，并在下一次每日同步时出现在本列表。

[lab]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=deepseek%2Fdeepseek-v4.1-flash&lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[model]: https://www.sandbase.ai/model/deepseek/deepseek-v4.1-flash?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[update]: https://blog.sandbase.ai/zh-CN/deepseek-v4-1-flash-1017-update-2026/?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=reading
[py]: https://blog.sandbase.ai/zh-CN/deepseek-v4-1-flash-1017-api-python-tutorial-2026/?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=reading
[browser-skill]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111470277309997492?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[pelican-voxel]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111426130549117402?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[coaster]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111450021849944508?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[svg-gkev]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111392745155936690?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
