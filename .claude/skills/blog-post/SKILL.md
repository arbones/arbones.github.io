---
name: blog-post
description: Scaffold and write a new ADIPOFAT blog post - creates the numbered posts/NN.slug/ folder, the index.qmd with correct front matter, two in-post figures, and one thumbnail in the established house style, then renders the site. Use whenever the user wants to start, draft, write, or add a blog post, a new entry, or "the next post" for this Quarto blog.
---

# New ADIPOFAT blog post

Every post is a folder under `posts/` holding `index.qmd`, exactly **two figures**, and
**one thumbnail**. Nothing else. The voice, the figure look, and the thumbnail look are
already fixed by posts 00-05; the job is to extend that set, not to reinvent it.

Read `reference/voice.md` before writing any prose. Read the two scripts in `scripts/`
before drawing anything.

## 1. Gather the inputs

Ask only for what is missing, in one round: title, subtitle, topic or source material,
and categories. Everything else is derivable. If the user hands over a paper, a set of
notes, or an analysis, that is the source material; do not invent findings around it.

Categories follow the existing vocabulary where it fits: `SingleCell`, `SRT`,
`Normalization`, `omics`, `bioinformatics`, `Claude`, `AI`, `Writing`, `Quarto`,
`GitHub`, `Repository`, `excel`, `data-wrangling`, `introduction`,
`Clinical-Applications`. Two or three per post.

## 2. Scaffold the folder

Number is the highest existing prefix plus one, zero padded. Slug is short and
descriptive, matching the existing mix of styles (`excel`, `awesomeSC`, `AIwriting`,
`Lying1`, `clinicalApplications`).

```bash
ls posts/                                   # find the highest NN
mkdir -p posts/06.yourSlug
```

Front matter, exactly this shape and key order, with today's date in ISO form:

```yaml
---
title: Your Title Without Quotes Unless It Contains A Colon
subtitle: One line that says what the reader gets, lowercase after the first word
layout: post
date: 2026-08-22
author: "JM"
image: "thumbnail.png"
categories: [SRT,Clinical-Applications]
---
```

No spaces after the commas in `categories`. Do not add `freeze` or
`title-block-banner`; `posts/_metadata.yml` already sets them for every post.

## 3. Write the post

Full guidance with worked examples is in `reference/voice.md`. The short version:

- Open cold on the concrete problem, in first or second person. Never "In this post I
  will".
- 800 to 2200 words. Sentence-case `##` headings, four to seven of them, no numbering.
- Name real tools, methods, and platforms. Use real numbers. Vague claims are the one
  thing this blog does not publish.
- Bold lead-ins (`**Pooling-based methods** like scran ...`) when enumerating a family
  of approaches.
- Close with practical advice, then a `## Further Reading` list of real references with
  DOIs. Never fabricate a citation; if a reference cannot be verified, leave it out.
- American English. No em dashes anywhere, use a semicolon or a full stop.
- In-prose citations use `(First author, Journal, Year)`.
- Figures are referenced bare, on their own line: `![](spatial.png)`. No captions, the
  surrounding prose does that work.

## 4. Two figures, always

These are conceptual diagrams that carry an argument, not decoration. Place the first
after the section that sets up the problem and the second in the analytical payoff
section.

Style, taken from `flow.png`, `spatial.png`, and `transforming.png`: landscape roughly
16:9, a dark slate title banner across the top, white or tinted rounded panels on a
light gray ground, either a numbered stage flow (1, 2, 3) or a two-column
before-and-after comparison, bold panel headings, small labeled elements, muted
blue / sage / lavender palette with one warm accent.

Two ways to produce them, in order of preference:

1. **BioRender**, which is where the existing figures came from. The BioRender MCP
   connector is configured for this account; authenticate and build there when the
   figure needs biological iconography (cells, tissue, instruments, people).
2. **`scripts/house_style.py`**, for schematic figures that are panels, arrows, and
   labels. Run `python3 scripts/example_figure.py` to see the comparison layout
   assembled, then adapt it. The `FIG` palette and `FIG_TINTS` are pre-sampled.

Name files for what they show (`flow.png`, `spatial.png`, `transforming.png`), lowercase,
no post number in the name.

## 5. One thumbnail

`thumbnail.png`, 2816x1536, in the flat vector style of posts 03-05: near-white ground,
navy line art, blue and green dots, faint grid, large title over subtitle, bold uppercase
captions under each half. It almost always states a contrast: before and after, wrong and
right, lost and retained.

```bash
python3 scripts/example_thumbnail.py        # the post 05 thumbnail, end to end
```

Copy that file, change the middle section, keep the scaffolding. Then check it small,
because the listing renders it at a few hundred pixels:

```python
Canvas.proof("thumbnail.svg", "proof_small.png", width=340)
```

Look at the 340px proof. If the captions turn to mush or the two halves stop reading as
different, cut elements and enlarge type until they do. Keep the working `.svg` in the
scratchpad, not in the post folder; only the `.png` belongs in `posts/NN.slug/`.

## 6. Render and hand over

```bash
quarto render
```

Confirm the post appears in the listing with its thumbnail, the two figures resolve, and
the category counts went up:

```bash
grep -c 'class="quarto-post' docs/index.html
```

Then stop. Do not run `git commit` or `git push`; JM stages and commits. Report the new
folder, the word count, the figure and thumbnail files, and anything you could not verify
(an unconfirmed citation, a figure that needed BioRender and could not be built).
