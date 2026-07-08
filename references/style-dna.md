# Style DNA

## One Sentence

Timepress videos turn a static idea into a readable motion metaphor: sparse, concrete, timed, and built around one visible main mover.

## Shared Visual Rules

- 16:9 by default: `1920x1080` for landscape video.
- The selected visual preset must be written in `DESIGN.md` before building HTML.
- At least 35% blank space. The subject should occupy roughly 40%-60% of the frame.
- Use 2-6 short Chinese labels per shot. Prefer 2-6 characters each.
- The main mover must perform the conceptual action. It can be a character, object, cursor, hand, card, line, machine, data point, or tool.
- Orange or other warm accent should indicate flow, path, pressure, timeline movement, or action energy.
- Red should mark warning, problem, error, risk, or rejected state.
- Blue or cool accent should mark system feedback, renderability, result, or secondary note.

## Visual Presets

### editorial-sketch

Default for articles, viewpoints, and conceptual explainers.

- White or visually white background.
- Black hand-drawn SVG line art, slightly wobbly, thin, low density.
- Main mover is usually a simple object, hand, line, lever, note, or tiny neutral actor.
- Strange physical metaphor is preferred over a clean corporate diagram.

### clean-product

Use for SaaS/product/workflow explainers.

- Quiet product-like surface, still sparse and motion-first.
- Use restrained panels, cards, cursors, connectors, and status chips.
- Avoid marketing hero layout, dense dashboard screenshots, or decorative blobs.

### data-flow

Use for systems, metrics, automation, model routing, and process maps.

- Nodes are simple objects or cards, not formal architecture boxes.
- Motion should reveal causality: feed, split, merge, gate, sort, retry, or output.
- Keep numbers large and few; avoid table-like frames.

### xiaohei-sketch

Optional preset only. Use when the user asks for Xiaohei, 小黑, Ian-style hand-drawn article illustration, or a deadpan black character.

- Pure white background: `#ffffff`.
- Black hand-drawn SVG line art: `#111111`.
- Orange flow: `#f57c00`.
- Red warning: `#e53935`.
- Blue note: `#1e88e5`.
- Xiaohei is the operator of the metaphor, not a sticker.
- Use a solid black irregular body, white dot eyes, thin legs, occasional thin arms, and a blank serious expression.
- Avoid cute mascot behavior, complex clothing, sparkly eyes, emoji expression, or standing aside while the system works.

## Typography

Use local Chinese system fonts only:

```css
font-family: "PingFang SC", "Hiragino Sans GB", "STKaiti", sans-serif;
letter-spacing: 0;
```

Minimum sizes:

- Main labels: 38-48px.
- Secondary labels: 28-36px.
- Avoid body copy inside the frame.

## Motion Feel

The motion should feel like the drawing was found on a whiteboard and gently came alive:

- Lines draw in with stroke-dashoffset.
- Objects slide, wobble, crank, compress, unfold, or output.
- The main mover has tiny purposeful movement, not bouncy cartoon acting.
- Hold the final frame long enough to read.
- No flashy transitions, glow, particle effects, 3D camera, or cinematic grading.

## Anti-Patterns

- PPT flowchart.
- Formal architecture diagram.
- Course slide with title and bullet list.
- Dense explainer with every node labeled.
- Commercial vector illustration.
- Image-to-video wobble with unreadable Chinese text.
- Paper texture, shadows, beige background, gradient, or noise.

## Attribution

The `xiaohei-sketch` preset derives from Ian's MIT-licensed Xiaohei skill family:

- `ian-xiaohei-illustrations`
- `ian-xiaohei-scenes`

Keep attribution when redistributing that preset or examples based on it, and make clear the broader Timepress skill is a motion-video derivative, not the original static illustration skill.
