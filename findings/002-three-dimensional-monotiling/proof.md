# Undecidability of a single translational tile in dimension three

**Roger Malcolm III · Research and drafting assistance using GPT-6**

[Overview](README.md) · [Verification record](verification.md) · [References](references.md)

**Status: proposed theorem, complete proof draft, pending external review.** The argument below supplies both directions of an effective reduction, including the finite compiler and the simultaneous realization of its two seeds. It has received AI-assisted source inspection and adversarial checks. It has not received independent specialist review or formal verification. Publication of this draft is not a correctness or priority certificate.

The compiler adapts the graph, dependence, activity, seed, common-solution, and stacking constructions in Sections 3–6 of *A translational tile with no fully periodic tiling in dimension three*, manuscript 155 in the OpenAI mathematics collection. The adaptation retains a cyclic finite factor while incorporating the decorated two-prime rule of Greenfeld and Tao. The computation encoding and the final quotient-to-lattice lift are explicitly identified published inputs. We prove the intervening construction here rather than assume manuscript 155's main theorem. [S1](references.md#s1), [S2](references.md#s2), [S3](references.md#s3)

## Contents

- [The proposed theorem](#main-theorem)
- [The published domino-to-Sudoku interface](#domino-interface)
- [The finite cyclic compiler](#cyclic-compiler)
- [Activation and the reverse implication](#activation)
- [Simultaneous forward realization](#forward-realization)
- [Stacking and the uniform lattice lift](#stacking-and-lift)
- [Completion, logical complexity, and finite tests](#completion)
- [A repulsive lattice-gas consequence](#lattice-gas)
- [Scope, attribution, and review status](#scope)

<a id="main-theorem"></a>

## 1. The proposed theorem

For subsets of an abelian group, write $A\oplus F=G$ when every element of $G$ has exactly one expression $a+f$ with $a\in A$ and $f\in F$. A tile is a finite nonempty set; its translation set may be infinite. All lattice translations in this note are integer translations. Tiles need not be connected, rotations and reflections are not allowed, and the target is the entire ambient group.

A finite domino system is a triple $\mathcal R=(\mathcal W_0,R_1,R_2)$, where $\mathcal W_0$ is a nonempty finite alphabet and $R_1,R_2\subseteq\mathcal W_0^2$ are the allowed horizontal and vertical neighbors. Its precise convention appears in Section 2.

**Theorem 1 — proposed effective reduction.** There is a total computable map assigning to every finite domino system $\mathcal R$ a finite nonempty set $T_{\mathcal R}\subseteq\mathbb Z^3$ such that

```math
\mathcal R\text{ has a configuration on }\mathbb Z^2
\quad\Longleftrightarrow\quad
\exists A\subseteq\mathbb Z^3:\ A\oplus T_{\mathcal R}=\mathbb Z^3.
```

Consequently, for each fixed $d\ge3$, the language of explicitly encoded finite shapes that tile $\mathbb Z^d$ by translations is $\Pi^0_1$-complete under computable many-one reductions. In dimensions one and two the corresponding language is decidable.

The reduction has four stages:

```math
\begin{aligned}
\text{domino rules}
&\longrightarrow \text{a finite decorated Sudoku rule},\\
&\longrightarrow \text{finite tiles with one common complement in }\mathbb Z^2\times V,\\
&\longrightarrow \text{one tile in }\mathbb Z^2\times\mathbb Z/Q\mathbb Z,\\
&\longrightarrow \text{one tile in }\mathbb Z^3.
\end{aligned}
```

The finite group $V$ will be cyclic, and its order will be computable from the input. Preserving this cyclicity is essential to the dimension-three conclusion. Aperiodicity by itself would not establish the theorem.

The proposed improvement concerns dimension three. A September 2026 draft by Li and Liu already claims undecidability in some fixed, very large dimension. Kim's August 2026 revision concerns two connected tiles in dimension three. These results and the earlier fixed-dimension question in Greenfeld's survey are discussed in the [scope section](#scope). No claim of certified priority is made. [S5](references.md#s5), [S6](references.md#s6), [S7](references.md#s7)

<a id="domino-interface"></a>

## 2. The published domino-to-Sudoku interface

### 2.1 Domino conventions and compactness

An $\mathcal R$-configuration on $E\subseteq\mathbb Z^2$ is a map $\mathcal D:E\to\mathcal W_0$ satisfying

```math
(\mathcal D(x),\mathcal D(x+e_j))\in R_j
\quad\text{whenever }x,x+e_j\in E,\qquad j=1,2.
```

This is Greenfeld–Tao's Definition 2.2. A Wang tileset gives such a system by using the tiles as symbols and matching edge colors as the two relations. An empty Wang tileset can first be replaced by the fixed impossible domino system with one symbol and no allowed neighbors, so the nonempty-alphabet convention loses no negative instances. [S2](references.md#s2)

**Lemma 2 — quadrant and plane.** A configuration exists on $\mathbb N_0^2$ if and only if one exists on $\mathbb Z^2$.

**Proof.** Restriction gives one direction. A quadrant configuration supplies a legal pattern on every square $\{0,\ldots,2r\}^2$. Translating gives a legal pattern on $[-r,r]^2$. In the compact product space $\mathcal W_0^{\mathbb Z^2}$, let $K_r$ consist of assignments satisfying all neighbor constraints with both endpoints in this square. These are nonempty nested closed sets. An element of their intersection is a plane configuration. This is also Greenfeld–Tao's Lemma 2.5. $\square$

### 2.2 The finite decorated rule

Fix, independently of the domino input, two distinct primes $p_1,p_2>200$. Set

```math
q=p_1p_2,\qquad N=q^2,\qquad I=\{0,\ldots,N-1\},
\qquad
\Sigma=\mathbb F_{p_1}^{\times}\times\mathbb F_{p_2}^{\times}\times\mathcal W_0.
```

These primes meet the hypothesis $p_\ell>48$ in Greenfeld–Tao's equation (4.3). For a prime $p$, put $\nu_p(0)=+\infty$, and define

```math
f_p(z)=z/p^{\nu_p(z)}\pmod p\quad(z\ne0),
\qquad f_p(0)=1.
```

We now state the finite rule of their Definition 5.1. A word $g=(g_1,g_2,\omega):I\to\Sigma$ belongs to $\mathcal L=\mathcal S^{\mathcal R}$ if there are integers $a,b$, not both zero modulo either prime, and a legal domino pattern

```math
\mathcal D_0:\{0,\ldots,t_1\}\times\{0,\ldots,t_2\}\to\mathcal W_0,
\qquad
t_\ell=
\begin{cases}
1,&p_\ell\nmid a,\\
0,&p_\ell\mid a,
\end{cases}
```

such that the following implications hold for every $n\in I$:

```math
\begin{aligned}
\nu_{p_\ell}(an+b)\le t_\ell
&\ \Longrightarrow\ g_\ell(n)=f_{p_\ell}(an+b)
\qquad(\ell=1,2),\\
\bigl(\nu_{p_1}(an+b)\le t_1\ \text{and}\ \nu_{p_2}(an+b)\le t_2\bigr)
&\ \Longrightarrow\
\omega(n)=\mathcal D_0\bigl(\nu_{p_1}(an+b),\nu_{p_2}(an+b)\bigr).
\end{aligned}
```

Coordinates not restricted by these implications are free. The cited version declares the domain $I=\{0,\ldots,N-1\}$ but prints $1,\ldots,N$ in one subsequent sentence of Definition 5.1. We follow its declared domain and subsequent proof. Consistently switching to one-based indexing is equivalent after shifting the affine intercept. [S2](references.md#s2)

**Lemma 3 — effective enumeration of the rule.** The full finite list $\mathcal L\subseteq\Sigma^I$ is computable from $\mathcal R$.

**Proof.** Enumerate $a,b$ modulo $q^2=p_1^2p_2^2$, discarding pairs that vanish simultaneously modulo either prime. These residues determine the two numbers $t_\ell$. For each $n$, they determine whether $an+b$ has valuation zero, one, or at least two at each prime. In the first two cases they also determine its last nonzero digit. Since the tests only use valuations at most $t_\ell\le1$, no further information about the integers is needed.

For each retained pair, enumerate assignments on the indicated rectangle, which has at most four cells, and check the finitely many domino constraints. Then enumerate all words in $\Sigma^I$ and retain those satisfying the displayed implications for at least one such pair and assignment. Remove duplicates. Every integer witness has a residue representative with the same tests, and every residue pair has integer lifts with exactly those tests. The output is therefore precisely $\mathcal L$. All searches are finite. $\square$

### 2.3 The cited equivalence and the canonical solution

A line-rule array is a map $Y:I\times\mathbb Z\to\Sigma$ with

```math
\bigl(Y(n,dn+e)\bigr)_{n\in I}\in\mathcal L
\qquad(d,e\in\mathbb Z).
```

A column has fixed first argument $n$. “Both structural components have nonconstant columns” means that each function $m\mapsto\operatorname{pr}_\ell Y(n,m)$ is nonconstant, for every $n\in I$ and both $\ell=1,2$.

**Published input GT — Greenfeld–Tao, Proposition 5.2.** For the parameters above, $\mathcal R$ has a quadrant configuration if and only if a line-rule array exists whose two structural components have nonconstant columns. Moreover, given a quadrant configuration $\mathcal D$, the forward proof supplies the array

```math
W(n,m)=
\bigl(f_{p_1}(m),f_{p_2}(m),
\mathcal D(\nu_{p_1}(m),\nu_{p_2}(m))\bigr)
\quad(m\ne0),
\qquad
W(n,0)=(1,1,w_*)
```

for any $w_*\in\mathcal W_0$. [S2](references.md#s2)

This is a cited theorem, not a lemma proved in the present note. Together with Lemma 2 it gives the plane equivalence needed here. There is no prescribed initial configuration or marked computational origin among its inputs. The canonical array has structural components exactly $f_{p_1}(m)$ and $f_{p_2}(m)$; this stronger property will be used for the forward realization.

<a id="cyclic-compiler"></a>

## 3. The finite cyclic compiler

For this section, $\mathcal L\subseteq\Sigma^I$ can be any explicitly supplied finite rule. We construct finitely many finite tiles in one group $G$, asking for the **same** translation set to tile $G$ with each tile. The reverse construction works for this general data. The forward construction will use the canonical array from Section 2.

The graph and activity mechanisms in this section are adapted from manuscript 155. The decorated alphabet and simultaneous two-prime seed conditions are the modification to be checked. All proofs needed for this compiler are included. [S1](references.md#s1)

### 3.1 Parameters, cyclicity, and the graph tile

Introduce ordinary channels and two seed channels:

```math
\mathcal C=I\sqcup\{\eta_1,\eta_2\},\qquad
J_n=\Sigma\ (n\in I),\qquad J_{\eta_t}=\{*\}.
```

For $x=(x_1,x_2)\in\mathbb Z^2$, write

```math
L_n(x)=x_2+nx_1,\qquad u_n=(1,-n),\qquad
S=(\mathbb Z/q^2\mathbb Z)^2,\qquad s(x)=x\bmod q^2,
\qquad D=q^4=|S|.
```

Choose mutually distinct auxiliary primes $a_i,b_i$, all avoiding $p_1,p_2$, with

```math
a_{\eta_1}=2,\qquad a_{\eta_2}=3,\qquad
b_{\eta_1},b_{\eta_2}>D.
```

For every $i\in\mathcal C$ and $j\in J_i$, choose another prime $r_{ij}$, distinct from $p_1,p_2$ and all other auxiliary primes, and nonnegative integers $A_{ij},B_{ij}$ such that

```math
r_{ij}=A_{ij}a_i+B_{ij}b_i.
```

These choices are effective. For coprime positive integers $a,b$ and an integer $r\ge(a-1)b$, choose $B\in\{0,\ldots,a-1\}$ with $Bb\equiv r\pmod a$. Then $A=(r-Bb)/a\ge0$. Thus searching sufficiently large unused primes, and applying this formula, terminates at every step.

Set

```math
\begin{aligned}
r_i&=\prod_{j\in J_i}r_{ij},&
K_i&=\mathbb Z/r_i\mathbb Z
\cong\prod_{j\in J_i}\mathbb Z/r_{ij}\mathbb Z,\\
P_i&=\mathbb Z/a_i\mathbb Z\times\mathbb Z/b_i\mathbb Z,&
K&=\prod_{i\in\mathcal C}K_i,\qquad P=\prod_{i\in\mathcal C}P_i.
\end{aligned}
```

The isomorphism for $K_i$ is the Chinese remainder residue map. Let $U_{ij}\le K_i$ be its subgroup supported in coordinate $j$. Define

```math
G=\mathbb Z^2\times V,\qquad
V=\mathbb Z/D\mathbb Z\times
\prod_{i\in\mathcal C}\bigl(\mathbb Z/r_i^2\mathbb Z\times P_i\bigr).
```

The orders $D$, all $r_i^2$, and all $a_i,b_i$ are pairwise coprime. Therefore $V$ is cyclic with an explicit Chinese remainder identification. Although $S$ is noncyclic, it only indexes residues of the two free coordinates; it is not a factor of $V$.

Write a point of $G$ as $(x,z,(v_i,c_i)_i)$, and put $k_i=v_i\bmod r_i$. The map retaining $(x,k)$ has finite kernel

```math
H_0=\{0\}\times\mathbb Z/D\mathbb Z\times
\prod_{i\in\mathcal C}
\bigl(r_i(\mathbb Z/r_i^2\mathbb Z)\times P_i\bigr).
```

Use $H_0$ as the first tile. The equation $A\oplus H_0=G$ says exactly that $A$ contains one point above each base $(x,k)\in\mathbb Z^2\times K$: each chosen point covers its entire fibre once by translation through $H_0$. Hence a common complement must be a graph with outputs $z(x,k)$, $c_i(x,k)$, and $v_i(x,k)$.

We use a sheared coordinate for its high digits. There is a unique $\beta_i(x,k)\in K_i$ such that

```math
v_i(x,k)=x_1+[k_i-x_1]_{r_i}+r_i\beta_i(x,k)
\quad\text{in }\mathbb Z/r_i^2\mathbb Z,
```

where brackets mean the least nonnegative residue. The first two terms have residue $k_i$, and multiplication by $r_i$ identifies $K_i$ with the zero-low-coordinate subgroup. This parametrizes each fibre exactly; it does not split the cyclic group of order $r_i^2$ into a product of two groups.

### 3.2 Dependence equations

**Lemma 4 — dependence test.** For a channel $i$ and a base shift $\sigma\in\mathbb Z^2\times K$, one can effectively construct a finite nonempty tile $F_{i,\sigma}$ such that a graph tiles with it exactly when $c_i(b)=c_i(b-\sigma)$ at every base $b$. It imposes no additional condition on the other output coordinates.

**Proof.** Lift $\sigma$ to $g\in G$ with $c_i(g)=0$. Set

```math
E_0=\{h\in H_0:c_i(h)=0\},\qquad
E_1=H_0\setminus E_0,\qquad
F_{i,\sigma}=E_1\cup(g+E_0).
```

The two parts are disjoint because their $c_i$ coordinates are respectively nonzero and zero. Above a target base $b$, the source graph point above $b$ together with offsets in $E_1$ covers every output except the slice $c_i=c_i(b)$, once. The source above $b-\sigma$ together with $g+E_0$ covers the slice $c_i=c_i(b-\sigma)$, once. In both cases all other fibre coordinates are free. Exact coverage is equivalent to equality of the two slices. $\square$

For each $i$, apply the lemma to one generator of every $K_j$ with $j\ne i$, without horizontal displacement. For ordinary channel $n$, also use the horizontal shift $u_n$. For each seed use the horizontal shifts $(q^2,0)$ and $(0,q^2)$. Because $\ker L_n=\mathbb Z u_n$, the resulting equations are equivalent to

```math
\begin{aligned}
c_n(x,k)&=\widetilde c_n(L_n(x),k_n)&& (n\in I),\\
c_{\eta_t}(x,k)&=\widetilde c_{\eta_t}(s(x),k_{\eta_t})&& (t=1,2).
\end{aligned}
```

At fixed $x$, denote these functions by $g_{i,x}:K_i\to P_i$. Define their active labels by

```math
\mathcal A_i(x)=
\{j\in J_i:\ \exists w,w'\in K_i,
\ w-w'\in U_{ij},\ g_{i,x}(w)\ne g_{i,x}(w')\}.
```

For ordinary channels the active set depends only on $L_n(x)$, and for seeds only on $s(x)$. It is empty precisely when $g_{i,x}$ is constant: any two points of $K_i$ can be joined by changing one Chinese remainder digit at a time.

### 3.3 Excluding a simultaneous collection of active labels

**Lemma 5 — cycle test.** Given a nonempty cyclically ordered list $C$ of distinct channels and a chosen label $j(i)\in J_i$ in each, one can construct a finite family of finite nonempty tiles whose common satisfaction by a graph with the stated dependences is equivalent to the following condition: at every $x$, at least one selected label is inactive.

**Proof.** For every tuple of maps

```math
d_i:P_{\operatorname{prev}(i)}\to U_{i,j(i)}\qquad(i\in C),
```

write $d_i[e]=d_i(e_{\operatorname{prev}(i)})$ on the cycle, and $d_i[e]=0$ outside it. Include the tile

```math
F_d=\left\{(0,\zeta,(\upsilon_i,e_i)_i):
\begin{array}{l}
e\in P,\quad \zeta\in\mathbb Z/D\mathbb Z,\\
\upsilon_i\in\mathbb Z/r_i^2\mathbb Z,\quad
\upsilon_i\bmod r_i=d_i[e]\ \text{for every }i
\end{array}\right\}.
```

There are finitely many such maps. At a fixed target base $(x,k)$, selecting $e$ forces the source low coordinates to be $k_i-d_i[e]$. The useful output is consequently

```math
\Phi_{x,k,d}(e)=
\bigl(e_i+g_{i,x}(k_i-d_i[e])\bigr)_{i\in\mathcal C}.
```

Once this output agrees with a target, its other coordinates uniquely determine $\zeta$ and the high lifts $\upsilon_i$. Thus $F_d$ tiles with the graph exactly when every map $\Phi_{x,k,d}:P\to P$ is bijective.

If $j(i_0)$ is inactive, the $i_0$ equation is simply $e_{i_0}+g_{i_0,x}(k_{i_0})$, independent of its predecessor. Solve it for $e_{i_0}$, then solve successive equations around the cycle. The first stays satisfied because it has no predecessor dependence. Equations outside the cycle are translations. This constructs a unique inverse for every $d$.

Conversely, suppose every selected label is active at one $x$. Choose $w_i,w'_i$ with difference in $U_{i,j(i)}$ and

```math
\varepsilon_i=g_{i,x}(w_i)-g_{i,x}(w'_i)\ne0
\qquad(i\in C).
```

Take $k_i=w_i$ on the cycle and extend $\varepsilon$ by zero outside it. Prescribe

```math
d_i(0)=0,\qquad
d_i(\varepsilon_{\operatorname{prev}(i)})=w_i-w'_i.
```

The prescribed arguments are distinct, so these extend to maps on the whole finite domains. The two distinct inputs $0$ and $\varepsilon$ then have the same image under $\Phi$: on the cycle this is the identity $\varepsilon_i+g_{i,x}(w'_i)=g_{i,x}(w_i)$, and outside it nothing changes. One tile equation therefore fails. The reasoning also covers a cycle with one channel. $\square$

Apply this test to the ordinary cycle $(0,1,\ldots,N-1)$ for each forbidden word in $\Sigma^I\setminus\mathcal L$. Put

```math
\Sigma_t=\{t\}\times\{t\}\times\mathcal W_0\qquad(t=1,2).
```

For each $t,n$, and each $j\in\Sigma\setminus\Sigma_t$, also test the two-channel cycle $(\eta_t,n)$ with labels $*$ and $j$. These finitely many equations express exactly

```math
\prod_{n\in I}\mathcal A_n(x)\subseteq\mathcal L,
\qquad
*\in\mathcal A_{\eta_t}(x)
\ \Longrightarrow\ \mathcal A_n(x)\subseteq\Sigma_t\quad(n\in I).
```

The first exclusion uses full decorated words. The second constrains the two prime components while leaving the domino decoration free. We next force the active sets needed to make these conditions meaningful.

<a id="activation"></a>

## 4. Activation and the reverse implication

### 4.1 A list with uniform marginals

For $e\in P_i$, let $\delta_e$ denote the singleton indicator. Define

```math
\omega_i=\delta_{(0,0)}-\delta_{(1,0)}-\delta_{(0,1)}+\delta_{(1,1)},
\qquad \mu_i=1+\omega_i.
```

This is a nonconstant nonnegative integer function of total mass $a_i b_i$. Its two marginals are constant:

```math
\sum_{\alpha\in\mathbb Z/a_i\mathbb Z}\mu_i(\alpha,\xi)=a_i,
\qquad
\sum_{\xi\in\mathbb Z/b_i\mathbb Z}\mu_i(\alpha,\xi)=b_i.
```

Choose an index set $\Delta_i$ of size $a_i b_i$ and a list $e_\delta=(e_\delta^a,e_\delta^b)$ in which $e$ appears $\mu_i(e)$ times. Repeated values have different indices. In each fibre $e_\delta^b=\xi$, choose a bijection from its $a_i$ indices to $\mathbb Z/a_i\mathbb Z$, and subtract $e_\delta^a$ from the assigned value to define $\rho_i^a(\delta)$. Independently do the same in each fibre $e_\delta^a=\alpha$, defining $\rho_i^b(\delta)$. Thus both maps

```math
\begin{aligned}
\{\delta:e_\delta^b=\xi\}&\longrightarrow\mathbb Z/a_i\mathbb Z,
&\delta&\longmapsto e_\delta^a+\rho_i^a(\delta),\\
\{\delta:e_\delta^a=\alpha\}&\longrightarrow\mathbb Z/b_i\mathbb Z,
&\delta&\longmapsto e_\delta^b+\rho_i^b(\delta)
\end{aligned}
```

are bijections. All these choices can be made by finite ordered enumeration.

### 4.2 The activation tiles

Let $R_j=r_j(\mathbb Z/r_j^2\mathbb Z)$ be the zero-low-coordinate subgroup. For $h\in\mathbb Z^2$, $e\in P_i$, and $E\subseteq\mathbb Z/D\mathbb Z$, define a finite batch

```math
\mathcal B_i(h,e;E)=
\left\{(h,\zeta,(w_j,d_j)_j):
\begin{array}{l}
\zeta\in E,\quad w_i=h_1\pmod{r_i^2},\quad d_i=e,\\
w_j\in R_j,\quad d_j\in P_j\quad(j\ne i)
\end{array}\right\}.
```

Every choice of its free coordinates occurs once. For an ordinary channel $i$, and each $(l,\delta)\in K_i\times\Delta_i$, choose $h=h^{(i)}_{l,\delta}\in\mathbb Z u_i$ with

```math
h_1\equiv l\pmod{r_i},\qquad
h_1\equiv\rho_i^a(\delta)\pmod{a_i},\qquad
h_1\equiv\rho_i^b(\delta)\pmod{b_i}.
```

The moduli are coprime, so infinitely many choices exist. Choose distinct horizontal vectors for different index pairs. Define

```math
F_i^{\mathrm{act}}=
\bigcup_{(l,\delta)\in K_i\times\Delta_i}
\mathcal B_i(h^{(i)}_{l,\delta},e_\delta;\mathbb Z/D\mathbb Z).
```

For a seed $i$, let $i'$ be the other seed. For each $(l,\delta,\tau)\in K_i\times\Delta_i\times S$, choose $h=h^{(i)}_{l,\delta,\tau}$ satisfying the same three congruences and additionally

```math
s(h)=\tau,\qquad h_1\equiv0\pmod{a_{i'}}.
```

There is no slope condition on these seed offsets. The first coordinate is prescribed modulo the pairwise coprime numbers $r_i,a_i,b_i,q^2,a_{i'}$, and the second only modulo $q^2$. Choose all vectors within this seed tile distinct, and set

```math
F_i^{\mathrm{act}}=
\bigcup_{(l,\delta,\tau)\in K_i\times\Delta_i\times S}
\mathcal B_i(h^{(i)}_{l,\delta,\tau},e_\delta;\{0\}).
```

The horizontal offsets make these unions disjoint, even when entries $e_\delta$ repeat. Each is a set, not a multiset. Both types of activation tile have cardinality

```math
D\prod_{j\in\mathcal C}r_j|P_j|=|H_0|.
```

For ordinary tiles the free $z$ offset supplies the factor $D$; for seed tiles the index $\tau$ supplies it. The graph, dependence, and cycle tiles also have this size, although the stacking argument below does not require equal sizes.

<a id="activation-fibres"></a>

### 4.3 Exact fibre criterion

**Lemma 6 — activation fibre maps.** For a graph over $(x,k)$, an ordinary activation equation holds if and only if, at every target base $(x,k)$, the map

```math
(l,\delta)\longmapsto
\bigl(c_i(x',k')+e_\delta,\beta_i(x',k')\bigr)
```

is a bijection from $K_i\times\Delta_i$ onto $P_i\times K_i$. For a seed the corresponding criterion is that

```math
(l,\delta,\tau)\longmapsto
\bigl(c_i(x',k')+e_\delta,\beta_i(x',k'),z(x',k')\bigr)
```

be a bijection onto $P_i\times K_i\times\mathbb Z/D\mathbb Z$. Here $h$ is the offset belonging to the indicated batch, and

```math
x'=x-h,\qquad k'_i=k_i-l,\qquad k'_j=k_j\quad(j\ne i).
```

**Proof.** A batch fixes its horizontal and low offsets, so it forces this source graph point. The congruence $h_1\equiv l\pmod{r_i}$ gives

```math
[k'_i-x'_1]_{r_i}=[k_i-x_1]_{r_i}.
```

Using the sheared coordinate, its target high coordinate is therefore

```math
v_i(x',k')+h_1
=x_1+[k_i-x_1]_{r_i}+r_i\beta_i(x',k')
\quad\text{in }\mathbb Z/r_i^2\mathbb Z.
```

Thus the batch retains the source's $\beta_i$ and adds $e_\delta$ to its useful output. In every other channel, the free offsets cover the complete zero-low subgroup and every useful coordinate, each once. The ordinary batch also covers the full $z$ coordinate once; the seed batch keeps the source's $z$. Hence each batch fills exactly one slice described by the displayed tuple, once. The slices give an exact partition precisely when the tuple map is bijective. $\square$

### 4.4 Activity forced by the equations

**Lemma 7 — ordinary and seed activity.** In a common solution of the graph, dependence, and activation equations, every ordinary channel has a nonempty active set at every $x$. Each seed has a nonempty active set at some $x$.

**Proof.** For an ordinary activation map, each useful output must occur $r_i$ times among the batches. If channel $i$ is inactive at $x$, its useful output is constant, say $c_0$. All its activation shifts lie in $\ker L_i$, so dependence makes every source output equal to $c_0$. The number of occurrences of $c$ is then $r_i\mu_i(c-c_0)$, which is nonuniform. This contradicts Lemma 6.

Suppose a seed $i$ were inactive everywhere. Dependence would give $c_i(x,k)=f(s(x))$ for some $f:S\to P_i$. Let its integer histogram be

```math
Q_i(\alpha,\xi)=|\{s\in S:f(s)=(\alpha,\xi)\}|,
\qquad \sum_{\alpha,\xi}Q_i(\alpha,\xi)=D.
```

For any fixed $\delta$, as $(l,\tau)$ vary, the source pair

```math
(s(x'),k'_i)=(s(x)-\tau,k_i-l)
```

runs through $S\times K_i$ once. This remains true although the integer offset depends on all the indices: its prescribed residues determine this pair exactly. Uniform useful-output counts in Lemma 6 give $Q_i*\mu_i=D$, where convolution is on $P_i$. Since $Q_i*1=D$, we get $Q_i*\omega_i=0$, namely

```math
Q_i(\alpha,\xi)-Q_i(\alpha-1,\xi)
-Q_i(\alpha,\xi-1)+Q_i(\alpha-1,\xi-1)=0.
```

The difference in the first coordinate is independent of the second. Choose $\alpha_0$ minimizing $Q_i(\alpha,0)$. Telescoping the first-coordinate differences yields

```math
Q_i(\alpha,\xi)=u(\alpha)+v(\xi),
\qquad
u(\alpha)=Q_i(\alpha,0)-Q_i(\alpha_0,0),
\qquad v(\xi)=Q_i(\alpha_0,\xi).
```

Both $u$ and $v$ are nonnegative integer functions. Summing gives

```math
D=b_i\sum_\alpha u(\alpha)+a_i\sum_\xi v(\xi).
```

Since $b_i>D$, the first sum is zero. Consequently $a_i$ divides $D$. This is impossible: for a seed $a_i$ is either two or three, whereas $D=p_1^4p_2^4$ is coprime to six. $\square$

### 4.5 Extracting the decorated array

**Proposition 8 — reverse implication.** From the finite rule $\mathcal L$ the compiler effectively constructs a finite list of finite nonempty tiles in $\mathbb Z^2\times V$, with $V$ cyclic. If these tiles have a common complement, there is a line-rule array with both structural components nonconstant in every column.

**Proof.** Fix a total order on $\Sigma$. By Lemma 7, define

```math
Y(n,m)=\min\mathcal A_n((0,m)).
```

Dependence on $L_n$ means $Y(n,L_n(x))$ is active at every $x$. At $x=(d,e)$, their joint word is $(Y(n,dn+e))_{n\in I}$. A forbidden word would have all its chosen labels active, contradicting its cycle test. Thus the line rule holds.

For each $t=1,2$, choose a point $x^{(t)}$ where seed $\eta_t$ is active. Its pair exclusions force

```math
Y(n,L_n(x^{(t)}))\in\Sigma_t
\qquad(n\in I).
```

For a fixed $n$, the two arguments $L_n(x^{(1)})$ and $L_n(x^{(2)})$ cannot coincide, since the same nonempty active set would then be contained in disjoint sets $\Sigma_1$ and $\Sigma_2$. Each prime component therefore takes both values one and two in that column. This holds for every column and for both primes.

The finite construction uses prime searches with the terminating bound given above, arithmetic, Chinese remainder computations, and enumeration of maps between finite sets. Distinct offsets are found by searching the available arithmetic progressions. Its size is unrestricted, but it is effective. $\square$

This proposition alone is not an undecidability reduction. It must be accompanied by a common complement for every satisfiable domino instance. In particular, separate realizations of the two seed equations would not suffice. We now construct one graph realizing both.

<a id="forward-realization"></a>

## 5. Simultaneous forward realization

Assume there is a line-rule array $W:I\times\mathbb Z\to\Sigma$ whose first two coordinates are exactly $f_{p_1}(m)$ and $f_{p_2}(m)$. The canonical array supplied by the published input GT has this property whenever the domino system has a configuration.

We retain all finite choices made by the compiler, including its offsets. None of these choices will depend on the infinite array. Only the eventual translation set will depend on $W$.

### 5.1 Labelled blocks

For a fixed digit $j\in J_i$, partition its representatives $\{0,\ldots,r_{ij}-1\}$ into $A_{ij}$ consecutive intervals of length $a_i$, followed by $B_{ij}$ consecutive intervals of length $b_i$. Label an interval of length $d$ increasingly by $\mathbb Z/d\mathbb Z$. For each fixed choice of the other digits, use the same partition. This defines a labelled block partition $\mathcal B_{ij}$ of $K_i$.

If $k_i$ has label $y$ in a block of size $d$, put

```math
C_{ij}(k_i)=
\begin{cases}
(y,0),&d=a_i,\\
(0,y),&d=b_i.
\end{cases}
```

Let $T_{ij}(t)$ preserve every block and add the integer $t$ to its cyclic label. This is a permutation of $K_i$ for every integer $t$. The map $C_{ij}$ depends only on digit $j$, and is nonconstant in that digit: each nonempty block has at least two labels and distinct corresponding outputs.

**Lemma 9 — uniform block inverse.** Fix $i,j,x_1,k_i$. Suppose integers $h_1(l,\delta)$ satisfy the three ordinary activation congruences. Then

```math
(l,\delta)\longmapsto
\left(C_{ij}(k_i-l)+e_\delta,
T_{ij}(x_1-h_1(l,\delta))(k_i-l)\right)
```

is a bijection from $K_i\times\Delta_i$ to $P_i\times K_i$.

**Proof.** Fix a target $((\alpha^*,\xi^*),\beta_i^*)$. The point $\beta_i^*$ specifies a block $B$ and its label $z_B$. Since every $T_{ij}(t)$ preserves blocks, the source $k'_i=k_i-l$ must lie in $B$.

If the block has size $a_i$, the equations

```math
e_\delta^b=\xi^*,\qquad
e_\delta^a+\rho_i^a(\delta)=\alpha^*+x_1-z_B
\quad\text{in }\mathbb Z/a_i\mathbb Z
```

give exactly one index $\delta$ by the first fibre ordering. Give $k'_i$ the label $y=\alpha^*-e_\delta^a$ in the block $B$, and set $l=k_i-k'_i$. Its useful output is the target, and its high label is

```math
y+x_1-h_1(l,\delta)
=\alpha^*+x_1-e_\delta^a-\rho_i^a(\delta)=z_B.
```

Conversely, a preimage must satisfy these equations, so it is unique.

If the block has size $b_i$, use instead

```math
e_\delta^a=\alpha^*,\qquad
e_\delta^b+\rho_i^b(\delta)=\xi^*+x_1-z_B
\quad\text{in }\mathbb Z/b_i\mathbb Z.
```

The second fibre ordering determines $\delta$, and label $y=\xi^*-e_\delta^b$ determines $k'_i$ and $l$. The resulting high label is again $z_B$. The inverse only uses the prescribed congruences, so arbitrary additional dependence of the integer lifts on their indices causes no problem. $\square$

### 5.2 Ordinary channels

For $n\in I$, define $j_n(x)=W(n,L_n(x))$ and set

```math
c_n(x,k)=C_{n,j_n(x)}(k_n),\qquad
\beta_n(x,k)=T_{n,j_n(x)}(x_1)k_n.
```

The useful output has the required dependence, and its active label set is exactly $\{j_n(x)\}$. At an ordinary activation target, all sources are displaced along $\ker L_n$, so they share the same $j_n$. The tuple in Lemma 6 is exactly the map in Lemma 9 and is therefore bijective. The free $z$ offsets in ordinary activation tiles leave the shared output $z$ unrestricted.

### 5.3 A residue partition for the two seeds

Select the following seven points of $S$, with coordinates taken modulo $q^2$:

```math
\begin{aligned}
S_{\eta_1}&=\{(0,1),(q,1),(2q,1)\},\\
S_{\eta_2}&=\{(0,2),(q,2),(2q,2),(3q,2)\},\\
S_0&=S\setminus(S_{\eta_1}\cup S_{\eta_2}).
\end{aligned}
```

They are distinct because $q>3$. Each point of $S_{\eta_t}$ has first coordinate zero and second coordinate $t$ modulo $q$. Also $q$ is coprime to six, so $D=q^4\equiv1\pmod6$ and $|S_0|=D-7$ is divisible by six.

Equip these sets with the following disjoint label spaces:

- The three points of $S_{\eta_1}$ form one copy of $\mathbb Z/3\mathbb Z$, with label $y_{\eta_2}=k$ at $(kq,1)$.
- The four points of $S_{\eta_2}$ form two copies of $\mathbb Z/2\mathbb Z$: the pair $(2cq,2),((2c+1)q,2)$ has labels $y_{\eta_1}=0,1$, for $c=0,1$.
- Enumerate $S_0$ lexicographically, split it into sets of six, and label each set by $(y_{\eta_1},y_{\eta_2})\in\mathbb Z/2\mathbb Z\times\mathbb Z/3\mathbb Z$, in order $3y_{\eta_1}+y_{\eta_2}$.

Thus seed $i$ has a label $y_i(s)$ exactly when $s\notin S_i$. A point is uniquely determined by its label-space identity and the labels present in that space.

For an integer $t$, let $R(t)$ preserve every label space and add $t$ to each label present there, in its own cyclic group. Then $R(t+u)=R(t)R(u)$ and $R(-t)=R(t)^{-1}$. Fix the bijection

```math
\lambda:S\to\mathbb Z/D\mathbb Z,\qquad
\lambda(s_1,s_2)=[s_1]_{q^2}+q^2[s_2]_{q^2}.
```

Define a single shared output by

```math
z(x,k)=\lambda(R(x_1)s(x)).
```

No compatibility with spatial addition is required of the label spaces or $\lambda$. Dependence equations constrain useful outputs only, so they place no condition on this $z$.

Abbreviate $C_{i,*},T_{i,*}$ to $C_i,T_i$ for a seed, and set

```math
(c_i(x,k),\beta_i(x,k))=
\begin{cases}
\bigl(C_i(k_i),T_i(x_1)k_i\bigr),&s(x)\in S_i,\\
\bigl((y_i(s(x)),0),k_i\bigr),&s(x)\notin S_i.
\end{cases}
```

These useful outputs have the seed dependence on $(s(x),k_i)$. The seed's single digit is active exactly on the nonempty set $S_i$.

<a id="seed-inverses"></a>

### 5.4 Inverting both seed tests

Fix one seed $i$ and denote the other by $i'$. Its preselected offsets $h=h^{(i)}_{l,\delta,\tau}$ obey

```math
\begin{aligned}
h_1&\equiv l\pmod{r_i},&
h_1&\equiv\rho_i^a(\delta)\pmod{a_i},&
h_1&\equiv\rho_i^b(\delta)\pmod{b_i},\\
s(h)&=\tau,&
h_1&\equiv0\pmod{a_{i'}}.
\end{aligned}
```

At target base $(x,k)$, write $x'=x-h$, $k'_i=k_i-l$, and $s'=s(x)-\tau$. To verify Lemma 6, fix a target tuple

```math
\bigl((\alpha^*,\xi^*),\beta_i^*,z^*\bigr),
\qquad s''=\lambda^{-1}(z^*).
```

The equation for its last coordinate is

```math
R(x_1-h_1)s'=s''.
```

Since $R$ preserves every label space, $s'$ and $s''$ must belong to the same region and the same copy of its label space. This divides the inverse into two exhaustive cases.

**Active-source case.** Suppose $s''\in S_i$. The only label in that space belongs to the inactive seed $i'$. Because $h_1\equiv0\pmod{a_{i'}}$, the equation for $z$ says

```math
y_{i'}(s'')=y_{i'}(s')+x_1
\quad\text{in }\mathbb Z/a_{i'}\mathbb Z.
```

The label-space identity is already fixed, so this determines $s'$ uniquely: subtract $x_1$ from its sole label. In particular, $\tau=s(x)-s'$ is determined before $l$ and $\delta$.

For that fixed $\tau$, the first two target coordinates require

```math
\left(C_i(k_i-l)+e_\delta,
T_i(x_1-h_1(l,\delta,\tau))(k_i-l)\right)
=\bigl((\alpha^*,\xi^*),\beta_i^*\bigr).
```

Lemma 9 supplies exactly one pair $(l,\delta)$, since these offsets satisfy its congruences. The resulting preselected offset also has the already fixed residue $\tau$ and is zero modulo $a_{i'}$ in its first coordinate. Hence it gives the prescribed $s'$ and $z^*$ as well. This is the unique preimage of the full target tuple.

**Inactive-source case.** Suppose $s''\notin S_i$, and write $z_i=y_i(s'')$. Here the high output is simply $k'_i$, so

```math
k'_i=\beta_i^*,\qquad l=k_i-\beta_i^*.
```

The useful output and the $i$-label of the $z$ equation require

```math
e_\delta^b=\xi^*,\qquad
y_i(s')=\alpha^*-e_\delta^a,\qquad
z_i=y_i(s')+x_1-\rho_i^a(\delta).
```

Equivalently, $\delta$ is the unique index with

```math
e_\delta^b=\xi^*,\qquad
e_\delta^a+\rho_i^a(\delta)=\alpha^*+x_1-z_i
\quad\text{in }\mathbb Z/a_i\mathbb Z.
```

Existence and uniqueness follow from the first fibre ordering. This determines $y_i(s')$. If the other seed is also inactive in this label space, its label is forced to be

```math
y_{i'}(s')=y_{i'}(s'')-x_1
\quad\text{in }\mathbb Z/a_{i'}\mathbb Z.
```

If the other seed is active, there is no such label to choose. In both situations, the identity of the label space and all labels present are now determined. They specify a unique $s'$, hence a unique $\tau=s(x)-s'$.

Together with the recovered $l,\delta$, this is a unique batch. Its actual offset satisfies every congruence used in deriving the inverse. Thus its source has the recovered residue and high digit, and its useful and $z$ outputs are the required ones. Every step was forced, so the inverse is unique.

This addresses the dependence of $h_1$ on all three indices: the inverse uses only its specified residues, and every allowed integer lift has those residues. There is no circular choice of an offset. The proof applies to either choice of seed, with exactly the same function $z$. The two tiles may use different batches for a given target; what matters is that each gives unique coverage using this one graph.

### 5.5 Completing the forward graph

**Proposition 10 — simultaneous forward realization.** If $W$ has the line rule and canonical structural components assumed above, one graph is a common complement for every compiler tile.

**Proof.** Use the ordinary and seed useful outputs and high digits just constructed, together with the shared $z$, and define the actual coordinates by

```math
v_i(x,k)=x_1+[k_i-x_1]_{r_i}+r_i\beta_i(x,k)
\quad\text{in }\mathbb Z/r_i^2\mathbb Z.
```

This gives one graph point above every base, so it satisfies the graph equation. Its useful outputs have precisely the dependences imposed in Section 3. No dependence equation restricts $\beta_i$ or $z$.

Lemma 9 gives all ordinary activation bijections; Section 5.4 gives both seed bijections. Lemma 6 converts these into the corresponding exact tiling equations. In particular, the identity of sheared residues in that lemma accounts for all carries in the cyclic coordinates; no additive splitting has been assumed.

At any $x$, the ordinary active labels are exactly $W(n,L_n(x))$. Their joint word belongs to $\mathcal L$ with slope $x_1$ and intercept $x_2$, so no forbidden ordinary cycle is fully active. If seed $\eta_t$ is active, then $s(x)\in S_{\eta_t}$, and

```math
x_1\equiv0\pmod q,\qquad x_2\equiv t\pmod q,
\qquad L_n(x)\equiv t\pmod{p_\ell}
\quad(n\in I,\ \ell=1,2).
```

Since $t=1$ or $2$, these arguments have valuation zero at both primes. The two structural components of $W(n,L_n(x))$ equal $t$, so the active label lies in $\Sigma_t$. Its decoration remains unrestricted, as the seed exclusions require. Lemma 5 therefore verifies every remaining exclusion equation.

All finite partitions, labels, and offset lists are chosen by terminating finite procedures before the infinite array is used. The common complement is an existence witness, not an asserted computable decoding of an arbitrary domino solution. This proves the proposition. $\square$

<a id="stacking-and-lift"></a>

## 6. Stacking and the uniform lattice lift

### 6.1 A finite partition with all differences

**Lemma 11 — difference-cover partition.** Given an integer $m\ge1$ and finitely many excluded primes, an algorithm finds an odd prime $\ell$ outside that list and a partition

```math
\mathbb Z/\ell\mathbb Z=E_1\sqcup\cdots\sqcup E_m
```

into nonempty sets with $E_\nu-E_\nu=\mathbb Z/\ell\mathbb Z$ for every $\nu$.

**Proof.** If $m=1$, take the whole cyclic group. Otherwise color each point of a prime cyclic group independently with $m$ equiprobable colors. Fix a color $\nu$ and $d\ne0$. The pairs

```math
\{2jd,(2j+1)d\},\qquad 0\le j<\lfloor\ell/2\rfloor,
```

are disjoint. The probability that no pair has both points of color $\nu$ is $(1-m^{-2})^{\lfloor\ell/2\rfloor}$. A monochromatic pair supplies the difference $d$. By a union bound, the probability of any failure is at most

```math
m(\ell-1)(1-m^{-2})^{\lfloor\ell/2\rfloor},
```

which is less than one for all sufficiently large primes. A coloring with no failures has every color nonempty, so it also supplies difference zero. For a deterministic procedure, search eligible primes until this rational inequality holds, then enumerate all their finite colorings and test the difference property. Existence proves termination. $\square$

### 6.2 Combining a common-complement system into one tile

**Lemma 12 — stacking.** Let $F_1,\ldots,F_m$ be finite nonempty subsets of an abelian group $H$, and use a partition from Lemma 11. The single set

```math
F^{\mathrm{st}}=\bigcup_{\nu=1}^m(F_\nu\times E_\nu)
\subseteq H\times\mathbb Z/\ell\mathbb Z
```

tiles its whole ambient group if and only if there is one set $A\subseteq H$ satisfying $A\oplus F_\nu=H$ for every $\nu$.

**Proof.** A common complement gives $A\times\{0\}$ as a complement for the stacked tile: the last coordinate chooses the color, and that color's equation supplies the horizontal representation.

Conversely, let $B$ be a complement for the stacked tile. At a horizontal target $g$, a contribution of color $\nu$ is a pair $((a,t),f)$ with $(a,t)\in B$, $f\in F_\nu$, and $a+f=g$. It covers the vertical translate $t+E_\nu$. There are finitely many possible contributions at $g$. Two distinct contributions of the same color cannot occur, because any two translates of $E_\nu$ intersect when $E_\nu-E_\nu$ is the entire cyclic group. Such an intersection would produce two representations of one target.

Write $n_\nu(g)\in\{0,1\}$ for their number. Counting the exact coverage of the vertical fibre yields

```math
\ell=\sum_{\nu=1}^m n_\nu(g)|E_\nu|
=\sum_{\nu=1}^m|E_\nu|.
```

As all $E_\nu$ are nonempty, each $n_\nu(g)$ must be one. Moreover, the projection $B\to H$ is injective: two points with the same horizontal coordinate, together with any $f\in F_1$, would give two color-one contributions at their common target. Therefore the projection $A$ of $B$ satisfies $A\oplus F_\nu=H$ for every $\nu$. $\square$

Apply this to the entire compiler list in $H=G$, including the graph tile. Choose $\ell$ not dividing $|V|$. Then $V\times\mathbb Z/\ell\mathbb Z$ is cyclic, with computable order $Q=\ell|V|$ and computable coordinate conversion. We have produced one finite tile in $\mathbb Z^2\times\mathbb Z/Q\mathbb Z$, equivalent to the common-complement system. Neither periodicity nor a density assumption enters this equivalence.

### 6.3 The published quotient-to-lattice theorem

For a finite tile $F\subseteq H$, define normalized complements by

```math
\operatorname{Tile}_0(F;H)=
\{A\subseteq H:0\in A,\ A\oplus F=H\}.
```

**Published input MSS — Meyerovitch–Sanadhya–Solomon, Theorem 1.1 with one tile.** Let $d\ge2$ and let $\pi:\mathbb Z^d\twoheadrightarrow H$ be a surjective homomorphism. Fix a transversal $\mathscr D$ for its kernel containing zero. There are an integer $M\ge1$ and finite auxiliary sets $T_1,T_2\subseteq\mathbb Z^d$ such that, for every finite $F\subseteq H$ containing zero, the single finite set

```math
\widehat F=
\left(M\bigl(\pi^{-1}(F\setminus\{0\})\cap\mathscr D\bigr)\oplus T_1\right)
\mathbin{\dot\cup}T_2
```

satisfies

```math
\operatorname{Tile}_0(\widehat F;\mathbb Z^d)
=\{M\pi^{-1}(A):A\in\operatorname{Tile}_0(F;H)\}.
```

Here multiplication by $M$ means coordinate dilation. The two auxiliary sets are parts of one output tile, not two prototiles. A nonempty complement can be translated to contain zero, so the identity implies equivalence of unnormalized tiling existence as well. [S3](references.md#s3)

We use this published result, including its rigidity argument. The following instantiation spells out the uniformity in the varying cyclic order, rather than infer uniformity from a statement about each fixed quotient.

**Lemma 13 — uniform lift as the quotient varies.** There is a total algorithm taking $Q\ge1$ and a nonempty finite $F\subseteq\mathbb Z^2\times\mathbb Z/Q\mathbb Z$ to a nonempty finite $\widehat F\subseteq\mathbb Z^3$ with the same tiling-existence answer.

**Proof.** Translate $F$ to contain zero. Use

```math
\pi(x,y,z)=(x,y,z\bmod Q),\qquad
w=(0,0,Q),\qquad \ker\pi=\mathbb Z w,
\qquad \mathscr D=\mathbb Z^2\times\{0,\ldots,Q-1\}.
```

Only the finitely many representatives of $F$ in $\mathscr D$ are needed. In Lemma 2.1 and formulas (3)–(4) of MSS, take free dimension $d=3$, two auxiliary tiles $s=2$, and kernel rank $r=1$. The following fixed parameters meet its finite separation requirements:

```math
B_j=[-j,j]^3\cap\mathbb Z^3,\qquad S_j=B_j\setminus B_{j-1},
\qquad m=50,\quad M=101,\quad
v_i=(22(i-3),0,0)\ (1\le i\le5).
```

Indeed, the five translates $v_i+B_5$ are pairwise disjoint and contained in $B_{50}$. The cited construction gives

```math
\begin{aligned}
T_0&=\left(B_{50}\setminus\bigcup_{i=1}^3(v_i+S_i)\right)
\mathbin{\dot\cup}\bigcup_{i=1}^3(Me_i+v_i+S_i),\\
T_j&=\bigl(T_0\setminus(v_{3+j}+S_{3+j})\bigr)
\mathbin{\dot\cup}(Mw+v_{3+j}+S_{3+j}),\qquad j=1,2.
\end{aligned}
```

These finite coordinate lists are computable from $Q$. The set

```math
R_F=\pi^{-1}(F\setminus\{0\})\cap\mathscr D
```

is found by taking the least nonnegative third-coordinate residues. Output $(M R_F\oplus T_1)\mathbin{\dot\cup}T_2$. The published identity proves its correctness. All operations are finite integer arithmetic, with no decision oracle for the quotient and no periodicity hypothesis. The kernel need not have finite index; here its rank is one. $\square$

<a id="completion"></a>

## 7. Completion, logical complexity, and finite tests

### 7.1 Proof of the effective reduction

**Proof of Theorem 1, reduction assertion.** Given $\mathcal R$, compute $\mathcal L$ by Lemma 3 and the finite compiler tiles by Sections 3–4. Stack them by Lemmas 11–12, identify the finite factor with $\mathbb Z/Q\mathbb Z$, and apply Lemma 13. This finite procedure returns $T_{\mathcal R}\subseteq\mathbb Z^3$ and terminates on every input.

If $\mathcal R$ has a plane configuration, restrict it to the quadrant. The published input GT supplies the canonical array $W$. Proposition 10 supplies one common complement for every compiler tile. Stacking and the MSS lift then give a complement for $T_{\mathcal R}$ in the full lattice.

Conversely, a tiling by $T_{\mathcal R}$ gives a quotient tiling through the MSS identity. Lemma 12 recovers a common complement for the compiler tiles. Proposition 8 extracts a line-rule array with both prime components nonconstant in every column. The published input GT gives a quadrant domino configuration, and Lemma 2 gives a plane configuration. This proves the claimed equivalence in both directions. $\square$

### 7.2 Membership and hardness in the arithmetical hierarchy

Use a fixed effective binary encoding of finite subsets of $\mathbb Z^d$, for example sorted coordinate lists without repetitions. Invalid encodings and the empty shape are negative instances. Denote the resulting tiling language by $\operatorname{TILE}_d$. For $n\ge0$, let $B_n^{(d)}=[-n,n]^d\cap\mathbb Z^d$, and define the finite predicate

```math
\mathcal P_d(F,n):\quad
\exists\theta:B_n^{(d)}-F\to\{0,1\}\quad
\forall x\in B_n^{(d)},\qquad
\sum_{f\in F}\theta(x-f)=1.
```

This allows tile origins outside the inspected cube. It tests the local exact-cover equations, not the possibility of filling a bounded box with pieces that must stay inside it.

**Lemma 14 — effective compactness.** The predicate $\mathcal P_d$ is decidable, and

```math
F\in\operatorname{TILE}_d
\quad\Longleftrightarrow\quad
\forall n\in\mathbb N_0\ \mathcal P_d(F,n).
```

**Proof.** Its Boolean domain is finite, so exhaustive enumeration decides the predicate. Let $C_n\subseteq\{0,1\}^{\mathbb Z^d}$ consist of global assignments satisfying the displayed equations inside $B_n^{(d)}$. These are nested compact cylinder sets and are nonempty exactly when $\mathcal P_d(F,n)$ holds. If every one is nonempty, compactness gives an assignment in their intersection, whose support is a tiling complement. Restriction proves the converse. $\square$

It follows that $\operatorname{TILE}_d$ is $\Pi^0_1$: its complement is computably enumerable by searching for a failed test. The classical machine-to-Wang reduction maps a Turing machine to a tileset admitting a plane tiling exactly when the machine does not halt. Greenfeld–Tao recall this polarity in their Introduction, page 2, and Section 2 gives the domino formulation used here. Thus domino solvability is $\Pi^0_1$-hard, not merely undecidable. Composing it with the proved reduction gives $\Pi^0_1$-hardness of $\operatorname{TILE}_3$, and Lemma 14 gives completeness. [S2](references.md#s2)

For a fixed $d>3$, send a three-dimensional tile $F$ to $F\times\{0\}^{d-3}$. A three-dimensional complement extends independently on every parallel slice. Conversely, any tiling by this embedded shape restricts on each slice to a tiling by $F$. This is an effective equivalence, so completeness holds for every fixed $d\ge3$.

### 7.3 Why the lower dimensions differ

In dimension one, translate a nonempty shape so that $\min F=0$ and put $D_1=\max F$. A singleton tiles. Otherwise the exact-cover equations

```math
\sum_{f\in F}a_{x-f}=1
```

define a binary shift with allowed words of length $D_1+1$. Form a finite directed graph whose vertices are binary words of length $D_1$, and whose edges are allowed overlapping words of length $D_1+1$. A directed cycle repeats to give a bi-infinite legal configuration. Conversely a bi-infinite legal path in a finite graph has a repeated vertex and hence a directed cycle. Cycle existence is decidable.

In dimension two, Bhattacharya's Theorem 1.1 and Corollary 1.2 apply to arbitrary finite shapes, without a connectedness assumption: every tileable shape has a complement periodic under a finite-index subgroup. Enumerate such period lattices and Boolean patterns on their finite quotients, checking the exact-cover equations with multiplicities. This semidecides positive instances. Searching for failure of $\mathcal P_2$ semidecides negative instances. Dovetailing the searches decides the language. This completes the dimension statement in Theorem 1. [S4](references.md#s4)

### 7.4 No computable finite-test radius

**Corollary 15.** There is no total computable function $R:\mathbb N_0\to\mathbb N_0$ such that every nontiling shape in $\mathbb Z^3$ of binary description length at most $L$ fails $\mathcal P_3(F,n)$ for some $n\le R(L)$.

**Proof.** Given an encoded shape of length $\ell(F)$, test $\mathcal P_3(F,R(\ell(F)))$. A tile passes every test. Under the asserted bound, a nontile fails some earlier test and therefore also fails this one, since the feasibility sets are nested. This would decide $\operatorname{TILE}_3$, contradicting Theorem 1. $\square$

Each individual nontile still has a finite least failing radius, by Lemma 14. For any total computable candidate $R$, infinitely many distinct nontiles have least failing radius greater than $R(\ell(F))$. Otherwise, a constant bounding the finitely many exceptional radii, together with the computable monotone envelope of $R$, would give the forbidden uniform bound. Description length here is a specified computable input length, not Kolmogorov complexity.

<a id="lattice-gas"></a>

## 8. A repulsive lattice-gas consequence

This consequence concerns a particular class of interactions determined by a single finite shape. It makes no novelty claim about physical undecidability in general.

Let $F\subseteq\mathbb Z^3$ be finite and nonempty, set $k=|F|$, and take binary occupations $n\in\{0,1\}^{\mathbb Z^3}$. Define the local nonnegative energy

```math
h_x(n)=\left(\sum_{f\in F}n_{x-f}-1\right)^2.
```

Let $\mathcal M$ be the set of translation-invariant Borel probability measures on this compact configuration space. Define the variational ground energy per site by

```math
e_0(F)=\min_{\mu\in\mathcal M}\int h_0\,d\mu.
```

The set $\mathcal M$ is nonempty and compact, and $h_0$ depends continuously on finitely many coordinates, so the minimum exists. This definition avoids a divergent infinite total-energy sum.

**Corollary 16 — exact zero energy and additive approximation.** For these interactions, deciding whether $e_0(F)=0$ is undecidable. The models are translation-invariant finite-range pairwise repulsive lattice gases with one binary species and a uniform chemical potential. Nevertheless $e_0(F)$ is uniformly computable to any positive prescribed additive error.

**Proof of the exact-zero assertion.** If $A\oplus F=\mathbb Z^3$, its indicator has $h_x=0$ for every $x$. Average point masses over its translates in growing cubes. Any weak limit is invariant: for each fixed translation the proportion of points in the symmetric difference of a cube and its translate tends to zero. The limit has integral of $h_0$ equal to zero.

Conversely, if a minimizing invariant measure has integral zero, nonnegativity implies $h_0=0$ almost surely. Invariance gives $h_x=0$ almost surely for every $x$. The intersection of these countably many full-measure events has measure one. A configuration in the intersection is the indicator of an exact tiling complement. Thus

```math
e_0(F)=0\quad\Longleftrightarrow\quad F\text{ tiles }\mathbb Z^3.
```

Theorem 1 supplies undecidability.

To see the interaction form, choose one representative $r$ of each pair $\{r,-r\}$ of nonzero differences in $F-F$, and put $c_r=|F\cap(F+r)|$. Expanding the square, using $n_x^2=n_x$ and translation invariance, gives

```math
\int h_0\,d\mu
=1-k\,\mathbb E_\mu[n_0]
+2\sum_r c_r\,\mathbb E_\mu[n_0n_r].
```

All pair couplings $2c_r$ are nonnegative and have finite support. The chemical potential is $k$, and the constant energy term is fixed at one. $\square$

**Proof of uniform additive computability.** Compute $r_0\ge1$ with $F\subseteq[-r_0,r_0]^3$ and let

```math
H=\max\{1,(k-1)^2\},\qquad 0\le h_x\le H.
```

For an integer $L>2r_0$, enumerate all binary configurations periodic with period $L$ in each coordinate. Compute exactly their minimum mean energy $u_L$, evaluating the local formula on the periodic extension. Uniform averaging over the translates of a periodic configuration gives an invariant measure, so $e_0(F)\le u_L$.

Sample the occupations in an $L$-cube from a minimizing invariant measure and repeat that cube periodically. At the $(L-2r_0)^3$ sites at least $r_0$ from its boundary, the local energy is unchanged. At every other site it is at most $H$. Taking expectations, and then choosing a sample with no greater than the expected periodic energy, proves

```math
0\le u_L-e_0(F)
\le H\left[1-\left(1-\frac{2r_0}{L}\right)^3\right]
\le\frac{6r_0H}{L}.
```

For a requested positive rational error, this formula gives a computable choice of $L$, and the finite enumeration gives the approximating rational $u_L$. It is a uniform algorithm; no efficient runtime is asserted. $\square$

For every nontile the minimum is strictly positive, because equality to zero was proved equivalent to tiling. There is no positive computable lower bound for all these nonzero energies in terms of the input length. Such a bound, combined with an approximation error smaller than a fixed fraction of it, would distinguish zero from positive energy and decide tiling. No robust promised energy gap, finite-temperature transition, or material realization follows from this statement.

<a id="scope"></a>

## 9. Scope, attribution, and review status

The central additional claim of this draft is the effective decorated compiler with a cyclic finite factor, including its forward existence implication. The following dependencies are deliberately distinguished:

| Ingredient | Source and treatment here |
| :--- | :--- |
| Domino and two-prime decorated Sudoku equivalence | Greenfeld–Tao, Definition 5.1 and Proposition 5.2; stated as a published input, with its finite enumeration made explicit. [S2](references.md#s2) |
| Graph, dependence, cycle, activity, seed, common-solution, and stacking mechanisms | Adapted from manuscript 155, Sections 3–6; the needed constructions and proofs are written out in Sections 3–6 above. [S1](references.md#s1) |
| Two-prime decorated adaptation | The seed exclusions retain full decorated symbols, both structural components become nonconstant in every column, and one shared output realizes both seed tests. |
| Quotient-to-lattice lift | Meyerovitch–Sanadhya–Solomon, Theorem 1.1 and Lemma 2.1; used as a published input with an explicit uniform specialization. [S3](references.md#s3) |
| Dimension-two decidability | Bhattacharya, Theorem 1.1 and Corollary 1.2. [S4](references.md#s4) |
| Complexity, finite-radius, and energy conclusions | Deduced in Sections 7–8 from the reduction, compactness, and explicit finite computations. |

The source attribution is substantive: the finite compiler is an adaptation of an existing construction, not a claim that all of its machinery originated in this note. Conversely, the present proof does not assume manuscript 155's assertion about a particular aperiodic three-dimensional tile or its geometric realization. The cited external theorems remain dependencies and are not reproved in full here.

The prior-work boundary is also specific. Greenfeld–Tao's result permits a finite group depending on the input; its lattice formulation does not already supply this whole-space, one-tile, fixed-dimension-three statement. An arbitrary finite group cannot be replaced by a cyclic group by the MSS theorem. Li–Liu's September 2026 draft claims a fixed but much larger dimension; its displayed construction has free rank four before its finite factors and does not specialize directly to dimension three. Kim's August 2026 revision proves a two-connected-tile result in dimension three; preserving the number of prototiles in a connectivity conversion does not turn that into a one-tile result. The present shapes may be disconnected, and no connectivity conversion is used. [S2](references.md#s2), [S3](references.md#s3), [S5](references.md#s5), [S6](references.md#s6)

Greenfeld's earlier 2026 survey, Remark 6.2 and Question 6.3, records the fixed-dimension question. That historical context must be read alongside subsequent drafts. The sources located in the recorded search did not contain the exact theorem proposed here as of October 8, 2026. This is a bounded literature-search conclusion, not proof of priority or absence of an unpublished observation. [S7](references.md#s7)

AI-assisted checks covered the finite cyclic factor, both directions of the compiler, the shared seed output and offset dependences, every-column nonconstancy, stacking over the whole ambient group, and uniformity of the lift as $Q$ varies. They also checked the finite-test formulation and the energy approximation bound. Such checks may share assumptions and failure modes; they are not independent peer review. The complete reduction remains a proposed theorem awaiting fresh specialist review. The [verification record](verification.md) records the actual checks and remaining limitations.

## Revisions

| Version | Date | Change |
| :--- | :--- | :--- |
| `0.1.0` | 2026-10-08 | Initial complete proof draft, with published inputs separated from the decorated cyclic compiler and its consequences. |
