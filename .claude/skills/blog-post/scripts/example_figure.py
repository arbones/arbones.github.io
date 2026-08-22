"""Worked example: an in-post figure in the ADIPOFAT figure style.

The figures in posts 03-05 are two-column comparisons or numbered stage flows
under a dark slate banner, drawn on tinted panels with labeled elements. This
builds the comparison variant. For a stage flow, drop three panels in a row and
join them with c.arrow().

    python3 example_figure.py               # writes figure.svg + .png here
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from house_style import FIG, FIG_TINTS, Canvas                # noqa: E402

c = Canvas(*FIG.size, bg=FIG.bg, pal=FIG)
c.banner("What Normalization Removes, and What It Should Not")

L, R, TOP, PH = 40, 920, 130, 820
c.panel(L, TOP, 840, PH, fill=FIG_TINTS["cool"], stroke="#c8d3e2", rx=14, sw=3)
c.panel(R, TOP, 840, PH, fill=FIG_TINTS["sage"], stroke="#c2d4c6", rx=14, sw=3)
c.text(L + 420, TOP + 66, "Standard Pipeline", 40, FIG.ink, weight="bold")
c.text(R + 420, TOP + 66, "Spatially Aware", 40, FIG.ink, weight="bold")

# left: a density gradient scaled flat, biology and all
for i in range(6):
    shade = ["#3f6ea8", "#5b86bd", "#7d9dc4", "#9db4d2", "#bccbe0", "#dbe3ee"][i]
    c.panel(L + 90 + i * 110, TOP + 150, 92, 200, fill=shade, stroke="none", rx=8, sw=0)
c.text(L + 420, TOP + 400, "regional library size", 30, "#44566b")
c.arrow(L + 250, TOP + 470, L + 590, shaft=34, head=44, head_h=44, fill="#ffffff", sw=3)
for i in range(6):
    c.panel(L + 90 + i * 110, TOP + 540, 92, 200, fill="#9db4d2", stroke="none", rx=8, sw=0)
c.text(L + 420, TOP + 790, "gradient gone, signal with it", 32, FIG.ink, weight="bold")

# right: the technical part removed, the anatomy kept
for i in range(6):
    shade = ["#3f6ea8", "#5b86bd", "#7d9dc4", "#9db4d2", "#bccbe0", "#dbe3ee"][i]
    c.panel(R + 90 + i * 110, TOP + 150, 92, 200, fill=shade, stroke="none", rx=8, sw=0)
c.text(R + 420, TOP + 400, "regional library size", 30, "#44566b")
c.arrow(R + 250, TOP + 470, R + 590, shaft=34, head=44, head_h=44, fill="#ffffff", sw=3)
for i in range(6):
    shade = ["#4a7d55", "#6b9c73", "#8bb492", "#a8c7ad", "#c4d8c8", "#dfe9e1"][i]
    c.panel(R + 90 + i * 110, TOP + 540, 92, 200, fill=shade, stroke="none", rx=8, sw=0)
c.text(R + 420, TOP + 790, "anatomy preserved", 32, FIG.ink, weight="bold")

here = Path(__file__).parent
c.save(str(here / "figure.svg"), png=str(here / "figure.png"))
print("wrote", here / "figure.png")
