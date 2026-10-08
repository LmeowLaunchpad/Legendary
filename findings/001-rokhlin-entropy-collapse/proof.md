# A conditional collapse of Rokhlin entropy

**Roger Malcolm III · Research using GPT-6**

[Overview](README.md) · [Verification record](verification.md) · [References](references.md)

The implication below combines a specified group-ring counterexample with established theorems of Brandon Seward. Its conclusion is conditional on that counterexample. This note does not independently establish the counterexample or certify its formalization.

## Premise and notation

**Premise (DF).** There exist a finite field $K$ of characteristic two, a finitely presented group $G$, and elements $a,b\in K[G]$ such that

```math
ab=1,\qquad ba\ne 1.
```

This is the part of the main theorem of *A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two* that we use, at repository commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Neither torsion-freeness nor a counterexample over the prime field is assumed. See [S1](references.md#s1).

The group $G$ is countable because it is finitely presented. It is infinite: if $G$ were finite, left multiplication would faithfully represent $K[G]$ on a finite-dimensional vector space, where a one-sided inverse is necessarily a two-sided inverse.

All probability spaces below are standard, and all actions preserve probability measure. For an ergodic action $\Gamma\curvearrowright(X,\mu)$, write

```math
h^{\mathrm{Rok}}_\Gamma(X,\mu)
=\inf_{\alpha\text{ generating}}\mathrm{H}_\mu(\alpha),
```

where the infimum is over countable measurable generating partitions, modulo null sets. We use natural logarithms. Following Seward, let $h^{\mathrm{Rok}}_{\mathrm{sup}}(\Gamma)$ be the supremum of the finite values $h^{\mathrm{Rok}}_\Gamma(X,\mu)$ over all essentially free ergodic probability-preserving actions of $\Gamma$ on standard probability spaces.

The restriction to **finite** entropy in this definition matters; the proof below separately excludes infinite-entropy actions. The theorem numbering used here is that of the author PDF of Seward's Part II. [S2](references.md#s2)

## The conditional theorem

**Theorem.** Assume (DF), choose a corresponding group $G$, and let $T$ be Thompson's circle group. Then the finitely presented group

```math
H=T\times G
```

has the following properties.

1. Every essentially free ergodic probability-preserving $H$-action has Rokhlin entropy zero.
2. Every nontrivial Bernoulli shift over $H$ has Rokhlin entropy zero, including the shift with uniform $[0,1]$ base.
3. For every action in item 1 and every $0<\varepsilon<1$, there is a binary generating partition $\{A,X\setminus A\}$ with $\mu(A)=\varepsilon$.

**Proof.** We first show that

```math
h^{\mathrm{Rok}}_{\mathrm{sup}}(G)<\infty.
```

Suppose instead that this supremum were infinite. Seward's Theorem 1.10 identifies the entropy of every finite-entropy-base Bernoulli shift as

```math
h^{\mathrm{Rok}}_G(L^G,\lambda^G)
=\min\left\{\mathrm{H}(\lambda),h^{\mathrm{Rok}}_{\mathrm{sup}}(G)\right\}.
```

It would therefore equal $\mathrm{H}(\lambda)$. The infinite supremum also supplies a free ergodic action of positive entropy. Theorem 1.12 then gives the same equality for infinite-entropy bases. Thus every Bernoulli shift over $G$ would have Rokhlin entropy equal to its base entropy. Corollary 1.8 says that this property implies direct finiteness of every field group algebra of $G$, contradicting (DF). [S2](references.md#s2)

Thompson's group $T$ is finitely presented. In its piecewise-linear circle model, the rotations

```math
x\longmapsto x+2^{-k}\pmod{1}
```

belong to $T$ and have order $2^k$. Hence $T$ contains finite subgroups of arbitrarily large order. Its finite presentability and circle model are classical; see [S4](references.md#s4).

Seward's Theorem 1.11, also numbered Theorem 6.7 in the body of the paper, now applies to $T\times G$ and yields

```math
h^{\mathrm{Rok}}_{\mathrm{sup}}(H)=0.
```

This directly rules out positive **finite** Rokhlin entropy. To rule out infinite entropy as well, use Corollary 7.7: a countably infinite group admits a free ergodic action of infinite Rokhlin entropy if and only if it admits one of positive finite Rokhlin entropy. Consequently every free ergodic $H$-action has entropy zero. This proves item 1. [S2](references.md#s2)

The group $H$ is finitely presented: combine finite presentations of $T$ and $G$ and add the finitely many commutator relations between generators of the two factors. Every nontrivial Bernoulli shift of a countably infinite group is essentially free and ergodic, so item 2 follows from item 1, irrespective of whether the base entropy is finite.

Finally, a free ergodic action of an infinite group on a probability space is nonatomic. For $0<\varepsilon<1$, the binary probability vector $(\varepsilon,1-\varepsilon)$ has positive Shannon entropy. Since the action has Rokhlin entropy zero, Seward's prescribed-distribution generator theorem supplies a generating partition with exactly these two measures. This is Theorem 1.1 as restated in Part II from Part I. It proves item 3. [S2](references.md#s2), [S3](references.md#s3) $\square$

The product with $T$ is substantive. The argument establishes finite $h^{\mathrm{Rok}}_{\mathrm{sup}}(G)$ for the original group; it does not establish that every free ergodic action of $G$ itself has zero entropy. The group $H$ also has torsion.

## What the binary generator means

Given the partition in item 3, define its symbolic observation by

```math
\Phi(x)(h)=\mathbf{1}_A(h^{-1}x),\qquad h\in H.
```

The generating property means that $\Phi$ is a measurable conjugacy, modulo null sets, between the original action and its image equipped with the pushforward measure. Every original measurable observation can therefore be recovered from the entire $H$-indexed binary configuration, almost surely. Its one-coordinate marginal is $(\varepsilon,1-\varepsilon)$.

This conclusion does not make the output coordinates independent. It does not give an isomorphism between Bernoulli shifts of unequal base entropy, nor does it provide an algorithm or a finite-window encoder.

For the uniform $[0,1]$-base shift, an exact inverse cannot determine the real coordinate at the identity from a finite binary window almost surely, even if the window is allowed to vary. There are only countably many finite subsets of the countable group $H$, and only finitely many binary patterns on each. A deterministic rule whose output is determined by one such pattern can produce only countably many real values. A uniform real random variable is nonatomic. Thus finite-window determination is impossible under this meaning of exact decoding.

A fixed finite-neighborhood encoder is also impossible. If the output bit at $g$ depends only on inputs in $gF$ for a fixed finite set $F$, varying the input at the identity changes only finitely many output bits. After fixing all other real input coordinates, the complete output therefore has only finitely many possible values along that fiber. An almost-surely injective map would, by Fubini's theorem, be injective on a Lebesgue-conull subset of almost every such fiber, which is impossible. This argument does not rule out every unbounded-radius encoding notion.

## A finite-window refinement

Fix a nonempty finite window $F\subseteq H$, $0<\varepsilon<1$, and $\eta>0$. Set $p=(1-\varepsilon,\varepsilon)$ for symbols $(0,1)$. Seward's Theorem 1.9 supplies a generating partition with this distribution and arbitrarily small normalized entropy deficit on $F$; inversion of $F$ accommodates the translate convention. [S2](references.md#s2)

For the corresponding binary process law $\nu$, the one-coordinate marginals are $p$, so

```math
D(\nu_F\Vert p^F)=|F|\mathrm{H}(p)-\mathrm{H}(\nu_F).
```

Choose the normalized deficit below $2\eta^2/|F|$. The displayed relative entropy is then below $2\eta^2$. Pinsker's inequality, using natural logarithms, gives

```math
\|\nu_F-p^F\|_{\mathrm{TV}}
\le\sqrt{\tfrac{1}{2}D(\nu_F\Vert p^F)}<\eta.
```

Thus a globally generating binary representation can look arbitrarily close to independent biased bits on any specified finite window. The representation can depend on both the window and the tolerance. No single representation independent on every finite window is obtained.

## An obstruction to two entropy requirements

**Corollary.** Under (DF), no assignment $\mathcal{E}$ to all essentially free ergodic probability-preserving actions of countably infinite groups can simultaneously satisfy both of the following requirements:

**1. Bernoulli normalization.** For every countably infinite group $\Gamma$ and every finite probability space $(L,\lambda)$ with positive Shannon entropy,

```math
\mathcal{E}(\Gamma\curvearrowright(L^\Gamma,\lambda^\Gamma))=\mathrm{H}(\lambda).
```

**2. Every finite generator bounds entropy.** For every finite generating partition $\alpha$ of an action,

```math
\mathcal{E}(\Gamma\curvearrowright(X,\mu))\le \mathrm{H}_\mu(\alpha).
```

**Proof.** Apply the requirements to the fair binary Bernoulli shift over the group $H$ in the theorem. The first assigns it $\log 2$. The theorem supplies binary generating partitions of probabilities $(\varepsilon,1-\varepsilon)$ for every $0<\varepsilon<1$. The second therefore forces

```math
\log 2\le
-\varepsilon\log\varepsilon-(1-\varepsilon)\log(1-\varepsilon)
\longrightarrow 0
\quad\text{as }\varepsilon\downarrow0,
```

a contradiction. $\square$

The quantifier “every finite generating partition” is essential. This corollary concerns these two specific requirements on the full class of countable-group actions. It is not an impossibility theorem for every conceivable notion of entropy.

## Appendix: a quantitative entropy deficit from the algebraic witness

The qualitative proof above is sufficient for the theorem. The following argument identifies a finite correlation responsible for an entropy deficit in the original group's Bernoulli shift.

Let $q=|K|$, and put

```math
d=1-ba\ne0,\qquad F=\operatorname{supp}(d),\qquad n=|F|.
```

For $r=\sum_u r_u u\in K[G]$, define the continuous linear map

```math
(T_r x)(g)=\sum_u r_u x(gu),\qquad x\in K^G.
```

These maps commute with the left shift and satisfy $T_rT_s=T_{rs}$. Thus $T_aT_b=I$, so $T_b$ maps $K^G$ injectively onto a closed invariant subgroup $Y$, with inverse $T_a|_Y$. Moreover,

```math
db=b-bab=0,
```

so every $y\in Y$ satisfies

```math
\sum_{u\in F}d_u y(u)=0.
```

These cellular-automaton identities are also established in Section 6 of the source preprint. [S1](references.md#s1)

Push forward the uniform product measure on $K^G$ by $T_b$, obtaining $\nu$ on $Y$. This gives a conjugate model of the uniform Bernoulli action. Let $\alpha$ be the partition of $Y$ according to the coordinate $y(e)$. It is generating. Since $b\ne0$, this coordinate is a nonzero $K$-linear form in independent uniform $K$-valued variables, and hence is uniform itself. Therefore

```math
\mathrm{H}_\nu(\alpha)=\log q.
```

The displayed nonzero linear constraint restricts the $F$-coordinate block to at most $q^{n-1}$ possibilities. Taking $E=F^{-1}$ if $\alpha^E=\bigvee_{g\in E}g\alpha$, we obtain

```math
\mathrm{H}_\nu(\alpha^E)\le(n-1)\log q,
\qquad |E|=n.
```

For each $0<\delta<(\log q)/n$, this implies

```math
\frac{1}{|E|}\mathrm{H}_\nu(\alpha^E)
<\mathrm{H}_\nu(\alpha)-\delta.
```

Seward's Theorem 1.3 then gives

```math
h^{\mathrm{Rok}}_G(Y,\nu)
<\log q-\frac{\delta}{16n^3}.
```

Letting $\delta\uparrow(\log q)/n$ and using conjugacy invariance yields

```math
h^{\mathrm{Rok}}_G(K^G,u_K^G)
\le\left(1-\frac{1}{16n^4}\right)\log q
<\log q.
```

Theorem 1.10 consequently identifies this entropy with $h^{\mathrm{Rok}}_{\mathrm{sup}}(G)$, giving the finite upper bound needed in the main proof. [S2](references.md#s2)

This estimate applies to the actual finite field in (DF); it makes no assumption that $K=\mathbb{F}_2$. It also makes no numerical claim about $n$ without a specified witness. All conclusions in this note retain the conditional dependence on (DF).
