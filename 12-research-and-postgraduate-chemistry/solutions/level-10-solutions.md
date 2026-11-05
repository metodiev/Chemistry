# Level 10 — Worked Solutions: Research and Postgraduate Chemistry

> **Level:** Research (Level 10 — University, Postgraduate and Research)
> **Items:** 51
> **Exercise bank:** [`../exercises/level-10-exercises.md`](../exercises/level-10-exercises.md)

Each solution gives the **Strategy**, the **Working**, the **Answer** and a **Check**.
Items marked **Multi-step** require at least three dependent operations. Research-design
answers state the design, the controls, the sample-size logic and the analysis plan,
because those four elements are what an examiner can mark; a design that omits one of
them is incomplete however good the chemistry.

Conventions: energies are in hartree unless stated; $1\ \mathrm{E_h} = 2625.4996\
\mathrm{kJ\,mol^{-1}}$; correlation energies are negative because Hartree–Fock is
variational; binding energies are negative for a bound dimer; rate and equilibrium
constants refer to the temperature stated; standard states are stated explicitly.
Sign conventions for thermochemical corrections, counterpoise corrections and Hammett
$\rho$ are given in the relevant solution rather than assumed.

---

## Part A — Conceptual questions

### 1. Which postulate licenses which step

**Strategy.** Match each step to the postulate that supplies the mathematical object,
then separate the statistical content of P3 from a dynamical collapse model.

**Working.** (a) The antisymmetrised product is licensed by **P5**: the state space of
identical fermions is the antisymmetric subspace of the tensor product, and P6 supplies
the two-dimensional spin factor. Without P5 the Hartree product would be admissible,
there would be no Pauli exclusion, no exchange integral $K_{ij}$ and no Fermi hole.
(b) The probability $|\langle a_n|\psi\rangle|^{2}$ is licensed by **P3**: possible
outcomes are eigenvalues and the probability is the squared overlap with the
eigenspace projector. Without P3 the formalism has no empirical content.
(c) The propagator $e^{-i\hat{H}t/\hbar}$ is licensed by **P4**. Without P4 there is no
time-dependent state and no spectroscopy.
(d) The tensor product is licensed by **P5**; without it entangled states, spin–orbit
coupling and the very notion of a composite system cannot be represented.

The word "collapse" is not part of P3 as the chapter states it. P3 gives the statistics
of outcomes for repeated measurements on identically prepared systems and the projected
state after a measurement; it does not specify a physical mechanism, a timescale or a
dynamical law for the update. The update is a change in the description conditional on
an outcome, not an additional postulate. A global phase is unobservable because it
cancels in $|\langle a|\psi\rangle|^{2}$; a relative phase is observable because it
changes interference.

**Answer.** (a) P5 with P6; (b) P3; (c) P4; (d) P5 with P6. P3 is a statistical
postulate, not a collapse dynamics.

**Check.** If P5 were dropped, the helium ground-state energy would omit the exchange
term and the exchange stabilisation of the $\ce{H2}$ triplet would be absent, so the
singlet–triplet gap would be wrong. If P3 were replaced by a deterministic statement,
the Stern–Gerlach splitting would be unexplained.

**Where marks are lost.** Answering P1 for (a) because a wavefunction is "a state", or
presenting collapse as a postulate with a mechanism and a timescale.

### 2. Why $E_{\mathrm{HF}}$ is not the sum of orbital energies

**Strategy.** Sum the orbital-energy expression and compare with the Hartree–Fock
energy expression; the difference is a pair-counting term.

**Working.** For canonical orbitals,
$$
\varepsilon_i = h_{ii} + \sum_j\left(J_{ij}-K_{ij}\right).
$$
Summing over occupied orbitals,
$$
\sum_i\varepsilon_i = \sum_i h_{ii} + \sum_{ij}\left(J_{ij}-K_{ij}\right)
= E_{\mathrm{HF}} + \tfrac12\sum_{ij}\left(J_{ij}-K_{ij}\right),
$$
because
$E_{\mathrm{HF}} = \sum_i h_{ii} + \tfrac12\sum_{ij}(J_{ij}-K_{ij})$. Hence
$$
E_{\mathrm{HF}} = \sum_i\varepsilon_i - \tfrac12\sum_{ij}\left(J_{ij}-K_{ij}\right)
= \tfrac12\sum_i\left(h_{ii}+\varepsilon_i\right).
$$
The correction is negative (the pair term is positive on balance), so the sum of orbital
energies is too negative. The physical reason is double counting: $\varepsilon_i$
contains the interaction of electron $i$ with the full density of the other $N-1$
electrons, and summing over $i$ counts each pair twice, once from each member. The
factor $\tfrac12$ removes the second copy.

**Answer.** $E_{\mathrm{HF}} = \tfrac12\sum_i(h_{ii}+\varepsilon_i)
= \sum_i\varepsilon_i - \tfrac12\sum_{ij}(J_{ij}-K_{ij})$. The correction is the
double-counted electron–electron repulsion.

**Check.** One electron: $J=K=0$, so $\varepsilon_1=h_{11}$ and $E=h_{11}=\sum_i\varepsilon_i$.
Two electrons in the same spatial orbital with opposite spins: $J_{11}=K_{11}$, so
$E=2h_{11}+J_{11}$; the orbital sum is $2(h_{11}+J_{11})=2h_{11}+2J_{11}$, and
subtracting $J_{11}$ recovers the correct energy.

**Where marks are lost.** Saying that "the $\tfrac12$ is because there are two
electrons" without the pair-counting argument, or omitting the exchange term from
$\varepsilon_i$.

### 3. Classifying correlation

**Strategy.** Ask first whether one determinant is qualitatively adequate. A near
degeneracy of configurations signals static correlation; a filled shell with a large
gap signals dynamic correlation only.

**Working.**
(a) **Ne at equilibrium.** The $2p$ shell is full and the HOMO–LUMO gap is large; the
leading determinant weight is essentially one. The correlation is **dynamic**, and
MP2 or CCSD(T) is the cheapest defensible method.
(b) **$\ce{H2}$ at $3r_e$.** The $\sigma_g^2$ and $\sigma_u^2$ configurations become
nearly degenerate as the bond stretches; in the valence-bond picture this is the
near-degeneracy of the covalent and ionic structures. The leading weight falls below
$0.9$ and eventually below $0.5$. The correlation is **static**; the cheapest
defensible treatment is CAS(2,2) with CASPT2 or NEVPT2 for the remaining dynamic
correlation.
(c) **Ozone at equilibrium.** The $\pi$ system has several near-degenerate
configurations and substantial biradical character; a single determinant is not
qualitatively adequate. The correlation is **static** (with dynamic correlation on
top), and CASSCF with an active space that includes the $\pi$ and $\pi^{*}$ orbitals
(and, if needed, the oxygen lone pairs) followed by CASPT2 or NEVPT2 is required.
(d) **Ethene at equilibrium.** The $\pi$ bond is well described by one configuration;
the correlation is **dynamic**, and MP2 or CCSD(T) is adequate.
(e) **A symmetry-forbidden cycloaddition transition state with a small HOMO–LUMO
gap.** The small gap and the avoided-crossing character make the transition state
biradicaloid; several configurations contribute. The correlation is **static**, and
CASSCF/CASPT2 is the defensible choice.

**Answer.** (a) dynamic, MP2/CCSD(T); (b) static, CAS(2,2)/CASPT2 or NEVPT2;
(c) static, CASSCF($\pi$)/CASPT2 or NEVPT2; (d) dynamic, MP2/CCSD(T); (e) static,
CASSCF/CASPT2.

**Check.** A T1 diagnostic above $0.02$ for a main-group molecule, a leading weight
below $0.9$, or a small HOMO–LUMO gap would support the static assignments; a large gap
and a weight near one would support the dynamic ones.

**Where marks are lost.** Equating "strong correlation" with "large correlation
energy". Static correlation is a small sum of large contributions, not a large total.

### 4. The Hohenberg–Kohn theorems and their domain

**Strategy.** State each theorem with its quantifier and domain, then separate the
existence claim from the approximation problem.

**Working.** **Theorem 1.** The ground-state density $\rho_0(\mathbf{r})$ determines
the external potential $v(\mathbf{r})$ up to an additive constant, and therefore the
Hamiltonian and every property. The proof is a *reductio*: if two potentials $v$ and
$v'$ differing by more than a constant had the same $\rho_0$, the variational principle
would give both $E_0<E_0'$ and $E_0'<E_0$, a contradiction. The original proof assumes
a **non-degenerate** ground state and that $\rho_0$ is **$v$-representable**, i.e. that
it comes from some external potential.

**Theorem 2.** For a trial density with $\tilde\rho\ge0$ and $\int\tilde\rho=N$,
$E[\tilde\rho]\ge E[\rho_0]=E_0$; the functional is minimised by the true density. In
the original formulation the domain is again the $v$-representable densities.

The **Levy constrained search** defines
$$
F[\rho] = \min_{\Psi\to\rho}\langle\Psi|\hat{T}+\hat{V}_{ee}|\Psi\rangle,
$$
where the minimum runs over antisymmetric wavefunctions yielding $\rho$. This defines
$F$ for every **$N$-representable** density, a much larger set, and it does not require
a non-degenerate ground state. The variational principle then applies on that domain.

The theorems are **existence** statements. They do not give the form of $F[\rho]$ or
$E_{xc}[\rho]$, do not guarantee that any practical functional is accurate, and do not
supply the derivative discontinuity that controls band gaps.

**Answer.** Theorem 1: $\rho_0\mapsto v$ up to a constant, hence all properties, for
non-degenerate $v$-representable ground states. Theorem 2: $E[\tilde\rho]\ge E[\rho_0]$
on the same domain. Levy extends the domain to $N$-representable densities. The theorems
guarantee existence, not accuracy.

**Check.** The constrained-search definition reduces to the ordinary variational
principle when $\rho$ is the density of a ground-state wavefunction; it is a
generalisation, not a different theory.

**Where marks are lost.** Claiming that the theorems prove that a specific functional is
exact, or omitting the non-degeneracy and $v$-representability qualifications.

### 5. One defect, five symptoms

**Strategy.** Trace every symptom to the residual self-repulsion of an electron with its
own density, then match the remedy to the range over which the error acts.

**Working.** For one electron the Hartree energy must be exactly cancelled by exchange.
Hartree–Fock satisfies this because $K_{ii}=J_{ii}$; a semilocal functional evaluates
exchange from the density point by point and cannot cancel the self-Coulomb exactly. The
residue is the self-interaction error, also called the delocalisation error.

(a) **Band gaps.** The exact energy as a function of electron number is piecewise linear
with a derivative discontinuity at integer $N$; the Kohn–Sham gap misses this
discontinuity, and the residual self-interaction lowers the gap further. A global hybrid
reduces the error; a range-separated functional is used for molecules, and DFT+$U$ or a
hybrid for correlated solids.
(b) **Charge-transfer excitations.** The separated electron and hole do not feel the
correct $-1/r$ attraction, so the CT energy is far too low. A range-separated functional
is the appropriate remedy because it restores long-range exact exchange.
(c) **Barriers.** The transition state is more delocalised than the reactant, so it is
stabilised more by the error; the barrier is too low. A global hybrid reduces the error.
(d) **Anions.** The extra electron is poorly bound because it repels its own density;
the anion is underbound or unbound. Diffuse functions plus a hybrid or range-separated
functional are required; an ECP is not a remedy for the correlation error.
(e) **Spin delocalisation.** The fractional-spin error favours symmetric, delocalised
spin densities over localised ones. A hybrid, a self-interaction correction or DFT+$U$
localises the spin.

None of the remedies removes the error because exact exchange is only partially
included, the correlation functional remains approximate, and the exact functional is
unknown. The fractional-charge and fractional-spin tests measure the residual curvature
directly.

**Answer.** All five are consequences of incomplete self-Coulomb cancellation; hybrids
and range separation mitigate (a)–(e) to different degrees, and DFT+$U$/SIC target
localised $d$ and $f$ systems. The error is reduced, never eliminated.

**Check.** The hydrogen atom is the cleanest test: exact $E=-0.5\ \mathrm{E_h}$; a
functional that gives a higher energy and a more diffuse density is showing
self-interaction error.

**Where marks are lost.** Treating the five symptoms as unrelated bugs, or claiming that
a hybrid "fixes" the band gap rather than reducing the error.

### 6. Dispersion and BSSE

**Strategy.** Separate three questions: what the functional can see, what the correction
adds, and what the basis set does.

**Working.** (a) A semilocal functional depends on $\rho$ and its gradients at a point.
The $C_6/R^{6}$ tail is a long-range correlation between fluctuations on two separated
density regions; it requires non-local information that a pointwise functional does not
have. The result is that a dimer binds far too weakly and a molecular crystal has the
wrong lattice energy.

(b) **D3** adds a damped pairwise term
$$
E_{\mathrm{disp}} = -\sum_{A<B}\left[s_6\frac{C_6^{AB}}{R_{AB}^{6}}f_6(R_{AB})
+s_8\frac{C_8^{AB}}{R_{AB}^{8}}f_8(R_{AB})\right],
$$
with precomputed reference coefficients and geometry-dependent scaling; it is a
post-SCF correction (the energy is added after the SCF, although the coefficients depend
on the geometry). A **non-local van der Waals functional** (vdW-DF, VV10) adds a
density-dependent integral term to $E_{xc}$ and is computed self-consistently, so it
also changes the density and the potential. **Many-body dispersion** treats coupled
oscillators and includes screening and three-body effects; it is usually applied
post-SCF.

(c) The damping function switches the correction off at short range, where the
functional already describes the correlation; without it the correction would
double-count. The counterpoise correction is a **basis-set** correction: it removes the
artificial stabilisation of each monomer by the partner's basis functions. It is
independent of dispersion: a calculation can have BSSE without a dispersion error, and a
dispersion correction does not remove BSSE. Both must be reported for a weak complex.

**Answer.** (a) Semilocal functionals lack the non-local information needed for the
$R^{-6}$ tail. (b) D3 is an additive pairwise correction; vdW-DF/VV10 is a
self-consistent non-local functional; MBD is a coupled-oscillator many-body correction.
(c) Damping prevents double counting; counterpoise corrects basis-set incompleteness,
not dispersion.

**Check.** A D3 correction changes the binding energy of a $\pi$-stacked dimer by an
amount comparable to the binding energy itself; a counterpoise correction is largest for
small bases and weak interactions.

**Where marks are lost.** Describing D3 as "part of the functional" (it is a
correction), or confusing BSSE with dispersion.

### 7. Force-field adequacy

**Strategy.** A fixed-charge, non-reactive force field has a fixed topology and fixed
partial charges; ask whether the chemistry requires bond breaking, charge transfer,
electronic polarisation or a change of spin state.

**Working.**
(a) **Proton transfer in an enzyme.** Inadequate. A proton transfer breaks and forms a
bond and moves charge; the fixed topology cannot represent it. Use a reactive force
field (ReaxFF), QM/MM with the active site in the quantum region, or ab initio MD. The
additional parameterisation is the bond-breaking/forming pathway, the charges along the
path and the proton-transfer barrier.
(b) **Ligand binding to a metal site.** Often inadequate. Fixed charges cannot describe
charge transfer, polarisation of the metal and ligand, or $d$-electron spin states. Use
a polarisable force field (Drude, AMOEBA) for the metal or QM/MM for the first
coordination shell; parameterise the metal–ligand bonds, the charge states and the
coordination geometry.
(c) **Density of liquid argon.** Adequate. Argon is monatomic and dispersion-dominated;
a Lennard-Jones model with $\varepsilon$ and $\sigma$ fitted to the density and vapour
pressure is sufficient. No bonded terms are needed.
(d) **Folding of a small peptide.** A validated fixed-charge protein force field with
explicit solvent is often adequate for conformational sampling, provided the force field
has been validated against experimental observables. It is not adequate for covalent
modification, proton transfer or electronic polarisation; use a polarisable force field
or QM/MM for those, and validate the folding free energy against experiment.

**Answer.** (a) no, reactive FF/QM/MM/AIMD; (b) no, polarisable FF or QM/MM;
(c) yes, Lennard-Jones; (d) generally yes for conformational sampling with a validated
protein FF, no for chemistry.

**Check.** The test is not whether the force field "looks reasonable" but whether it
reproduces the observable of interest in a validation set; a force field outside its
training domain is an extrapolation.

**Where marks are lost.** Saying "force fields cannot do metals" without naming the
extension, or claiming that a fixed-charge FF describes proton transfer because the
proton has a charge.

### 8. Thermostats compared

**Strategy.** Separate the mean-temperature behaviour from the distribution, then
separate equilibration from production.

**Working.**

| Thermostat | Canonical distribution? | Side effects | Appropriate use |
|---|---|---|---|
| Berendsen | No; fluctuations suppressed | Drives $T$ exponentially; wrong variance; flying-ice-cube risk | Equilibration only |
| Nosé–Hoover | Yes, for ergodic systems | Oscillatory $T$ if $\tau$ too small; can be non-ergodic for stiff systems | Production with a tested $\tau$ |
| Langevin | Yes, by construction (fluctuation–dissipation) | Stochastic; adds friction; changes dynamics | Production, implicit solvent, robust sampling |
| Bussi–Donadio–Parrinello | Yes | Stochastic rescaling; little bias | Production, safe default |

The canonical kinetic-energy variance is
$$
\mathrm{var}(K) = \frac{3N}{2}k_\mathrm{B}^{2}T^{2}.
$$
Berendsen scaling gives a narrower distribution, so the variance test detects it even
when the mean temperature is correct. The **flying-ice-cube** artefact arises when a
thermostat rescales all velocities indiscriminately: kinetic energy is removed from
internal motion and deposited in centre-of-mass translation, so the whole system drifts
and the internal temperature falls while the thermostat reports the target. Remedies:
remove the centre-of-mass velocity periodically, use a thermostat that acts on peculiar
velocities, and check the temperature computed from the peculiar kinetic energy.

**Answer.** Berendsen for equilibration only; Nosé–Hoover, Langevin and BDP for
production, with Langevin/BDP the safest defaults; the variance criterion and the
peculiar-velocity check are the diagnostics.

**Check.** A production run with Berendsen may show the correct mean $T$ but a variance
below $(3N/2)k_\mathrm{B}^{2}T^{2}$; that is the signature of the error.

**Where marks are lost.** Saying Berendsen "is wrong" without saying what it is wrong
for, or forgetting that the number of degrees of freedom changes when constraints are
used.

### 9. Ranking mechanistic evidence

**Strategy.** Rank by how directly the evidence identifies a species on the reaction
path and how little it depends on a model.

**Working.** Strongest to weakest: **(b) > (d) > (a) > (c)**.
(b) A transient absorption at 450 nm whose decay matches the formation of product is
direct spectroscopic evidence for a species that is kinetically competent. It identifies
the species and its lifetime; the caveat is that the observed species may be off-path or
generated by the probe.
(d) A crossover product in a labelling experiment establishes intermolecularity and the
origin of atoms. It is strong evidence about mechanism, but it does not identify the
intermediate or its lifetime.
(a) A rate law first order in substrate and zeroth order in nucleophile constrains the
stoichiometry of the rate-determining step; several mechanisms can give the same law.
(c) A computed free-energy profile supports a mechanism but depends on the model
chemistry, the conformer search and the functional; it does not replace experiment.

A radical-trapping experiment can change the mechanism it is meant to probe: the trap
consumes radicals, lowers their steady-state concentration, can shut down a chain,
create a new product, or quench the excited state. The perturbation can shift the
system to a different pathway. The defences are to use low trap concentrations, to
measure the trapping rate, to check that the product distribution at low conversion is
unchanged, and to use a trap that reports on the radical without removing it.

**Answer.** (b) > (d) > (a) > (c). Direct observation of a kinetically competent
intermediate outranks labelling, which outranks rate law, which outranks computation.

**Check.** A species observed at 450 nm is only an intermediate if its decay is
correlated with product formation and if its concentration responds to the substrate in
the way the mechanism predicts.

**Where marks are lost.** Ranking computation above experiment, or treating a rate law
as a unique structural assignment.

### 10. Dual-use review

**Strategy.** Apply the five questions in order; separate the scientific claim from the
operational recipe; record the decision.

**Working.** The five questions are: what is the plausible misuse; how feasible is it
for a non-specialist; does the paper provide information that is not already public;
does the scientific value justify the risk; can the risky material be removed without
destroying the scientific claim. For a scheduled precursor, the plausible misuse is
clear; the feasibility question asks whether the paper supplies the missing step
(purification, stabilisation, scale-up, precursor synthesis). If the answer is yes and
the information is not already public, the risk is real.

Publishable: the mechanism, the selectivity, the analytical characterisation, the
general transformation and the safety-relevant properties. Withheld or generalised: exact
quantities, purification procedures, stabilisation, scale-up, the identity of scheduled
precursors and any weaponisation-relevant detail. A controlled appendix available to
reviewers and regulators can carry the operational detail without printing it.

The norm is workable because the scientific claim is usually separable from the
operational recipe: a reader can evaluate the mechanism and the selectivity without
being able to repeat the dangerous step. It is not censorship because it is a
harm-based condition on publication, applied transparently by an institutional review
body, with a documented decision and an appeal route, and because it leaves the
scientific conclusion in the public record. The researcher is also bound by national
implementing legislation and institutional policy; the ethical obligation goes beyond
legality.

**Answer.** Publish the mechanism and the scientific claim; withhold the enabling
detail; record the five-question review and the decision. The norm is a proportionate,
reviewable restriction, not censorship.

**Check.** If removing the operational detail leaves the scientific claim intact, the
restriction is proportionate; if the claim cannot be evaluated without the recipe, the
work should not be published in that form and the institution's dual-use body should
decide.

**Where marks are lost.** Treating the question as a legal checklist, or claiming that
"everything must be published" without engaging with the harm.

---

## Part B — Theory and derivations

### 11. The Hartree–Fock energy from the Slater–Condon rules

**Strategy.** Write the determinant, apply the one- and two-electron Slater–Condon
rules, then inspect the self-interaction term.

**Working.** Let $\{\chi_i\}$ be orthonormal spin-orbitals and
$$
\Psi(\mathbf{x}_1,\dots,\mathbf{x}_N) = \frac{1}{\sqrt{N!}}
\det\left[\chi_1(\mathbf{x}_1)\cdots\chi_N(\mathbf{x}_N)\right].
$$
The electronic Hamiltonian is
$$
\hat{H} = \sum_{i=1}^{N}\hat{h}(i) + \sum_{i<j}^{N}\frac{1}{r_{ij}},
\qquad
\hat{h}(i) = -\frac12\nabla_i^{2} - \sum_A\frac{Z_A}{|\mathbf{r}_i-\mathbf{R}_A|}.
$$
The one-electron term gives
$$
\left\langle\Psi\left|\sum_i\hat{h}(i)\right|\Psi\right\rangle
= \sum_i h_{ii},
\qquad
h_{ii} = \int\chi_i^{*}(\mathbf{x})\hat{h}\,\chi_i(\mathbf{x})\,\mathrm{d}\mathbf{x}.
$$
The two-electron term gives, for each ordered pair $(i,j)$,
$J_{ij}-K_{ij}$, with
$$
J_{ij} = \iint|\chi_i(1)|^{2}\frac{1}{r_{12}}|\chi_j(2)|^{2}\,\mathrm{d}1\,\mathrm{d}2,
\qquad
K_{ij} = \iint\chi_i^{*}(1)\chi_j(1)\frac{1}{r_{12}}\chi_j^{*}(2)\chi_i(2)\,\mathrm{d}1\,\mathrm{d}2.
$$
The double sum counts each unordered pair twice, so
$$
E_{\mathrm{HF}} = \sum_i h_{ii} + \frac12\sum_{ij}\left(J_{ij}-K_{ij}\right).
$$
For $i=j$, $J_{ii}=K_{ii}$: the Coulomb integral of an orbital with itself equals the
exchange integral of that orbital with itself, because both are the same two-electron
integral with the labels rearranged. The self term therefore cancels exactly. This is
the Hartree–Fock statement that an electron neither repels nor exchanges with itself.
The factor $\tfrac12$ is the pair-counting correction, not a physical factor.

Assumptions: non-relativistic Hamiltonian, Born–Oppenheimer clamped nuclei, no external
field, orthonormal spin-orbitals, a single determinant, a finite basis, and fixed
nuclear geometry (the nuclear repulsion $V_{NN}$ is added separately).

**Answer.** $E_{\mathrm{HF}} = \sum_i h_{ii} + \tfrac12\sum_{ij}(J_{ij}-K_{ij})$,
with $J_{ii}=K_{ii}$.

**Check.** Two electrons in the same spatial orbital with opposite spins:
$K_{12}=0$ because $\langle\alpha|\beta\rangle=0$, so $E=2h_{11}+J_{11}$. Two electrons
with parallel spins in orthogonal orbitals: $E=h_{11}+h_{22}+J_{12}-K_{12}$, and the
exchange term lowers the triplet, as it must.

**Where marks are lost.** Omitting the $\tfrac12$, or claiming that $K_{ij}$ is
nonzero for antiparallel spins. Exchange acts only between parallel spins.

### 12. The Fock operator from constrained variation

**Strategy.** Minimise the energy subject to orthonormality with a Hermitian matrix of
Lagrange multipliers; then use the Hermiticity of the Fock operator to diagonalise.

**Working.** The functional is
$$
L = E[\{\chi\}] - \sum_{ij}\varepsilon_{ij}\left(\langle\chi_i|\chi_j\rangle-\delta_{ij}\right).
$$
Varying $\chi_i^{*}$ and requiring stationarity gives
$$
\hat{h}\chi_i + \sum_j\left(\hat{J}_j-\hat{K}_j\right)\chi_i = \sum_j\varepsilon_{ij}\chi_j,
$$
with
$$
\hat{J}_j(1)\chi_i(1) = \chi_i(1)\int|\chi_j(2)|^{2}r_{12}^{-1}\,\mathrm{d}2,
\qquad
\hat{K}_j(1)\chi_i(1) = \chi_j(1)\int\chi_j^{*}(2)\chi_i(2)r_{12}^{-1}\,\mathrm{d}2.
$$
The bracketed operator is the **Fock operator**
$\hat{F} = \hat{h} + \sum_j(\hat{J}_j-\hat{K}_j)$, so
$\hat{F}\chi_i = \sum_j\varepsilon_{ij}\chi_j$.

Because $\hat{F}$ is Hermitian, the matrix $\varepsilon_{ij}$ is Hermitian and can be
diagonalised by a unitary transformation $U$ among the occupied orbitals. The
transformation $\chi'_i = \sum_j\chi_j U_{ji}$ leaves the determinant unchanged up to a
phase, so the energy and density are unchanged. In the new basis
$\hat{F}\chi'_i = \varepsilon_i\chi'_i$: these are the **canonical orbitals**.

The orbital energy follows by multiplying by $\chi_i^{*}$ and integrating:
$$
\varepsilon_i = h_{ii} + \sum_j\left(J_{ij}-K_{ij}\right).
$$
Summing,
$$
\sum_i\varepsilon_i = \sum_i h_{ii} + \sum_{ij}\left(J_{ij}-K_{ij}\right)
= E_{\mathrm{HF}} + \tfrac12\sum_{ij}\left(J_{ij}-K_{ij}\right),
$$
so
$$
E_{\mathrm{HF}} = \tfrac12\sum_i\left(h_{ii}+\varepsilon_i\right).
$$

The derivation fails for a multideterminant wavefunction because the energy is no longer
stationary with respect to independent orbital rotations in the same way: Brillouin's
theorem does not hold, the one-electron operator that would generate the orbitals is not
the Fock operator of the correlated state, and the orbital transformation changes the
CI coefficients as well as the orbitals. A multireference treatment requires a
generalised or state-averaged Fock operator and a CI step.

**Answer.** $\hat{F}\chi_i = \varepsilon_i\chi_i$ with
$\hat{F} = \hat{h} + \sum_j(\hat{J}_j-\hat{K}_j)$, and
$E_{\mathrm{HF}} = \tfrac12\sum_i(h_{ii}+\varepsilon_i)$.

Assumptions: single determinant, orthonormal spin-orbitals, Hermitian $\hat{F}$,
canonical orbitals chosen by a unitary transformation among occupied orbitals.

**Check.** For one electron, $\hat{F}=\hat{h}$, $\varepsilon_1=h_{11}$, and
$E=\tfrac12(h_{11}+\varepsilon_1)=h_{11}$.

**Where marks are lost.** Forgetting the Lagrange multipliers, or claiming that the
canonical orbitals change the determinant. They change it only by a phase.

### 13. Coupling $l=1$ with $s=1/2$

**Strategy.** Apply the lowering operator to the stretched state, use the known ladder
matrix elements, and fix the orthogonal combination by normalisation and orthogonality.

**Working.** The stretched state is
$|3/2,3/2\rangle = |1,1\rangle|\tfrac12,\tfrac12\rangle$. With
$\hat{J}_- = \hat{L}_- + \hat{S}_-$,
$$
\hat{J}_-|3/2,3/2\rangle = \hbar\sqrt{3}\,|3/2,1/2\rangle,
$$
because
$\sqrt{j(j+1)-m(m-1)} = \sqrt{(3/2)(5/2)-(3/2)(1/2)} = \sqrt{3}$.
On the uncoupled states,
$$
\hat{L}_-|1,1\rangle = \hbar\sqrt{2}\,|1,0\rangle,
\qquad
\hat{S}_-|\tfrac12,\tfrac12\rangle = \hbar\,|\tfrac12,-\tfrac12\rangle.
$$
Therefore
$$
\hbar\sqrt{3}\,|3/2,1/2\rangle
= \hbar\sqrt{2}\,|1,0\rangle|\tfrac12,\tfrac12\rangle
+ \hbar\,|1,1\rangle|\tfrac12,-\tfrac12\rangle,
$$
so
$$
|3/2,1/2\rangle = \sqrt{\tfrac23}\,|1,0\rangle|\tfrac12,\tfrac12\rangle
+ \sqrt{\tfrac13}\,|1,1\rangle|\tfrac12,-\tfrac12\rangle.
$$
The orthogonal combination is
$$
|1/2,1/2\rangle = -\sqrt{\tfrac13}\,|1,0\rangle|\tfrac12,\tfrac12\rangle
+ \sqrt{\tfrac23}\,|1,1\rangle|\tfrac12,-\tfrac12\rangle,
$$
which is normalised, $1/3+2/3=1$, and orthogonal to the quartet:
$-\sqrt{2}/3+\sqrt{2}/3=0$.

The phase convention is the Condon–Shortley convention: the ladder matrix elements are
real and positive, and the stretched state carries the conventional phase. The sign of
the doublet is fixed by orthogonality once the quartet phase is fixed; the overall sign
of either state is not physical. The derivation assumes that $\hat{\mathbf{L}}$ and
$\hat{\mathbf{S}}$ act on different degrees of freedom and therefore commute, so
$\hat{\mathbf{J}}=\hat{\mathbf{L}}+\hat{\mathbf{S}}$ obeys the angular-momentum algebra.

**Answer.** As above; the quartet and doublet are the $J=3/2$ and $J=1/2$ coupled
states, and the dimensions match: $4+2=6=3\times2$.

**Check.** Apply $\hat{J}^{2}$ to the quartet: $J(J+1)=15/4$, as required for $j=3/2$.
The doublet has $J(J+1)=3/4$. The sum of the multiplicities equals the dimension of the
uncoupled space.

**Where marks are lost.** Normalising the doublet by inspection without imposing
orthogonality, or using a different phase convention and then treating the sign as
physical.

### 14. Size consistency of CI and coupled cluster

**Strategy.** Compare the excitation rank of the same physical event in the monomer and
in the dimer, then compare the CI and exponential ansätze.

**Working.** Take two helium atoms at a separation large enough that their interaction
is negligible. For one atom, the reference is $1s^{2}$ and the leading correlation
excitation is the double excitation $1s^{2}\to 2s^{2}$ (or $2p^{2}$). For the dimer, the
reference is the product of the two atomic references. The **simultaneous** double
excitation on both atoms is a **quadruple** excitation relative to the dimer reference:
it excites two electrons on atom A and two on atom B. CISD includes at most double
excitations of the dimer, so it omits this quadruple. The CISD energy of the dimer is
therefore not twice the CISD energy of the monomer: the missing term is the product of
the two double-excitation amplitudes, of order $\lambda^{2}$, which is precisely the
disconnected correlation that a size-consistent method must retain.

In coupled cluster,
$$
|\Psi_{\mathrm{CC}}\rangle = e^{\hat{T}}|\Phi_0\rangle
= \left(1+\hat{T}_1+\hat{T}_2+\tfrac12\hat{T}_2^{2}+\cdots\right)|\Phi_0\rangle.
$$
The $\tfrac12\hat{T}_2^{2}$ term generates the disconnected quadruple. For two
non-interacting fragments, $\hat{T}=\hat{T}_A+\hat{T}_B$ and the exponential factorises:
$$
e^{\hat{T}_A+\hat{T}_B} = e^{\hat{T}_A}e^{\hat{T}_B}.
$$
The energy is therefore additive, $E_{AB}=E_A+E_B$, at every truncation level, because
the exponential generates the products of fragment excitations to all orders. CCSD
truncates the connected cluster operator at doubles, but the products of doubles are
retained through the exponential.

The consequence for CISD is that reaction energies and atomisation energies are
size-inconsistent: the error grows with the number of bonds, so a reaction that changes
the number of bonds is biased. The error can be corrected empirically (Davidson
correction) but not removed.

Assumptions: localised orbitals, non-interacting fragments, the same one-particle basis
for monomer and dimer, and negligible inter-fragment overlap. The argument is exact in
the limit of zero interaction and is the standard definition of size consistency.

**Answer.** CISD omits the disconnected quadruple $\tfrac12 T_2^2$; CC retains it
through the exponential, so CC is size-consistent at every truncation and CISD is not.

**Check.** Two non-interacting He atoms: CISD gives $E_{\mathrm{CISD}}(\mathrm{dimer})
\ne 2E_{\mathrm{CISD}}(\mathrm{monomer})$, while CCSD gives equality to numerical
precision. The difference is the missing disconnected quadruple.

**Where marks are lost.** Saying that CISD is "not size-consistent because it is
truncated" without identifying the missing term, or claiming that CCSD is variational
(it is not).

### 15. The Kohn–Sham equations

**Strategy.** Vary the density expressed through orbitals, impose the particle-number
constraint, and identify the exchange–correlation potential as the functional derivative.

**Working.** The energy is
$$
E[\rho] = T_s[\rho] + \int v(\mathbf{r})\rho(\mathbf{r})\,\mathrm{d}\mathbf{r}
+ \frac12\iint\frac{\rho(\mathbf{r})\rho(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}
\,\mathrm{d}\mathbf{r}\,\mathrm{d}\mathbf{r}' + E_{xc}[\rho],
$$
with $\rho = \sum_i|\phi_i|^{2}$ and $T_s = -\tfrac12\sum_i\langle\phi_i|\nabla^{2}|\phi_i\rangle$.
Impose the particle-number constraint $\int\rho=N$ with a Lagrange multiplier $\mu$ and
the orbital orthonormality with multipliers $\varepsilon_{ij}$; because $N$ orthonormal
orbitals integrate to $N$ electrons, the particle-number constraint is automatically
satisfied once orthonormality is enforced, so $\mu$ can be absorbed into the orbital
multipliers. Varying $\phi_i^{*}$:
$$
\frac{\delta T_s}{\delta\phi_i^{*}} = -\tfrac12\nabla^{2}\phi_i,
\qquad
\frac{\delta J}{\delta\rho} = v_H(\mathbf{r})
= \int\frac{\rho(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|}\,\mathrm{d}\mathbf{r}',
\qquad
\frac{\delta E_{xc}}{\delta\rho} = v_{xc}(\mathbf{r}).
$$
Stationarity gives
$$
\left[-\tfrac12\nabla^{2}+v(\mathbf{r})+v_H(\mathbf{r})+v_{xc}(\mathbf{r})\right]\phi_i
= \sum_j\varepsilon_{ij}\phi_j,
\qquad
v_{xc} = \frac{\delta E_{xc}}{\delta\rho}.
$$
The bracketed operator is the Kohn–Sham Hamiltonian $\hat{F}^{\mathrm{KS}}$. It is
Hermitian, so $\varepsilon_{ij}$ is Hermitian and a unitary transformation among the
occupied orbitals diagonalises it without changing the density. In the canonical basis,
$$
\hat{F}^{\mathrm{KS}}\phi_i = \varepsilon_i\phi_i,
$$
which is the Kohn–Sham equation. The assumption is **non-interacting
$v$-representability**: the interacting density must be representable by a
non-interacting determinant. If it is not, the Kohn–Sham construction fails and one
must use an ensemble or a more general formulation.

The Kohn–Sham orbitals are mathematical objects: they reproduce the density but the true
wavefunction is not a determinant, and the orbitals have no direct physical meaning. Only
the highest occupied orbital energy approximates an ionisation energy, and the orbital
energy differences are not excitation energies. All the missing physics is in
$E_{xc}$, which is approximated.

**Answer.** The Kohn–Sham equations above, with
$v_{xc}=\delta E_{xc}/\delta\rho$; the assumption is non-interacting
$v$-representability, and the orbitals are not physical.

**Check.** For a one-electron system, $J[\rho]$ and $E_{xc}$ must cancel exactly to
give the hydrogenic equation; an approximate functional does not cancel, which is the
self-interaction error.

**Where marks are lost.** Writing $v_{xc}$ as an ordinary potential without saying it is
a functional derivative, or treating the Kohn–Sham orbitals as the physical orbitals.

### 16. The counterpoise correction

**Strategy.** Define each energy with its superscript (basis) and subscript (nuclei),
then form the two interaction energies and subtract.

**Working.** The uncorrected interaction energy is
$$
\Delta E_{\mathrm{int}}^{\mathrm{uncorr}} = E_{AB}^{AB} - E_A^{A} - E_B^{B},
$$
where the superscript is the basis and the subscript the nuclei present. The
counterpoise-corrected interaction energy evaluates each monomer in the **dimer basis**:
$$
\Delta E_{\mathrm{int}}^{\mathrm{CP}} = E_{AB}^{AB} - E_A^{AB} - E_B^{AB}.
$$
The basis-set superposition error is the stabilisation of the monomers by the partner's
basis functions:
$$
E_{\mathrm{BSSE}} = \left(E_A^{AB}+E_B^{AB}\right) - \left(E_A^{A}+E_B^{B}\right).
$$
Then
$$
\Delta E_{\mathrm{int}}^{\mathrm{CP}}
= E_{AB}^{AB} - E_A^{A} - E_B^{B}
- \left[\left(E_A^{AB}+E_B^{AB}\right)-\left(E_A^{A}+E_B^{B}\right)\right]
= \Delta E_{\mathrm{int}}^{\mathrm{uncorr}} - E_{\mathrm{BSSE}}.
$$
Since $E_{\mathrm{BSSE}}$ is usually negative (the monomers are lower in the dimer
basis), subtracting it makes the binding less negative: the correction **weakens** the
binding.

The assumption is that the fragment deformation is negligible: the monomers are held at
the geometry they have in the dimer, and the interaction energy is the difference
between the dimer and the separated monomers at that geometry. If the monomer geometry
is relaxed in the dimer basis, the CP monomer energy includes a deformation that is not
a physical interaction, and the correction can overcorrect. The standard protocol keeps
the geometry fixed and uses ghost functions for the partner.

**Answer.** $\Delta E_{\mathrm{int}}^{\mathrm{CP}} = \Delta E_{\mathrm{int}}^{\mathrm{uncorr}} - E_{\mathrm{BSSE}}$;
a negative BSSE makes the corrected binding weaker; the correction assumes negligible
fragment deformation.

**Check.** If the monomer energies are unchanged by the partner basis,
$E_A^{AB}=E_A^A$ and $E_B^{AB}=E_B^B$, then $E_{\mathrm{BSSE}}=0$ and the two
interaction energies agree.

**Where marks are lost.** Reversing the sign of the BSSE, or describing the correction
as a dispersion correction. It is a basis-set correction.

### 17. Verlet integration and stability

**Strategy.** Expand positions forward and backward, add, and read off the truncation
order; then analyse the harmonic recursion.

**Working.** Taylor expansion about $t$:
$$
\mathbf{r}(t+\Delta t) = \mathbf{r}(t)+\mathbf{v}(t)\Delta t
+\frac{\mathbf{F}(t)}{2m}\Delta t^{2}
+\frac{\dddot{\mathbf{r}}(t)}{6}\Delta t^{3}+O(\Delta t^{4}),
$$
$$
\mathbf{r}(t-\Delta t) = \mathbf{r}(t)-\mathbf{v}(t)\Delta t
+\frac{\mathbf{F}(t)}{2m}\Delta t^{2}
-\frac{\dddot{\mathbf{r}}(t)}{6}\Delta t^{3}+O(\Delta t^{4}).
$$
Adding eliminates the odd terms:
$$
\mathbf{r}(t+\Delta t) = 2\mathbf{r}(t)-\mathbf{r}(t-\Delta t)
+\frac{\mathbf{F}(t)}{m}\Delta t^{2}+O(\Delta t^{4}).
$$
The local truncation error is $O(\Delta t^{4})$; the global error is $O(\Delta t^{2})$,
so Verlet is a second-order integrator.

For a harmonic oscillator, $F=-m\omega^{2}x$, so
$$
x_{n+1} = \left(2-\omega^{2}\Delta t^{2}\right)x_n - x_{n-1}.
$$
Substituting $x_n=A\lambda^{n}$ gives
$$
\lambda^{2}-\left(2-\omega^{2}\Delta t^{2}\right)\lambda+1=0.
$$
The product of the roots is 1. For $\omega\Delta t<2$ the discriminant is negative and
the roots are a complex-conjugate pair on the unit circle, so the motion is bounded. For
$\omega\Delta t>2$ the roots are real and one has modulus greater than one, so the
trajectory grows exponentially. The stability limit is therefore
$$
\Delta t<\frac{2}{\omega}.
$$
The analysis assumes a harmonic potential, constant mass, forces that depend only on
position, and no constraints or thermostat. The stability limit is not an accuracy
criterion: at $\omega\Delta t=0.2$ the fractional energy error per period is already of
order $10^{-3}$, and 10–20 steps per period are needed for quantitative work. A step can
be stable and still fail to resolve the motion.

**Answer.** Local error $O(\Delta t^{4})$, global $O(\Delta t^{2})$, stability
$\Delta t<2/\omega$.

**Check.** A C–H stretch near $3000\ \mathrm{cm^{-1}}$ has
$\omega\approx5.65\times10^{14}\ \mathrm{s^{-1}}$, so $2/\omega\approx3.5\ \mathrm{fs}$;
a $2\ \mathrm{fs}$ step is stable but gives only about $5.6$ steps per period, which is
not accurate.

**Where marks are lost.** Calling Verlet third-order because the local error is
$O(\Delta t^{4})$, or confusing the stability limit with the accuracy requirement.

### 18. Umbrella sampling and the free-energy profile

**Strategy.** Write the biased ensemble average, factor the bias out of the integral,
and identify the additive constant per window.

**Working.** Let $\xi(\Gamma)$ be the collective variable. The biased probability
density is
$$
P_b(\xi) = \frac{1}{Z_b}\int\mathrm{d}\Gamma\,\delta(\xi-\xi(\Gamma))\,
e^{-\beta\left[U(\Gamma)+U_b(\xi(\Gamma))\right]},
\qquad
Z_b = \int\mathrm{d}\Gamma\,e^{-\beta\left[U+U_b\right]}.
$$
Because $U_b$ depends only on $\xi$, it can be taken outside the integral at fixed
$\xi$:
$$
P_b(\xi) = e^{-\beta U_b(\xi)}\frac{1}{Z_b}\int\mathrm{d}\Gamma\,\delta(\xi-\xi(\Gamma))\,
e^{-\beta U(\Gamma)}
= e^{-\beta U_b(\xi)}P_0(\xi)\frac{Z_0}{Z_b}.
$$
Therefore
$$
P_0(\xi) = P_b(\xi)\,e^{\beta U_b(\xi)}\,\frac{Z_b}{Z_0},
$$
and the free energy is
$$
F(\xi) = -k_\mathrm{B}T\ln P_0(\xi)
= -k_\mathrm{B}T\ln P_b(\xi) - U_b(\xi) + C,
$$
with $C$ constant for the window. Each window determines $F(\xi)$ up to an additive
constant. The constants are fixed by the requirement that the windows agree in their
regions of overlap; WHAM or MBAR solve for them self-consistently by maximising the
likelihood of the overlapping histograms. Without overlap the relative offset is
unknown, and the spliced profile is arbitrary.

Assumptions: ergodicity within each window, adequate sampling, a collective variable
that captures the slow mode, a known bias potential, constant temperature, and a
Boltzmann distribution in the biased ensemble.

**Answer.** $F(\xi) = -k_\mathrm{B}T\ln P_b(\xi)-U_b(\xi)+C$; the constants are fixed
by overlap and solved by WHAM/MBAR.

**Check.** A factor of two in probability corresponds to
$k_\mathrm{B}T\ln2\approx1.72\ \mathrm{kJ\,mol^{-1}}$ at 298 K. Overlap factors between
about 0.1 and 10 are acceptable; below 0.01 the windows are effectively disconnected.

**Where marks are lost.** Omitting the $-U_b(\xi)$ term (which would leave the biased
free energy), or claiming that the constants are determined by the absolute free energy
of one window rather than by overlap.

### 19. The Eyring equation

**Strategy.** Start from the quasi-equilibrium between reactants and the transition
state, multiply by the universal frequency for crossing the barrier, and convert the
equilibrium constant to a free energy.

**Working.** Transition-state theory assumes a quasi-equilibrium between the reactants
and the transition state, with
$$
K^{\ddagger} = \frac{[\mathrm{TS}]}{[\mathrm{reactants}]}
= \frac{Q^{\ddagger}}{Q_R}e^{-\Delta E_0/k_\mathrm{B}T},
$$
where $Q^{\ddagger}$ includes all modes of the transition state except the reaction
coordinate, and $\Delta E_0$ is the barrier at 0 K. The reaction coordinate is treated
as a free translation over a length $\delta$; the frequency of crossing the barrier is
$k_\mathrm{B}T/h$, independent of $\delta$, and the corresponding partition function
cancels the unknown $\delta$. The rate is
$$
k = \kappa\frac{k_\mathrm{B}T}{h}K^{\ddagger},
$$
where $\kappa$ is the transmission coefficient (the probability that a trajectory
crossing the barrier goes on to product). Converting $K^{\ddagger}$ to a standard free
energy, $\Delta G^{\ddagger} = -RT\ln K^{\ddagger}$,
$$
k = \kappa\frac{k_\mathrm{B}T}{h}e^{-\Delta G^{\ddagger}/RT}.
$$
Using $\Delta G^{\ddagger}=\Delta H^{\ddagger}-T\Delta S^{\ddagger}$,
$$
k = \kappa\frac{k_\mathrm{B}T}{h}e^{\Delta S^{\ddagger}/R}
e^{-\Delta H^{\ddagger}/RT}.
$$
Taking logarithms,
$$
\ln\frac{k}{T} = \ln\frac{\kappa k_\mathrm{B}}{h}
+\frac{\Delta S^{\ddagger}}{R}
-\frac{\Delta H^{\ddagger}}{R}\frac{1}{T}.
$$
A plot of $\ln(k/T)$ against $1/T$ therefore has slope $-\Delta H^{\ddagger}/R$ and
intercept $\ln(\kappa k_\mathrm{B}/h)+\Delta S^{\ddagger}/R$.

Assumptions: a single rate-determining step, quasi-equilibrium between reactants and
the transition state, $\kappa\approx1$ in the absence of tunnelling, classical motion
along the reaction coordinate, $\Delta H^{\ddagger}$ and $\Delta S^{\ddagger}$
independent of temperature over the measured range, and a consistent standard state.

**Answer.** $k=\kappa(k_\mathrm{B}T/h)e^{-\Delta G^{\ddagger}/RT}$; slope
$-\Delta H^{\ddagger}/R$, intercept $\ln(\kappa k_\mathrm{B}/h)+\Delta S^{\ddagger}/R$.

**Check.** For a unimolecular reaction at 298 K, $k_\mathrm{B}T/h\approx6.21\times10^{12}\
\mathrm{s^{-1}}$; a rate constant of $10^{-4}\ \mathrm{s^{-1}}$ corresponds to
$\Delta G^{\ddagger}\approx96\ \mathrm{kJ\,mol^{-1}}$, which is a chemically reasonable
barrier.

**Where marks are lost.** Using $k=Ae^{-E_a/RT}$ and calling $E_a$ equal to
$\Delta H^{\ddagger}$ without the $RT$ correction, or forgetting the $\ln(T_2/T_1)$ term
in the two-temperature form.

### 20. Sample size for a two-sample comparison

**Strategy.** Standardise the difference of means under the null and under the
alternative, then solve for $n$.

**Working.** Let $\bar{x}_1-\bar{x}_2$ be the observed difference, with equal group
sizes $n$ and common variance $\sigma^{2}$. Under the null hypothesis the difference has
variance $2\sigma^{2}/n$, so
$$
Z = \frac{\bar{x}_1-\bar{x}_2}{\sqrt{2\sigma^{2}/n}}\sim N(0,1).
$$
The two-sided test at level $\alpha$ rejects when
$|\bar{x}_1-\bar{x}_2|>z_{1-\alpha/2}\sqrt{2\sigma^{2}/n}$. If the true difference is
$\delta$, the power is
$$
1-\beta = P\left(|Z+\delta\sqrt{n/(2\sigma^{2})}|>z_{1-\alpha/2}\right)
\approx \Phi\left(\delta\sqrt{\frac{n}{2\sigma^{2}}}-z_{1-\alpha/2}\right),
$$
neglecting the lower tail. Setting this equal to $1-\beta$ gives
$$
\delta\sqrt{\frac{n}{2\sigma^{2}}}-z_{1-\alpha/2}=z_{1-\beta},
$$
and hence
$$
n = \frac{2\left(z_{1-\alpha/2}+z_{1-\beta}\right)^{2}\sigma^{2}}{\delta^{2}}
= \frac{2\left(z_{1-\alpha/2}+z_{1-\beta}\right)^{2}}{d^{2}},
\qquad d=\frac{\delta}{\sigma}.
$$
The result is the number **per group** and must be rounded up.

Assumptions: independent observations, equal variances, normality (or large $n$ so the
central limit theorem applies), a two-sided test, known $\sigma$, and a simple
two-group comparison. With a $t$-test, iterate with the $t$ quantiles; with unequal
variances, use the Welch form; with blocking or covariates, the relevant variance is the
residual variance after the design, not the raw variance.

The formula depends on the **smallest effect size of interest**, not on the observed
effect, because $\delta$ must be chosen before the data are seen. Choosing $\delta$ after
the experiment to match the observed difference guarantees a significant result and is a
form of circular analysis.

**Answer.** $n=2(z_{1-\alpha/2}+z_{1-\beta})^{2}/d^{2}$ per group; $d=\delta/\sigma$.

**Check.** For $d=0.5$, $\alpha=0.05$ and power 0.80,
$n=2(1.960+0.842)^{2}/0.25=62.8$, so 63 per group; for $d=1.25$, $n=10.0$, so 11 per
group. The $1/d^{2}$ scaling is the reason small effects are expensive.

**Where marks are lost.** Using a one-sided $z$ by mistake, forgetting to round up, or
substituting the observed effect for the smallest effect of interest.

---

## Part C — Computational and data problems

### 21. Correlation energy from two total energies **(Multi-step)**

**Strategy.** Subtract the Hartree–Fock energy from the exact energy in the same basis,
convert with the Hartree-to-kJ factor, and express the magnitude relative to the total
and to a bond enthalpy.

**Working.**
$$
E_{\mathrm{corr}} = E_{\mathrm{exact}}-E_{\mathrm{HF}}
= -40.4412-(-40.2187) = -0.2225\ \mathrm{E_h}.
$$
In $\mathrm{kJ\,mol^{-1}}$:
$$
E_{\mathrm{corr}} = -0.2225\times2625.4996
= -5.8417\times10^{2}\ \mathrm{kJ\,mol^{-1}}.
$$
As a percentage of the total:
$$
\frac{0.2225}{40.4412}\times100 = 0.5502\,\%.
$$
Relative to a $350\ \mathrm{kJ\,mol^{-1}}$ C–C bond:
$$
\frac{584.2}{350} = 1.67.
$$

**Answer.** $-0.2225\ \mathrm{E_h} = -584\ \mathrm{kJ\,mol^{-1}}$, which is $0.550\%$
of the total energy and about $1.67$ C–C bond enthalpies.

**Check.** Correlation energies of $0.1$–$0.5\ \mathrm{E_h}$ are typical for first-row
molecules; $0.22\ \mathrm{E_h}$ is in range. The sign is negative because Hartree–Fock
is variational, and the magnitude is chemically decisive even though the percentage is
small.

**Where marks are lost.** Reporting a positive correlation energy, or comparing the
percentage with the bond enthalpy instead of the absolute value.

### 22. Basis extrapolation and CCSD(T) cost **(Multi-step)**

**Strategy.** Use the two-point extrapolation to eliminate $A$, then evaluate at
$X=4$; use the $K^{7}$ scaling for the cost.

**Working.** With $(2.5)^{-3}=0.064000$ and $(3.5)^{-3}=0.023324$,
$$
-0.4120 = E_\infty+0.064000A,
\qquad
-0.4475 = E_\infty+0.023324A.
$$
Subtracting:
$$
-0.0355 = A(0.023324-0.064000) = -0.040676A,
\qquad
A = 0.8727\ \mathrm{E_h}.
$$
Then
$$
E_\infty = -0.4120-0.064000(0.8727) = -0.4679\ \mathrm{E_h}.
$$
For $X=4$, $(4.5)^{-3}=0.010974$:
$$
E_4 = -0.4679+0.8727(0.010974) = -0.4583\ \mathrm{E_h}.
$$
For CCSD(T), the formal scaling is $K^{7}$:
$$
\frac{\mathrm{cost}(2K)}{\mathrm{cost}(K)} = 2^{7}=128,
\qquad
\frac{\mathrm{cost}(3K)}{\mathrm{cost}(K)} = 3^{7}=2187.
$$
If $K$ doubles from $X=3$ to $X=4$ and $X=3$ took $12\ \mathrm{h}$,
$$
t_4 \approx 128\times12\ \mathrm{h} = 1536\ \mathrm{h} \approx 64\ \mathrm{days}.
$$

**Answer.** $A=0.873\ \mathrm{E_h}$, $E_\infty=-0.468\ \mathrm{E_h}$,
$E_4=-0.458\ \mathrm{E_h}$; $128\times$ for doubled $K$, $2187\times$ for tripled $K$;
about $64$ days for $X=4$, which is usually unaffordable without a smaller model, a
local correlation method or an extrapolation from $X=2,3$.

**Check.** The extrapolated $E_\infty$ is below $E_4$, which is below $E_3$ in the sense
of being more negative; the sequence approaches $E_\infty$ monotonically from less
negative values, as a variational method should for the correlation energy in a
systematically convergent basis.

**Where marks are lost.** Using $X^{-3}$ instead of $(X+\tfrac12)^{-3}$, or applying the
$K^{7}$ factor to the energy rather than to the cost.

### 23. Counterpoise correction **(Multi-step)**

**Strategy.** Compute the uncorrected and corrected interaction energies from the
definitions, then take the difference to obtain the BSSE.

**Working.** Uncorrected:
$$
\Delta E_{\mathrm{int}}^{\mathrm{uncorr}}
= -1532.4412-(-766.2050)-(-766.2190)
= -0.01720\ \mathrm{E_h}.
$$
Counterpoise-corrected:
$$
\Delta E_{\mathrm{int}}^{\mathrm{CP}}
= -1532.4412-(-766.2080)-(-766.2210)
= -0.01220\ \mathrm{E_h}.
$$
BSSE:
$$
E_{\mathrm{BSSE}} = (-766.2080-766.2210)-(-766.2050-766.2190)
= -1532.4290+1532.4240 = -0.00500\ \mathrm{E_h}.
$$
In $\mathrm{kJ\,mol^{-1}}$:
$$
\Delta E_{\mathrm{int}}^{\mathrm{uncorr}} = -45.16,
\qquad
\Delta E_{\mathrm{int}}^{\mathrm{CP}} = -32.03,
\qquad
E_{\mathrm{BSSE}} = -13.13.
$$
The corrected binding is weaker because the BSSE artificially stabilised the monomers;
removing it removes $13.1\ \mathrm{kJ\,mol^{-1}}$ of the apparent binding, about $29\%$
of the uncorrected value.

**Answer.** Uncorrected $-0.01720\ \mathrm{E_h}$ ($-45.2\ \mathrm{kJ\,mol^{-1}}$),
CP-corrected $-0.01220\ \mathrm{E_h}$ ($-32.0\ \mathrm{kJ\,mol^{-1}}$), BSSE
$-0.00500\ \mathrm{E_h}$ ($-13.1\ \mathrm{kJ\,mol^{-1}}$). The correction weakens the
binding.

**Check.** $\Delta E^{\mathrm{CP}} = \Delta E^{\mathrm{uncorr}} - E_{\mathrm{BSSE}}
= -0.01720+0.00500 = -0.01220$, as required.

**Where marks are lost.** Adding the BSSE instead of subtracting it, or quoting the
uncorrected value as the binding energy.

### 24. From electronic energy to a reaction free energy **(Multi-step)**

**Strategy.** Sum the thermochemical corrections, convert the result, then apply the
standard-state correction with the correct sign for $\Delta n_{\mathrm{gas}}=-1$.

**Working.** The correction is
$$
\Delta G_{\mathrm{corr}} = \mathrm{ZPE}+\Delta H_{\mathrm{thermal}}-T\Delta S
= 0.0120+0.0075-0.0150 = +0.0045\ \mathrm{E_h}.
$$
Therefore
$$
\Delta G = -0.0450+0.0045 = -0.0405\ \mathrm{E_h}
= -0.0405\times2625.4996 = -106.33\ \mathrm{kJ\,mol^{-1}}
$$
at the 1 atm gas-phase standard state. For the $1\ \mathrm{mol\,dm^{-3}}$ standard
state, the correction is
$$
\Delta n_{\mathrm{gas}}\times7.9 = (-1)(7.9) = -7.9\ \mathrm{kJ\,mol^{-1}},
$$
so
$$
\Delta G(1\ \mathrm{mol\,dm^{-3}}) = -106.33-7.9 = -114.2\ \mathrm{kJ\,mol^{-1}}.
$$
The sign is negative because the reaction consumes two gas molecules and produces one.
The molar volume of an ideal gas at 1 atm and 298 K is about
$24.5\ \mathrm{dm^{3}\,mol^{-1}}$, so a $1\ \mathrm{mol\,dm^{-3}}$ standard state
corresponds to an effective pressure of about $24.5\ \mathrm{atm}$. A reaction that
reduces the number of gas molecules is therefore more strongly favoured in the
$1\ \mathrm{mol\,dm^{-3}}$ standard state. Each gas molecule gains
$RT\ln(24.5)\approx7.9\ \mathrm{kJ\,mol^{-1}}$ of standard chemical potential; with
$\Delta n_{\mathrm{gas}}=-1$ the net change is $-7.9\ \mathrm{kJ\,mol^{-1}}$.

**Answer.** $\Delta G(1\ \mathrm{atm})=-106\ \mathrm{kJ\,mol^{-1}}$;
$\Delta G(1\ \mathrm{mol\,dm^{-3}})=-114\ \mathrm{kJ\,mol^{-1}}$.

**Check.** The correction is small compared with the electronic energy but larger than
the typical accuracy of a DFT reaction energy; it cannot be omitted when the reaction
changes the number of gas molecules.

**Where marks are lost.** Applying the correction with the wrong sign, or adding the
correction without converting the electronic energy to $\mathrm{kJ\,mol^{-1}}$ first.

### 25. Timestep from a vibrational frequency **(Multi-step)**

**Strategy.** Convert the wavenumber to frequency and period, compute the stability
limit $2/\omega$, and compare the timestep with the period.

**Working.** For $\tilde\nu=3000\ \mathrm{cm^{-1}}$,
$$
\nu = c\tilde\nu = (2.99792458\times10^{8}\ \mathrm{m\,s^{-1}})(3000\times10^{2}\ \mathrm{m^{-1}})
= 8.9938\times10^{13}\ \mathrm{Hz}.
$$
The period is
$$
T = \frac{1}{\nu} = 1.1119\times10^{-14}\ \mathrm{s} = 11.12\ \mathrm{fs},
$$
and
$$
\omega = 2\pi\nu = 5.651\times10^{14}\ \mathrm{s^{-1}},
\qquad
\frac{2}{\omega} = 3.539\times10^{-15}\ \mathrm{s} = 3.539\ \mathrm{fs}.
$$
The number of steps per period is $T/\Delta t$:
$$
\Delta t = 1\ \mathrm{fs}:\ 11.1\ \mathrm{steps},
\qquad
\Delta t = 2\ \mathrm{fs}:\ 5.56\ \mathrm{steps}.
$$
A $2\ \mathrm{fs}$ step is below the stability limit of $3.54\ \mathrm{fs}$, so the
integration is stable, but $5.6$ steps per period is below the 10–20 needed for
accuracy: the C–H stretch is poorly resolved and the energy will drift or oscillate on a
timescale that contaminates the observables. Without a constraint, $2\ \mathrm{fs}$ is
not acceptable for a system containing C–H bonds. Constraining the C–H bonds removes the
$3000\ \mathrm{cm^{-1}}$ mode; the fastest remaining motions are heavy-atom stretches
near $1000\ \mathrm{cm^{-1}}$, with a period of about $33\ \mathrm{fs}$, so a
$2\ \mathrm{fs}$ step gives about 17 steps per period and is adequate.

**Answer.** $\nu=8.99\times10^{13}\ \mathrm{Hz}$, $T=11.1\ \mathrm{fs}$,
$2/\omega=3.54\ \mathrm{fs}$; 11.1 and 5.56 steps per period at 1 and 2 fs. A 2 fs step
is stable but inaccurate without constraints; constraining C–H makes it acceptable.

**Check.** The stability limit is not the accuracy limit: $2\ \mathrm{fs}<3.54\
\mathrm{fs}$, yet the resolution is inadequate. This is why the rule of thumb is 10–20
steps per period, not "below $2/\omega$".

**Where marks are lost.** Using $\omega=2\pi c\tilde\nu$ with the wavenumber in
$\mathrm{cm^{-1}}$ without converting to $\mathrm{m^{-1}}$, or treating the stability
limit as the accuracy criterion.

### 26. Temperature, diffusion and RMS speed **(Multi-step)**

**Strategy.** Use the equipartition temperature formula, the Einstein relation for
three-dimensional diffusion, and kinetic theory for the RMS speed; then compare the
implied mean free path with a molecular diameter.

**Working.** (a) With $N=432$ and no constraints,
$$
T = \frac{2K}{3Nk_\mathrm{B}}
= \frac{2(2.68\times10^{-18})}{3(432)(1.380649\times10^{-23})}
= 299.6\ \mathrm{K}.
$$
(b) In three dimensions $\mathrm{MSD}=6Dt$, so
$$
D = \frac{12.0}{6}\ \mathrm{nm^{2}\,ns^{-1}}
= 2.00\ \mathrm{nm^{2}\,ns^{-1}}
= 2.00\times10^{-9}\ \mathrm{m^{2}\,s^{-1}}.
$$
(c) The RMS speed is
$$
v_{\mathrm{rms}} = \sqrt{\frac{3k_\mathrm{B}T}{m}},
\qquad
m = 18.015\,m_\mathrm{u} = 2.9915\times10^{-26}\ \mathrm{kg},
$$
$$
v_{\mathrm{rms}} = \sqrt{\frac{3(1.380649\times10^{-23})(299.6)}{2.9915\times10^{-26}}}
= 6.44\times10^{2}\ \mathrm{m\,s^{-1}}.
$$
The length scale implied by $D\approx\tfrac13 v\lambda$ is
$$
\lambda \approx \frac{3D}{v} = \frac{3(2.00\times10^{-9})}{644}
= 9.3\times10^{-12}\ \mathrm{m} = 0.093\ \mathrm{\AA},
$$
which is far smaller than a molecular diameter (about $3\ \mathrm{\AA}$). The kinetic
theory relation is therefore not quantitatively applicable to a liquid: diffusion in
water is an activated, correlated process, not a dilute-gas random walk. A better
estimate is the Stokes–Einstein relation,
$$
D = \frac{k_\mathrm{B}T}{6\pi\eta r}
\approx \frac{(1.380649\times10^{-23})(299.6)}{6\pi(1.0\times10^{-3})(1.5\times10^{-10})}
\approx 1.5\times10^{-9}\ \mathrm{m^{2}\,s^{-1}},
$$
which is within about $25\%$ of the simulated value.

**Answer.** (a) $300\ \mathrm{K}$; (b) $2.0\times10^{-9}\ \mathrm{m^{2}\,s^{-1}}$;
(c) $644\ \mathrm{m\,s^{-1}}$, implying $\lambda\approx0.09\ \mathrm{\AA}$, so the
gas-phase relation is only an order-of-magnitude check.

**Check.** The Stokes–Einstein estimate is close to the simulated $D$, which is the
appropriate check for a liquid; the gas-phase mean free path is not.

**Where marks are lost.** Using $\mathrm{MSD}=2Dt$ in one dimension for a
three-dimensional simulation, or forgetting to convert $\mathrm{nm^{2}\,ns^{-1}}$ to
$\mathrm{m^{2}\,s^{-1}}$.

### 27. Atom economy, E-factor and convergence **(Multi-step)**

**Strategy.** Apply the atom-economy definition to the balanced equation, then the mass
metrics to the process, then the yield products.

**Working.** The esterification is
$$
\ce{CH3COOH(l) + C2H5OH(l) -> CH3COOC2H5(l) + H2O(l)}.
$$
The atom economy is
$$
\mathrm{AE} = \frac{M_{\mathrm{product}}}{\sum M_{\mathrm{reactants}}}\times100
= \frac{88.106}{60.052+46.069}\times100
= \frac{88.106}{106.121}\times100 = 83.02\,\%.
$$
For $120\ \mathrm{kg}$ of total input and $10.0\ \mathrm{kg}$ of product,
$$
\mathrm{PMI} = \frac{m_{\mathrm{total\ input}}}{m_{\mathrm{product}}}
= \frac{120}{10.0} = 12.0,
\qquad
E = \frac{m_{\mathrm{waste}}}{m_{\mathrm{product}}}
= \frac{120-10.0}{10.0} = 11.0.
$$
The linear route:
$$
Y_{\mathrm{linear}} = 0.88^{8} = 0.3596 \quad (36.0\,\%).
$$
The convergent route:
$$
Y_{\mathrm{conv}} = 0.88^{4}\times0.88^{4}\times0.92
= 0.5997\times0.5997\times0.92 = 0.3309 \quad (33.1\,\%).
$$
The convergent route has one more operation than the linear route (the coupling), so
its overall yield is lower here even though the coupling yield ($92\%$) exceeds the
step yield ($88\%$): the extra operation costs more than the better coupling recovers.
Its advantage is the shorter longest linear sequence, five operations (four steps plus
the coupling) against eight for the linear route, rising to six if a final deprotection
follows the coupling.

**Answer.** AE $=83.0\%$; PMI $=12.0$; E-factor $=11.0$; linear $36.0\%$, convergent
$33.1\%$; the linear route wins on yield, the convergent route on longest linear
sequence.

**Check.** The E-factor and PMI satisfy $\mathrm{PMI}=E+1$ for a single product with no
recycling. Atom economy counts only the product in the numerator while the by-product's
atoms remain in the denominator, which is why the value is below $100\%$.

**Where marks are lost.** Using the product molar mass alone in the numerator and
forgetting the by-product in the denominator, or quoting the convergent route as better
without doing the arithmetic.

### 28. Enantiomeric excess and diastereomeric ratio **(Multi-step)**

**Strategy.** Convert the ratio to a fraction, apply the ee definition, then recompute
after the crystallisation.

**Working.** For $97:3$,
$$
\mathrm{ee} = \frac{97-3}{97+3}\times100 = 94.0\,\%.
$$
Removing half of the minor enantiomer leaves $97:1.5$, so
$$
\mathrm{ee} = \frac{97-1.5}{97+1.5}\times100
= \frac{95.5}{98.5}\times100 = 96.95\,\%.
$$
For a $9:1$ mixture,
$$
\mathrm{dr} = 9:1,
\qquad
\mathrm{de} = \frac{9-1}{9+1}\times100 = 80.0\,\%.
$$
For $99.5:0.5$,
$$
\mathrm{ee} = \frac{99.5-0.5}{99.5+0.5}\times100 = 99.0\,\%.
$$

**Answer.** $94.0\%$; $97:1.5$ and $97.0\%$; dr $9:1$, de $80.0\%$; $99.0\%$ ee.

**Check.** A single crystallisation raises the ee by only about three percentage points
here; reaching $99\%$ by crystallisation alone would require repeated crops and material
loss, which is why improving the asymmetric step is usually preferable.

**Where marks are lost.** Reporting ee as the ratio $97:3$ or as $97\%$, or applying the
crystallisation to the ee rather than to the amounts.

### 29. Activation parameters from two rate constants **(Multi-step)**

**Strategy.** Use the two-temperature Eyring relation with the correct sign, then
compute $\Delta G^{\ddagger}$ from $k$ at 298 K and $\Delta S^{\ddagger}$ from the
difference.

**Working.** The Eyring relation at two temperatures is
$$
\ln\frac{k_2}{k_1}
= -\frac{\Delta H^{\ddagger}}{R}\left(\frac{1}{T_2}-\frac{1}{T_1}\right)
+\ln\frac{T_2}{T_1}.
$$
With $k_2/k_1=4.0$, $\ln4=1.3863$, $\ln(308/298)=0.03301$ and
$1/308-1/298=-1.0895\times10^{-4}\ \mathrm{K^{-1}}$,
$$
\Delta H^{\ddagger}
= -R\frac{\ln(k_2/k_1)-\ln(T_2/T_1)}{1/T_2-1/T_1}
= -8.314\frac{1.3863-0.03301}{-1.0895\times10^{-4}}
= 1.033\times10^{2}\ \mathrm{kJ\,mol^{-1}}.
$$
At 298 K, $k_\mathrm{B}T/h=6.209\times10^{12}\ \mathrm{s^{-1}}$, so
$$
\Delta G^{\ddagger}
= -RT\ln\frac{kh}{k_\mathrm{B}T}
= -(8.314)(298)\ln\left(3.221\times10^{-17}\right)
= 9.409\times10^{1}\ \mathrm{kJ\,mol^{-1}}.
$$
Then
$$
\Delta S^{\ddagger}
= \frac{\Delta H^{\ddagger}-\Delta G^{\ddagger}}{T}
= \frac{(103.27-94.09)\times10^{3}}{298}
= +3.08\times10^{1}\ \mathrm{J\,K^{-1}\,mol^{-1}}.
$$

**Answer.** $\Delta H^{\ddagger}=103\ \mathrm{kJ\,mol^{-1}}$,
$\Delta G^{\ddagger}=94.1\ \mathrm{kJ\,mol^{-1}}$,
$\Delta S^{\ddagger}=+30.8\ \mathrm{J\,K^{-1}\,mol^{-1}}$.

**Check.** A positive $\Delta S^{\ddagger}$ of about $+31\ \mathrm{J\,K^{-1}\,mol^{-1}}$
is consistent with a unimolecular ionisation, where the transition state is looser and
the solvent is released; an associative bimolecular step would give a negative
$\Delta S^{\ddagger}$ because two species combine. The sign therefore supports the
unimolecular assignment.

**Where marks are lost.** Dropping the $\ln(T_2/T_1)$ term, which changes
$\Delta H^{\ddagger}$ by about $2.5\ \mathrm{kJ\,mol^{-1}}$ here, or using the wrong sign
in the Eyring relation.

### 30. Principal component analysis by hand **(Multi-step)**

**Strategy.** Centre, form the covariance matrix, diagonalise the $2\times2$ matrix
analytically, and project the centred data onto the first eigenvector.

**Working.** The data are $(1,2)$, $(2,5)$, $(3,4)$, $(4,7)$, $(5,6)$; the means are
$\bar{x}=3.0$ and $\bar{y}=4.8$. The centred data are
$(-2,-2.8)$, $(-1,0.2)$, $(0,-0.8)$, $(1,2.2)$, $(2,1.2)$.

The covariance matrix with $n-1=4$ is
$$
\mathbf{C} =
\begin{pmatrix}
2.5 & 2.5\\
2.5 & 3.7
\end{pmatrix},
$$
because
$$
S_{xx}=\frac{4+1+0+1+4}{4}=2.5,\quad
S_{yy}=\frac{7.84+0.04+0.64+4.84+1.44}{4}=3.7,\quad
S_{xy}=\frac{5.6-0.2+0+2.2+2.4}{4}=2.5.
$$
The eigenvalues satisfy
$$
\lambda^{2}-6.2\lambda+(2.5)(3.7)-(2.5)^{2}=0
\quad\Longrightarrow\quad
\lambda^{2}-6.2\lambda+3.0=0,
$$
so
$$
\lambda_1=5.671,\qquad \lambda_2=0.529.
$$
The explained variance is
$$
\frac{5.671}{6.200}\times100 = 91.5\,\%,
\qquad
\frac{0.529}{6.200}\times100 = 8.5\,\%.
$$
The first eigenvector follows from
$(2.5-5.671)v_1+2.5v_2=0$, so $v_2=1.268v_1$; normalising gives
$\mathbf{v}_1=(0.619,0.785)$.

The scores are $\mathbf{x}_i\cdot\mathbf{v}_1$ on the centred data:
$$
-3.44,\quad -0.46,\quad -0.63,\quad 2.35,\quad 2.18.
$$
Sample 1 deviates most from the trend. Sample 3 is also slightly below the trend: its
first-component score is negative although its $x$ value is at the mean, because its $y$
value is below the mean.

(d) If the two variables have different units, the variable with the larger numerical
variance dominates the first component even if it is scientifically less important. The
covariance matrix is unit-dependent; standardising each variable to unit variance
(equivalently, using the correlation matrix) is required before PCA when the units
differ.

**Answer.** Means $(3.0,4.8)$; $\mathbf{C}=\begin{pmatrix}2.5&2.5\\2.5&3.7\end{pmatrix}$;
$\lambda_1=5.67$, $\lambda_2=0.529$; $91.5\%$ and $8.5\%$;
$\mathbf{v}_1=(0.619,0.785)$; scores $-3.44,-0.46,-0.63,2.35,2.18$; sample 1 deviates
most. Unscaled variables make the result unit-dependent.

**Check.** The eigenvalues sum to the trace, $5.671+0.529=6.200=2.5+3.7$, and their
product is the determinant, $5.671\times0.529=3.000$. The first score is the largest in
magnitude and negative, consistent with sample 1 being the lowest on both variables.

**Where marks are lost.** Forgetting to centre the data, dividing by $n$ instead of
$n-1$ without saying so, or interpreting the loadings as scores.

---

## Part D — Research-design problems

### 31. Power, randomisation and analysis for a yield comparison **(Multi-step)**

**Strategy.** Treat the comparison as a two-sample test of means with a pre-specified
smallest effect of interest; design the randomisation and blocking before choosing the
analysis.

**Working.** (a) With $\delta=6$ percentage points, $\sigma=4.5$ points,
$z_{0.975}=1.960$ and $z_{0.80}=0.842$,
$$
n = \frac{2(1.960+0.842)^{2}(4.5)^{2}}{6^{2}}
= \frac{2(7.849)(20.25)}{36} = 8.83,
$$
so **9 reactions per condition** (18 in total). The standardised effect is
$d=6/4.5=1.33$. A $t$-based iteration with $t_{0.975,16}=2.120$ gives
$$
n = \frac{2(2.120+0.842)^{2}(20.25)}{36} = 9.87,
$$
so 10 per condition is the safer planning value; the $z$ formula is the planning
approximation and the $t$ iteration is the check.

(b) **Design.** A randomised complete block design: block by day (or by batch of
substrate), and within each block randomise the run order of the two conditions. If
nine runs per condition are affordable, run them across at least three blocks so that
block-to-block variation is separable. Randomise the position in the reactor and the
order of work-up as well, because temperature drift and analyst fatigue are real
nuisance variables.

(c) **Controls.** A negative control with no catalyst establishes that the yield is not
background; a positive control with a benchmark ligand establishes that the assay can
detect the expected effect; a blank (solvent and reagents without substrate) checks the
analytical baseline. If the yield is measured by calibrated GC or HPLC, include an
internal standard and a calibration curve on the same day.

(d) **Analysis plan.** Pre-specify a two-sample $t$-test on the block-adjusted
difference, or an ANCOVA with block as a factor and the pre-specified covariates; report
the difference in percentage points with its 95% confidence interval, the standardised
effect $d=1.33$, and the individual run values. Check the residuals for normality and
homoscedasticity; if the variances differ, use Welch's test. Pre-specify the outlier
rule (none, or a robust rule) and report every excluded run. The primary claim is the
interval, not the p-value.

(e) **Validity.** Internal: confounding by run order, day or reagent lot, controlled by
randomisation and blocking; instrument drift, controlled by running standards
periodically. External: one substrate, one scale and one analyst, so the result
generalises only after replication on a second substrate and a larger scale.

**Answer.** 9 per condition by the $z$ formula (10 after $t$ iteration); randomised
complete block design with day as block; negative, positive and blank controls; a
block-adjusted two-sample test with a 95% CI and $d=1.33$; the main threats are run-order
confounding and over-generalisation from one substrate.

**Check.** The sample size scales as $1/\delta^{2}$: halving the effect to 3 points
would require about 36 per condition, which is why the smallest effect of interest must
be chosen on scientific grounds, not after the data.

**Where marks are lost.** Giving $n=9$ without saying it is per group, omitting the
controls, or proposing a $t$-test on unblocked data when the design is blocked.

### 32. Screening and response-surface optimisation **(Multi-step)**

**Strategy.** Separate screening (which factors matter) from optimisation (where the
optimum lies); choose the resolution by what must be estimated.

**Working.** (a) For five factors, a half-fraction is generated by $E=ABCD$, giving the
defining relation $I=ABCDE$. The design has $2^{5-1}=16$ runs and resolution V, because
the shortest word in $I$ has length 5. Main effects are aliased with four-factor
interactions, and two-factor interactions are aliased with three-factor interactions;
main effects are clear of two-factor interactions. The alias sets are
$\{A,BCDE\}$, $\{B,ACDE\}$, $\{C,ABDE\}$, $\{D,ABCE\}$, $\{E,ABCD\}$ for the main
effects, and $\{AB,CDE\}$, $\{AC,BDE\}$, $\{AD,BCE\}$, $\{AE,BCD\}$, $\{BC,ADE\}$,
$\{BD,ACE\}$, $\{BE,ACD\}$, $\{CD,ABE\}$, $\{CE,ABD\}$, $\{DE,ABC\}$ for the two-factor
interactions.

(b) A resolution III design aliases main effects with two-factor interactions. If an
interaction is present, the main-effect estimate is biased by it, and the experiment
cannot tell whether a factor matters or whether an interaction does. Resolution III is
a screening tool for the assumption of negligible interactions, not a design for
interpreting them.

(c) A **central composite design** for the three most important factors: the $2^{3}=8$
factorial points, $2\times3=6$ axial points at $\pm\alpha$, and 4 centre points, for
18 runs. With $\alpha=(2^{3})^{1/4}=1.682$ the design is rotatable. Alternatively, a
**Box–Behnken** design uses 12 edge midpoints plus 3 centre points (15 runs) and avoids
the extreme corners, which is preferable if the corners are unsafe. The model is
$$
y=\beta_0+\sum_i\beta_i x_i+\sum_i\beta_{ii}x_i^{2}+\sum_{i<j}\beta_{ij}x_ix_j+\varepsilon,
$$
with 10 parameters for three factors (intercept, 3 linear, 3 quadratic, 3 interactions).

(d) **Sample-size logic.** The 10 parameters require at least 10 runs; 18 runs leave 8
residual degrees of freedom, enough to test lack of fit and to estimate pure error from
the centre points. If the first model shows lack of fit, add runs or enlarge the region;
do not simply add parameters. **Analysis plan.** Fit by least squares, inspect residual
plots and lack-of-fit, test the quadratic terms, then locate the stationary point
$$
\mathbf{x}_s=-\tfrac12\mathbf{B}^{-1}\mathbf{b},
$$
where $\mathbf{b}$ is the vector of linear coefficients and $\mathbf{B}$ the matrix of
second-order coefficients. Classify it by the eigenvalues of $\mathbf{B}$: all negative,
maximum; all positive, minimum; mixed signs, saddle, in which case the optimum lies on
the boundary and a ridge or constrained analysis is required. Confirm the predicted
optimum with three replicate runs and report the prediction interval.

**Answer.** $2^{5-1}$ with $I=ABCDE$, 16 runs, resolution V; resolution III is
inadequate because main effects alias two-factor interactions; follow up with an
18-run rotatable CCD (or 15-run Box–Behnken) and a full quadratic model; 8 residual df;
classify the stationary point by the eigenvalues of $\mathbf{B}$.

**Check.** A resolution V design with 16 runs estimates 5 main effects and 10 two-factor
interactions (15 quantities) with one degree of freedom for error only if centre points
are added; the run count is the minimum for the stated model, not a generous one.

**Where marks are lost.** Writing $I=ABCD$ for five factors, confusing resolution with
the number of runs, or fitting a quadratic model without checking lack of fit.

### 33. Distinguishing hydroxybenzoate isomers

**Strategy.** Use the symmetry of the ring as the primary discriminator, then the
aromatic coupling pattern, then the vibrational evidence.

**Working.** **Methyl 4-hydroxybenzoate** has a mirror plane through C1 and C4. Its
eight carbons fall into six environments: the ester carbonyl, C4 (C–OH), C1
(C–CO$_2$Me), C2/C6 (equivalent), C3/C5 (equivalent) and the OCH$_3$. The $^{1}$H
aromatic region is an AA$'$BB$'$ system: two doublets, each integrating to 2H, with
$J\approx8.8\ \mathrm{Hz}$.

**Methyl 2-hydroxybenzoate** has no symmetry: eight distinct carbons and four aromatic
protons, each 1H, with a mixture of ortho (about 8 Hz) and meta (about 2 Hz) couplings
rather than two 2H doublets. **Methyl 3-hydroxybenzoate** also has no symmetry: eight
carbons and four 1H aromatic signals, again with a mixture of ortho and meta couplings.

The IR spectra all show O–H and ester C=O. In the 2-isomer the O–H is intramolecularly
hydrogen-bonded, which tends to sharpen the O–H band, make it less
concentration-dependent, and lower the C=O stretch (towards about $1670\ \mathrm{cm^{-1}}$);
the 4-isomer is intermolecularly hydrogen-bonded, with a broad concentration-dependent
O–H and a C=O near $1680\ \mathrm{cm^{-1}}$. The IR difference is supporting evidence,
not proof.

The **decisive single experiment** is a $^{13}$C/DEPT or HSQC count of unique aromatic
CH environments: the 4-isomer gives two aromatic CH signals (each 2C), while the 2- and
3-isomers give four (each 1C). The $^{1}$H coupling pattern then separates the 2- from
the 3-isomer. No single one-dimensional experiment distinguishes all three, so the
honest answer names the combination; if one experiment must be chosen, HSQC counting is
decisive against the 4-isomer.

What would overturn the assignment: a mixture, or a sample whose symmetry is broken by
aggregation or by a chiral environment. An authentic sample or a crystal structure
settles the question.

**Answer.** 4-isomer: 6 $^{13}$C signals, two 2H doublets, intermolecular H-bond;
2-isomer: 8 signals, four 1H multiplets, intramolecular H-bond; 3-isomer: 8 signals,
four 1H multiplets. HSQC counting is decisive against the 4-isomer; the $^{1}$H pattern
separates 2 from 3.

**Check.** The 4-isomer's two 2H doublets require a mirror plane; the 2- and 3-isomers
cannot have one. The count of $^{13}$C signals therefore follows from symmetry alone,
independent of chemical-shift prediction.

**Where marks are lost.** Claiming that the IR alone distinguishes the isomers, or
forgetting that the 3-isomer is also unsymmetrical.

### 34. Critical appraisal of a hypothetical abstract

**Strategy.** Separate claim, evidence, validity, reporting and interpretation; tie every
criticism to something absent rather than to a suspicion about the authors.

**Working.** The abstract is hypothetical and cites no real publication. Five specific
weaknesses:

1. **No catalyst-free control.** Without a reaction run under the same conditions but
   without the palladium complex, a background or metal-leaching contribution cannot be
   excluded. The evidence that would resolve it is the control yield and a hot-filtration
   or mercury-poisoning test.
2. **"Solvent-free" is asserted, not demonstrated.** A 98% isolated yield on 0.5 mmol
   requires a work-up, which normally uses solvent; the procedure must state every
   liquid used, including eluents. The evidence is a full mass balance and a solvent
   inventory.
3. **The recycle claim lacks mass balances and metal analysis.** "Five times without
   loss of activity" could reflect fresh catalysis by leached palladium. The evidence is
   the recovered-catalyst mass and composition, ICP-MS of the filtrate after each cycle,
   and a hot-filtration test.
4. **"Superior to conventional protocols" is not a comparison.** No matched protocol, no
   reference, no same-substrate comparison under the same conditions. The evidence is a
   side-by-side run with a matched benchmark protocol and a stated criterion.
5. **"Scalable" and "green" are unsupported.** 0.5 mmol is not a scale demonstration, and
   no E-factor, PMI, solvent recovery or energy per mole is reported. The evidence is a
   100 mmol run with isolated yield, plus the green metrics over a stated boundary.

Two further reporting failures are worth naming: no characterisation or purity data, and
no $n$ or uncertainty on the 98%. The 98% figure cannot be audited without the isolated
mass and the identity of the product.

**Corrected claim.** "On a 0.5 mmol scale, 10 mol% of the new complex converted
4-bromoanisole and phenylboronic acid to 4-methoxybiphenyl in 98% isolated yield after
5 min at 120 °C under microwave irradiation; the work-up solvent was not reported, and
no claim about recycling, scalability or environmental benefit is supported by the data
presented."

**Answer.** The five weaknesses are the missing control, the unsubstantiated
solvent-free claim, the unsupported recycle claim, the unmatched comparison and the
unsupported scale/green claims; each is resolved by a specific control or metric, and the
corrected claim is restricted to what was measured.

**Check.** Every criticism is tied to an absent item, not to an allegation. The yield
itself is arithmetically possible; the problem is the derived claims, which is the
common pattern in overstated abstracts.

**Where marks are lost.** Writing a list of adjectives ("vague", "overstated") without
naming the missing evidence, or proposing a new experiment that does not address the
specific claim.

### 35. A reproducible computational workflow **(Multi-step)**

**Strategy.** Treat reproducibility as provenance: every number must be traceable to an
input, a code version and a parameter set.

**Working.** (a) **Archive.** For each stationary point: Cartesian coordinates, charge,
multiplicity, conformer identifier, electronic energy, zero-point energy, frequencies
(including imaginary frequencies), and the optimisation convergence criteria. For the
method: functional name and version, dispersion correction and damping, basis set and
version, ECP and relativistic treatment, integration grid, SCF convergence and DIIS
settings, and the software name, version and build. For thermochemistry: temperature,
pressure, standard state, rigid-rotor/harmonic-oscillator or quasi-RRHO treatment,
scaling factor, symmetry number and the treatment of low-frequency modes. For solvation:
the model, cavity parameters and solvent. Archive the inputs and outputs, not only the
extracted numbers.

(b) **Version control and environment.** Put scripts, inputs and the manuscript in Git;
record the commit hash in the paper and supporting information; tag the published
version. Pin the language, libraries and software with a lockfile or a container image
identified by digest. Record every random seed: conformer search, initial velocities,
cross-validation folds, bootstrap resamples and clustering initialisation. Add regression
tests that reproduce a known energy or barrier for a small molecule, and unit tests for
parsers and unit conversions; run them in continuous integration.

(c) **FAIR deposit.** Findable, Accessible, Interoperable and Reusable: a persistent
identifier (DOI), rich metadata (README, data dictionary, units, software versions), an
open licence, and community formats (xyz, csv, json, standard output files). Deposit the raw outputs and the analysis scripts, not
only the processed table. State any access restriction explicitly.

(d) **Failure mode.** All files are present but the reported conformer was selected by
an unrecorded manual inspection, or the single-point energy used a different grid from
the optimisation, or the thermochemical scaling factor was chosen by the authors and not
recorded. The provenance of the reported number is then missing, and the result cannot
be reproduced even though every file exists. "Available on request" is not a substitute
for a deposit.

**Answer.** Archive geometry, method, grid, dispersion, solvation and thermochemistry
for every stationary point; use Git, pinned environments, recorded seeds and regression
tests; deposit under FAIR with raw outputs and scripts; the residual failure mode is
missing provenance for the chosen structure or parameter.

**Check.** A reader with none of the authors' intuition should be able to regenerate
every table from the deposit. If a step requires a private decision, that decision is
part of the data.

**Where marks are lost.** Listing file formats without saying what must be in them, or
treating "data available on request" as reproducibility.

### 36. Authorship, misconduct and conflict of interest **(Multi-step)**

**Strategy.** Apply the four ICMJE criteria to each contributor, then classify the two
proposals against the FFP/QRP definitions.

**Working.** The ICMJE criteria are: (1) substantial contribution to conception/design
or to acquisition, analysis or interpretation; (2) drafting or critical revision for
important intellectual content; (3) final approval of the version to be published; and
(4) agreement to be accountable for all aspects of the work.

- **Group leader.** Funding and "commented on the draft" are not enough by themselves.
  If the comments were substantive critical revision and the leader accepts
  accountability, the leader is an author; if they were editorial, the leader is
  acknowledged. Funding acquisition alone is explicitly insufficient.
- **Postdoc.** Designed the study and wrote the first draft: author.
- **PhD student.** Performed the experiments; if also involved in analysis or
  interpretation and approves the final version, author. Acquisition alone can satisfy
  criterion 1, but criteria 2–4 must also be met; in practice the student should be
  involved in revision.
- **Collaborator.** Supplied the ligand and discussed the results. If the discussion
  contributed to interpretation and the collaborator revised the manuscript, author;
  if only the material was supplied, acknowledgment with permission.
- **Technician.** Ran the NMR spectra. Acknowledgment unless the technician also
  contributed to design or interpretation.
- **Industrial partner.** Provided a compound under confidentiality. Authorship requires
  accountability and access to the data, which a confidentiality agreement may prevent.
  If the partner cannot meet all four criteria, acknowledge and declare the relationship.

A **CRediT** statement could read: conceptualisation (postdoc, group leader);
investigation (PhD student); resources (collaborator, industrial partner); formal
analysis (postdoc, PhD student); supervision (group leader); project administration
(group leader); writing – original draft (postdoc); writing – review and editing (all
authors); funding acquisition (group leader). A name with no role stands out, which is
the point of the taxonomy.

**Gift authorship risk:** the department head, who provided no contribution. **Ghost
authorship risk:** a professional writer or the partner's scientist who drafted text but
is not named. Both are QRPs; the correct response is to agree authorship in writing
before the work begins and to record contributions.

**The two proposals.** Adding the department head is **gift authorship**, a questionable
research practice that misallocates credit and dilutes accountability; the correct
response is to refuse, to explain the ICMJE criteria, and to escalate if necessary.
Removing a data point that weakens a patent claim is **falsification**, because data are
suppressed so that the record misrepresents the work; it is research misconduct, not a
QRP. The correct response is to refuse, retain the full dataset, report it, and disclose
the request to the institution's research integrity officer. If the partner insists, the
collaboration should be terminated or the manuscript withdrawn.

**Conflict of interest.** Declare the industrial partnership, any financial interest
(consultancy, equity, patents), the confidentiality agreement and the partner's role.
Manage it by independent analysis of the data, no sponsor control of the conclusions,
data access for all authors, and a publication-rights clause. A generic "no conflict"
statement is false if these relationships exist.

**Answer.** Postdoc and PhD student are authors; the group leader and collaborator are
authors only if they meet criteria 2–4; the technician is acknowledged; the industrial
partner is acknowledged and declared unless it can accept accountability and data
access. The department-head proposal is gift authorship; the data-deletion request is
falsification. Declare and manage the industrial COI.

**Check.** Every authorship decision turns on what the person did, not on seniority or
funding. The misconduct classification turns on whether data were invented, altered or
suppressed, not on whether the motive was commercial.

**Where marks are lost.** Making the group leader an author because of funding, or
classifying gift authorship as fabrication.

### 37. Binding free-energy study for ten analogues **(Multi-step)**

**Strategy.** Design the calculation around the decision it must support: a ranking of
ten analogues with an uncertainty smaller than the differences that matter, validated
against controls.

**Working.** (a) **Force-field validation.** Three layers: pure-liquid properties
(density, heat of vaporisation, compressibility, dielectric constant); solvation free
energies for a set spanning the ligand chemistry; and conformational or binding
benchmarks against experimental data. Validate at least two force fields or charge
models, because the force field is usually the dominant systematic error.

(b) **Ligand parameterisation.** Use a transferable force field (GAFF, CGenFF or OPLS)
with RESP or equivalent charges fitted to a quantum electrostatic potential; check the
protonation state at the experimental pH; validate the torsional profiles against
quantum calculations. Record every parameter and charge.

(c) **System.** A truncated octahedron or dodecahedron with at least $1.2\ \mathrm{nm}$
between the solute and the box edge; explicit water (TIP3P, OPC or equivalent);
$0.15\ \mathrm{mol\,dm^{-3}}$ salt; PME for electrostatics with a $1.0$–$1.2\ \mathrm{nm}$
real-space cutoff; a $2\ \mathrm{fs}$ timestep with SHAKE/LINCS on bonds involving
hydrogen, or $4\ \mathrm{fs}$ with hydrogen mass repartitioning if validated; a Langevin or
Bussi–Donadio–Parrinello thermostat and a Parrinello–Rahman or Monte Carlo barostat.

(d) **Enhanced sampling.** Alchemical relative binding free energies along a
thermodynamic cycle, with 12–20 windows and 5–10 ns per window, or umbrella sampling
along a physical coordinate if the alchemical path is problematic. Run 3–5 independent
replicates with different seeds. Check overlap, hysteresis and the absence of
restraints at the endpoints. State the cycle and the standard state.

(e) **Controls.** A positive control with a measured affinity, a negative control with a
truncated or chemically similar inactive analogue, and a self-perturbation that should
give $\Delta\Delta G=0$. These controls test the protocol, not the hypothesis.

(f) **Error analysis.** Block averaging with blocks longer than the correlation time;
bootstrap over independent replicates; report the standard error of the mean. Separate
the statistical error from the systematic contributions: force field (spread between two
force fields), finite-size, cutoff, protonation, sampling and the alchemical path.
Combine in quadrature only when the contributions are independent; otherwise report the
budget. A free-energy difference quoted to $0.1\ \mathrm{kJ\,mol^{-1}}$ without a budget
is not a result.

(g) **Decision rule.** Claim that an analogue is more potent only if the computed
$\Delta\Delta G$ is negative by more than the combined uncertainty, if the ranking is
consistent across replicates and force fields, and if the positive and negative controls
rank correctly. Pre-specify the threshold (for example, $1\ \mathrm{kcal\,mol^{-1}}$ or
the propagated uncertainty, whichever is larger), report the full ranking with intervals,
and do not interpret differences smaller than the force-field spread.

**Sample-size logic.** Run a pilot with three replicates to estimate the
between-replicate standard deviation $s$. Choose the number of replicates so that the
standard error $s/\sqrt{n}$ is at most one-third of the smallest $\Delta\Delta G$ that
would change the decision. With $s=0.5\ \mathrm{kcal\,mol^{-1}}$ and a target difference
of $1\ \mathrm{kcal\,mol^{-1}}$, the minimum is $n\ge3$ replicates; use four for a
margin. The number of analogues does not substitute for replication.

**Answer.** A validated two-force-field protocol with explicit solvent, PME, constrained
2 fs dynamics, alchemical relative free energies with 12–20 windows and 3–5 replicates,
positive/negative/self controls, a full error budget, and a pre-specified decision rule
based on the combined uncertainty.

**Check.** If the positive control is not ranked above the negative control, the protocol
has failed regardless of the analogue ranking. If the two force fields disagree by more
than the claimed effect, the claim is not supported.

**Where marks are lost.** Quoting a single replicate to $0.1\ \mathrm{kcal\,mol^{-1}}$,
omitting the positive and negative controls, or treating the force-field error as
statistical noise.

### 38. Closed photoredox cycle versus radical chain **(Multi-step)**

**Strategy.** Choose observables for which the two mechanisms predict qualitatively
different behaviour, and combine them because no single test is decisive.

**Working.** (a) **Quantum yield.** Measure with a chemical actinometer. A closed cycle
converts at most one molecule per absorbed photon, so $\Phi\le1$; a chain can give
$\Phi\gg1$. A value near 1 is not decisive, because a short chain can also give about 1;
a value above 1 is decisive for a chain.

(b) **Rate law and catalyst loading.** In a closed cycle the rate is first order in
catalyst at low loading and saturates at high loading. In a chain the catalyst may be
regenerated and the rate can be zero or fractional in catalyst. Vary the loading over a
tenfold range and plot $\log(\mathrm{rate})$ against $\log[\mathrm{catalyst}]$: slope 1
supports a closed cycle, while a slope near 0 or a fractional order supports a chain.
Check that the catalyst is stable over the range.

(c) **Radical trap.** Both mechanisms can be inhibited, so a trap alone is not
discriminating. Use a trap with a known rate constant, vary its concentration, and
measure the product and trapped-adduct yields. A chain is more sensitive because the
trap competes with propagation; a closed cycle may be unaffected if the trap does not
quench the excited state. A trap that changes the product distribution at low conversion
is perturbing the mechanism.

(d) **Light on/off.** A closed cycle stops within the excited-state lifetime (nanoseconds
to microseconds) when the light is switched off. A chain can persist for seconds or
minutes, producing a "dark burst" of conversion. Measure conversion in the dark after a
short illumination period; a significant dark burst supports a chain.

(e) **Electron-transfer quencher.** A quencher that oxidises or reduces the excited
catalyst suppresses a closed cycle. A chain may be less affected if the chain carrier is
an organic radical rather than the catalyst. Use Stern–Volmer quenching to show that the
quencher actually interacts with the excited state.

**Decision rule.** $\Phi>1$ is conclusive for a chain. If $\Phi\approx1$, require at
least two of: catalyst-order zero, a dark burst, and insensitivity to a quencher. A
single negative trap result is not evidence for a closed cycle.

**Perturbation.** The trap can quench the excited state, alter the redox potentials, or
consume the chain carrier; the quencher can change the ionic strength or the pH. Run the
trap and quencher experiments at low conversion, with matched controls, and check that
the catalyst's absorption spectrum and the product selectivity are unchanged.

**Answer.** Use quantum yield as the primary discriminator, supported by catalyst-order,
dark-burst and quenching experiments; $\Phi>1$ proves a chain, while $\Phi\approx1$
requires the supporting tests. The main risk is that the probe perturbs the mechanism.

**Check.** A chain mechanism must also explain the catalyst's role: if the catalyst is
only an initiator, its loading dependence will be weak, and a radical initiator should
reproduce the reaction in the dark.

**Where marks are lost.** Treating a radical trap as decisive, or measuring the quantum
yield without an actinometer and calling a relative yield a quantum yield.

---

## Part E — Advanced problems

### 39. A multireference decision from diagnostics **(Multi-step)**

**Strategy.** Compare each diagnostic with its threshold, then decide whether the
qualitative picture (one determinant) is defensible before choosing a method.

**Working.** (a) The T1 diagnostic is $0.045$, above the chapter's main-group threshold
of $0.02$ (and below the transition-metal threshold of $0.05$, but this is a main-group
molecule). The leading-determinant weight is $0.82$, below the $0.9$ threshold at which
a single-reference treatment becomes suspect. The %TAE is $8\%$, above "a few per cent",
so a large fraction of the atomisation energy comes from post-Hartree–Fock correlation.
The T1 and the leading weight point to static correlation; the %TAE reinforces the need
for a high-level treatment but does not by itself prove static correlation, because it
also counts dynamic correlation.

(b) A single-reference CCSD(T) treatment is **not defensible without a multireference
check**. The T1 and the weight both warn of static correlation; CCSD(T) may still give a
plausible number, but the number is not trustworthy because the reference is poor.

(c) The active space must contain the orbitals involved in the near-degeneracy. The
procedure is: inspect the natural-orbital occupations; include orbitals with occupation
between about $0.02$ and $1.98$; start with the smallest chemically meaningful space
(2 electrons in 2 orbitals for a single bond, 6 electrons in 6 orbitals for a $\pi$
system, 8 electrons in 6 orbitals for a metal–oxo unit); check that the leading weight
rises above $0.9$ and that the results are stable when the space is enlarged. Then add
dynamic correlation with CASPT2 or NEVPT2; use MRCI with the Davidson correction as a
check if the property demands it.

(d) Two ways the calculation could still fail. First, the active space may be too small:
the leading weight remains low, the occupation numbers are still far from 0 and 2, and
the property is wrong even though the method is multireference. Second, the perturbative
treatment may fail: intruder states in CASPT2, a poor zeroth-order Hamiltonian, or a
near-degeneracy between the state of interest and a state outside the active space. A
third risk is that the basis set or relativistic correction is inadequate; a fourth is
that the property requires state averaging or a different electronic state.

**Answer.** T1 $0.045$ and weight $0.82$ indicate strong static correlation; a
single-reference treatment is not defensible. Use CASSCF in the active space containing
the near-degenerate orbitals, then CASPT2/NEVPT2, and check that the weight rises and the
result is stable to enlarging the space.

**Check.** A successful CASSCF should show a leading weight above $0.9$ and natural
occupations close to 0 or 2 for the inactive orbitals. If the weight remains low, the
active space is wrong, not the method.

**Where marks are lost.** Treating the T1 diagnostic as a yes/no test, or choosing
CASSCF without adding dynamic correlation and quoting a barrier.

### 40. Isodesmic error cancellation **(Multi-step)**

**Strategy.** Count the bonds broken and formed in each reaction, apply the per-bond
error model, and compare the totals.

**Working.** (a) For the direct reaction
$$\ce{C6H5CH3 + H2 -> C6H6 + CH4},$$
the bond changes are: one C–C bond broken (toluene), one H–H bond broken, and two C–H
bonds formed (one on benzene, one on methane). Under the model,
$$
\Delta E_{\mathrm{err}} = (+40) + (+10) + 2(-15) = +20\ \mathrm{kJ\,mol^{-1}}.
$$
(b) For the isodesmic reaction
$$\ce{C6H5CH3 + CH4 -> C6H6 + C2H6},$$
the bond counts are identical on both sides: one C–C bond and twelve C–H bonds. Writing
the changes explicitly, one C–C is broken
$(+40)$ and one formed $(-40)$; four C–H are broken $(4\times+15=+60)$ and four formed
$(4\times-15=-60)$; there is no H–H change. The total is
$$
(+40)+(-40)+(+60)+(-60)=0.
$$
The per-bond errors cancel because each bond type appears with both signs.

(c) In practice the error is not a pure per-bond function. It depends on hybridisation,
charge, ring strain, conjugation, dispersion and the local environment, so an isodesmic
reaction that conserves the total count of each bond type can still leave a residual
that depends on the structural change. The diagnostic is to compute the same reaction
with two functionals with different error profiles and with a homodesmotic scheme; if
the isodesmic and homodesmotic results differ by more than the expected error, the
cancellation is incomplete. A plot of the error against a bond-type descriptor, or a
comparison with a high-level benchmark on a subset, makes the residual visible.

(d) A **homodesmotic** reaction conserves not only the number of bonds of each type but
also the hybridisation of each carbon (and often the number of C–H bonds on each type of
carbon). For a substituted benzene this matters because the sp$^{2}$/sp$^{3}$ character
of the substituent and the ring changes the correlation energy; an isodesmic reaction
that conserves only the total bond count can leave a hybridisation-dependent residual.

**Answer.** Direct error $+20\ \mathrm{kJ\,mol^{-1}}$; the isodesmic reaction cancels it
exactly under the model; in practice the cancellation is incomplete because the error
depends on environment and hybridisation; a homodesmotic reaction additionally conserves
carbon hybridisation.

**Check.** The direct reaction changes the number of C–H and H–H bonds, so it cannot
cancel; the isodesmic reaction changes none of the net bond counts, so it must cancel
under a per-bond model. The logic is the design principle, not a numerical coincidence.

**Where marks are lost.** Counting the bonds incorrectly, or claiming that error
cancellation makes a low-level method "accurate" rather than "consistent".

### 41. Benchmark statistics and functional choice **(Multi-step)**

**Strategy.** Compute the four statistics, then separate the average performance from
the worst case.

**Working.** (a) For A:
$$
\bar{e}=0.0,\quad \mathrm{MAE}=4.5,\quad
\mathrm{RMSE}=\sqrt{\frac{16+36+4+64+25+9+49+1}{8}}=5.05,\quad \max|e|=8.
$$
For B:
$$
\bar{e}=+1.5,\quad \mathrm{MAE}=2.25,\quad
\mathrm{RMSE}=\sqrt{\frac{1+1+4+4+0+1+4+81}{8}}=3.46,\quad \max|e|=9.
$$
For C:
$$
\bar{e}=-0.75,\quad \mathrm{MAE}=6.25,\quad
\mathrm{RMSE}=\sqrt{\frac{100+9+16+144+36+4+64+25}{8}}=7.05,\quad \max|e|=12.
$$
(b) For a **set of similar reactions**, B is preferable: it has the lowest MAE and RMSE,
and its mean bias of $+1.5\ \mathrm{kJ\,mol^{-1}}$ is systematic and can be corrected or
tolerated. For a **single reaction energy**, the choice is conditional. A has a smaller
maximum error (8 versus 9) and zero mean bias, so A is safer if the target could belong
to the class of B's outlier. If the target is a typical member of the set, B is still
better on average. The honest answer states the condition rather than choosing
unconditionally.

(c) The maximum error changes the recommendation because a study reports one number, not
an ensemble average. B's outlier of $+9\ \mathrm{kJ\,mol^{-1}}$ may correspond to a
transition state, a spin-state problem or a different bonding motif; if the target is in
that class, B's average performance is irrelevant. Request the identity of the outlier,
the per-reaction errors, the reference values and their uncertainties, the error
distribution, and a breakdown by reaction class; also ask whether the outlier was
included in the MAE and whether a robust statistic (median absolute error) was reported.

**Answer.** A: mean $0.0$, MAE $4.5$, RMSE $5.05$, max $8$. B: mean $+1.5$, MAE $2.25$,
RMSE $3.46$, max $9$. C: mean $-0.75$, MAE $6.25$, RMSE $7.05$, max $12$. B for a set of
similar reactions; A or B for a single reaction depending on whether the target belongs
to the outlier class.

**Check.** The RMSE is always at least the MAE, and both are at least the absolute mean;
the values satisfy $5.05\ge4.5\ge0$, $3.46\ge2.25\ge1.5$ and $7.05\ge6.25\ge0.75$.

**Where marks are lost.** Choosing on MAE alone without reporting the maximum, or
treating the mean signed error as a measure of accuracy.

### 42. Jarzynski estimate and its convergence **(Multi-step)**

**Strategy.** Compute the exponential average, convert to a free energy, then compare
with the mean work and examine the effect of an added high-work pull.

**Working.** (a) With $RT=2.478\ \mathrm{kJ\,mol^{-1}}$,
$$
\left\langle e^{-W/RT}\right\rangle
= \frac13\left(e^{-18/2.478}+e^{-20/2.478}+e^{-23/2.478}\right)
= \frac13\left(6.99\times10^{-4}+3.13\times10^{-4}+9.29\times10^{-5}\right)
= 3.683\times10^{-4}.
$$
$$
\Delta F = -RT\ln\left(3.683\times10^{-4}\right)
= 19.59\ \mathrm{kJ\,mol^{-1}}.
$$
The mean work is $\langle W\rangle=20.33\ \mathrm{kJ\,mol^{-1}}$, so the dissipation is
$0.74\ \mathrm{kJ\,mol^{-1}}$.

(b) Adding $W=30\ \mathrm{kJ\,mol^{-1}}$:
$$
\left\langle e^{-W/RT}\right\rangle
= \frac14\left(6.99\times10^{-4}+3.13\times10^{-4}+9.29\times10^{-5}+5.50\times10^{-6}\right)
= 2.776\times10^{-4},
$$
$$
\Delta F = -RT\ln\left(2.776\times10^{-4}\right)
= 20.29\ \mathrm{kJ\,mol^{-1}},
$$
and $\langle W\rangle=22.75\ \mathrm{kJ\,mol^{-1}}$, so the apparent dissipation rises to
$2.46\ \mathrm{kJ\,mol^{-1}}$. The estimate rises slightly, but this is not evidence of
convergence: adding a high-work pull dilutes the exponential average, and the direction
of the change depends on the sample. The finite-sample bias remains downward because the
rare low-work tail is undersampled.

(c) The estimator is reliable when there are many independent pulls, the work
distribution has sufficient overlap with the exponential weight, the pulling is not too
fast, and the protocol is identical for every pull. Bidirectional estimators (Crooks,
Bennett acceptance ratio) use both forward and reverse work and converge much better,
because they use the overlap of the two distributions instead of relying on the rare
low-work tail of one.

**Answer.** (a) $\langle W\rangle=20.33$, $\Delta F=19.59\ \mathrm{kJ\,mol^{-1}}$;
(b) with the fourth pull, $\Delta F=20.29\ \mathrm{kJ\,mol^{-1}}$, still biased low;
(c) reliable with many pulls and good overlap, and bidirectional estimators are preferred.

**Check.** The second law requires $\langle W\rangle\ge\Delta F$; both estimates satisfy
it, and the gap is the dissipated work. A negative dissipation would signal an error.

**Where marks are lost.** Averaging the work values and calling the mean the free
energy, or using $\Delta F=-RT\ln\langle W\rangle$ instead of the exponential average.

### 43. Retrosynthesis and green metrics for a biaryl **(Multi-step)**

**Strategy.** Disconnect the strategic bond first, then compare the two routes on atom
economy and on the process metrics, stating the convention for the base.

**Working.** (a) **Suzuki–Miyaura.** Disconnect the biaryl C–C bond to give a
4-methoxyphenyl synthon and a phenyl synthon; the reagents are 4-bromoanisole and
phenylboronic acid. The strategic bond is the new C(sp$^{2}$)–C(sp$^{2}$) bond.
**Buchwald–Hartwig.** Disconnect the C–N bond to give a 4-methoxyphenyl synthon and a
phenylamine synthon; the reagents are 4-bromoanisole and aniline. The strategic bond is
the new C(sp$^{2}$)–N bond.

(b) Suzuki:
$$
\mathrm{AE} = \frac{184.24}{187.04+121.93}\times100 = 59.63\,\%.
$$
Buchwald–Hartwig, including the base:
$$
\mathrm{AE} = \frac{199.25}{187.04+93.13+96.10}\times100 = 52.95\,\%.
$$
Excluding the base gives $199.25/(187.04+93.13)=71.1\%$, so the convention matters. The
base is a stoichiometric reactant and should be included in a like-for-like comparison;
the boron by-product and the base-derived waste are both real.

(c) PMI:
$$
\mathrm{PMI} = \frac{150}{12.0} = 12.5,
\qquad
E = \frac{150-12.0}{12.0} = 11.5.
$$

(d) **Medicinal chemistry:** the Suzuki route, because boronic acids are commercially
available and the coupling is modular for analogue synthesis; the biaryl is assembled in
one step and the methoxy group is tolerated. **Process:** the Suzuki route on the stated
metrics (higher atom economy, one C–C bond-forming step, and a base loading that can be
optimised), provided the boronic acid is available at scale and the palladium can be
removed to the specification. The Buchwald–Hartwig route is the fallback
if the aniline is significantly cheaper or the boronic acid is unstable; it has lower
atom economy and produces NaBr and tert-butanol, so its E-factor is likely higher unless
the base is recycled. On safety, the Suzuki route avoids handling aniline (toxic and
air-sensitive) and a strong alkoxide base at scale; the Buchwald–Hartwig route requires
both. The recommendation should state the criteria, not just the name.

**Answer.** Suzuki: biaryl C–C disconnection; AE $59.6\%$. Buchwald–Hartwig: C–N
disconnection; AE $53.0\%$ including the base ($71.1\%$ excluding it). PMI $12.5$,
E-factor $11.5$. Suzuki for medicinal chemistry; Suzuki for process if the boronic acid
is available, with Buchwald–Hartwig as a cost-driven fallback.

**Check.** The two atom economies differ by about seven percentage points, which is
smaller than the difference in the conventions; stating the convention is therefore as
important as the number. The PMI and E-factor satisfy $\mathrm{PMI}=E+1$ for a single
product.

**Where marks are lost.** Comparing one route's AE including the base with the other's
excluding it, or recommending a route on AE alone without considering cost, metal
removal and safety.

### 44. Hammett analysis and the kinetic isotope effect **(Multi-step)**

**Strategy.** Compute $\rho$ from each substituent, interpret the sign, then compare the
observed KIE with the semiclassical primary maximum.

**Working.** (a) From $\log(k/k_0)=\rho\sigma$:
$$
\rho_1 = \frac{\log_{10}(3.2)}{-0.27} = \frac{0.50515}{-0.27} = -1.871,
\qquad
\rho_2 = \frac{\log_{10}(0.35)}{0.23} = \frac{-0.45593}{0.23} = -1.982.
$$
The mean is $\rho=-1.93$.

(b) The negative sign means that electron-donating substituents accelerate the reaction,
so positive charge develops at the reaction centre in the transition state. The magnitude
is large (about $-1.9$), consistent with an ionisation or an electrophilic attack with
substantial charge separation, not with a nucleophilic attack on a neutral substrate
(which would give a positive $\rho$). The likely rate-determining step is the
ionisation/cleavage rather than the attack of the nucleophile.

(c) For a KIE of $1.08$,
$$
\Delta\Delta G^{\ddagger} = -RT\ln(1.08)
= -(8.314)(298)\ln(1.08)/1000
= -0.191\ \mathrm{kJ\,mol^{-1}}.
$$
A primary C–H cleavage would give about $7.8$ at 298 K, corresponding to
$\Delta\Delta G^{\ddagger}\approx-5.08\ \mathrm{kJ\,mol^{-1}}$. The observed $1.08$ is far
too small, so C–H cleavage is **not** rate-limiting. The small normal effect is consistent
with an $\alpha$-secondary effect or a change in hybridisation at the benzylic carbon.

(d) For a C–H stretch at $2900\ \mathrm{cm^{-1}}$,
$$
\Delta\mathrm{ZPE} = \tfrac12 hc\left(2900-\frac{2900}{\sqrt2}\right)
= \tfrac12(0.011962)(2900-2051)
= 5.08\ \mathrm{kJ\,mol^{-1}},
$$
$$
\frac{k_\mathrm{H}}{k_\mathrm{D}} = \exp\left(\frac{5.08}{2.478}\right)
= e^{2.05} = 7.77.
$$
The observed $1.08$ is far below $7.8$, so a primary effect is excluded.

**Answer.** $\rho=-1.87$ and $-1.98$, mean $-1.93$; negative $\rho$ indicates positive
charge development in the transition state; $\Delta\Delta G^{\ddagger}=-0.191\
\mathrm{kJ\,mol^{-1}}$, so C–H cleavage is not rate-limiting; the primary maximum is
$7.77$, confirming that the observed $1.08$ is secondary.

**Check.** A primary KIE near $7.8$ would require the C–H bond to break in the
rate-determining step, which is inconsistent with the large negative $\rho$ for an
ionisation mechanism; the two pieces of evidence agree.

**Where marks are lost.** Using $\ln$ instead of $\log_{10}$ in the Hammett equation, or
interpreting a KIE of $1.08$ as proof that no C–H bond is involved anywhere in the
mechanism (it is only excluded from the rate-determining step).

### 45. Complete elucidation of an unknown **(Multi-step)**

**Strategy.** Formula first, then degrees of unsaturation, then the functional groups from
IR, then the symmetry and coupling pattern from NMR, then assembly and validation.

**Working.**

**Step 1 — Formula.** For $\ce{[M+H]+}$ at $m/z$ 153.0549, the calculated value
for $\ce{C8H9O3+}$ is $153.0546$, a difference of $+1.8\ \mathrm{ppm}$, inside a
$5\ \mathrm{ppm}$ window. The neutral molecule is $\ce{C8H8O3}$. The double-bond
equivalent is
$$
\mathrm{DBE} = 8-\frac{8}{2}+1 = 5:
$$
one aromatic ring (4) plus one carbonyl (1).

**Step 2 — Functional groups.** The broad IR band at $3310\ \mathrm{cm^{-1}}$ is an O–H
stretch; the band at $1680\ \mathrm{cm^{-1}}$ is a conjugated ester carbonyl (a saturated
ester would be at $1735$–$1750$); the bands at $1605$ and $1510\ \mathrm{cm^{-1}}$ are
aromatic; the strong bands at $1250$ and $1100\ \mathrm{cm^{-1}}$ are C–O stretches of
the ester.

**Step 3 — Symmetry and coupling.** The $^{1}$H spectrum shows two doublets, each 2H,
with $J=8.8\ \mathrm{Hz}$. This is an AA$'$BB$'$ pattern of a **para-disubstituted**
ring. The $^{13}$C spectrum shows six signals for eight carbons: $167.2$ (ester C=O),
$160.1$ (C–OH), $132.0$ (2C, aromatic CH), $121.7$ (quaternary C–CO$_2$Me), $115.4$ (2C,
aromatic CH) and $52.0$ (OCH$_3$). DEPT-135 is positive at $132.0$, $115.4$ and $52.0$,
with no negative signal, so there is no CH$_2$; the OCH$_3$ is the only sp$^{3}$ carbon.

**Step 4 — Impurities.** The singlet at $\delta$ 2.17 (0.3H) is acetone, a common
solvent impurity; the singlet at $\delta$ 7.26 is residual $\ce{CHCl3}$ in
$\ce{CDCl3}$. Neither is part of the analyte. The broad singlet at $\delta$ 5.85 is the
phenolic O–H; it disappears on shaking with $\ce{D2O}$ and is not seen in the HSQC.

**Step 5 — Assembly.** The para-disubstituted ring, the methyl ester and the phenolic
OH give methyl 4-hydroxybenzoate. The assignments are: C1 $=121.7$ (ipso to the ester),
C2/C6 $=132.0$, C3/C5 $=115.4$, C4 $=160.1$, C=O $=167.2$, OCH$_3$ $=52.0$; the
$^{1}$H shifts are H-2/H-6 $=7.96$, H-3/H-5 $=6.91$, OCH$_3$ $=3.90$, OH $=5.85$.

**Step 6 — Excluding the isomers.** Methyl 2-hydroxybenzoate has no symmetry: eight
$^{13}$C signals and four aromatic $^{1}$H signals, each 1H, with a mixture of ortho and
meta couplings. Its intramolecular hydrogen bond would sharpen the O–H and lower the C=O
stretch. Methyl 3-hydroxybenzoate is also unsymmetrical: eight $^{13}$C signals and four
1H aromatic signals, again with ortho and meta couplings. The observed two 2H doublets
and six $^{13}$C signals exclude both.

**Answer.** Methyl 4-hydroxybenzoate, $\ce{C8H8O3}$; all signals assigned; acetone and
residual $\ce{CHCl3}$ are impurities; the 2- and 3-hydroxy isomers are excluded by the
symmetry of the $^{13}$C and $^{1}$H spectra.

**Check.** The formula, the DBE, the IR functional groups, the six $^{13}$C signals, the
two 2H doublets and the DEPT multiplicities are all consistent with one structure, and
every observed signal is assigned. No predicted signal is missing.

**Where marks are lost.** Assigning the 2.17 or 7.26 signals to the analyte, or proposing
a structure that does not explain the two 2H doublets.

### 46. Multiplicity, false discovery and predictive value **(Multi-step)**

**Strategy.** Compute the family-wise error, the Bonferroni threshold and the
Benjamini–Hochberg step-up rejects; then compute the PPV from the pre-study odds.

**Working.** (a) For 20 independent tests at $\alpha=0.05$,
$$
\alpha_{\mathrm{FWER}} = 1-(1-0.05)^{20} = 1-0.95^{20} = 0.6415.
$$
The Bonferroni threshold is $0.05/20 = 0.0025$; only the first two p-values
($0.0002$ and $0.001$) pass.

(b) The Benjamini–Hochberg thresholds are $i\times0.05/20=i\times0.0025$:
$$
\begin{array}{c|cccccc}
i & 1 & 2 & 3 & 4 & 5 & 6\\
p_{(i)} & 0.0002 & 0.001 & 0.004 & 0.009 & 0.012 & 0.018\\
i q/m & 0.0025 & 0.0050 & 0.0075 & 0.0100 & 0.0125 & 0.0150
\end{array}
$$
The first five satisfy $p_{(i)}\le iq/m$; the sixth does not. The largest $i$ that
satisfies the inequality is 5, so **five discoveries** are declared: $0.0002$, $0.001$,
$0.004$, $0.009$ and $0.012$. The $p=0.03$ comparison mentioned in the question is not
among them.

(c) The positive predictive value is
$$
\mathrm{PPV} = \frac{(1-\beta)R}{(1-\beta)R+\alpha}
= \frac{(0.8)(0.2)}{(0.8)(0.2)+0.05}
= \frac{0.16}{0.21} = 0.762.
$$
About $76\%$ of the significant findings would be true under these assumptions.

(d) The authors should report all 20 comparisons, the pre-specified primary endpoint,
the effect sizes with confidence intervals, the raw p-values and the BH-adjusted
q-values, and they should label the remaining comparisons as exploratory. Highlighting a
single $p=0.03$ among 20 tests is the multiplicity fallacy. A design change that would
make the conclusion robust is to pre-register one primary comparison, power the study for
it, replicate in an independent cohort, and use a hierarchical or gatekeeping strategy
for the secondary comparisons; alternatively, treat the study as a screening experiment
and report false-discovery-rate-controlled results.

**Answer.** FWER $=0.642$; Bonferroni threshold $0.0025$; BH declares five discoveries
($0.0002$, $0.001$, $0.004$, $0.009$, $0.012$); PPV $=0.762$. Report all comparisons with
effect sizes and adjusted q-values, and pre-register a primary endpoint.

**Check.** Under the global null, the expected number of p-values below $0.05$ is one;
five BH discoveries is more than chance, but the FWER shows that treating all 20 as
confirmatory would be unjustified. The PPV of $0.76$ is consistent with a field where
one hypothesis in five is true.

**Where marks are lost.** Applying Bonferroni and BH as if they answered the same
question, or claiming that a single $p=0.03$ is significant without adjusting for the 20
comparisons.

---

## Part F — Multiple-choice self-check

### 47. CCSD(T)

**Strategy.** Test each statement against the definitions of variationality, size
consistency and cost scaling.

**Working.** CCSD solves the coupled-cluster equations iteratively at a cost of $K^{6}$;
the triples correction is added non-iteratively at a cost of $K^{7}$. The
similarity-transformed Hamiltonian is non-Hermitian, so the energy is not an expectation
value and the method is not variational. The exponential ansatz factorises for
non-interacting fragments, so the method is size-consistent. Therefore A is true and B,
C, D are false.

**Answer: A.**

**Reason.** CCSD(T) is size-consistent and non-variational, and its formal cost scales as
$K^{7}$ (the iterative CCSD part is $K^{6}$, and the perturbative triples step is $K^{7}$).
It is the standard benchmark for thermochemistry and non-covalent interactions precisely
because it combines size consistency with an accurate treatment of dynamic correlation.

**Best distractor: B.** CCSD(T) is *not* variational: the similarity-transformed
Hamiltonian is non-Hermitian, and the energy is not an expectation value, so it does not
provide an upper bound. B states the opposite and is the most tempting because many
quantum-chemical methods (HF, CI, CASSCF) are variational.

**Why C is wrong.** The triples are perturbative, not iterative; the iterative method is
CCSD, which scales as $K^{6}$.

**Why D is wrong.** CCSD(T) is an approximation even within a finite basis; it is not
exact.

**Check.** Doubling the basis functions multiplies the triples step by $2^{7}=128$, not
by $2^{6}$.

### 48. Functional for charge transfer

**Strategy.** Identify the dominant physical error in a long-range charge-transfer
excitation and match it to the functional ingredient that repairs it.

**Working.** At 8 Å the electron–hole attraction is $-1/r$, which a semilocal functional
does not reproduce; the CT energy is therefore too low. Range separation uses exact
exchange at long range and restores the correct asymptote. Dispersion is a ground-state
correlation effect and does not repair the CT error. Therefore C.

**Answer: C.**

**Reason.** At an 8 Å separation the electron and hole interact through a long-range
$-1/r$ potential. A range-separated functional such as CAM-B3LYP uses a larger fraction
of exact exchange at long range, restoring the correct asymptotic potential and
substantially repairing the charge-transfer error.

**Best distractor: D.** B3LYP with D3 sounds sophisticated, and dispersion is important
at 8 Å, but the dominant error for a charge-transfer excitation is the missing long-range
exchange, not dispersion. D3 changes the ground-state energy, not the CT excitation
energy in the required way.

**Why A is wrong.** LDA is exact for the uniform electron gas, not for a separated
electron–hole pair; it has the wrong asymptotic potential.

**Why B is wrong.** The GGA gradient correction improves thermochemistry but does not
restore the $-1/r$ asymptote.

**Check.** The CT error of a global hybrid decreases as the exact-exchange fraction
increases; a range-separated functional is designed for exactly this limit.

### 49. The Berendsen thermostat

**Strategy.** Compare what the algorithm controls (the mean temperature) with the
ensemble it generates (the distribution).

**Working.** Berendsen rescaling multiplies velocities by
$\lambda=[1+(\Delta t/\tau)(T_0/T-1)]^{1/2}$, which drives $T$ to $T_0$ but lacks the
random force required by the fluctuation–dissipation theorem; the variance is suppressed.
It is a thermostat, not a barostat, and it does not conserve NVE energy. Therefore D.

**Answer: D.**

**Reason.** Berendsen scaling multiplies velocities by a factor that drives the mean
temperature towards the target, but it does not include the random forces required by the
fluctuation–dissipation theorem. The distribution is therefore narrower than canonical,
and the kinetic-energy variance is suppressed. It is useful for equilibration, not for
production.

**Best distractor: A.** A is the common misconception: the mean temperature is correct,
so the thermostat "works". The variance test shows that it does not generate the canonical
ensemble.

**Why B is wrong.** Berendsen is a thermostat, not a barostat; the barostat counterpart is
a separate algorithm.

**Why C is wrong.** It does not conserve total energy in NVE; it is not an NVE method, and
it actively changes the kinetic energy.

**Check.** In a production run, compare $\mathrm{var}(K)$ with $(3N/2)k_\mathrm{B}^{2}T^{2}$;
a value below the canonical variance is the signature of Berendsen scaling.

### 50. A primary KIE of 7.8

**Strategy.** Compare the observed KIE with the semiclassical maximum obtained from the
zero-point energy difference.

**Working.** $\Delta\mathrm{ZPE}=5.08\ \mathrm{kJ\,mol^{-1}}$ and
$k_\mathrm{H}/k_\mathrm{D}=e^{5.08/2.478}=7.77$. The observed 7.8 is at the semiclassical
maximum, so it supports rate-limiting C–H cleavage without requiring tunnelling; a much
larger value with a curved Arrhenius plot would indicate tunnelling. Therefore C.

**Answer: C.**

**Reason.** For a C–H stretch near $2900\ \mathrm{cm^{-1}}$, the semiclassical zero-point
energy difference gives $k_\mathrm{H}/k_\mathrm{D}\approx7.8$ at 298 K when the
transition state has no isotope-sensitive bonding. The observed value therefore supports
rate-limiting C–H cleavage and does not require tunnelling.

**Best distractor: A.** Values *substantially above* the semiclassical maximum (for
example, well above 10 with a curved Arrhenius plot and a small pre-exponential factor)
are the signature of tunnelling. A value at the maximum is consistent with the
semiclassical model and is not proof of tunnelling.

**Why B is wrong.** 7.8 is a normal primary KIE, not an impossible one; a secondary
effect is typically 1.1–1.3.

**Why D is wrong.** A primary KIE of this size indicates that the C–H bond *is* broken in
the rate-determining step; if it were not, the effect would be near 1.

**Check.** The expected value from $\Delta\mathrm{ZPE}=5.08\ \mathrm{kJ\,mol^{-1}}$ is
$e^{5.08/2.478}=7.77$, in agreement with the observation.

### 51. Fabrication versus falsification

**Strategy.** Apply the three questions in order: was the observation made, was it
altered, was the work of others used without credit.

**Working.** A: real data suppressed, so falsification. B: text reused without credit, so
plagiarism. C: data altered, so falsification. D: observation never made, so fabrication.
Therefore D.

**Answer: D.**

**Reason.** Fabrication is making up data or results and recording or reporting them. A
spectrum for a compound that was never synthesised is an invented observation.

**Best distractor: A.** Deleting three inconvenient replicates is a serious offence, but
it is **falsification**: real data are suppressed so that the record misrepresents the
work. The distinction is whether the observation was ever made.

**Why B is wrong.** Reusing a paragraph with the citation moved is plagiarism: the words
are used without appropriate credit.

**Why C is wrong.** Adjusting a baseline until the integral matches the expectation is
falsification: the data are altered.

**Check.** Ask three questions in order: was the observation made; was it altered; was
the work of others used without credit. Only an invented observation is fabrication.

---

## Top ten errors at research level

| Rank | Error | Why it costs marks | Correct habit |
|---|---|---|---|
| 1 | Comparing total energies from different methods or basis sets | The numbers are in the same unit but describe different model chemistries | Compare energy differences at a consistent level, and state the model chemistry |
| 2 | Using a single-reference method when static correlation is possible | The reference is qualitatively wrong and the number is plausible but meaningless | Check T1, the leading weight and the gap; use CASSCF/CASPT2 when indicated |
| 3 | Reporting a binding energy without BSSE or dispersion | The uncorrected value can be wrong by the binding energy itself | Apply counterpoise and a dispersion correction, and report both values |
| 4 | Quoting a free energy to $0.1\ \mathrm{kJ\,mol^{-1}}$ without an error budget | The precision is not the accuracy; the force field and sampling dominate | Separate statistical and systematic error and report a combined uncertainty |
| 5 | Treating the Kohn–Sham gap as the fundamental gap or as an excitation energy | The derivative discontinuity is missing and the orbital energies are not physical | Use $\Delta$SCF, TD-DFT, EOM-CCSD or a many-body method for the observable |
| 6 | Using Berendsen for production, or miscounting degrees of freedom | The ensemble is wrong or the temperature is biased | Use a canonical thermostat and count $3N-N_c$ degrees of freedom when constraints are present |
| 7 | Inferring a mechanism from products alone or from one trapping experiment | Several mechanisms give the same product, and the trap perturbs the system | Combine kinetics, labelling, spectroscopy and computation; test the probe |
| 8 | Reporting the one significant comparison among many | The family-wise error rate is large and the finding may be noise | Pre-specify the primary comparison; report effect sizes, intervals and adjusted q-values |
| 9 | Claiming scalability or greenness from a small, uncontrolled experiment | The claim is not supported by the data and cannot be audited | Demonstrate at scale, report E-factor/PMI over a stated boundary, and use a control |
| 10 | Assigning authorship by seniority and leaving conflicts undeclared | Credit is misallocated, accountability is diluted and the record is compromised | Apply the ICMJE criteria, record CRediT roles, declare and manage conflicts |
