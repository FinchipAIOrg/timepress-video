# Motion Patterns

## Motion Shot List Schema

For each shot, write:

```markdown
### Shot N: <short name>

- Anchor:
- 3-second read:
- Structure type:
- Main mover:
- Main object:
- Labels:
- Color accents:
- Motion beats:
- Duration:
- Transition:
- Failure risks:
```

Keep each shot to one conceptual action.

## Structure Types

### Workflow Machine

Use for input -> processing -> output.

Visual: paper/card/source on the left, weird low-tech machine in the middle, output artifact on the right. A character, object, cursor, hand, or tool cranks, presses, sorts, or feeds the machine.

Motion beats:

1. Input line/card draws in.
2. Main mover starts action.
3. Machine activates with a small wobble.
4. Inner labels appear in order.
5. Output strip/card/timeline emerges.

### Before / After

Use for messy -> clear, manual -> automatic, static -> dynamic.

Visual: left state is loose or tangled; right state is clean but not too perfect. The main mover performs the transformation rather than pointing at it.

Motion beats:

1. Messy state appears.
2. Main mover pulls, folds, or compresses.
3. Orange path connects to after-state.
4. Red problem note fades down or moves away.
5. Blue result note appears.

### Role State

Use for anxiety, stuckness, creator workflow, product operator status.

Visual: 2-4 small states on one line or path. The main mover changes role through small actions.

Motion beats:

1. States appear one at a time.
2. Main mover travels or passes an object between states.
3. Final status gets a small hold.

### Concept Object

Use for one abstract claim.

Visual: one memorable low-tech object such as a funnel, well, press, drawer, bridge, pipe, scale, box, or gate. The main mover operates it.

Motion beats:

1. Object draws in.
2. Input appears.
3. Main mover action changes the object.
4. Output/realization appears.

### Long Scroll Story

Use for project history, personal journey, product evolution.

Visual: very wide path with 5-8 object nodes. In video, pan across the path or reveal it in segments. Do not make a numbered timeline.

Motion beats:

1. Path draws in segments.
2. Each object node reveals through main-mover action.
3. Final node resolves the current focus.

## Motion Operators

Use these small operators instead of generic animation:

- `draw`: SVG strokes reveal from zero length.
- `feed`: object slides into machine, drawer, box, or gate.
- `crank`: circular handle rotates 1-3 times.
- `press`: machine compresses with 1-3 tiny vertical shakes.
- `pull`: orange line/rope moves under the mover's hand/tool.
- `sort`: small objects separate into 2-3 paths.
- `output`: film strip, card, key, note, or timeline emerges.
- `write`: label opacity and slight y-motion, never typewriter long text.
- `hold`: final readable frame for at least 1 second.

## Timing Defaults

For one 8-second shot:

- 0.0-0.3s: white hold.
- 0.3-1.5s: main lines draw.
- 1.2-2.5s: input and main mover enter.
- 2.3-4.2s: core main-mover action.
- 3.0-5.0s: labels appear in conceptual order.
- 4.5-6.2s: output emerges.
- 6.2-8.0s: final hold and micro-motion.

For multi-shot videos, use 5-8 seconds per shot. Do not exceed 5 shots unless the user explicitly asks for a longer video.

## Label Rules

- Use labels as hand-written notes, not subtitles.
- Keep labels spatially attached to objects.
- Avoid top-left title labels such as "流程图", "系统架构", "常见坑".
- If a label overlaps during object motion, fade it out before the object travels.
