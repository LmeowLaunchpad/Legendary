# Verification record

[← Finding 002](README.md) · [Proof](proof.md) · [References](references.md)

**Author:** Roger Malcolm III. **Research, drafting, and implementation assistance:** GPT-6, including several agents within one shared-model investigation. Separate agent checks are not independent external peer review; the agents shared sources, context, and possible failure modes.

**Investigation date:** 2026-10-08 (America/New_York). **Source snapshot:** `adc7f1241b42e322a6451854ab7e4b4c146bf78a` of `openai/math`.

**Mathematical record:** a complete written candidate proof is supplied, with explicit proofs of the generalized finite compiler and its forward and reverse implications, followed by cited external theorem interfaces. The compiler is not left as an additional conjectural premise. **Review record:** source inspection, adversarial AI-assisted checks, and a reproducible reduced finite calculation. No external human mathematical review, Lean formalization, or proof-assistant verification of this finding has been completed.

## Exact claim under review

The input is one finite nonempty set $T\subset\mathbb Z^3$, supplied by its integer coordinates. The question is whether some $A\subset\mathbb Z^3$ satisfies $A\oplus T=\mathbb Z^3$. The tile varies with the input; the dimension, whole-lattice target, and allowance of translations only are fixed. Connectedness is not required. The written proof gives a computable many-one reduction from the domino problem and the standard finite-obstruction upper bound, yielding the claimed $\Pi^0_1$-completeness.

This is not a decision problem about one permanently fixed tile, an efficiency claim, a connected-polycube theorem, or an assertion about arbitrary Euclidean translations and rotations.

## Checks of the proof

| Component | Check performed | Limit of the check |
| :--- | :--- | :--- |
| Attribution and source construction | Read S1's Sections 3–6; identified the graph, cycle, activation, shared seed output, and stacking mechanisms being adapted. | No certification of all claims or formalizations elsewhere in the source repository. |
| Decorated input rule | Checked S2's Definition 5.1 and Proposition 5.2, the two prime projections, nonconstant-column condition, and canonical yes-instance array. The finite rule can be enumerated using affine coefficients modulo $p_1^2p_2^2$ and local domino rectangles of at most four sites. | S2's full foundational Sudoku theorem is a cited input, not re-proved here. |
| Cyclic finite group | Checked that all auxiliary prime factors avoid both structural primes and each other, and that the residue set indexes horizontal classes rather than becoming an extra noncyclic group factor. | The very large finite compiler has not been generated for arbitrary input instances. |
| Reverse compiler | Checked graph fibres, dependence tiles, the exclusion-cycle collision, ordinary activation, and the nonnegative integer histogram argument forcing seed activation. | These are mathematical checks of the general proof, not machine-checked proofs. |
| Extraction | Checked selection of a full decorated label, all affine line words, and both seed values in every column. The seeds constrain both prime components while leaving the decoration free. | No claim that every admissible Sudoku array can be realized by the forward construction. |
| Forward compiler | Checked explicit block inverses and both cases of each seed activation map using the same output $z$. Checked the $3/4/(D-7)$ residue partition, CRT offsets, and the sheared high coordinate including carries. | The finite check below samples target fibres in a reduced model; the general statement rests on the written inverse formulas. |
| Stacking | Checked uniqueness of each color contribution, projection without multiplicity, both existence implications, and a terminating search for a difference-cover partition in a fresh prime cyclic group. | This concerns equations with a common translation set, not arbitrary multi-prototile tilings with separate translation sets. |
| Final lift | Checked S3's Theorem 1.1 with one prototile and the quotient $\mathbb Z^3\twoheadrightarrow\mathbb Z^2\times\mathbb Z/Q\mathbb Z$, including the finite construction when $Q$ varies with the input. | The general quotient-lifting theorem is a cited external result. |
| Consequences | Checked the finite-obstruction compactness argument, the no-computable-uniform-obstruction-bound implication, and the separate pairwise lattice-gas reformulation. | Exact zero ground-state energy is distinguished from numerical approximation or practical material prediction. |

The reverse compiler and the forward seed construction were each read by another agent assigned to seek failures. In particular, the audit challenged whether the seeds constrain only a diagonal, whether the offset choices create a circular inverse, whether the finite factor remains cyclic, and whether stacking preserves whole-lattice existence. No defect was found in those checks. That outcome records the scope and result of the investigation, not a guarantee of correctness.

## Reproducing the finite calculation

The checked script is [checks/check_seed_maps.py](checks/check_seed_maps.py). It uses only the Python standard library and requires Python 3.8 or later. From the repository root, run:

```sh
python findings/002-three-dimensional-monotiling/checks/check_seed_maps.py
```

For the check's scope and usage:

```sh
python findings/002-three-dimensional-monotiling/checks/check_seed_maps.py --help
```

The recorded run used **Python 3.12.10** and exited successfully with:

```json
{"status": "passed", "fibers": 8, "representations": 614500, "seeds": 2, "scope": "reduced finite shared-seed model only; not a proof of the theorem"}
```

The program refuses optimized Python execution because its collision, coverage, and CRT checks use assertions. It is deterministic and requires no network access or input data.

### What those numbers mean

The model uses $S=(\mathbb Z/5\mathbb Z)^2$ and $D=25$, with abstract seed regions of sizes 3 and 4 and a remaining region of size 18. It retains the common output rotation, the two independent shift-list orderings, active and inactive seed formulas, and coprime CRT constraints.

Its seed parameters are $(a,b,r,a_{\mathrm{other}})=(2,29,37,3)$ and $(3,31,43,2)$. For each seed it checks all batch indices at four selected target bases: $(-7,2,0)$, $(0,0,1)$, $(6,-3,r-1)$, and $(23,19,7)$. This includes negative horizontal coordinates and several low coordinates. Each first-seed fibre has 53,650 representations; each second-seed fibre has 99,975. All outputs are distinct and each target fibre is covered, giving $4(53{,}650+99{,}975)=614{,}500$ representations over eight fibres.

This is **not** the full two-prime construction: it does not meet that construction's structural-prime hypotheses, implement its decorated Sudoku rule, test its seed congruences, build the complete cyclic compiler, execute the quotient lift, or decide any infinite tiling problem. It tests the shared-seed algebra in the displayed finite model. It neither replaces the general inverse proof nor validates the full reduction computationally.

## Prior-art search and its limits

The search on 2026-10-08 focused on the exact combination of one input tile, translations only, all of $\mathbb Z^3$, and fixed dimension three. It compared the versioned primary sources listed in [references.md](references.md), together with the author's September 2023 [explanation of the Greenfeld–Tao result](https://terrytao.wordpress.com/2023/09/18/undecidability-of-translational-monotilings/). That explanation is contextual evidence about quantifiers, not a theorem used in the proof.

The most important comparison is [Li–Liu's September 7 draft](references.md#s5), which already claims whole-lattice one-tile undecidability in a fixed sufficiently large dimension. Consequently, **this finding makes no claim to be the first fixed-dimensional undecidability result**. The candidate distinction is dimension three, with dimension two decidable by [Bhattacharya](references.md#s4). The Li–Liu PDF is mutable, and its printed date alone does not establish a historical upload time or settle priority.

Other comparisons addressed specific potential shortcuts:

- [Greenfeld–Tao](references.md#s2) plus [quotient lifting](references.md#s3) does not automatically compress a varying finite group's generator rank into one cyclic coordinate.
- Li–Liu's stated route through a group with free part $\mathbb Z^4$ is not a quotient of $\mathbb Z^3$; improving finite-generator bookkeeping alone does not remove that free-rank obstruction.
- [Kim's two-polycube theorem](references.md#s6) retains two prototiles. The common-complement stacking lemma used here starts from a different type of system.
- [S1](references.md#s1) supplies a three-dimensional aperiodic example and the compiler machinery; an input-dependent existence equivalence still has to be proved.

The source investigation read S1's introduction and compiler sections and searched every `.tex` file in its `build` directory for `undecid`, `algorithm`, `decidab`, and `computab`. No statement of the new undecidability conclusion was located there; the undecidability matches were Greenfeld–Tao citation keys. To repeat the text search against the cited snapshot, substitute its local manuscript directory for `MANUSCRIPT`:

```sh
rg -n -i 'undecid|algorithm|decidab|computab' MANUSCRIPT/build -g '*.tex'
```

Representative web queries included:

```text
"monotilings" "dimension three" undecidability
"monotilings" "dimension 3" undecidability
"monotiling" "Z^3" undecidable
"Undecidability of translational monotilings in fixed dimension"
"translational monotilings" "cyclic" undecidability
"single tile" "Z3" undecidability 2026
"one tile" "Z^3" undecidability 2026
"monotiling" "Pi_1" OR "Π" OR "co-r.e." "three"
"Yoonhu Kim" tiling undecidability 2026
site:github.com/openai/math/issues "tiling"
site:github.com/openai/math/discussions "155"
"A translational tile with no fully periodic tiling" undecidable
```

The searches used title and spelling variants and inspected primary papers, versions, author pages, and publisher records for the substantive comparisons. They were not a complete crawl of repository discussions, unindexed manuscripts, theses, or non-English literature, and no authors were contacted. Search results can change and indexing can lag. The recorded outcome is therefore limited: **no earlier statement of the exact dimension-three theorem was located in the sources examined**. It is not a proof of discovery priority, novelty everywhere, or publication readiness.

## Remaining review work

The central next check is external mathematical review of the complete effective reduction, particularly its source adaptations and the interface between the variable cyclic quotient and S3. A proof-assistant formalization and an implementation of the complete finite reduction have not been supplied. The source versions and the finite calculation make the present record inspectable; they do not eliminate the possibility of an error in the written proof or in a cited input.
