# Stationary Coulomb crystallization from Gaussian minimality

**Roger Malcolm III · Research and drafting assistance using GPT-6**

**Version 0.1.0 · 8 October 2026**

[Overview](README.md) · [Verification record](verification.md) · [References](references.md)

**Status: conditional theorem, complete proof draft, pending independent specialist review.** The main theorem assumes the deterministic Gaussian minimality statement formulated below as Hypothesis G. That hypothesis is asserted in OpenAI's family 090 manuscripts; the present work does not independently certify their complete analytic proof. The transfer argument has received AI-assisted derivation and adversarial checks, but not formal verification or independent specialist review. Publication of this draft is not a correctness or priority certificate.

**Abstract.** Assuming that the covolume-one triangular lattice minimizes every Gaussian pair energy among planar configurations of centered density one, we prove a nonnegative heat-defect lower bound for stationary logarithmic Coulomb energy. Equality forces the triangular nearest-neighbor distance as a hard core. A sharp planar Voronoi-cell bound and Palm mass transport then classify all minimizing stationary laws as mixtures of uniformly translated, rotated triangular lattices. A one-sided comparison with the Leblé–Serfaty point-process energy transfers this classification to that functional. Consequences include infinite specific relative entropy of every ground state and triangular structure of every zero-temperature cluster law of free-energy minimizers. The qualitative classification requires no strict Fourier-minorant certificate.

Petrache and Serfaty already established the broad connection from universal optimality to Coulomb and Riesz minimum values. The argument developed here concerns stationary equality and its consequences; it does not claim that earlier connection as a new discovery. [S2](references.md#s2)

## Contents

- [Definitions and the Gaussian hypothesis](#definitions)
- [The main conditional theorem](#main-theorem)
- [Local moments and invariant-component density](#moments-and-density)
- [Stationary Gaussian minimality](#stationary-gaussian-minimality)
- [The stationary Onsager comparison](#onsager-comparison)
- [The spectral lower bound](#spectral-bound)
- [Gaussian smearing and the heat-defect inequality](#heat-defect)
- [Equality and the hard core](#hard-core)
- [Palm and Voronoi rigidity](#packing-rigidity)
- [The standard point-process energy](#standard-energy)
- [Infinite specific relative entropy](#entropy)
- [The zero-temperature limit](#low-temperature)
- [Scope, attribution, and dependencies](#scope)

<a id="definitions"></a>

## 1. Definitions and the Gaussian hypothesis

Set

```math
b=\frac{\sqrt 3}{2},\qquad
A=b^{-1/2}\{m(1,0)+n(1/2,b):m,n\in\mathbb Z\},\qquad
a=b^{-1/2}=\sqrt{\frac{2}{\sqrt 3}}.
```

The lattice $`A`$ has covolume one and shortest nonzero distance $`a`$. Its stationary law $`P_A`$ is obtained by translating it uniformly in a fundamental cell. For an angle $`\theta`$, let $`P_{\theta A}`$ be the corresponding stationary law of the rotated lattice. Angles are taken modulo $`\pi/3`$.

### 1.1 The external Gaussian hypothesis

Write $`B_R`$ for the closed disk of radius $`R`$ centered at the origin.

**Hypothesis G — deterministic Gaussian minimality.** For every $`\alpha>0`$ and every locally finite simple set $`C\subset\mathbb R^2`$ satisfying

```math
N_R=\#(C\cap B_R),\qquad \frac{N_R}{|B_R|}\longrightarrow 1,
```

one has

```math
\liminf_{R\to\infty}\frac{1}{N_R}
\sum_{\substack{x,y\in C\cap B_R\\x\ne y}}
e^{-\pi\alpha|x-y|^2}
\ \ge\ 
\sum_{v\in A\setminus\{0\}}e^{-\pi\alpha|v|^2}.
```

Pairs are ordered. The lower limit on the left may be infinite. Density one ensures that $`N_R>0`$ for all sufficiently large $`R`$.

This is the Gaussian specialization of the principal deterministic energy theorem in *An atomic certificate for triangular-lattice universal optimality*, in family 090 of the OpenAI mathematics collection. The source snapshot is fixed in [S1](references.md#s1). The proof below uses exactly this hypothesis. It does not assume strict inequalities in a Fourier certificate or a deterministic classification of equality cases.

### 1.2 Stationary configurations and compatible fields

A stationary point process is a translation-invariant probability law on locally finite simple configurations in $`\mathbb R^2`$. Throughout, its intensity is one. Write $`P`$ for the law and $`n`$ for the associated counting measure.

A compatible field lift consists of a jointly stationary pair $`(n,E)`$, where $`E\in L^p_{\mathrm{loc}}(\mathbb R^2;\mathbb R^2)`$ for a fixed $`1<p<2`$ and

```math
-\mathrm{div}\,E=2\pi(n-dx)
```

in distributions. No curl-free condition is imposed in this definition.

Let $`g(x)=-\log|x|`$, and let $`\sigma_\delta`$ be uniform probability measure on the circle of radius $`\delta`$. Define

```math
f_\delta=g-g*\sigma_\delta
   =\max\!\left\{\log\frac{\delta}{|x|},0\right\},
\qquad
E_\delta=E-\sum_{p\in n}\nabla f_\delta(\,\cdot-p).
```

Each correction has compact support. For a stationary square-integrable field $`F`$, put

```math
M(F)=\mathbb E\int_Q |F(x)|^2\,dx,
```

where $`Q`$ is any unit-area box. Stationarity makes this the mean squared field per unit area. All expectations of products of stationary fields below have the same local-mean interpretation; they do not require a distinguished pointwise version of an $`L^2`$ field.

A lift is admissible if $`M(E_{\delta_0})<\infty`$ for at least one fixed $`\delta_0>0`$. In the raw field convention, with no factor $`1/2`$, define

```math
\mathcal W(E)=\lim_{\delta\downarrow0}
  \left[M(E_\delta)+2\pi\log\delta\right],
\qquad
\mathcal W_{\mathrm{all}}(P)=\inf\mathcal W(E),
```

where the infimum is over admissible compatible stationary lifts of $`P`$. Section 5 proves existence of the displayed cutoff limit with values in $`\mathbb R\cup\{+\infty\}`$. An empty infimum is $`+\infty`$.

The subscript emphasizes that all compatible fields are allowed. The comparison with the standard point-process functional will use only a one-sided lifting relation. We do not identify different field domains at arbitrary energies.

### 1.3 Pair and spectral measures

Let $`\alpha_P`$ be the reduced ordered factorial pair measure, normalized by

```math
\mathbb E\sum_{x\in n\cap Q}\ 
             \sum_{\substack{y\in n\\y\ne x}} h(y-x)
   =|Q|\int h(z)\,\alpha_P(dz)
```

for nonnegative $`h`$ and bounded measurable $`Q`$. Since the intensity is one, this is also the Palm expected counting measure of the other points.

With Fourier convention

```math
\widehat f(\omega)=\int_{\mathbb R^2}
             f(x)e^{-2\pi i x\cdot\omega}\,dx,
```

the covariance distribution of $`Z=n-dx`$ is $`\delta_0+\alpha_P-dx`$. Section 3 establishes the moment bounds that make it tempered. Its spectral measure $`\rho_P`$ is nonnegative and satisfies

```math
\mathbb E|Z(\psi)|^2
  =\int|\widehat\psi(\omega)|^2\,\rho_P(d\omega)
```

for Schwartz test functions $`\psi`$.

Finally, put

```math
\Psi_t(x)=\frac{1}{4\pi t}e^{-|x|^2/(4t)},\qquad
H_P(t)=\int\Psi_t(z)\,\alpha_P(dz),\qquad
D_P(t)=H_P(t)-H_A(t),
```

where $`\alpha_A=\sum_{v\in A\setminus\{0\}}\delta_v`$ and $`H_A=H_{P_A}`$.

<a id="main-theorem"></a>

## 2. The main conditional theorem

**Theorem 1 — stationary Coulomb crystallization, conditional on G.** Assume Hypothesis G. For every stationary simple intensity-one point process $`P`$ with finite $`\mathcal W_{\mathrm{all}}(P)`$,

```math
\mathcal W_{\mathrm{all}}(P)-\mathcal W_{\mathrm{all}}(P_A)
 \ \ge\ 4\pi^2\int_0^\infty D_P(t)\,dt
 \ \ge\ 0.
```

Equality $`\mathcal W_{\mathrm{all}}(P)=\mathcal W_{\mathrm{all}}(P_A)`$ holds if and only if

```math
P=\int_{[0,\pi/3)}P_{\theta A}\,\nu(d\theta)
```

for a probability measure $`\nu`$ on orientations modulo $`\pi/3`$.

In particular, each translation-ergodic minimizing law has one fixed orientation and a uniform random translation. The fieldwise proof also bounds every finite-energy admissible lift below by the same lattice value, so an infimum of such lifts cannot be $`-\infty`$.

The theorem classifies stationary laws. It does not classify every deterministic configuration having minimum energy per area: finite or sufficiently sparse defects can leave such an energy unchanged.

The proof occupies Sections 3–9. The application to the Leblé–Serfaty functional and the consequences follow in Sections 10–12.

<a id="moments-and-density"></a>

## 3. Local moments and invariant-component density

### 3.1 Local second moments

Suppose $`F`$ is a stationary field with $`M(F)<\infty`$ and

```math
-\mathrm{div}\,F=2\pi(n*\chi-dx),
```

where $`\chi`$ is a compactly supported nonnegative probability measure. A fixed circle smearing is sufficient here.

For a bounded set $`Q`$, choose a nonnegative smooth compactly supported function $`\phi`$ that is at least one on $`Q+\mathrm{supp}\,\chi`$. Positivity and the divergence equation give

```math
n(Q)\le\int\phi\,d(n*\chi)
     =\int\phi\,dx+\frac{1}{2\pi}\int F\cdot\nabla\phi\,dx.
```

The last expression has finite second moment by Cauchy–Schwarz and stationarity. Therefore $`\mathbb E[n(Q)^2]<\infty`$ for every bounded $`Q`$.

For translates $`C+j`$ of a unit cell, stationarity and Cauchy–Schwarz imply

```math
\mathbb E[n(C)n(C+j)]\le\mathbb E[n(C)^2].
```

Covering $`C+B_R(z)`$ by $`O((1+R)^2)`$ such cells and using Campbell's formula yields

```math
\alpha_P(B_R(z))\le C_P(1+R)^2
```

uniformly in $`z`$. In particular, the pair measure has uniformly bounded mass on translated unit-size sets, and every Schwartz function is absolutely integrable against it. All Gaussian pair integrals are finite.

The covariance distribution is consequently tempered and positive definite. The usual spectral representation for positive-definite tempered distributions supplies the nonnegative tempered measure $`\rho_P`$ used above.

### 3.2 Density in each invariant component

Let $`B`$ be an event invariant under joint translations of the field and point measure. The distribution $`\mathbb E[\mathbf 1_BF(x)]`$ is a constant vector. The weighted point measure $`\mathbb E[\mathbf 1_Bn]`$ is stationary, hence equals $`c_B\,dx`$ for some $`c_B`$. Taking expected divergence gives

```math
0=2\pi\bigl(c_B-\mathbb P(B)\bigr)\,dx.
```

Convolution by the probability measure $`\chi`$ preserves the weighted intensity. It follows that

```math
\mathbb E[\mathbf 1_B n(dx)]=\mathbb P(B)\,dx.
```

Thus the conditional intensity on the invariant sigma-field is one.

For completeness, take a smooth nonnegative compactly supported probability density $`\chi`$, supported in $`B_L`$. The spatial ergodic theorem along disks, applied to the integrable stationary function $`n*\chi`$, gives

```math
\frac{1}{|B_R|}\int_{B_R}(n*\chi)(x)\,dx\longrightarrow1
\qquad\text{almost surely}.
```

The integrals over $`B_{R-L}`$ and $`B_{R+L}`$ respectively bound $`n(B_R)`$ from below and above. Dividing by $`\pi R^2`$ proves

```math
\frac{n(B_R)}{|B_R|}\longrightarrow1
\qquad\text{almost surely}.
```

This argument excludes mixtures of distinct macroscopic densities from the finite-energy domain, even when their averaged intensity is one.

<a id="stationary-gaussian-minimality"></a>

## 4. Stationary Gaussian minimality

Fix $`\alpha>0`$ and let

```math
q_R=\sum_{\substack{x,y\in n\cap B_R\\x\ne y}}
                  e^{-\pi\alpha|x-y|^2}.
```

Almost every realization satisfies the density hypothesis in G. Multiplying the conclusion of G by $`n(B_R)/|B_R|\to1`$ gives

```math
\liminf_{R\to\infty}\frac{q_R}{|B_R|}
 \ge\sum_{v\in A\setminus\{0\}}e^{-\pi\alpha|v|^2}
\qquad\text{almost surely}.
```

The summands are nonnegative, so Fatou gives the same lower bound for the lower limit of expectations. On the other hand, Campbell's formula gives

```math
\frac{\mathbb E q_R}{|B_R|}
 =\int e^{-\pi\alpha|z|^2}
       \frac{|B_R\cap(B_R-z)|}{|B_R|}\,\alpha_P(dz).
```

The overlap fraction lies between zero and one and tends to one for each fixed $`z`$. Gaussian integrability, proved in Section 3, permits dominated convergence. Therefore

```math
\int e^{-\pi\alpha|z|^2}\,\alpha_P(dz)
 \ge\sum_{v\in A\setminus\{0\}}e^{-\pi\alpha|v|^2}.
```

Taking $`\alpha=1/(4\pi t)`$ and inserting the heat-kernel normalization shows

```math
D_P(t)\ge0\qquad(t>0).
```

Only Hypothesis G was used. The sharp Fourier minorants asserted in [S1](references.md#s1) provide another route to this inequality but are not an additional premise of the theorem.

<a id="onsager-comparison"></a>

## 5. The stationary Onsager comparison

Let $`\chi`$ be a nonnegative smooth compactly supported radial probability density. Define

```math
k_\chi=g-g*(\chi*\chi),\qquad
m_2(\chi)=\int |x|^2\chi(x)\,dx,\qquad
F_\chi=E-\nabla\bigl[(g-g*\chi)*n\bigr].
```

Newton's radial formula gives

```math
k_\chi\ge0,\qquad
\mathrm{supp}\,k_\chi\text{ is compact},\qquad
\int k_\chi(x)\,dx=\pi m_2(\chi).
```

Although $`g-g*\chi`$ is singular at the origin, the difference between $`F_\chi`$ and a fixed circle-regularized field is a compact per-charge gradient with bounded magnitude. The local second moments proved in Section 3 therefore imply $`M(F_\chi)<\infty`$.

We claim the exact extended identity

```math
\mathcal W(E)-\left[M(F_\chi)-2\pi(g*\chi*\chi)(0)\right]
 =2\pi\alpha_P(k_\chi)-2\pi^2m_2(\chi).
```

### 5.1 Integration by parts at a fixed cutoff

Fix $`\delta>0`$ and put

```math
h_\delta=g*(\sigma_\delta-\chi),\qquad
V=h_\delta*n,\qquad
q_\delta=g*(\sigma_\delta*\sigma_\delta-\chi*\chi).
```

The radial formula makes $`h_\delta`$ bounded, compactly supported, and globally Lipschitz, with bounded gradient. Hence $`V`$ and $`\nabla V`$ have finite stationary second moments. Moreover,

```math
E_\delta=F_\chi+\nabla V,
\qquad
-\Delta V=2\pi n*(\sigma_\delta-\chi).
```

To justify the integration by parts, multiply by a smooth compactly supported spatial test $`\eta`$ with $`\int\eta=1`$. Expectations of $`VF_\chi`$ and $`V\nabla V`$ are finite constant vectors by stationarity, so all terms containing $`\nabla\eta`$ vanish after expectation. The resulting identities are

```math
\begin{aligned}
\mathbb E[F_\chi\cdot\nabla V]
 &=2\pi\mathbb E[V(n*\chi-dx)],\\
M(\nabla V)
 &=2\pi\mathbb E[V(n*\sigma_\delta-n*\chi)].
\end{aligned}
```

The expressions on the right denote the densities of expected stationary random measures. In particular, $`n*\sigma_\delta`$ is not treated as a pointwise density. Its product with $`V`$ is well-defined because $`V`$ is continuous. One can first mollify $`V`$: locally uniform convergence controls the random-measure terms, while local and stationary mean-square convergence of gradients controls the field terms. Local count second moments give domination for these passages.

Expanding $`M(F_\chi+\nabla V)`$, combining the preceding identities, and applying Campbell's formula gives

```math
M(E_\delta)-M(F_\chi)
 =2\pi\left[q_\delta(0)+\alpha_P(q_\delta)
                      -\int q_\delta(x)\,dx\right].
```

The self and background terms are

```math
\begin{aligned}
q_\delta(0)&=-\log\delta-(g*\chi*\chi)(0),\\
\int q_\delta(x)\,dx&=\pi\bigl(m_2(\chi)-\delta^2\bigr).
\end{aligned}
```

Here $`(g*\sigma_\delta*\sigma_\delta)(0)=-\log\delta`$. The background formula follows from the radial identity

```math
\int(g-g*\mu)(x)\,dx=\frac{\pi}{2}\int|x|^2\,\mu(dx)
```

for a compact radial probability measure $`\mu`$, applied to the two convolutions.

### 5.2 Removal of the cutoff

As $`\delta\downarrow0`$, Newton's formula makes $`g*\sigma_\delta*\sigma_\delta`$ increase to $`g`$ away from zero. Thus $`q_\delta`$ increases to $`k_\chi`$ there. Fix $`\delta_0>0`$. The function $`q_{\delta_0}`$ is bounded and compactly supported, so $`\alpha_P(|q_{\delta_0}|)<\infty`$. Apply monotone convergence to the nonnegative increasing difference $`q_\delta-q_{\delta_0}`$.

Adding $`2\pi\log\delta`$ to the fixed-cutoff identity and passing to the limit proves

```math
\mathcal W(E)-\left[M(F_\chi)-2\pi(g*\chi*\chi)(0)\right]
 =2\pi\alpha_P(k_\chi)-2\pi^2m_2(\chi).
```

This proves existence of the cutoff limit with a finite lower bound. It also shows that finite $`\mathcal W(E)`$ forces the relevant close-pair logarithmic integrability. Such integrability was not assumed in advance. The subtraction of $`q_{\delta_0}`$ is essential: $`g*\chi*\chi`$ itself is not compactly supported.

Discarding the nonnegative pair term gives the comparison needed later:

```math
M(F_\chi)-2\pi(g*\chi*\chi)(0)
 \le\mathcal W(E)+2\pi^2m_2(\chi).
```

<a id="spectral-bound"></a>

## 6. The spectral lower bound

For every stationary finite-mean-square field $`F`$ satisfying

```math
-\mathrm{div}\,F=2\pi(n*\chi-dx),
```

with $`\chi`$ a smooth compact radial probability density, we prove

```math
M(F)\ge\int_{\mathbb R^2}
       \frac{|\widehat\chi(\omega)|^2}{|\omega|^2}\,\rho_P(d\omega).
```

### 6.1 The spectral atom at zero

Choose a real smooth compactly supported $`\phi`$ with $`\int\phi=1`$, and set $`\phi_R(x)=R^{-2}\phi(x/R)`$. The divergence equation and stationary Cauchy–Schwarz imply

```math
\begin{aligned}
\mathrm{Var}\bigl[(n*\chi-dx)(\phi_R)\bigr]
 &\le\frac{M(F)}{4\pi^2}\|\nabla\phi_R\|_{L^1}^2\\
 &=O(R^{-2}).
\end{aligned}
```

The spectral expression for the variance is

```math
\int |\widehat\chi(\omega)|^2
       |\widehat\phi_R(\omega)|^2\,\rho_P(d\omega)
 \ge\rho_P(\{0\}),
```

because both Fourier transforms equal one at zero. Hence $`\rho_P(\{0\})=0`$. Optimizing tests supported away from zero alone would not supply this step.

### 6.2 Nonzero frequencies

Let $`U=\psi*(n-dx)`$, where $`\widehat\psi`$ is real, even, smooth, and compactly supported away from zero. The Hilbert-space inequality

```math
M(F)\ge2\mathbb E[F\cdot\nabla U]-M(\nabla U)
```

holds by nonnegativity of $`M(F-\nabla U)`$. Stationary integration by parts and the covariance formula identify its right side as

```math
4\pi\int\widehat\chi\,\widehat\psi\,d\rho_P
 -4\pi^2\int|\omega|^2|\widehat\psi(\omega)|^2\,\rho_P(d\omega).
```

These expectations are well-defined because the test is Schwartz and the spectral measure is tempered. Integration by parts is justified by a compact spatial test of integral one: the expected product $`UF`$ is a finite constant vector, so the spatial boundary term vanishes. Compact approximations to the convolution give the same identity.

Choose smooth even annular cutoffs $`0\le\theta\le1`$ and put

```math
\widehat\psi(\omega)
 =\frac{\theta(\omega)\widehat\chi(\omega)}{2\pi|\omega|^2}.
```

The resulting bound is

```math
M(F)\ge\int
 \bigl(2\theta(\omega)-\theta(\omega)^2\bigr)
 \frac{|\widehat\chi(\omega)|^2}{|\omega|^2}\,\rho_P(d\omega).
```

Exhaust the punctured plane by such cutoffs. The integrands are nonnegative, and Fatou, or monotone exhaustion, gives the stated spectral bound. The zero-atom argument completes the treatment of the origin. No gradient assumption on $`F`$ is required.

<a id="heat-defect"></a>

## 7. Gaussian smearing and the heat-defect inequality

### 7.1 A one-sided Gaussian limit

Fix $`t>0`$ and let $`\gamma=\Psi_{t/2}`$. Approximate it by normalized nonnegative smooth compact radial cutoffs $`\chi_R`$. They can be chosen to converge to $`\gamma`$ in the Schwartz topology. Then

```math
m_2(\chi_R)\longrightarrow2t,
\qquad
\widehat\chi_R\longrightarrow\widehat\gamma
\quad\text{pointwise},
\qquad
(g*\chi_R*\chi_R)(0)\longrightarrow(g*\Psi_t)(0).
```

The self-interaction convergence follows from local integrability of the logarithm, uniform boundedness of the convolved densities near zero, and Gaussian decay at infinity.

Combine the Onsager comparison with the spectral lower bound. Fatou for the nonnegative spectral integrands gives

```math
\begin{aligned}
S_P(t)&=\int\frac{e^{-4\pi^2t|\omega|^2}}{|\omega|^2}
                      \,\rho_P(d\omega),\\
S_P(t)-c_t&\le\mathcal W(E)+4\pi^2t,\\
c_t&=2\pi(g*\Psi_t)(0).
\end{aligned}
```

This is fieldwise, so taking the infimum over lifts yields

```math
S_P(t)-c_t\le \mathcal W_{\mathrm{all}}(P)+4\pi^2t.
```

Attainment of the infimum is unnecessary. The passage uses Fatou, not a spectral dominated-convergence assertion at the singular frequency. In particular, $`S_P(t)<\infty`$ whenever $`P`$ has a finite-energy lift.

### 7.2 The heat identity

The covariance relation gives

```math
H_P(u)+\Psi_u(0)-1
 =\int e^{-4\pi^2u|\omega|^2}\,\rho_P(d\omega)\ge0.
```

For nonzero $`\omega`$,

```math
\frac{e^{-4\pi^2t|\omega|^2}}{|\omega|^2}
 =4\pi^2\int_t^\infty e^{-4\pi^2u|\omega|^2}\,du.
```

Tonelli and the absence of a zero atom therefore give

```math
S_P(t)=4\pi^2\int_t^\infty
             \bigl[H_P(u)+\Psi_u(0)-1\bigr]\,du.
```

The bracket is nonnegative and the integral is finite. Subtract the corresponding finite integral for $`A`$. The diagonal and background terms cancel, and

```math
S_P(t)-S_A(t)=4\pi^2\int_t^\infty D_P(u)\,du.
```

This difference is absolutely integrable on $`[t,\infty)`$, since its absolute value is bounded by the sum of the two nonnegative spectral brackets. No difference of separately divergent logarithmic pair integrals is taken.

### 7.3 The lattice reference value

Let $`E_A`$ be the canonical mean-zero periodic gradient field of the uniformly translated lattice, and set $`W_A=\mathcal W(E_A)`$. Its Gaussian-smoothed energy is exactly

```math
S_A(t)=\sum_{w\in A^*\setminus\{0\}}
                  \frac{e^{-4\pi^2t|w|^2}}{|w|^2},
```

where $`A^*`$ is the dual lattice. Define

```math
\begin{aligned}
k_t(r)&=g(r)-(g*\Psi_t)(r)\\
 &=2\pi\int_0^t\Psi_u(r)\,du
  =\int_r^\infty e^{-s^2/(4t)}\frac{ds}{s}.
\end{aligned}
```

For $`r\ge a`$,

```math
0\le k_t(r)\le\frac{2t}{r^2}e^{-r^2/(4t)}.
```

Thus the sum of $`k_t`$ over nonzero lattice sites tends to zero exponentially as $`t\downarrow0`$.

The compact Onsager identity passes to the Gaussian for this reference lattice and gives the exact formula

```math
W_A=S_A(t)-c_t
       +2\pi\sum_{v\in A\setminus\{0\}}k_t(v)-4\pi^2t.
```

To justify equality in this passage, choose the compact cutoffs with $`\chi_R\le C\Psi_{t/2}`$ for all sufficiently large $`R`$. Radial Newton's formula gives $`0\le k_{\chi_R}(r)\le C^2k_t(r)`$, which is summable over nonzero lattice sites. Periodic Fourier series handles the field term, with Schwartz bounds on the cutoffs. The self and second-moment terms converge as above. This argument establishes equality for the lattice; only an inequality was needed for a general process.

Consequently,

```math
S_A(t)-c_t\longrightarrow W_A\qquad(t\downarrow0).
```

All constants are fixed by the stated circle regularization. Explicitly, with $`\gamma_{\mathrm E}`$ denoting Euler's constant,

```math
c_t=-\pi\log(4t)+\pi\gamma_{\mathrm E},
\qquad
W_A=\lim_{t\downarrow0}
 \left[
 \sum_{w\in A^*\setminus\{0\}}
       \frac{e^{-4\pi^2t|w|^2}}{|w|^2}
       +\pi\log(4t)-\pi\gamma_{\mathrm E}
 \right].
```

### 7.4 Completion of the lower bound

Combining the Gaussian inequality, heat identity, and exact lattice identity gives

```math
\mathcal W_{\mathrm{all}}(P)-W_A
 \ge4\pi^2\int_t^\infty D_P(u)\,du
       -2\pi\sum_{v\in A\setminus\{0\}}k_t(v).
```

Section 4 proved $`D_P(u)\ge0`$. Monotone convergence as $`t\downarrow0`$, together with the vanishing lattice correction, yields

```math
\mathcal W_{\mathrm{all}}(P)-W_A
 \ge4\pi^2\int_0^\infty D_P(u)\,du\ge0.
```

The same argument applies before the infimum to every finite-energy lift. For $`P=P_A`$ it gives $`\mathcal W_{\mathrm{all}}(P_A)\ge W_A`$, while the canonical field gives the reverse inequality. Therefore $`\mathcal W_{\mathrm{all}}(P_A)=W_A`$, proving the lower-bound part of Theorem 1 without assuming this equality in advance.

<a id="hard-core"></a>

## 8. Equality forces the optimal hard core

Suppose $`\mathcal W_{\mathrm{all}}(P)=W_A`$. The nonnegative integral in Theorem 1 vanishes, so $`D_P(t)=0`$ for almost every $`t>0`$. Choose $`t_j\downarrow0`$ from this full-measure equality set.

For a fixed $`r<a`$,

```math
\begin{aligned}
\alpha_P(B_r)e^{-r^2/(4t_j)}
 &\le\int e^{-|z|^2/(4t_j)}\,\alpha_P(dz)\\
 &=\sum_{v\in A\setminus\{0\}}e^{-|v|^2/(4t_j)}.
\end{aligned}
```

Fix $`t_0>0`$. For $`t_j\le t_0`$, the last sum is at most

```math
C(t_0)e^{-a^2/(4t_j)},\qquad
C(t_0)=\sum_{v\in A\setminus\{0\}}
                  e^{-(|v|^2-a^2)/(4t_0)}<\infty.
```

It follows that

```math
\alpha_P(B_r)\le C(t_0)e^{-(a^2-r^2)/(4t_j)}\longrightarrow0.
```

Hence $`\alpha_P(B_r)=0`$ for every $`r<a`$. Apply Campbell's formula to counts of such pairs with the first point in a bounded box. Their expectations vanish, so their counts vanish almost surely. Countably many boxes and rational radii approaching $`a`$ show that almost surely no distinct pair anywhere has separation less than $`a`$.

This deduction uses only nonnegative Gaussian gaps and their equality at times tending to zero. No strict minorant estimate is required.

<a id="packing-rigidity"></a>

## 9. Palm and Voronoi rigidity

The sharp planar local packing theorem states that a Voronoi cell in a packing of disks of radius $`a/2`$ has area at least

```math
\frac{\sqrt 3}{2}a^2=1,
```

with equality only for the regular circumscribed hexagon. The bound does not require periodicity or saturation. An unbounded cell has infinite area. A self-contained proof of this classical bound and its equality case is given in [S4](references.md#s4).

Apply the theorem to the hard-core configurations obtained in Section 8. Let $`\mathbb E^0`$ denote Palm expectation and $`V_0`$ the Voronoi cell of the Palm point at the origin. The stationary nearest-point allocation and mass transport give, at intensity one,

```math
\mathbb E^0|V_0|=\mathbb P(n\ne\varnothing)\le1.
```

Indeed, each point sends Lebesgue mass from its Voronoi cell, while each location receives total mass one whenever the configuration is nonempty. Ties lie on a Lebesgue-null set. The lower bound $`|V_0|\ge1`$ therefore forces equality, nonemptiness almost surely, and a regular hexagonal Palm cell almost surely.

The point intensity of non-hexagonal cells is zero. Campbell's formula on countably many bounded boxes rules out such cells everywhere almost surely. Adjacent regular hexagonal cells share a side; their centers are reflected across that side, and their orientations agree modulo the hexagonal symmetries. Propagation through the connected cell adjacency graph produces one rotated, translated triangular lattice.

Conditional on the orientation, stationarity makes the translation distribution invariant under every translation on the lattice torus. It is therefore the Haar probability. Thus

```math
P=\int_{[0,\pi/3)}P_{\theta A}\,\nu(d\theta).
```

Conversely, every such mixture admits the corresponding mixture of canonical periodic gradient-field lifts, each with energy $`W_A`$. The lower bound from Section 7 supplies the reverse inequality. This proves both directions of Theorem 1. $`\square`$

<a id="standard-energy"></a>

## 10. Transfer to the standard point-process energy

Let $`\mathcal W_{\mathrm{LS}}`$ denote the stationary point-process energy of Leblé and Serfaty, with its normalization as specified in their definitions. Section 2.7.3 of that paper divides raw field energy by $`2\pi`$. Their stationary-lift result, Lemma 3.8 together with the expected truncation identity (3.14), gives the relation needed here:

```math
\mathcal W_{\mathrm{all}}(P)\le2\pi \mathcal W_{\mathrm{LS}}(P),
\qquad
W_A=2\pi \mathcal W_{\mathrm{LS}}(P_A).
```

The first statement is one-sided: a stationary lift supplied by the standard energy theory is among the fields allowed in the larger infimum defining $`\mathcal W_{\mathrm{all}}`$. The second follows from the canonical periodic lattice field and the periodic Green-function formula. These interfaces use the field classes and normalizations of [S3](references.md#s3).

Combining this relation with Theorem 1 gives

```math
0\le \mathcal W_{\mathrm{all}}(P)-W_A
 \le2\pi\bigl(\mathcal W_{\mathrm{LS}}(P)-\mathcal W_{\mathrm{LS}}(P_A)\bigr).
```

Therefore $`\mathcal W_{\mathrm{LS}}(P)\ge \mathcal W_{\mathrm{LS}}(P_A)`$. Equality for $`\mathcal W_{\mathrm{LS}}`$ forces equality for $`\mathcal W_{\mathrm{all}}`$, so its minimizing laws are precisely the same triangular orientation mixtures. The converse follows from their canonical stationary lifts and the lower bound.

No equality between the two functionals at other energies is asserted. In particular, the argument does not rely on uniqueness of arbitrary compatible fields: adding a nonconstant divergence-free field preserves compatibility.

<a id="entropy"></a>

## 11. Infinite specific relative entropy of every ground state

Let $`\Pi^1`$ be the unit-intensity Poisson process. Write $`\mathrm{Ent}(\mu\mid\nu)`$ for relative entropy and

```math
\mathrm{ent}(P\mid\Pi^1)
 =\lim_{R\to\infty}\frac{1}{|Q_R|}
       \mathrm{Ent}(P_{Q_R}\mid\Pi^1_{Q_R})
```

for specific relative entropy along expanding squares. Its existence and lower semicontinuity for stationary processes are standard inputs recorded in [S3](references.md#s3).

**Corollary 2 — entropy of ground states, conditional on G.** Every minimizer of $`\mathcal W_{\mathrm{all}}`$ or $`\mathcal W_{\mathrm{LS}}`$ has infinite specific relative entropy with respect to $`\Pi^1`$.

**Proof.** Choose a fixed square large enough that every translate and rotation of $`A`$ has at least two points in it. Such a square exists because the lattice has a uniform covering radius, unchanged by translation or rotation. Two suitably separated disks of that covering radius can be placed inside a sufficiently large square.

Any pair from a translate or rotation of $`A`$ has separation in the countable shell set

```math
\mathcal D_A=\{|v|:v\in A\setminus\{0\}\}.
```

For a Poisson configuration in a bounded square, conditional on its finite point count the positions have a joint density. Each prescribed pair distance has probability zero. A finite union over pairs and a countable union over $`\mathcal D_A`$ still has probability zero.

Every ground-state mixture is supported on the event that the chosen square contains a pair whose distance belongs to $`\mathcal D_A`$, whereas Poisson assigns that event zero probability. The restricted ground-state law is therefore singular to Poisson. Its relative entropy is infinite in this square and every larger square. Dividing by the square area and taking the limit proves the claim. $`\square`$

This conditionally answers the Log2 infinite-specific-relative-entropy question posed in Section 1.9 of [S3](references.md#s3).

<a id="low-temperature"></a>

## 12. The zero-temperature limit

We use the standard energy $`\mathcal W_{\mathrm{LS}}`$ in this section. Its lower semicontinuity and compact energy sublevels are the results of Lemma 3.9 in [S3](references.md#s3).

### 12.1 Finite-entropy near-lattice competitors

Choose $`0<2\varepsilon<a`$. Independently displace each point of $`A`$ by a vector uniform in $`B_\varepsilon`$, and then average a uniform translation in a fundamental cell. Denote the resulting stationary intensity-one law by $`P_\varepsilon`$.

Conditional on the uniform translation, each unit-area Voronoi cell contains exactly one point in a centered disk of area $`v=\pi\varepsilon^2`$. That disk lies in its cell because $`\varepsilon<a/2`$. Relative to unit Poisson restricted to the cell, this law has density $`e/v`$ on the event of exactly one point in the disk. Its relative entropy is consequently

```math
1-\log v=1-\log(\pi\varepsilon^2).
```

For a large observation square, take the union of all translated Voronoi cells that meet it. Conditional independence makes the relative entropy on this union the number of cells times the preceding quantity. Restriction to the square can only reduce relative entropy. The number of cells equals the area of the square plus an error of order its perimeter. Convexity of relative entropy allows averaging the uniform translation. Dividing by area and taking the limit gives

```math
\mathrm{ent}(P_\varepsilon\mid\Pi^1)
 \le1-\log(\pi\varepsilon^2)<\infty.
```

### 12.2 The energy of the competitors

First work on the flat torus $`\mathbb R^2/(nA)`$, whose area and number of lattice sites are $`N=n^2`$, with $`n\ge2`$. Give its $`N`$ sites independent uniform $`B_\varepsilon`$ displacements, repeat the perturbed configuration periodically, and average a uniform torus translation.

Let $`G_n`$ be the periodic Green potential satisfying

```math
-\Delta G_n=2\pi\left(\delta_0-\frac1N\right).
```

Away from the torus origin, $`\Delta G_n=2\pi/N`$. For a difference $`z`$ of distinct lattice sites modulo $`nA`$, the disk of radius $`2\varepsilon`$ around $`z`$ avoids that origin. If $`X,Y`$ are independent radial jitters, $`X-Y`$ is radial and supported in that disk. Subtracting the local quadratic particular solution and applying the harmonic mean-value property gives

```math
\mathbb E G_n(z+X-Y)-G_n(z)
 =\frac{\pi}{2N}\mathbb E|X-Y|^2.
```

For uniform disk displacements,

```math
\mathbb E|X|^2=\frac{\varepsilon^2}{2},
\qquad
\mathbb E|X-Y|^2=\varepsilon^2.
```

In the $`\mathcal W_{\mathrm{LS}}`$ normalization, the periodic energy is the ordered Green pair sum divided by $`N`$, plus the configuration-independent regularized self term. There are $`N(N-1)`$ ordered distinct pairs. The expected increase of this periodic candidate energy is therefore exactly

```math
\frac{
  N(N-1)}{N}\frac{\pi\varepsilon^2}{2N}
 =\frac{\pi}{2}\left(1-\frac1N\right)\varepsilon^2.
```

The corresponding increase in the raw field convention is $`\pi^2(1-1/N)\varepsilon^2`$. The self term is unchanged by translating individual sites. The canonical periodic gradient fields supply admissible upper bounds for the point-process energies, which is all that is needed here.

As $`n\to\infty`$, the stationary periodic laws converge locally to $`P_\varepsilon`$. Any fixed bounded window eventually sees independent jitters at distinct sites rather than repeated copies of a torus site. Lower semicontinuity of $`\mathcal W_{\mathrm{LS}}`$ gives

```math
\mathcal W_{\mathrm{LS}}(P_\varepsilon)
 \le \mathcal W_{\mathrm{LS}}(P_A)+\frac{\pi}{2}\varepsilon^2.
```

### 12.3 Free-energy minimizers

For $`\beta>0`$, consider

```math
F_\beta(P)=\frac{\beta}{2}\mathcal W_{\mathrm{LS}}(P)
                +\mathrm{ent}(P\mid\Pi^1)
```

on stationary intensity-one processes. Under G, the lower bound for $`\mathcal W_{\mathrm{LS}}`$, nonnegativity of entropy, compact energy sublevels, and lower semicontinuity give existence of a minimizer by the direct method. The competitors above ensure a finite infimum.

Let $`P_\beta`$ be any minimizer. Comparing it with $`P_\varepsilon`$ and discarding its nonnegative entropy gives

```math
\begin{aligned}
0&\le \mathcal W_{\mathrm{LS}}(P_\beta)-\mathcal W_{\mathrm{LS}}(P_A)\\
 &\le\frac{\pi}{2}\varepsilon^2
      +\frac{2}{\beta}
           \left[1-\log(\pi\varepsilon^2)\right].
\end{aligned}
```

Taking $`\varepsilon=\beta^{-1/2}`$ for sufficiently large $`\beta`$ yields

```math
0\le \mathcal W_{\mathrm{LS}}(P_\beta)-\mathcal W_{\mathrm{LS}}(P_A)
 \le C\frac{1+\log\beta}{\beta}.
```

**Corollary 3 — zero-temperature cluster laws, conditional on G.** Every cluster law of free-energy minimizers $`P_\beta`$ as $`\beta\to\infty`$ is a mixture of uniformly translated, rotated triangular lattices. Moreover,

```math
\mathrm{ent}(P_\beta\mid\Pi^1)\longrightarrow+\infty.
```

**Proof.** The preceding energy estimate places all sufficiently low-temperature minimizers in one compact energy sublevel. Any sequence $`\beta_j\to\infty`$ has a convergent subsequence. Lower semicontinuity and convergence of the energies to the minimum make its limit a ground state. Section 10 classifies that limit.

If the entropies did not diverge, there would be such a sequence with bounded entropy. Extract a convergent subsequence using energy compactness. Entropy lower semicontinuity would give a ground state with finite entropy, contradicting Corollary 2. $`\square`$

The conclusion is convergence to the set of triangular orientation mixtures; it does not select a single orientation. The energy rate itself is not asserted to be new.

The use of finite-entropy near-minimum competitors is established; compare the one-dimensional argument in Section 7.3 of [S10](references.md#s10). The calculation above records its two-dimensional implementation and normalization.

<a id="scope"></a>

## 13. Scope, attribution, and dependencies

The main nonstandard premise is Hypothesis G, as asserted in [S1](references.md#s1). The proof here is conditional on that statement and is not a replacement proof of it. A finite arithmetic checker and selected source arguments have been inspected in the accompanying verification work; this does not certify the entire infinite analytic construction.

The transfer argument uses standard spatial ergodic and spectral representation theorems, Campbell and Palm identities, the classical planar Voronoi equality theorem, periodic Coulomb Green formulas, and the stationary lifting and compactness results of Leblé and Serfaty. Their roles and normalizations are identified in the proof. Additional context for stationary Coulomb energy and spectral theory is supplied by [S6](references.md#s6).

The distinction between minimum values and equality classification is central. Petrache and Serfaty established the universal-optimality-to-Coulomb connection and periodic conclusions in [S2](references.md#s2). Leblé proved a stationary uniqueness result for the one-dimensional logarithmic problem in [S5](references.md#s5). The present argument concerns all stationary minimizers in two dimensions under G. The literature checks recorded with this finding did not locate this exact classification, but they do not establish priority.

Stationarity is essential to the conclusion. Finite deterministic defects may have zero energy-density cost, whereas a nonzero stationary intensity of a local defect is detected by the pair measure. The theorem therefore does not assert that every individual deterministic minimum-energy configuration is exactly a lattice.

A quantitative linear estimate for the density of pairs shorter than the triangular spacing would require additional strictness information and a separate proof. That refinement is outside the theorem proved here.

Established empirical-field results can connect a stationary-minimizer classification to confined logarithmic gases and specified Ginzburg–Landau vortex limits. Their confinement, scaling, applied-field, and limit-order hypotheses must be retained. See [S7](references.md#s7) and [S8](references.md#s8). No claim is made here about a crystalline phase at fixed positive temperature, arbitrary joint limits, arbitrary applied fields, quantum-electron crystallization, or a practical device.
