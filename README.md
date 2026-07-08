# Timepress Video

Timepress Video is a Codex skill for turning Chinese articles, viewpoints, scripts, product workflows, and static visual briefs into short browser-playable motion explainers.

The core idea is simple: press a static idea into a timeline. The skill asks the agent to extract one clear cognitive anchor, choose a visual preset, design a motion shot list, then build a self-contained `index.html` with inline SVG and a GSAP timeline.

This is not an image-to-video skill. It does not generate every frame as an AI image. The agent writes SVG shapes and GSAP animation code; the browser renders the motion in real time.

## What It Produces

A normal finished output should contain:

- `index.html`: a playable HTML/SVG/GSAP composition.
- `DESIGN.md`: the selected visual preset, style prompt, colors, typography, and anti-patterns.
- `frames/`: optional screenshots for visual proof.
- A directly openable preview link, such as `http://127.0.0.1:<port>/index.html` or a published preview URL.

The final user-facing delivery must include a link that can be opened directly. The agent should start or publish the preview itself and should not ask the user to run terminal commands just to view the result.

## What It Does Not Require

Timepress Video does not require video encoders or heavyweight rendering infrastructure for its default workflow.

The default deliverable is validated playable HTML. File export is a separate downstream task.

## Visual Presets

The skill is intentionally not tied to one character or one illustration style.

Available presets:

- `editorial-sketch`: default for articles, ideas, and conceptual explainers.
- `clean-product`: for product, SaaS, and workflow explanations.
- `data-flow`: for systems, metrics, automation, process maps, and routing diagrams.
- `xiaohei-sketch`: optional only; use when the user explicitly asks for Xiaohei, 小黑, Ian-style hand-drawn article illustration, or a deadpan black character.

The `xiaohei-sketch` preset is inspired by Ian's MIT-licensed Xiaohei skill family, but the broader Timepress workflow is general-purpose and does not require Xiaohei.

## How The Animation Works

The animation is built as a web composition:

1. The agent writes a final SVG scene first.
2. The scene contains SVG elements such as paths, text, arrows, cards, machines, cursors, characters, or other main movers.
3. The agent registers a paused GSAP timeline.
4. GSAP animates SVG/CSS attributes over time, such as `opacity`, `x`, `y`, `scale`, `rotation`, and `strokeDashoffset`.
5. The browser renders each visible frame during playback.

There is no per-frame AI image generation. The "frames" are browser-rendered states of the same SVG scene over time.

## Recommended Agent Prompt

Use this prompt to test the skill with a fresh agent:

```text
Use $timepress-video at /path/to/timepress-video to turn the following Chinese viewpoint into an 8-second browser-playable motion explainer.

Viewpoint:
AI tools do not replace the creator. They turn the stuck middle of the creative process into a fast, visible timeline of experiments.

Requirements:
- Do not use Xiaohei or any mascot unless the chosen preset explicitly requires it.
- Choose the best visual preset and explain the choice in DESIGN.md.
- Produce index.html and DESIGN.md.
- Use inline SVG plus a GSAP timeline.
- Run the skill validator on the output folder.
- Start or publish a preview yourself.
- Final response must include a directly openable preview link and must not ask the user to run command-line steps.
```

Chinese version:

```text
Use $timepress-video at /path/to/timepress-video to 把下面这个中文观点做成一段 8 秒左右、浏览器可直接播放的时间线动态视频。

观点：
AI 工具真正改变创作的地方，不是替你完成作品，而是把原本卡住的中间过程变成可以快速试错的可见时间线。

要求：
1. 不要使用小黑或吉祥物，除非你明确选择了 xiaohei-sketch preset，并在 DESIGN.md 里说明理由。
2. 选择合适的 visual preset。
3. 产出 index.html 和 DESIGN.md。
4. 使用 inline SVG + GSAP timeline。
5. 运行 skill 自带 validator。
6. 自己启动或发布预览。
7. 最终回复必须给我一个可以直接打开的预览链接，不能让我去操作命令行。
```

## Output Contract For Agents

When using this skill, the agent should follow this contract:

1. Digest the source material and extract one to five cognitive anchors.
2. Choose a visual preset before coding.
3. Write a motion shot list before building the HTML.
4. Create or update `DESIGN.md`.
5. Build `index.html` with inline SVG and a deterministic GSAP timeline.
6. Run `scripts/validate_motion_project.py` against the output folder.
7. Start a local preview server or publish the result.
8. Final reply with the preview link, output paths, and validation result.

The preview link is part of the deliverable, not a nice-to-have.

## Project Structure

```text
timepress-video/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── examples/
│   │   └── timepress-demo.gif
│   └── templates/
│       └── timepress-demo/
│           ├── DESIGN.md
│           └── index.html
├── references/
│   ├── html-motion-workflow.md
│   ├── motion-patterns.md
│   ├── qa-checklist.md
│   └── style-dna.md
└── scripts/
    └── validate_motion_project.py
```

## Key Files

- `SKILL.md`: trigger description, core workflow, output contract, and boundaries.
- `references/style-dna.md`: visual presets and style rules.
- `references/motion-patterns.md`: shot list schema, scene archetypes, and motion operators.
- `references/html-motion-workflow.md`: HTML/SVG/GSAP composition contract and preview requirement.
- `references/qa-checklist.md`: final checks before delivery.
- `scripts/validate_motion_project.py`: lightweight project validator.
- `assets/templates/timepress-demo/`: starter composition using the optional `xiaohei-sketch` preset.

## Validator

The validator checks that a generated project has the expected shape:

- `index.html` exists.
- `DESIGN.md` exists.
- The composition declares width and height.
- A timeline is registered in `window.__timelines`.
- The GSAP timeline is paused for deterministic control.
- The project avoids common capture/preview problems such as random values, infinite repeats, and missing SVG.

Example:

```bash
python3 scripts/validate_motion_project.py assets/templates/timepress-demo
```

Expected result:

```text
PASS
Validated assets/templates/timepress-demo
```

## Installation

Use this repository as a local Codex skill folder.

Common options:

1. Clone or copy this folder into your Codex skills directory.
2. Keep the folder name as `timepress-video`.
3. Start a new Codex thread and invoke it with `$timepress-video`.

Example invocation:

```text
Use $timepress-video to 把这个产品流程做成一段浏览器可播放的动态视频：用户输入模糊需求，系统拆成目标、约束、素材和验收标准，最后输出任务卡。
```

## Design Principles

- Prefer readable motion over decorative motion.
- Build one conceptual action per shot.
- Use short Chinese labels attached to objects.
- Keep the composition sparse and scannable.
- Use a main mover that performs the core action.
- Avoid slideshow, dense flowchart, generic dashboard, neon UI, and image-to-video aesthetics.
- Do not require Xiaohei unless the user explicitly selected the `xiaohei-sketch` preset.

## Attribution

The optional `xiaohei-sketch` preset is inspired by and adapts visual language and workflow ideas from Ian's MIT-licensed Xiaohei skills:

- `ian-xiaohei-illustrations`
- `ian-xiaohei-scenes`

The Timepress workflow itself is a general browser-motion skill and does not depend on Xiaohei.
