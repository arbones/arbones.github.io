"""House-style drawing primitives for ADIPOFAT thumbnails and figures.

Colors are sampled from the existing thumbnails, so anything drawn with these
helpers sits next to posts 00-05 without looking imported. Build a Canvas, draw
on it, call save(); rasterization goes through rsvg-convert.

    from house_style import Canvas, THUMB, FIG

    c = Canvas(*THUMB.size, bg=THUMB.bg)
    c.grid(); c.title("The Molecular Microscope", "Spatial transcriptomics ...")
    c.save("thumbnail.svg", png="thumbnail.png")
    c.proof("thumbnail.svg")     # 340px check: does it survive the listing?
"""

import math
import random
import subprocess
from dataclasses import dataclass

FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"


@dataclass(frozen=True)
class Palette:
    size: tuple
    bg: str
    ink: str
    blue: str
    green: str
    gray: str
    grid: str
    panel: str


# flat vector look: thumbnails only
THUMB = Palette(size=(2816, 1536), bg="#fdfdfa", ink="#212a31", blue="#4d85b4",
                green="#73b87f", gray="#d5dbdb", grid="#eceeea", panel="#e6eaec")

# BioRender-adjacent look: in-post figures
FIG = Palette(size=(1800, 1000), bg="#f2f4f6", ink="#2c3e50", blue="#7d9dc4",
              green="#9dbfa4", gray="#c7d0d8", grid="#e4e8ec", panel="#ffffff")

FIG_TINTS = {"cool": "#eaeff7", "warm": "#f3ece2", "sage": "#eaf1ea",
             "lilac": "#ece9f3", "accent": "#e8a05c"}


class Canvas:
    def __init__(self, w, h, bg="#fdfdfa", pal=THUMB):
        self.w, self.h, self.pal = w, h, pal
        self.parts = [f'<rect width="{w}" height="{h}" fill="{bg}"/>']
        random.seed(7)                      # placements stay reproducible

    def add(self, s):
        self.parts.append(s)

    # ---- backdrop ------------------------------------------------------
    def grid(self, x0=640, y0=380, x1=2480, y1=1200, step=190):
        self.add(f'<g stroke="{self.pal.grid}" stroke-width="3">')
        for x in range(x0, x1 + 1, step):
            self.add(f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y1}"/>')
        for y in range(y0, y1 + 1, step):
            self.add(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}"/>')
        self.add('</g>')

    # ---- type ----------------------------------------------------------
    def text(self, x, y, s, size=60, fill=None, weight="normal", anchor="middle"):
        fill = fill or self.pal.ink
        self.add(f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" '
                 f'font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
                 f'fill="{fill}">{s}</text>')

    def title(self, title, subtitle=None, y=188, size=146, sub_size=80):
        self.text(self.w / 2, y, title, size, "#15262d")
        if subtitle:
            self.text(self.w / 2, y + 104, subtitle, sub_size, "#2c3b45")

    def caption(self, x, bold, plain=None, y=1330, size=66):
        """Bold uppercase label under a panel, optional plain line below."""
        self.text(x, y, bold, size, "#15262d", weight="bold")
        if plain:
            self.text(x, y + 94, plain, size - 6, "#2c3b45")

    def banner(self, title, h=86, fill="#4a5f73"):
        """Dark slate title bar across the top; the in-post figure convention."""
        self.add(f'<rect x="0" y="0" width="{self.w}" height="{h}" fill="{fill}"/>')
        self.text(self.w / 2, h * 0.68, title, int(h * 0.44), "#ffffff", weight="bold")

    # ---- shapes --------------------------------------------------------
    def dot(self, x, y, r, fill):
        self.add(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{fill}"/>')

    def panel(self, x, y, w, h, fill=None, stroke=None, rx=18, sw=4):
        fill = fill or self.pal.panel
        stroke = stroke or self.pal.ink
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
                 f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def arrow(self, x0, y0, x1, shaft=116, head=130, head_h=None, fill=None, sw=8):
        """Blunt block arrow pointing right, centered on y0.

        head is the length of the barb, head_h its half-height; keep head_h
        comfortably wider than the shaft or it reads as a thin dart.
        """
        fill = fill or self.pal.panel
        tip, s = x1, shaft / 2
        hh = head_h if head_h is not None else head
        self.add(f'<path d="M {x0} {y0-s} L {tip-head} {y0-s} L {tip-head} {y0-hh} '
                 f'L {tip} {y0} L {tip-head} {y0+hh} L {tip-head} {y0+s} '
                 f'L {x0} {y0+s} Z" fill="{fill}" stroke="{self.pal.ink}" '
                 f'stroke-width="{sw}" stroke-linejoin="round"/>')

    def blob(self, cx, cy, radii, squash=0.76, fill="#f4f6f5", stroke=None, sw=8):
        """Organic closed outline; pass ~10 radii to vary the silhouette."""
        stroke = stroke or self.pal.ink
        pts = []
        for i, r in enumerate(radii):
            a = math.radians(i * 360 / len(radii))
            pts.append((cx + r * math.cos(a), cy + r * squash * math.sin(a)))
        self.add(f'<path d="{_smooth_closed(pts)}" fill="{fill}" stroke="{stroke}" '
                 f'stroke-width="{sw}" stroke-linejoin="round"/>')

    def scatter(self, n, colors, bounds, r=21, gap=58, placed=None):
        """Non-overlapping dots. bounds(rng) -> (x, y) or None to reject."""
        placed = placed if placed is not None else []
        made, guard = 0, 0
        while made < n and guard < 8000:
            guard += 1
            p = bounds(random)
            if p is None:
                continue
            x, y = p
            if any((x - px) ** 2 + (y - py) ** 2 < gap * gap for px, py in placed):
                continue
            placed.append((x, y))
            self.dot(x, y, r, colors[made % len(colors)])
            made += 1
        return placed

    # ---- output --------------------------------------------------------
    def svg(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" '
                f'height="{self.h}" viewBox="0 0 {self.w} {self.h}">\n'
                + "\n".join(self.parts) + "\n</svg>")

    def save(self, svg_path, png=None):
        open(svg_path, "w").write(self.svg())
        if png:
            rasterize(svg_path, png, self.w, self.h)
        return svg_path

    @staticmethod
    def proof(svg_path, png="proof_small.png", width=340):
        """Render at listing size. Look at it: if the captions are mush, redraw."""
        subprocess.run(["rsvg-convert", "-w", str(width), svg_path, "-o", png],
                       check=True)
        return png


def rasterize(svg_path, png_path, w, h):
    subprocess.run(["rsvg-convert", "-w", str(w), "-h", str(h), svg_path,
                    "-o", png_path], check=True)
    return png_path


def _smooth_closed(points):
    """Catmull-Rom through the points, emitted as cubic beziers."""
    n = len(points)
    d = [f'M {points[0][0]:.0f} {points[0][1]:.0f}']
    for i in range(n):
        p0, p1 = points[(i - 1) % n], points[i]
        p2, p3 = points[(i + 1) % n], points[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d.append(f'C {c1[0]:.0f} {c1[1]:.0f} {c2[0]:.0f} {c2[1]:.0f} '
                 f'{p2[0]:.0f} {p2[1]:.0f}')
    return " ".join(d) + " Z"
