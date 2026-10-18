# DeepSeek V4.1 Flash 1017 tutorial: from prompt to video

English · [简体中文](zh-CN/tutorial.md) · [← Back to the collection](../README.md)

From a prompt to an MP4 in four steps. V4.1 Flash 1017 writes a web page; you play it and record it.

## 1. Start from a video you like

Open any title in the [collection](../README.md) to reach its page on [SandBase Lab][lab]: the video, the original post and, when the creator shared one, the prompt. Press **Recreate**. Lab opens the text arena with the post loaded and DeepSeek V4.1 Flash selected. Sign in, run it, and you get the HTML back, with a live preview.

No prompt shared? Write one with the [prompt guide](prompt-guide.md). It has a fill-in template.

## 2. Compare models on the same prompt

In the [text arena][arena], add one or two more models next to V4.1 Flash (for example `anthropic/claude-opus-5.5`, `openai/gpt-6.1-sol` or `google/gemini-4-argon`) and run once. Every model gets the same words, and each result shows its cost and time. That's the quickest way to check a claim from the [comparison page](model-comparison.md) on your own task.

## 3. Or call the API

DeepSeek V4.1 Flash 1017 is `deepseek/deepseek-v4.1-flash` on SandBase, OpenAI-compatible. The id moved to the 1017 checkpoint on October 17, 2026, so there is no separate 1017 id to pick ([what the update changes][update]).

1. Create a key in the [console][keys] and export it: `export SANDBASE_API_KEY=sk-sb-...`
2. Save your prompt as `prompt.txt`.
3. Run:

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

- `max_tokens: 32000`: the model reasons before it writes, and the hidden reasoning tokens come out of the same budget. With a low limit you can get an empty answer and still pay for the tokens ([Python tutorial][py]). SandBase accepts up to 384,000.
- `--max-time 900`: one long page can take several minutes.
- `sed '/^```/d'` removes Markdown fences if the model added them.
- `usage` shows the tokens you were billed for, including `completion_tokens_details.reasoning_tokens`. Reasoning bills at the output rate. Prices are on the [model page][model].
- Optional: add `reasoning_effort` to trade thinking for speed. The [Python tutorial][py] measured its effect and notes that an invalid value returns an error.

Open `deepseek.html` in a browser. If it's blank, open the developer console: the usual causes are a truncated file (raise `max_tokens`) or a CDN that didn't load (ask for everything inline).

### With the SandBase CLI

The same call through the [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli), which reads `SANDBASE_API_KEY` as well:

```bash
npx -y @sandbaseai/cli@latest inspect deepseek/deepseek-v4.1-flash   # input fields and price, free
jq -n --rawfile prompt prompt.txt '{max_tokens: 32000, messages: [{role: "user", content: $prompt}]}' > input.json
npx -y @sandbaseai/cli@latest run sandbase_deepseek_deepseek_v4_1_flash -f input.json --timeout 900 -o result.json
```

`-o result.json` saves the response; the page is in the assistant message, as with the API.

## 4. Turn the page into a video

Most creators screen-record the page. To get the same clip every time, record it headlessly with [`scripts/record.mjs`](../scripts/record.mjs):

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # or use your installed Chrome: export RECORD_CHANNEL=chrome
node scripts/record.mjs deepseek.html deepseek.mp4 12 1920 1080   # 12 seconds at 1080p
```

It opens the page at the size you give, records for that many seconds, and converts to H.264 MP4 with ffmpeg. For a clean result, ask in the prompt for an autoplay camera tour or a fixed-length loop (see [prompt guide §7](prompt-guide.md#7-plan-for-the-recording)), so nothing depends on a mouse.

Want sound? The recording is picture only, so add audio in the edit. Several creators here say the model wrote background music into the page itself ([@hqmank][browser-skill], [@UFO2002616][pelican-voxel]).

Many videos in this list were made in DeepSeek's own Harness rather than with a single API call; creators report harness runs of about 15 to 37 minutes ([@GKev1n][svg-gkev], [@UFO2002616][pelican-voxel]), and the model can drive Blender ([@Yunn260414][coaster]). For setup, see [DeepSeek V4.1 Flash API: preview access and Harness setup](https://blog.sandbase.ai/deepseek-v4-1-flash-api-harness-preview-2026/?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=reading). For a full Python walkthrough with streaming, tool calls and JSON output, see [DeepSeek V4.1-Flash-1017 in Python][py].

## Run generated code safely

The HTML is code you haven't read. Opening it from disk is usually fine for a single-file page, but it can still load scripts and make network requests. For anything you don't trust, or to run many pages automatically, use a [SandBase Sandbox][sandbox]: an isolated environment with a time limit and no access to your files or keys.

## Share it

Post your video on X with the prompt and mention DeepSeek V4.1 Flash 1017. To have it added here, [submit it](https://github.com/sandbase-lab/awesome-deepseek-v4.1-flash-1017/issues/new?template=submit-video.yml); accepted posts go into the Lab collection and show up in this list on the next daily sync.

[lab]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=deepseek%2Fdeepseek-v4.1-flash&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[model]: https://www.sandbase.ai/model/deepseek/deepseek-v4.1-flash?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[update]: https://blog.sandbase.ai/deepseek-v4-1-flash-1017-update-2026/?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=reading
[py]: https://blog.sandbase.ai/deepseek-v4-1-flash-1017-api-python-tutorial-2026/?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=reading
[browser-skill]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111470277309997492?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[pelican-voxel]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111426130549117402?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[coaster]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111450021849944508?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[svg-gkev]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111392745155936690?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
