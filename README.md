<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/paulfxyz/openline-brand-assets/main/logo/png/openline-logo-white.png" />
  <img src="https://raw.githubusercontent.com/paulfxyz/openline-brand-assets/main/logo/png/openline-logo-color.png" alt="Openline" width="120" height="120" />
</picture>

# Openline · Audit Shots & OS Badge System

**The public image host for Openline's UI/UX audit screenshots and every badge, nav button, and hero banner used across the Openline OS Notion workspace.**

[![Purpose](https://img.shields.io/badge/purpose-audit%20·%20OS%20badges-6D28D9?style=flat-square)](#what-this-repo-is)
[![Audit shots](https://img.shields.io/badge/audit%20shots-36-2563EB?style=flat-square)](#1--uiux-audit-screenshots-shots)
[![OS badges](https://img.shields.io/badge/OS%20badges-90-0E9CA8?style=flat-square)](#2--os-badge--hero-system-os-nav)
[![Staff images](https://img.shields.io/badge/staff%20images-8-22C55E?style=flat-square)](#3--staff-dashboard-images-staff)
[![Visibility](https://img.shields.io/badge/visibility-public%20(required)-F38020?style=flat-square)](#why-this-repo-must-stay-public)
[![Hot-link](https://img.shields.io/badge/hot--link-pinned%20SHA-9333EA?style=flat-square)](#hot-link-urls-raw-github)
[![Status](https://img.shields.io/badge/status-actively%20maintained-22C55E?style=flat-square)](#changelog)
[![Website](https://img.shields.io/badge/openline.com-Visit-FF6A00?style=flat-square)](https://openline.com)

</div>

---

> **Openline** is an eSIM provider that always gets the best signal — instant data in **190+ countries**, multi-carrier Tier-1 networks, automatic switching, no roaming bills.
>
> This repository serves two jobs:
> 1. **An archive** of the annotated UI/UX audit screenshots taken of `openline.com`.
> 2. **The live image host** for the badges, nav buttons, and hero banners that decorate the **Openline OS** Notion workspace — hot-linked straight into pages via pinned-SHA raw GitHub URLs.

---

## ⚠️ Why this repo must stay public

Every badge and hero image in the Openline OS Notion workspace is embedded with a **`raw.githubusercontent.com`** URL like:

```
https://raw.githubusercontent.com/paulfxyz/openline-audit-shots/<SHA>/os-nav/badge-tasks.png
```

`raw.githubusercontent.com` **only serves files from public repositories.** If this repo is flipped to **private**, every one of those URLs returns `404` and **all badges, nav buttons, and hero banners across the entire OS (Plan, Develop, Operate, Grow, Team, Production, Guidebook, Executive, Archives, plus every staff dashboard) break instantly.**

> **Bottom line: keep this repo `public`.** It contains no secrets — only screenshots and decorative PNGs. The whole point is that GitHub serves the images for free, forever, at a stable URL. This README exists (like the one in [`openline-brand-assets`](https://github.com/paulfxyz/openline-brand-assets)) precisely *because* the repo is public and benefits from a proper front door.

---

## Table of contents

- [What this repo is](#what-this-repo-is)
- [At a glance](#at-a-glance)
- [Repository layout](#repository-layout)
- [1 · UI/UX audit screenshots (`shots/`)](#1--uiux-audit-screenshots-shots)
- [2 · OS badge & hero system (`os-nav/`)](#2--os-badge--hero-system-os-nav)
- [3 · Staff dashboard images (`staff/`)](#3--staff-dashboard-images-staff)
- [Hot-link URLs (raw GitHub)](#hot-link-urls-raw-github)
- [How to generate / regenerate badges](#how-to-generate--regenerate-badges)
- [The publishing loop](#the-publishing-loop)
- [Contributing & maintenance](#contributing--maintenance)
- [Changelog](#changelog)

---

## What this repo is

| Layer | What it holds | Who reads it |
| --- | --- | --- |
| **Audit** | 36 annotated screenshots of `openline.com` surfacing UI/UX bugs and opportunities | The Openline team, during the site audit |
| **OS badges** | 90 badges, nav buttons, and hero banners for the Notion OS | Notion (hot-linked) + the badge generator |
| **Staff** | 8 hero + section images for staff dashboards | Notion (hot-linked) |
| **Generator** | `scripts/gen.py` + per-batch scripts + Lucide icons | Anyone making a new badge |
| **Docs** | [`BADGE-SYSTEM.md`](BADGE-SYSTEM.md), [`CONTEXT.md`](CONTEXT.md), this README | Maintainers |

---

## At a glance

| You need… | Grab… |
| --- | --- |
| A specific **audit screenshot** | [`shots/01_home_hero.png`](shots/01_home_hero.png) … [`shots/36_payment_icons.png`](shots/36_payment_icons.png) |
| An **OS section badge** (e.g. above an inline DB) | [`os-nav/badge-tasks.png`](os-nav/badge-tasks.png), [`os-nav/badge-objectives.png`](os-nav/badge-objectives.png), … |
| An **OS nav button** (home → section) | [`os-nav/button-plan.png`](os-nav/button-plan.png), [`os-nav/button-executive-hq.png`](os-nav/button-executive-hq.png), … |
| An **OS section hero** (Overview banner) | [`os-nav/button-plan-overview.png`](os-nav/button-plan-overview.png), [`os-nav/button-overview-orange.png`](os-nav/button-overview-orange.png), … |
| A **staff dashboard** image | [`staff/staff-button-dashboard.png`](staff/staff-button-dashboard.png), [`staff/staff-badge-tasks.png`](staff/staff-badge-tasks.png), … |
| To **make a new badge** | Read [`BADGE-SYSTEM.md`](BADGE-SYSTEM.md), then run `scripts/gen.py` |
| To understand **how images reach Notion** | See [`CONTEXT.md`](CONTEXT.md) |

---

## Repository layout

```
openline-audit-shots/
├── README.md                ← you are here
├── BADGE-SYSTEM.md          ← single source of truth for making badges
├── CONTEXT.md               ← how images are served into Notion + full inventory
│
├── shots/                   ← 36 annotated UI/UX audit screenshots of openline.com
│   ├── 01_home_hero.png
│   ├── 02_destinations_count.png
│   └── … (through 36_payment_icons.png)
│
├── os-nav/                  ← 90 published OS badges / nav buttons / heroes (hot-linked to Notion)
│   ├── badge-*.png          ← section badges (auto×34px pills)
│   ├── button-*.png         ← nav buttons & section heroes (280×50)
│   ├── mini-*.png           ← legacy mini nav badges
│   └── _*_sheet.png         ← contact / verification preview sheets
│
├── staff/                   ← 8 staff-dashboard images (hot-linked to Notion)
│   ├── staff-button-dashboard.png
│   └── staff-badge-*.png
│
├── out_images/              ← generator scratch output (git-tracked working copies)
│
└── scripts/                 ← the badge generator
    ├── gen.py               ← core: make(preset, fill, icon, label, outfile)
    ├── build_all.py         ← builds the full OS badge set
    ├── make_staff.py        ← builds staff-dashboard images
    ├── gen_*.py             ← per-batch scripts (archives, production, guidebook, …)
    └── lucide/*.svg         ← bundled Lucide icon source files
```

---

## 1 · UI/UX audit screenshots (`shots/`)

The original purpose of this repo. `shots/` holds **36 annotated screenshots** captured during the UI/UX audit of `openline.com` — each one numbered and named for the issue or surface it documents (broken cart, dead buttons, currency mix-ups, mobile quick-buy flow, payment icons, and so on).

These are a **point-in-time audit artifact**. They are not regenerated; they're kept for reference and traceability of what was found and when.

---

## 2 · OS badge & hero system (`os-nav/`)

`os-nav/` is the **live image host** for the Openline OS Notion workspace. A **badge** is a solid rounded pill with a flat color fill (Openline palette), a Lucide icon tinted from the fill, and an ALL-CAPS **Lato Black** white label. They sit above inline databases and at the tops of tabs to label sections; nav buttons and heroes are the larger 280×50 banners.

Every image is produced by one generator (`scripts/gen.py`) so the look is identical everywhere. See [`BADGE-SYSTEM.md`](BADGE-SYSTEM.md) for the full design system, color palette, size presets, and ready-to-run prompts.

**Notion embeds each image via a raw GitHub URL pinned to a commit SHA** (never `main`) so the image never changes underneath a page:

```
https://raw.githubusercontent.com/paulfxyz/openline-audit-shots/<SHA>/os-nav/<file>.png
```

When you regenerate and push, the SHA changes — you must then update the SHA in the referencing Notion pages (find-and-replace old SHA → new SHA). The pages that reference these images are listed in [`CONTEXT.md`](CONTEXT.md) § 5.

---

## 3 · Staff dashboard images (`staff/`)

`staff/` holds the **8 images** used on staff dashboards and the staff database templates: one deep-red hero (`staff-button-dashboard`) plus seven varied-color section badges. They follow the same generator and embed pattern as `os-nav/`, but on an independent SHA so they can be re-pushed without disturbing the OS pages.

---

## Hot-link URLs (raw GitHub)

These resolve **only while the repo is public** (see [above](#why-this-repo-must-stay-public)). Always pin a commit SHA. The current `HEAD` is `1f635dc`:

```
https://raw.githubusercontent.com/paulfxyz/openline-audit-shots/1f635dc/os-nav/button-plan.png
https://raw.githubusercontent.com/paulfxyz/openline-audit-shots/1f635dc/os-nav/badge-tasks.png
https://raw.githubusercontent.com/paulfxyz/openline-audit-shots/1f635dc/os-nav/badge-badge-system.png
https://raw.githubusercontent.com/paulfxyz/openline-audit-shots/1f635dc/os-nav/badge-ai-agent.png
https://raw.githubusercontent.com/paulfxyz/openline-audit-shots/1f635dc/staff/staff-button-dashboard.png
https://raw.githubusercontent.com/paulfxyz/openline-audit-shots/1f635dc/shots/01_home_hero.png
```

> For **high-traffic** placements you could front these through jsDelivr (`https://cdn.jsdelivr.net/gh/paulfxyz/openline-audit-shots@<SHA>/<path>`), but the Notion OS embeds are low-traffic and raw GitHub is fine.

---

## How to generate / regenerate badges

Requirements: Python 3 with **Pillow** and **cairosvg**, plus the **Lato Black** font at `/usr/share/fonts/truetype/lato/Lato-Black.ttf`. Lucide SVG icons are bundled in `scripts/lucide/`.

```bash
pip install Pillow cairosvg

# Build the full OS badge set       → writes to out_images/
python scripts/build_all.py

# Build staff-dashboard images       → writes to out_images/
python scripts/make_staff.py
```

To make **one new badge**, the simplest path is a small per-batch script that calls `make(...)` from `gen.py`:

```python
from gen import make
# make(preset, fill, icon_name, label, outfile, autowidth=True)
make("section", "fuchsia", "palette", "BADGE SYSTEM", "badge-badge-system.png")
```

- **preset**: `section` (auto×34 pill), `button` (280×50 hero/nav), or `mini` (legacy).
- **fill**: a palette name (`violet`, `indigo`, `blue`, `cyan`, `teal`, `emerald`, `green`, `lime`, `amber`, `orange`, `rust`, `red`, `rose`, `pink`, `fuchsia`, `slate`).
- **icon_name**: a Lucide icon present in `scripts/lucide/`. To add one:
  ```bash
  cd scripts/lucide && curl -fsSL \
    "https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/<name>.svg" -o <name>.svg
  ```

Full design rules, color guidance, and copy-paste prompts live in [`BADGE-SYSTEM.md`](BADGE-SYSTEM.md).

---

## The publishing loop

```bash
# 1. Regenerate into out_images/, then copy the changed file into the served folder
cp out_images/badge-new.png os-nav/        # or staff/

# 2. Commit & push
git add os-nav staff scripts *.md
git commit -m "Describe the change"
git push origin HEAD

# 3. Grab the new SHA — this is what Notion must point at
git rev-parse HEAD
```

Then in Notion, find-and-replace the old SHA → new SHA inside the referencing pages' image URLs. Keep the `os-nav/` and `staff/` SHAs independent — you can re-push one without touching the other, as long as you only update the affected pages.

---

## Contributing & maintenance

This repo is **actively maintained** alongside the Openline OS.

- **Adding a section to the OS?** Generate its badge (see above), push, then embed the pinned-SHA raw URL in the Notion page.
- **Spotted a broken badge in Notion?** It's almost always a stale or private-repo URL — confirm the repo is still **public** and that the page points at a SHA that actually contains the file.
- **New audit screenshots?** Drop them in `shots/` with the next sequential number and a descriptive slug.

### Don'ts

- ❌ Don't make this repo private — it breaks every OS badge ([why](#why-this-repo-must-stay-public)).
- ❌ Don't reference images via `…/main/…` in Notion — always pin a **commit SHA**.
- ❌ Don't store anything secret here — it's public by design.

### Maintainer

- **[@paulfxyz](https://github.com/paulfxyz)** — repository owner.

---

## Changelog

### 2026-06-29

- 📝 **Added this README** — documents both repo purposes (audit shots + OS badge system), the public-repo requirement, layout, hot-link URLs, and the generate/publish loop.
- 🤖 Added **AI Agent** tab badge (`badge-ai-agent.png`, cyan/bot).
- 🎨 Added **Badge System** guidebook-tab badge (`badge-badge-system.png`, fuchsia/palette).
- 🧹 Cleaned up: committed the badge generator scripts, Lucide icons, and generated assets; added `.gitignore` for `__pycache__`.

### Earlier

- Initial drop: 36 UI/UX audit screenshots of `openline.com` (`shots/`), followed by the OS badge & hero system (`os-nav/`, `staff/`, `scripts/`) and the [`BADGE-SYSTEM.md`](BADGE-SYSTEM.md) / [`CONTEXT.md`](CONTEXT.md) references.

---

<div align="center">

<sub>© Openline · <a href="https://openline.com">openline.com</a> · Keep this repo <strong>public</strong></sub>

</div>
