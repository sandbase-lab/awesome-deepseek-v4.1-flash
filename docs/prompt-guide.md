# DeepSeek V4.1 Flash 1017 prompt guide: how to prompt V4.1 Flash for video

English · [简体中文](zh-CN/prompt-guide.md) · [← Back to the collection](../README.md)

DeepSeek V4.1 Flash 1017 doesn't output video. It writes code (an HTML page with Three.js, Canvas or SVG), and the creator records that page playing. In DeepSeek's Harness it can also drive Blender. The patterns below come from prompts creators posted with their videos and from the fixed prompts SandBase Lab uses to test models. Each example links to the video it produced.

## 1. Say what file you want

Name the format and where it runs. The shared prompts that worked nearly all do this in the first line:

- "用 Three.js 写一个**可直接打开的单文件 index.html**" ("write a **single-file index.html that opens directly**, using Three.js") ([@zmdsb259414][isaac], translated)
- "a first-person parkour run **in a single html file**" ([@thehypedotnews][parkour])
- "使用svg画一个鹈鹕骑车的html。" ("draw a pelican riding a bicycle in SVG, as an HTML page") ([@aizhibeibei][svg-pelican])
- For SVG on its own, ban scripts so it plays inside an `<img>`: "Use **CSS or SMIL animation only, no JavaScript**. The animation loops seamlessly." (Lab [Pelican Test][pelican])

## 2. A one-line wish can carry a whole piece

V4.1 Flash 1017 fills in a lot from a short brief, and several creators got a full game or scene from one line:

- "build a call of duty 23 fps game use three js." ([@YifeiZhou][fps]): the creator reports 37 minutes, $0.1, and a game with five waves, three operators and three difficulty levels.
- "设计一个3D的东京塔的场景。" ("design a 3D Tokyo Tower scene") ([@vincent_ddup][tokyo], translated): 27 minutes, ¥1.5, no revisions.
- Open briefs run long in a harness. "尽你最大的能力…交付一个高水准的宣传视频" ("do your best… deliver a high-quality promo video") took 18m34s and 49.4M tokens ([@hiwise_aigc][whale-promo], translated); "go all out" on a 15-second showreel used about 68M tokens ([@aGim_asf][showreel]).

Short prompts give you the model's choices, not yours, and it doesn't always fix your mistakes. [@UFO2002616][pelican-voxel] typed 醍醐 instead of 鹈鹕 (pelican) and says the model didn't catch it. Proofread the subject.

## 3. Spell out every input and rule

Name each control and what it does, and give the numbers the game has to respect. The longest shared prompt in this list does exactly that:

- "WASD 移动，方向键/鼠标射泪；每局随机生成 5–9 个连通房间…3 颗红心，清房开门" ("WASD to move, arrow keys or mouse to shoot; each run generates 5–9 connected rooms… 3 hearts, clearing a room opens the doors") ([@zmdsb259414][isaac], translated). It goes on to ask for at least six passive items and a two-phase boss.
- Games: list the keys. "Space or swipe up = jump. Down arrow or swipe down = slide." (Lab [Endless Runner][runner])

## 4. Set hard constraints up front

Long outputs fail in predictable ways: a missing CDN, a file cut off halfway, code that only runs on a server. Rule those out first:

- "美术全部程序化…无外部素材" ("all art procedural… no external assets") ([@zmdsb259414][isaac], translated)
- "Everything inline: no external files, fonts, images, libraries or CDNs. The file must work when opened from disk with no network connection." (Lab [Endless Runner][runner])
- "Return ONLY the complete HTML code. No markdown fences, no explanation." (same)
- Build textures in code and sounds with the Web Audio API, so there is nothing to load. (Lab [Watermelon Test][watermelon])

Creators keep pointing out that their best results used no assets at all: "all in code without any external assets, just Three.js" ([@ItsmeAjayKV][oneshot-3d]).

## 5. Ask it to check its own work

[@MaxForAI][maxforai] noticed 1017 running many smoke tests and confirmation gates on its own (translated). Put that to use by naming the test:

- The Isaac prompt ends with "自动瞄准清图到通关的 Playwright 自测，最终零控制台错误" ("a Playwright self-test that auto-aims and clears the map through to the win, ending with zero console errors") ([@zmdsb259414][isaac], translated).
- [@thehypedotnews][parkour] gave four flash models the same brief with "four stages and one fix round".

Also give it a finish line. [@teortaxesTex][turtle] found 1017 much faster than the previous V4.1 Flash "up until it does 90% of the job", after which it can "rabbithole into some oracle theater or microscopic polish". A test that must pass is a natural place to stop.

## 6. Show it a reference

V4.1 Flash reads images, and a reference often beats a long description:

- "添付画像を参考にBlenderで3Dモデルを作成して" ("use the attached image as a reference and make a 3D model in Blender") ([@npaka123][blender-ref], translated)
- "one prompt + one reference image" to rebuild a 3D globe dashboard ([@aibuilderclub_][globe]). The creator says the model also added a day mode and a night mode on its own.
- [@GeekCatX][mower] gave it another creator's Opus 5.5 video to recreate and reports a closely matching result (translated).

## 7. Plan for the recording

If you want a video at the end, ask for it:

- A fixed camera move or an autoplay tour, so the page plays without a mouse. [@wikiwayne][tour] got "a 24-second Three.js tour" from one prompt. The Tokyo Tower post lists "加一段自动巡游镜头" ("add an automatic fly-through camera") as a suggested next step ([@vincent_ddup][tokyo], translated).
- A loop of known length. [@GKev1n][svg-gkev] had it write a native SVG animation (wheels turning, feet on the pedals) and turned that into an 11-second video.
- State you can check. Lab's watermelon prompt makes the page set `document.body.dataset.bands` and `dataset.state = "burst"`, so a script knows when the interesting part happens.

Then record it with [`scripts/record.mjs`](../scripts/record.mjs) (see the [tutorial](tutorial.md#4-turn-the-page-into-a-video)).

## A prompt to start from

```text
Build [subject] as ONE self-contained HTML file that opens directly from disk.

Look: [style, e.g. voxel art / low-poly / cinematic PBR], [mood, lighting, palette].
Motion: [what moves and how]. Autoplay a [10]-second camera tour on load, then loop.
Interaction: [drag = …, scroll = …, click = …, keys = …].
Rules: [the numbers it must respect: rooms, lives, waves, gear ratios, collisions].

Technical:
- Use Three.js as an ES module from a CDN import map. No other libraries.
- No external images, models, fonts or audio: generate textures in code, sound with Web Audio.
- Fill the viewport, no scrolling, 60 fps on a laptop.
- Before you finish, check that the page loads with zero console errors and that every control works.
- Return only the complete HTML, from <!DOCTYPE html> to </html>. Do not abbreviate.
```

Try it on the [Lab text arena][arena] to run it on V4.1 Flash 1017 and other models side by side, or with the API in the [tutorial](tutorial.md).

## Settings

- **Output budget.** The model reasons before it answers, and those hidden tokens count toward `max_tokens` and bill as output. SandBase's own test got an empty answer at `max_tokens: 300` ([Python tutorial][py]). On the Lab Pelican Test, runs on October 17 used 12,076 to 18,527 completion tokens for one SVG ([comparison](model-comparison.md#what-we-measured-lab-pelican-test)); [@wikiwayne][seven] reports 343,227 output tokens for seven games, 250,426 of them reasoning. Set `max_tokens` to 32,000 or more (SandBase accepts up to 384,000).
- **Reasoning.** Creators who state a setting mostly used Max in DeepSeek's Harness ([@marcthecreatorr][medieval], [@zmdsb259414][isaac], [@UFO2002616][pelican-voxel]). [@UFO2002616][pelican-voxel] also warns to use Max with care because it spends a lot of effort going back and forth (translated); [@GKev1n][svg-gkev] started on Max and finished on High. Over the API the knob is `reasoning_effort` ([Python tutorial][py]).
- **One shot vs. iteration.** Many videos here are one shot. Iterating costs more and can pay off: [@SahilPanhotra][peacock] reports $0.53 for a one-shot peacock, then about $1.50 with a recursive loop and much better legs and feet ([second run][peacock-loop]).

For tested code with tools, JSON output and reasoning control, with token counts and cost, see [DeepSeek V4.1-Flash-1017 in Python](https://blog.sandbase.ai/deepseek-v4-1-flash-1017-api-python-tutorial-2026/?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=reading) on the SandBase blog.

---

Quotes are short excerpts credited to their authors; follow the links for full prompts and videos. Translations from Chinese and Japanese are ours.

[isaac]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111477584924209246?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[parkour]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111472170190684243?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[svg-pelican]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111460614656913914?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[fps]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111410853522129220?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[tokyo]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111438861318418817?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[whale-promo]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111402753566310600?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[showreel]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111466670405599370?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[pelican-voxel]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111426130549117402?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[oneshot-3d]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111434381323907105?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[maxforai]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111440821484667343?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[turtle]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111394568725774765?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[blender-ref]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111454710498766979?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[globe]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111453908002562494?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[mower]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111487932515410366?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[tour]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111459465472176150?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[svg-gkev]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111392745155936690?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[seven]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111426732217532722?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[medieval]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111401362713968942?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[peacock]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111415760681849025?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[peacock-loop]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111454840337600839?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[pelican]: https://www.sandbase.ai/lab/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[runner]: https://www.sandbase.ai/lab/endless-runner?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[watermelon]: https://www.sandbase.ai/lab/watermelon-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=deepseek%2Fdeepseek-v4.1-flash&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[py]: https://blog.sandbase.ai/deepseek-v4-1-flash-1017-api-python-tutorial-2026/?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=reading
