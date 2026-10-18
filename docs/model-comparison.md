# DeepSeek V4.1 Flash 1017 vs Claude Opus 5.5, GPT-6 and Gemini 4 Argon

English · [简体中文](zh-CN/model-comparison.md) · [← Back to the collection](../README.md)

Two kinds of evidence, kept apart:

1. **What we measured.** The Lab [Evals boards][evals] show Artificial Analysis data, and the Lab [Pelican Test][pelican] runs the same fixed prompt on every model and scores the result. Small samples, but the same conditions for everyone.
2. **What creators reported.** Head-to-heads posted on X with their own prompts, costs and times. Useful context, not verified by us.

DeepSeek-V4.1-Flash-1017 replaced the September V4.1 Flash under the same name on October 17, 2026 ([what the update changes][update]). A score labelled "DeepSeek V4.1 Flash" is only about 1017 if it was measured on or after that date, so each section below says which build it can speak for.

## What we measured: Lab Evals boards

Rows from the Lab boards on 2026-10-17 (snapshot fetched 17:33 UTC). Data: [Artificial Analysis][aa]. Rank is out of every row on that board.

| Model (row on the board) | [Intelligence Index][b-intel] | [Output speed][b-speed] | [Cost per task][b-cost] |
|---|---|---|---|
| Claude Opus 5.5 (Max, Default Fallback) | 57.6 (#1 of 694) | 97 tok/s (#181 of 373) | $5.98 (#187 of 189) |
| GPT-6 Astra (Max) | 52.7 (#8) | 57 tok/s (#280) | $3.26 (#173) |
| Gemini 4 Argon (High) | 52.6 (#9) | not on the board | $1.99 (#157) |
| GPT-6.1 Sol (Max) | 51.8 (#13) | 66 tok/s (#257) | $0.724 (#112) |
| **DeepSeek V4.1 Flash (Max)** | **39.5 (#67)** | **180 tok/s (#62)** | **$0.265 (#74)** |
| GPT-6 Luna (Max) | 38.1 (#77) | 121 tok/s (#133) | $0.068 (#35) |
| DeepSeek V4.1 Flash (Non-reasoning) | 24.7 (#172) | 171 tok/s (#70) | $0.147 (#58) |

What this says, and what it doesn't:

- **These are probably not 1017 numbers yet.** Both DeepSeek rows have the same Intelligence Index and cost per task as in the previous snapshot, dated 2026-10-14, three days before the 1017 release. Read them as the September build until Artificial Analysis re-measures.
- **Cheaper and faster than the frontier group, well below it on the index.** On these rows V4.1 Flash costs less than a twentieth of Opus 5.5 per task and runs nearly twice as fast, but trails Opus 5.5, GPT-6 Astra, Gemini 4 Argon and GPT-6.1 Sol on the Intelligence Index by 12 to 18 points.
- **No coding or agentic row.** Neither DeepSeek V4.1 Flash nor Opus 5.5, Argon, GPT-6.1 Sol or GPT-6 Luna has a row on the [Coding][b-coding] or [Agentic][b-agentic] boards; GPT-6 Astra does. Those are the areas where DeepSeek's own 1017 benchmarks moved most (see [more measurements](#more-measurements)).

## What we measured: Lab Pelican Test

The [Pelican Test][pelican] asks each model for an SVG of a pelican riding a bicycle, once static and once animated (wheels spin, legs pedal, CSS/SMIL only). The page is rendered to PNG and scored 0 to 5 by `google/gemini-3.8-flash` on four questions: recognizable, actually riding, a bike that works, looks good. Cost is the real billed amount on SandBase.

Leaderboard rows for the models on this page, from the [live leaderboard][pelican] on 2026-10-18 (20 models, 102 results):

| Rank | Model | Results | Score | Renders | Animation moves | Avg cost |
|---|---|---|---|---|---|---|
| 1 | openai/gpt-6.1-sol | 6 | 3.79 | 100% | 100% | $0.026 |
| 2 | google/gemini-4-argon | 4 | 3.75 | 100% | 100% | $0.150 |
| 4 | anthropic/claude-opus-5.5 | 6 | 3.42 | 100% | 100% | $0.223 |
| 5 | **deepseek/deepseek-v4.1-flash** | 6 | **3.29** | 100% | 100% | $0.017 |
| 6 | openai/gpt-6-luna | 2 | 3.25 | 100% | 100% | $0.006 |
| 8 | openai/gpt-6-astra | 6 | 3.08 | 83% | 67% | $0.102 |

The DeepSeek row mixes runs from 2026-10-06 (the September build) and 2026-10-17, so it is not a 1017 score. The results dated 2026-10-17 all come after the first 1017 posts on X (this collection has one from 04:03 UTC that day). Those are the [scored results][pelican-ds] for the 1017 build:

| Time (UTC) | Kind | Score | Recognizable / riding / bike / looks | Output tokens | Time | Cost | Judge's note |
|---|---|---|---|---|---|---|---|
| 09:14 | Static | 3.25 | 4 / 3 / 3 / 3 | 12,076 | 67 s | $0.016 | "This snappy pelican pedals smoothly into the wind, though its bike could use a proper saddle." |
| 09:14 | Animated | 3.25 | 4 / 3 / 3 / 3 | 15,272 | 81 s | $0.017 | "…the bird is coasting without any legs." |
| 11:25 | Static | 3.25 | 4 / 3 / 3 / 3 | 14,419 | 75 s | $0.017 | "…it is missing a saddle to sit on and wings on the handlebars." |
| 11:29 | Static | 3.5 | 4 / 3 / 3 / 4 | 14,350 | 70 s | $0.017 | "A stylish pelican catches a ride, though it seems to have forgotten its bike saddle." |
| 12:33 | Animated | 3.5 | 4 / 3 / 3 / 4 | 17,530 | 87 s | — | "…it's gliding on the handlebars rather than pedaling." |
| 13:06 | Animated | 3.0 | 4 / 2 / 3 / 3 | 15,805 | 81 s | — | "…it mostly hovers above the bike rather than pedaling it." |
| 13:28 | Animated | 3.5 | 4 / 3 / 3 / 4 | 18,527 | 92 s | $0.020 | "…the bicycle frame geometry is slightly distorted." |

Five more animated runs that day ended with status "failed" and no score.

What this says:

- **Recognizable every time, never fully riding.** All seven drawings scored 4 on recognizable and none above 3 on riding or on the bike. The judge's notes keep coming back to a missing saddle and a pelican that coasts or hovers instead of pedaling.
- **Mid-table quality at a very low price.** The seven 1017 results average 3.32, close to the mixed leaderboard row, at about 2 cents a drawing: roughly a tenth of Opus 5.5's or Argon's average cost, and below GPT-6.1 Sol's, which scores higher.
- **It spends tokens.** A median 15,272 output tokens and 81 s per SVG.
- **Sample size.** Seven scored results on one day. [Run it yourself][pelican-run] to add more.

The other Lab code tests don't have 1017 results yet: [Endless Runner][runner] (a canvas game) has no V4.1 Flash result, and V4.1 Flash's [Watermelon Test][watermelon] results are from 2026-10-10 and 2026-10-12, before 1017.

## What creators reported

Same-prompt comparisons posted on X. Numbers are as the creator stated them: different tools (DeepSeek Harness, API, OpenRouter, resellers), different reasoning settings, peak and off-peak prices, often one run. Click through to watch both results.

| Creator | Task | V4.1 Flash 1017 | Other model | Creator's verdict |
|---|---|---|---|---|
| [@marcthecreatorr][marc-opus] | Same prompt | ~1 hour, $0.23 | Opus 5.5: 20 min, ~$6 | Opus better on animation, sound and detail; DeepSeek "pretty close", a few errors |
| [@ItsWonda_][wonda] | Same figures as the row above | 1 hour, $0.23 | Opus 5.5: 20 min, $6 | Opus wins on polish and controls; DeepSeek close "for 26x less" |
| [@wquguru][gummy] | Gummy bear you can grab, stretch and throw | ~$0.32 (off-peak), 54 min | Opus 5.5 with Fable 5.1 as advisor: ~$7.8 (API list), 61 min | Equal at rest; DeepSeek's bear tears and its eyes drift once you touch it |
| [@aGim_asf][showreel] | 15 s motion graphics showreel | ~68M tokens | Opus 5.5: 26 min, $5.75 | "Opus cooked", DeepSeek "a lot cheaper" |
| [@kepochnik][fnaf] | Five Nights at Freddy's game | 24 min | Opus 5.5: 38 min | Asks viewers |
| [@Bhavani_00007][rocket] | Rocket launch scene | $0.78, 3 min | GPT-6.1 Sol: $6.10, 5 min | DeepSeek "absolutely cooked" |
| [@SPAC89][sol] | Same test, Max vs Sol Ultra | "0.44 cents" API cost | GPT-6.1 Sol Ultra: about the same time | DeepSeek's quality "incredible" for the price |
| [@thehypedotnews][parkour] | First-person parkour run, one HTML file, four flash models | $0.141, 1h 27m | Claude Haiku 5.5: $0.08, 23m 33s · GPT-6 Luna: $0.036, 8m 07s · Qwen3.8 Flash: $0.227, 2h 04m | DeepSeek had "the best effects of the four" |
| [@atomic_chat_hq][roadster] | Tesla Roadster event in 3D voxels | $0.89 | GPT-6 Luna: $1.07 | — |
| [@VulKan42069][vpelican] | Voxel pelican, both on Max | — | GPT-6 Luna | — |
| [@Bhavani_00007][whale] | Whale breach test | One shot "blown out"; then capped at $2.50 | Kimi K3: $2.50, one shot | Kimi better; DeepSeek "not on par with Opus 5 or Kimi in frontend and 3D" |
| [@wikiwayne][seven] | The same 7 game prompts | 9m 30s, $0.21, 343,227 output tokens | Gemini 4 Argon: $1.34 · Beam: free, 3m 45s | All 7 loaded clean; "crushed Argon on price" |

Verdicts without a side-by-side video: [@GeekCatX][mower] puts its 3D work at Opus 5.5's level and on par with Gemini 4 Argon, but slower (translated); [@aibuilderclub_][globe] calls it on par with Opus 5.5 on taste and detail; [@YifeiZhou][fps] says it "seems the same level as Gemini 4 and better than Chatgpt 6.1 sol"; [@UFO2002616][pelican-voxel] notes that Gemini 4 and GPT Astra caught a typo in the prompt that DeepSeek did not (translated).

Against the September V4.1 Flash, on the same prompt:

- [@NFT_Chen][rain-1], [@karanC_12][rain-2] and [@AndyL5cc][rain-3] show the same rainy-night convenience store, old build on the left and 1017 on the right, with visibly better light, mood and detail.
- [@leo114119][old-3d] finds 1017's Three.js modeling far stronger than the old version (translated).
- [@teortaxesTex][turtle] finds 1017 "massively faster" on the same turtle prompt "but only up until it does 90% of the job"; after that "you've got to handhold it".

Solo 1017 runs with reported cost:

| Creator | Task | Reported |
|---|---|---|
| [@wikiwayne][tour] | 24-second Three.js tour, one prompt | 194.2 s, $0.0334 (API reported) |
| [@alohaproxy][robo] | Robot assembly and launch test, Three.js | $0.04 |
| [@YifeiZhou][fps] | FPS game from one line | 37 min, $0.1 |
| [@hqmank][browser-skill] | Motion video for an open-source project | $0.25 |
| [@SahilPanhotra][peacock] | Peacock test: one shot, then a recursive loop | $0.53, then ~$1.50 ([second run][peacock-loop]) |
| [@notjazii][frieren] | SVG drawing with background music | 1h 15m, 65.7M tokens, $0.70 |
| [@vincent_ddup][tokyo] | 3D Tokyo Tower scene | 27 min, ¥1.5, no revisions |
| [@GKev1n][svg-gkev] | SVG pelican in the Harness, driven by Codex | 15m 47s, ~2.87M tokens (92% cache hit), a little over ¥1 |
| [@hiwise_aigc][whale-promo] | Whale promo video in the Harness | 18m 34s, 247 tok/s, 49.4M tokens (99% cache hit), ¥2.17 |
| [@UFO2002616][pelican-voxel] | Voxel pelican on a unicycle, Max | 37 min, ¥2.7 |
| [@marcthecreatorr][medieval] | Medieval voxel world, over 2 million voxels, max reasoning | ~25 min, ~$5 |

The pattern across both sources: a one-shot V4.1 Flash 1017 page costs cents, and long harness runs cost from about ¥1 up to $5. Against Opus 5.5, creators mostly still preferred Opus's polish while paying about 24x to 26x more, and DeepSeek was not always faster. Against GPT-6.1 Sol and GPT-6 Luna, more creators preferred the DeepSeek result.

## Rerun before you trust a comparison

Results move a lot with the setup. [@Bhavani_00007][whale]'s one-shot whale came out "completely blown out" before a second, capped run; [@SahilPanhotra][peacock-loop] got a much better peacock by adding a recursive loop and one word to the prompt; [@YxzRainy][four-demos] and [@AndyL5cc][four-demos-2] asked how long DeepSeek's own showcase demos ran, how many rounds they took and whether ordinary users can reproduce them (translated). Run the prompt yourself: paste it into the [Lab text arena][arena] with two or three models selected, or see the [tutorial](tutorial.md).

## More measurements

- [DeepSeek V4.1-Flash-1017: what the October update changes](https://blog.sandbase.ai/deepseek-v4-1-flash-1017-update-2026/?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=reading): DeepSeek's own benchmark table, which compares 1017 with the September build, Claude Opus 5, GPT-5.6 Sol, Kimi K3 and GLM-5.3 (vendor-reported, not Opus 5.5, GPT-6 or Argon).
- [DeepSeek V4.1 Flash vs V4 Pro: prices, vision, Pro status](https://blog.sandbase.ai/deepseek-v4-1-flash-vs-v4-flash-pro-2026/?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=reading).
- The same list for Gemini 4 Argon: [awesome-gemini4-argon](https://github.com/sandbase-lab/awesome-gemini4-argon).

---

Lab data: [Evals boards][evals] (Artificial Analysis, snapshot 2026-10-17) and [Pelican Test][pelican] (snapshot 2026-10-18). Creator data: their posts, linked; not independently verified.

[evals]: https://www.sandbase.ai/lab/evals?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[b-intel]: https://www.sandbase.ai/lab/evals/llm-intelligence?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[b-coding]: https://www.sandbase.ai/lab/evals/llm-coding?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[b-agentic]: https://www.sandbase.ai/lab/evals/llm-agentic?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[b-speed]: https://www.sandbase.ai/lab/evals/llm-speed?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[b-cost]: https://www.sandbase.ai/lab/evals/llm-cost?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[aa]: https://artificialanalysis.ai/
[update]: https://blog.sandbase.ai/deepseek-v4-1-flash-1017-update-2026/?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=reading
[pelican]: https://www.sandbase.ai/lab/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[pelican-ds]: https://www.sandbase.ai/lab/pelican-test/m/deepseek--deepseek-v4.1-flash?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[pelican-run]: https://www.sandbase.ai/lab/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=run
[runner]: https://www.sandbase.ai/lab/endless-runner?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[watermelon]: https://www.sandbase.ai/lab/watermelon-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=deepseek%2Fdeepseek-v4.1-flash&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[marc-opus]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111427716142571554?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[wonda]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111440074831536446?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[gummy]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111440154078703961?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[showreel]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111466670405599370?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[fnaf]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111421758691827905?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[rocket]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111501438564331534?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[sol]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111413922989224089?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[parkour]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111472170190684243?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[roadster]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111474429410566422?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[vpelican]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111476518694384061?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[whale]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111417280366031318?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[seven]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111426732217532722?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[mower]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111487932515410366?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[globe]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111453908002562494?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[fps]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111410853522129220?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[pelican-voxel]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111426130549117402?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[rain-1]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111354975213519082?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[rain-2]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111371468399689740?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[rain-3]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111397507674857813?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[old-3d]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111466664613269898?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[turtle]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111394568725774765?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[tour]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111459465472176150?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[robo]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111466763959271873?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[browser-skill]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111470277309997492?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[peacock]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111415760681849025?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[peacock-loop]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111454840337600839?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[frieren]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111476965429645706?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[tokyo]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111438861318418817?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[svg-gkev]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111392745155936690?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[whale-promo]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111402753566310600?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[medieval]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111401362713968942?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[four-demos]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111388754573398252?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
[four-demos-2]: https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111395155505033338?utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017
