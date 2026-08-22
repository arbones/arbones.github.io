"""Worked example: the thumbnail for posts/05.clinicalApplications.

Run it to see the house style assembled end to end, then adapt the middle
section for the new post. The shape of the argument is always the same: a
left panel, an arrow, a right panel, two captions.

    python3 example_thumbnail.py            # writes thumbnail.svg + .png here
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from house_style import THUMB, Canvas                       # noqa: E402

c = Canvas(*THUMB.size, bg=THUMB.bg)
c.grid()
c.title("The Molecular Microscope",
        "Spatial transcriptomics in clinical research")

# left: homogenate, every transcript stripped of its address
TX, TW, TOP, BOT = 470, 440, 545, 1165
c.add(f'<path d="M {TX} {TOP} L {TX} {BOT-90} Q {TX} {BOT} {TX+90} {BOT} '
      f'L {TX+TW-90} {BOT} Q {TX+TW} {BOT} {TX+TW} {BOT-90} L {TX+TW} {TOP} Z" '
      f'fill="#eef1f1" stroke="{THUMB.ink}" stroke-width="8" stroke-linejoin="round"/>')
c.panel(TX - 34, TOP - 56, TW + 68, 56, fill=THUMB.panel, rx=14, sw=8)


def in_tube(rng):
    x = rng.uniform(TX + 52, TW + TX - 52)
    y = rng.uniform(TOP + 70, BOT - 58)
    if y > BOT - 120 and abs(x - (TX + TW / 2)) > TW / 2 - 70:
        return None
    return x, y


c.scatter(44, [THUMB.blue, THUMB.green, THUMB.gray], in_tube, gap=54)

# middle: the chemistry that keeps the address
c.arrow(1230, 828, 1650)
c.text(1440, 1058, "IN SITU", 56, "#2c3b45")

# right: the same molecules, still in place
CX, CY = 2140, 828
c.blob(CX, CY, [432, 408, 425, 396, 418, 404, 430, 400, 422, 410])
c.add(f'<circle cx="{CX}" cy="{CY}" r="196" fill="#e3ecf3" '
      f'stroke="{THUMB.blue}" stroke-width="7"/>')
c.add(f'<circle cx="{CX}" cy="{CY}" r="272" fill="none" stroke="{THUMB.green}" '
      f'stroke-width="7" stroke-dasharray="26 22"/>')

ring = lambda lo, hi, sq=1.0: (lambda rng: (
    CX + (r := rng.uniform(lo, hi)) * math.cos(a := rng.uniform(0, 2 * math.pi)),
    CY + r * sq * math.sin(a)))

placed = c.scatter(15, [THUMB.blue], ring(0, 150), gap=62)
placed = c.scatter(18, [THUMB.green], ring(224, 258), gap=62, placed=placed)
c.scatter(11, [THUMB.gray], ring(310, 392, 0.74), gap=66, placed=placed)

c.caption(TX + TW / 2, "BULK RNA-SEQ", "location lost")
c.caption(CX, "SPATIAL RNA-SEQ", "location retained")

here = Path(__file__).parent
c.save(str(here / "thumbnail.svg"), png=str(here / "thumbnail.png"))
print("wrote", here / "thumbnail.png")
print("proof:", Canvas.proof(str(here / "thumbnail.svg"),
                             str(here / "thumbnail_340.png")))
