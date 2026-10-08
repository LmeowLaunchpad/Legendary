# References and dependency map

[← Finding 003](README.md) · [Proof](proof.md) · [Verification record](verification.md)

**Author:** Roger Malcolm III. **Research assistance:** GPT-6. **Version:** `0.1.0`.

The proposed contribution is the stationary equality argument and its stated consequences. The Gaussian premise, general universal-optimality connection, geometric theorem and stationary-energy framework are credited below. A source's presence here does not mean the present investigation independently verified its entire proof.

| Reference | Role |
| :--- | :--- |
| S1 | Claimed Gaussian minimality; the explicit conditional premise. |
| S2 | Earlier universal-optimality-to-Coulomb connection and the distinction between minimum values and uniqueness. |
| S3 | Standard stationary energy, lifting and compactness, specific entropy, free energy, and the Log2 entropy question. |
| S4 | Sharp planar Voronoi-cell area bound and its equality case. |
| S5 | Earlier stationary uniqueness in one dimension. |
| S6 | Context for stationary planar Coulomb energy and spectral methods. |
| S7–S8 | Context for microscopic limits; their full model assumptions remain necessary. |
| S9 | Local universal optimality of the hexagonal lattice, distinct from a global stationary classification. |
| S10 | Earlier point-process energy theory and low-temperature crystallization in one dimension. |

<a id="s1"></a>
## S1 · OpenAI source premise

OpenAI, *An atomic certificate for triangular-lattice universal optimality*, manuscript family 090, September 26, 2026. The Gaussian specialization of Theorem 1.1 is the premise used here.

- [Pinned manuscript directory](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026).
- [Main mathematical source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/build/main.tex).
- [Finite arithmetic checker](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/verification/check_certificate.py).
- [Formalization scope document](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/090.md).
- [Related Coulomb manuscript's conclusion and limitations](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/build/sections/07-conclusion.tex).

The version pin is `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. The present theorem uses only the explicit Gaussian premise in its own proof, not every assertion in this source family. The related Coulomb manuscript does not itself provide the all-stationary-minimizer classification claimed conditionally here. The [verification record](verification.md) distinguishes a finite checker run, analytic source inspection, and the absence of a fresh full Lean build.

<a id="s2"></a>
## S2 · The earlier universal-optimality connection

Mircea Petrache and Sylvia Serfaty, *Crystallization for Coulomb and Riesz Interactions as a Consequence of the Cohn–Kumar Conjecture* (2020).

[arXiv:1908.09714v3](https://arxiv.org/abs/1908.09714v3).

This work already proves the general implication from universal optimality to the relevant renormalized-energy minima and discusses its physical consequences. Its uniqueness discussion distinguishes periodic configurations from the failure of deterministic uniqueness under finite changes. This note does not claim to have discovered the universal-optimality-to-Coulomb bridge.

<a id="s3"></a>
## S3 · Stationary energy, free energy and entropy

Thomas Leblé and Sylvia Serfaty, *Large Deviation Principle for Empirical Fields of Log and Riesz Gases*, Inventiones Mathematicae **210** (2017), 645–757.

[arXiv:1502.02970v3](https://arxiv.org/abs/1502.02970v3) · [DOI](https://doi.org/10.1007/s00222-017-0738-0) · [Author-hosted corrected text](https://math.nyu.edu/faculty/serfaty/LDPcorrection.pdf).

The interfaces used are the Log2 stationary point-process energy, the stationary lifting result in Lemma 3.8 and formula (3.14), the compactness and lower semicontinuity statement in Lemma 3.9, and the specific-relative-entropy framework. Section 1.9 asks whether ground states have infinite specific relative entropy. The lifting comparison used here is one-sided; no general identification of distinct electric-field domains is assumed. Section 2.7.3 specifies the factor of $`2\pi`$ relating the raw field normalization to this source's energy; the proof retains that factor explicitly.

<a id="s4"></a>
## S4 · Local Voronoi rigidity

A. Mazel, I. Stuhl and Y. Suhov, *Minimal Area of a Voronoi Cell in a Packing of Unit Circles* (2022).

[arXiv:2211.03255v1](https://arxiv.org/abs/2211.03255v1).

This is a self-contained proof of the classical local result: in a unit-circle packing every Voronoi cell has area at least $`2\sqrt3`$, with equality only for the regular circumscribed hexagon. Rescaling to disks of radius $`a/2`$ gives the area bound $`\sqrt3a^2/2`$ used in the proof. The local statement, including equality, is essential; a bound on global packing density alone would not suffice.

<a id="s5"></a>
## S5 · One-dimensional stationary uniqueness

Thomas Leblé, *A Uniqueness Result for Minimizers of the 1D Log-gas Renormalized Energy* (2015).

[arXiv:1408.2283v1](https://arxiv.org/abs/1408.2283v1).

This establishes uniqueness at the level of stationary point processes for the one-dimensional logarithmic problem, while explaining why individual infinite configurations need not be unique. It is an important precedent for the level at which the present two-dimensional claim is formulated.

<a id="s6"></a>
## S6 · Further stationary Coulomb context

Martin Huesmann and Thomas Leblé, *The link between hyperuniformity, Coulomb energy, and Wasserstein distance to Lebesgue for two-dimensional point processes*.

[arXiv:2404.18588v2](https://arxiv.org/abs/2404.18588v2).

Context for stationary Coulomb energy, covariance and spectral methods. The present proof supplies its own stationary smearing comparison and spectral lower bound rather than assuming an unproved identity between all energy conventions.

<a id="s7"></a>
## S7 · Confined planar log gases

Etienne Sandier and Sylvia Serfaty, *2D Coulomb Gases and the Renormalized Energy* (2015).

[arXiv:1201.3503](https://arxiv.org/abs/1201.3503).

Theorem 2(C) and Remark 1.5 describe the microscopic renormalized-energy minimization arising from confined systems under the paper's hypotheses. They give an application framework, not permission to drop confinement, density normalization or limiting-regime assumptions.

<a id="s8"></a>
## S8 · Ginzburg–Landau vortex limits

Etienne Sandier and Sylvia Serfaty, *From the Ginzburg–Landau Model to Vortex Lattice Problems* (2012).

[arXiv:1011.4617](https://arxiv.org/abs/1011.4617).

Theorem 4 concerns a specified domain and applied-field regime. Its microscopic current normalization has point intensity $`m/(2\pi)`$ when $`\mathrm{curl}\,j=2\pi\nu-m`$. This is context for further applications after the relevant scaling and hypotheses are checked, not a theorem here about every vortex system or applied field.

<a id="s9"></a>
## S9 · Local universal optimality

Thomas Leblé, *The hexagonal lattice is universally locally optimal*, arXiv submission 2025.

[arXiv:2511.03353v1](https://arxiv.org/abs/2511.03353v1).

Theorems 1–2 prove minimality against sufficiently small uniformly bounded displacements of the lattice for Gaussian and completely monotone squared-distance potentials. Section 1.3 explains the local scope. This is a substantive nearby result, but it does not classify all stationary minimizers of the logarithmic Coulomb functional. It neither replaces Hypothesis G nor supplies the global equality conclusion of this note.

<a id="s10"></a>
## S10 · Earlier point-process and low-temperature methods

Thomas Leblé, *Logarithmic, Coulomb and Riesz energy of point processes*, Journal of Statistical Physics **162** (2016), 887–923.

[arXiv:1509.05253v1](https://arxiv.org/abs/1509.05253v1).

Theorem 3 and Section 7 concern low-temperature crystallization in dimension one. Section 7.3 uses finite-entropy near-minimum competitors, an established variational method also relevant here. Theorem 1 distinguishes intrinsic and electric energy comparisons in the Coulomb case. This note supplies the specific two-dimensional jitter calculation and keeps its comparison one-sided; it does not claim to invent the low-temperature competitor method.
