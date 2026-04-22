# Mockups

## Viewing

Open any `.svg` file in a web browser (Chrome, Safari, Firefox). The fonts load from Google Fonts — need internet on first view. GitHub strips remote fonts for security, so GitHub's SVG preview won't be accurate — download and open locally for the real look.

## Wave 1 — Launch Collection (Navy Framed Panels)

The aesthetic matches the user's existing Coughlin's Law sign: midnight navy substrate, warm cream ink, stepped art-deco border, Limelight serif titles, Caveat handwritten body. Printed on paper, shipped in a thin black frame via Printify's framed-poster product.

| File | Sign | Size | Layout |
|---|---|---|---|
| `sign-01-daltons-rules.svg` | Dalton's Rules | 11×14 portrait | Rules-list format with title |
| `sign-02-lloyd.svg` | Lloyd "Your money's no good here" | 11×14 portrait | Quote + attribution |
| `sign-03-tombstone.svg` | Tombstone "Hell's coming with me" | 11×14 portrait | Quote + small-star ornament |
| `sign-04-casablanca-gin-joints.svg` | Casablanca "Of all the gin joints" | 11×14 portrait | Quote + art-deco fan |
| `sign-05-animal-house.svg` | Animal House "start drinking heavily" | 11×14 portrait | Quote + oversized "HEAVILY." accent |
| `sign-06-bond-martini.svg` | Bond "Shaken, not stirred" | 11×14 portrait | Quote + martini-glass ornament |
| `sign-07-sideways-merlot.svg` | Sideways Merlot | 11×14 portrait | Quote + wine-bottle/glass + oversized "MERLOT." |
| `sign-08-dude-abides.svg` | The Dude abides | 12×12 square | Big quote + rug-pattern divider |
| `sign-09-ferris-bueller.svg` | Ferris Bueller | 12×18 landscape | Long-quote landscape layout |
| `sign-10-coughlins-law.svg` | Coughlin's Law (anchor) | 12×16 portrait | 9-rule list matching the user's existing physical sign |

## Shop Assets

Brand collateral for Etsy setup + packaging. See `shop-assets/README.md`.

- `shop-assets/banner-1200x300.svg` — Etsy shop banner
- `shop-assets/icon-500x500.svg` — Etsy shop icon
- `shop-assets/insert-card-4x6-front.svg` — packaging insert, front
- `shop-assets/insert-card-4x6-back.svg` — packaging insert, back

## Wave 2 — Premium Rustic Wood (deferred)

Original rustic-wood designs are archived in `wave-2-premium-wood/`. They'll be revived when we upgrade winning quotes to the Etsy Manufacturing Partner premium tier (real wood, painted/engraved lettering, $75–$100 price point).

## Exporting for Printify

Each SVG exports to PNG at 300 DPI using Inkscape, Affinity Designer, or Illustrator. Pixel dimensions per size are documented in `../06-printify-product-spec.md`.

Quick command (Inkscape CLI):

```bash
inkscape sign-02-lloyd.svg --export-type=png --export-dpi=300 --export-filename=sign-02-lloyd-11x14.png
```
