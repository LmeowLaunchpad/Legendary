# Legendary

**Mathematical findings, with the arguments and evidence attached.**

Research by **Roger Malcolm III**, using **GPT-6** and **Fable 5.1**.

A growing collection of research notes on substantial mathematical consequences. Each finding has a stable identifier, a readable overview, a detailed argument, primary references, and an explicit verification record.

> [!IMPORTANT]
> Findings 001, 003 and 004 are **conditional on upstream claimed theorems**. Finding 002 is a **proposed theorem with a complete proof draft**. The findings have undergone AI-assisted checks; no external peer review or formal verification of these downstream arguments is recorded here. Publication is not a claim of established novelty.

## Findings

| ID | Finding | Mathematical status | Review status |
| :--- | :--- | :--- | :--- |
| **001** | [From a group-algebra counterexample to universal zero Rokhlin entropy](findings/001-rokhlin-entropy-collapse/) | Conditional corollary | AI-assisted checks; no external review recorded |
| **002** | [Undecidability of translational monotiling in dimension three](findings/002-three-dimensional-monotiling/) | Proposed theorem; complete proof draft | AI-assisted checks; no external review recorded |
| **003** | [Stationary Coulomb crystallization from Gaussian minimality](findings/003-stationary-coulomb-crystallization/) | Conditional theorem; complete proof draft | AI-assisted checks; no external review recorded |
| **004** | [Euclidean rings of integers in real abelian fields from uniform primitive roots](findings/004-euclidean-real-abelian-fields/) | Conditional theorem; complete proof draft | AI-assisted checks; no external review recorded |

### Latest finding · 004

Conditional on three statements of OpenAI manuscript 029, every **real abelian number field of class number one is Euclidean**. In particular every real quadratic principal ideal domain is Euclidean, the statement Weinberger proved in 1973 under the generalized Riemann hypothesis and Narkiewicz reduced in 2007 to at most two possible exceptions.

The proof re-runs the manuscript's primitive-root engine with a unit of the field in place of an integer base. Two new ingredients make this work: the Kummer field of a unit has discriminant controlled by $`q^q`$ alone, and primes $`p\equiv-1`$ modulo the conductor with $`p\equiv3\pmod4`$ split completely in a real field while making the unit $`-1`$ a quadratic non-residue, which handles the prime 2. Graves's growth criterion then gives the Euclidean algorithm. The same count gives infinitely many primes with a Fibonacci primitive root, Shanks's 1972 question, previously known only under GRH. One premise of the source depends in turn on a second unformalized manuscript; the note records the full dependency chain and its own finite checks.

**[Read the overview →](findings/004-euclidean-real-abelian-fields/)** · [Proof](findings/004-euclidean-real-abelian-fields/proof.md) · [Verification record](findings/004-euclidean-real-abelian-fields/verification.md) · [References](findings/004-euclidean-real-abelian-fields/references.md)

### Finding · 003

Conditional on the triangular lattice minimizing every Gaussian pair energy, a proposed stationary equality argument classifies **every stationary planar logarithmic Coulomb ground state** as a mixture of uniformly translated, rotated triangular lattices.

The proof passes from an energy excess bound to an exact minimum separation, then uses local Voronoi rigidity. Consequences include infinite specific relative entropy of every ground state and the triangular structure of every zero-temperature cluster law of the stationary free-energy variational model. The note credits Petrache–Serfaty for the earlier universal-optimality-to-Coulomb connection and distinguishes the new conditional argument from its source premise.

**[Read the overview →](findings/003-stationary-coulomb-crystallization/)** · [Proof](findings/003-stationary-coulomb-crystallization/proof.md) · [Verification record](findings/003-stationary-coulomb-crystallization/verification.md) · [References](findings/003-stationary-coulomb-crystallization/references.md)

### Finding · 002

A proposed effective reduction encodes arbitrary domino rules into **one finite tile of the whole three-dimensional integer lattice**. If the proof is correct, this gives the sharp dimension boundary: the translational monotiling problem is decidable in dimensions one and two, and undecidable in every fixed dimension at least three.

The argument extends a cyclic encoding from OpenAI manuscript 155 and uses published theorems of Greenfeld–Tao and Meyerovitch–Sanadhya–Solomon. The note includes a full proof draft, a precise lattice-gas consequence, the prior-art comparison, and a reproducible reduced finite check. A Gödel supplement derives conditional independence results and explains how every finite local test can be provable while whole-space tileability remains independent of the chosen axiom system.

**[Read the overview →](findings/002-three-dimensional-monotiling/)** · [Proof](findings/002-three-dimensional-monotiling/proof.md) · [Gödel supplement](findings/002-three-dimensional-monotiling/godel.md) · [Verification record](findings/002-three-dimensional-monotiling/verification.md) · [References](findings/002-three-dimensional-monotiling/references.md)

### Featured finding · 001

If the cited finitely presented group-algebra counterexample is correct, there is a finitely presented group $H$ for which **every free ergodic probability-preserving action has zero Rokhlin entropy**. This includes a Bernoulli shift with independent continuous labels.

The argument combines the claimed counterexample with Brandon Seward's published theorems. It also yields binary generating observations with arbitrarily small probability of a 1, and an obstruction to extending a familiar pair of entropy requirements to every countable group.

**[Read the overview →](findings/001-rokhlin-entropy-collapse/)** · [Proof](findings/001-rokhlin-entropy-collapse/proof.md) · [Verification record](findings/001-rokhlin-entropy-collapse/verification.md) · [References](findings/001-rokhlin-entropy-collapse/references.md)

## How to read this collection

- **Overview:** what a finding says and why it matters.
- **Proof:** precise assumptions, deductions, and limitations.
- **Verification record:** what was checked, what remains unresolved, and the scope of any prior-art search.
- **References:** the sources and exact versions on which the argument depends.

Mathematical status and review status are recorded separately. A conditional deduction can have a complete argument while its premise remains unverified. Agreement among AI agents is not independent human peer review.

## Keeping the record useful

[Research standards](docs/RESEARCH_STANDARDS.md) · [Finding template](docs/FINDING_TEMPLATE.md) · [Corrections and contributions](CONTRIBUTING.md) · [Machine-readable index](findings/index.json)

For a correction or an earlier source for a claimed consequence, [open a correction or prior-art report](https://github.com/LmeowLaunchpad/Legendary/issues/new?template=correction.yml). Please identify the finding and the exact claim involved.

When citing a note, include its title, finding ID, version, and a commit-specific GitHub URL. Git history records revisions; each note also carries a short revision log.

---

Maintained by **Roger Malcolm III** ([LmeowLaunchpad](https://github.com/LmeowLaunchpad)). The findings were researched and drafted using **GPT-6** (findings 001 to 003) and **Fable 5.1** (finding 004), including multiple agent checks. Each note documents its mathematical sources and the scope of that assistance.
