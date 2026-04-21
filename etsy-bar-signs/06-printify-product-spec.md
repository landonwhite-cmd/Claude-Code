# Printify Product Spec — Wave 1 Launch

The exact Printify product(s) to set up, with pricing and design file requirements.

---

## Product Choice

**Use: "Wood Prints" / "Printed Wood Wall Art"** from Printify.

Specifically, look for the provider **"Eco Products Wall Art"** or **"Artsadd"** in Printify's catalog. Filter by:
- Category: Wall Decor → Wood Signs / Wood Prints
- Material: Birch plywood, HDF with real wood veneer, or pine
- Sort by provider reviews — pick a US-based provider with >4.5 star provider rating to minimize shipping time

### Why this product

- Real wood substrate (birch/pine panels, not MDF with wood-print paper)
- UV-printed — the print is durable, not a decal
- Pre-drilled keyhole mount or sawtooth hanger included
- Ships in 3–5 business days from US
- Multiple sizes available

### Sizes to offer per listing

For consistency across the shop, offer **3 sizes per sign**:

| Size | Orientation | Printify cost (typical) | Retail | Margin |
|---|---|---|---|---|
| 8×10" | portrait | $14–18 | **$29** | ~$8–12 |
| 11×14" | portrait | $18–24 | **$42** | ~$14–20 |
| 16×20" | portrait | $28–35 | **$62** | ~$22–29 |

For **landscape signs** (Ferris Bueller, the long-quote ones), offer:
- 12×8" ($29), 18×12" ($42), 24×18" ($72)

For **square signs** (Dalton's Rules, The Dude):
- 10×10" ($29), 12×12" ($42), 16×16" ($62)

**Prices include Etsy fees baked in. Margin assumes free shipping (built into retail).**

---

## Printify Setup Steps

### 1. Account + Etsy connection
- Printify → Connect → Etsy → authorize
- Go through their "new seller" flow

### 2. Create first product
- Catalog → Wall Decor → Wood Prints
- Pick the provider (see above)
- Click "Start Designing"

### 3. Upload design file for Sign #1 (example: Lloyd's)
- Upload the 300 DPI PNG for the 11×14 size (see export guide in `07-launch-runbook.md`)
- Printify shows preview — adjust if there's bleed clipping
- Save variant

### 4. Add other sizes as variants
- Same product listing, different sizes
- Upload separate PNG file for each (at matching DPI and dimensions)
- 8×10 PNG: 2475×3075 px @ 300 DPI
- 11×14 PNG: 3375×4275 px
- 16×20 PNG: 4875×6075 px

### 5. Set retail prices
- Enter retail per size (see pricing table above)
- Printify calculates your profit — confirm margin looks right

### 6. Publish to Etsy
- Title, description, tags come from your per-sign listing copy (see `08-etsy-listings.md`)
- Images: Printify auto-generates mockups — replace with your own once you're comfortable
- Publish as **Draft** first, review on Etsy side, then activate

---

## Design File Requirements (Printify)

**Per Printify's spec:**

- **File format:** PNG (preferred) or JPG
- **Resolution:** 300 DPI minimum at final size
- **Color mode:** RGB (sRGB color profile)
- **Max file size:** 50 MB
- **Bleed:** Printify shows a bleed guide in their designer — leave your key content within the "safe zone" indicated
- **Background:** Make sure your background color/texture fills the entire file — **don't leave transparent edges** unless you want the wood to show through (Style B signs)

### Specific pixel dimensions (ready to export)

| Sign | Size | Pixel dimensions |
|---|---|---|
| Portrait signs | 8×10 | 2475×3075 |
| | 11×14 | 3375×4275 |
| | 16×20 | 4875×6075 |
| Landscape (Ferris) | 12×8 | 3675×2475 |
| | 18×12 | 5475×3675 |
| | 24×18 | 7275×5475 |
| Square (Dalton's, Dude) | 10×10 | 3075×3075 |
| | 12×12 | 3675×3675 |
| | 16×16 | 4875×4875 |

*All dimensions include ~0.125" bleed on each side — Printify trims.*

---

## Shipping Config

- **Profile:** "Free shipping" baked into retail (US buyers love this and Etsy's algorithm rewards it)
- **Processing time:** Set to **3–5 business days** (Printify production time)
- **Ship to:** US + Canada for launch. Add UK/EU once you've shipped ~20 orders.

---

## Cost / Margin Sanity Check

On a 11×14 Lloyd's sign at $42 retail:

| Item | $ |
|---|---|
| Retail | 42.00 |
| Printify cost (incl. shipping) | -22.00 |
| Etsy transaction fee (6.5%) | -2.73 |
| Etsy payment processing (3% + $0.25) | -1.51 |
| Etsy listing fee (amortized) | -0.20 |
| **Net profit** | **~15.56** |

**~37% margin.** Acceptable for launch tier. Premium tier (Wave 2 real-wood upgrade) will target ~55%.

---

## Once Printify is Set Up

Produce the 9 signs as 9 Printify listings, each with 3 sizes, and push all to Etsy. See `07-launch-runbook.md` for the exact sequence.
