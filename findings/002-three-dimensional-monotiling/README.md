# 002 · Undecidability of translational monotiling in dimension three

**A proposed optimal-dimensional theorem, with a complete proof draft and a verification record.**

Research by **Roger Malcolm III**, using **GPT-6**.

[← All findings](../../README.md#findings) · [Detailed proof](proof.md) · [Gödel supplement](godel.md) · [Verification record](verification.md) · [References](references.md)

| Record | Value |
| :--- | :--- |
| Finding ID | `002` |
| Author | Roger Malcolm III |
| Research assistance | GPT-6 |
| Version | `0.2.0` |
| Research date | October 8, 2026 |
| First published | October 8, 2026 |
| Mathematical status | Proposed theorem; complete proof draft supplied |
| Review status | AI-assisted proof and source checks; no external review or formal verification recorded |
| Areas | Discrete geometry · computability · tilings · mathematical physics |

> [!IMPORTANT]
> This is a **research proof draft offered for review**, not an externally verified resolution or a certified priority claim. The finite compiler is adapted from OpenAI manuscript 155 and proved here in its generalized form. The computation encoding and quotient lift are published inputs. Agreement among the participating AI agents is not independent human peer review. [Verification scope](verification.md).

## The proposed theorem

There is no algorithm that, for every finite nonempty shape in the three-dimensional integer lattice, always terminates and correctly decides whether translated copies of that shape cover the entire lattice exactly once.

More precisely, the proof draft gives a total computable map from a finite domino system $`\mathcal R`$ to a finite nonempty set $`T_{\mathcal R}\subset\mathbb Z^3`$ such that

```math
\begin{aligned}
&\mathcal R\text{ admits a matching tiling of }\mathbb Z^2\\
&\quad\Longleftrightarrow\quad
\exists A\subseteq\mathbb Z^3:
A\oplus T_{\mathcal R}=\mathbb Z^3.
\end{aligned}
```

Here $`A\oplus T=\mathbb Z^3`$ means that every lattice point has exactly one representation as $`a+t`$, with $`a\in A`$ and $`t\in T`$. The shape supplied to the algorithm varies with the input; every individual instance uses **one tile type**. Copies have the same orientation, translations are integer vectors, and the shape may be disconnected.

The proposed decision problem is $`\Pi^0_1`$-complete: non-tileability has a finite obstruction that can eventually be found, while the full decision problem can encode non-halting computations. Since translational monotiling is decidable in dimensions one and two, dimension three would be the sharp boundary. [Proof](proof.md) · [Two-dimensional baseline](references.md#s4).

## In plain language

Imagine a finite collection of occupied unit cells used as one rigid shape. The question is whether infinitely many identical copies, shifted but never rotated, can fill the three-dimensional lattice without gaps or overlaps.

The proposed theorem says that no general-purpose algorithm can always answer that question for every input shape. Some shapes can still be understood easily; the impossibility concerns a guaranteed decision method covering all shapes.

The construction is finite but enormous. It provides an algorithmic reduction, not a practical manufactured object or an efficient simulation method.

## The connection

The starting manuscript constructs a three-dimensional tile that has no fully periodic tiling. **Aperiodicity alone does not imply undecidability.** The additional argument must encode every finite domino input and preserve solvability in both directions.

The proof has four parts:

1. **Encode domino rules as decorated Sudoku.** Use Greenfeld–Tao's published equivalence, including two prime components that must each be nonconstant in every column. [Source S2](references.md#s2).
2. **Extend the cyclic compiler.** Adapt manuscript 155's finite tiling equations to the larger decorated alphabet. Two seed channels constrain both prime components while leaving the decoration free. Explicit inverse maps show that all equations have the same translation set whenever the input has a solution. [Source S1](references.md#s1).
3. **Combine the equations into one tile.** A finite stacking construction preserves a cyclic finite coordinate. The resulting ambient group has two infinite coordinates and one finite cyclic coordinate.
4. **Lift to the three-dimensional lattice.** Apply Meyerovitch–Sanadhya–Solomon's published quotient reduction, preserving the number of tile types and tileability of the whole space. [Source S3](references.md#s3).

The extra information occupies a finite **cyclic** group even as the input alphabet grows. This is the feature that permits the final lift to stay in dimension three. The [detailed proof](proof.md) includes the finite equations, activity tests, common solution, stacking argument, and effectivity checks; it does not simply assume the generalized compiler works.

## Consequences in the proof draft

### No computable universal finite test radius

For every shape that fails to tile the lattice, some finite region has incompatible local exact-cover constraints. But there can be no computable bound, based on the input description length, that always tells us how far to inspect to expose that failure.

The finite test allows tiles to cross the inspected region's boundary. It is not the different problem of filling a bounded box with tiles required to remain inside it.

### A restricted lattice-gas model

For binary occupation variables, assign the local energy

```math
h_x(n)=\left(\sum_{f\in F}n_{x-f}-1\right)^2.
```

Every local energy vanishes exactly when the occupied sites are the translation vectors of an exact tiling. Expanding the square gives one binary species, translation-invariant finite-range pairwise repulsions, and a uniform chemical potential.

The draft therefore implies undecidability of whether the minimum energy density in this class is **exactly zero**. It also proves that the energy density can be approximated to any prescribed positive additive error. Exact zero testing and finite-precision approximation are different tasks. [Derivation and scope](proof.md).

### Gödel independence and finite simulations

Conditional on the proposed reduction, for every consistent, effectively axiomatized extension of ZFC, a finite three-dimensional tile can be effectively specified whose whole-lattice tileability is true but neither provable nor refutable in that theory. Each individual finite local test still has a provable satisfying witness. No fully periodic tiling exists, since a finite unit cell would certify tileability.

For the associated lattice gas, every finite periodic calculation has positive minimum energy, although the infinite-system minimum is zero. Arbitrarily accurate positive upper bounds can be certified within the theory while exact zero remains independent. Local tests permit boundary-crossing tiles; periodic calculations require a pattern that repeats forever.

The [Gödel supplement](godel.md) gives the assumptions and proofs. It applies established Gödel and Rosser machinery; Li–Liu already state a Rosser monotiling consequence in a much larger fixed dimension. The potential refinement here is one tile in dimension three. No coordinate list for the particular independent tile has been generated. [Prior work](references.md#s5), [logical sources](references.md#s9).

## Prior work and proposed distinction

The potential advance is **one tile of the whole lattice in fixed dimension three**.

| Related result | Distinction |
| :--- | :--- |
| [Greenfeld–Tao](references.md#s2) | The lattice dimension and a periodic target subset can vary with the input. |
| [Li–Liu's September 2026 draft](references.md#s5) | Already claims one-tile undecidability in a fixed, very large dimension. |
| [Kim's August 2026 revision](references.md#s6) | Proves undecidability with two connected tiles in dimension three. |
| [OpenAI manuscript 155](references.md#s1) | Supplies the cyclic encoding machinery and an aperiodicity theorem, rather than the arbitrary-input undecidability statement. |

The searches recorded here did not locate an earlier exact dimension-three theorem. They do **not** establish that nobody has observed it. This note does not claim to be the first fixed-dimensional undecidability result, nor to invent the published encoding and lifting theorems.

## Interpretation and limits

- The target is infinite space. Every fixed finite exact-cover instance is decidable by finite enumeration.
- Only translations are allowed. Connected shapes, rotations, reflections, and arbitrary real translation vectors are not part of the stated theorem.
- The shape's size and the lattice-gas interaction range can grow with the input. No practical complexity bound or material realization is supplied.
- The theorem and its corollaries have a complete proposed argument, but no independent specialist review or formal proof is recorded.
- The finite computation in the verification record checks a reduced model of the shared-seed equations. It does not certify the full theorem.

## Provenance and revisions

The source construction is pinned to OpenAI math commit [`adc7f1241b42e322a6451854ab7e4b4c146bf78a`](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a). Its graph, cycle, activation, shared-seed, and stacking constructions are credited explicitly. The new argument is the effective decorated two-prime extension and its composition with the cited theorems.

Roger Malcolm III directed the investigation and the development of this finding. Research, drafting, source inspection, and separate adversarial checks were performed using GPT-6. These were multiple passes within the same AI-assisted investigation, not independent external peer review. The [verification record](verification.md) documents the checks and their limits.

**Suggested citation:** Roger Malcolm III. *Undecidability of translational monotiling in dimension three.* Legendary, Finding 002, version 0.2.0, 2026. Research assistance: GPT-6. [Repository note](https://github.com/LmeowLaunchpad/Legendary/tree/main/findings/002-three-dimensional-monotiling). For a fixed version, replace `main` with the commit being cited.

| Version | Change |
| :--- | :--- |
| `0.2.0` | October 8, 2026: add the conditional Gödel and Rosser supplement, finite-test and periodic-energy consequences, source attribution, and review record. Main reduction unchanged. |
| `0.1.1` | October 8, 2026: repair unsupported GitHub macros and protect inline math from Markdown parsing. Mathematical claims unchanged. |
| `0.1.0` | October 8, 2026: initial proof draft, dependency record, finite-test and lattice-gas corollaries, prior-art audit, and reproducible reduced seed check. |
