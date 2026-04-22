# Shop Assets

Brand collateral for The Scripted Pour.

| File | Purpose | Size (final output) |
|---|---|---|
| `banner-1200x300.svg` | Etsy shop banner (top of shop page) | 1200×300 px |
| `icon-500x500.svg` | Etsy shop icon (profile/thumbnail) | 500×500 px |
| `insert-card-4x6-front.svg` | Packaging insert — front | 4×6 in @ 300 DPI = 1200×1800 px |
| `insert-card-4x6-back.svg` | Packaging insert — back (address / thank-you copy) | 4×6 in @ 300 DPI = 1200×1800 px |

## Exporting

**Etsy assets** (banner + icon): export as PNG at 1× (the viewBox is already the final size).

```bash
inkscape banner-1200x300.svg --export-type=png --export-filename=banner.png
inkscape icon-500x500.svg --export-type=png --export-filename=icon.png
```

**Packaging insert card**: export at 300 DPI as PDF (VistaPrint / Moo both accept PDF directly). If your printer needs PNG, export at the pixel dimensions shown above.

```bash
inkscape insert-card-4x6-front.svg --export-type=pdf --export-filename=insert-front.pdf
inkscape insert-card-4x6-back.svg --export-type=pdf --export-filename=insert-back.pdf
```

## Printing the insert card

Recommended vendors:
- **Moo** — premium paper stock, small batch (50-pack minimum), ~$50 for the batch
- **VistaPrint** — cheaper, larger batch (250-pack+), ~$40
- **GotPrint** — in between

Ask for **4×6 in postcard, double-sided, matte finish, 16pt or heavier cardstock**.
