# HTML Motion Workflow

## Project Layout

Default output:

```text
<output-dir>/
├── DESIGN.md
├── index.html
└── frames/            # optional browser screenshots
```

Use `assets/templates/timepress-demo/` as a starter when helpful.

## HTML Contract

`index.html` must include:

- One top-level composition element:

```html
<div
  id="root"
  data-composition-id="..."
  data-duration="8"
  data-track-index="0"
  data-width="1920"
  data-height="1080"
>
```

- Inline SVG for the frame.
- A paused GSAP timeline registered for deterministic preview control:

```js
window.__timelines = window.__timelines || {};
const tl = gsap.timeline({ paused: true });
window.__timelines["<composition-id>"] = tl;
```

- Browser preview playback:

```js
const previewMode = !new URLSearchParams(window.location.search).has("capture");
if (previewMode) tl.play(0);
```

## GSAP Rules

- Animate `opacity`, `x`, `y`, `scale`, `rotation`, color, and stroke offsets.
- Do not use `Math.random()`, `Date.now()`, `repeat: -1`, async timeline construction, or media play/pause calls.
- Use finite repeats for cranks and machine vibration.
- Build the hero frame first, then animate from hidden/offscreen states.

## Local Preview

1. Start a local static server yourself or publish the folder to a preview host.
2. Final delivery must include a directly openable link, usually `http://127.0.0.1:<port>/index.html` for local work or a public preview URL for shared review.
3. Do not ask the user to run command-line steps to view the result.
4. Scrub by using browser DevTools or temporarily seeking the registered GSAP timeline in the console.
5. Capture browser screenshots in `frames/` if visual proof is useful.

The completed deliverable is the validated playable HTML project. File export is outside this skill.

## Validation Script

Run:

```bash
python <skill-dir>/scripts/validate_motion_project.py <output-dir>
```

The validator checks required files, timeline registration, composition attributes, banned nondeterministic patterns, and obvious missing Timepress motion-project markers.
