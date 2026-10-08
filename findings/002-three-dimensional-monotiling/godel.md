# 002 · Gödel independence for one three-dimensional tile

**Roger Malcolm III · Research and drafting assistance using GPT-6**

[Overview](README.md) · [Main proof](proof.md) · [Verification record](verification.md) · [References](references.md)

| Record | Value |
| :--- | :--- |
| Version | `0.2.0` |
| Date | October 8, 2026 |
| Mathematical status | Conditional on the correctness of Finding 002's proof |
| Review status | AI-assisted source and argument checks; no external specialist review or formal verification |

For each consistent, computably axiomatized extension of ZFC, the proposed compiler yields a finite shape that tiles the three-dimensional lattice, although that theory can prove neither tileability nor its negation. Its associated lattice gas has exactly zero minimum energy density, while every periodic finite-volume minimum is positive.

No coordinate list for such an independent tile has been generated. The logical machinery is established: Meyerovitch–Sanadhya–Solomon provide ZFC provability transfer in Corollary 1.4, and Li–Liu's September 2026 draft applies Rosser's theorem to monotiling in a much larger fixed dimension in Section 7, PDF page 25. The proposed geometric distinction here is **one tile of the whole lattice in dimension three**, not a new incompleteness theorem or a certified priority claim. [S3](references.md#s3), [S5](references.md#s5), [S9](references.md#s9).

<a id="g1"></a>

## G1. The compiler and its proof-theoretic interface

Let $`B_n=[-n,n]^3\cap\mathbb Z^3`$. For a finite nonempty shape $`F`$, let $`P(F,n)`$ assert the existence of an assignment $`\theta:B_n-F\to\{0,1\}`$ satisfying

```math
\sum_{f\in F}\theta(x-f)=1
\qquad(x\in B_n).
```

Origins outside the inspected cube are permitted. Finite enumeration decides this predicate. [Lemma 14](proof.md#completion) gives

```math
\Phi_F:=\forall n\,P(F,n)
\quad\Longleftrightarrow\quad
F\text{ tiles }\mathbb Z^3.
```

Use the standard arithmetic encoding of these finite tests; equivalently, $`\Phi_F`$ says that the search for a failed test never halts. This is a $`\Pi^0_1`$ sentence.

Combining the machine-to-domino reduction with [Theorem 1](proof.md#main-theorem) gives a total computable compiler $`C`$ such that

```math
\Phi_{C(e)}\quad\Longleftrightarrow\quad
\mathrm{NonHalts}(e).
```

Here programs have a fixed designated input. The independence transfer below requires this equivalence and the compiler's totality **provable in the base theory**, not merely true externally. We take ZFC as that base, conditional on the main argument being correct as an ordinary ZFC proof. Its ingredients are finite constructions, standard computation encodings, and countable compactness. This does not claim a completed proof-assistant formalization or that every weak arithmetic theory proves the reduction.

<a id="g2"></a>

## G2. Rosser independence from consistency alone

**Theorem G2.** Under G1, an effective procedure assigns to each presentation of a consistent computably enumerable theory $`T\supseteq\mathrm{ZFC}`$ a finite nonempty $`G_T\subset\mathbb Z^3`$ that tiles, with

```math
T\nvdash\Phi_{G_T},
\qquad
T\nvdash\neg\Phi_{G_T}.
```

**Proof.** Encode proofs with finite certificates for any enumerated axioms, making proof verification decidable. The effective diagonal lemma produces a Rosser sentence $`R_T`$ whose equivalence to the following statement is provable in arithmetic:

```math
\forall p\left(
\mathrm{Prf}_T(p,\ulcorner R_T\urcorner)
\Longrightarrow
\exists q\le p\,
\mathrm{Prf}_T(q,\ulcorner\neg R_T\urcorner)
\right).
```

If $`T`$ proved $`R_T`$ with code $`p`$, consistency would exclude every proof of its negation. Checking the finitely many codes $`q\le p`$ would then let $`T`$ prove $`\neg R_T`$, a contradiction. If $`T`$ proved $`\neg R_T`$ with code $`q`$, consistency would exclude proofs of $`R_T`$. The finitely many cases $`p<q`$ could be checked; for $`p\ge q`$, the known negative proof supplies the witness. Thus $`T`$ would prove $`R_T`$, again a contradiction. Hence neither sentence is provable, and $`R_T`$ is true because there is no positive proof. This is the standard Rosser argument. [S9](references.md#s9).

Let $`M_T`$ search for a code $`p`$ violating the displayed condition. Put $`G_T=C(M_T)`$. Arithmetic verifies the search's meaning, and G1 yields

```math
\mathrm{ZFC}\vdash
\bigl(\Phi_{G_T}\Longleftrightarrow R_T\bigr).
```

The two unprovabilities transfer through this equivalence. Truth of $`R_T`$ gives actual tileability. Every construction is effective from an axiom-enumerator index; producing the finite shape does not wait for the search to halt. $`\square`$

<a id="g3"></a>

## G3. Every finite local test is provable; no fully periodic tiling exists

**Corollary G3.** For $`F=G_T`$, each fixed standard $`n`$ satisfies $`T\vdash P(F,n)`$, but $`T\nvdash\forall n\,P(F,n)`$. Moreover, $`F`$ has no fully periodic tiling.

**Proof.** Actual tileability supplies a finite satisfying assignment for each cube, which ZFC can verify. A fully periodic tiling would similarly provide a finite-index period lattice and a pattern on its finite quotient. Checking the exact-cover equations there, including multiplicities, would prove global tileability in ZFC and hence in $`T`$, contradicting G2. $`\square`$

A brute-force algorithm produces each finite covering witness and its proof. Its universal success is true externally but unprovable in $`T`$. This does not make the running time on this fixed shape noncomputable. The periodicity conclusion excludes rank-three period lattices; it does not exclude rank-one or rank-two periods or establish that every tiling is noncomputable.

<a id="g4"></a>

## G4. Independent zero energy and positive periodic minima

For $`a\in\{0,1\}^{\mathbb Z^3}`$, define

```math
h_x(a)=\left(\sum_{f\in F}a_{x-f}-1\right)^2,
\qquad
e_0(F)=\min_{\mu\in\mathcal M}\int h_0\,d\mu,
```

where $`\mathcal M`$ consists of translation-invariant Borel probability measures. [Corollary 16](proof.md#lattice-gas) proves existence of this minimum and

```math
e_0(F)=0\quad\Longleftrightarrow\quad\Phi_F.
```

The interaction has one binary species, finite-range pairwise repulsions, and a uniform chemical potential. Its range varies with the shape.

**Corollary G4.** For $`F=G_T`$, the actual energy density is zero, but $`T`$ proves neither $`e_0(F)=0`$ nor $`e_0(F)>0`$. Let $`r\ge1`$ satisfy $`F\subseteq[-r,r]^3`$, put $`H=\max\{1,(|F|-1)^2\}`$, and let $`u_L`$ be the exact minimum mean energy among arrays with period $`L`$ in every coordinate. Then, for $`L>2r`$,

```math
\frac1{L^3}\le u_L\le\frac{6rH}{L},
\qquad e_0(F)=0.
```

**Proof.** The energy equivalence is provable in the intended ZFC base, so G2 transfers to the two energy claims. Every local energy is a nonnegative integer. Zero energy on a periodic array would give a fully periodic tiling, excluded by G3. Its sum over an $`L`$-cell is therefore at least one, giving the lower bound. The boundary estimate in Corollary 16 gives

```math
0\le u_L-e_0(F)\le\frac{6rH}{L},
```

which proves the upper bound. $`\square`$

For each fixed positive rational $`\varepsilon`$, a finite periodic pattern witnesses $`e_0(F)<\varepsilon`$. ZFC verifies its energy and the invariant measure obtained by averaging its translates, so $`T`$ proves that particular bound. It cannot prove the universal exact-zero assertion. These are **periodic** finite-volume minima; they are not the finite local tests in G3, which allow boundary crossings.

This gives no quantum spectral-gap result, positive-entropy assertion, finite-temperature transition, or material realization.

<a id="g5"></a>

## G5. An entire effective catalogue

Let $`T_0,T_1,\ldots`$ be uniformly computably enumerable extensions of the same ZFC base whose combined axioms are consistent. Their deductive closure $`U`$ is consistent and computably enumerable. G2 gives one shape independent of $`U`$ and therefore of every $`T_i`$.

Likewise, starting with a consistent effective $`T_0\supseteq\mathrm{ZFC}`$, set $`T_{n+1}=T_n+\Phi_{G_{T_n}}`$. Independence ensures consistency at each stage. The ascending union remains consistent and computably enumerable, and has another independent shape. This is ordinary incompleteness for a preselected effective sequence, not independence from every possible axiom system.

## Revision log

| Version | Date | Change |
| :--- | :--- | :--- |
| `0.2.0` | October 8, 2026 | Added the conditional Rosser supplement, finite-test and periodicity deductions, energy bounds, and effective-catalogue consequence. |
