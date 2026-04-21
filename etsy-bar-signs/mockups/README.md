# Mockups

## Viewing

Open any `.svg` file in a web browser (Chrome, Safari, Firefox) to see it rendered with the real Google Fonts and wood-grain filters. The fonts load from `fonts.googleapis.com` so you need internet on first view.

## What's here

### Wave 1 (launch collection — 9 of 10 below, Coughlin's Laws uses the existing sign)

| File | Sign | Style | Size |
|---|---|---|---|
| `sample-01-daltons-rules.svg` | Dalton's Rules (R2) | A — dark walnut | 12×12 square |
| `sample-02-lloyd-shining.svg` | Lloyd "Your money's no good here" (#2) | A — dark walnut | 11×14 portrait |
| `sample-03-tombstone.svg` | Tombstone "Hell's coming with me" (#7) | B — exposed pine | 11×14 portrait |
| `sample-04-casablanca-gin-joints.svg` | Casablanca "Of all the gin joints" (#12) | A — dark walnut + art deco | 11×14 portrait |
| `sample-05-animal-house.svg` | Animal House "start drinking heavily" (#3) | A — dark walnut | 11×14 portrait |
| `sample-06-bond-martini.svg` | Bond "Vodka martini. Shaken, not stirred." (#9) | A — dark walnut | 11×14 portrait |
| `sample-07-sideways-merlot.svg` | Sideways Merlot (#8) | A — dark walnut + oxblood | 11×14 portrait |
| `sample-08-dude-abides.svg` | The Dude abides (#14) | B — exposed pine | 12×12 square |
| `sample-09-ferris-bueller.svg` | Ferris Bueller "Life moves pretty fast" (#11) | B — exposed pine | 12×18 landscape |

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
