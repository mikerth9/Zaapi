# Build rules

## One self-contained file

- **One file:** `prototype/zaapi_setup_prototype.html`. All CSS, JS, data and images inline. **No network requests at runtime**: no CDN, no Google Fonts, no icon fonts.
- **Font:** Inter if it's installed, otherwise the system font: `font-family: Inter, -apple-system, "Segoe UI", system-ui, sans-serif`. Don't embed a web font.
- **Icons:** small inline SVGs. Make a simple stand-in for Zaapi's ∞-style AI mark.
- **Photos:** Mike has approved downloading the six Unsplash photos listed in `03_merchants.md` from `images.unsplash.com` (about 15 KB each, at 160×160). Download them into `prototype/assets/` with `curl`, convert them to base64 data URIs, and inline them. Keep `prototype/assets/` for reference.
- **Size:** keep the file under 1.5 MB.
- **Code:** plain JS, no build step and no framework. Structure it as a data object (one entry per merchant, keyed by id) plus render functions per screen. Keep the data easy to edit: all merchant content should sit in one clearly marked `const MERCHANTS = {...}` block at the top of the script.

## Design system

- Use `prototype/tokens.css` values (paste the needed tokens into the file's `<style>`) and follow `prototype/design_system.md`:
  - root font 14px;
  - Untitled UI greys;
  - brand `#09c8ab`;
  - the AI gradient `linear-gradient(93.88deg, #1ed1bb 1.46%, #5e40e1 143.22%)` for primary buttons;
  - the light AI gradient surface and gradient text for AI-produced content;
  - status pills as specified.
- **The look comes from the Stitch designs in `prototype/stitch/`** (the PNGs, plus `DESIGN.md` sections 4–6). They deliberately make today's app larger and calmer. Where they differ from `design_system.md`, the Stitch designs win:
  - body text 14px, not the dense 12.25px;
  - cards 12px radius with 24px padding, buttons and inputs 8px radius and 40px tall;
  - one primary button per screen;
  - the left rail at 72px with labels under the seven sections.
- Desktop layout. Test at 1280×800 and 1440×900. Nothing should overflow at 1024 wide.

## State and behaviour

- State in memory: current merchant, step status and fixes applied. Optional `localStorage` for "remember last merchant", wrapped in `try/catch`; the prototype must work without it.
- **Simulated AI:** use `setTimeout` loaders of 1–5 seconds, with a progress bar and changing status text. Never block a click for more than about 5 seconds.
- **Fixes:** applying one changes that merchant's state. The step 5 re-run then shows the "after" numbers, the tracker updates, and the home turns into the dashboard once all 7 steps are done.
- **Switching merchant:** keeps each merchant's progress separately. "Reset this merchant" restores the preset start (step 1 not started, except Aisha, who can start at step 1 as well).
- **Demo shortcuts** (in the demo controls): "Jump to step…", and "Complete all steps" to show the dashboard. This is useful in an interview.

## Presenter sidebar

- Build the sidebar exactly as `07_sidebar_copy.md` describes, using its text word for word. Put all sidebar text in one `const SIDEBAR = {...}` block so it's easy to edit.
- It must look like presenter notes, not Zaapi UI (grey background, dashed left border, "Presenter notes" label).
- The running tracker ticks changes as screens are visited.

## Verify it works

1. Serve the folder locally, e.g. `python3 -m http.server 8766 --directory /Users/miker/Documents/Zaapi/prototype`, and open it in the built-in Browser pane with `preview_start`. `file://` pages can't be scripted.
2. Click through **every merchant, every step**, including every Fix button, the re-run, the dashboard and the switcher. Check the browser console has no errors.
3. Check the network log shows **no requests** apart from the HTML file itself.
4. Check with `grep` that there's no `http` in `src=` or `href=` apart from the photo credits text.
5. **Language check:** run the banned-phrase grep from `07_sidebar_copy.md` on the whole HTML file, not just the sidebar. Report the command and the result. Fix anything it finds in the UI copy too.
6. Run through `06_acceptance_checklist.md` and tick each item in the final message.

## Publishing the private link

Load the `artifact-design` skill as the Artifact tool requires, then publish the **same file**, with icon "setup" and a one-sentence description. Report the link. It's private by default; Mike decides whether to share it.

## Working style

- Work step by step, and post a short progress line every few minutes.
- Build in this order: shell and home → steps 1–7 for **Aisha** end to end → the other five merchants → notes, switcher polish and demo shortcuts → verify → README → publish → prompt log.
- If something in the context is ambiguous, make a sensible choice and note it in the README under "Decisions made while building". Only stop to ask if a choice changes what the prototype argues.
