# Launch Runbook — From Zero to Live Etsy Shop

Do these in order. Expect **6–10 hours total** to get the shop live. Don't skip the export step — it's the piece most likely to derail you.

---

## Phase 0 — Accounts (≤30 min)

### 0.1 Etsy seller account
- Go to `etsy.com/sell`
- Sign up as a seller (you can use a personal Etsy account if you have one, but a fresh dedicated email is cleaner)
- Set shop name (see `05-shop-identity.md` — verify it's available first)
- Set shop currency (USD) + language (English) + country
- Skip the "first listing" flow for now — we'll list via Printify
- Payment: Etsy Payments. Enter bank info.
- Bill info: Etsy charges a $0.20 listing fee per listing + fees on sales

### 0.2 Printify account
- Go to `printify.com`
- Sign up, confirm email
- **Connect to Etsy:** Settings → Shops → Connect → Etsy → authorize

### 0.3 Google Fonts download (needed for exports)

Download these 4 fonts as TTF/OTF for use in your design tool:
- **Playfair Display** (Regular, Bold, Black, Italic, Black Italic)
- **IM Fell English** (Regular, Italic)
- **Cinzel** (Regular, Bold)
- **Rye** (Regular)

Source: `fonts.google.com` — each has a "Download family" button. Install into your OS.

---

## Phase 1 — Export SVGs to PNG (1–2 hours, the critical step)

The SVGs in `mockups/` are the designs. Printify needs PNGs at 300 DPI at the final print size.

### Recommended tool: **Inkscape** (free, Mac/Windows/Linux)

Download at `inkscape.org`. Install. Then for each sign:

1. Open the `.svg` in Inkscape
2. File → Export (or `Shift + Cmd/Ctrl + E`)
3. Export area: **Document**
4. DPI: **300**
5. For 11×14 portrait signs, Inkscape will compute pixels automatically (3375 × 4275 at 300 DPI if the SVG viewBox is 1100×1400 — which it is). **Verify** the pixel dimensions match the table in `06-printify-product-spec.md`.
6. Export as PNG → save to `mockups/exports/` as e.g. `lloyd-11x14.png`
7. Repeat for each size you want (8×10, 16×20) — resize the Inkscape document page to the corresponding aspect ratio and re-export, or just export the same file at 3 different DPIs (for same aspect): 228 DPI for 8×10, 300 DPI for 11×14, 436 DPI for 16×20

### Alternative: **Affinity Designer** or **Adobe Illustrator**
Same idea. Open SVG, export as PNG at 300 DPI at exact pixel size.

### Alternative: **Figma** (free)
- Import SVG into Figma
- Select frame → Export → 3x PNG (gives 3300×4200 for 1100×1400 SVG — close to 300 DPI for 11×14)

### What NOT to do
- ❌ Don't screenshot from browser — not high enough DPI
- ❌ Don't use a free online "SVG to PNG" converter — they strip custom fonts

### Sanity check before uploading to Printify
For each PNG:
- Open it and zoom to 100% — should look crisp, not pixelated
- Right-click → Properties (Windows) / Cmd+I (Mac) — confirm pixel dimensions match the table

---

## Phase 2 — Set up first Printify product (30 min)

Work through **one** sign end-to-end first. I recommend **Lloyd's** (`sample-02-lloyd-shining.svg`) — most iconic, validates the flow.

1. Printify → Catalog → Wall Decor → **Wood Prints** / **Wooden Wall Art**
2. Pick a provider (read the provider review stars; US-based preferred)
3. Click **Start Designing**
4. Upload your `lloyd-11x14.png` for the 11×14 variant
5. Check the preview — ensure nothing is clipped at the bleed
6. Repeat for 8×10 and 16×20 variants (upload the corresponding PNG)
7. Set retail prices per `06-printify-product-spec.md`
8. **Save as draft** in Printify
9. **Publish to Etsy** → this creates the Etsy listing as a draft

---

## Phase 3 — Flesh out the Etsy listing (20 min per sign)

After Printify pushes a draft to Etsy, go to Etsy → Listings → find the draft.

### What Printify pre-fills
- Title (generic — you'll rewrite)
- Description (generic — you'll rewrite)
- Photos (Printify mockups — usable)
- Variants (sizes — should be correct)

### What you'll replace from `08-etsy-listings.md`
- **Title** (140 char limit — SEO-optimized)
- **Description** (the whole thing)
- **Tags** (13 tags, front-loaded for search)
- **Category** — "Home & Living > Home Décor > Signs"
- **Attributes:**
  - Primary color: Brown
  - Orientation: Portrait / Landscape / Square
  - Room: Home Bar / Man Cave / Game Room
  - Occasion: Housewarming, Father's Day, Birthday, Christmas

### Photos (order matters — first is the thumbnail)
1. Front-on clean shot of the sign on a wood wall (Printify's mockup)
2. In-context: above a home bar (Printify has "scene" mockups)
3. Close-up detail of typography
4. Size comparison (three sizes shown to scale)
5. Packaging / included-hardware shot
6. (optional) Second in-context scene

For launch, use Printify's mockups as-is. Once you have sales, replace with real photography.

### Before publishing the listing
- Preview on Etsy
- Check on mobile preview (most Etsy traffic is mobile)
- Hit Publish ($0.20 listing fee charged)

---

## Phase 4 — Repeat Phase 2–3 for the other 8 signs (4–6 hours)

Batch the work:
1. Export **all 9 SVGs** to **all 3 sizes each** first (27 PNGs total). Done in one Inkscape session, saves context-switching.
2. Then batch **Printify product creation** (9 products).
3. Then batch **Etsy listing cleanup** (9 listings).

**Working order** — do these signs in this sequence:

| Order | Sign | Why first/middle/last |
|---|---|---|
| 1 | Lloyd (`sample-02`) | Validates the flow — iconic, classic layout |
| 2 | Casablanca gin joints (`sample-04`) | Best SEO words ("gin joint sign") |
| 3 | Tombstone (`sample-03`) | Tests Style B (exposed pine) |
| 4 | Bond martini (`sample-06`) | Minimal — easy to verify alignment |
| 5 | Dalton's Rules (`sample-01`) | Square format test |
| 6 | Animal House (`sample-05`) | |
| 7 | Sideways Merlot (`sample-07`) | |
| 8 | The Dude (`sample-08`) | |
| 9 | Ferris Bueller (`sample-09`) | Landscape — different shipping box |

---

## Phase 5 — Shop setup before going live (1 hour)

Before you flip the "Open Shop" switch, finish these on Etsy:

### 5.1 Shop announcement
Short message at the top of the shop page. Use the tagline from `05-shop-identity.md`.

### 5.2 Shop policies
Copy from `09-shop-policies.md`:
- Shipping policy (processing 3–5 days, US free, Canada $8)
- Returns (within 14 days, restocking fee for personalization)
- Production disclaimer (made to order)

### 5.3 About section
Copy the bio from `05-shop-identity.md`.

### 5.4 Banner + shop icon
- **Shop icon:** 500×500 — simple wordmark on walnut
- **Banner:** 1200×300 — wider version of same

(You can ship without these and add them week 2.)

### 5.5 Featured listings
Pin the 3–4 strongest at the top of your shop (drag-reorder in Etsy):
1. Lloyd's (visual impact)
2. Casablanca gin joints (search volume)
3. Dalton's Rules (rules-sign format demonstrates range)
4. Bond martini (broadest appeal)

---

## Phase 6 — Publish + first orders (ongoing)

- **Publish** all 9 listings → shop is live
- **Share** once on a personal channel — Instagram story, close friends, that's it. Don't do paid ads yet.
- **Wait for first real order.** Critical: when it comes in, let Printify fulfill, then **check the received product yourself** if possible (ship a test order to yourself as customer #1). This catches bleed/alignment issues before a stranger buys.

---

## Post-Launch — Week 1 checklist

- [ ] Place a test order to yourself — inspect quality of the first physical sign
- [ ] If quality is good: leave a review on your own listing? NO — against Etsy TOS. Ask a friend to buy instead.
- [ ] Monitor Etsy stats for which listings get views vs favorites vs purchases
- [ ] Respond to every message within 4 hours — Etsy rewards fast response time in search ranking
- [ ] After ~10 sales, start planning Wave 2 (more designs + possibly Manufacturing Partner upgrade)

---

## Common first-launch mistakes to avoid

- **Pricing too low.** You can always discount later; you can't raise without losing early buyers.
- **Too many tags repeating the same word.** Etsy uses tag variety for matching. "bar sign" + "home bar decor" + "whiskey bar" > three tags all saying "bar sign."
- **Generic titles.** "Bar Sign" is dead. "Movie Quote Bar Sign - Gin Joint Print on Rustic Wood - Casablanca Quote Wall Art for Home Bar" ranks.
- **Fulfillment backlog.** Don't list more than you can service. 9 signs is plenty for launch.
- **Ignoring messages.** Etsy tracks response time; slow responses hurt ranking.
