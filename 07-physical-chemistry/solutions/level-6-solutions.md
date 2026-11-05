# Level 6 — Worked Solutions: Physical Chemistry

> **Level:** Advanced (Level 6 — Physical Chemistry)
> **Items:** 50
> **Exercise bank:** [`../exercises/level-6-exercises.md`](../exercises/level-6-exercises.md)

Each solution gives the **Strategy**, the **Working**, the **Answer** and a
**Check**. Items marked **multi-step** need at least three dependent operations.
Constants are those of the exercise data sheet; intermediate values are carried to
four or five figures and rounded only at the end. In derivations the assumption is
stated where it is used, not collected in a list at the end.

---

## Part A — Conceptual questions

### 1. The content of the four laws

**Strategy.** Give each law the one sentence that identifies what it adds, then
separate the first law (a conservation statement) from the second (a directional
statement).

**Working.** The **zeroth law** states that if A is in thermal equilibrium with B
and B with C, then A is in equilibrium with C. It makes temperature a measurable
property and justifies the thermometer.

The **first law** states that the internal energy of a closed system changes by the
heat absorbed plus the work done on it, $\Delta U = q + w$. It asserts the
equivalence of heat and work and identifies $U$ as a state function; it is a
conservation statement and is time-reversal symmetric.

The **second law** states that the entropy of an isolated system never decreases,
$\Delta S_{\text{univ}} \ge 0$, with equality only for a reversible process. It
introduces the direction of spontaneous change and forbids processes that the first
law permits.

The **third law** states that the entropy of a perfect crystal with a non-degenerate
ground state tends to zero as $T \to 0$, or equivalently that absolute zero cannot
be reached in a finite number of operations. It fixes the absolute entropy scale.

The second law cannot follow from the first because the first law is an equality
that holds for every process consistent with energy conservation, including the
spontaneous flow of heat from cold to hot. A universe in which heat flows uphill
conserves energy perfectly; only the second law excludes it.

**Answer.** Zeroth: temperature. First: internal energy and the equivalence of heat
and work. Second: entropy and the direction of spontaneous change. Third: the
absolute entropy scale and the unattainability of $0\ \text{K}$. The second law is
independent of the first.

**Check.** The first law alone would allow a cup of tea to warm itself while the
room cools; the second law assigns that process $\Delta S_{\text{univ}} < 0$.

**Where marks are lost.** Saying the third law "defines absolute zero" instead of
the entropy at absolute zero, or stating the second law only as "entropy increases"
without the isolated-system qualifier.

### 2. Exact differentials and the integrating factor

**Strategy.** Link exactness to path independence, then test both differentials with
the Euler reciprocity condition.

**Working.** (a) A state function $f(x,y)$ has a unique value at each state, so
$\int_A^B \mathrm{d}f = f(B) - f(A)$ depends only on the endpoints. For an
infinitesimal change $\mathrm{d}f = M\,\mathrm{d}x + N\,\mathrm{d}y$ with
$M = (\partial f/\partial x)_y$ and $N = (\partial f/\partial y)_x$, equality of the
mixed second derivatives (Schwarz) gives
$(\partial M/\partial y)_x = (\partial N/\partial x)_y$. Conversely, if that
condition holds on a simply connected domain, a potential $f$ exists.

(b) For an ideal gas, $\delta q = \mathrm{d}U + p\,\mathrm{d}V
= C_V\,\mathrm{d}T + (nRT/V)\,\mathrm{d}V$. Here $M = C_V$ and $N = nRT/V$, so
$(\partial M/\partial V)_T = 0$ while $(\partial N/\partial T)_V = nR/V \ne 0$. The
differential is inexact: heat is not a state function. Multiplying by $1/T$ gives
$\mathrm{d}S = (C_V/T)\,\mathrm{d}T + (nR/V)\,\mathrm{d}V$, and now
$\partial(C_V/T)/\partial V = 0 = \partial(nR/V)/\partial T$. The factor $1/T$ is
the integrating factor, and the resulting exact differential is
$\mathrm{d}S = \delta q_{\text{rev}}/T$.

(c) For $\mathrm{d}f = y\,\mathrm{d}x - x\,\mathrm{d}y$, $M = y$ and $N = -x$, so
$(\partial M/\partial y)_x = +1$ and $(\partial N/\partial x)_y = -1$. The form is
inexact and no state function has this differential. (It becomes exact after
multiplication by $1/x^2$, since $\mathrm{d}(y/x) = (x\,\mathrm{d}y -
y\,\mathrm{d}x)/x^2$.)

**Answer.** Exactness is equivalent to path independence. $\delta q$ is inexact;
$1/T$ is its integrating factor, producing $\mathrm{d}S$. The form
$y\,\mathrm{d}x - x\,\mathrm{d}y$ is inexact.

**Check.** For a cycle, $\oint \mathrm{d}U = 0$ but $\oint \delta q = \oint \delta w$
can be non-zero; that is the definition of a cycle in a $p$–$V$ diagram.

**Where marks are lost.** Testing exactness at fixed $T$ rather than with the
partial derivative at constant $y$, or claiming $q$ is a state function because a
reversible path has a well-defined $q_{\text{rev}}$.

### 3. A Maxwell relation from the Helmholtz energy

**Strategy.** Differentiate the definition $A = U - TS$, substitute the fundamental
relation, then impose equality of mixed second derivatives.

**Working.** With $A = U - TS$,

$$
\mathrm{d}A = \mathrm{d}U - T\,\mathrm{d}S - S\,\mathrm{d}T
= (T\,\mathrm{d}S - p\,\mathrm{d}V) - T\,\mathrm{d}S - S\,\mathrm{d}T
= -S\,\mathrm{d}T - p\,\mathrm{d}V .
$$

Because $\mathrm{d}A$ is exact, $\partial^2A/\partial V\partial T =
\partial^2A/\partial T\partial V$. From the coefficients,
$(\partial A/\partial T)_V = -S$ and $(\partial A/\partial V)_T = -p$, so

$$
-\left(\frac{\partial S}{\partial V}\right)_T
= -\left(\frac{\partial p}{\partial T}\right)_V
\quad\Longrightarrow\quad
\left(\frac{\partial S}{\partial V}\right)_T
= \left(\frac{\partial p}{\partial T}\right)_V .
$$

The relation replaces an isothermal entropy change, which requires calorimetry and a
reversible heat measurement, by the temperature coefficient of pressure at constant
volume, which follows from an equation of state or from a series of pressure
measurements. For an ideal gas $(\partial p/\partial T)_V = nR/V$, so
$(\partial S/\partial V)_T = nR/V$ and $\Delta S = nR\ln(V_2/V_1)$ at constant $T$.

**Answer.** $\left(\partial S/\partial V\right)_T =
\left(\partial p/\partial T\right)_V$; it converts an inaccessible entropy
derivative into a mechanical one.

**Check.** The sign is positive for a gas: expanding at constant $T$ increases the
entropy and $(\partial p/\partial T)_V > 0$.

**Where marks are lost.** Dropping a minus sign when reading the coefficients of
$\mathrm{d}A$, or differentiating at constant $p$ instead of constant $V$.

### 4. The phase rule

**Strategy.** Count intensive variables, count the equilibrium constraints, and
subtract.

**Working.** (a) Each phase is described by $C - 1$ independent mole fractions plus
$T$ and $p$, so $C + 1$ intensive variables per phase and $P(C+1)$ in total. Thermal
equilibrium imposes $P - 1$ equalities, mechanical equilibrium $P - 1$ more, and
equality of the chemical potential of each component across all phases imposes
$C(P - 1)$. Hence

$$
F = P(C+1) - (P-1) - (P-1) - C(P-1) = C - P + 2 .
$$

(b) (i) Water at its triple point: $C = 1$, $P = 3$, so $F = 0$; the triple point is
fixed. (ii) Liquid water in equilibrium with vapour: $C = 1$, $P = 2$, so $F = 1$;
one variable (for example $T$) fixes $p$. (iii) Aqueous $\ce{NaCl}$ in equilibrium
with vapour: $C = 2$ (water and $\ce{NaCl}$), $P = 2$, so $F = 2$; temperature and
solution composition may be varied independently, and $p$ follows.

(c) Fixing the pressure removes one intensive variable and one degree of freedom,
giving the condensed-phase rule $F = C - P + 1$.

**Answer.** $F = C - P + 2$; $F = 0$, $1$ and $2$ for the three cases;
$F = C - P + 1$ at fixed pressure.

**Check.** A pure substance has a unique boiling point at a fixed pressure, which is
$F = 1 - 2 + 1 = 0$ in the condensed rule: at fixed $p$ the boiling temperature is
fixed.

**Where marks are lost.** Counting the components as the number of chemical species
rather than the number of independent components, or forgetting that the vapour
above a solution is a separate phase.

### 5. Maxwell–Boltzmann, Fermi–Dirac and Bose–Einstein

**Strategy.** Compare the occupation functions, their physical origin, and the limit
in which all three coincide.

**Working.** The mean occupation numbers are

$$
n_i^{\text{MB}} = e^{-(\varepsilon_i-\mu)/k_{\text{B}}T}, \qquad
n_i^{\text{FD}} = \frac{1}{e^{(\varepsilon_i-\mu)/k_{\text{B}}T}+1}, \qquad
n_i^{\text{BE}} = \frac{1}{e^{(\varepsilon_i-\mu)/k_{\text{B}}T}-1}.
$$

Maxwell–Boltzmann describes distinguishable, non-interacting particles and allows
any occupation. Fermi–Dirac describes indistinguishable fermions (half-integral
spin), for which antisymmetry of the wavefunction forbids double occupancy, so
$n_i \le 1$. Bose–Einstein describes indistinguishable bosons (integral spin), for
which multiple occupancy is allowed.

When $e^{(\varepsilon-\mu)/k_{\text{B}}T} \gg 1$ the $\pm 1$ is negligible and both
quantum forms collapse to the exponential. This is the classical limit. It is
equivalent to $n\Lambda^3 \ll 1$: the thermal de Broglie wavelength is small compared
with the mean interparticle spacing, so the wavepackets do not overlap and the
symmetry of the many-particle wavefunction is irrelevant.

Fermi–Dirac explains the finite heat capacity and pressure of conduction electrons,
the Fermi level in semiconductors and the stability of white dwarfs. Bose–Einstein
explains the Planck distribution, phonons, and superfluidity and condensation in
$\ce{^4He}$. Maxwell–Boltzmann explains the classical ideal gas, the Maxwell speed
distribution and the exponential form of the Arrhenius law.

**Answer.** The distributions differ in the denominator; the classical limit is
$n\Lambda^3 \ll 1$, when both quantum forms reduce to the exponential.

**Check.** At $300\ \text{K}$ and $1\ \text{bar}$, $n\Lambda^3 \sim 10^{-7}$ for
argon, so the classical form is accurate; for electrons in a metal it is of order
one or larger, so Fermi–Dirac is required.

**Where marks are lost.** Saying Fermi–Dirac applies to "small particles" rather
than to fermions, or claiming Bose–Einstein requires high temperature.

### 6. Postulates, Hermitian operators and measurement

**Strategy.** State the postulates in the order in which they are used, then explain
the two consequences asked for.

**Working.** The postulates used here are: (1) the state of a system is described by
a normalisable, single-valued, continuous wavefunction $\Psi(\mathbf r,t)$ that
contains all available information; (2) every observable is represented by a
Hermitian operator, and the only possible results of a measurement are its
eigenvalues; (3) for a system in state $\Psi$, the probability of observing
eigenvalue $a_n$ of $\hat A$ is $|\langle a_n|\Psi\rangle|^2$, and immediately after
the measurement the state is the corresponding eigenstate $|a_n\rangle$; (4) the
state evolves according to $i\hbar\,\partial\Psi/\partial t = \hat H\Psi$; (5) the
wavefunction of identical fermions is antisymmetric and of identical bosons is
symmetric under exchange.

Observables are Hermitian because Hermiticity guarantees real eigenvalues, which is
required of a measured quantity, and orthogonal eigenfunctions that form a complete
basis, which is required for the expansion and the probability rule. Hermiticity also
conserves the norm.

The commutator $[\hat x,\hat p_x] = i\hbar$ means that $\hat x$ and $\hat p_x$ have
no simultaneous eigenbasis, so a state cannot possess definite values of both. It
implies the Robertson bound $\sigma_x\sigma_p \ge \hbar/2$. It does not mean that
either quantity is unmeasurable, nor that a measurement cannot be repeated.

The measurement postulate is non-destructive projection: after a measurement with
outcome $a_n$, the state is projected onto $|a_n\rangle$, and an immediate repeat
measurement returns $a_n$ with certainty.

**Answer.** Real eigenvalues and a complete orthogonal basis follow from
Hermiticity; the commutator forbids simultaneous sharp values and gives
$\sigma_x\sigma_p \ge \hbar/2$; measurement collapses the state onto the
eigenstate of the observed eigenvalue.

**Check.** A free particle is not in an eigenstate of $\hat x$ or $\hat p$; a
localised state is a superposition of momenta, consistent with the bound.

**Where marks are lost.** Writing the uncertainty relation as an equality, or
saying the commutator means that momentum cannot be measured.

### 7. The Born–Oppenheimer approximation

**Strategy.** Separate the electronic and nuclear coordinates, justify the separation
by the mass ratio, then state where the separation breaks down.

**Working.** Write the molecular wavefunction as
$\Psi(\mathbf r,\mathbf R) \approx \psi_{\text{el}}(\mathbf r;\mathbf R)\,
\chi_{\text{nuc}}(\mathbf R)$, where $\mathbf r$ denotes electronic and $\mathbf R$
nuclear coordinates. For each fixed $\mathbf R$ solve

$$
\hat H_{\text{el}}(\mathbf R)\psi_{\text{el}}(\mathbf r;\mathbf R)
= E_{\text{el}}(\mathbf R)\psi_{\text{el}}(\mathbf r;\mathbf R).
$$

The electronic energy, plus the nuclear repulsion, is then used as the potential
$V(\mathbf R)$ in the nuclear Schrödinger equation. Because $M/m_{\text{e}} \ge 1836$,
nuclear velocities are smaller than electronic velocities by roughly
$(m_{\text{e}}/M)^{1/2} \sim 1/43$, so the electrons adjust essentially
instantaneously to nuclear motion. The resulting $E_{\text{el}}(\mathbf R)$ is the
potential energy surface on which molecular structure, vibrational frequencies and
reaction barriers are defined.

The approximation fails when two electronic states become degenerate or nearly
degenerate, at a conical intersection, because the nuclear kinetic energy operator
then couples them strongly; this is the mechanism of most photochemical
non-radiative decay. It also fails when nuclear quantum effects are large, as for
proton transfer and hydrogen tunnelling, and when the electronic gap is comparable
to a vibrational quantum.

**Answer.** The approximation freezes the nuclei, solves the electronic problem
parametrically in $\mathbf R$, and uses $E_{\text{el}}(\mathbf R)$ as the potential
for nuclear motion; it fails at conical intersections and for light-atom quantum
effects.

**Check.** The approximation is best for heavy nuclei and large electronic gaps,
which is why it works well for ground-state organic chemistry and poorly for
photochemistry near avoided crossings.

**Where marks are lost.** Saying the approximation "assumes nuclei do not move"
instead of "nuclei move slowly compared with electrons", or omitting the nuclear
repulsion from the potential.

### 8. The Jablonski diagram

**Strategy.** List the states, then the transitions in order of timescale, then the
two rules asked for.

**Working.** The diagram arranges singlet states $S_0, S_1, S_2$ and triplet states
$T_1, T_2$ vertically by energy. Absorption $S_0 \to S_n$ is spin-allowed and takes
about $10^{-15}\ \text{s}$. Vibrational relaxation within a state and internal
conversion between states of the same spin take $10^{-12}$–$10^{-10}\ \text{s}$.
Fluorescence $S_1 \to S_0$ is spin-allowed and takes $10^{-9}$–$10^{-7}\ \text{s}$.
Intersystem crossing $S_1 \to T_1$ is spin-forbidden but spin–orbit coupling makes it
possible in $10^{-10}$–$10^{-6}\ \text{s}$. Phosphorescence $T_1 \to S_0$ is
spin-forbidden and takes $10^{-3}$–$10\ \text{s}$.

Kasha's rule states that emission occurs from the lowest vibrational level of the
lowest excited state of a given multiplicity, because vibrational relaxation and
internal conversion from higher states are faster than radiative decay. The triplet
lies below the corresponding singlet because the exchange interaction stabilises
parallel spins, so phosphorescence is red-shifted relative to fluorescence and, being
spin-forbidden, is much slower.

The fluorescence quantum yield is
$\phi_{\text{F}} = k_{\text{F}}/(k_{\text{F}} + k_{\text{IC}} + k_{\text{ISC}}
+ k_Q[Q])$, and the lifetime is the reciprocal of the same denominator,
$\tau = 1/(k_{\text{F}} + k_{\text{IC}} + k_{\text{ISC}} + k_Q[Q])$.

**Answer.** Absorption, vibrational relaxation, internal conversion, fluorescence,
intersystem crossing and phosphorescence, with the timescales above; Kasha's rule
follows from fast internal conversion; phosphorescence is red-shifted because $T_1$
lies below $S_1$; $\phi_{\text{F}} = k_{\text{F}}\tau$.

**Check.** A molecule with $\phi_{\text{F}} = 1$ has $k_{\text{F}} \gg$ all
non-radiative rates and $\tau = 1/k_{\text{F}}$, the natural radiative lifetime.

**Where marks are lost.** Drawing phosphorescence from $S_1$, or stating Kasha's rule
as a conservation law rather than a kinetic result.

---

## Part B — Derivations

### 9. The fundamental relation and a Maxwell relation

**Strategy.** Combine the first law for a reversible path with the second-law
definition of entropy, then cross-differentiate.

**Working.** For a closed system doing only $pV$ work, the first law is

$$
\mathrm{d}U = \delta q + \delta w .
$$

For a reversible path the work is $\delta w = -p\,\mathrm{d}V$, and the second law
defines $\delta q_{\text{rev}} = T\,\mathrm{d}S$. Substituting,

$$
\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V .
$$

The assumptions are: closed system, only $pV$ work, a reversible path through
equilibrium states, and uniform $T$ and $p$. Because $U$, $S$ and $V$ are state
functions, the relation connects equilibrium states and holds for any path between
them, although it was derived for a reversible one.

Since $\mathrm{d}U$ is exact,

$$
\left(\frac{\partial T}{\partial V}\right)_S
= \frac{\partial^2 U}{\partial V\,\partial S}
= -\left(\frac{\partial p}{\partial S}\right)_V .
$$

**Answer.** $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V$ and
$(\partial T/\partial V)_S = -(\partial p/\partial S)_V$.

**Check.** For an ideal gas, $S = C_V\ln T + nR\ln V + \text{const}$, so at constant
$S$, $\mathrm{d}T/T = -(nR/C_V)\,\mathrm{d}V/V$ and
$(\partial T/\partial V)_S = -nRT/(C_VV)$. Also
$(\partial p/\partial S)_V = (\partial p/\partial T)_V(\partial T/\partial S)_V
= (nR/V)(T/C_V) = nRT/(C_VV)$, so the relation holds with the minus sign.

**Where marks are lost.** Using $\delta q = \mathrm{d}U + p\,\mathrm{d}V$ for an
irreversible path and then treating $p$ as the system pressure; the identity requires
the reversible path.

### 10. $C_p - C_V = nR$

**Strategy.** Differentiate $H = U + pV$ at constant pressure and expand
$(\partial U/\partial T)_p$ in terms of $T$ and $V$.

**Working.** From $H = U + pV$,

$$
C_p = \left(\frac{\partial H}{\partial T}\right)_p
= \left(\frac{\partial U}{\partial T}\right)_p
+ p\left(\frac{\partial V}{\partial T}\right)_p .
$$

Treating $U$ as a function of $T$ and $V$,

$$
\left(\frac{\partial U}{\partial T}\right)_p
= \left(\frac{\partial U}{\partial T}\right)_V
+ \left(\frac{\partial U}{\partial V}\right)_T
\left(\frac{\partial V}{\partial T}\right)_p .
$$

Hence

$$
C_p = C_V + \left[\left(\frac{\partial U}{\partial V}\right)_T + p\right]
\left(\frac{\partial V}{\partial T}\right)_p .
$$

Ideality enters twice: $(\partial U/\partial V)_T = 0$ (Joule's law, no interaction
energy) and $pV = nRT$, so $(\partial V/\partial T)_p = nR/p$. Therefore

$$
C_p - C_V = p\cdot\frac{nR}{p} = nR .
$$

For a real gas $(\partial U/\partial V)_T = T(\partial p/\partial T)_V - p \ne 0$,
so the difference is not $nR$; it approaches $nR$ only as $p \to 0$.

**Answer.** $C_p - C_V = nR$, with ideality used for both the internal pressure and
the equation of state.

**Check.** For a monatomic ideal gas $C_V = \tfrac{3}{2}nR$ and
$C_p = \tfrac{5}{2}nR$, so the difference is $nR$, as observed.

**Where marks are lost.** Assuming $(\partial U/\partial T)_p = C_V$ without
justification; that equality holds only because $(\partial U/\partial V)_T = 0$.

### 11. Clapeyron and Clausius–Clapeyron

**Strategy.** Equate the chemical potentials along the coexistence curve, expand both
sides, and then integrate with the ideal-vapour approximation.

**Working.** At coexistence $\mu_\alpha(T,p) = \mu_\beta(T,p)$. Moving along the
coexistence curve by $\mathrm{d}T$ and $\mathrm{d}p$ keeps the phases in equilibrium,
so $\mathrm{d}\mu_\alpha = \mathrm{d}\mu_\beta$. With
$\mathrm{d}\mu = -S_{\text{m}}\,\mathrm{d}T + V_{\text{m}}\,\mathrm{d}p$,

$$
-S_{\alpha}\,\mathrm{d}T + V_{\alpha}\,\mathrm{d}p
= -S_{\beta}\,\mathrm{d}T + V_{\beta}\,\mathrm{d}p ,
$$

so

$$
\frac{\mathrm{d}p}{\mathrm{d}T}
= \frac{S_{\beta} - S_{\alpha}}{V_{\beta} - V_{\alpha}}
= \frac{\Delta_{\text{trs}}S}{\Delta_{\text{trs}}V}
= \frac{\Delta_{\text{trs}}H}{T\,\Delta_{\text{trs}}V} .
$$

The assumptions are a pure substance, two phases in equilibrium, and reversible
transfer of latent heat, so that $\Delta S = \Delta H/T$.

For liquid–vapour equilibrium, treat the vapour as ideal,
$V_{\text{m,g}} = RT/p$, neglect $V_{\text{m,l}}$ compared with $V_{\text{m,g}}$,
and assume $\Delta_{\text{vap}}H$ independent of $T$. Then

$$
\frac{\mathrm{d}p}{\mathrm{d}T} = \frac{p\,\Delta_{\text{vap}}H}{RT^2}
\quad\Longrightarrow\quad
\frac{\mathrm{d}\ln p}{\mathrm{d}T} = \frac{\Delta_{\text{vap}}H}{RT^2},
$$

and integrating between $(T_1,p_1)$ and $(T_2,p_2)$ gives

$$
\ln\frac{p_2}{p_1} = -\frac{\Delta_{\text{vap}}H}{R}
\left(\frac{1}{T_2} - \frac{1}{T_1}\right).
$$

**Answer.** $\mathrm{d}p/\mathrm{d}T = \Delta H/(T\Delta V)$; the integrated form is
$\ln(p_2/p_1) = -(\Delta H/R)(1/T_2 - 1/T_1)$.

**Check.** For water, $\Delta_{\text{vap}}H > 0$ and $\Delta V > 0$, so
$\mathrm{d}p/\mathrm{d}T > 0$: vapour pressure rises with temperature.

**Where marks are lost.** Using $\Delta H$ per molecule with $R$ instead of per
mole, or forgetting the reciprocal-temperature difference and integrating as if
$1/T^2$ were constant.

### 12. The Boltzmann distribution

**Strategy.** Maximise the logarithm of the number of microstates subject to the two
constraints, using Stirling's approximation and Lagrange multipliers.

**Working.** For $n_i$ particles in level $i$,

$$
W = \frac{N!}{\prod_i n_i!},
\qquad
\ln W = N\ln N - N - \sum_i (n_i\ln n_i - n_i)
= N\ln N - \sum_i n_i\ln n_i .
$$

The constraints are $\sum_i n_i = N$ and $\sum_i n_i\varepsilon_i = E$, so
$\sum_i \mathrm{d}n_i = 0$ and $\sum_i \varepsilon_i\,\mathrm{d}n_i = 0$. Setting
$\mathrm{d}\ln W = 0$,

$$
\mathrm{d}\ln W = -\sum_i (\ln n_i + 1)\,\mathrm{d}n_i = 0 .
$$

Introduce multipliers $\alpha$ and $\beta$ for the two constraints:

$$
\sum_i \left(\ln n_i + 1 + \alpha + \beta\varepsilon_i\right)\mathrm{d}n_i = 0 .
$$

Since the $\mathrm{d}n_i$ are otherwise independent,
$\ln n_i = -(1+\alpha) - \beta\varepsilon_i$, so

$$
n_i = C e^{-\beta\varepsilon_i}, \qquad
\frac{n_i}{N} = \frac{e^{-\beta\varepsilon_i}}{q}, \qquad
q = \sum_i e^{-\beta\varepsilon_i}.
$$

The molecular partition function is $q$; for $N$ independent distinguishable
molecules $Q = q^N$, and for indistinguishable molecules $Q = q^N/N!$.

To identify $\beta$, use $S = k_{\text{B}}\ln W = k_{\text{B}}(N\ln q + \beta U)$ and
$(\partial S/\partial U)_V = 1/T$. Since
$\mathrm{d}\ln q/\mathrm{d}\beta = -\langle\varepsilon\rangle$ and
$U = -N\,\mathrm{d}\ln q/\mathrm{d}\beta$, differentiation gives
$(\partial S/\partial U)_V = k_{\text{B}}\beta$, hence $\beta = 1/k_{\text{B}}T$.

**Answer.** $n_i/N = e^{-\varepsilon_i/k_{\text{B}}T}/q$ with
$q = \sum_i e^{-\varepsilon_i/k_{\text{B}}T}$ and $\beta = 1/k_{\text{B}}T$.

**Check.** For a two-level system with gap $\varepsilon$, the ratio
$n_1/n_0 = e^{-\varepsilon/k_{\text{B}}T}$, which tends to zero as $T \to 0$ and to
one as $T \to \infty$, as required.

**Where marks are lost.** Omitting the $+1$ in $\mathrm{d}\ln W$ (harmless after
normalisation but wrong in the derivation), or treating the particles as
distinguishable in $Q$ for a gas.

### 13. The translational partition function

**Strategy.** Write the box energies, convert the sum to an integral over momentum,
and evaluate the Gaussian integral.

**Working.** For a particle in a cubic box of side $L$,

$$
\varepsilon = \frac{h^2}{8mL^2}\left(n_x^2+n_y^2+n_z^2\right),
\qquad n_x,n_y,n_z = 1,2,\dots
$$

The partition function is

$$
q_{\text{trans}} = \sum_{n_x,n_y,n_z} e^{-\beta h^2(n_x^2+n_y^2+n_z^2)/8mL^2}.
$$

At ordinary $T$ and macroscopic $L$ the levels are so close that the sum may be
replaced by an integral. With $p_x = hn_x/2L$, so $\mathrm{d}n_x = (2L/h)\,\mathrm{d}p_x$,

$$
q_{\text{trans}} = \left(\frac{2L}{h}\right)^3
\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}
e^{-\beta(p_x^2+p_y^2+p_z^2)/2m}\,\mathrm{d}p_x\,\mathrm{d}p_y\,\mathrm{d}p_z .
$$

Each integral is $\sqrt{2\pi mk_{\text{B}}T}$, so

$$
q_{\text{trans}} = \frac{V}{h^3}(2\pi mk_{\text{B}}T)^{3/2}
= \frac{V}{\Lambda^3},
\qquad
\Lambda = \frac{h}{\sqrt{2\pi mk_{\text{B}}T}} .
$$

The replacement is legitimate when the spacing between levels is much smaller than
$k_{\text{B}}T$, that is $L \gg \Lambda$, and when the gas is dilute enough that
$n\Lambda^3 \ll 1$.

**Answer.** $q_{\text{trans}} = V/\Lambda^3$ with
$\Lambda = h/(2\pi mk_{\text{B}}T)^{1/2}$.

**Check.** For argon at $298\ \text{K}$, $\Lambda \approx 1.6\times10^{-11}\ \text{m}$,
so $\Lambda \ll L$ for any laboratory box, and $q \sim 10^{29}$ in $1\ \text{dm}^3$.

**Where marks are lost.** Integrating over $x$ rather than $p$ without the density of
states, which loses a factor of $h^3$, or using $h$ instead of $\hbar$ in the
energy.

### 14. The particle in a one-dimensional box

**Strategy.** Solve the free-particle Schrödinger equation and apply the two boundary
conditions.

**Working.** Inside the box $V = 0$, so

$$
-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2\psi}{\mathrm{d}x^2} = E\psi
\quad\Longrightarrow\quad
\frac{\mathrm{d}^2\psi}{\mathrm{d}x^2} = -k^2\psi,
\qquad k^2 = \frac{2mE}{\hbar^2}.
$$

The general solution is $\psi = A\sin kx + B\cos kx$. The infinite wall at $x = 0$
requires $\psi(0) = 0$, so $B = 0$. The wall at $x = L$ requires $\psi(L) = 0$, so
$\sin kL = 0$ and $kL = n\pi$ with $n = 1,2,3,\dots$ ($n = 0$ gives the trivial
solution). Therefore

$$
E_n = \frac{\hbar^2k^2}{2m} = \frac{n^2\pi^2\hbar^2}{2mL^2}
= \frac{n^2h^2}{8mL^2}.
$$

Normalisation gives

$$
\int_0^L A^2\sin^2\frac{n\pi x}{L}\,\mathrm{d}x = A^2\frac{L}{2} = 1
\quad\Longrightarrow\quad
A = \sqrt{\frac{2}{L}} .
$$

The wavefunction $\sin(n\pi x/L)$ has $n-1$ interior nodes.

**Answer.** $E_n = n^2h^2/8mL^2$,
$\psi_n = (2/L)^{1/2}\sin(n\pi x/L)$, with $n-1$ nodes.

**Check.** The ground state has no node and finite energy, consistent with the
uncertainty principle: confining the particle increases its momentum spread and hence
its energy as $L$ decreases.

**Where marks are lost.** Allowing $n = 0$, which gives $\psi = 0$ everywhere, or
using $n^2h^2/4mL^2$ from confusing $h$ and $\hbar$ in $k = 2\pi/\lambda$.

### 15. The variational theorem

**Strategy.** Expand the trial function in the exact eigenbasis, then use the
ordering of the eigenvalues.

**Working.** Let $\hat H\psi_n = E_n\psi_n$ with $E_0 \le E_1 \le \dots$ and
$\langle\psi_m|\psi_n\rangle = \delta_{mn}$. Expand a normalised trial function as
$\phi = \sum_n c_n\psi_n$ with $\sum_n|c_n|^2 = 1$. Then

$$
\langle\phi|\hat H|\phi\rangle
= \sum_n |c_n|^2E_n
\ge E_0\sum_n|c_n|^2 = E_0 .
$$

Equality holds only if every $c_n$ with $E_n > E_0$ vanishes, that is if $\phi$ is the
true ground state. This proves the upper bound.

For the linear method, write $\phi = \sum_i c_i\chi_i$ with a non-orthogonal basis
and overlap $S_{ij} = \langle\chi_i|\chi_j\rangle$. Minimise
$\langle\phi|\hat H|\phi\rangle$ subject to $\langle\phi|\phi\rangle = 1$ using a
multiplier $E$:

$$
\frac{\partial}{\partial c_i}\left[
\sum_{jk}c_j^*H_{jk}c_k
- E\left(\sum_{jk}c_j^*S_{jk}c_k - 1\right)\right] = 0
\quad\Longrightarrow\quad
\sum_k (H_{ik} - ES_{ik})c_k = 0 .
$$

A non-trivial solution requires $\det(H_{ik} - ES_{ik}) = 0$, the secular equation.
Its roots are upper bounds to the true energies; the lowest root bounds $E_0$ from
above, and the roots interlace the exact levels because the trial space is a subspace
of the full Hilbert space.

**Answer.** $\langle\phi|\hat H|\phi\rangle \ge E_0$ with equality only for the exact
ground state; the linear method gives $\det(H - ES) = 0$, whose lowest root is the
best variational estimate of $E_0$.

**Check.** With a one-function basis the root is $H_{11}/S_{11}$, the expectation
value of that function, which must lie above $E_0$.

**Where marks are lost.** Forgetting the overlap matrix $S$ for a non-orthogonal
basis, or claiming the variational theorem bounds every excited state from above
independently of symmetry.

### 16. The Eyring equation

**Strategy.** Treat the transition state as a species in quasi-equilibrium with the
reactants, multiply its concentration by the frequency of crossing the barrier, then
convert the equilibrium constant to $\Delta G^\ddagger$.

**Working.** For $\ce{A + B <=>[$^\ddagger$]}$ with equilibrium constant
$K^\ddagger = a^\ddagger/(a_{\text{A}}a_{\text{B}})$, the rate is the concentration of
transition states multiplied by the frequency with which they cross to products.
The reaction coordinate is a free translation of length $\delta$ with a frequency
$\nu = k_{\text{B}}T/h$, so

$$
v = \nu[\ddagger] = \frac{k_{\text{B}}T}{h}[\ddagger],
\qquad
k = \frac{k_{\text{B}}T}{h}K^\ddagger .
$$

With $K^\ddagger = \exp(-\Delta G^\ddagger/RT)$ and a transmission coefficient
$\kappa$ for recrossing and tunnelling,

$$
k = \kappa\frac{k_{\text{B}}T}{h}\exp\left(-\frac{\Delta G^\ddagger}{RT}\right).
$$

The assumptions are: quasi-equilibrium between reactants and transition state; the
reaction coordinate is separable and has one imaginary frequency; the transmission
coefficient accounts for dynamics on either side of the barrier; and the other modes
are treated classically or with their own partition functions.

Writing $\Delta G^\ddagger = \Delta H^\ddagger - T\Delta S^\ddagger$,

$$
\ln k = \ln\frac{k_{\text{B}}T}{h} + \frac{\Delta S^\ddagger}{R}
- \frac{\Delta H^\ddagger}{RT}.
$$

Differentiating with respect to $T$ at constant pressure,

$$
\frac{\mathrm{d}\ln k}{\mathrm{d}T}
= \frac{1}{T} + \frac{\Delta H^\ddagger}{RT^2},
\qquad
E_{\text{a}} = RT^2\frac{\mathrm{d}\ln k}{\mathrm{d}T}
= \Delta H^\ddagger + RT .
$$

For a bimolecular reaction the equilibrium constant carries the dimension of inverse
concentration; converting from the pressure standard state to the concentration
standard state introduces one further factor of $T$, so
$E_{\text{a}} = \Delta H^\ddagger + 2RT$. In general
$E_{\text{a}} = \Delta H^\ddagger + nRT$ for an $n$-molecular reaction.

**Answer.** $k = \kappa(k_{\text{B}}T/h)e^{-\Delta G^\ddagger/RT}$, with
$E_{\text{a}} = \Delta H^\ddagger + nRT$.

**Check.** For a unimolecular reaction at $298\ \text{K}$, $RT = 2.48\ \text{kJ mol}^{-1}$,
so $E_{\text{a}}$ exceeds $\Delta H^\ddagger$ by that amount, as observed for
first-order gas-phase decompositions.

**Where marks are lost.** Omitting the $k_{\text{B}}T/h$ prefactor and quoting only
the exponential, or using $\Delta H^\ddagger$ and $\Delta G^\ddagger$ interchangeably.

## Part C — Basic calculations

### 17. Isothermal reversible expansion

**Strategy.** For an ideal gas at constant $T$, $\Delta U = \Delta H = 0$; the work
follows from $w = -\int p\,\mathrm{d}V$ and the entropy from the reversible heat.

**Working.** **Multi-step.**

$$
w = -nRT\ln\frac{V_2}{V_1}
= -(2.00)(8.314462618)(298.15)\ln\frac{30.0}{10.0}
= -5.4468\times10^{3}\ \text{J}.
$$

Since $\Delta U = q + w = 0$, $q = -w = +5.4468\ \text{kJ}$. For an ideal gas
$\Delta H = \Delta U + \Delta(nRT) = 0$. The entropy change is

$$
\Delta S = \frac{q_{\text{rev}}}{T}
= \frac{5446.8}{298.15} = 18.269\ \text{J K}^{-1},
$$

or equivalently $nR\ln(V_2/V_1) = 18.269\ \text{J K}^{-1}$. The surroundings lose
$18.269\ \text{J K}^{-1}$, so $\Delta S_{\text{univ}} = 0$.

**Answer.** $q = +5.45\ \text{kJ}$, $w = -5.45\ \text{kJ}$,
$\Delta U = \Delta H = 0$, $\Delta S = +18.3\ \text{J K}^{-1}$,
$\Delta S_{\text{univ}} = 0$.

**Check.** The gas does work, so $w < 0$; it must absorb heat to stay isothermal, so
$q > 0$; the expansion is reversible, so the universe gains no entropy.

**Where marks are lost.** Reporting $\Delta S_{\text{univ}} = 18.3\ \text{J K}^{-1}$
by forgetting the surroundings, or using $C_V\ln(T_2/T_1)$ when $T$ is constant.

### 18. Reversible adiabatic expansion

**Strategy.** Use the adiabatic relation between $T$ and $p$, then get $V$ from the
ideal-gas law and $w$ from $\Delta U$.

**Working.** **Multi-step.** For a reversible adiabatic process,
$T p^{(1-\gamma)/\gamma} = \text{const}$ with $\gamma = C_p/C_V = 5/3$, so

$$
T_2 = T_1\left(\frac{p_2}{p_1}\right)^{(\gamma-1)/\gamma}
= 300.0\left(\frac{1.00}{5.00}\right)^{0.400}
= 157.59\ \text{K}.
$$

The initial volume is $V_1 = nRT_1/p_1 = 4.9887\ \text{dm}^3$, and

$$
V_2 = \frac{nRT_2}{p_2} = 13.103\ \text{dm}^3 .
$$

For an adiabatic process $q = 0$, so

$$
w = \Delta U = nC_{V,\text{m}}(T_2-T_1)
= (1.00)(12.4717)(157.59-300.0) = -1.776\times10^{3}\ \text{J}.
$$

The enthalpy change is
$\Delta H = nC_{p,\text{m}}\Delta T = (1.00)(20.786)(-142.41)
= -2.960\times10^{3}\ \text{J}$.

**Answer.** $T_2 = 158\ \text{K}$, $V_2 = 13.1\ \text{dm}^3$,
$w = -1.78\ \text{kJ}$, $\Delta H = -2.96\ \text{kJ}$.

**Check.** $V_2/V_1 = 2.626$ and $(p_1/p_2)^{1/\gamma} = 5^{0.6} = 2.626$, as the
adiabatic relation requires. Cooling on expansion is expected.

**Where marks are lost.** Using $T_2/T_1 = (p_2/p_1)^{(\gamma-1)}$ and omitting the
division by $\gamma$, or using $C_p$ to compute $w$.

### 19. Kirchhoff's law

**Strategy.** Compute $\Delta C_p$ from the stoichiometric coefficients and integrate
it over the temperature interval.

**Working.** **Multi-step.** For
$\ce{CH4(g) + 2O2(g) -> CO2(g) + 2H2O(l)}$,

$$
\Delta C_p = C_p(\ce{CO2}) + 2C_p(\ce{H2O,l}) - C_p(\ce{CH4}) - 2C_p(\ce{O2})
= 37.1 + 150.6 - 35.7 - 58.8 = 93.2\ \text{J K}^{-1}\text{mol}^{-1}.
$$

With $\Delta C_p$ constant,

$$
\Delta_\text{r}H^\circ(373.15) = \Delta_\text{r}H^\circ(298.15) + \Delta C_p\Delta T
= -890.3 + \frac{93.2\times75.00}{1000}
= -890.3 + 6.99 = -883.3\ \text{kJ mol}^{-1}.
$$

**Answer.** $\Delta_\text{r}H^\circ(373.15) = -883\ \text{kJ mol}^{-1}$.

**Check.** The reaction produces fewer gas moles than it consumes and the products
include liquid water, so $\Delta C_p > 0$ and the combustion becomes less exothermic
as $T$ rises, as found.

**Where marks are lost.** Forgetting the stoichiometric coefficient 2 for water and
oxygen, or integrating $\Delta C_p$ without converting J to kJ.

### 20. Clausius–Clapeyron

**Strategy.** Integrate the Clausius–Clapeyron equation between the normal boiling
point and the required temperature.

**Working.**

$$
\ln\frac{p_2}{p_1} = -\frac{\Delta_{\text{vap}}H}{R}
\left(\frac{1}{T_2}-\frac{1}{T_1}\right)
= -\frac{40\,700}{8.314462618}
\left(\frac{1}{363.15}-\frac{1}{373.15}\right).
$$

The bracket is $2.75368\times10^{-3} - 2.67989\times10^{-3} = 7.3793\times10^{-5}\ \text{K}^{-1}$,
so the exponent is $-4895.0\times7.3793\times10^{-5} = -0.36122$. Hence

$$
p_2 = 101.325\,e^{-0.36122} = 70.60\ \text{kPa}.
$$

**Answer.** $p \approx 70.6\ \text{kPa}$ at $363.15\ \text{K}$.

**Check.** The normal boiling point of water is $373.15\ \text{K}$ at
$101.3\ \text{kPa}$; at $363\ \text{K}$ the vapour pressure is about
$0.70\ \text{atm}$, consistent with the measured value near $70\ \text{kPa}$.

**Where marks are lost.** Using $T$ in Celsius inside $1/T$, or using the gas
constant per molecule.

### 21. Two-level Boltzmann population

**Strategy.** Convert the wavenumber gap to an energy and apply the Boltzmann factor.

**Working.** The energy gap is $\Delta\varepsilon = hc\tilde\nu$ with
$hc = 1.98644586\times10^{-23}\ \text{J cm}$. For $\tilde\nu = 100.0\ \text{cm}^{-1}$,

$$
\Delta\varepsilon = 1.98644586\times10^{-21}\ \text{J},
\qquad
k_{\text{B}}T = 1.380649\times10^{-23}\times300.0 = 4.14195\times10^{-21}\ \text{J}.
$$

Therefore $\Delta\varepsilon/k_{\text{B}}T = 0.47960$ and

$$
\frac{n_1}{n_0} = e^{-0.47960} = 0.6190,
\qquad
\frac{n_1}{n_0+n_1} = \frac{0.6190}{1.6190} = 0.3823 .
$$

**Answer.** $n_1/n_0 = 0.619$; $38.2\ \%$ of the molecules are in the upper level.

**Check.** The gap corresponds to $144\ \text{K}$ in temperature units
($\theta = hc\tilde\nu/k_{\text{B}} = 1.4388\times100 = 143.9\ \text{K}$), comparable
to $300\ \text{K}$, so substantial excited population is expected.

**Where marks are lost.** Forgetting the degeneracy factor when the levels are
degenerate, or computing $n_1/(n_0+n_1)$ as $e^{-x}$ instead of $e^{-x}/(1+e^{-x})$.

### 22. Translational partition function of argon

**Strategy.** Compute $\Lambda$ and use $q = V/\Lambda^3$.

**Working.** **Multi-step.** The molecular mass is
$m = 39.948\times1.66053906660\times10^{-27} = 6.6335\times10^{-26}\ \text{kg}$, so

$$
\Lambda = \frac{h}{\sqrt{2\pi mk_{\text{B}}T}}
= \frac{6.62607015\times10^{-34}}
{\sqrt{2\pi(6.6335\times10^{-26})(1.380649\times10^{-23})(298.15)}}
= 1.5997\times10^{-11}\ \text{m}.
$$

Then

$$
q_{\text{trans}} = \frac{V}{\Lambda^3}
= \frac{1.00\times10^{-3}}{(1.5997\times10^{-11})^3}
= \frac{1.00\times10^{-3}}{4.096\times10^{-33}}
= 2.44\times10^{29}.
$$

**Answer.** $q_{\text{trans}} = 2.44\times10^{29}$.

**Check.** $\Lambda \approx 0.016\ \text{nm}$, far smaller than the box and than the
mean interparticle spacing at this density, so the classical integral is valid and
$q \gg 1$.

**Where marks are lost.** Using the molar mass in place of the molecular mass, which
makes $\Lambda$ too small by a factor of $\sqrt{N_{\text{A}}}$.

### 23. Rotational and vibrational partition functions of CO

**Strategy.** Convert $B$ and $\tilde\nu$ to characteristic temperatures, then use the
high-temperature rotational and harmonic vibrational expressions.

**Working.** **Multi-step.**

$$
\theta_{\text{rot}} = \frac{hcB}{k_{\text{B}}}
= \frac{(1.98644586\times10^{-23})(1.931)}{1.380649\times10^{-23}}
= 2.778\ \text{K},
$$

$$
\theta_{\text{vib}} = \frac{hc\tilde\nu}{k_{\text{B}}}
= \frac{(1.98644586\times10^{-23})(2143)}{1.380649\times10^{-23}}
= 3083\ \text{K}.
$$

With $\sigma = 1$,

$$
q_{\text{rot}} = \frac{T}{\sigma\theta_{\text{rot}}}
= \frac{298.15}{2.778} = 107.3,
\qquad
q_{\text{vib}} = \frac{1}{1-e^{-\theta_{\text{vib}}/T}}
= \frac{1}{1-e^{-10.34}} = 1.00003 .
$$

**Answer.** $\theta_{\text{rot}} = 2.78\ \text{K}$,
$\theta_{\text{vib}} = 3.08\times10^{3}\ \text{K}$, $q_{\text{rot}} = 107$,
$q_{\text{vib}} \approx 1.000$.

**Check.** $T \gg \theta_{\text{rot}}$, so the classical rotational integral is valid;
$T \ll \theta_{\text{vib}}$, so essentially only $v = 0$ is populated, consistent with
$q_{\text{vib}} \approx 1$.

**Where marks are lost.** Using $\sigma = 2$ for the heteronuclear CO, or forgetting
to convert cm⁻¹ to m⁻¹ before dividing by $k_{\text{B}}$.

### 24. Electron in a one-nanometre box

**Strategy.** Use $E_n = n^2h^2/8mL^2$, form the difference, then convert to a photon
wavelength.

**Working.** **Multi-step.**

$$
E_1 = \frac{h^2}{8m_{\text{e}}L^2}
= \frac{(6.62607015\times10^{-34})^2}
{8(9.1093837015\times10^{-31})(1.00\times10^{-9})^2}
= 6.0247\times10^{-20}\ \text{J}.
$$

In electronvolts, $E_1 = 6.0247\times10^{-20}/1.602176634\times10^{-19}
= 0.3760\ \text{eV}$. Since $E_2 = 4E_1$,

$$
\Delta E = 3E_1 = 1.8074\times10^{-19}\ \text{J} = 1.1281\ \text{eV}.
$$

The photon wavelength is

$$
\lambda = \frac{hc}{\Delta E}
= \frac{(6.62607015\times10^{-34})(2.99792458\times10^{8})}
{1.8074\times10^{-19}}
= 1.0991\times10^{-6}\ \text{m}.
$$

(d) For hydrogen, $\Delta E = 13.6(1 - 1/4) = 10.2\ \text{eV}
= 1.634\times10^{-18}\ \text{J}$, so

$$
\lambda = \frac{hc}{\Delta E}
= \frac{1.98644586\times10^{-25}}{1.634\times10^{-18}}
= 1.216\times10^{-7}\ \text{m}.
$$

The hydrogen transition is at $121.6\ \text{nm}$, about 110 times shorter in
wavelength than the box transition, because the Coulomb attraction is far stronger
than the confinement of a $1\ \text{nm}$ box.

**Answer.** $E_1 = 6.02\times10^{-20}\ \text{J} = 0.376\ \text{eV}$;
$\Delta E = 1.81\times10^{-19}\ \text{J} = 1.13\ \text{eV}$;
$\lambda = 1.10\ \mu\text{m}$ for the box and $121.6\ \text{nm}$ for hydrogen.

**Check.** A $1\ \text{nm}$ box gives an infrared transition, and the $n^{-2}$ scaling
means a $0.1\ \text{nm}$ box would give about $100$ times the energy, in the vacuum
ultraviolet.

**Where marks are lost.** Using $h$ instead of $\hbar$ in $E = \hbar^2k^2/2m$ and
omitting the factor $\pi^2$, or reporting $\Delta E = E_1$.

### 25. Force constant and zero-point energy of HCl

**Strategy.** Compute the reduced mass, then $k = \mu\omega^2$ with
$\omega = 2\pi c\tilde\nu$, and $E_0 = \tfrac{1}{2}hc\tilde\nu$ per molecule.

**Working.** **Multi-step.**

$$
\mu = \frac{m_{\text{H}}m_{\text{Cl}}}{m_{\text{H}}+m_{\text{Cl}}}
= \frac{(1.0078)(34.9689)}{35.9767}\ \text{u}
= 0.97957\ \text{u} = 1.6266\times10^{-27}\ \text{kg}.
$$

The angular frequency is

$$
\omega = 2\pi c\tilde\nu
= 2\pi(2.99792458\times10^{8})(2886\times10^{2})
= 5.4364\times10^{14}\ \text{rad s}^{-1},
$$

so

$$
k = \mu\omega^2 = (1.6266\times10^{-27})(5.4364\times10^{14})^2
= 480.7\ \text{N m}^{-1}.
$$

The zero-point energy per mole is

$$
E_0 = \tfrac{1}{2}hc\tilde\nu N_{\text{A}}
= \tfrac{1}{2}(1.98644586\times10^{-23})(2886)(6.02214076\times10^{23})
= 17.26\ \text{kJ mol}^{-1}.
$$

**Answer.** $\mu = 1.63\times10^{-27}\ \text{kg}$,
$k = 481\ \text{N m}^{-1}$,
$E_0 = 17.3\ \text{kJ mol}^{-1}$.

**Check.** The HCl force constant is close to $480\ \text{N m}^{-1}$, the accepted
value; the zero-point energy is about $2\ \%$ of a typical bond enthalpy, as expected
for a light hydride.

**Where marks are lost.** Using the total mass instead of the reduced mass, or
forgetting the factor $2\pi$ in $\omega$.

### 26. Rotational constant and bond length of CO

**Strategy.** The line spacing is $2B$; invert $B = h/(8\pi^2cI)$ for $I$, then use
$I = \mu r^2$.

**Working.** **Multi-step.** For a rigid rotor, successive lines are separated by
$2B$, so

$$
B = \frac{3.862}{2} = 1.931\ \text{cm}^{-1} = 193.1\ \text{m}^{-1}.
$$

Then

$$
I = \frac{h}{8\pi^2cB}
= \frac{6.62607015\times10^{-34}}
{8\pi^2(2.99792458\times10^{8})(193.1)}
= 1.4497\times10^{-46}\ \text{kg m}^2 .
$$

The reduced mass is

$$
\mu = \frac{(12.000)(15.9949)}{27.9949}\ \text{u}
= 6.8562\ \text{u} = 1.1385\times10^{-26}\ \text{kg},
$$

so

$$
r = \sqrt{\frac{I}{\mu}}
= \sqrt{\frac{1.4497\times10^{-46}}{1.1385\times10^{-26}}}
= 1.1284\times10^{-10}\ \text{m}.
$$

**Answer.** $B = 1.931\ \text{cm}^{-1} = 1.931\times10^{2}\ \text{m}^{-1}$,
$I = 1.45\times10^{-46}\ \text{kg m}^2$, $r = 112.8\ \text{pm}$.

**Check.** The accepted CO bond length is $112.8\ \text{pm}$, and the line spacing of
$3.86\ \text{cm}^{-1}$ corresponds to a rotational temperature of $2.78\ \text{K}$,
consistent with a microwave spectrum.

**Where marks are lost.** Using the line spacing as $B$ rather than $2B$, or failing
to convert $B$ from cm⁻¹ to m⁻¹ before using SI values.

---

## Part D — Intermediate problems

### 27. Entropy and enthalpy from a Maxwell relation

**Strategy.** Replace the unmeasurable $(\partial S/\partial p)_T$ by $-V\alpha$,
integrate at constant $T$, then obtain $\Delta H$ from its pressure derivative.

**Working.** **Multi-step.** With $(\partial S/\partial p)_T = -V\alpha$ and constant
$V$ and $\alpha$,

$$
\Delta S = -V\alpha\Delta p
= -(1.00\times10^{-3})(2.0\times10^{-4})(9.0\times10^{5})
= -0.180\ \text{J K}^{-1}.
$$

The reversible heat is $q_{\text{rev}} = T\Delta S = (298.15)(-0.180)
= -53.7\ \text{J}$; heat is released. For the enthalpy,

$$
\left(\frac{\partial H}{\partial p}\right)_T
= V - T\left(\frac{\partial V}{\partial T}\right)_p
= V(1-\alpha T),
$$

so

$$
\Delta H = V(1-\alpha T)\Delta p
= (1.00\times10^{-3})(1 - 2.0\times10^{-4}\times298.15)(9.0\times10^{5})
= 846\ \text{J}.
$$

**Answer.** $\Delta S = -0.180\ \text{J K}^{-1}$,
$q_{\text{rev}} = -53.7\ \text{J}$, $\Delta H = +846\ \text{J}$.

**Check.** Compression at constant $T$ orders the phase and lowers $S$; the enthalpy
rises because $V(1-\alpha T) > 0$, and the mechanical term $V\Delta p = 900\ \text{J}$
dominates the small thermal correction $-\alpha T V\Delta p = -53.7\ \text{J}$.

**Where marks are lost.** Integrating $(\partial S/\partial V)_T$ over pressure, or
using $\Delta H = \Delta U + \Delta(pV)$ with $pV$ from the ideal-gas law for a
condensed phase.

### 28. Henry's law activity and chemical potential

**Strategy.** Convert pressure to mole fraction with Henry's law, then use
$\mu = \mu^\circ + RT\ln a$ with $a = x$ on the Henry's law scale.

**Working.** **Multi-step.** (a)
$x = p/K_{\text{H}} = 1.00/1.67\times10^{3} = 5.988\times10^{-4}$.

(b) With the Henry's law standard state, $a = x$, so

$$
\mu - \mu^\circ = RT\ln x
= (8.314462618)(298.15)\ln(5.988\times10^{-4})
= (2478.8)(-7.4206)
= -1.8395\times10^{4}\ \text{J mol}^{-1}.
$$

(c) At $p = 0.100\ \text{bar}$, $x = 5.988\times10^{-5}$ and
$\mu - \mu^\circ = (2478.8)(-9.7233) = -2.4103\times10^{4}\ \text{J mol}^{-1}$.
The difference is

$$
(-1.8395) - (-2.4103) = 0.5708\ \text{kJ mol}^{-1}
= RT\ln 10 = (2.4788)(2.302585).
$$

**Answer.** $x = 5.99\times10^{-4}$; $\mu-\mu^\circ = -18.4\ \text{kJ mol}^{-1}$ at
$1.00\ \text{bar}$ and $-24.1\ \text{kJ mol}^{-1}$ at $0.100\ \text{bar}$; the
difference is $5.71\ \text{kJ mol}^{-1}$.

**Check.** A tenfold drop in pressure lowers the chemical potential by $RT\ln 10$,
the same factor by which an ideal-gas chemical potential falls.

**Where marks are lost.** Using the pure-liquid standard state for a dissolved gas,
or inserting $p$ in bar into $RT\ln p$ without a standard pressure.

### 29. Melting point of ice under pressure

**Strategy.** Use the Clapeyron equation with the volume change on melting calculated
from the densities.

**Working.** **Multi-step.** The molar volume change is

$$
\Delta_{\text{fus}}V = M\left(\frac{1}{\rho_{\text{liq}}}-\frac{1}{\rho_{\text{solid}}}\right)
= 18.015\left(\frac{1}{0.9998}-\frac{1}{0.9168}\right)\ \text{cm}^3\ \text{mol}^{-1}
= -1.6313\ \text{cm}^3\ \text{mol}^{-1}.
$$

That is $-1.6313\times10^{-6}\ \text{m}^3\ \text{mol}^{-1}$. Then

$$
\frac{\mathrm{d}T}{\mathrm{d}p} = \frac{T\Delta_{\text{fus}}V}{\Delta_{\text{fus}}H}
= \frac{(273.15)(-1.6313\times10^{-6})}{6008}
= -7.416\times10^{-8}\ \text{K Pa}^{-1}.
$$

For an increase from $1.00$ to $100\ \text{bar}$, $\Delta p = 9.9\times10^{6}\ \text{Pa}$,
so

$$
\Delta T = (-7.416\times10^{-8})(9.9\times10^{6}) = -0.734\ \text{K}.
$$

**Answer.** The melting point falls by $0.734\ \text{K}$, to $272.42\ \text{K}$.

**Check.** Ice is less dense than liquid water, so $\Delta V < 0$ and pressure lowers
the melting point; this is the thermodynamic basis of pressure melting and of
regulation.

**Where marks are lost.** Reversing the density difference and predicting a rise in
melting point, or using $\Delta H$ in J with $\Delta V$ in cm³.

### 30. Sackur–Tetrode entropy of argon

**Strategy.** Evaluate $q_{\text{trans}}$ at the standard molar volume and insert it
into $S = R[\ln(q/N_{\text{A}}) + 5/2]$.

**Working.** **Multi-step.** At $1\ \text{bar}$ and $298.15\ \text{K}$,

$$
V_{\text{m}} = \frac{RT}{p}
= \frac{(8.314462618)(298.15)}{1.00\times10^{5}}
= 2.4789\times10^{-2}\ \text{m}^3\ \text{mol}^{-1}.
$$

From item 22, $\Lambda = 1.59969\times10^{-11}\ \text{m}$, so

$$
\frac{q_{\text{trans}}}{N_{\text{A}}}
= \frac{V_{\text{m}}}{N_{\text{A}}\Lambda^3}
= \frac{2.4789\times10^{-2}}
{(6.02214076\times10^{23})(4.0962\times10^{-33})}
= 1.0050\times10^{7}.
$$

Therefore

$$
S^\circ_{\text{m}} = R\left[\ln(1.0050\times10^{7}) + \frac{5}{2}\right]
= 8.314462618\,(16.1233 + 2.5000)
= 154.85\ \text{J K}^{-1}\ \text{mol}^{-1}.
$$

**Answer.** $S^\circ_{\text{m}} = 154.8\ \text{J K}^{-1}\ \text{mol}^{-1}$, in
agreement with the calorimetric value of $154.84$ to within
$0.01\ \text{J K}^{-1}\ \text{mol}^{-1}$.

**Check.** The agreement confirms that argon is a monatomic gas with no rotational,
vibrational or electronic contribution at $298\ \text{K}$, and that the third-law
entropy has no residual term.

**Where marks are lost.** Using $q$ rather than $q/N_{\text{A}}$ in the logarithm,
which adds $R\ln N_{\text{A}} \approx 110\ \text{J K}^{-1}\ \text{mol}^{-1}$.

### 31. Two-state linear variational calculation

**Strategy.** Write the secular determinant with overlap, expand it as a quadratic,
and solve.

**Working.** **Multi-step.** (a) The secular equations are
$\sum_k(H_{ik} - ES_{ik})c_k = 0$, so

$$
\begin{vmatrix}
H_{11}-E & H_{12}-ES_{12}\\
H_{12}-ES_{12} & H_{22}-E
\end{vmatrix} = 0 .
$$

(b) Expanding,

$$
(1-S_{12}^2)E^2 + \left[-(H_{11}+H_{22}) + 2H_{12}S_{12}\right]E
+ (H_{11}H_{22} - H_{12}^2) = 0 .
$$

With $H_{11} = -10.0$, $H_{22} = -8.0$, $H_{12} = -2.5\ \text{eV}$ and
$S_{12} = 0.200$:

$$
0.960E^2 + 17.0E + 73.75 = 0,
\qquad
E = \frac{-17.0 \pm \sqrt{289.0 - 283.2}}{1.920}
= \frac{-17.0 \pm 2.4083}{1.920}.
$$

The roots are $E_- = -10.108\ \text{eV}$ and $E_+ = -7.600\ \text{eV}$.

(c) For the lower root,
$(H_{11}-E)c_1 + (H_{12}-ES_{12})c_2 = 0$, so

$$
\frac{c_1}{c_2} = -\frac{H_{12}-ES_{12}}{H_{11}-E}
= -\frac{-2.5 - (-10.108)(0.200)}{-10.0 + 10.108}
= 4.408 .
$$

Normalising, $c_2 = (1 + 4.408^2)^{-1/2} = 0.2213$ and $c_1 = 0.9753$, so
$\psi_- = 0.975\chi_1 + 0.221\chi_2$. For the upper root the ratio is
$c_1/c_2 = -0.4083$, giving $c_2 = 0.9258$, $c_1 = -0.3780$ and
$\psi_+ = -0.378\chi_1 + 0.926\chi_2$.

(d) The lower root lies below both diagonal elements and the upper root above both.
The repulsion of the two levels is the non-crossing behaviour produced by the
off-diagonal coupling: the lower state is stabilised by mixing in the higher
function, and the upper state is destabilised by the same mixing.

**Answer.** $E_- = -10.11\ \text{eV}$,
$\psi_- = 0.975\chi_1 + 0.221\chi_2$;
$E_+ = -7.600\ \text{eV}$, $\psi_+ = -0.378\chi_1 + 0.926\chi_2$.

**Check.** The roots straddle the diagonal elements, the coefficients are normalised,
and the lower state is dominated by $\chi_1$ as expected since $H_{11}$ is lower.

**Where marks are lost.** Omitting $S_{12}$ from the off-diagonal element, which
moves the roots by about $0.1\ \text{eV}$, or normalising $c_1^2 + c_2^2$ without
checking the sign of the mixing.

### 32. Two-level system: exact versus perturbation theory

**Strategy.** Diagonalise the $2\times2$ matrix exactly, then apply the standard
first- and second-order formulae.

**Working.** **Multi-step.** (a) The Hamiltonian is

$$
H = \begin{pmatrix} 0 & 2.0\\ 2.0 & 10.0\end{pmatrix}\ \text{eV}.
$$

Its eigenvalues are

$$
E_\pm = \frac{\varepsilon}{2} \pm \sqrt{\left(\frac{\varepsilon}{2}\right)^2 + V^2}
= 5.00 \pm \sqrt{25.0 + 4.00}
= 5.00 \pm 5.3852,
$$

so $E_- = -0.3852\ \text{eV}$ and $E_+ = 10.3852\ \text{eV}$.

(b) The first-order corrections vanish because $V_{11} = V_{22} = 0$. The
second-order corrections are

$$
E_1^{(2)} = \frac{|V_{12}|^2}{E_1^{(0)}-E_2^{(0)}} = \frac{4.00}{-10.0} = -0.400\ \text{eV},
\qquad
E_2^{(2)} = \frac{4.00}{10.0} = +0.400\ \text{eV}.
$$

Hence $E_1 \approx -0.400\ \text{eV}$ and $E_2 \approx 10.400\ \text{eV}$.

(c) The perturbative values differ from the exact ones by $0.0148\ \text{eV}$, or
$3.8\ \%$ for the lower level and $0.14\ \%$ for the upper. The exact lower level lies
above the second-order value because the neglected fourth-order term is positive; the
expansion parameter is $V/\Delta E = 0.20$, so the series converges quickly.

**Answer.** Exact: $-0.385$ and $10.385\ \text{eV}$; second order: $-0.400$ and
$10.400\ \text{eV}$.

**Check.** The exact splitting is
$\sqrt{\Delta^2 + 4V^2} = \sqrt{100 + 16} = 10.770\ \text{eV}$, against $10.800\ \text{eV}$
from second-order theory, consistent with the small error.

**Where marks are lost.** Applying the first-order formula to the diagonal elements
and concluding that the energies are unchanged, or using $V$ rather than $V^2$ in the
second-order expression.

### 33. Morse analysis of the CO vibration

**Strategy.** Use the fundamental and first overtone to solve for $\omega_e$ and
$\omega_e x_e$, then the Morse relations for $D_e$ and $D_0$.

**Working.** **Multi-step.** With
$G(v) = \omega_e(v+\tfrac{1}{2}) - \omega_e x_e(v+\tfrac{1}{2})^2$,

$$
\tilde\nu_{0\to1} = \omega_e - 2\omega_e x_e = 2143\ \text{cm}^{-1},
\qquad
\tilde\nu_{0\to2} = 2\omega_e - 6\omega_e x_e = 4260\ \text{cm}^{-1}.
$$

Dividing the second by 2 gives $\omega_e - 3\omega_e x_e = 2130\ \text{cm}^{-1}$.
Subtracting the first equation, $\omega_e x_e = 13.0\ \text{cm}^{-1}$ and
$\omega_e = 2169\ \text{cm}^{-1}$.

The well depth is

$$
D_e = \frac{\omega_e^2}{4\omega_e x_e}
= \frac{(2169)^2}{4(13.0)} = 9.047\times10^{4}\ \text{cm}^{-1}.
$$

Using $hcN_{\text{A}} = 0.0119627\ \text{kJ mol}^{-1}$ per cm⁻¹,
$D_e = 1082\ \text{kJ mol}^{-1}$. The zero-point energy is

$$
G(0) = \frac{\omega_e}{2} - \frac{\omega_e x_e}{4}
= 1084.5 - 3.25 = 1081.3\ \text{cm}^{-1},
$$

so $D_0 = D_e - G(0) = 89\,391\ \text{cm}^{-1} = 1069\ \text{kJ mol}^{-1}$.

**Answer.** $\omega_e = 2169\ \text{cm}^{-1}$,
$\omega_e x_e = 13.0\ \text{cm}^{-1}$,
$D_e = 9.05\times10^{4}\ \text{cm}^{-1} = 1082\ \text{kJ mol}^{-1}$,
$D_0 = 8.94\times10^{4}\ \text{cm}^{-1} = 1069\ \text{kJ mol}^{-1}$.

**Check.** The accepted CO dissociation energy is about
$1072\ \text{kJ mol}^{-1}$; the difference reflects the neglect of higher anharmonic
terms, and $D_0 < D_e$ as required.

**Where marks are lost.** Using $\tilde\nu_{0\to2} = 2\omega_e(1-2x_e)$, which
confuses the overtone with twice the fundamental, or quoting $D_e$ as the
dissociation energy at $0\ \text{K}$.

### 34. Beer–Lambert law and dilution

**Strategy.** Invert $A = \varepsilon c l$ for $c$, convert absorbance to
transmittance, then use $c_1V_1 = c_2V_2$.

**Working.** **Multi-step.** (a)

$$
c = \frac{A}{\varepsilon l}
= \frac{0.842}{(1.42\times10^{4})(1.00)}
= 5.930\times10^{-5}\ \text{mol dm}^{-3}.
$$

(b) $A = -\log_{10}T$, so
$T = 10^{-0.842} = 0.1439$, or $14.4\ \%$.

(c) For dilution, $c_1V_1 = c_2V_2$ with $c_2 = 2.00\times10^{-5}\ \text{mol dm}^{-3}$
and $V_2 = 100.0\ \text{cm}^3$:

$$
V_1 = \frac{(2.00\times10^{-5})(100.0)}{5.930\times10^{-5}} = 33.7\ \text{cm}^3 .
$$

**Answer.** $c = 5.93\times10^{-5}\ \text{mol dm}^{-3}$; $T = 14.4\ \%$;
$V_1 = 33.7\ \text{cm}^3$.

**Check.** The diluted solution is about one third as concentrated, so one third of
the volume of stock is needed, consistent with $33.7/100$.

**Where marks are lost.** Using $\ln$ instead of $\log_{10}$ for the absorbance, or
using $A = \varepsilon c/l$.

### 35. Michaelis–Menten kinetics

**Strategy.** Derive the rate law from the steady state on $\ce{ES}$, then solve the
two data points for $K_{\text{M}}$ and $V_{\text{max}}$.

**Working.** **Multi-step.** (a) For

$$
\ce{E + S <=>[k_1][k_{-1}] ES ->[k_2] E + P}
$$

the steady-state condition is

$$
\frac{\mathrm{d}[\ce{ES}]}{\mathrm{d}t}
= k_1[\ce{E}][\ce{S}] - k_{-1}[\ce{ES}] - k_2[\ce{ES}] \approx 0,
$$

so $[\ce{ES}] = k_1[\ce{E}][\ce{S}]/(k_{-1}+k_2)$. With
$[\ce{E}]_0 = [\ce{E}] + [\ce{ES}]$,

$$
[\ce{ES}] = \frac{[\ce{E}]_0[\ce{S}]}{K_{\text{M}}+[\ce{S}]},
\qquad
K_{\text{M}} = \frac{k_{-1}+k_2}{k_1},
\qquad
v = \frac{k_2[\ce{E}]_0[\ce{S}]}{K_{\text{M}}+[\ce{S}]}
= \frac{V_{\text{max}}[\ce{S}]}{K_{\text{M}}+[\ce{S}]}.
$$

(b) Dividing the two rate equations eliminates $V_{\text{max}}$:

$$
\frac{v_2}{v_1} = \frac{[\ce{S}]_2(K_{\text{M}}+[\ce{S}]_1)}
{[\ce{S}]_1(K_{\text{M}}+[\ce{S}]_2)}
\Longrightarrow
1.667 = \frac{8.00\times10^{-4}(K_{\text{M}}+2.00\times10^{-4})}
{2.00\times10^{-4}(K_{\text{M}}+8.00\times10^{-4})}.
$$

Solving, $1.667(K_{\text{M}} + 8.00\times10^{-4})
= 4.00(K_{\text{M}} + 2.00\times10^{-4})$, so
$2.333K_{\text{M}} = 5.333\times10^{-4}$ and
$K_{\text{M}} = 2.286\times10^{-4}\ \text{mol dm}^{-3}$. Then

$$
V_{\text{max}} = \frac{v_1(K_{\text{M}}+[\ce{S}]_1)}{[\ce{S}]_1}
= \frac{(1.20)(4.286\times10^{-4})}{2.00\times10^{-4}}
= 2.571\ \mu\text{mol dm}^{-3}\ \text{s}^{-1}.
$$

(c) $k_{\text{cat}} = V_{\text{max}}/[\ce{E}]_0
= 2.571\times10^{-6}/2.00\times10^{-9} = 1.29\times10^{3}\ \text{s}^{-1}$.

(d) When $k_2 \ll k_{-1}$, $K_{\text{M}} = (k_{-1}+k_2)/k_1 \to k_{-1}/k_1$,
the dissociation constant of the enzyme–substrate complex. The binding step is then a
rapid pre-equilibrium, and the rate law becomes
$v = k_2[\ce{E}]_0[\ce{S}]/(K_{\text{S}}+[\ce{S}])$, with $K_{\text{S}} = k_{-1}/k_1$.
The steady-state law therefore contains the pre-equilibrium law as the fast-binding
limit.

**Answer.** $K_{\text{M}} = 2.29\times10^{-4}\ \text{mol dm}^{-3}$,
$V_{\text{max}} = 2.57\ \mu\text{mol dm}^{-3}\ \text{s}^{-1}$,
$k_{\text{cat}} = 1.29\times10^{3}\ \text{s}^{-1}$.

**Check.** At $[\ce{S}] = K_{\text{M}}$, $v = V_{\text{max}}/2 = 1.29$, which lies
between the two measured rates as expected; the computed $K_{\text{M}}$ is below both
substrate concentrations, so both points are on the approaching-saturation part of the
curve.

**Where marks are lost.** Using $v = V_{\text{max}}[\ce{S}]/K_{\text{M}}$ (the
low-substrate limit) for both points, or defining $K_{\text{M}} = k_{-1}/k_1$ and
omitting $k_2$.

### 36. Activation parameters from transition-state theory

**Strategy.** Invert the Eyring equation for $\Delta G^\ddagger$, then split it into
enthalpy and entropy and extrapolate to the second temperature.

**Working.** **Multi-step.** At $298.15\ \text{K}$,

$$
\frac{k_{\text{B}}T}{h}
= \frac{(1.380649\times10^{-23})(298.15)}{6.62607015\times10^{-34}}
= 6.2124\times10^{12}\ \text{s}^{-1}.
$$

From $k = (k_{\text{B}}T/h)e^{-\Delta G^\ddagger/RT}$,

$$
\Delta G^\ddagger = RT\ln\frac{k_{\text{B}}T}{hk}
= (8.314462618)(298.15)\ln\frac{6.2124\times10^{12}}{1.00\times10^{-3}}
= 90.148\ \text{kJ mol}^{-1}.
$$

With $\Delta G^\ddagger = \Delta H^\ddagger - T\Delta S^\ddagger$,

$$
\Delta S^\ddagger = \frac{\Delta H^\ddagger - \Delta G^\ddagger}{T}
= \frac{80.0 - 90.148}{298.15}\times10^{3}
= -34.04\ \text{J K}^{-1}\ \text{mol}^{-1}.
$$

At $308.15\ \text{K}$, $k_{\text{B}}T/h = 6.4208\times10^{12}\ \text{s}^{-1}$, so

$$
k = (6.4208\times10^{12})\exp\left(\frac{-80\,000}{(8.314462618)(308.15)}\right)
\exp\left(\frac{-34.04}{8.314462618}\right)
= 2.95\times10^{-3}\ \text{s}^{-1}.
$$

**Answer.** $\Delta G^\ddagger = 90.1\ \text{kJ mol}^{-1}$;
$\Delta S^\ddagger = -34.0\ \text{J K}^{-1}\ \text{mol}^{-1}$;
$k(308.15\ \text{K}) = 2.95\times10^{-3}\ \text{s}^{-1}$.

**Check.** The rate rises by a factor of $2.95$ over $10\ \text{K}$. The Arrhenius
expression with $E_{\text{a}} = \Delta H^\ddagger + RT = 82.5\ \text{kJ mol}^{-1}$
gives $\exp[(82\,500/R)(1/298.15 - 1/308.15)] = 2.94$, consistent.

**Where marks are lost.** Using $\Delta G^\ddagger$ in place of $\Delta H^\ddagger$ in
the extrapolation, or forgetting that $k_{\text{B}}T/h$ itself depends on $T$.

## Part E — Advanced problems

### 37. Thermodynamic consistency at high pressure

**Strategy.** Integrate the Maxwell relation with the exponential volume, then compare
with the linear approximation.

**Working.** **Multi-step.** With
$V(p) = V_0\exp[-\kappa_T(p-p_0)]$ and constant $\alpha$,

$$
\Delta S = -\int_{p_0}^{p_1}\alpha V\,\mathrm{d}p
= -\frac{\alpha V_0}{\kappa_T}
\left(1 - e^{-\kappa_T\Delta p}\right),
$$

$$
\Delta H = \int_{p_0}^{p_1}V(1-\alpha T)\,\mathrm{d}p
= \frac{(1-\alpha T)V_0}{\kappa_T}
\left(1 - e^{-\kappa_T\Delta p}\right).
$$

Here $\kappa_T\Delta p = (5.00\times10^{-5})(99) = 4.95\times10^{-3}$ and
$1 - e^{-4.95\times10^{-3}} = 4.9378\times10^{-3}$. Therefore

$$
\Delta S = -\frac{(2.00\times10^{-4})(1.00\times10^{-3})}{5.00\times10^{-10}\ \text{Pa}^{-1}}
(4.9378\times10^{-3})
$$

with $\kappa_T = 5.00\times10^{-10}\ \text{Pa}^{-1}$, giving
$\Delta S = -1.975\ \text{J K}^{-1}$. For the enthalpy,
$1-\alpha T = 1 - 0.05963 = 0.94037$, so

$$
\Delta H = \frac{(0.94037)(1.00\times10^{-3})}{5.00\times10^{-10}}
(4.9378\times10^{-3}) = 9.287\times10^{3}\ \text{J}.
$$

The linear approximations are $\Delta S \approx -\alpha V_0\Delta p = -1.980\ \text{J K}^{-1}$
and $\Delta H \approx (1-\alpha T)V_0\Delta p = 9.310\ \text{kJ}$; the exact values
differ by $0.25\ \%$.

**Answer.** $\Delta S = -1.98\ \text{J K}^{-1}$,
$\Delta H = +9.29\ \text{kJ}$; the linear approximation is in error by
$0.25\ \%$.

**Check.** Both signs are physically sensible: compression reduces the entropy and
increases the enthalpy. The correction is small because $\kappa_T\Delta p \ll 1$, which
is the condition for the linear approximation to be valid.

**Where marks are lost.** Using $\kappa_T$ in bar⁻¹ without converting to Pa⁻¹, which
changes the exponent by $10^{5}$.

### 38. Phase rule and the lever rule

**Strategy.** Count phases and components for $F$, then apply the lever rule with the
phase compositions.

**Working.** **Multi-step.** (a) There are two components, A and B, and two phases,
liquid and solid. At fixed pressure,

$$
F = C - P + 1 = 2 - 2 + 1 = 1 .
$$

One intensive variable, for example temperature or the liquid composition, fixes the
rest.

(b) The lever rule on the B mole fraction gives

$$
f_{\text{liq}} = \frac{x_{\text{solid}} - x_{\text{overall}}}
{x_{\text{solid}} - x_{\text{liq}}}
= \frac{0.70 - 0.40}{0.70 - 0.25} = 0.667,
$$

so $f_{\text{solid}} = 1 - 0.667 = 0.333$.

(c) As $x_{\text{overall}} \to 0.70$, $f_{\text{liq}} \to 0$ and $f_{\text{solid}} \to 1$;
the last liquid disappears when the overall composition equals the solid composition.

**Answer.** $F = 1$; $66.7\ \%$ liquid and $33.3\ \%$ solid; the liquid fraction tends
to zero as the overall composition approaches $70\ \text{mol}\ \%$ B.

**Check.** The fractions sum to one, and the lever arms are inversely proportional to
the distances from the overall composition to each phase, as required.

**Where marks are lost.** Using $F = C - P + 2$ at fixed pressure, or inverting the
lever-rule arms and assigning the larger fraction to the phase farther from the
overall composition.

### 39. Fermi energy and Fermi–Dirac occupation in sodium

**Strategy.** Compute the electron density from the mass density, evaluate
$E_{\text{F}} = (\hbar^2/2m)(3\pi^2n)^{2/3}$, then use the Fermi–Dirac function.

**Working.** **Multi-step.** (a) With one conduction electron per atom,

$$
n = \frac{\rho N_{\text{A}}}{M}
= \frac{(0.968\times10^{3})(6.02214076\times10^{23})}{22.99\times10^{-3}}
= 2.536\times10^{28}\ \text{m}^{-3}.
$$

(b)

$$
E_{\text{F}} = \frac{\hbar^2}{2m_{\text{e}}}\left(3\pi^2n\right)^{2/3}
= \frac{(1.054571817\times10^{-34})^2}{2(9.1093837015\times10^{-31})}
\left(3\pi^2\times2.536\times10^{28}\right)^{2/3}
= 5.042\times10^{-19}\ \text{J}.
$$

In electronvolts, $E_{\text{F}} = 5.042\times10^{-19}/1.602176634\times10^{-19}
= 3.147\ \text{eV}$.

(c) The occupation is
$f = [e^{(\varepsilon-\mu)/k_{\text{B}}T}+1]^{-1}$ with
$\varepsilon-\mu = 0.10\ \text{eV} = 1.6022\times10^{-20}\ \text{J}$. At
$300\ \text{K}$, $k_{\text{B}}T = 4.14195\times10^{-21}\ \text{J}$ and the exponent is
$3.868$, so $f = 1/(47.85+1) = 0.0205$. At $1000\ \text{K}$ the exponent is
$1.1605$ and $f = 1/(3.191+1) = 0.239$.

(d) The occupation depends on $(\varepsilon-\mu)/k_{\text{B}}T$. Raising $T$ from
$300$ to $1000\ \text{K}$ reduces the exponent by a factor $3.33$, which changes
$f$ by more than an order of magnitude. The chemical potential $\mu$ itself shifts
only by terms of order $(kT/E_{\text{F}})^2$, which is $7\times10^{-5}$ at
$300\ \text{K}$ and $8\times10^{-4}$ at $1000\ \text{K}$, so $E_{\text{F}}$ is
essentially temperature-independent.

**Answer.** $n = 2.54\times10^{28}\ \text{m}^{-3}$;
$E_{\text{F}} = 5.04\times10^{-19}\ \text{J} = 3.15\ \text{eV}$;
$f = 0.0205$ at $300\ \text{K}$ and $0.239$ at $1000\ \text{K}$.

**Check.** The Fermi temperature is $E_{\text{F}}/k_{\text{B}} = 3.65\times10^{4}\ \text{K}$,
so at ordinary temperatures the electron gas is strongly degenerate and only states
within about $kT$ of $E_{\text{F}}$ can respond.

**Where marks are lost.** Omitting $N_{\text{A}}$ when converting molar density to
number density, or using the classical Boltzmann factor for the occupation, which gives
$e^{-3.87} = 0.021$ by coincidence at $300\ \text{K}$ but fails badly at low $T$.

### 40. Equilibrium constant for $\ce{H2 + D2 <=> 2HD}$

**Strategy.** Write $K$ as a product of translational, rotational and symmetry factors
times the zero-point exponential, then evaluate each factor.

**Working.** **Multi-step.** (a) For

$$
\ce{H2(g) + D2(g) <=> 2HD(g)}
$$

with $q_i$ the molecular partition function referred to the same standard volume,

$$
K = \frac{(q_{\ce{HD}}/V)^2}{(q_{\ce{H2}}/V)(q_{\ce{D2}}/V)}
e^{-\Delta E_0/k_{\text{B}}T}
= \frac{q_{\ce{HD}}^2}{q_{\ce{H2}}q_{\ce{D2}}}
e^{-\Delta E_0/k_{\text{B}}T}.
$$

Each $q = q_{\text{trans}}q_{\text{rot}}q_{\text{vib}}q_{\text{el}}$, with
$q_{\text{vib}} \approx 1$ because all three wavenumbers exceed
$3000\ \text{cm}^{-1}$ ($\theta_{\text{vib}} > 4300\ \text{K}$) and $q_{\text{el}} = 1$.

(b) Translation: $q_{\text{trans}} \propto m^{3/2}$, so

$$
\left(\frac{m_{\ce{HD}}^2}{m_{\ce{H2}}m_{\ce{D2}}}\right)^{3/2}
= \left(\frac{3.022^2}{(2.016)(4.028)}\right)^{3/2}
= (1.1246)^{3/2} = 1.193 .
$$

Rotation: $q_{\text{rot}} \propto I/\sigma$, and $I = \mu r^2$ with equal $r$, so

$$
\frac{\mu_{\ce{HD}}^2}{\mu_{\ce{H2}}\mu_{\ce{D2}}}
= \frac{(0.6717)^2}{(0.5040)(1.0070)} = 0.8891,
$$

and the symmetry numbers $(\sigma_{\ce{H2}},\sigma_{\ce{D2}},\sigma_{\ce{HD}}) = (2,2,1)$
give a factor $(1)^2/[(1/2)(1/2)] = 4$. The pre-exponential factor is therefore

$$
1.193\times0.8891\times4 = 4.242 .
$$

(c) The zero-point energy change is

$$
\Delta E_0 = \tfrac{1}{2}hc\left(2\tilde\nu_{\ce{HD}}
- \tilde\nu_{\ce{H2}} - \tilde\nu_{\ce{D2}}\right)
= \tfrac{1}{2}hc(2\times3817 - 4401 - 3116)
= 58.5\ \text{cm}^{-1},
$$

or $0.6998\ \text{kJ mol}^{-1}$. Hence

$$
K(298.15) = 4.242\exp\left(-\frac{699.8}{(8.314462618)(298.15)}\right)
= 4.242\,e^{-0.2823} = 3.20,
$$

$$
K(500.0) = 4.242\exp\left(-\frac{699.8}{(8.314462618)(500.0)}\right)
= 4.242\,e^{-0.1683} = 3.59 .
$$

(d) $K > 1$ because the symmetry factor of 4 favours the two heteronuclear molecules,
and this outweighs the zero-point penalty of $0.70\ \text{kJ mol}^{-1}$. At high $T$
the exponential tends to one and $K$ tends to the temperature-independent factor
$4.24$, not exactly 4, because the masses and moments of inertia differ.

**Answer.** $K(298.15) = 3.20$ and $K(500.0) = 3.59$; the high-temperature limit is
$4.24$.

**Check.** The experimental equilibrium constant for this exchange at room temperature
is about 3.2, and the reaction is nearly thermoneutral, so a value of order unity is
expected.

**Where marks are lost.** Omitting the symmetry numbers, which changes $K$ by a factor
of 4, or using the wavenumbers in cm⁻¹ directly as energies in the exponential.

### 41. First-order perturbation theory for helium

**Strategy.** Add the first-order repulsion to the sum of the hydrogenic orbital
energies, compare with the exact value, and explain the direction of the error.

**Working.** **Multi-step.** (a) The zeroth-order energy is the sum of two hydrogenic
$1s$ energies with $Z = 2$:

$$
E^{(0)} = 2\left(-\frac{Z^2}{2}\ \text{hartree}\right)
= 2(-54.4\ \text{eV}) = -108.8\ \text{eV}.
$$

The first-order correction is the electron–electron repulsion,
$E^{(1)} = +34.0\ \text{eV}$, so

$$
E^{(0)} + E^{(1)} = -108.8 + 34.0 = -74.8\ \text{eV}.
$$

(b) The exact non-relativistic energy is $-79.0\ \text{eV}$, so the error is

$$
\frac{79.0 - 74.8}{79.0}\times100\ \% = 5.3\ \%,
$$

and the calculated energy is too high by $4.2\ \text{eV}$.

(c) The first-order result lies above the exact energy because the trial function is
the product of two hydrogenic $1s$ orbitals with the full nuclear charge $Z = 2$. Each
electron screens the other, so the true effective nuclear charge is lower; the
unscreened function is too contracted and the repulsion is overestimated. The
variational theorem guarantees that any normalised trial function gives an energy
above $E_0$, and optimising the exponent $\zeta$ in
$\psi = (\zeta^3/\pi)^{1/2}e^{-\zeta r}$ gives
$\zeta = Z - 5/16 = 1.6875$ and

$$
E = -\left(Z - \frac{5}{16}\right)^2\ \text{hartree} = -77.5\ \text{eV},
$$

which is lower than the first-order value and closer to the exact result.

**Answer.** $E = -74.8\ \text{eV}$; error $5.3\ \%$; the value lies above the exact
$-79.0\ \text{eV}$ because screening is neglected; a variational treatment lowers it
to $-77.5\ \text{eV}$.

**Check.** The residual $2.5\ \text{eV}$ between the optimised variational and exact
energies is largely the correlation energy, which a single Slater determinant cannot
capture.

**Where marks are lost.** Reporting a positive total energy, or claiming the
first-order result is below the exact energy because "perturbation theory always
improves the energy".

### 42. Fluorescence quantum yield, lifetime and quenching

**Strategy.** Split the total decay rate into radiative and non-radiative parts, then
apply the Stern–Volmer relation.

**Working.** **Multi-step.** (a)

$$
k_{\text{F}} = \frac{\phi_{\text{F}}}{\tau_0} = \frac{0.35}{5.0\times10^{-9}}
= 7.0\times10^{7}\ \text{s}^{-1},
$$

and the total decay rate in the absence of quencher is
$1/\tau_0 = 2.0\times10^{8}\ \text{s}^{-1}$, so
$k_{\text{nr}} = 2.0\times10^{8} - 7.0\times10^{7} = 1.3\times10^{8}\ \text{s}^{-1}$.

(b) $K_{\text{SV}} = k_q\tau_0 = (5.0\times10^{9})(5.0\times10^{-9})
= 25.0\ \text{dm}^3\ \text{mol}^{-1}$, and with
$[Q] = 5.0\times10^{-3}\ \text{mol dm}^{-3}$,

$$
\frac{I_0}{I} = 1 + K_{\text{SV}}[Q] = 1 + (25.0)(5.0\times10^{-3}) = 1.125 .
$$

(c) The lifetime in the presence of quencher is

$$
\tau = \frac{1}{1/\tau_0 + k_q[Q]}
= \frac{1}{2.0\times10^{8} + 2.5\times10^{7}}
= 4.44\times10^{-9}\ \text{s},
$$

and $\phi_{\text{F}} = k_{\text{F}}\tau = (7.0\times10^{7})(4.44\times10^{-9}) = 0.311$.

(d) $k_q = 5.0\times10^{9}$ is below the diffusion limit of about
$7\times10^{9}\ \text{dm}^3\ \text{mol}^{-1}\ \text{s}^{-1}$ but within a factor of
1.4 of it. The quenching is therefore at, or close to, the encounter limit, and is
best described as diffusion-controlled.

**Answer.** $k_{\text{F}} = 7.0\times10^{7}\ \text{s}^{-1}$,
$k_{\text{nr}} = 1.3\times10^{8}\ \text{s}^{-1}$,
$K_{\text{SV}} = 25.0\ \text{dm}^3\ \text{mol}^{-1}$, $I_0/I = 1.125$,
$\tau = 4.44\ \text{ns}$, $\phi_{\text{F}} = 0.311$; the quenching is
diffusion-controlled.

**Check.** $I_0/I - 1 = 0.125 = K_{\text{SV}}[Q]$, and the quenching reduces both the
lifetime and the quantum yield by the same factor $1.125$, as required for dynamic
quenching.

**Where marks are lost.** Treating $K_{\text{SV}}$ as dimensionless and omitting the
quencher concentration, or computing $\tau$ from $\tau_0/(1+K_{\text{SV}})$ with
$K_{\text{SV}}$ in the wrong units.

### 43. Diffusion control and activation control

**Strategy.** Use Smoluchowski for the encounter rate, then the series resistance
model for the observed rate.

**Working.** **Multi-step.** (a)

$$
k_{\text{d}} = \frac{8RT}{3\eta}
= \frac{8(8.314462618)(298.15)}{3(8.90\times10^{-4})}
= 7.428\times10^{6}\ \text{m}^3\ \text{mol}^{-1}\ \text{s}^{-1}
= 7.43\times10^{9}\ \text{dm}^3\ \text{mol}^{-1}\ \text{s}^{-1}.
$$

(b) With $k_{\text{obs}} = 1.20\times10^{9}$,

$$
\frac{1}{k_{\text{act}}} = \frac{1}{k_{\text{obs}}} - \frac{1}{k_{\text{d}}}
= 8.333\times10^{-10} - 1.346\times10^{-10}
= 6.987\times10^{-10}\ \text{dm}^{-3}\ \text{mol s},
$$

so $k_{\text{act}} = 1.43\times10^{9}\ \text{dm}^3\ \text{mol}^{-1}\ \text{s}^{-1}$.

(c) The probability that an encounter leads to reaction is

$$
p = \frac{k_{\text{obs}}}{k_{\text{d}}}
= \frac{1.20}{7.43} = 0.162 .
$$

Since $k_{\text{act}} < k_{\text{d}}$, the chemical step is slower than encounter, so
the reaction is activation-controlled, although the two rates are within a factor of
five and the reaction is close to the diffusion limit.

**Answer.** $k_{\text{d}} = 7.43\times10^{9}$,
$k_{\text{act}} = 1.43\times10^{9}\ \text{dm}^3\ \text{mol}^{-1}\ \text{s}^{-1}$;
$p = 0.162$; activation-controlled.

**Check.** $1/1.43\times10^{9} + 1/7.43\times10^{9} = 8.34\times10^{-10}$, whose
reciprocal is $1.20\times10^{9}$, consistent with $k_{\text{obs}}$.

**Where marks are lost.** Adding the rate constants instead of the reciprocals, or
concluding that a rate close to $k_{\text{d}}$ is necessarily diffusion-controlled
without checking which step is slower.

### 44. Collision theory and the steric factor

**Strategy.** Compute the mean relative speed and the hard-sphere collision frequency,
multiply by the Boltzmann factor, then compare with experiment to extract $P$.

**Working.** **Multi-step.** (a) The reduced mass is

$$
\mu = \frac{M_{\text{A}}M_{\text{B}}}{M_{\text{A}}+M_{\text{B}}}\frac{1}{N_{\text{A}}}
= \frac{(30.0)(46.0)}{76.0}\times\frac{10^{-3}}{6.02214076\times10^{23}}
= 3.0152\times10^{-26}\ \text{kg}.
$$

The mean relative speed is

$$
\bar v = \sqrt{\frac{8k_{\text{B}}T}{\pi\mu}}
= \sqrt{\frac{8(1.380649\times10^{-23})(600)}{(\pi)(3.0152\times10^{-26})}}
= 836.4\ \text{m s}^{-1}.
$$

The collision frequency factor is

$$
Z = N_{\text{A}}\pi d^2\bar v
= (6.02214076\times10^{23})(\pi)(3.5\times10^{-10})^2(836.4)
= 1.9385\times10^{8}\ \text{m}^3\ \text{mol}^{-1}\ \text{s}^{-1}.
$$

Multiplying by the Boltzmann factor,

$$
A = Z\,e^{-E_{\text{a}}/RT}
= (1.9385\times10^{8})(6.6619\times10^{-3})
= 1.2914\times10^{6}\ \text{m}^3\ \text{mol}^{-1}\ \text{s}^{-1},
$$

which is $1.2914\times10^{9}\ \text{dm}^3\ \text{mol}^{-1}\ \text{s}^{-1}$.

(b) The experimental pre-exponential factor follows from
$k = A_{\text{exp}}e^{-E_{\text{a}}/RT}$:

$$
A_{\text{exp}} = \frac{2.0\times10^{6}}{e^{-25\,000/(8.314462618\times600)}}
= \frac{2.0\times10^{6}}{6.6619\times10^{-3}}
= 3.00\times10^{8}\ \text{dm}^3\ \text{mol}^{-1}\ \text{s}^{-1}.
$$

Hence

$$
P = \frac{A_{\text{exp}}}{A_{\text{theory}}}
= \frac{3.00\times10^{8}}{1.29\times10^{9}} = 0.232 .
$$

(c) The experimental pre-exponential factor is
$3.00\times10^{8}\ \text{dm}^3\ \text{mol}^{-1}\ \text{s}^{-1}$.

(d) A steric factor of $0.23$ means that only about one collision in four has the
orientation needed to reach the transition state. The transition state is therefore
tight and anisotropic: the two reactants must approach with a specific alignment, and
most collisions are non-reactive even when the energy is sufficient.

**Answer.** $A_{\text{theory}} = 1.29\times10^{9}$,
$A_{\text{exp}} = 3.00\times10^{8}\ \text{dm}^3\ \text{mol}^{-1}\ \text{s}^{-1}$,
$P = 0.232$.

**Check.** $P < 1$ as required; a value of order $0.1$–$1$ is typical for bimolecular
gas reactions, whereas $P \ll 10^{-3}$ would suggest a very demanding orientation or
an incorrect $E_{\text{a}}$.

**Where marks are lost.** Using the molar reduced mass in the Maxwell–Boltzmann
speed, which makes $\bar v$ too large by $\sqrt{N_{\text{A}}}$, or multiplying by
$e^{-E_{\text{a}}/RT}$ twice.

---

## Part F — Multiple-choice self-check

### 45. Ideal-gas derivative

**Answer: A.** For an ideal gas $U$ depends only on $T$, so
$(\partial U/\partial V)_T = 0$. B is $C_V$, which is positive; C is $C_V/T$; D is
$-S$.

**Why B is wrong.** $(\partial U/\partial T)_V = C_V$, which is not zero for any
material.

**Why C is wrong.** $(\partial S/\partial T)_V = C_V/T > 0$.

**Why D is wrong.** $(\partial G/\partial T)_p = -S$, which is negative but not zero.

**Where marks are lost.** Confusing "independent of volume" with "independent of
temperature".

### 46. Fermi–Dirac statistics

**Answer: A.** Electrons are fermions (spin $\tfrac{1}{2}$), so the Pauli principle
gives $n_i \le 1$ and Fermi–Dirac statistics.

**Why B is wrong.** Photons are bosons with chemical potential zero; their
distribution is the Planck or Bose–Einstein form.

**Why C is wrong.** $\ce{^4He}$ is a boson; below the lambda point it shows
Bose–Einstein behaviour, not Fermi–Dirac.

**Why D is wrong.** Argon at $300\ \text{K}$ and $1\ \text{bar}$ has
$n\Lambda^3 \ll 1$ and is described by Maxwell–Boltzmann statistics.

**Where marks are lost.** Choosing the distribution by the mass of the particle
rather than by its spin.

### 47. Consequence of the commutator

**Answer: B.** The Robertson relation for $[\hat x,\hat p_x] = i\hbar$ is
$\sigma_x\sigma_p \ge \hbar/2$, a positive lower bound on the product of the
uncertainties.

**Why A is wrong.** The commutator means that no state has definite values of both
observables, so simultaneous exact measurement is impossible.

**Why C is wrong.** Quantisation of energy follows from boundary conditions or a
confining potential, not from this commutator.

**Why D is wrong.** Conservation of angular momentum follows from rotational symmetry
of the Hamiltonian, not from $[\hat x,\hat p_x]$.

**Where marks are lost.** Reading the inequality as a statement about the clumsiness
of instruments rather than about the state itself.

### 48. Infrared-inactive, Raman-active vibration

**Answer: A.** The symmetric stretch of $\ce{CO2}$ preserves the centre of symmetry
and produces no dipole change, so it is infrared inactive; the polarisability changes,
so it is Raman active.

**Why B is wrong.** The asymmetric stretch produces a dipole change and is infrared
active (and also Raman active in this case).

**Why C is wrong.** The $\ce{H2O}$ bend changes both dipole and polarisability, so it
is active in both.

**Why D is wrong.** The $\ce{HCl}$ stretch changes the dipole and is infrared active.

**Where marks are lost.** Applying the mutual exclusion rule to a molecule without a
centre of symmetry.

### 49. Diffusion-controlled rate constant in water

**Answer: A.** Smoluchowski gives
$k_{\text{d}} = 8RT/3\eta = 8(8.314)(298)/(3\times8.9\times10^{-4})
\approx 7.4\times10^{6}\ \text{m}^3\ \text{mol}^{-1}\ \text{s}^{-1}$, which is
$7.4\times10^{9}\ \text{dm}^3\ \text{mol}^{-1}\ \text{s}^{-1}$.

**Why B is wrong.** $7\times10^{6}$ is the value in $\text{m}^3\ \text{mol}^{-1}\ \text{s}^{-1}$,
not in $\text{dm}^3$.

**Why C is wrong.** $7\times10^{3}$ is three orders of magnitude too small; it would
correspond to a viscosity of about $10^{3}\ \text{Pa s}$.

**Why D is wrong.** $7\times10^{12}$ exceeds the encounter limit for small molecules
in water by three orders of magnitude.

**Where marks are lost.** Failing to convert $\text{m}^3$ to $\text{dm}^3$.

### 50. Phosphorescence

**Answer: B.** Phosphorescence is the spin-forbidden radiative transition
$T_1 \to S_0$; the small spin–orbit coupling makes it slow, with lifetimes from
milliseconds to seconds, and $T_1$ lies below $S_1$, so it is red-shifted.

**Why A is wrong.** $S_1 \to S_0$ on a nanosecond timescale is fluorescence.

**Why C is wrong.** $S_1 \to S_0$ is fluorescence; the red shift belongs to the
triplet emission.

**Why D is wrong.** Phosphorescence is radiative, not non-radiative; internal
conversion is a separate non-radiative channel.

**Where marks are lost.** Describing phosphorescence as "delayed fluorescence"; delayed
fluorescence is emission from $S_1$ repopulated from the triplet, not $T_1 \to S_0$.

---

## Top ten errors in this level

| Rank | Error | Why it costs marks | Correct habit |
|---|---|---|---|
| 1 | Mixing $h$ and $\hbar$ in box and oscillator formulae | Energies wrong by $(2\pi)^2$ or $2\pi$ | Write $E = \hbar^2k^2/2m$ and $k = n\pi/L$ before substituting |
| 2 | Sign of work and heat in expansions | $w$, $q$ and $\Delta S$ all inverted | Use $w = -\int p\,\mathrm{d}V$; expansion means $w < 0$ |
| 3 | Using $\Delta G^\ddagger$ as $\Delta H^\ddagger$ in extrapolations | Rate constant wrong by orders of magnitude | Split $\Delta G^\ddagger = \Delta H^\ddagger - T\Delta S^\ddagger$ first |
| 4 | Omitting $q/N_{\text{A}}$ in the Sackur–Tetrode logarithm | Entropy too high by $R\ln N_{\text{A}} \approx 110\ \text{J K}^{-1}\ \text{mol}^{-1}$ | Use the molar volume and divide by $N_{\text{A}}$ |
| 5 | Counting components by species rather than independent components | Phase-rule degrees of freedom wrong | Count components after allowing for reaction and electroneutrality |
| 6 | Wrong sign of $\Delta V$ in the Clapeyron equation | Melting-point shift has the wrong sign | $\Delta V = V_{\text{final}} - V_{\text{initial}}$; ice contracts on melting |
| 7 | Using $T$ in °C in Clausius–Clapeyron | Vapour pressure wrong by a large factor | Convert to kelvin before forming $1/T$ |
| 8 | Molar reduced mass in collision theory | $A$ too large by $\sqrt{N_{\text{A}}}$ | Divide the molar reduced mass by $N_{\text{A}}$ |
| 9 | Reporting $\Delta S$ of the system as $\Delta S_{\text{univ}}$ | Reversible and irreversible processes become indistinguishable | Add $-\Delta H/T$ or $-q/T$ for the surroundings |
| 10 | Treating a Raman-active mode as infrared-active without checking symmetry | Selection-rule question answered backwards | Check for a dipole change (IR) and a polarisability change (Raman) separately |

