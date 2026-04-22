# Design System — Navy Framed Panels

The visual rules every sign in the Wave 1 launch collection follows. Goal: a **cohesive brand** that matches the existing Coughlin's Law sign (the anchor product) so the shop looks like one intentional collection.

> **Substrate pivot, April 2026.** We pivoted from rustic wood to navy framed panels after the user's existing Coughlin's Law turned out to be a printed navy panel in a thin black frame, not wood. That aesthetic is more Etsy-friendly, higher-margin, and more giftable. The rustic-wood system is preserved in `wave-2-premium-wood/` for the future premium tier.

---

## Aesthetic Mood Board (in words)

Think: **1920s speakeasy menu card, framed and hung behind the bar.**

- Midnight navy panel inside a thin black frame
- Warm cream ink — printed, not embossed
- Restrained stepped art-deco border
- Serif slab title in the Limelight / Copperplate family
- Handwritten script body (Caveat) that reads like a bartender's notebook
- No distressing, no textures — clean, high-contrast, gallery-ready

**Reference brands to emulate:** Death & Co menu design, Dante NYC, Employees Only menu cards, Art Deco hotel signage (The Beekman, The Greenbrier)

**Reference brands to avoid:** Rustic-wood farmhouse decor, cricut-cut vinyl signs, neon bar signs, distressed-metal "man cave" aesthetic

---

## Color Palette

### Base (use on every sign)

| Role | Hex | Name | Notes |
|---|---|---|---|
| Panel navy | `#1A2238` | Midnight | Primary background — every sign |
| Ink cream | `#F2E4C4` | Parchment | Primary lettering, border, all ornaments |
| Frame black | `#0A0A0A` | Frame Black | Not printed on sign — the physical frame |

That's it. Single-color ink. No per-genre accents. Consistency is the brand.

---

## Typography

### Fonts (all free/open-license on Google Fonts)

| Use | Font | Why |
|---|---|---|
| **Title / section headers** | **Limelight** | Art-deco slab serif, wide tracking, gallery-menu feel |
| **Body / quote text** | **Caveat** (600 weight) | Handwritten script, upright, bartender's-notebook energy |
| **Attribution / small caps** | **Cinzel** (600 weight) | Engraved small-caps Roman, anchors the composition |
| **Numerals (rules signs)** | **Cinzel** (700 weight) | I. II. III. in tracked small caps |
| **Accent word (oversized)** | **Limelight** at 120–180pt | For single-word emphasis: "HEAVILY.", "MERLOT." |

### Type rules

- **Never mix more than 3 fonts** on a single sign (Limelight + Caveat + Cinzel)
- **Body is the hero** — largest Caveat at 70–100pt
- **Attribution** is Cinzel small caps, 20–26pt, letter-spacing +10
- **Rules signs use titles.** Single-quote signs do not — go straight from ornament (if any) to quote.

---

## Layout Grid

### Standard proportions

- **Safe area:** inner ~85% of canvas
- **Border:** stepped art-deco frame at ~8% inset, with decorative center notches on each edge and angled outer corner brackets
- **Inner rectangle:** plain single-line at ~10% inset, creates the double-line effect
- **Quote zone:** centered, takes 50–60% of vertical height
- **Attribution zone:** bottom ~10%, above a horizontal rule

### Orientations

| Orientation | Use for |
|---|---|
| **11×14 portrait** | Default — most signs |
| **12×12 square** | Short quotes (Dalton's Rules, The Dude) |
| **12×18 landscape** | Long quotes (Ferris Bueller, Blues Brothers in Wave 2) |

---

## The Art-Deco Border

Every sign uses the same border system so the collection reads as a set.

### Structure (portrait 1100×1400 example)
- Outer line: 4 path segments (one per edge) with:
  - Small center notches (step up–over–down) at the midpoint of each edge
  - Angled outer corner brackets at each corner
- Inner line: plain rectangle at +20–25px inset
- All strokes cream `#F2E4C4`, 0.8–1.5px weight

### Structure (square 1200×1200 and landscape 1800×1200)
Same pattern, notch positions scaled proportionally. Reference implementations in `sign-08-dude-abides.svg` and `sign-09-ferris-bueller.svg`.

---

## Ornaments (use sparingly)

Each sign may include at most one small ornament at the top (optional). All ornaments are monochrome cream stroke.

| Ornament | Use on |
|---|---|
| 5-point star | Tombstone |
| Martini glass outline | Bond |
| Wine bottle + glass outline | Sideways |
| Art-deco fan | Casablanca |
| Rug-pattern chevron | The Dude |

Signs with no ornament: Dalton's Rules, Lloyd's, Animal House, Ferris Bueller, Coughlin's Law. The typography and border do the work.

---

## Composition Rules

1. **One focal point per sign.** Either the quote (most signs) or the oversized accent word (Animal House, Sideways).
2. **Generous whitespace.** When in doubt, make the quote smaller.
3. **Symmetrical composition only.** Everything centered.
4. **Ornaments are earned.** Most signs don't need one.
5. **Attribution is always Cinzel small caps,** anchored by a horizontal rule above.
6. **No movie titles on the sign.** Ever — attribute to character + plausible venue.
7. **No narrator lead-ins** ("— A REMINDER —", "— ON THE HOUSE —", etc.). Ornament directly to quote.
8. **No color beyond cream on navy.** Discipline — no oxblood, no gold, no per-genre accents in Wave 1.

---

## Printify Production Specs

For Printify's framed-poster products (paper print in a thin black frame):

- **Resolution:** 300 DPI at final print size
- **Color profile:** sRGB
- **File format:** PNG (preferred) or JPG
- **Bleed:** 0.125" on all sides
- **Safe area:** 0.25" from edge
- **Background:** Solid navy fills the entire print — no transparent edges

### Design file sizes (pixels at 300 DPI, matching print size)

| Sign size | Pixel dimensions (w/ bleed) |
|---|---|
| 8×10 portrait | 2475×3075 px |
| 11×14 portrait | 3375×4275 px |
| 12×12 square | 3675×3675 px |
| 12×18 landscape | 5475×3675 px |
| 16×20 portrait | 4875×6075 px |

---

## Wave 2 — Premium Rustic Wood (future)

Once Wave 1 reveals which quotes sell, the winners get a premium-tier companion SKU: real stained oak or pine, hand-painted or laser-engraved lettering, sold $75–$100 via an Etsy Manufacturing Partner. The original rustic-wood designs in `mockups/wave-2-premium-wood/` are the starting point for those — they'll need slight adaptation for real-wood production but the composition transfers.

---

## Brand Preview

Files with brand-level details:
- **Shop name:** The Scripted Pour — *"Where the movies meet the bar."* (see `05-shop-identity.md`)
- **Voice:** smart bartender who's seen every movie, not fan-merch seller
- **Packaging concept:** kraft cardboard + twine + a printed insert card (draft in `05-shop-identity.md`)
