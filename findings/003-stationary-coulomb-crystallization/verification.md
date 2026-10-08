# Verification record

[← Finding 003](README.md) · [Proof](proof.md) · [References](references.md)

**Author:** Roger Malcolm III. **Research, drafting, and implementation assistance:** GPT-6, including several agents within one shared-model investigation. Separate agent checks are not independent external peer review; the agents shared sources, context, and possible failure modes.

**Investigation date:** 2026-10-08 (America/New_York). **Version:** `0.1.0`. **Source snapshot:** `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` of `openai/math`.

**Mathematical record:** a complete conditional proof draft is supplied. **Review record:** targeted primary-source inspection, multiple adversarial AI-assisted checks, execution of the source's finite arithmetic checker, and a textual formalization-dependency scan. No external human mathematical review or formal verification of this downstream theorem has been completed. The entire analytic proof of the source premise has not been independently certified.

## Exact claim under review

Assuming the explicitly stated Gaussian-minimality hypothesis, the draft classifies all stationary intensity-one minimizers of planar logarithmic Coulomb energy as mixtures of uniformly translated triangular lattices with arbitrary orientation distribution. It proves a heat-kernel excess lower bound, the equality classification, a transfer to the standard Leblé–Serfaty point-process functional, infinite specific relative entropy of all ground states, and the stated low-temperature variational consequences.

The theorem concerns probability laws invariant under every planar translation. It does not claim that every deterministic minimum-energy configuration is a lattice. Finite changes to an individual infinite configuration illustrate why that stronger assertion would fail.

## Checks of the downstream argument

| Component | Check performed | Limit of the check |
| :--- | :--- | :--- |
| Moments and intensity | Derived local count second moments from one finite-energy smearing; checked intensity one in every invariant component before using the deterministic source hypothesis. | Written mathematical argument, not a machine-checked ergodic theorem. |
| Stationary Gaussian bound | Checked ordered pairs, disk-overlap factors, Fatou's lemma and Gaussian integrability. | Conditional on the source's Gaussian theorem. |
| Smearing comparison | Re-derived the stationary Onsager identity, circle-charge measure terms, self subtraction, background constant, and close-pair monotone limit. | Uses the stated local regularity and second-moment domination. |
| Spectral bound | Checked the Hilbert-space variational inequality, all factors of $`2\pi`$, and exclusion of a zero-frequency covariance atom. | Positive spectral representation is a standard external input. |
| Gaussian passage | Used nonnegative compact cutoffs and Fatou for the general-process lower bound; separately justified equality for the lattice reference. | Does not identify all possible field-energy conventions. |
| Heat identity | Checked cancellation of the diagonal and background terms, finiteness before subtraction, the Euler-constant self term, and the periodic lattice reference. | The periodic Green-function framework is established machinery. |
| Equality and packing | Checked that equality along a sequence of short times excludes all pairs below the optimal spacing; then applied the local Voronoi equality theorem and Palm mass transport. | The local packing theorem is cited; no new packing theorem is claimed. |
| Field domain in applications | Used only the stationary-lifting inequality to the Leblé–Serfaty functional, with equality at the lattice. | No uniqueness assertion for arbitrary compatible fields; divergence-free additions are allowed in the main domain. |
| Entropy and low temperature | Checked the common countable distance-shell event for orientation mixtures; the jitter entropy bound; periodic Green-function averaging; the $`\pi/2`$ jitter coefficient in the standard normalization; compactness and entropy lower semicontinuity. | No finite-temperature phase transition or metric convergence rate follows. |

Two rounds of internal review corrected or clarified several delicate points before this publication: zero frequency is treated explicitly; the general Gaussian-cutoff passage uses Fatou; the lattice self constant is fixed; monotone convergence subtracts a bounded compact difference kernel; the application uses a one-sided lifting comparison; and the qualitative equality argument no longer depends on strict Fourier-minorant slack. These changes are incorporated in the proof, rather than left as unresolved assumptions.

No concrete defect was found in those checks. That records the outcome of an AI-assisted investigation, not a guarantee of correctness.

## Source premise: what was checked

The source's Gaussian-minorant argument was inspected beyond its finite checker. The targeted audit covered the lattice and reciprocal-parameter normalization, atomic and rational-column spectral formulas, Schwartz convergence from summable coefficients, repeated interpolation nodes, Schur/Neumann inversion on the infinite coefficient space, continuous-radius sign bounds, and the correspondence of the script's quantities to the manuscript's finite estimates.

This was a substantial targeted audit, but not an independent reconstruction of every analytic lemma or of the entire formal proof. **Gaussian minimality remains the explicitly named premise.**

### Finite arithmetic receipt

The [upstream script](references.md#s1) was inspected and executed with Python 3.12, isolated mode, and assertions enabled. The recorded run exited with code `0`, produced no standard output, and took approximately 3.8 seconds. Its imports and fixed arithmetic operations were inspected; this receipt is not inferred from a static source manifest.

To reproduce against the pinned source checkout, run from its repository root, without Python optimization flags:

```sh
python -I preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/verification/check_certificate.py
```

The LF-normalized source is 12,726 bytes and has SHA-256:

```text
5689152e970b652a8e40c3c120eda3b45320c8745968a5cb416fa9b9dbdc5385
```

The inspected Windows checkout used CRLF line endings, producing 13,115 bytes and raw SHA-256:

```text
8164f7214ebeef483b061cd3e726fb03caa2d2274f7e1443f3e7419c28a31c0c
```

The line-ending-normalized hash matches the source manifest. The script checks finite interval-arithmetic bounds. It does not alone establish the infinite interpolation, all-radius analytic claims, stationary energy argument, or the new classification theorem.

### Formalization inspection, not a build receipt

The source's challenge metadata names `OAI.Analysis.Triangular.Main` as the solution module. An intentionally unfinished comparator challenge is separate from that module. A recursive textual scan of the solution's imports visited 215 OAI modules, found no missing OAI imports, and found Mathlib as the only external import. No occurrences of the tokens `axiom`, `sorry`, `admit`, `unsafe`, or `native_decide` were found in that scanned source closure.

This inspection is useful evidence about the source files, but **no fresh Lean build or compiled transitive-axiom check was performed**. Textual absence of those tokens is not a formal-verification certificate. The new downstream theorem has not been formalized.

<a id="novelty"></a>
## Prior-art search and its limits

The primary comparisons are [Petrache–Serfaty](references.md#s2), [Leblé's one-dimensional stationary uniqueness](references.md#s5), [Leblé–Serfaty's planar ground-state entropy question](references.md#s3), the OpenAI source and its Coulomb companion, and the stationary-energy literature in [S6](references.md#s6). Searches considered stationary minimizers, equality cases, triangular crystallization, Gaussian or universal optimality, and infinite specific relative entropy.

The general universal-optimality-to-Coulomb implication and its potential physical applications were already known. The proposed distinction is the all-stationary-minimizer equality argument in two dimensions and the resulting resolution, conditional on the source input, of the stated entropy question.

### Fresh prepublication search · October 8, 2026

Two agents performed focused additional searches for the stationary classification and for a prior resolution of the Log2 entropy question, while the main investigation checked nearby local-optimality and point-process papers. The comparison used theorem statements and surrounding hypotheses, rather than relying only on titles or abstracts.

| Candidate overlap | Exact comparison | Assessment |
| :--- | :--- | :--- |
| Coulomb minimum from universal optimality | [S2](references.md#s2), Theorems 1–2 and the uniqueness discussion on PDF page 6 | Already established. Its uniqueness discussion treats periodic configurations and explains why finite modifications obstruct deterministic uniqueness. The present note claims no novelty for the minimum-value bridge. |
| Stationary equality classification | [S5](references.md#s5), main theorem; [S10](references.md#s10), Theorem 3 and Section 7 | Stationary uniqueness and low-temperature crystallization are established in dimension one. These statements do not supply the proposed two-dimensional result. |
| Local stability in the plane | [S9](references.md#s9), Theorems 1–2 and Section 1.3 | Minimality against sufficiently small bounded displacements of a lattice; this does not give a classification of arbitrary stationary Coulomb minimizers. |
| Infinite ground-state entropy | [S3](references.md#s3), Section 1.9, compared with its earlier observation about crystalline configurations | Infinite entropy of exact crystalline laws is already observed. The proposed added conclusion covers every Log2 energy minimizer through the conditional classification. No separate novelty claim is made for lattice singularity itself. |
| Low-temperature method | [S10](references.md#s10), Section 7.3 | Finite-entropy near-minimum competitors and the variational limiting method are prior work. This note includes the planar jitter calculation; it makes no priority claim for the energy rate. |
| OpenAI source overlap | [S1](references.md#s1), Gaussian theorem and the Coulomb companion's conclusion | The Gaussian manuscript supplies the premise. The companion explicitly does not assert uniqueness or defect exclusion; the checked passages do not state the stationary classification or entropy consequence. |

Representative queries in the fresh search were:

```text
"Coulomb" "stationary" "triangular" "uniqueness"
"Gaussian minimality" "stationary" crystallization
"universal optimality" "stationary" "minimizers"
"triangular" "stationary point processes" "minimizers"
"specific relative entropy" "ground states" "Log2"
"Coulomb" "ground states" "specific relative entropy"
"The hexagonal lattice is universally locally optimal"
```

The outcome supports describing the stationary equality argument as a **potentially new conditional theorem**, with the entropy result as a consequence. It does not support calling the entire universal-optimality connection new or claiming confirmed discovery priority.

No exact earlier two-dimensional classification was located in the sources examined. The search did not cover every thesis, unpublished manuscript, discussion, language or unindexed source, and no authors were contacted. It does not establish discovery priority or justify describing the broad Coulomb connection as new.

## Publication checks

The repository catalogue and machine-readable index were checked against the existing finding format. Author credit, assistance disclosure, source pins, relative links, explicit anchors, balanced math fences and portable macros were checked. All 315 mathematical expressions in the four-page publication rendered without MathJax errors in a local browser preview. The overview and representative proof sections were visually inspected. These are presentation checks, separate from mathematical verification.

## Scope of this version and remaining review

The main theorem uses Gaussian minimality alone. A stronger quantitative bound on short-pair density would need additional strict-minorant estimates; it is not a theorem claimed in this version. The low-temperature rate concerns energy excess only. Applications to finite confined log gases or Ginzburg–Landau vortices require the precise hypotheses of their separate limit theorems.

The most valuable next checks are external specialist review of the stationary comparison and equality argument, independent verification of the full Gaussian premise, and a closer priority review of the two-dimensional stationary classification. Formalization of the new argument has not been supplied. This repository publication makes the precise claim, proof and dependencies available for that review.
