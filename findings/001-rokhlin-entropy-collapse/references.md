# References

Repository links below are pinned to `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. The theorem numbers for Seward refer to the linked author manuscripts. Bibliographic metadata was checked against the publisher's record, author manuscripts, and the digitized journal record during the 2026-10-07 investigation.

<a id="s1"></a>

**S1. Upstream premise.** *A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two*, September 23, 2026, in the OpenAI math repository.

- [Pinned manuscript directory](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026).
- [Main theorem and scope](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/build/sections/01-introduction.tex).
- [Cellular-automaton transfer](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/build/sections/06-cellular-automata.tex).

This is the conditional input: a finitely presented group with a non-directly-finite group algebra over a finite characteristic-two field.

<a id="s2"></a>

**S2. Brandon Seward.** *Krieger's finite generator theorem for actions of countable groups II*. **Journal of Modern Dynamics 15 (2019), 1–39.** DOI: [10.3934/jmd.2019012](https://doi.org/10.3934/jmd.2019012).

- [Publisher's record](https://www.aimsciences.org/article/doi/10.3934/jmd.2019012).
- [Author manuscript](https://mathweb.ucsd.edu/~bseward/Files/krieger2.pdf).
- [arXiv:1501.03367](https://arxiv.org/abs/1501.03367).

Relevant items: Theorem 1.3 (a finite-block entropy deficit), Corollary 1.8 (the direct-finiteness connection), Theorem 1.9 (almost-independent generating observations on a specified finite window), Theorem 1.10 (= 6.6; finite-base Bernoulli entropy), Theorem 1.11 (= 6.7; the direct-product argument), Theorem 1.12 (infinite-base entropy), and Corollary 7.7 (positive finite versus infinite entropy). Theorem 1.1 restates the generator theorem from Part I.

<a id="s3"></a>

**S3. Brandon Seward.** *Krieger's finite generator theorem for actions of countable groups I*. **Inventiones Mathematicae 215 (2019), 265–310.** DOI: [10.1007/s00222-018-0826-9](https://doi.org/10.1007/s00222-018-0826-9).

- [Author manuscript](https://www.math.ucsd.edu/~bseward/Files/krieger1.pdf).
- [arXiv:1405.3604](https://arxiv.org/abs/1405.3604).

Theorem 1.1 supplies a generating partition with prescribed probability vector when its Shannon entropy strictly exceeds the action's Rokhlin entropy. The journal metadata is also recorded in Part II's published bibliography, reference 31.

<a id="s4"></a>

**S4. J. W. Cannon, W. J. Floyd, and W. R. Parry.** *Introductory notes on Richard Thompson's groups*. **L'Enseignement Mathématique 42 (1996), 215–256.**

- [Digitized journal article](https://www.e-periodica.ch/digbib/view?pid=ens-001%3A1996%3A42%3A%3A416).
- [Full article PDF, hosted by Emmanuel Breuillard](https://www.imo.universite-paris-saclay.fr/~emmanuel.breuillard/Cannon.pdf).

The introduction and Section 5 give the relevant facts about Thompson's circle group $T$. Its circle model contains the rotations by $2^{-j}$, yielding finite cyclic subgroups of unbounded order.

<a id="s5"></a>

**S5. Upstream formalization evidence.** OpenAI math repository, the same pinned snapshot.

- [Family 197 scope document](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/197.md).
- [Lean declaration and proof wrapper](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/RingTheory/DirectFiniteness/FinitelyPresented.lean).
- [Comparator challenge](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/KaplanskyFinitelyPresented.lean).
- [Comparator configuration](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/KaplanskyFinitelyPresented.json).

The inspected declaration is `OAI.KaplanskyCounterexample.finitelyPresented_counterexample`. Reading these files is not a substitute for rebuilding Lean, running Comparator, or auditing the complete dependency closure. None of those checks was performed in this investigation.

<a id="discussion-checks"></a>

## Public discussion checked for prior notice

These are **search-scope evidence only**, not primary mathematical support or independent validation of this finding. Accessed during the 2026-10-07 investigation.

- [Public survey: *openai/math: 372 claimed theorems, 26 million lines of Lean, and what the green tick means*](https://ai.thesatyajit.com/articles/openai-math). Its full HTML was extracted and searched for the terms reported in [the verification record](verification.md).
- [M0-AR/openai-math-verify-2026](https://github.com/M0-AR/openai-math-verify-2026). The visible README was inspected; other files and discussions were not exhaustively searched.

These limited checks establish no discovery priority.
