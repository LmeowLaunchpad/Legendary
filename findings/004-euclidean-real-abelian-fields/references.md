# References and dependency map

[← Finding 004](README.md) · [Proof](proof.md) · [Verification record](verification.md)

**Author:** Roger Malcolm III. **Research assistance:** Fable 5.1. **Version:** `0.1.1`.

The proposed contribution is the transfer of the manuscript's prime-construction and uniform-splitting machinery from integer bases to units of real abelian fields, and the resulting conditional Euclidean and primitive-root theorems. The analytic inputs, the Euclidean criterion, and the earlier conditional and partial results are credited below. A source's presence here does not mean the present investigation independently verified its entire proof.

| Reference | Role |
| :--- | :--- |
| S1 | The three claimed statements used as explicit premises: uniform zero-free strip, prime construction, uniform explicit formula. |
| S2 | The growth criterion: enough prime ideals with unit-generated residue fields force a Euclidean algorithm. |
| S3–S4 | Harper's unconditional method and the Harper–Murty theorem for unit rank at least four. |
| S5 | The Clark–Murty criterion for totally real Galois fields. |
| S6 | Weinberger's GRH-conditional theorem, the statement made conditional on S1 here. |
| S7 | Narkiewicz's "at most two exceptions" theorem for real quadratic fields. |
| S8 | Lenstra's GRH-conditional treatment of Artin's conjecture for units and Euclid's algorithm. |
| S9 | Hooley's GRH-conditional proof of Artin's conjecture, the template for the Kummer-field splitting argument. |
| S10 | The unconditional sieve results of Gupta–Murty and Heath-Brown, the source of the large-prime-factor device. |
| S11 | Survey of Artin's conjecture, including the Euclidean section and the Fibonacci primitive root problem. |
| S12 | Shanks's Fibonacci primitive root conjecture and Sander's GRH-conditional result. |
| S13 | Standard algebraic number theory used without further comment. |
| S14 | The published record for large prime factors of $`p-1`$, against which the strength of Hypothesis B is weighed. |

<a id="s1"></a>
## S1 · OpenAI source premises

OpenAI, *Primitive roots for every admissible integer base*, manuscript family 029, October 4, 2026. Three statements of this manuscript are used as explicit premises: Theorem 1.2 (a zero-free strip $`\Re s>1-10^{-6}`$ for every finite-order Hecke $`L`$-function of every cyclotomic field containing $`\zeta_{12}`$, uniform in the field and the character), Proposition 2.1 (primes $`p\equiv u\pmod M`$ in $`(x,2x)`$ with $`p-1=crQ`$, $`Q>x^{0.9}`$ prime, and all prime factors of $`r`$ in a prescribed middle range, in number $`\gg x/(\log x)^2`$), and Lemma 9.2 (a smooth explicit formula for prime ideals of an arbitrary number field with a zero-free strip, uniform in the field).

- [Pinned manuscript directory](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026).
- [Manuscript PDF](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/primitive-roots-all-integer-bases.pdf).
- [Theorems 1.1 and 1.2](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/01-introduction.tex) · [Propositions 2.1 and 2.2 and the splitting test](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/01a-reduction.tex) · [Section 9, uniform splitting](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/07-splitting.tex) · [Section 12, the prime construction](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/12-construction.tex).
- Formalization status: this family has **no entry** in the repository's [formalization catalogue](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/formalization.yaml) and no `lean/docs` page at the pinned commit. The premises are unformalized claims.

The proof of Proposition 2.1 (Section 12 of the manuscript) imports its bilinear "marked Type II" estimate, stated as the manuscript's Theorem 10.1, from Theorem 3.1 of a second manuscript, family 011: OpenAI, *The Poisson–Dirichlet law for prime predecessors*, September 24, 2026. That family is likewise absent from the formalization catalogue.

- [Pinned family-011 manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/paper.pdf).

The version pin is `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. The present theorem uses only the three statements named above, not the manuscript's headline theorem on integer bases, and it does not use any numerical constant from the zero-free strip beyond its existence. The [verification record](verification.md) records which parts of the source were read and which were used as black boxes.

<a id="s2"></a>
## S2 · The growth criterion

Hester Graves, *Growth results and Euclidean ideals*, Journal of Number Theory **133** (2013), no. 8, 2756 ff.

[arXiv:1008.2479](https://arxiv.org/abs/1008.2479).

Theorem 2: if $`K`$ is a number field with infinitely many units and $`C`$ an ideal whose class generates the class group, and if the prime ideals $`\mathfrak p`$ in the class of $`C`$ with $`\mathcal O_K^{\times}\twoheadrightarrow(\mathcal O_K/\mathfrak p)^{\times}`$ and $`N\mathfrak p\le x`$ number $`\gg x/(\log x)^2`$, then $`C`$ is a Euclidean ideal. With $`C=\mathcal O_K`$ and class number one this is exactly the statement that $`\mathcal O_K`$ is a Euclidean domain. This generalizes Harper's criterion (S3) and the Harper–Murty criterion (S4) and is used here as a black box.

<a id="s3"></a>
## S3 · Harper's unconditional method

Malcolm Harper, *$`\mathbb Z[\sqrt{14}]`$ is Euclidean*, Canadian Journal of Mathematics **56** (2004), no. 1, 55–70.

[Cambridge Core](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/is-euclidean/A20F443C0FDB4E3935DC1402C1060D74).

The first unconditional proof that a specific non-norm-Euclidean real quadratic ring is Euclidean. Its large-sieve growth criterion is the ancestor of S2. Harper's method handles one field at a time and relies on a computation of admissible primes; it does not by itself treat every real quadratic field of class number one.

<a id="s4"></a>
## S4 · The Harper–Murty theorem

Malcolm Harper and M. Ram Murty, *Euclidean rings of algebraic integers*, Canadian Journal of Mathematics **56** (2004), no. 1, 71–76.

[Cambridge Core](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/euclidean-rings-of-algebraic-integers/B66EAE5371EDD740117CF87710BFBCA1).

Unconditionally, a Galois number field of class number one with unit rank at least four is Euclidean. The unit-rank restriction comes from the sieve input available at the time: unconditionally one could only show that a product of several independent units generates enough residue fields. Real quadratic, cubic and quartic fields are outside its scope; closing that gap is the content of the present note.

<a id="s5"></a>
## S5 · The Clark–Murty criterion

David A. Clark and M. Ram Murty, *The Euclidean algorithm for Galois extensions of $`\mathbb Q`$*, Journal für die reine und angewandte Mathematik **459** (1995), 151–162.

For totally real Galois fields this replaces the earlier size conditions by the existence of a suitably large set of admissible primes. Together with S3 and S4 it is the published chain through which a primitive-root count becomes a Euclidean algorithm.

<a id="s6"></a>
## S6 · Weinberger's conditional theorem

Peter J. Weinberger, *On Euclidean rings of algebraic integers*, in: Analytic Number Theory, Proceedings of Symposia in Pure Mathematics **24**, American Mathematical Society (1973), 321–332.

Assuming the generalized Riemann hypothesis for Dedekind zeta functions of Kummer extensions, every ring of integers with infinitely many units is Euclidean if and only if it is a principal ideal domain. The present note replaces that hypothesis, for real abelian fields, by the explicit premises in S1.

<a id="s7"></a>
## S7 · At most two exceptions

Władysław Narkiewicz, *Euclidean algorithm in small Abelian fields*, Functiones et Approximatio Commentarii Mathematici **37** (2007), no. 2, 337–340.

[DOI](https://doi.org/10.7169/facm/1229619657).

A small change in the Harper–Murty argument shows that at most two real quadratic fields of class number one, and at most one normal cubic field of class number one, fail to be Euclidean. The present note, if its premises hold, removes those possible exceptions. This source bounds what is genuinely new here.

<a id="s8"></a>
## S8 · Artin's conjecture for units, under GRH

H. W. Lenstra, Jr., *On Artin's conjecture and Euclid's algorithm in global fields*, Inventiones Mathematicae **42** (1977), 201–224.

[Author-hosted PDF](https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1977d/art.pdf).

Under GRH this treats the generalized Artin conjecture for subgroups of units of global fields and its connection with Euclid's algorithm, and gives the density criterion. Its Theorem 8.1 is the GRH-conditional source for the Fibonacci primitive root statement in S12. The unit-generated primitive-root counts proved conditionally here were previously available only through this GRH-conditional route.

<a id="s9"></a>
## S9 · Hooley's template

Christopher Hooley, *On Artin's conjecture*, Journal für die reine und angewandte Mathematik **225** (1967), 209–220.

The proof of Artin's conjecture under GRH for the Kummer fields $`\mathbb Q(\zeta_q,a^{1/q})`$. The present argument follows the same three-range division of the prime divisors $`q`$ of $`p-1`$, with GRH replaced by the uniform zero-free strip of S1 in the middle range and by a norm-size count in the large range.

<a id="s10"></a>
## S10 · Unconditional sieve inputs

Rajiv Gupta and M. Ram Murty, *A remark on Artin's conjecture*, Inventiones Mathematicae **78** (1984), 127–130. D. R. Heath-Brown, *Artin's conjecture for primitive roots*, Quarterly Journal of Mathematics Oxford (2) **37** (1986), 27–38.

[Gupta–Murty, DOI](https://doi.org/10.1007/BF01388719).

These unconditional results introduced the device of restricting to primes $`p`$ for which $`p-1`$ has a very large prime factor, which the manuscript in S1 and the present note both use. Heath-Brown's theorem gives Artin's conjecture for all but at most two prime bases; it does not give it for any specified base or unit.

<a id="s11"></a>
## S11 · Survey

Pieter Moree, *Artin's primitive root conjecture — a survey*, Integers **12A** (2012), John Selfridge memorial issue, with contributions by Hester Graves on Euclidean domains.

[arXiv:math/0412262](https://arxiv.org/abs/math/0412262).

Section 9.6 states Harper's criterion in the form used here and records the Harper–Murty, Petersen–Murty and Narkiewicz results. The open-problem list includes the Fibonacci primitive root problem. This survey was the primary check that the unconditional Euclidean statement for real quadratic fields of class number one was open before the OpenAI release.

<a id="s12"></a>
## S12 · Fibonacci primitive roots

Daniel Shanks, *Fibonacci primitive roots*, The Fibonacci Quarterly **10** (1972), no. 2, 163–168, 181. J. W. Sander, *On Fibonacci primitive roots*, The Fibonacci Quarterly **28** (1990), no. 1, 79–80.

[Shanks, scanned article](https://www.mathstat.dal.ca/FQ/Scanned/10-2/shanks-a.pdf) · [Sander, scanned article](https://www.mathstat.dal.ca/FQ/Scanned/28-1/sander.pdf).

Shanks asked whether infinitely many primes have a primitive root $`g`$ with $`g^2\equiv g+1\pmod p`$ and conjectured a density. Sander proved the density under GRH. The corollary in the present note gives the infinitude, with a lower bound of order $`x/(\log x)^2`$, conditional on S1.

<a id="s13"></a>
## S13 · Standard background

Jürgen Neukirch, *Algebraic Number Theory*, Grundlehren der mathematischen Wissenschaften **322**, Springer (1999).

Used for the Kronecker–Weber theorem, the congruence description of splitting in abelian fields, Kummer theory, discriminants of composita with coprime discriminants, and the factorization of Dedekind zeta functions of abelian extensions into Hecke $`L`$-functions (Chapter VII, Corollary 10.5 and Theorem 10.6). No result beyond standard textbook material is taken from this source.

<a id="s14"></a>
## S14 · Large prime factors of shifted primes

R. C. Baker and G. Harman, *The Brun–Titchmarsh theorem on average*, in: Analytic Number Theory, Volume 1 (Allerton Park, 1995), Progress in Mathematics **138**, Birkhäuser (1996), 39–103.

[arXiv:2508.18285](https://arxiv.org/abs/2508.18285), *An average Brun–Titchmarsh theorem and shifted primes with a large prime factor* (2025), for the current record.

Baker and Harman show that a positive proportion of primes $`p`$ have a prime factor of $`p-1`$ exceeding $`p^{0.677}`$; the 2025 preprint reaches $`0.679`$ for infinitely many primes. Hypothesis B of the present note implies the exponent $`0.9`$ for at least a constant times $`x/(\log x)^2`$ primes. These sources are cited only to make the strength of that premise visible; they are not used in the proof.
