# References

[← Finding 002](README.md) · [Proof](proof.md) · [Gödel supplement](godel.md) · [Verification](verification.md)

The repository source is pinned to commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. ArXiv links identify the revisions used for theorem numbering. Other sources were checked during the 2026-10-08 investigation; an access date or a version identifier is not a mathematical certification.

<a id="s1"></a>

## S1 · The cyclic compiler adapted in this finding

**OpenAI math repository, family 155.** *A translational tile with no fully periodic tiling in dimension three*. Manuscript dated September 23, 2026.

- [Pinned manuscript directory](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026).
- [Section 3: cyclic encoding, graph and dependence equations, cycle exclusion](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/sections/03-cyclic-encoding.tex).
- [Section 4: activation and extraction](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/sections/04-activation.tex).
- [Section 5: the common solution and shared seed output](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/sections/05-common-solution.tex).
- [Section 6: stacking](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/build/sections/06-stacking.tex).

These sections supply the construction being generalized, including its underlying graph, cycle, activation, shared-output, and stacking mechanisms. Finding 002 supplies explicit proofs for the decorated two-prime version and its effective reduction. It does not claim to originate those mechanisms. The source's aperiodicity statement alone is not the undecidability conclusion; the input-dependent equivalence is essential. The final quotient lift is credited separately to S3.

<a id="s2"></a>

## S2 · Greenfeld–Tao: decorated Sudoku and monotiling undecidability

**Rachel Greenfeld and Terence Tao.** *Undecidability of translational monotilings*. **arXiv:2309.09504v2**, October 24, 2023. Published online in the **Journal of the European Mathematical Society**, June 21, 2025. DOI: [10.4171/JEMS/1673](https://doi.org/10.4171/JEMS/1673).

- [Versioned arXiv record](https://arxiv.org/abs/2309.09504v2).
- [Versioned full text](https://arxiv.org/html/2309.09504v2).
- [Publisher's record](https://ems.press/content/serial-article-files/50916).

The proof uses Definition 5.1 and Proposition 5.2: the finite decorated two-prime word rule, its equivalence with a domino configuration, and the canonical array in the proposition's proof. Definitions 3.1 and 4.5 specify the line and column conventions; equation (4.3) gives the prime-size requirement. Lemma 2.5 relates quadrant and plane configurations. For prior-art comparison, Theorem 1.3, Corollary 1.5, and Section 7.1 specify the varying finite group, varying dimension, and periodic-target qualifications of the earlier monotiling statements.

<a id="s3"></a>

## S3 · Meyerovitch–Sanadhya–Solomon: effective quotient lifting

**Tom Meyerovitch, Shrey Sanadhya, and Yaar Solomon.** *A note on reduction of tiling problems*. **Israel Journal of Mathematics 267 (2025), 421–435.** DOI: [10.1007/s11856-025-2716-3](https://doi.org/10.1007/s11856-025-2716-3). The version used for theorem numbering is **arXiv:2211.07140v1**, November 14, 2022.

- [Versioned record](https://arxiv.org/abs/2211.07140v1).
- [Versioned full text](https://arxiv.org/html/2211.07140v1).
- [Versioned PDF](https://arxiv.org/pdf/2211.07140v1).
- [Authors' institutional publication record](https://cris.bgu.ac.il/en/publications/a-note-on-reduction-of-tiling-problems-2/).

Theorem 1.1 provides the tiling-equivalence lift from a quotient of a lattice to that lattice, preserving the number of prototiles. Lemma 2.1 and the construction in its proof are relevant to effectivity. Here the quotient map is explicitly

```math
\mathbb Z^3\longrightarrow\mathbb Z^2\times\mathbb Z/Q\mathbb Z,
\qquad(a,b,c)\longmapsto(a,b,c\bmod Q).
```

The finding checks that the finite construction can be performed with the input-dependent integer $`Q`$. It does not assert a new general dimension-lowering theorem or apply this lift to an arbitrary finite group with unbounded generator rank.

For the [Gödel supplement](godel.md), Corollary 1.4 states a provability implication: in a first-order theory supporting the proof of correspondence (2), a proof that the lifted tiles tile the lattice yields a proof that the original tiles tile the quotient. The following paragraph identifies ZFC as sufficient for explicit finitely generated abelian groups and explicit quotient maps. Theorem 1.1 supplies the full tiling correspondence; the corollary itself is worded in one direction. These are established transfer results, not new logical machinery introduced here.

<a id="s4"></a>

## S4 · Bhattacharya: the dimension-two decidability boundary

**Siddhartha Bhattacharya.** *Periodicity and decidability of tilings of $`\mathbb Z^2`$*. **arXiv:1602.05738v1**, February 18, 2016.

- [Versioned record](https://arxiv.org/abs/1602.05738v1).
- [Versioned full text](https://arxiv.org/html/1602.05738v1).
- [Versioned PDF](https://arxiv.org/pdf/1602.05738v1).

Theorem 1.1 and Corollary 1.2 establish periodicity and decidability for a single finite translational tile of the whole two-dimensional integer lattice. This is the cited lower-dimensional comparison behind the word “optimal.” It does not address tiling by several prototiles or with rotations.

<a id="s5"></a>

## S5 · Li–Liu: an earlier dated fixed-dimension claim

**Heng Li and Xizhi Liu.** *Undecidability of translational monotilings in fixed dimension*. Author-hosted draft dated **September 7, 2026**; accessed October 8, 2026.

- [Author-hosted PDF](https://xliu2022.github.io/Unpolished_Manuscripts/Undecidability%20of%20translational%20monotilings%20in%20fixed%20dimension.pdf).
- [Author's publications and research-notes page](https://xliu2022.github.io/).

Theorem 1.1 already claims undecidability for one tile of the whole lattice in every fixed dimension above a sufficiently large constant. Section 6 uses a group with free part $`\mathbb Z^4`$; Section 7 gives an explicit large dimension bound. This is essential prior-claim context: Finding 002 does **not** claim the first fixed-dimensional monotiling undecidability result.

Section 7, PDF page 25, also explicitly compiles a Rosser sentence into a monotile whose tileability is independent of ZFC, assuming ZFC is consistent, in those larger fixed dimensions. Its argument specifies a counterexample-search machine and a tiling equivalence provable in ZFC. Thus the Rosser-to-monotile connection already appears in this earlier dated draft. The [Gödel supplement](godel.md) applies established incompleteness arguments to the proposed dimension-three compiler; it does not claim a new general connection between tilings and Gödel incompleteness.

The PDF is mutable. Its printed date is not an independently established first-public-upload date. The author's page places the work among preliminary research notes, under a general notice that some entries have not been fully polished or human-verified. Its complete proof was not independently certified in this investigation, and Finding 002 does not depend on its theorem. These qualifications do not erase its priority-relevant claim.

<a id="s6"></a>

## S6 · Kim: the two-polycube comparison

**Yoonhu Kim.** *Undecidability of Translational Tiling with 2 Polycubes*. **arXiv:2508.11725v2**, August 10, 2026; first submitted August 15, 2025.

- [Versioned record](https://arxiv.org/abs/2508.11725v2).
- [Versioned full text](https://arxiv.org/html/2508.11725v2).

Theorem 4.1 concerns two polycubes in dimension three. Theorem 2.5 preserves the number of prototiles when making them connected; it is not a conversion from two prototiles to one. Section 6 supplies a dated discussion of the remaining one-tile problem. This source is used for comparison, not as a dependency of the main theorem or as evidence for a connectedness claim here.

<a id="s7"></a>

## S7 · Greenfeld's ICM survey

**Rachel Greenfeld.** *Translational Tilings: Structured or Wild?* **Proceedings of the International Congress of Mathematicians 2026**, Volume 3, pp. 76–96. DOI: [10.1137/25M1801694](https://doi.org/10.1137/25M1801694).

- [Publisher's full text](https://epubs.siam.org/doi/full/10.1137/25M1801694).
- [arXiv:2509.25576v1](https://arxiv.org/abs/2509.25576v1), September 29, 2025.

Remark 6.2 and Question 6.3 distinguish an unbounded generator-rank reduction from undecidability in a fixed dimension. They locate the historical problem; S5 prevents treating that open-question statement as a complete October 2026 status report. Section 2 also recalls the machine-nonhalting-to-domino-solvability direction of Berger's reduction. This survey is contextual support, not a replacement for the exact theorem interfaces in S2 and S3.

<a id="s8"></a>

## S8 · Berger: the classical domino-problem input

**Robert Berger.** *The undecidability of the domino problem*. **Memoirs of the American Mathematical Society 66 (1966), 1–72.** DOI: [10.1090/memo/0066](https://doi.org/10.1090/memo/0066).

- [AMS publisher link](https://www.ams.org/books/memo/0066/).
- [Contemporary AMS description, January 1967 Notices](https://www.ams.org/journals/notices/196701/196701FullIssue.pdf).

This is the classical source of the domino undecidability reduction. The contemporary publisher description explicitly records a domino set solvable precisely when the encoded machine never halts; S7 discusses the same direction. Finding 002 takes this classical input as cited rather than re-proving Berger's construction. The finite-obstruction compactness argument supplying the upper computability bound is given in the finding's proof.

<a id="s9"></a>

## S9 · Constructive incompleteness and the Rosser distinction

**Saeed Salehi and Payam Seraji.** *On constructivity and the Rosser property: a closer look at some Gödelean proofs*. **Annals of Pure and Applied Logic 169(10) (2018), 971–980.** DOI: [10.1016/j.apal.2018.04.009](https://doi.org/10.1016/j.apal.2018.04.009). The version used for theorem numbering is **arXiv:1612.02549v2**, February 14, 2018.

- [Versioned record](https://arxiv.org/abs/1612.02549v2).
- [Versioned full text](https://arxiv.org/html/1612.02549v2).
- [Author-hosted published article](https://saeedsalehi.ir/pdf/papers/APAL-2.pdf).

The introduction distinguishes effective construction of a true unprovable sentence from independence under consistency alone. Theorem 2.2 gives a constructive Kleene argument; Theorem 2.3 demonstrates why that construction need not have the Rosser property. These distinctions explain the supplement's use of the Rosser construction for two-sided independence under consistency alone. The source does not establish the geometric compiler in Finding 002.

**J. Barkley Rosser.** *Extensions of some theorems of Gödel and Church*. **The Journal of Symbolic Logic 1(3) (1936), 87–91.** DOI: [10.2307/2269028](https://doi.org/10.2307/2269028). [Publisher's record and extract](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/extensions-of-some-theorems-of-godel-and-church/0461E34DC1F219C459EE84CC2FA89068).

Rosser's original result supplies the consistency-only incompleteness principle. The publisher's bibliographic record and extract were checked; its full original proof was not re-audited here. The supplement uses this established theorem and makes no claim to a new proof of Gödel's or Rosser's theorem. The prior monotiling application is separately credited in S5.
