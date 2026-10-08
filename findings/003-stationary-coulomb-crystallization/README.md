# 003 · Stationary Coulomb crystallization from Gaussian minimality

**A conditional classification of all stationary ground states of the planar logarithmic Coulomb energy.**

Research by **Roger Malcolm III**, using **GPT-6**.

[← All findings](../../README.md#findings) · [Detailed proof](proof.md) · [Verification record](verification.md) · [References](references.md)

| Record | Value |
| :--- | :--- |
| Finding ID | `003` |
| Author | Roger Malcolm III |
| Research assistance | GPT-6 |
| Version | `0.1.0` |
| Research date | October 8, 2026 |
| First published | October 8, 2026 |
| Mathematical status | Conditional theorem; complete proof draft supplied |
| Review status | AI-assisted proof and source checks; no external review or formal verification recorded |
| Areas | Mathematical physics · probability · discrete geometry · crystallization |

> [!IMPORTANT]
> The theorem is **conditional on Gaussian minimality**, stated precisely in the [proof](proof.md). OpenAI manuscript 090 claims that input. The present note supplies a proposed downstream proof; it does not independently certify the entire source theorem. Neither correctness nor novelty has been established by external review. [Verification scope](verification.md).

## The conditional theorem

Assume that the density-one triangular lattice minimizes every Gaussian pair energy among all locally finite simple planar configurations of centered density one.

Then the stationary probability laws minimizing the planar logarithmic Coulomb energy at intensity one are **exactly mixtures of uniformly translated, rotated triangular lattices**. A translation-ergodic minimizing law has a fixed lattice orientation and a uniform random translation.

Let $`A`$ be the covolume-one triangular lattice, $`P_A`$ its uniformly translated law, and $`\mathcal W_{\mathrm{all}}`$ the field energy defined in the proof. The proposed argument establishes

```math
\mathcal W_{\mathrm{all}}(P)-\mathcal W_{\mathrm{all}}(P_A)
\ge 4\pi^2\int_0^\infty
\bigl(H_P(t)-H_A(t)\bigr)\,dt
\ge 0.
```

Here $`H_P(t)`$ is the expected ordered-pair energy for the planar heat kernel. Equality holds precisely when

```math
P=\int_{\mathbb R/(\pi/3)\mathbb Z}P_{\theta A}\,\nu(d\theta),
```

where $`\nu`$ is a probability distribution over lattice orientations. The proof also transfers the classification to the standard point-process energy of Leblé and Serfaty, with its normalization and field-lifting relation stated explicitly. [Main theorem and proof](proof.md#main-theorem).

## In plain language

Consider infinitely many identical repelling charges in a plane, balanced by a uniform neutralizing background. Look at their arrangement from a randomly placed observation point, with no preferred location.

The conclusion says that, at the lowest possible energy, the arrangement must look like a perfect triangular crystal. Its orientation can be random, and so can the observer's position within one repeating cell. Subject to the stated premise and the correctness of the proof, no other stationary ground-state law is possible.

The statement concerns this precise infinite-system model. Changing finitely many points of a deterministic crystal can leave its energy per area unchanged. Such configurations are why the theorem is formulated for **stationary laws**, rather than asserting uniqueness for every individual infinite configuration.

## The connection and the proposed contribution

The broad route from universal optimality to Coulomb minimum energy is already due to [Petrache and Serfaty](references.md#s2). The proposed contribution here is an **equality argument classifying every stationary minimizing law**.

1. **Transfer Gaussian minimality to stationary laws.** Finite field energy supplies local count moments and density one in every invariant component. The deterministic hypothesis then bounds the expected Gaussian pair energies.
2. **Bound Coulomb excess by Gaussian excess.** A stationary smearing comparison and a spectral lower bound control the integral of the nonnegative heat-kernel energy differences, including self-energy and background terms.
3. **Extract a minimum separation from equality.** At short times, a pair closer than the triangular nearest-neighbor distance would contribute more than the triangular Gaussian tail allows. Equality therefore excludes every such pair almost surely.
4. **Force the crystal geometrically.** The sharp local Voronoi-cell area bound, together with stationary mass transport, makes every cell a regular hexagon. These cells propagate one triangular lattice throughout each realization.

The qualitative classification uses only Gaussian minimality. It does **not** require a further strict numerical margin from a Fourier certificate.

## Consequences proved in the note

### Infinite specific relative entropy at the ground state

Every minimizing stationary law has infinite specific relative entropy relative to the unit Poisson process. In a large enough window, the crystal forces a pair distance into a countable set of exact lattice distances. A Poisson configuration satisfies that event with probability zero.

Conditional on the theorem, this answers the planar logarithmic case of a question in [Leblé–Serfaty, Section 1.9](references.md#s3). This is a statement about a mathematical measure of randomness relative to Poisson, not infinite thermodynamic entropy. [Proof](proof.md#entropy).

Leblé and Serfaty already observe that exact crystalline laws have infinite specific relative entropy. The proposed classification extends that observation to **every** ground state under the Gaussian premise.

### Low-temperature limits of the variational model

For minimizers of the standard stationary free-energy functional

```math
\mathcal F_\beta(P)
=\frac{\beta}{2}\mathcal W_{\mathrm{LS}}(P)
+\mathrm{ent}(P\mid\Pi^1),
```

every cluster law as $`\beta\to\infty`$ is a triangular orientation mixture, and the specific relative entropy tends to infinity. Small independent jitters of a lattice give finite-entropy competitors and the energy bound

```math
0\le\mathcal W_{\mathrm{LS}}(P_\beta)
-\mathcal W_{\mathrm{LS}}(P_A)
\le C\frac{1+\log\beta}{\beta}
```

for large $`\beta`$. This bound is not asserted to be a new rate, and it is not a rate of convergence in a metric on point processes. [Proof and normalization](proof.md#low-temperature).

## Prior work and scope

| Source | What is already established or supplied |
| :--- | :--- |
| [OpenAI manuscript 090](references.md#s1) | Claims the all-parameter Gaussian minimality used as the explicit premise. |
| [Petrache–Serfaty](references.md#s2) | Connects universal optimality to Coulomb and Riesz minimum energies; discusses periodic uniqueness and physical applications. |
| [Leblé](references.md#s5) | Proves uniqueness of the minimizing stationary law for the one-dimensional logarithmic energy. |
| [Leblé's local-optimality theorem](references.md#s9) | Proves stability against sufficiently small bounded lattice perturbations, rather than a global stationary classification. |
| [Leblé–Serfaty](references.md#s3) | Supplies the stationary energy, lifting, compactness and entropy framework, and asks the ground-state entropy question. |
| [Mazel–Stuhl–Suhov](references.md#s4) | Gives a self-contained proof of the classical sharp local Voronoi-cell theorem. |

The literature checks did not locate this exact two-dimensional stationary classification in the sources examined. That is a limited search result, not a certificate that nobody has observed it.

The conclusion can inform existing microscopic-limit theorems for log gases and specified vortex regimes once their assumptions are retained. This note does not assert a crystalline phase at fixed positive temperature, a melting transition, crystallization of quantum electrons, arbitrary joint particle/temperature limits, or a practical technology. The stronger quantitative short-pair estimate investigated during drafting is outside the claims of this version.

## Provenance and revisions

The source premise is pinned to OpenAI math commit [`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb). The universal-optimality input, earlier Coulomb connection, geometric rigidity and stationary probability machinery are credited separately in the [references](references.md).

Roger Malcolm III directed the investigation and the development of this finding. Research, drafting, source inspection, and separate adversarial checks were performed using GPT-6. These were multiple passes within the same AI-assisted investigation, not independent external peer review. The [verification record](verification.md) documents the checks and their limits.

**Suggested citation:** Roger Malcolm III. *Stationary Coulomb crystallization from Gaussian minimality.* Legendary, Finding 003, version 0.1.0, 2026. Research assistance: GPT-6. [Repository note](https://github.com/LmeowLaunchpad/Legendary/tree/main/findings/003-stationary-coulomb-crystallization). For a fixed version, replace `main` with the commit being cited.

| Version | Change |
| :--- | :--- |
| `0.1.0` | October 8, 2026: initial conditional proof draft, stationary minimizer classification, entropy and low-temperature consequences, source attribution, and verification record. |
