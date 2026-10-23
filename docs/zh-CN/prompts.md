# DeepSeek V4.1 Flash 1017 提示词

[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

共 32 条 DeepSeek V4.1 Flash 1017 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 V4.1 Flash 一键 **复刻**。第一次写 V4.1 Flash 提示词？先看 [提示词写法](prompt-guide.md)。

每条都按 X 上发布的原文引用作者帖子，提示词就在其中；部分作者把完整提示词放在回复里，请打开 X 原帖查看讨论串。帖子原文保留作者语言。

- [3D 场景](#3d-scene) (12)
- [动效](#motion-graphics) (1)
- [游戏](#game) (7)
- [发布片](#launch-film) (2)
- [测试对比](#comparison) (10)

<a id="3d-scene"></a>

## 3D 场景

### 体素风穿旗袍骑独轮车的鹈鹕

[@UFO2002616](https://x.com/UFO2002616/status/2111426130549117402) · 0:42 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111426130549117402/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111426130549117402?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
Deepseek-v4.1-flash 1017 体素中国风鹈鹕测试来了
dsh开max运行37分钟，一共花费2.7元人民币
 
提示词如下：
给我生成一个体素风格的中国风动画，一个穿着旗袍的醍醐在开独轮车。我要你用web3d构建这个动画
  
其中鹈鹕被误打为醍醐，ds并未能正确识别并纠偏，Gemini 4 和 GPT Astra 是能自己纠偏的，但它制作了背景音乐，场景方面和顶模有所差距，但是这性价比要什么自行车
 
另外max慎用，实在是太内耗了
```

### Three.js 3D东京塔场景

[@vincent_ddup](https://x.com/vincent_ddup/status/2111438861318418817) · 0:48 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111438861318418817/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111438861318418817?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
DeepSeek V4.1 Flash 1017  《东京塔3D》
 
需求：设计一个3D的东京塔的场景。
耗时：27分钟
费用：1.5元人民币
修改次数：0

技术说明：Three.js r160 + 自定义 GLSL（塔身高度渐变、fresnel、城市窗格、星空、天空雾） + EffectComposer / UnrealBloom / OutputPass

提示继续方向：加一段自动巡游镜头、环境音，或把当前帧导出成 4K 海报；也可以把这种“实时场景 + 编辑式 HUD”的语言接到你的网站。

兄弟们，这能打吗？
```

### Three.js 制作的特斯拉 Roadster 遥测轨迹仿真

[@IFITALEX](https://x.com/IFITALEX/status/2111441312323088473) · 0:20 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111441312323088473/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111441312323088473?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
Deepseek V4.1 1017实测完爆Gemini 4 Argon!

我将Tesla  Roadster视频分别喂给Deepseek V4.1 1017和Gemini 4 Argon，构建一个基于 Three.js的单文件交互式科学遥测网页，完整模拟并拆解Tesla × SpaceX Roadster 在 McGregor 基地实测的全过程运动轨迹。

在Deepseek Harness环境中，Deepseek V4.1耗时1h30s，总计花费¥4.04，除了运动轨迹以及汽车赛道没有完全模拟出来，3D建模这块真的完爆Gemini 4 Argon！

反观Gemini 4 Argon，除了gemini网页端花费34min就制作出成品，汽车赛道比较完整外，汽车建模真的就很敷衍。

以下是完整的提示词，想复刻的可以自己改改用！

---------分割线---------

# Tesla Roadster (SpaceX Package) 运动轨迹 3D 仿真网页制作方案

## 一、 核心生成提示词（Master Prompt 归纳版）

> **角色与任务**：构建一个基于 **Three.js** 的单文件交互式科学遥测网页（Single-File HTML），完整模拟并拆解 2026.10.15 Tesla × SpaceX Roadster 在 McGregor 基地实测的**“C 型半圆弧倒置跳台发射 → 坡顶水平倒挂射出 → 空中水平 180° 桶滚 → 离地 1m 水平喷气悬停 → 四轮平稳着陆”**全过程运动轨迹，帮助用户直观、简洁地学习整套运动学过程。
>
> **设计风格（Archival Telemetry × Risograph）**：
> - **基底质感**：1970 年代 NASA 档案级特种米白图纸（`#F3EDE0`）叠加 SVG 纸张纤维噪点与正交工程坐标网格。
> - **四色孔版油墨（Risograph Inks）**：联邦档案蓝（`#004E98`，车身主色与跳台结构）、荧光橙红（`#FF432E`，SpaceX 冷气推进羽流、主动尾翼与受力矢量）、孔雀青（`#00916E`，底盘 2G 真空吸附负压场）、档案赭黄（`#D99414`，楔形车头前照灯与质心轨迹线）、铅黑（`#1B1D21`，粗边框、实体轮胎与卡通描边）。
>
> **3D 实体汽车建模要求（拒绝简陋线框）**：
> - 主体汽车必须采用 **Three.js 程序化 3D 实体超跑模型（Solid 3D Coupe Mesh）**，严禁使用空心透明线框（Wireframe）。
> - 使用 `THREE.Shape` + `THREE.ExtrudeGeometry`（带斜切倒角 Bevel）构建低趴楔形车头、流线型深色玻璃座舱、宽体前后轮拱、车尾高翘主动尾翼与四个独立自转的 3D 实体车轮。
> - **正反面高对比分色**：车身上表面采用**联邦蓝 + 深墨色座舱顶**，底盘下表面采用**孔雀青涡扇区 + 荧光红喷口底板**，外加 `BackSide` 铅黑轮廓描边（Ink Outline），确保在 3D 空间翻转时一眼分清车头/车尾、车顶/车底。

---

## 二、 极简页面布局架构（Single-Stage Minimalist Layout）

彻底砍掉右侧多画布侧边栏与繁杂参数表，采用 **“全画幅 3D 舞台 + 轻量化浮层讲义 + 底部六阶段时间轴”** 的极简三段式单屏布局（`100vh` 无滚动）：

1. **顶部极简档案栏（Header, 46px）**
   - 左侧：档案标题 `TSLA × SPACEX ROADSTER // FLIGHT TELEMETRY` 与机密印章标签。
   - 右侧：3D 视角一键切换按钮（`[默认微倾 3D 轴测]` / `[自由鼠标环绕 Orbit]` / `[车尾第一人称跟拍]`）+ `[蓝图暗房模式]`。

2. **中央全画幅 3D 轨迹仿真舞台（Main 3D Viewport, 占屏幕 82% 面积）**
   - **单一主视觉**：左侧为带钢桁架支撑的 3D 立体 **C 型半圆弧悬挑跳台（`⊂` 形）**，右侧为平抛空翻区、1m 水平悬停反推区与着陆跑道。
   - **3D 实体频闪重影（3D Solid Strobe Ghosts）**：在轨迹的 6 个关键节点上，定格摆放半透明（Opacity 0.30）的 3D 实体跑车重影，一图看穿全过程姿态变化（可一键开关）。
   - **右上角轻量化悬浮讲义卡（Floating Stage Card）**：仅用 **1 个标题 + 2 句精炼白话解析 + 3 个核心状态标（车头朝向 / 俯仰角 Pitch / 横滚角 Roll）** 实时说明当前阶段的运动原理。

3. **底部六阶段交互时间轴（Footer Scrubber, 74px）**
   - 上排：`[▶ 播放/暂停]`、`[0.25x 慢动作]`、`[3D 频闪重影开关]`、`[3D 受力矢量箭头开关]` + 连续时间拖拽滑块（`0.00s – 3.40s`）。
   - 下排：**6 个阶段速学书签按钮**，点击任意阶段直接跳转并定格相机。

---

## 三、 核心运动轨迹与六阶段 3D 实体汽车姿态规范（100% 物理还原）

全程运动在同一条连续时间轴 $t \in [0.00\text{s}, 3.40\text{s}]$ 内完成，严格遵循以下空间坐标与刚体欧拉角：

| 阶段编号与名称 | 时间区间 | 车头切向朝向 (Heading) | 车身俯仰 (Pitch $\theta$) | 车身横滚 (Roll $\phi$) | 3D 实体姿态与物理特效表现 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **01 地面加速切入** | `0.00s – 0.55s` | **严格朝左 (`◀`, $-X$)** | $0^\circ$ (水平) | $0^\circ$ (四轮朝下) | 跑车从右侧助跑道向左高速冲入 `⊂` 型坡底；车尾喷射 3D 荧光红锥形冷气羽流。 |
| **02 2G 吸附爬坡** | `0.55s – 1.35s` | **沿弧切线顺时针调头**<br>(`◀` → `▲ 朝上` → `↗`) | 随圆弧切线旋转<br>($0^\circ \rightarrow 180^\circ$) | 车轮锁死弧面 | 底盘开启孔雀青色 3D 负压吸附光环（$\vec{F}_{\text{suction}} = 2.0G$ 垂直压向坡面），克服重力沿内壁爬上坡顶。 |
| **03 坡顶倒挂射出** | `1.35s – 1.75s` | **严格朝右 (`▶`, $+X$)** | **$0^\circ$ (平行地面)** | **$180^\circ$ (四轮朝天)** | 爬至坡顶悬挑段时车头已调头朝右（`▶`），**四轮朝上贴顶、深色车顶朝下**，平行于地面水平射出坡顶边缘！ |
| **04 高空水平横滚** | `1.75s – 2.50s` | **严格朝右 (`▶`, $+X$)** | **$0^\circ$ (全程水平不低头)** | **$180^\circ \rightarrow 90^\circ \rightarrow 0^\circ$** | 离坡后风扇关闭；在下落抛物线上半段**车身保持水平（Pitch $\equiv 0^\circ$）**，两侧冷气喷嘴一上一下喷射产生力偶，使 3D 实体车身绕水平纵轴完成 $180^\circ$ 桶滚回正。 |
| **05 离地 1m 水平悬停** | `2.50s – 2.95s` | **严格朝右 (`▶`, $+X$)** | **$0^\circ$ (严格水平)** | **$0^\circ$ (四轮水平朝下)** | **高空早已回正**；在离地约 $1\text{m}$ 处，以四轮水平朝下的正向姿态触发底盘垂直向下猛喷高压冷气（$\vec{F}_{\text{thruster}} \uparrow \gg mg$），在半空呈现**短暂水平悬停**，地面扩散 3D 气浪环。 |
| **06 四轮水平触地** | `2.95s – 3.40s` | **严格朝右 (`▶`, $+X$)** | **$0^\circ$ (严格水平)** | **$0^\circ$ (四轮同时落轮)** | 底部反推气流平缓衰减，四个实体车轮保持水平同时轻柔触地，向右平稳滑行收尾。 |

---

## 四、 3D 空间受力矢量可视化（直接绑定在主车质心）

无需额外的侧边图表，直接在 3D 跑车质心上实时渲染三根高对比度 **3D 实体圆锥箭头（`THREE.ArrowHelper` / 自定义立体箭头）**：
1. **重力 $\vec{F}_g$（铅黑色，恒定垂直向下 $-Y$）**：全阶段常驻，作为受力参考基准。
2. **真空风扇吸附力 $\vec{F}_{\text{suction}}$（孔雀青色，垂直指向 C 型坡面法向）**：仅在 `STAGE 01–03` 激活，直观解释为什么车子能吸在倒置天花板上。
3. **SpaceX 冷气推力 $\vec{F}_{\text{thruster}}$（荧光橙红色）**：
   - `STAGE 01–03`：沿车头方向推动加速；
   - `ST…
```

### 通过Blender生成的3D过山车视频

[@Yunn260414](https://x.com/Yunn260414/status/2111450021849944508) · 0:28 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111450021849944508/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111450021849944508?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
这是我用DeepSeek-V4.1-Flash 1017一句提示词生成的过山车视频

是用的DeepSeek Harness做的，它自己调用blender做出来的，音乐也是ai做的

提示词用的很简单，这个视频很粗糙，晚些发一个更精致的版本

提示词如下：
做一个过山车的视频，要3d建模出来的，长度你自己定，要足够炫酷，轨道可以错综复杂一点
```

### 基于参考图生成的Blender 3D模型

[@npaka123](https://x.com/npaka123/status/2111454710498766979) · 0:04 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111454710498766979/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111454710498766979?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
deepseek-v4.1-flash-1017 をおためし中

プロンプト:
添付画像を参考にBlenderで3Dモデルを作成して

←完成　添付画像→
```

### Three.js构建的暴风雨中的灯塔

[@TokenGremlin](https://x.com/TokenGremlin/status/2111581758575550546) · 0:30 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111581758575550546/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111581758575550546?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
DeepSeek V4.1 Flash-1017 built a lighthouse in a storm.

One prompt, DeepThink on, Three.js in a single HTML file.

> Waves with foam on the crests
> Heavy rain and lightning flashes
> Lighthouse beam sweeping through the fog
> Drone camera, zero input

I feel like this model was heavily inspired by GPT-6 Sol.
```

### Three.js模拟椋鸟群与猎鹰互动

[@TokenGremlin](https://x.com/TokenGremlin/status/2111584413280792581) · 0:28 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111584413280792581/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111584413280792581?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
DeepSeek V4.1 Flash-1017, DeepThink on, Three.js.

5,000 starlings and a hawk, all from one prompt.

> Boids with a spatial hash grid
> The flock folds, splits and merges on its own
> The hawk dives into it, or you steer it with your mouse
> The lake reflects the whole flock

The sun glow is way too blown out, but the flock motion is legit.

(Extremely laggy because I'm running this on my humble 2019 Acer Nitro 5.)
```

### Three.js特斯拉跑车物理特技动画

[@my189](https://x.com/my189/status/2111795634827354332) · 0:13 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111795634827354332/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111795634827354332?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
刚跑完这段 Three.js 动画，我盯着屏幕愣了很久。

DeepSeek-V4.1-Flash-1017 一次写通「磁吸倒挂 + RCS 
冷气翻滚 + 反推缓降 + 悬挂回弹」整套连续物理状态。
一个带 Flash 后缀的模型，居然把这一整套状态一次性丝滑写了出来。以前调重力、阻尼、粒子喷射和手持镜头抖动，够前端熬几个通宵

现在一段分镜级 Prompt 就能生成可交互 Web 3D，门槛是真的被踏平了。

把亲测效果拉满的分镜级物理提示词放下面，直接抄，也可以替换载具和受力状态，改成你自己的交互主页：

Prompt：

夜间户外实拍直播画面，得州 SpaceX 测试场，强烈的工业聚光灯照射。一辆流线型白色第二代 Tesla Roadster 高速冲上巨大的金属 C 形弧形坡道，驶至顶部 180 度完全倒置区域时，依靠车底强力吸附风扇稳稳倒挂静止在半空中。1 秒后，车辆脱离轨道顶端。车底反推喷口持续喷射白色高压冷气，缓慢降低下降速度；车身四周再爆发数道短促白色冷气脉冲（无明火），推动车身完成 180° 横滚回正。接近地面时车底向下喷出高压白雾缓冲，四轮柔和接地，避震压缩回弹。手持长焦跟拍，8K 写实物理引擎感，真实夜间光学眩光。用 Three.js + SVG 构建这段动画。

换载具或受力状态就能改成自己的交互主页。跑出更酷的版本，评论区见
```

### Three.js 打造鹈鹕骑自行车 3D 场景

[@dextune](https://x.com/dextune/status/2111830546313781515) · 0:30 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111830546313781515/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111830546313781515?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
DeepSeek V4.1 Flash 1017

Substantially improved 3D capabilities over the previous version.

Some are even wondering if it distilled Astro.

Either way, the performance is solid.

[ Prompt ]
Create a complete single-file HTML application using Three.js. Build a detailed 3D pelican riding a bicycle. Synchronize the wheels, crank, pedals, legs, and body motions. Add orbit controls and adjustable cycling speed. Use procedural geometry without external 3D models.
```

### Three.js 打造鹈鹕骑自行车的 3D 交互场景

[@0xmomonifty](https://x.com/0xmomonifty/status/2111832005222793362) · 0:20 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111832005222793362/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111832005222793362?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
DeepSeek-V4.1-Flash 1017 High + DSH 0.2.1-rc.2

提示词：

使用 Three.js 创建一个精致、可交互的 3D 网页场景：一只鹈鹕正在骑自行车。

鹈鹕、自行车、环境、动画、灯光、摄像机和交互均通过程序实现

鹈鹕需要真实地骑自行车，并具有协调的腿部、脚踏、车轮和身体运动

不要使用 SVG、2D Canvas、外部 3D 模型或预渲染动画

最终输出一个可以直接在现代浏览器中运行的完整 HTML 文件
```

### Three.js 机械镂空陀飞轮手表建模

[@GeekCatX](https://x.com/GeekCatX/status/2112170183209226383) · 0:30 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2112170183209226383/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2112170183209226383?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
兄弟们，听猫哥一句劝：别再给天价大模型交智商税了。

昨天猫哥刚测完 DeepSeek-V4.1-Flash-1017 的 3D 代码能力，基本上跟 Gemini 4 打得有来有回。

今天手痒直接上强度，扔了张图让它跑 2D 转 3D。 结果半个小时拉满出片，直接把我看跪了——

兄弟们看图（图1），我扔的根本不是什么普通大三针石英表，而是建模地狱级的： 全透蓝宝石水晶壳 + 机械全镂空陀飞轮（Tourbillon）！

我提示词甚至没给分步参数，就一句大白话： “基于 Three.js 建模，保持齿轮正常机械转动。”

懂 3D 和 WebGL 的兄弟都知道这有多离谱： Blender 资深美术拓扑这种镂空件都得死磕两天，更别说还要把透明折射和齿轮传动比写成代码。

结果它交出来的答卷狠到令人发指：
 1️⃣ 材质吃透：把外壳识别成高透物理材质（Transmission + 菲涅尔反射），透光感直接拉满。
 2️⃣ 多层纵深解构：从表盘桥板到下层传动轴，4 层机械深度拆得清清楚楚，完全不是偷懒贴平面贴图！
 3️⃣ 物理传动真实咬合：擒纵轮、中心轮、逃轮按传动比写了完整的动效循环，跑起来齿齿相扣，丝滑到 60 帧！

它叫 Flash 啊兄弟们！是个成本几乎可以忽略不计的轻量模型！

别人还在吹天价大模型怎么写诗画画，DeepSeek 已经在后台单图编译机械三维空间了。 传统 3D 互动展示页面外包动辄大几万，现在喂张图，半小时连几何体带物理动画全给你敲出来。
```

### Three.js构建的动态体素宝塔

[@Chris_Wozniczek](https://x.com/Chris_Wozniczek/status/2112652706091352471) · 1:19 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2112652706091352471/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2112652706091352471?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
First time running new Deepseek v4.1 flash 1017

Running via Deepseek Harness

Voxel Pagoda from an absolutely simple and vague prompt:

"create a one html threejs voxel pagoda animated, one html file, make the most beatiful and advanced voxel pagoda you can think of"

> 1 turn, 92 steps
> 23.3M tokens
> 233tok/s speed
> Cache hit 99.7%
> 39 min
```

<a id="motion-graphics"></a>

## 动效

### SVG 绘制的鹈鹕骑车动画

[@aizhibeibei](https://x.com/aizhibeibei/status/2111460614656913914) · 0:06 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111460614656913914/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111460614656913914?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
DeepSeek-V4.1-Flash-1017实际测评

prompt:使用svg画一个鹈鹕骑车的html。
结论：风格太想gpt 6系列了？难不成蒸蒸日上了？还是特定的风格训练？
#Deepseek
```

<a id="game"></a>

## 游戏

### Three.js 构建的第一人称射击游戏

[@YifeiZhou](https://x.com/YifeiZhou/status/2111410853522129220) · 1:36 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111410853522129220/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111410853522129220?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
Prompt is dead. Now just make a wish.

Guys, I just test latest deepseek v4.1 flash 1017 @deepseek_ai. 
It is insane. It is so insane.

ONLY one prompt, one shot, and it built the cod style fps game: 

build a call of duty 23 fps game use three js.

It auto build 37 mins and JUST 0.1 USD!

5-wave tactical survival operation, 3 operators，3 difficulty protocols. 

I can not find word to describe my feelings now. 

It seems the same level as Gemini 4 and better than Chatgpt 6.1 sol
@deepseek_ai is back.
```

### Three.js复刻以撒结合风格肉鸽游戏

[@zmdsb259414](https://x.com/zmdsb259414/status/2111477584924209246) · 4:02 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111477584924209246/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111477584924209246?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
震惊瘫坐！我用DeepSeek-V4.1-Flash-1017 MAX    

48 分钟复刻了简版《以撒结合》并且拥有模型自己的风格

玩了一晚上 DS 新模型，许愿式编程真没开玩笑 ！

几行提示词就能做游戏，而且 token 很便宜

游玩链接就在下方，点击即可游玩
https://t.co/RiCnOHggRw

提示词：用 Three.js 写一个可直接打开的单文件 index.html：《以撒的结合》风格俯视角双摇杆肉鸽。WASD 移动，方向键/鼠标射泪；每局随机生成 5–9 个连通房间（起点/战斗/宝箱/Boss），3 颗红心，清房开门；敌人会移动/射击，死亡概率掉落红心或金币；宝箱房必须三选一，提供至少 6 种被动（射速/弹体/弹射/移速/穿透/追踪等）；Boss 两阶段，击败通关。美术全部程序化：暗黑骨瓷风、基础几何体角色、Canvas 纹理、粒子、WebAudio 音效，无外部素材。包含红心/楼层/道具 UI、暂停/死亡/胜利界面，以及自动瞄准清图到通关的 Playwright 自测，最终零控制台错误。
```

### 可玩赛车小游戏与SVG相机演示

[@datouboshibb](https://x.com/datouboshibb/status/2111749742929883258) · 0:15 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111749742929883258/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111749742929883258?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
DeepSeek 又更新了！帮大家测了一下性能

这次测试 demo 里有一辆能玩的赛车，还有一台用 SVG 画出来的相机、一段能直接播放的教程动效。

翻了一圈各个平台上的原帖，跑分没记住几个，倒是这些玩意儿让人多停了两秒。然后就想：给它一个具体需求，最后交到我手里的到底是什么。

【更新了什么】

10 月 17 日，V4.1 Flash 变成 V4.1-Flash-1017，网页、App、API 同步。开发者不用改代码，还是调 deepseek-flash，价格没动。

官方这次重点不在分数，在从零做游戏、做 3D 建模这种完整项目，说新版任务耗时和输出长度都短了。演示跑在 DeepSeek Harness 上。基准图也是官方自己测的，看的时候连测试条件一起看。

普通人想知道值不值，其实不用盯这些。找一件边界清楚的小事丢给它，看能不能做成。

赛车那段，过程比结果有意思

视频里那辆车，代码来自这次留下的 deepseek-flash 会话，之后在浏览器里跑起来录的。

记录里存了两版。第一版自动演示跑到 5.8 秒撞了。把这个“撞车”原样丢回去，第二版跑完 15 秒。左右换道、重新开始也都试了，重开之后分数归零。

得说清楚几点：自动演示带辅助控制，画面上标了；这个会话没锁 1017，也没做新旧对比。所以它证明的是一个小项目从跑不通到跑通的过程，证明不了模型之间的强弱。

想自己试，从一个文件开始

发这么一段就行：

“帮我做一个单文件 HTML 赛车小游戏。方向键控制左右换道，有障碍、计分、碰撞结束、重新开始。不用外部图片，不联网。先给能跑的基础版和完整代码，再说怎么保存、怎么打开。最后列三条需要我手动验的。缺信息就先说你的假设。”

这段是这轮现写的，还没拿新版跑过。

拿到代码存成 race.html，浏览器打开。没做过网页的，让它一步步讲怎么存。

然后只验三件事：能不能打开；按键灵不灵；点重新开始，状态和分数是不是都回去了。

出毛病的时候，把“我点了什么、看到什么、本来想看到什么”写清楚。比如“点了重新开始，车回起点了，分数还留着”。这种描述下一轮才接得住。

同样的法子能套在活动预算、倒计时、排班表上。挑一件你每周真的会点开的东西，别挑“一个厉害的工具”。

【费用】

单价没变。新增的是 Search 和 Fetch，一个找网页，一个读正文，每千次成功且有结果的请求 5 元。服务端的自动搜索、抓取从北京时间 11 月 1 日 00:00 开始计费。

用 Harness 的，官方建议升到 0.2.1-rc.1 以上。
#deepseek
```

### 原生 WebGL 从零手搓可玩的我的世界

[@XingYao47854](https://x.com/XingYao47854/status/2111770397570126118) · 1:45 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111770397570126118/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111770397570126118?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
deepseek依旧让我震惊，梁圣依旧牛逼！

deepseek v4.1 flash 1017测试第二弹。

提示词我会放评论区。

我让它从零开始，不借鉴任何素材，手搓一个minecraft（我的世界）出来，花了7元人民币，以及一个小时12分钟，他展示出了他的实力。甚至连光影和水反都搓出来了。

它还把红石信号给搓出来了。（红石大佬狂喜）

有点幻视fable 5刚出来那会，手搓minecraft的场面了。

如视频所示。

他说有这么些东西：
渲染：原生 WebGL2 + GLSL ES 3.00；64 层程序化 16×16 材质、51 种方块、72 种物品；PBR 风格地形、动态日月阴影（PCF）、天光/AO、火把点光、水面法线/菲涅尔/雾、HDR、Bloom、ACES、FXAA、暗角、颗粒。
世界：无限种子地形、8 种生物群系、河流、洞穴、7 种矿脉、橡树/白桦/云杉、仙人掌、花草、海水与雪原；16×16×128 区块流式加载/卸载。
生存循环：生命、饥饿、氧气、摔落/溺水/饥饿伤害、食物、工具速度、矿石掉落、死亡与重生。
建造：挖掘、放置、中键选取、目标描边、破坏进度、粒子碎屑、方块音效、快捷栏与 36 格背包、22 个配方、配方书、创造物品面板。
生物：猪、僵尸、苦力怕。苦力怕会靠近、引信闪烁、爆炸并破坏地形；生物有受击、掉落、夜间生成与简单 AI。
模式/系统：生存 / 创造、创造飞行、种子输入、自动保存与继续世界、暂停/设置/帮助/背包/死亡界面。
声音：风、鸟、脚步、挖掘、放置、受伤、进食、合成、水花、僵尸低吼、苦力怕爆炸，以及生成式氛围音乐——全部 Web Audio 实时合成。
经典 3×3 合成网格：光标拾取/拆分/放置，实时显示产物；工作台右键打开合成页；配方书保留。
天气系统：晴 / 雨 / 雷暴 / 雪原降雪；天空、雾、环境光随天气变暗；屏幕雨幕、雪花、闪电白闪；雨声、雷声；天气写入存档。
农业与食物链：木/石/铁锄、耕地、四阶段小麦、自动生长、收获、面包；苹果/猪排/牛肉/羊肉/鸡肉等食物。
更多动物：牛、羊、鸡，加上原有猪/僵尸/苦力怕；白天游荡、掉落肉/皮革/羊毛/羽毛，带独立叫声和模型。
附魔台：附魔 UI、青金石消耗、随机三项报价；效率（挖掘速度）、锋利（近战伤害）、时运（额外方块掉落）、抢夺（额外生物掉落），可叠 I–III。
简单红石：拉杆 → 红石线 → 红石灯；15 格网络传播，通电变色、灯发光并提供点光；红石线按四邻接自动选择 X/Z/十字贴图。
```

### 生成的我的世界风3D箱庭游戏

[@jun1228909](https://x.com/jun1228909/status/2112896112847982928) · 0:17 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2112896112847982928/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2112896112847982928?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
Sage-A1.5 Q4_K_M お試し
i7-14700/5090/DDR5 128GB/Windows11/dsh/200K ctx

「マイクラ風3D箱庭ゲーム作って」
・14m25s で完走後、画面が真っ暗だったためスクショを貼って１回修正依頼
・常時 180 tok/s 前後、最大 220tok/s 超えも

流石 Qwen3.6 35B A3B ベースだけあって、安定感がある
そしてもちろんビジョンも OK😎

今回のマイクラはブロックが壊せなかったり
水平移動量が異様に小さくてほぼ動けなかったりしたけどｗ
一応形にはなってた😃

これ結構ありなのでは…？！
Qwen3.6 35B A3B が元々優秀だったから、今回のモデルとの差分の比較が難しいところではあるけど

少なくとも Qwen3.8 Flash Next や DeepSeek V4.1 Flash 1017 の Q1 や Q2 を無理に動かすよりは多くの環境でのエージェント用途の助けになりそうな感触🤔

InternScience/Sage-A1.5
```

### 用DeepSeek复刻C64国际空手道游戏

[@ivanfioravanti](https://x.com/ivanfioravanti/status/2113263765000986874) · 0:56 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2113263765000986874/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2113263765000986874?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
Do you remember "International Karate" for C64?
I've asked to DeepSeek V4.1 1017 to implement something similar using DeepSeek Harness (this is important! ⚠️ Harness makes a big difference with this model!)

Very basic prompt: "Implement the old international karate game that was running on Commodore 64."

0-shot! Starting point for additional changes. Quite impressive!

P.S.: now trying same prompt locally on Apple M3 Ultra 512GB and with MiniMax M3.1 too!
```

### 社区防洪等距视角游戏生成演示

[@BuildFastWithAI](https://x.com/BuildFastWithAI/status/2113309219202158652) · 2:45 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2113309219202158652/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2113309219202158652?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
DeepSeek V4 is insane, tested it on the Same prompt across 4 models: build an isometric flood-control game set in a Filipino neighborhood. Zero-shot, max reasoning, one run each.

V4.1 Flash 1017 genuinely surprised us. Rich colors, clean visuals, smooth camera, and an excellent tutorial.

It feels like a more polished GPT-6 Astra output.
```

<a id="launch-film"></a>

## 发布片

### DeepSeek鲸鱼宣传动画

[@hiwise_aigc](https://x.com/hiwise_aigc/status/2111402753566310600) · 0:36 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111402753566310600/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111402753566310600?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
在 Harness 中 Deepseek v4.1-flash-1017 生成一个自由发挥的宣传视频

本次耗时：18分34秒
输出速度（TPS）：247 tok/s （真爽）
token消耗：49.4m
缓存命中：99% （真高）
消费金额：￥2.17

提示词如下 👇

制作作一个关于deepseek 鲸鱼的宣传视频，尽你最大的能力，使用svg、canvas、three.js等技术、可以找网上免费的视频素材或者图片素材，交付一个高水准的宣传视频
```

### 网站创意宣传短片

[@hkdom](https://x.com/hkdom/status/2111451107318993293) · 1:47 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111451107318993293/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111451107318993293?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
使用最新的 DeepSeek Harness + DeepSeek V4.1 Flash 1017 做的宣傳片。

Prompt : 請為 https://t.co/i4YurTWh5e 做一條宣傳片，請盡量發揮你的創意

@DeepSeekHarness @deepseek_ai 我真的有點意想不到，你們已經可以做到這種地步（雖然看完後我是面紅了)
```

<a id="comparison"></a>

## 测试对比

### SpaceX超重型助推器捕获动画对比

[@adamshafizullah](https://x.com/adamshafizullah/status/2111398174548214218) · 0:22 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111398174548214218/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111398174548214218?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
🚀 DeepSeek-V4.1-Flash-1017 just dropped, so I put it head to head with Claude Opus 5.5 (High) and Claude Sonnet 5.5 (High).

Same prompt for all three: a Three.js animation of the SpaceX Super Heavy booster being caught by Mechazilla, in a single HTML file.
```

### 动态图形作品集多模型对比实测

[@aGim_asf](https://x.com/aGim_asf/status/2111466670405599370) · 0:15 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111466670405599370/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111466670405599370?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
Opus 5.5 vs DeepSeek V4.1 Flash-1017

Task: "make a 15-second motion graphics showreel… go all out"

•Opus: 26 mins, $5.75
•DeepSeek: ~68M tokens, open source

Opus cooked, but DeepSeek is a lot cheaper 

Which one would you hire?
```

### 多模型第一人称跑酷游戏生成对比

[@thehypedotnews](https://x.com/thehypedotnews/status/2111472170190684243) · 0:30 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111472170190684243/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111472170190684243?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
new deepseek v4.1 flash 1017 just built a parkour run with the best effects of the four

four flash models, one brief: a first-person parkour run in a single html file, four stages and one fix round

- deepseek v4.1 flash – $0.141, 1h 27m, thousands of glowing windows
- claude haiku 5.5 – $0.08, 23m 33s
- gpt-6 luna – $0.036, 8m 07s
- qwen3.8 flash – $0.227, 2h 04m

which one would you play?
```

### 电动机 3D 动画原理解释对比

[@rubenssoto_ai](https://x.com/rubenssoto_ai/status/2111513156589629941) · 0:40 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111513156589629941/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111513156589629941?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
Opus 5.5 vs DeepSeek V4.1 Flash 1017

Same prompt.  Same task. 

Build a cinematic 3D animation explaining how a Tesla-style electric motor works.

Is Opus in trouble?
```

### 浣熊洗碗动画生成效果对比

[@benjistacked](https://x.com/benjistacked/status/2111844370731430358) · 0:20 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111844370731430358/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111844370731430358?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
cheapest open source model? put it to the test 🦝

same prompt: a raccoon washing the dishes

• DeepSeek V4.1 Flash 1017: 22 mins, $0
• Opus 5.5: 57 mins, $10.07

opus wins. deepseek still got the raccoon out the window for $0
```

### Canvas 螺旋星系动画生成效果对比

[@WescheNex1q](https://x.com/WescheNex1q/status/2111921937865687247) · 0:09 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2111921937865687247/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2111921937865687247?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
DeepSeek V4.1 orig vs 1017 on Spark-Bench, solar / galaxy / DNA

-Orig (EXL3 2.9bpw, thinking on)
1,251,777 tok · TrueScore 88.7 · median 24.8s · galaxy HTML 9,622 B

-1017 (same stack)
632,363 tok · TrueScore 86.1 · median 16.4s · galaxy HTML 6,324 B

1017 made the better galaxy. Half the tokens.

Prompt:
“Create a single self-contained HTML file (no external libraries) with a canvas animation of a spiral galaxy: hundreds of stars rotating around a bright core, with subtle color variation and twinkle, on a black background, animated via requestAnimationFrame. Output ONLY the HTML in one code block.”
```

### JavaScript房间漫游效果对比

[@grokkedd](https://x.com/grokkedd/status/2112207013971214693) · 0:25 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2112207013971214693/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2112207013971214693?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
DeepSeek V4.1 Flash 1017 vs Claude Haiku 5.5. Same prompt: build a sweet room in JavaScript

A Reddit user ran both and posted the camera tour side by side. DeepSeek ran in a coding harness this time, not the web UI.

What to check in the video:

> Light: how window light and shadows fall on the floor and the bed
> Props: desk, shelves, plant, posters, and how much detail each model added
> Camera: how smoothly it moves through the room
> Rough edges: clipping, flat spots, blown-out highlights

The author does not name a winner, so judge it from the video.

If you run this test yourself, keep the setup identical for both models. Harness versus web UI can change the result.

Credit: u/Impressive-Chard-666 on r/DeepSeek
```

### DeepSeek 与 Opus 网页设计效果对比

[@borjaperfra](https://x.com/borjaperfra/status/2112246508376444987) · 0:35 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2112246508376444987/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2112246508376444987?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
El nuevo Deepseek v4.1 flash 1017 vs Opus 5.5
👀 He estado probando el nuevo DeepSeek v4.1 Flash 1071 a nivel de diseño. Y me ha sorprendido mucho. 

Y lo he querido comparar con Opus 5.5 👀
- Mismo prompt para los dos
- Cada uno con su harness (Claude Code vs DSH)

Les he pedido a ambos que me crearan una publicación digital sobre tecnología, IA, cultura digital e internet. Una web con un diseño muy cuidado. 
Tenéis el prompt abajo de todo. No les he dado ninguna guía de diseño. Es más, les he dicho literalmente que tienen "libertad creativa".

Pero Borja, ¿es mejor Deepseek u Opus? 
En cuestiones de diseño puro y duro, Opus sigue estando un poco por delante.
A pesar de que el juez del benchmark (un LLM ciego) haya dado algo más de puntuación a Deepseek, en cuanto a dirección artística y gusto, Opus ha conseguido crear una experiencia mucho más completa. Además, la lectura me parece mucho más cómoda. 
Para mí, está un escalón por encima. 
Eso sí, estamos hablando de detalles que con Deepseek se podrían refinar una v.2. 
A nivel de velocidad, Opus ha terminado en apenas 17 min frente a los 40 que le ha llevado a Deepseek. 

Una de las cosas más llamativas es que AMBOS han llegado a la misma dirección artística de manera independiente. Han cogido la metáfora de la radio y del signal/ noise y lo han llevado a los mismos colores, tipografías y recursos visuales. 
Entiendo que tiene que ver con el set de datos de entrenamiento en el que se basan, pero es muy curioso.  

Os dejo aquí las dos webs que han creado con la comparativa para que las podáis ver. Creo que esto podemos convertirlo en un benchmark de diseño conforme vayan saliendo los modelos. 
- Web del Design Challenge con ambas para comparar: https://t.co/b2OdwmfGZB
- Web de Deepseek: https://t.co/5aCfs2e1w8
- Web de Opus: https://t.co/G1LSVJQwwG

Repito que esto ha sido el primer resultado con un solo prompt. 

Este es el prompt, por si queréis probarlo vosotros
"### Tu misión

Diseña y desarrolla una publicación digital experimental llamada **SIGNAL / NOISE**.

Es una revista independiente sobre tecnología, inteligencia artificial, cultura digital y el futuro de internet.

Queremos una web que pueda competir visualmente con los mejores proyectos de diseño editorial digital. Una experiencia con personalidad, no otra landing genérica de SaaS.

Tienes libertad creativa para decidir la dirección de arte, tipografía, composición, paleta cromática, animaciones y sistema visual.

No quiero que me expliques cómo diseñarías la web. **Quiero que la construyas.**

### Producto

La web tendrá cuatro componentes principales:

**1. Portada editorial**

Una primera pantalla que establezca inmediatamente la identidad de la publicación.

Debe incluir el nombre SIGNAL / NOISE, el número de edición (ISSUE 001), una pieza editorial protagonista y una composición visual que resulte memorable.

**2. Índice de artículos**

Una selección de seis artículos ficticios, pero verosímiles, sobre tecnología y cultura digital.

No uses seis tarjetas idénticas. Diseña una composición editorial que permita distinguir historias protagonistas, artículos secundarios y contenidos breves.

**3. Experiencia de lectura**

Desarrolla al menos un artículo completo, al que se pueda acceder desde la portada.

Título del artículo: "The Internet Is Becoming a Place Without People".

Incluye una entradilla, varios apartados, citas destacadas y algún recurso visual integrado en el contenido.

Debe ser una experiencia de lectura agradable y cuidada.

**4. Navegación e interacciones**

Implementa navegación funcional, transiciones, estados hover, indicadores visuales y pequeños detalles de interacción.

Las animaciones deben aportar algo a la experiencia, no ser decoración gratuita.

### Requisitos técnicos

- React, TypeScript y Tailwind CSS.
- Puedes utilizar librerías de animación e iconos.
- Diseño responsive para escritorio y móvil.
- Accesibilidad básica, navegación por teclado y soporte para `prefers-reduced-motio…
```

### 像素风橘猫骑自行车模型对比测试

[@IFITALEX](https://x.com/IFITALEX/status/2112521347805143490) · 0:21 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2112521347805143490/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2112521347805143490?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
主流Flash模型实测第二弹～Minimax M3.1 flash耗时82分钟，产出只有DeepSeek一半，Gemini 3.8 flasH极速交付综合性能更好！

同一任务交给 DeepSeek、Gemini 和 Minimax 的最新Flash模型，在各自的 Harness 中运行。单看最终代码的工程完备度与细节，DeepSeek 最为扎实，但三者展现出了截然不同的工程取向：

- DeepSeek V4.1 flash 1017

用时 36 分钟，实际有效输出达 25.4 万 Token（三者中最多），99.7% 的缓存命中率确实🐮，最终的输出质量最扎实，但审美不如Gemini。

- Gemini 3.8 flash

仅耗时 5 分半交付，总 Token 消耗只有 31 万（输出近 6 万），缓存命中率 73.19%。，算力开销极低、响应极快，非常契合高频迭代场景，最终的输出效果我最喜欢！兼顾速度与质量。

- Minimax M3.1 flash

运行了 1 小时 22 分钟，有效输出 12.8 万 Token（约为 Gemini 的两倍），总消耗约 1300 万 Token，缓存命中率 95.51%。在长程任务中展现出很强的探索持续性，但时间成本相对较高。

使用的提示词如下：

-----------分割线------------

使用 Canvas 实现 16-bit 像素艺术风格的“橘猫骑自行车”侧面全身循环动画，画面居中、色彩鲜明、背景简洁，开启 image-rendering: pixelated 保持清晰像素颗粒感。输出单个独立的 HTML 网页（内联 CSS 与 JS）。

-----------分割线------------
```

### 纯代码 3D 营火生成模型对比测试

[@EvoLinkAi](https://x.com/EvoLinkAi/status/2113707025066492154) · 0:30 · [观看](https://www.sandbase.ai/lab/media/x/deepseek-v4-1-flash-1017/2113707025066492154/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/deepseek-v4-1-flash-1017/2113707025066492154?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-deepseek-v4.1-flash-1017&utm_content=prompt-index)

```text
🔥DeepSeek V4.1 Flash 1017 beats MiniMax M3.1 Flash in this code-only 3D campfire test.

DeepSeek V4.1 Flash 1017
Est. cost: $0.33 | Time: 3h 12m 35s

MiniMax M3.1 Flash
Est. cost: $0.51 | Time: ~3h 52m

Both via EvoLink.

Prompt below👇
```
