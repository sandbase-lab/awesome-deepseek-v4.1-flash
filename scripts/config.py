"""Every model-specific value for this list. The other scripts are generic and read from here."""
import os

ORIGIN = os.environ.get('LAB_ORIGIN', 'https://www.sandbase.ai').rstrip('/')
SITE = 'https://www.sandbase.ai'  # public links in READMEs and docs always use the canonical host

SLUG = 'deepseek-v4-1-flash-1017'
REPO = 'sandbase-lab/awesome-deepseek-v4.1-flash-1017'

CFG = dict(
    slug=SLUG,
    name='DeepSeek V4.1 Flash 1017',
    short='V4.1 Flash',  # how the prose refers to the model after the first mention
    vendor='DeepSeek',
    model_id='deepseek/deepseek-v4.1-flash',
    repo=REPO,
    repo_url=f'https://github.com/{REPO}',
    campaign='awesome-deepseek-v4.1-flash-1017',
    lab_collection=f'{SITE}/lab/ai-videos/{SLUG}',
    lab_data=f'{ORIGIN}/lab/data/ai-videos/{SLUG}.json',
    media_prefix=f'{SITE}/lab/media/x/{SLUG}/',
    model_page=f'{SITE}/model/deepseek/deepseek-v4.1-flash',
    arena=f'{SITE}/lab/x/llm-arena?models=deepseek%2Fdeepseek-v4.1-flash',
    evals=f'{SITE}/lab/evals',
    pelican=f'{SITE}/lab/pelican-test',
    keys=f'{SITE}/console/keys',
    sandbox=f'{SITE}/landing/sandbox',
    lab_home=f'{SITE}/lab/',
    all_collections=f'{SITE}/lab/ai-videos',
    user_agent=f'awesome-deepseek-v4.1-flash-1017-sync/1.0 (+https://github.com/{REPO})',
    html_out='deepseek.html',
    # Output limit for the curl example. SandBase accepts max_tokens up to 384,000 for this model
    # (`sandbase inspect deepseek/deepseek-v4.1-flash --json`); 32,000 leaves room for a full page.
    max_tokens=32000,
    max_tokens_limit=384000,
    context_length=1048576,
    guide_patterns=7,  # numbered sections in docs/prompt-guide.md
    banner_title='Awesome DeepSeek V4.1 Flash 1017',
    banner_sub='Videos · prompts · tutorial · model comparison',
    # Finished pieces only on the banner: no comparisons or other models' names.
    banner_skip=('vs', 'versus', 'comparison', 'compar', 'benchmark', 'test', 'opus', 'claude', 'sonnet',
                 'gpt', 'gemini', 'argon', 'kimi', 'qwen', 'glm'),
    not_affiliated={'en': 'Not affiliated with or endorsed by DeepSeek.', 'zh-CN': '与 DeepSeek 无隶属或背书关系。'},
    # SandBase blog posts on this model: (slug, English title, Chinese title), titles as published.
    reading=[
        ('deepseek-v4-1-flash-1017-update-2026',
         'DeepSeek V4.1-Flash-1017: What the October Update Changes',
         'DeepSeek V4.1-Flash-1017：这次 10 月更新改了什么'),
        ('deepseek-v4-1-flash-1017-api-python-tutorial-2026',
         'DeepSeek V4.1-Flash-1017 in Python: Tested Code for Tools, JSON and Reasoning',
         'DeepSeek V4.1-Flash-1017 Python 实测：工具调用、JSON 与推理控制'),
        ('deepseek-v4-1-flash-vs-v4-flash-pro-2026',
         'DeepSeek V4.1 Flash vs V4 Pro: Prices, Vision, Pro Status',
         'DeepSeek V4.1 Flash vs V4 Pro：价格、看图与 Pro 现状'),
        ('deepseek-v4-1-flash-api-harness-preview-2026',
         'DeepSeek V4.1 Flash API: Preview Access and Harness Setup',
         'DeepSeek V4.1 Flash 怎么用？内测 API 型号与 Harness 配置'),
    ],
)

# README and prompt-index copy. Placeholders in {braces} are filled by build_readme.py
# ({name}, {short}, {model_id}, {html_out}, links such as {lab_stats} or {model_page}, counts {n}/{a}/{p}).
# Every fact here is sourced: the 1017 update post and the Python tutorial on blog.sandbase.ai,
# `sandbase inspect deepseek/deepseek-v4.1-flash`, the Lab Evals boards, and creators' posts.
COPY = {
    'en': {
        'switch': 'English · [简体中文](README.zh-CN.md)',
        'tagline': 'A curated list of **DeepSeek V4.1 Flash 1017 examples**: videos, prompts and demos made with DeepSeek-V4.1-Flash-1017, the October 17, 2026 update of DeepSeek\'s V4.1 Flash model. Three.js and WebGL 3D scenes, SVG and canvas animation, motion graphics and playable browser games, most of them written as code from a prompt, each one credited to its creator and linked to the original post.',
        'alt': 'Awesome DeepSeek V4.1 Flash 1017: videos, prompts, tutorial and model comparison',
        'stats': '**{n} videos** from **{a} creators** · **{p}** with the creator\'s prompt · synced daily from [SandBase Lab]({lab_stats})',
        'start': 'Start here',
        'start_rows': [
            ('Watch the videos', '[Browse by category](#contents) below, or [play them full-size on SandBase Lab]({lab_quickstart})'),
            ('Copy a prompt', '[Prompt index](docs/prompts.md): every video that comes with its prompt'),
            ('Write your own prompt', '[Prompt guide](docs/prompt-guide.md): {guide_patterns} patterns and a fill-in template'),
            ('Make a video', '[Tutorial](docs/tutorial.md): prompt → HTML → MP4, with the API, the CLI and a recording script'),
            ('Pick a model', '[DeepSeek V4.1 Flash 1017 vs. Claude Opus 5.5, GPT-6 and Gemini 4 Argon](docs/model-comparison.md)'),
            ('Try it now', '[Run DeepSeek V4.1 Flash 1017 in the Lab arena]({arena_quickstart}), next to other models'),
        ],
        'goal': 'I want to…', 'where': 'Go to',
        'how': 'Click a preview to play the video. Click a title for the post, the prompt and **Recreate** on SandBase Lab. **@handle** links to the creator\'s post on X.',
        'contents': 'Contents',
        'featured': 'Featured',
        'show_all': 'Show all {n}',
        'recreate': 'Recreate a video with {name}',
        'recreate_body': [
            'Every video page on [SandBase Lab]({lab_recreate}) has a **Recreate** button: it sends the post to {short} in the Lab text arena and returns the code, ready to play in the browser.',
            '',
            'With the API, {name} is `{model_id}` on SandBase (OpenAI-compatible); the id has served the 1017 checkpoint since October 17, 2026. Put a prompt in `prompt.txt`, create a key in the [console]({keys}), and run:',
        ],
        'recreate_after': 'Open `{html_out}` in a browser, or run it in a [SandBase Sandbox]({sandbox}) to keep generated code isolated. The model reasons before it answers and those tokens count toward `max_tokens`, so leave room. Full walkthrough: [tutorial](docs/tutorial.md). Pricing: [model page]({model_page}).',
        'prompt_tag': 'prompt',
        'more': '**[See all {n} on SandBase Lab →]({lab_section})**',
        'faq': 'FAQ',
        'faq_items': [
            ('What is DeepSeek V4.1 Flash 1017?', 'DeepSeek-V4.1-Flash-1017 is the October 17, 2026 update of DeepSeek V4.1 Flash, the September model it replaced. DeepSeek moved its `deepseek-flash` API name to it with no change to the calling method or price, and published the weights under the MIT license. On SandBase it is `{model_id}`, with a 1M-token context window and up to 384K output tokens. Source: [the 1017 update, explained]({blog_update}).'),
            ('How are these DeepSeek V4.1 Flash 1017 videos made?', 'The model doesn\'t render video. It writes a web page (HTML with Three.js, WebGL, Canvas or SVG), and the creator records the page playing. Some creators ran it in DeepSeek\'s Harness, where it also drove Blender. See the [tutorial](docs/tutorial.md).'),
            ('Where do I find the prompt for a video?', 'Videos tagged **prompt** come with the creator\'s prompt on their Lab page. The [prompt index](docs/prompts.md) lists all of them.'),
            ('How do I write a good DeepSeek V4.1 Flash 1017 prompt?', 'Ask for one self-contained HTML file, list every input and rule, ban external assets, and ask it to test its own page. Leave a large `max_tokens`: hidden reasoning shares that budget. Details and a template: [prompt guide](docs/prompt-guide.md).'),
            ('How do I use the DeepSeek V4.1 Flash 1017 API?', 'On SandBase the model id is `{model_id}` on the OpenAI-compatible `/v1/chat/completions` endpoint. One key works for every model, and existing code picked up 1017 without changes. See [Recreate](#recreate) and the [model page]({model_page}).'),
            ('Is DeepSeek V4.1 Flash 1017 better than Claude Opus 5.5, GPT-6 or Gemini 4 Argon?', 'It depends on the rival. In creators\' same-prompt tests against Opus 5.5, Opus usually wins on polish and controls while {short} costs a small fraction (for example $0.23 against about $6). Against GPT-6.1 Sol and GPT-6 Luna, several creators preferred the DeepSeek result at a lower price. Against Argon, one creator reports the same seven game prompts cost $0.21 against $1.34. On the Lab [Evals boards]({evals}) (Artificial Analysis data, 2026-10-17) the V4.1 Flash row trails Opus 5.5, GPT-6 Astra, GPT-6.1 Sol and Argon on the Intelligence Index and costs less per task than all four; that row has not changed since before the 1017 release. Details: [model comparison](docs/model-comparison.md).'),
            ('How much does one video cost?', 'Creators report from about $0.03 (a 24-second Three.js tour) to about $5 (a 2-million-voxel world on max reasoning); most one-shot pages cost cents. The list price on SandBase is $0.30 per million input tokens and $1.20 per million output tokens, and reasoning tokens bill as output.'),
            ('Can I reuse these videos?', 'No, not by default. They belong to their creators. See [MEDIA-RIGHTS](MEDIA-RIGHTS.md).'),
        ],
        'reading': 'Further reading',
        'reading_intro': 'In-depth articles on the SandBase blog, with our own runs, token counts and costs:',
        'contribute': 'Suggest a video',
        'contribute_body': 'Know a DeepSeek V4.1 Flash 1017 creation that should be here? [Open a submission]({repo_url}/issues/new?template=submit-video.yml) with the original X post. Accepted posts are added on SandBase Lab and show up here on the next daily sync. If this list helped you, a ⭐ helps others find it.',
        'credits': 'Credits & rights',
        'credits_body': [
            'Every video, prompt and post belongs to its creator. Cards credit the author and link to the original post. The MIT license covers this repository\'s scripts only. To correct a credit or remove a video, see [MEDIA-RIGHTS](MEDIA-RIGHTS.md).',
            '{not_affiliated}',
        ],
        'footer': 'Maintained by [SandBase Lab]({lab_home}) · [All AI video collections]({all_collections})',
        'p_title': 'DeepSeek V4.1 Flash 1017 prompts',
        'p_switch': 'English · [简体中文](zh-CN/prompts.md) · [← Back to the collection](../README.md)',
        'p_intro': '{n} DeepSeek V4.1 Flash 1017 videos whose creators shared the prompt. Open one to read the prompt, watch the video and **Recreate** it with {short} on SandBase Lab. New to prompting {short}? Start with the [prompt guide](prompt-guide.md).',
        'p_note': 'Each entry quotes the creator\'s post as published on X, where the prompt is shared. Some creators put the full prompt in a reply: open the post on X to read the thread. Posts keep the creator\'s language.',
        'p_watch': 'Watch',
        'p_open': 'Recreate on SandBase Lab',
    },
    'zh-CN': {
        'switch': '[English](README.md) · 简体中文',
        'tagline': '精选 **DeepSeek V4.1 Flash 1017 案例**合集：用 DeepSeek-V4.1-Flash-1017（DeepSeek V4.1 Flash 在 2026 年 10 月 17 日的更新版）做出的视频、提示词和演示。包括 Three.js / WebGL 3D 场景、SVG 与 Canvas 动画、动效和可在浏览器里玩的游戏，大多是模型根据提示词写成的代码，均注明作者并链接原帖。',
        'alt': 'Awesome DeepSeek V4.1 Flash 1017：视频、提示词、教程和模型对比',
        'stats': '共 **{n} 条视频**，来自 **{a} 位创作者** · **{p} 条**附作者提示词 · 每天从 [SandBase Lab]({lab_stats}) 同步',
        'start': '从这里开始',
        'start_rows': [
            ('看视频', '在下方 [按分类浏览](#contents)，或 [在 SandBase Lab 大屏播放]({lab_quickstart})'),
            ('复制提示词', '[提示词索引](docs/zh-CN/prompts.md)：所有附带提示词的视频'),
            ('自己写提示词', '[提示词写法](docs/zh-CN/prompt-guide.md)：{guide_patterns} 条写法和一个填空模板'),
            ('做一个视频', '[教程](docs/zh-CN/tutorial.md)：提示词 → HTML → MP4，含 API、CLI 调用和录屏脚本'),
            ('选模型', '[DeepSeek V4.1 Flash 1017 对比 Claude Opus 5.5、GPT-6 和 Gemini 4 Argon](docs/zh-CN/model-comparison.md)'),
            ('马上试试', '[在 Lab 竞技场运行 DeepSeek V4.1 Flash 1017]({arena_quickstart})，和其他模型并排对比'),
        ],
        'goal': '我想…', 'where': '去这里',
        'how': '点击预览图播放视频；点击标题前往 SandBase Lab 查看原帖、提示词，并一键 **复刻**；**@作者** 链接到 X 原帖。',
        'contents': '目录',
        'featured': '精选',
        'show_all': '展开全部 {n} 条',
        'recreate': '用 {name} 复刻视频',
        'recreate_body': [
            '[SandBase Lab]({lab_recreate}) 的每个视频页都有 **复刻** 按钮：在 Lab 文本竞技场把帖子内容发给 {short}，返回可在浏览器直接播放的代码。',
            '',
            '用 API 的话，{name} 在 SandBase 上的模型 ID 是 `{model_id}`（兼容 OpenAI），从 2026 年 10 月 17 日起由 1017 版本提供服务。把提示词写进 `prompt.txt`，在 [控制台]({keys}) 创建 Key，然后运行：',
        ],
        'recreate_after': '用浏览器打开 `{html_out}`，或在 [SandBase Sandbox]({sandbox}) 中运行，让生成的代码保持隔离。模型会先推理再作答，推理 token 也计入 `max_tokens`，请留足余量。完整步骤见 [教程](docs/zh-CN/tutorial.md)，价格见 [模型页]({model_page})。',
        'prompt_tag': '提示词',
        'more': '**[在 SandBase Lab 查看全部 {n} 条 →]({lab_section})**',
        'faq': '常见问题',
        'faq_items': [
            ('DeepSeek V4.1 Flash 1017 是什么？', 'DeepSeek-V4.1-Flash-1017 是 DeepSeek V4.1 Flash 在 2026 年 10 月 17 日的更新版，替换了 9 月发布的 V4.1 Flash。DeepSeek 把 `deepseek-flash` 这个 API 名称直接切到了新版本，调用方式和价格不变，权重以 MIT 许可开源。在 SandBase 上它是 `{model_id}`，上下文窗口 100 万 token，最多输出 384K token。来源：[1017 更新解读]({blog_update})。'),
            ('这些 DeepSeek V4.1 Flash 1017 视频是怎么做出来的？', '模型并不直接渲染视频。它写出一个网页（用 Three.js、WebGL、Canvas 或 SVG 的 HTML），作者再把页面播放过程录下来。也有作者在 DeepSeek Harness 里运行，让它调用 Blender 建模。见 [教程](docs/zh-CN/tutorial.md)。'),
            ('在哪里找到视频的提示词？', '标有 **提示词** 的视频，其 Lab 页面上有作者的提示词。[提示词索引](docs/zh-CN/prompts.md) 列出了全部。'),
            ('怎么写好 DeepSeek V4.1 Flash 1017 提示词？', '要求输出一个独立的 HTML 文件，列清每个操作和规则，禁止外部素材，并让它自测页面。`max_tokens` 要给足：隐藏的推理 token 也占用这个额度。详细写法和模板见 [提示词写法](docs/zh-CN/prompt-guide.md)。'),
            ('怎么调用 DeepSeek V4.1 Flash 1017 API？', '在 SandBase 上模型 ID 是 `{model_id}`，使用兼容 OpenAI 的 `/v1/chat/completions` 接口，一个 Key 调用所有模型；原有代码无需修改就已切到 1017。见 [复刻](#recreate) 和 [模型页]({model_page})。'),
            ('DeepSeek V4.1 Flash 1017 比 Claude Opus 5.5、GPT-6 或 Gemini 4 Argon 更强吗？', '要看和谁比。创作者与 Opus 5.5 的同提示词对比中，Opus 通常在精致度和操控上胜出，而 {short} 的花费只是零头（例如 $0.23 对约 $6）。与 GPT-6.1 Sol、GPT-6 Luna 对比时，好几位创作者更喜欢 DeepSeek 的结果，而且更便宜。与 Argon 相比，一位创作者报告同样 7 个游戏提示词花费 $0.21 对 $1.34。在 Lab [Evals 榜单]({evals})（Artificial Analysis 数据，2026-10-17）上，V4.1 Flash 这一行的智能指数低于 Opus 5.5、GPT-6 Astra、GPT-6.1 Sol 和 Argon，单任务成本则低于这四个模型；这一行自 1017 发布前以来没有变化。详见 [模型对比](docs/zh-CN/model-comparison.md)。'),
            ('做一个视频要花多少钱？', '创作者报告从约 $0.03（一段 24 秒的 Three.js 漫游）到约 $5（max 推理下 200 万体素的世界）不等，多数一次生成的页面只要几美分。SandBase 标价为每百万输入 token $0.30、每百万输出 token $1.20，推理 token 按输出计费。'),
            ('可以转用这些视频吗？', '默认不可以，视频归作者所有。见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。'),
        ],
        'reading': '延伸阅读',
        'reading_intro': 'SandBase 博客上的深度文章，包含我们自己的实测、token 数和成本：',
        'contribute': '推荐作品',
        'contribute_body': '发现了应该收录的 DeepSeek V4.1 Flash 1017 作品？附上 X 原帖 [提交给我们]({repo_url}/issues/new?template=submit-video.yml)。通过后会先加入 SandBase Lab，下一次每日同步时出现在这里。觉得有用的话，点个 ⭐ 能让更多人看到。',
        'credits': '致谢与权利',
        'credits_body': [
            '所有视频、提示词和帖子归作者所有。每张卡片都注明作者并链接原帖。MIT 许可证只覆盖本仓库的脚本。更正署名或下架视频请见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。',
            '{not_affiliated}',
        ],
        'footer': '由 [SandBase Lab]({lab_home}) 维护 · [全部 AI 视频合集]({all_collections})',
        'p_title': 'DeepSeek V4.1 Flash 1017 提示词',
        'p_switch': '[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)',
        'p_intro': '共 {n} 条 DeepSeek V4.1 Flash 1017 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 {short} 一键 **复刻**。第一次写 {short} 提示词？先看 [提示词写法](prompt-guide.md)。',
        'p_note': '每条都按 X 上发布的原文引用作者帖子，提示词就在其中；部分作者把完整提示词放在回复里，请打开 X 原帖查看讨论串。帖子原文保留作者语言。',
        'p_watch': '观看',
        'p_open': '在 SandBase Lab 复刻',
    },
}

# Labels mirror shared/ai-videos.ts VIDEO_CATEGORIES in the Lab repo.
CATEGORIES = {
    '3d-scene': ('3D scenes', '3D 场景'),
    'motion-graphics': ('Motion graphics', '动效'),
    'game': ('Games', '游戏'),
    'ui-demo': ('Product UI', '产品界面'),
    'particles': ('Particles & shapes', '粒子与形状'),
    'data-viz': ('Charts & diagrams', '图表图解'),
    'kinetic-type': ('Kinetic type', '文字动效'),
    'explainer': ('Explainers', '讲解'),
    'launch-film': ('Launch films', '发布片'),
    'short-film': ('Short films', '短片'),
    'music-video': ('Music videos', '音乐视频'),
    'anime': ('Anime', '动画'),
    'action': ('Action', '动作'),
    'ad': ('Ads', '广告'),
    'comparison': ('Tests & comparisons', '测试对比'),
    'showcase': ('Model showcases', '模型展示'),
}


def utm(medium, content=None):
    q = f'utm_source=github&utm_medium={medium}&utm_campaign={CFG["campaign"]}'
    return q + (f'&utm_content={content}' if content else '')
