# Mockups

## Viewing

Open any `.svg` file in a web browser (Chrome, Safari, Firefox) to see it rendered with the real Google Fonts and wood-grain filters. The fonts load from `fonts.googleapis.com` so you need internet on first view.

## What's here

| File | Sign | Style | Purpose |
|---|---|---|---|
| `sample-01-daltons-rules.svg` | Dalton's Rules (R2) | Style A — full dark walnut stain | Validates rules-sign format |
| `sample-02-lloyd-shining.svg` | Lloyd "Your money's no good here" (#2) | Style A — full dark walnut stain | Validates horror/classy vibe |
| `sample-03-tombstone.svg` | Tombstone "Hell's coming with me" (#7) | Style B — exposed pine grain | Validates western / light-wood variant |

## Exporting for Printify (once we finalize)

SVG → PNG at 300 DPI, using **Inkscape** (free):

```bash
inkscape sample-02-lloyd-shining.svg --export-type=png --export-dpi=300 --export-filename=lloyd-11x14.png
```

Or via **ImageMagick** (quick preview, less accurate for fonts):

```bash
convert -density 300 -background white sample-02-lloyd-shining.svg lloyd-11x14.png
```

Final print files will be sized per `04-design-system.md` → "Design file sizes" table.

## Feedback I need from you

For each of the three samples:
1. Does the **vibe** land? (classy rustic, not farmhouse/cricut)
2. Is the **legibility** right? Too big / too small / hierarchy clear?
3. Are the **attributions** right? (e.g. "AS LAID DOWN AT THE DOUBLE DEUCE" for Dalton's — yes / too cute / change to what?)
4. Style A (dark stain) vs Style B (exposed grain) — which do you prefer overall?
5. Any font changes? (Playfair / IM Fell / Cinzel / Rye)
