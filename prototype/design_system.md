# Zaapi design system: reference for the prototype

*Extracted from app.zaapi.com on 25 Sep 2026. The tokens are in `prototype/tokens.css`. Sources: the app's own Tailwind v4 theme variables, plus computed styles sampled on seven screens: Knowledge source, the Add-source drawer (with validation errors), Scenario handling and its template chooser, Test chat, Deploy, Settings → Integrations, and Flow Builder. The inbox was skipped because a real Gmail account is connected. "Inferred" means not directly measured.*

## What the system is

- **Built on:** Tailwind CSS v4 with a custom theme. Neutrals and status colours use the **Untitled UI** palette (e.g. gray-200 `#eaecf0`, error-500 `#f04438`), plus Zaapi brand tokens.
- **Everything is scaled down.** The root font size is **14px**, so the Tailwind scale renders at 87.5%: text-sm = 12.25px, radius-lg = 7px, spacing unit = 3.5px. That's why the app feels dense and small. **A prototype has to set `html { font-size: 14px }`** or everything will look about 14% too big.
- **Font:** Inter. Some drawer contents render in the system font (`-apple-system`), which looks like a small inconsistency in their portal styling. Use Inter throughout.
- **Icons:** **Font Awesome 7 Pro**. Regular (`far`) is the default; Solid (`fas`) for chevrons and some headers; Light (`fal`) for plus and close; and a **custom kit icon, `fa-ai-symbol`** (the ∞-style AI mark), used for AI Agent in the nav, on AI bubbles and on template tiles. For a prototype, the free Font Awesome set is close enough, but the AI mark needs a stand-in.
- **Desktop only:** content min-width 850px, max 1400px. No dark mode seen.

## Brand and AI styling

The AI gets its own visual language: **a teal-to-purple gradient**. Three named tokens:

| Token | Value | Where it's used |
|---|---|---|
| `--color-ai-gradient` | `linear-gradient(93.88deg, #1ed1bb 1.46%, #5e40e1 143.22%)` | Primary buttons ("Add knowledge source", "Use this template"), switch "on" fill |
| `--color-ai-gradient-light` | same, at 10% opacity | AI chat bubble background, 70px template icon tiles, the "Activate AI…" info banner |
| `--color-ai-gradient-text` | `linear-gradient(to right, #008a77, #875bf7)`, clipped to text | AI reply text, "Escalated by AI Agent", the AI node title in Flow Builder |

The solid brand colour ("electric green") is **`#09c8ab`** (500), with `#00a892` (600) and `#008a77` (700). It's used for selected radios, checked boxes, the switch-on base, and the Flow Builder trigger node title. Flow action nodes use indigo `#444ce7`.

**Implication for the prototype:** anything AI-driven (a readiness score, a suggested scenario, a drafted answer) should use the light gradient surface with gradient text. That's how Zaapi already marks "this came from the AI".

## Colour

| Role | Value |
|---|---|
| Primary text | `#1d2939` (gray-800) |
| Page H1 | `#000` |
| Table header text | `#344054` |
| Secondary text / helper links | `#667085` |
| Muted ("Show thinking", counters) | `#98a2b3` |
| Inactive side-menu text | `#64748b` |
| Active nav item | bg `#edeff4`, text `#475467`, weight 500 |
| Default border | `#eaecf0` |
| Focus ring / radio border | `#d0d5dd` |
| App shell and drawer background | `#f9fafb` |
| Content area | `#fefeff` (effectively white) |
| Customer chat bubble | `#f2f4f7` |
| Success pill (Completed, Enabled) | bg `#edfcf2`, text `#099250` |
| Neutral pill (Draft) | bg `#f2f4f7`, text `#667085` |
| Failed pill | bg `#fef3f2`, text `#d92d20` *(inferred from the palette; seen red in a screenshot)* |
| Pending pill | warning palette *(inferred)* |
| Error border and helper text | `#f04438` |
| Upsell button ("Subscribe now") | `linear-gradient(79deg, #1d2939 50%, #52729f 101%)` |
| "Publish" button | solid `#1d2939` |

## Typography (Inter, 14px root)

| Use | Size / weight / line height |
|---|---|
| Page H1 ("Knowledge source") | 21px / 500 / 28px, black |
| Settings page title | 17.5px / 500 |
| Drawer title ("Add scenario") | 15.75px / 600, `#1d2939` |
| Section title, sidebar heading, card title on settings | 14px / 500–600 |
| **Default UI text, labels, buttons, table cells** | **12.25px / 400 (500 for labels, table headers, card titles) / 17.5px** |
| Status pills | 12px / 500 |
| Small labels (nav group names) | 10.5px / 500 |

## Spacing, radius, elevation

- **Spacing unit** 3.5px; common values 7, 10.5, 14, 17.5, 21px.
- **Radius:** 5.25px (inputs, nav items, icon buttons); **7px** (buttons, cards, drawer, panels, filters); 10.5px (chat bubbles, dropzone, channel cards); 14px (pills); full (switches, radios).
- **Shadows** are rare. The drawer uses the standard Tailwind large shadow, `0 10px 15px -3px / 0 4px 6px -4px`, at 10% black, over a 50% black overlay. Cards are flat, with a 1px `#eaecf0` border.

## Layout

```
┌──────────────────────── trial banner 52px ("Free trial ends in 6 days" + Subscribe now) ────────────────────────┐
│ icon rail │ side menu 240px            │ content area (8px margin, white, rounded top-left 7px)                │
│ 56px      │ "AI Agent" 14/600          │ breadcrumb · H1 21/500 · description 12.25 #667085 · primary CTA top-right│
│ #f9fafb   │ group label 10.5/500       │ filter buttons (32px, white, bordered) · table (48px header)          │
│ 32px icon │ items 32px, 219px wide     │                                                                        │
│ buttons   │ active: #edeff4            │ drawers slide in from the right: 800px, #f9fafb, white section panels │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Components

| Component | Spec |
|---|---|
| **Primary button** | 32px high, padding 0 14px (21px on template cards), radius 7px, AI gradient, white 12.25px text (weight 400; 500 on cards) |
| **Secondary / filter button** | 32px, white, 1px `#eaecf0`, radius 7px, `#1d2939` text, Font Awesome icon on the left |
| **Icon button** | 32×32, radius 5.25px, transparent; active: `#edeff4` |
| **Dark button** | "Publish": 28px, `#1d2939`, radius 5.25px |
| **Text input** | 35px, padding 7px 10.5px, radius 5.25px, 1px `#eaecf0`; focus: 1px `#d0d5dd` ring; error: `#f04438` border plus "This field is required" (12.25px, `#f04438`) below, with a character counter ("0/100", right-aligned) |
| **Textarea / chat composer** | 98px, radius 5.25px, white at 80% opacity, send icon inset right |
| **Select / combobox** | 36px, radius 7px, bordered, value on the left, chevron on the right |
| **Switch** | 42×25 in tables (42×21 in the test header, 35×18 in Flow Builder); off `#eaecf0`; on `#09c8ab` + AI gradient |
| **Radio** | 18px circle, 2px `#d0d5dd`; selected: 2px `#09c8ab` with an inner dot. Used inside **radio cards** (Upload File / Add Website / Write it yourself): bordered, radius 7px; selected card border teal |
| **Checkbox** | Teal-filled rounded square with a white tick when checked *(radius inferred ~3.5px)*; used in the channel multi-select |
| **Multi-select popover** | 336px, white, 1px `#eaecf0`, radius 5.25px; header "Integrations / N selected"; parent row per channel type, child row per account |
| **Status pill** | 12px / 500, padding 1.75px 7px, radius 14px |
| **Table** | White; header 48px, 12.25/500 `#344054`; sortable headers; status toggle in the first column; row menu (⋮) in the last column; horizontal scroll |
| **Drawer** | 800px, right side, `#f9fafb`, radius 7px, padding 17.5px 21px; title 15.75/600 with close (×); content in white panels (radius 7px, padding 14px); footer Cancel (secondary) + primary on the right |
| **Card** (Deploy template, scenario template) | White, 1px `#eaecf0`, radius 7px, padding 14px (bottom 17.5px); 70px icon tile on the AI light gradient; title 12.25/500; description 12.25 `#667085`; full-width primary button |
| **Dropzone** | Dashed 1px, radius 10.5px; red dashed on error |
| **Info banner** ("Activate AI by adding…") | AI light gradient, teal left border *(width inferred)*, AI icon, text 12.25, link in purple `#9810fa` |
| **Trial banner** | 52px, centred "Free trial ends in **6** days" (14px) + "Subscribe now" dark-gradient button |
| **Chat: customer bubble** | Left aligned, `#f2f4f7`, radius 10.5px, padding 7px 10.5px, 12.25px `#1d2939` |
| **Chat: AI bubble** | Right aligned, max ~520px, AI light gradient background, **gradient text**, radius 10.5px; "Show thinking" (`#98a2b3`, comment icon) inside; small AI avatar at bottom right |
| **Chat: system marker** | "Escalated by AI Agent at 17:11", gradient text, 12.25px, under the bubble |
| **Toast** | Top right, light green, check icon, e.g. "Knowledge source successfully added" *(from screenshots)* |
| **Flow Builder node** | White card, 320px, 1px `#eaecf0`, radius 7px; coloured title per node type (trigger teal `#00a892`, AI gradient text, action indigo `#444ce7`); branch labels right-aligned with connector dots; dotted canvas (React Flow) |

## Gaps (not captured)

- The inbox and ticket views (skipped for privacy), notifications, empty states other than "No data", loading skeletons, and the mobile app.
- Exact Failed and Pending pill colours, the checkbox radius, and the info banner's border width (inferred above).
- Hover and pressed states (not sampled).
- The custom `fa-ai-symbol` glyph itself: a stand-in will be needed.
