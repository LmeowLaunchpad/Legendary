# Verification record

**Author:** Roger Malcolm III. **Research and drafting assistance:** GPT-6, including multiple agent checks. These agents were part of the same AI-assisted investigation, not independent external reviewers.

**Status:** a conditional deduction reviewed by AI assistants, not an independent certification of the upstream theorem or independent peer review. **Investigation date:** 2026-10-07 (America/New_York). **Upstream snapshot:** `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

The premise is the September 23 manuscript's existence of a finite field $K$ of characteristic two, a finitely presented group $G$, and $a,b\in K[G]$ with $ab=1$ and $ba\ne1$. It does **not** require or assert $K=\mathbb F_2$. The separate October 4 torsion-free claim is unnecessary. [Source S1](references.md#s1)

## Checks performed

| Item | Scope and outcome |
| --- | --- |
| Upstream statement | Read the manuscript's main theorem and relevant cellular-automaton transfer, and compared its scope with the formalization documentation. The full incidence, embedding, and construction proof was not independently audited. |
| Lean evidence | Inspected `OAI.KaplanskyCounterexample.finitelyPresented_counterexample` in `OAI/RingTheory/DirectFiniteness/FinitelyPresented.lean`, the scope document, and Comparator configuration. The declaration includes finite presentability and the finite-field one-sided inverse. **No Lean build, Comparator run, or complete dependency/axiom audit was performed.** [Source S5](references.md#s5) |
| Published entropy transfer | Checked Seward II's Theorems 1.10 and 1.12, Corollary 1.8, and Theorem 1.11 (= 6.7). They give finite $h_{\mathrm{sup}}(G)$ from the premise, followed by $h_{\mathrm{sup}}(T\times G)=0$. [Source S2](references.md#s2) |
| Infinite-entropy case | Checked Corollary 7.7. This is essential because $h_{\mathrm{sup}}$ takes a supremum only over **finite** entropy values. The corollary also excludes infinite-entropy free ergodic actions when that supremum is zero. [Source S2](references.md#s2) |
| Group hypotheses | Checked Thompson $T$'s finite presentability and circle model. Dyadic rotations give finite subgroups of unbounded order. A direct-product presentation adds finitely many cross-generator commutators. [Source S4](references.md#s4) |
| Generators and interpretation | Checked the prescribed-distribution generator theorem and the measurable coding argument. The binary process has an almost-everywhere equivariant inverse; its coordinates are not asserted to be independent. [Source S3](references.md#s3) |
| Additional consequences | Checked the elementary contradiction between Bernoulli-normalized entropy and an upper bound by every finite generator's Shannon entropy. Also checked the finite-neighborhood encoder obstruction by Fubini and the finite-transcript obstruction to exact recovery of a continuous random variable. |

These were separate checks within one GPT-6-assisted investigation. Agreement between assistants is not external mathematical validation. The downstream deduction has not been formalized in Lean here.

## Search for prior notice

The investigation screened the repository's catalogue of 722 manuscripts in 372 families, then read selected sources. It was **not** a full-text or proof audit of all 722 manuscripts.

Text searches covered the complete catalogue; the downloaded TeX, Markdown, and bibliography files of the September 23 characteristic-two and September 26 odd-characteristic direct-finiteness papers; and all seven sections of the October 4 torsion-free paper. Searches included `Rokhlin`, `Rokhlin entropy`, `Seward`, and `Bernoulli`; further searches in the characteristic-two and torsion-free source trees included `Krieger`, `Thompson`, and `entropy`. No discussion of this entropy application was found in that scope. The catalogue's occurrences of Rokhlin concern other problems.

Targeted web queries on 2026-10-07 included:

```text
"OpenAI" "Rokhlin" "entropy"
"OpenAI" "Kaplansky" "Rokhlin"
"openai/math" "Rokhlin"
"openai/math" "Bernoulli" entropy
"Kaplansky" "Rokhlin" 2026
"finitely presented" "Rokhlin entropy" zero
"Kaplansky" "Seward" "counterexample"
"direct finiteness" "zero Rokhlin"
"OpenAI" "zero Rokhlin entropy"
"Kaplansky" "entropy" "October" "2026"
"Seward" "OpenAI" math
"Thompson" "Rokhlin" entropy
"all" "free ergodic" "zero Rokhlin entropy" group
"direct finiteness" "binary" entropy
```

No relevant returned result explicitly announced this application. Seward's existing conditional connection was readily found and is credited; the mathematical connection itself is not new.

The full HTML of the public survey listed under [discussion checks](references.md#discussion-checks) was extracted and searched. It contained no `Seward`, `Rokhlin entropy`, or `zero entropy`; its direct-finiteness discussion covered nonsoficity, surjunctivity, and determinant consequences. The visible README of the second linked verification repository was also checked and contained no `Rokhlin`. Its other files, issues, and discussions were not exhaustively searched. These checks concern prior discussion, not mathematical correctness.

**Priority statement:** we did not find this application in the catalogue, direct-finiteness sources, or public discussions checked. We do not claim that nobody noticed it, that it is unpublished everywhere, or that it is the most consequential implication in the entire collection.

## Remaining limitations

The starting theorem remains an assumed premise in this record. The implication uses established results of Seward and the classical properties of Thompson $T$; it does not independently establish the new group-algebra counterexample. The coding conclusion is measurable, with null sets allowed. It supplies no finite/local or efficient encoder, no independent binary output measure, and no violation of finite-source Shannon coding bounds. It also does not prove that Bernoulli shifts with unequal base entropies are isomorphic.
