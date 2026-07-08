# QA Checklist

## Required

- `DESIGN.md` exists and defines the selected Timepress visual preset.
- `index.html` exists and opens directly in a browser.
- The composition is 16:9, usually `1920x1080`.
- The background matches the selected preset and remains readable.
- A visible main mover performs the core action.
- The video has one clear conceptual action per shot.
- The frame has at least 35% blank space.
- Chinese labels are short, readable, and sparse.
- Accent colors have semantic roles, such as flow, warning, result, or system feedback.
- The final frame holds long enough to read.

## Must Not Appear

- Top-left type title such as "流程图", "架构图", "路线图", "常见坑".
- PPT-like boxes, bullet lists, dense node labels, formal swimlanes.
- Generic tech UI, dashboard, app screenshot, or neon/cyber style.
- Beige paper, shadows, gradients, texture, noise, glow, bokeh, or dark canvas.
- Cute mascot behavior or expressive cartoon acting.
- Infinite repeats, random values, async timeline setup, or render-time network data fetches.
- A required Xiaohei character unless the selected preset is `xiaohei-sketch`.

## Motion Check

Scrub or sample at least three moments:

- Early: line drawing and first object enter.
- Middle: the main mover performs the main action.
- Late: output artifact and final labels are visible.

For each sample, check:

- No text overlaps an object.
- No label leaves the frame.
- The main mover remains connected to the action.
- The viewer can understand the 3-second read.

## Preview Check

- Run the skill validator against the output folder.
- Open `index.html` directly or through `python3 -m http.server`.
- Confirm the animation plays without console errors.
- Final response includes a directly openable preview link and does not ask the user to run terminal commands.
- Capture browser screenshots in `frames/` if the user needs visual proof.
- Treat validated playable HTML as the finished deliverable. File export is a separate downstream task.
