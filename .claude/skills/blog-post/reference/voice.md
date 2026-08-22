# The ADIPOFAT voice

Distilled from posts 00-05. Quotations below are from the published posts; match this,
do not imitate generic science-blog register.

## Stance

An experienced computational biologist talking to a peer who is about to make a mistake,
or has just made one. Confident, specific, occasionally funny, never promotional and
never breathless. The reader is assumed competent: they know what a count matrix is, they
do not need "single-cell RNA sequencing (scRNA-seq)" spelled out twice.

Criticism is aimed at methods, tools, and habits; never at named individuals.

## Openings

Cold open on the concrete situation. No throat-clearing, no roadmap paragraph.

> So here's the thing about analyzing gene expression data. You load up your Xenium or
> Visium dataset, you run the standard Seurat or SpatialData pipelines because that's
> what everyone does, you get your clusters, and you write your paper. Great. Except
> maybe not great, because it turns out that the normalization step you copied from the
> single-cell RNA-seq tutorial might be quietly removing the very biological signal
> you're trying to find.

Note the moves: second person, real tool names, a short flat sentence ("Great.") used as
a beat, then the turn. Openings that begin "In this post" or "Let's explore" are wrong.

## Sentences

Mixed lengths. Long explanatory sentences carrying the mechanism, broken by three- to
six-word sentences that land the point. Fragments are allowed when they do work.

> Cell lysis efficiency varies. mRNA capture rates fluctuate. Amplification introduces
> biases. Sequencing depth differs across cells.

Active voice, present tense for how things behave. Contractions are fine and frequent
("doesn't", "you're", "here's").

## Structure

Four to seven `##` sections in sentence case, no numbers. Titles state a claim or a
question, not a topic label: "Where Spatial Data Breaks the Rules" rather than "Spatial
Data". A `## Looking Forward` or equivalent forward-looking section before the close is
common but not mandatory.

When enumerating a family of approaches, use bold lead-ins in running prose rather than
a bullet list:

> **Pooling-based methods** like scran take a different approach. Instead of computing
> size factors from individual cells, which fails when cells have lots of zeros, scran
> aggregates counts across pools of similar cells.

Bullet lists are reserved for genuinely enumerable things: file inventories, option
lists, checklists.

## Evidence

Every substantive claim carries something concrete: a method name, a platform, a number,
a study. The Excel post cites the 15,841 lost COVID cases and the 20-30% of genomics
papers with corrupted gene names. The normalization post names LogNormalize, SCTransform
v2, scran, Dino, BASiCS, scVI, countland, SpaNorm. Do not write "studies have shown"
without saying which.

In-prose citation format is `(First author, Journal, Year)`.

## Emphasis

Italics for the one sentence per post that is the actual thesis:

> _When you apply standard single-cell normalization methods to spatial transcriptomics
> data, especially in tissues with anatomically structured variation in cell density or
> RNA content, you can inadvertently erase genuine biology_.

Blockquotes for a closing reflection. Bold for method-family lead-ins and for terms being
defined. Never all three at once.

## Closings

Practical advice in imperative mood, short sentences, then one sentence that restates the
stake:

> For now, the practical advice is simple. Understand your tools. Validate your results.
> Don't assume that methods designed for single-cell RNA-seq transfer directly to spatial
> data.

Then a horizontal rule and `## Further Reading` grouped by theme, entries as:

```
Hafemeister C, Satija R. Normalization and variance stabilization of single-cell RNA-seq
data using regularized negative binomial regression. *Genome Biology* 2019.
https://doi.org/10.1186/s13059-019-1874-1
```

Only references that actually exist and were actually consulted. A short honest list
beats a long invented one.

## House rules

American English throughout: normalization, analyze, color, behavior.

No em dashes. Use a semicolon where the clause continues, a full stop otherwise. This
applies to the prose, the front matter, and the figure labels.

Dates in ISO form in front matter.

## Tells to avoid

The register is conversational, which makes generic AI cadence especially visible. Do not
write: "delve into", "it's worth noting that", "in the ever-evolving landscape of",
"revolutionize", "game-changer", "unlock the power of", tricolon summaries
("faster, cheaper, and more accurate"), or a closing paragraph that restates the post
without adding anything. Do not open consecutive paragraphs with the same construction.
If a sentence would survive unchanged in a vendor brochure, cut it.
