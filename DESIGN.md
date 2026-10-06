---
name: Jordy Support
description: A practical learning site with ink, paper, green accents, and Plex typography.
colors:
  green-dark: "#22503b"
  green: "#2e6b4f"
  paper: "#fbfaf6"
  ink: "#23281f"
  muted: "#5d6157"
  border: "#d9d7cc"
  panel: "#f3f2ea"
  button-light: "#ffffff"
  button-dark: "#10160f"
  slate-green: "#86c2a4"
  slate-link: "#9ccdb4"
  slate-header: "#1a2420"
  slate-ink: "#e8eae4"
  slate-muted: "#a5aa9f"
  slate-border: "#3a4038"
  slate-panel: "#232823"
typography:
  display:
    fontFamily: "IBM Plex Serif, Georgia, serif"
    fontSize: "clamp(2.25rem, 4.3vw, 3.75rem)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.035em"
  page-title:
    fontFamily: "IBM Plex Serif, Georgia, serif"
    fontSize: "2em"
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: "0"
  headline:
    fontFamily: "IBM Plex Serif, Georgia, serif"
    fontSize: "1.5625em"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0"
  title:
    fontFamily: "IBM Plex Serif, Georgia, serif"
    fontSize: "1.06rem"
    fontWeight: 600
  body:
    fontFamily: "IBM Plex Sans, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
    fontSize: "0.88rem"
    lineHeight: 1.75
  label:
    fontFamily: "IBM Plex Sans, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
    fontSize: "0.7rem"
    fontWeight: 600
  button:
    fontFamily: "IBM Plex Sans, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
    fontWeight: 600
  code:
    fontFamily: "IBM Plex Mono, SFMono-Regular, Consolas, Menlo, monospace"
rounded:
  square: "0"
  code: "2px"
  control: "3px"
  panel: "4px"
  callout: "0 4px 4px 0"
spacing:
  action-gap: "0.6rem"
  component-gap: "0.8rem"
  row-gap: "1rem"
  section-gap: "1.8rem"
components:
  button-primary:
    backgroundColor: "{colors.green-dark}"
    textColor: "{colors.button-light}"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "0.625em 2em"
  button-primary-hover:
    backgroundColor: "{colors.green}"
    textColor: "{colors.button-light}"
  button-outline:
    textColor: "{colors.green-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "0.625em 2em"
  button-outline-hover:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.green-dark}"
  signup-button:
    backgroundColor: "{colors.green-dark}"
    textColor: "{colors.button-light}"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "0.55rem 1.1rem"
  signup-input:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "0.55rem 0.7rem"
  worked-example:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    rounded: "{rounded.square}"
    padding: "1.3rem 1.6rem"
  task-row:
    textColor: "{colors.ink}"
    padding: "1.1rem 0.7rem 1.1rem 0"
  library-row:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    padding: "0.9rem 1.1rem"
  playbook-strip:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    rounded: "{rounded.panel}"
---

# Design System: Jordy Support

## Overview

**Creative North Star: "Field Manual"**

The existing theme describes itself as ink on paper with one tool-green accent. Warm reading surfaces, serif headings, and plain controls support a site of guides, examples, and downloads. This document records that implemented visual world rather than proposing a replacement identity.

Plex Sans carries explanations and controls; Plex Serif marks chapters, task names, and example titles. Rules, rows, and softly contrasting panels organize information without shadows or hover lift. The homepage pairs a plain introduction with an example that shows a request, a draft, and the reader's check. Its composition is a homepage pattern, not a required layout for every guide.

**Key Characteristics:**

- Warm paper and dark ink in the light scheme.
- Green for actions, links, focus outlines, and chapter rules.
- Plex Serif headings with Plex Sans reading text and Plex Mono code.
- Flat surfaces, fine dividers, and small control and panel radii.
- Numbered task rows and divided playbook strips.
- Brief state transitions with reduced-motion support.

## Colors

The shared palette uses one green accent family against warm neutrals. The frontmatter records light values and the custom slate overrides; the actual color scheme switches the corresponding CSS variables.

### Primary

- **Deep Tool Green:** primary buttons, links, outlined control borders, and the light-scheme header.
- **Tool Green:** chapter rules, task arrows, hover borders, focus outlines, and primary-button hover.
- **Slate Green:** the lighter green used for accents and controls in the dark scheme.
- **Slate Link:** the separate light green used for dark-scheme reading links.

### Neutral

- **Paper:** the light-scheme reading canvas.
- **Ink:** headings, reading content, and task-row text.
- **Muted Ink:** supporting explanations, row descriptions, and small notes.
- **Paper Border:** dividers and outlined panels.
- **Panel Paper:** worked examples, library rows, metadata strips, and callouts.
- **Button Light / Button Dark:** contrasting primary-control text in the light and slate schemes.
- **Slate Header, Ink, Muted, Border, and Panel:** custom dark-scheme counterparts. The remaining dark canvas and syntax colors come from MkDocs Material.

VALE and TUSK download pages retain localized dark product heroes and media surfaces. VALE uses red and cyan details; TUSK uses amber. These page-specific colors are not shared learning-site tokens.

**The Shared Accent Rule.** Use the green family for shared learning controls and reading patterns. Keep product-page accent colors local to their existing product surfaces.

## Typography

**Display Font:** IBM Plex Serif with Georgia and serif fallbacks.

**Body Font:** IBM Plex Sans with the inherited system sans-serif fallback stack.

**Label/Mono Font:** IBM Plex Mono with the inherited system monospace fallback stack.

**Character:** Serif headings distinguish sections and tasks while the sans-serif body keeps instructions readable. Monospace supports code, numbered steps, and compact download metadata. The current reading styles hide the earlier uppercase kickers.

### Hierarchy

- **Display:** the homepage title uses the display token, a short measure (20ch), and a responsive size. Its mobile size is recorded in Layout.
- **Page Title:** guide titles use the page-title token and normally carry a short green rule above them.
- **Headline:** section headings use the headline token; their top spacing is generous (2.3rem). Subheadings remain serif (weight 600, line-height 1.4).
- **Title:** task names use the title token. Library names are smaller (1rem); the worked-example title is larger (1.2rem).
- **Body:** the body token governs reading content. Homepage lead paragraphs are larger (1rem) with a limited measure (48ch).
- **Label:** the label token identifies parts of the worked example. Compact step and download metadata use monospace with their local sizes and tracking.

**The Chapter Rule.** Keep ordinary guide titles serif and retain their short green rule (2.6rem wide, 0.28rem high). The homepage title and dark product heroes explicitly omit that rule.

## Layout

The Material shell has a bounded grid (76rem). Guide pages retain the framework's navigation and table of contents; the homepage hides its side navigation and table of contents. On wide screens, non-home reading content receives additional inner padding (0 1.5rem 1.5rem) at the observed threshold (min-width 76.25em).

The homepage introduction uses two unequal columns (1.4fr and 1fr) and a fluid gap (clamp(2rem, 5vw, 5rem)). Task links are full rows with a number, text, and arrow. Library rows align text and actions horizontally. Playbook metadata and step strips divide three equal columns; older path strips divide five. The recurring spacing values in frontmatter are extracted values, not a comprehensive spacing scale.

At the custom compact threshold (max-width 52rem), the homepage introduction and learning paths stack, library actions move below their descriptions, strips become single columns, and anchor buttons expand to full width. Body text becomes slightly smaller (0.86rem). The homepage title uses a mobile clamp (clamp(2.1rem, 7.5vw, 3rem)); example padding reduces (1rem 1.1rem). Media and product grids also stack. The separate Material desktop navigation threshold is inherited (tabs hidden at max-width 76.234375em).

**The Stack Rule.** Preserve source order when layouts become single columns. Keep descriptions, controls, and each strip's labels together at the compact threshold.

## Elevation & Depth

Custom buttons, cards, reading tables, admonitions, and the header remove their shadows. Fine borders and contrasting panel tones provide separation. Cards change border color on hover without moving. This applies to the documented custom reading surfaces; framework overlays and other inherited utilities retain their own behavior.

**The Flat Surface Rule.** Shared reading cards and controls do not gain shadows or hover lift. Use the existing border and surface-color states.

## Shapes

Controls have a small radius; ordinary panels, strips, reading tables, and media frames have a slightly larger one. Inline code uses the smallest radius. The worked example and dark product heroes are square. Several callout panels keep square left corners and slightly rounded right corners. Fine panel strokes (1px) and somewhat heavier control strokes (1.5px) distinguish surfaces from actions.

**The Small Corner Rule.** Preserve the documented square and small-radius shapes. Do not convert controls or panels into pills.

## Components

### Buttons

Rectangular, clear actions with solid and outlined variants. Primary controls use Deep Tool Green with contrasting light text; outlined controls use a green stroke. Both inherit Material's button padding through the documented tokens. Primary hover uses Tool Green; outlined hover uses Panel Paper. Their custom transitions change background and text color (120ms ease). Keyboard focus receives a green outline (2px) with space around it (4px).

The newsletter submit control uses its smaller local padding and type (0.8rem). Its disabled state reduces opacity (0.6) and returns to the default cursor. Slate primary-control text uses Button Dark.

### Cards / Containers

Flat, bordered surfaces group related information. Ordinary card and strip shapes use the panel radius; a hovered link card changes its border to green. Library rows pair a serif name and muted description with an action. Download media panels preserve actual screenshots, their captions, and separate product accents.

### Inputs / Fields

The newsletter email field uses the reading canvas, ink text, a fine border, and the control radius. Its placeholder is muted and its type is compact (0.8rem). Focus uses the shared green outline. The original input focus offset (1px) is superseded by the shared keyboard-focus offset (4px) when focus is visible. No custom error appearance is established in the inspected styles.

### Navigation

MkDocs Material provides the header, desktop tabs, side navigation, mobile drawer, search, and table of contents. The custom header is flat, and tab text is small (0.76rem) with a subdued resting opacity (0.9). The active tab uses full opacity and an underline with a generous offset (0.5rem); hovered tabs use full opacity. Active side-navigation links use a heavier weight (600). Mobile navigation retains Material's drawer behavior.

### Worked Example

A square Panel Paper surface with a fine outline and stronger green top rule (3px). A serif title introduces three parts separated by rules: the request, the draft, and the reader's check. Small green labels make the sequence easy to scan. It has no hover movement or fabricated interface chrome.

### Task Rows

Numbered text links span a divider-based list. Each row pairs a small monospace number, a serif task name, muted supporting text, and a green arrow. Hover changes the row surface to Panel Paper without underlining the whole row; keyboard focus uses the shared outline.

### Playbook Strips

One bordered container holds equal cells with contrasting panel backgrounds and interior dividers. Monospace labels appear above short descriptions. The compact layout replaces vertical dividers with horizontal ones rather than squeezing the columns.

**The State Motion Rule.** Use the existing short color and border transitions for custom components. Preserve the reduced-motion override that removes transitions; do not add content-reveal motion to reading patterns.

## Do's and Don'ts

### Do:

- **Do** pair serif headings and task titles with sans-serif explanations.
- **Do** use green for shared actions, links, focus, and chapter markers.
- **Do** separate related content with fine dividers and the existing panel tones.
- **Do** preserve keyboard focus outlines and the reduced-motion override.
- **Do** stack the documented row and strip layouts at their existing compact threshold.
- **Do** use actual product screenshots on their existing download surfaces.

### Don't:

- **Don't** add gradients, shadows, hover lift, or pill shapes to shared reading patterns.
- **Don't** turn localized VALE or TUSK accents into the learning site's primary palette.
- **Don't** impose the homepage's two-column introduction on every guide.
- **Don't** reintroduce uppercase kickers into the current reading pages.
- **Don't** present a decorative mock interface as a worked example or product capture.

<!-- Extracted from PRODUCT.md, mkdocs.yml, docs/index.md, docs/playbooks/index.md,
     docs/stylesheets/extra.css,
     and inherited selectors in site/assets/stylesheets/main.ec1eaa64.min.css.
     No browser-computed-style or live-panel rendering verification was performed.
     Sidecar tonal ramps are synthesized panel previews, not implemented theme scales. -->
