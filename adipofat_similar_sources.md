# ADIPOFAT: The Neighboring Landscape

A survey of blogs, newsletters, and video channels that publish content close to what ADIPOFAT covers: omics, spatial biology, data science practice, and critical commentary on computational method.

Compiled 22 August 2026.

---

## 1. Closest matches

These sources share ADIPOFAT's core combination of technical depth, personal voice, and willingness to criticize standard practice.

**Chatomics (Ming "Tommy" Tang)**: <https://divingintogeneticsandgenomics.com/>
The single closest analog. An individual researcher writing tutorials and opinion on single-cell genomics, ATAC-seq, batch correction, R and Python workflow, and reproducibility. Over 230 tutorials and roughly 6,000 monthly readers. Tang is Director of Bioinformatics at AstraZeneca. He also runs a companion newsletter and maintains the `awesome_spatial_omics` and `awesome-single-cell`-adjacent repositories on GitHub, which overlaps directly with ADIPOFAT's post on curated community resources. Active in 2026.

**JEFworks Lab (Jean Fan, Johns Hopkins)**: <https://jef.works/blog>
A lab blog rather than a personal one, but written in the same register. Posts cover MERFISH, Visium and Xenium analysis, dimensionality reduction, spatial method comparison, and, recently, AI-assisted analysis and "vibe coding" with their own tools. Recent posts run to May 2026. The strongest overlap with ADIPOFAT's spatial transcriptomics thread.

**Bits of DNA (Lior Pachter, Caltech)**: <https://liorpachter.wordpress.com/>
The reference point for critical commentary in computational biology. Long, evidence-heavy posts that take apart published methods and claims. Posts infrequently, but each entry is substantial. This is the tradition ADIPOFAT's "Why Your Spatial Transcriptomics Analysis Might Be Lying to You" post belongs to.

**Paired Ends (Stephen Turner)**: <https://blog.stephenturner.us/>
Successor to the long-running Getting Genetics Done blog, which ran from 2008. Covers new research, programming technique, statistics, and general bioinformatics commentary. Turner also writes about Quarto specifically, which matters given ADIPOFAT's own publishing stack. The archived Getting Genetics Done remains a useful reference at <https://gettinggeneticsdone.blogspot.com/>.

---

## 2. Newsletters

**Behind the Bioinformatics (Sebastiaan Vanuytven)**: <https://behindthebioinformatics.substack.com/>
Weekly reading digest of single-cell and computational biology papers and tools. Published reliably through 2026. Useful both as a source of post material and as an outlet that might link to ADIPOFAT.

**The Single-Cell World (Cátia Moutinho)**: <https://thesinglecellworld.substack.com/>
Monthly "Single-Cell Drops" roundups of technology, methods, and trends, plus an interview podcast with people in the field. More communication-oriented and less code-heavy than ADIPOFAT, so it complements rather than competes.

**Spatial Omics Weekly**: <https://omics.substack.com/>
Focused digest of spatial omics developments. Archive is strong through 2023 and 2024, so check current cadence before relying on it.

---

## 3. Aggregators and news sites

**RNA-Seq Blog**: <https://www.rna-seqblog.com/>
High-volume aggregator of transcriptomics methods and papers, with an active spatial transcriptomics tag. Broad rather than deep, and a good place to track what is being published.

**R-bloggers**: <https://www.r-bloggers.com/>
Syndicates R-focused posts, including bioinformatics and Quarto content. Worth noting because syndication there is one of the cheapest ways to expand readership for a Quarto and R blog.

**Biostars**: <https://www.biostars.org/>
Question-and-answer community rather than a blog, but it is where the practical problems ADIPOFAT writes about get raised first.

---

## 4. YouTube channels

**Sanbomics**: <https://www.youtube.com/channel/UCuf90yPD_Yx53xZyVLtvRmA>
Practical single-cell and RNA-seq analysis walkthroughs in Python and R. Clear code-first teaching with little filler.

**Bioinformagician**: <https://www.youtube.com/c/Bioinformagician>
Step-by-step Seurat, scRNA-seq, integration, and pseudotime tutorials. Probably the most direct video equivalent of ADIPOFAT's tutorial posts.

**OMGenomics (Maria Nattestad)**: <https://www.youtube.com/channel/UCG4kmWK8UyzfenZ60xVBapw>
Genomic data visualization and tooling, with an engineering sensibility. Companion site at <https://omgenomics.com/>.

**Bioinformatics Coach**: <https://www.youtube.com/channel/UCOJM9xzqDc6-43j2x_vXqCQ>
Beginner-oriented pipeline and tool tutorials. Useful as a model for how to pitch to wet-lab researchers moving into computation.

**StatQuest (Josh Starmer)**: <https://www.youtube.com/user/joshstarmer>
Statistical and machine learning concepts explained from first principles. Not omics-specific, but the standard reference when a post needs to lean on a statistical idea.

**Bioinformatics.ca and Griffith Lab (rnabio.org)**: <https://rnabio.org/>
Full workshop lecture series posted publicly, including a 2026 single-cell RNA-seq analysis course. Institutional rather than personal, and the closest thing to a canonical curriculum.

---

## 5. Vendor and institutional blogs

These are commercially motivated but technically competent, and they set the terms much of the field uses.

**10x Genomics Analysis Guides**: <https://www.10xgenomics.com/resources/analysis-guides>
**Technology Networks**: <https://www.technologynetworks.com/>
**scverse tutorials and forum**: <https://scanpy-tutorials.readthedocs.io/> and <https://discourse.scverse.org/>
**Bioconductor OSCA book**: <https://bioconductor.org/books/release/OSCA/>

The scverse and Bioconductor resources are the reference documentation ADIPOFAT posts will most often need to argue with or build on.

---

## 6. Where ADIPOFAT sits

Three observations from the survey.

First, the crowded space is tutorial content. Seurat and Scanpy walkthroughs exist in large numbers, in text and video, from individuals and institutions alike. Competing there on volume is not promising.

Second, the thin space is critical methodological commentary. Bits of DNA does it rarely and at length. Very few others do it at all. ADIPOFAT's normalization post occupies ground that is largely empty, and the "might be lying to you" series is the strongest differentiator in the current catalog.

Third, the genuinely open space is AI-assisted research workflow written from inside real practice. The published literature on LLMs in bioinformatics is mostly framework papers and position pieces. Almost no one is documenting a concrete, reproducible Quarto and Claude Code writing pipeline the way the December 2025 post does. Jean Fan has begun touching this from the analysis side, and Tang writes about AI in drug discovery, but neither covers the writing and publishing workflow in detail.

The combination that no one else currently holds is spatial biology methodology, critical rather than promotional, plus transparent AI-assisted workflow, published as a reproducible Quarto notebook.

---

## 7. Practical next steps

Syndicating to R-bloggers costs almost nothing and reaches the R and Quarto audience directly. Subscribing to Behind the Bioinformatics and The Single-Cell World supplies a steady stream of post material and identifies people who link outward. Engaging in the scverse forum and Biostars threads on normalization puts the spatial series in front of exactly the readers it is written for.
