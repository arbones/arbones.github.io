"""The shared thumbnail for every ADIPOFAT source digest.

Digests are a recurring series, so they share one masthead rather than getting a
new drawing each week. The argument is the one a digest always makes: a wide
sweep of journals, preprints and blogs on the left, a handful of items worth
reading on the right. Nothing here is dated, so the same image serves any week.

    python3 digest_thumbnail.py

Writes assets/digest_thumbnail.svg and .png at the repo root. Copy the png into
the new posts/NN.digestYYYYMMDD/ folder as thumbnail.png.
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from house_style import THUMB, Canvas                        # noqa: E402

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)

c = Canvas(*THUMB.size, bg=THUMB.bg)
c.grid()
c.title("ADIPOFAT Source Digest",
        "The week in omics, spatial biology and data science")

TOP, HEIGHT = 545, 620

# left: everything published this week, undifferentiated
LX, LW = 300, 980
c.panel(LX, TOP, LW, HEIGHT, fill="#ffffff", rx=22, sw=8)
c.panel(LX, TOP, LW, 62, fill=THUMB.panel, rx=22, sw=8)
c.add(f'<rect x="{LX + 8}" y="{TOP + 40}" width="{LW - 16}" height="26" '
      f'fill="#ffffff"/>')
c.add(f'<line x1="{LX}" y1="{TOP + 62}" x2="{LX + LW}" y2="{TOP + 62}" '
      f'stroke="{THUMB.ink}" stroke-width="8"/>')

field = lambda rng: (rng.uniform(LX + 58, LX + LW - 58),
                     rng.uniform(TOP + 130, TOP + HEIGHT - 58))
c.scatter(96, [THUMB.gray, THUMB.blue, THUMB.gray, THUMB.green, THUMB.gray],
          field, r=17, gap=46)

# middle: the only work a digest actually does
c.arrow(1400, TOP + HEIGHT / 2, 1810)
c.text(1605, TOP + HEIGHT / 2 + 230, "READ AND SIFT", 56, "#2c3b45")

# right: the few items that survive it
RX, RW = 1980, 540
c.panel(RX, TOP, RW, HEIGHT, fill="#eef5ef", stroke=THUMB.green, rx=22, sw=8)

keeps = [(0.28, 0.24, THUMB.blue), (0.64, 0.37, THUMB.green),
         (0.28, 0.56, THUMB.green), (0.64, 0.69, THUMB.blue),
         (0.28, 0.88, THUMB.gray)]
for fx, fy, color in keeps:
    x, y = RX + fx * RW, TOP + fy * HEIGHT
    c.dot(x, y, 34, color)
    c.add(f'<line x1="{x + 62}" y1="{y - 12}" x2="{x + 118}" y2="{y - 12}" '
          f'stroke="{THUMB.gray}" stroke-width="14" stroke-linecap="round"/>')
    c.add(f'<line x1="{x + 62}" y1="{y + 22}" x2="{x + 92}" y2="{y + 22}" '
          f'stroke="{THUMB.gray}" stroke-width="14" stroke-linecap="round"/>')

c.caption(LX + LW / 2, "THE FULL SWEEP", "journals, preprints, blogs")
c.caption(RX + RW / 2, "THE DIGEST", "what earned your time")

svg = c.save(str(OUT / "digest_thumbnail.svg"),
             png=str(OUT / "digest_thumbnail.png"))
c.proof(svg, png=str(OUT / "digest_thumbnail_proof.png"))
print(f"wrote {OUT / 'digest_thumbnail.png'}")
