# Level 3 — Worked Solutions

> **Level:** Advanced (Level 3 — Undergraduate core)
> **Companion to:** [`../exercises/level-3-exercises.md`](../exercises/level-3-exercises.md)
> **Items:** 60

Each solution states the model first, then writes the relation in symbols, substitutes
with units, and quotes the answer at the precision the data allow. Standard potentials
refer to 298 K; pH values refer to 25 °C. Where a value depends on temperature, the
temperature is stated.

---

## Part A — Conceptual questions

### 1. The wavefunction, the Born rule and nodes — [Ch. 1]

**Strategy.** Define the object, state what is measurable, then interpret a node.

**Answer.** The wavefunction $\psi(\mathbf{r})$ is the solution of the Schrödinger
equation; it is generally complex and has no direct physical meaning on its own. The
Born interpretation states that $|\psi|^{2}\,\mathrm{d}\tau$ is the probability of
finding the particle in the volume element $\mathrm{d}\tau$, so it is the probability
density $|\psi|^{2}$ that is measurable, not $\psi$. A global phase factor
$e^{i\phi}$ leaves every observable unchanged, which is why $\psi$ and $e^{i\phi}\psi$
describe the same state. A node is a surface on which $\psi = 0$; the probability
density vanishes there, so the particle is never found exactly on a nodal surface. The
number of nodes rises with the principal quantum number — a $1s$ orbital has none, a
$2s$ orbital has one radial node — and each additional node corresponds to an extra
half-wavelength fitted into the region.

**Check.** If $\psi$ were directly observable, an overall minus sign would change the
state; it does not, because only $|\psi|^{2}$ enters the prediction.

### 2. Why $4s$ fills first but empties first — [Ch. 2]

**Strategy.** Separate the filling order, which is governed by orbital energy in the
neutral atom, from the ionisation order, which is governed by the energies in the ion.

**Answer.** In potassium and calcium the $4s$ orbital penetrates the argon core and
experiences a high effective nuclear charge near the nucleus, so its energy lies below
that of $3d$, which is diffuse and well screened. That is why $4s$ is occupied first
and why the Madelung rule gives $4s$ before $3d$. Once the $3d$ shell begins to fill,
the ten added protons and the compact $3d$ radial distribution lower the $3d$ energy
below $4s$; in the transition metals the $3d$ electrons are therefore more tightly
bound than the $4s$ electrons. When a first-row transition metal is ionised, the
highest-energy electrons are removed first, so $\ce{Fe}$ ($[\ce{Ar}]3d^{6}4s^{2}$)
forms $\ce{Fe^2+}$ as $[\ce{Ar}]3d^{6}$, not $[\ce{Ar}]3d^{4}4s^{2}$. The apparent
contradiction is resolved by remembering that orbital energies are not fixed: they
depend on the configuration of the atom or ion concerned.

**Check.** The same logic explains why $\ce{Sc+}$ is $[\ce{Ar}]3d^{1}4s^{1}$ rather
than $[\ce{Ar}]3d^{2}$.

### 3. Paramagnetism of $\ce{O2}$ — [Ch. 3]

**Strategy.** Count valence electrons, fill the MO diagram in order of increasing
energy, and apply Hund's rule to the degenerate $\pi^{*}$ pair.

**Answer.** Oxygen has 12 valence electrons, which fill the orbitals as
$\sigma_{2s}^{2}\sigma_{2s}^{*2}\sigma_{2p}^{2}\pi_{2p}^{4}\pi_{2p}^{*2}$. The two
electrons in the degenerate $\pi^{*}$ pair occupy separate orbitals with parallel
spins, by Hund's rule, so the molecule has two unpaired electrons and is paramagnetic.
The Lewis structure $\ce{O=O}$ pairs every electron and therefore predicts a
diamagnetic molecule, which is wrong. The MO treatment also gives a bond order of
$(8-4)/2 = 2$, consistent with the observed double bond, and it accounts for the
weaker, longer bond in $\ce{O2-}$, where an extra electron enters $\pi^{*}$ and lowers
the bond order to 1.5. The paramagnetism of liquid oxygen is one of the clearest
experimental demonstrations that delocalised molecular orbitals, not localised bonds,
are the better model.

**Check.** Removing one $\pi^{*}$ electron to give $\ce{O2+}$ leaves one unpaired
electron and raises the bond order to 2.5, exactly as the model predicts.

### 4. $\Delta G$ and $\Delta G^{\circ}$ — [Ch. 4]

**Strategy.** Distinguish the standard-state value from the value at the actual
composition, and use the reaction quotient to connect them.

**Answer.** $\Delta G^{\circ}$ is the Gibbs energy change when every reactant and
product is in its standard state — unit activity, which for a gas means
$p = 10^{5}\ \text{Pa}$ and for a solute a standard concentration — at a stated
temperature. It is a fixed property of the reaction at that temperature and it fixes
the equilibrium constant through $\Delta G^{\circ} = -RT\ln K$. $\Delta G$ is the
change at the actual composition and is given by
$\Delta G = \Delta G^{\circ} + RT\ln Q$. A reaction with $\Delta G^{\circ} > 0$ has
$K < 1$, so products are favoured only weakly, but if $Q$ is small enough the term
$RT\ln Q$ is negative enough to make $\Delta G < 0$ and the forward reaction proceeds.
This is why a sparingly soluble salt still dissolves when a small amount of solid is
placed in pure water, and why precipitates form when the ion product exceeds $K_{sp}$.

**Check.** At equilibrium $Q = K$ and $\Delta G = 0$; substituting
$\Delta G^{\circ} = -RT\ln K$ returns zero identically, which is the consistency test.

### 5. Rate-determining step, steady state and pre-equilibrium — [Ch. 5]

**Strategy.** Define the control of flux, then contrast the two approximations used to
eliminate intermediates.

**Answer.** The rate-determining step is the step with the highest activation barrier
in the sequence, so it has the smallest rate constant and controls the flux through
the mechanism; the overall rate cannot exceed the rate at which that step supplies
product. The steady-state approximation sets $\mathrm{d}[\text{intermediate}]/\mathrm{d}t
\approx 0$ for every reactive intermediate, which is valid when the intermediate is
consumed as fast as it is formed; it produces a rate law without needing to know the
relative magnitudes of the individual rate constants. The pre-equilibrium approximation
assumes that a fast reversible step reaches thermodynamic equilibrium before the slow
step consumes its product, which requires $k_{-1} \gg k_2$; it is a special case of the
steady-state result in that limit. Both approximations fail when the intermediate
accumulates or when the steps have comparable rates.

**Check.** For a two-step mechanism with a fast first step, the pre-equilibrium result
and the steady-state result must agree as $k_{-1}/k_2 \to \infty$; if they do not, one
derivation contains an algebra error.

### 6. What a catalyst can and cannot change — [Ch. 6]

**Strategy.** Separate thermodynamics (which fixes the endpoint) from kinetics (which
fixes how fast it is reached).

**Answer.** A catalyst provides an alternative pathway whose transition state is lower
in Gibbs energy, so it lowers $\Delta G^{\ddagger}$ and accelerates both the forward
and the reverse reaction. The initial and final states are unchanged, so $\Delta G^{\circ}$
and therefore $K = \exp(-\Delta G^{\circ}/RT)$ are unchanged: a catalyst cannot shift an
equilibrium position, only help it to be reached. Turnover frequency is the number of
catalytic cycles per active site per unit time, with units of $\text{s}^{-1}$; turnover
number is the total number of cycles per site before the catalyst dies, and is
dimensionless. A homogeneous catalyst is in the same phase as the reactants — an acid
in solution, for example — whereas a heterogeneous catalyst is in a different phase,
typically a solid surface in contact with gases or a liquid, as in iron in the
Haber–Bosch process.

**Check.** If a proposal claims a catalyst raises the yield of an equilibrium-limited
reaction at fixed temperature, it is thermodynamically impossible and the claim is
false.

### 7. Buffer capacity and the limits of Henderson–Hasselbalch — [Ch. 7]

**Strategy.** Define capacity quantitatively, locate its maximum, then examine the
assumptions behind the equilibrium expression.

**Answer.** Buffer capacity $\beta$ is the amount of strong acid or base, per unit
volume, required to change the pH by one unit; equivalently
$\beta = \mathrm{d}n_{\text{base}}/\mathrm{dpH}$. It reaches a maximum when
$\mathrm{pH} = \mathrm{p}K_a$, that is when $[\ce{HA}] = [\ce{A-}]$, with
$\beta_{\max} = 0.576\,C$ for a total buffer concentration $C$; the buffer is
practically useful within about one pH unit of the $\mathrm{p}K_a$, where the ratio
$[\ce{A-}]/[\ce{HA}]$ lies between 1:10 and 10:1. The Henderson–Hasselbalch equation
assumes that the activity coefficients of $\ce{HA}$ and $\ce{A-}$ are equal and that
the equilibrium concentrations equal the formal concentrations. At high ionic strength
the two activity coefficients diverge, so a pH calculated from concentrations departs
from the measured pH, which is defined through the hydrogen-ion activity; the
Debye–Hückel limiting law is the first correction, and it is reliable only below about
$I = 0.01\ \text{mol dm}^{-3}$.

**Check.** A buffer prepared at pH 5.0 from an acid of $\mathrm{p}K_a = 2.0$ has almost
no $\ce{HA}$ left and negligible capacity, however much the equation is trusted.

### 8. Why $E^{\circ}$ is intensive — [Ch. 8]

**Strategy.** Relate the potential to energy per charge, then use
$\Delta G^{\circ} = -zFE^{\circ}$.

**Answer.** An electrode potential is an energy per unit charge, measured in volts
($\text{J C}^{-1}$), so it is an intensity and does not depend on how much substance
reacts; doubling the amount of a half-reaction doubles both the charge transferred and
the energy, leaving the ratio unchanged. $\Delta G^{\circ}$ is an extensive energy per
mole of reaction, so doubling the stoichiometric coefficients doubles it. The
consistency relation $\Delta G^{\circ} = -zFE^{\circ}$ shows why: the doubled reaction
has $2z$ electrons and $2\Delta G^{\circ}$, so $E^{\circ}$ is unchanged. For the same
reason, cell potentials are never added when half-cells are combined; the Gibbs energies
are added and the result is converted back with the total $z$.

**Check.** Reversing a half-reaction reverses the sign of $E^{\circ}$ but not its
magnitude, exactly as reversing the reaction reverses $\Delta G^{\circ}$.

### 9. $\Delta_o$ against the pairing energy — [Ch. 9]

**Strategy.** Compare the crystal-field gain from occupying the lower $t_{2g}$ set with
the repulsion cost of pairing two electrons in one orbital.

**Answer.** In an octahedral field the $t_{2g}$ set is stabilised by $0.4\Delta_o$ per
electron and the $e_g$ set destabilised by $0.6\Delta_o$ per electron. For a $d^{4}$ to
$d^{7}$ ion there is a choice: promote an electron into $e_g$ and keep spins parallel
(high spin), or pair it in $t_{2g}$ (low spin). Low spin wins when
$\Delta_o > P$, because the extra stabilisation exceeds the pairing energy; high spin
wins when $\Delta_o < P$. Cyanide is high in the spectrochemical series and produces a
large splitting, so for $\ce{Fe^3+}$ ($d^{5}$) with $\Delta_o = 24\,000\ \text{cm}^{-1}$
and $P = 21\,000\ \text{cm}^{-1}$ the low-spin $t_{2g}^{5}$ configuration is favoured,
with one unpaired electron. Water is a weak-field ligand, giving
$\Delta_o = 14\,000\ \text{cm}^{-1} < P$, so $\ce{[Fe(H2O)6]^3+}$ is high spin with five
unpaired electrons. The magnetic moments follow the spin-only formula
$\mu = \sqrt{n(n+2)}\,\mu_{\text{B}}$, so the two complexes are magnetically
distinguishable.

**Check.** For $d^{5}$, high spin has CFSE exactly zero, so the low-spin form must gain
$2P - 2\Delta_o$; with these numbers that is
$42\,000 - 48\,000 = -6000\ \text{cm}^{-1}$, a genuine stabilisation.

### 10. TMS, $^{13}\mathrm{C}$ decoupling and the IR activity of $\ce{CO2}$ — [Ch. 10]

**Strategy.** Treat each as a selection-rule or practical-reference question.

**Answer.** Tetramethylsilane is used as the NMR reference because its twelve protons
are equivalent and give a single sharp line, it is volatile and easily removed, it is
inert and soluble in most organic solvents, and its resonance lies upfield of almost
all others, so it can be defined as $\delta = 0$ without overlapping the sample signals.
Carbon-13 has a natural abundance of only about 1.1 %, and each carbon would otherwise
be split into a multiplet by coupling to its attached protons, so spectra are recorded
with broadband proton decoupling: every carbon signal collapses to a singlet and the
signal-to-noise ratio improves through the nuclear Overhauser effect. Carbon dioxide
has a centre of symmetry: the symmetric stretch moves both C=O bonds in phase, leaving
the dipole moment unchanged, so it is infrared inactive; the asymmetric stretch and
the bend change the dipole moment and are infrared active. The same symmetry argument
makes $\ce{N2}$ and $\ce{O2}$ infrared inactive.

**Check.** Raman spectroscopy, which requires a change in polarisability rather than in
dipole moment, shows the symmetric stretch of $\ce{CO2}$ strongly — the two techniques
are complementary.

---

## Part B — Basic problems

### 11. Photon energy at 400 nm — [Ch. 1]

**Strategy.** Use $E = hc/\lambda$ for one photon, then multiply by $N_{\text{A}}$ for
one mole.

**Working.**

$$
E = \frac{hc}{\lambda}
= \frac{(6.626\times10^{-34})(2.998\times10^{8})}{400\times10^{-9}}
= 4.966\times10^{-19}\ \text{J}
$$

$$
E_{\text{molar}} = (4.966\times10^{-19})(6.022\times10^{23})
= 2.99\times10^{5}\ \text{J mol}^{-1}
$$

**Answer.** $E = 4.97\times10^{-19}\ \text{J}$ per photon;
$E_{\text{molar}} = 299\ \text{kJ mol}^{-1}$.

**Check.** Visible photons carry about $2$–$3\ \text{eV}$; here
$4.97\times10^{-19}/1.602\times10^{-19} = 3.10\ \text{eV}$, consistent.

**Where marks are lost.** Using $\lambda$ in nanometres without converting to metres;
forgetting to multiply by $N_{\text{A}}$ when the answer is requested per mole.

### 12. de Broglie wavelength of an electron — [Ch. 1]

**Strategy.** Use $\lambda = h/(mv)$ and keep the mass in kilograms.

**Working.**

$$
\lambda = \frac{h}{m_ev}
= \frac{6.626\times10^{-34}}{(9.109\times10^{-31})(1.00\times10^{6})}
= 7.27\times10^{-10}\ \text{m}
$$

**Answer.** $\lambda = 7.27\times10^{-10}\ \text{m} = 727\ \text{pm}$.

**Check.** An electron accelerated through about $3\ \text{V}$ has a de Broglie
wavelength of roughly $0.7\ \text{nm}$, so the magnitude is right; such wavelengths are
comparable to atomic spacings, which is why electron diffraction works.

**Where marks are lost.** Using the electron mass in atomic mass units; forgetting that
$1\ \text{pm} = 10^{-12}\ \text{m}$.

### 13. Quantum-number sets and shell capacity — [Ch. 2]

**Strategy.** Apply $l \le n-1$ and $|m_l| \le l$, then count orbitals as
$\sum_l (2l+1)$.

**Working.** (a) $(3,2,-1)$: $l = 2 < 3$ and $|m_l| = 1 \le 2$, allowed.
$(2,2,0)$: $l = n$, not allowed. $(4,0,0)$: allowed. $(3,3,-2)$: $l = n$, not allowed.

(b) For $n = 3$ the subshells are $3s$ ($l = 0$, one orbital), $3p$ ($l = 1$, three
orbitals) and $3d$ ($l = 2$, five orbitals):

$$
1 + 3 + 5 = 9\ \text{orbitals}, \qquad 2n^{2} = 18\ \text{electrons}
$$

**Answer.** (a) $(3,2,-1)$ and $(4,0,0)$ are allowed; the other two are not.
(b) Nine orbitals, holding eighteen electrons.

**Check.** The count $2n^{2}$ reproduces the periodic-table capacities $2, 8, 18, 32$.

**Where marks are lost.** Accepting $(2,2,0)$ by confusing $l$ with $n$; counting
electrons when orbitals are asked for.

### 14. Bond orders from molecular orbital theory — [Ch. 3]

**Strategy.** Count bonding and antibonding valence electrons and apply
$\text{BO} = (N_{\text{b}} - N_{\text{a}})/2$.

**Working.**

$$
\ce{N2}: 10\ \text{valence e}^-,\quad
\text{BO} = \frac{8-2}{2} = 3.0
$$

$$
\ce{O2}: 12\ \text{valence e}^-,\quad
\text{BO} = \frac{8-4}{2} = 2.0
$$

$$
\ce{O2-}: 13\ \text{valence e}^-,\quad
\text{BO} = \frac{8-5}{2} = 1.5
$$

$$
\ce{N2+}: 9\ \text{valence e}^-,\quad
\text{BO} = \frac{7-2}{2} = 2.5
$$

**Answer.** $\ce{N2}$ 3.0; $\ce{O2}$ 2.0; $\ce{O2-}$ 1.5; $\ce{N2+}$ 2.5.

**Check.** Bond order correlates inversely with bond length, so $\ce{N2}$ should have
the shortest bond and $\ce{O2-}$ the longest of the oxygen species; that is observed.

**Where marks are lost.** Counting core electrons in $N_{\text{b}}$ and $N_{\text{a}}$;
forgetting that the added electron in $\ce{O2-}$ enters an antibonding orbital.

### 15. Signs of entropy change — [Ch. 4]

**Strategy.** Compare the number and freedom of motion of the species on each side,
remembering that gas formation dominates.

**Working.** (a) One mole of solid gives one mole of solid plus one mole of gas, so
$\Delta S^{\circ} > 0$. (b) Four moles of gas give two moles of gas, so
$\Delta S^{\circ} < 0$. (c) Liquid water becomes solid ice, losing translational and
rotational freedom, so $\Delta S < 0$.

**Answer.** (a) positive; (b) negative; (c) negative.

**Check.** The magnitudes are consistent with the standard values: the decomposition of
calcium carbonate has $\Delta S^{\circ} = +160.7\ \text{J K}^{-1}\ \text{mol}^{-1}$,
while the Haber reaction has $-198.1\ \text{J K}^{-1}\ \text{mol}^{-1}$.

**Where marks are lost.** Judging entropy by the number of molecules alone rather than
by the number of gas molecules; forgetting that freezing is exothermic but
entropy-reducing.

### 16. Gibbs energy and the crossover temperature — [Ch. 4]

**Strategy.** Convert $\Delta S^{\circ}$ to $\text{kJ K}^{-1}\ \text{mol}^{-1}$, then
apply $\Delta G^{\circ} = \Delta H^{\circ} - T\Delta S^{\circ}$.

**Working.**

$$
\Delta G^{\circ} = 50.0\ \text{kJ mol}^{-1}
- (298\ \text{K})(0.150\ \text{kJ K}^{-1}\ \text{mol}^{-1})
= 50.0 - 44.7 = +5.3\ \text{kJ mol}^{-1}
$$

$$
T_{\text{cross}} = \frac{\Delta H^{\circ}}{\Delta S^{\circ}}
= \frac{50.0}{0.150} = 333\ \text{K}
$$

**Answer.** $\Delta G^{\circ} = +5.3\ \text{kJ mol}^{-1}$ at $298\ \text{K}$; not
spontaneous under standard conditions; spontaneous above $333\ \text{K}$ (60 °C).

**Check.** Both terms are positive, so the reaction is entropy-driven and becomes
spontaneous only at high temperature, in agreement with the sign pattern
$\Delta H > 0$, $\Delta S > 0$.

**Where marks are lost.** Mixing joules and kilojoules; inverting the ratio for
$T_{\text{cross}}$.

### 17. Order and units of $k$ — [Ch. 5]

**Strategy.** Read the exponents from the rate law, add them for the overall order, and
use $\text{units of } k = (\text{mol dm}^{-3})^{1-N}\text{s}^{-1}$.

**Working.** First order in $\ce{A}$, second order in $\ce{B}$, third order overall
($N = 3$).

$$
\text{units of } k = (\text{mol dm}^{-3})^{1-3}\ \text{s}^{-1}
= \text{dm}^{6}\ \text{mol}^{-2}\ \text{s}^{-1}
$$

**Answer.** $m = 1$, $n = 2$, overall order 3;
$k$ in $\text{dm}^{6}\ \text{mol}^{-2}\ \text{s}^{-1}$.

**Check.** Substituting the units into $v = k[\ce{A}][\ce{B}]^{2}$ returns
$\text{mol dm}^{-3}\ \text{s}^{-1}$, as required.

**Where marks are lost.** Quoting $\text{s}^{-1}$ for any reaction; treating the
stoichiometric coefficients as orders.

### 18. Langmuir fractional coverage — [Ch. 6]

**Strategy.** Use $\theta_{\text{A}} = K_{\text{A}}p_{\text{A}}/(1 + K_{\text{A}}p_{\text{A}})$.

**Working.**

$$
K_{\text{A}}p_{\text{A}} = (2.0\times10^{-4}\ \text{Pa}^{-1})(1.0\times10^{4}\ \text{Pa}) = 2.0
$$

$$
\theta_{\text{A}} = \frac{2.0}{1 + 2.0} = 0.667
$$

**Answer.** $\theta_{\text{A}} = 0.667$ (dimensionless).

**Check.** At $Kp = 1$ the coverage would be $0.5$; doubling $Kp$ raises it to $0.667$,
consistent with the shape of the isotherm.

**Where marks are lost.** Reporting a percentage without converting, or forgetting that
$\theta$ cannot exceed 1.

### 19. Buffer pH from the Henderson–Hasselbalch equation — [Ch. 7]

**Strategy.** Substitute the ratio of formal concentrations into
$\mathrm{pH} = \mathrm{p}K_a + \log_{10}([\ce{A-}]/[\ce{HA}])$.

**Working.**

$$
\mathrm{pH} = 4.20 + \log_{10}\frac{0.050}{0.100}
= 4.20 + \log_{10}(0.500)
= 4.20 - 0.301
$$

**Answer.** $\mathrm{pH} = 3.90$.

**Check.** The buffer contains more acid than base, so the pH must lie below the
$\mathrm{p}K_a$ by $0.30$ of a unit; it does.

**Where marks are lost.** Inverting the ratio, which gives 4.50 and the wrong side of
the $\mathrm{p}K_a$.

### 20. Standard cell potential — [Ch. 8]

**Strategy.** Use $E^{\circ}_{\text{cell}} = E^{\circ}_{\text{cathode}} - E^{\circ}_{\text{anode}}$
with tabulated reduction potentials for both electrodes.

**Working.**

$$
E^{\circ}_{\text{cathode}} = E^{\circ}(\ce{Ag+}/\ce{Ag}) = +0.80\ \text{V}
$$

$$
E^{\circ}_{\text{anode}} = E^{\circ}(\ce{Zn^2+}/\ce{Zn}) = -0.76\ \text{V}
$$

$$
E^{\circ}_{\text{cell}} = 0.80 - (-0.76) = 1.56\ \text{V}
$$

**Answer.** $E^{\circ}_{\text{cell}} = +1.56\ \text{V}$; silver is the cathode, zinc the
anode.

**Check.** The positive value means the reaction
$\ce{Zn(s) + 2Ag+(aq) -> Zn^2+(aq) + 2Ag(s)}$ is spontaneous, which agrees with the
observation that zinc displaces silver from solution.

**Where marks are lost.** Subtracting in the wrong order, which gives $-1.56\ \text{V}$;
adding the two potentials after reversing one sign.

### 21. Spin-only magnetic moment of a high-spin $d^{5}$ ion — [Ch. 9]

**Strategy.** Count unpaired electrons in the high-spin $d^{5}$ configuration and apply
$\mu = \sqrt{n(n+2)}\,\mu_{\text{B}}$.

**Working.** High-spin $d^{5}$ has one electron in each of the five $d$ orbitals, so
$n = 5$:

$$
\mu = \sqrt{5(5+2)} = \sqrt{35} = 5.92\ \mu_{\text{B}}
$$

**Answer.** $n = 5$; $\mu = 5.92\ \mu_{\text{B}}$.

**Check.** The maximum possible spin-only moment for a $d$-block ion is $5.92\ \mu_{\text{B}}$,
so a value above this would signal an error or a large orbital contribution.

**Where marks are lost.** Using the low-spin configuration ($n = 1$,
$\mu = 1.73\ \mu_{\text{B}}$); forgetting the square root.

### 22. Concentration from absorbance — [Ch. 10]

**Strategy.** Rearrange the Beer–Lambert law for $c$.

**Working.**

$$
A = \varepsilon bc
\qquad\Longrightarrow\qquad
c = \frac{A}{\varepsilon b}
= \frac{0.60}{(1.5\times10^{4})(1.00)}
= 4.0\times10^{-5}\ \text{mol dm}^{-3}
$$

**Answer.** $c = 4.0\times10^{-5}\ \text{mol dm}^{-3}$.

**Check.** With $\varepsilon$ of order $10^{4}$, an absorbance near 1 corresponds to
concentrations near $10^{-4}\ \text{mol dm}^{-3}$; the result is consistent.

**Where marks are lost.** Using $b$ in metres while $\varepsilon$ is quoted per
centimetre; using $A = \log_{10}(I/I_0)$ with the wrong sign.

---

## Part C — Intermediate problems

### 23. The one-dimensional box applied to hexatriene — [Ch. 1]

**Strategy.** Six $\pi$ electrons fill three levels; the absorption promotes one
electron from $n = 3$ to $n = 4$. Use $E_n = n^{2}h^{2}/(8mL^{2})$.

**Working.**

$$
E_1 = \frac{h^{2}}{8m_eL^{2}}
= \frac{(6.626\times10^{-34})^{2}}{8(9.109\times10^{-31})(0.84\times10^{-9})^{2}}
= 8.539\times10^{-20}\ \text{J}
$$

$$
\Delta E = (4^{2} - 3^{2})E_1 = 7(8.539\times10^{-20})
= 5.977\times10^{-19}\ \text{J}
$$

$$
\lambda = \frac{hc}{\Delta E}
= \frac{(6.626\times10^{-34})(2.998\times10^{8})}{5.977\times10^{-19}}
= 3.32\times10^{-7}\ \text{m}
$$

**Answer.** $\Delta E = 5.98\times10^{-19}\ \text{J}$; $\lambda = 332\ \text{nm}$.

**Check.** The result lies in the near ultraviolet, close to the observed absorption of
hexatriene at about $260\ \text{nm}$; the box model overestimates the wavelength
because it ignores the finite barrier and electron repulsion.

**Where marks are lost.** Using $n = 6$ to $n = 7$, which counts electrons rather than
levels; forgetting that the HOMO of six electrons is $n = 3$.

### 24. Photoelectric effect in caesium — [Ch. 1]

**Strategy.** Convert the work function to joules, then use
$h\nu = \Phi + E_{k,\max}$.

**Working.** (a)

$$
\Phi = (2.14\ \text{eV})(1.602\times10^{-19}\ \text{J eV}^{-1})
= 3.429\times10^{-19}\ \text{J}
$$

$$
\lambda_{\text{threshold}} = \frac{hc}{\Phi}
= \frac{(6.626\times10^{-34})(2.998\times10^{8})}{3.429\times10^{-19}}
= 5.79\times10^{-7}\ \text{m}
$$

(b) At $400\ \text{nm}$,

$$
E_{\text{photon}} = 4.966\times10^{-19}\ \text{J}
$$

$$
E_{k,\max} = 4.966\times10^{-19} - 3.429\times10^{-19}
= 1.538\times10^{-19}\ \text{J}
= 0.960\ \text{eV}
$$

**Answer.** (a) $579\ \text{nm}$; (b) $1.54\times10^{-19}\ \text{J} = 0.960\ \text{eV}$.

**Check.** $400\ \text{nm}$ is shorter than the threshold, so photoemission occurs;
the photon energy is $3.10\ \text{eV}$ and $3.10 - 2.14 = 0.96\ \text{eV}$, as found.

**Where marks are lost.** Using the threshold wavelength with the $400\ \text{nm}$
photon; forgetting that the kinetic energy is the difference, not the photon energy.

### 25. Nodes and effective nuclear charge — [Ch. 2]

**Strategy.** Apply radial nodes $= n - l - 1$, angular nodes $= l$, then Slater's
grouping for a $3p$ electron.

**Working.** (a) $3d$: $n = 3$, $l = 2$, so radial nodes $= 3 - 2 - 1 = 0$ and angular
nodes $= 2$; total $= 2$. $4p$: $n = 4$, $l = 1$, so radial nodes $= 4 - 1 - 1 = 2$
and angular nodes $= 1$; total $= 3 = n - 1$.

(b) For a $3p$ electron of chlorine ($Z = 17$), Slater's groups give:

- six other electrons in the same $3s3p$ group at $0.35$ each: $2.10$;
- eight electrons in the $n = 2$ shell at $0.85$ each: $6.80$;
- two $1s$ electrons at $1.00$ each: $2.00$.

$$
\sigma = 2.10 + 6.80 + 2.00 = 10.90
$$

$$
Z_{\text{eff}} = 17 - 10.90 = 6.10
$$

**Answer.** (a) $3d$: 0 radial, 2 angular; $4p$: 2 radial, 1 angular.
(b) $Z_{\text{eff}} = 6.10$.

**Check.** The total node count equals $n - 1$ in both cases: 2 for $3d$ and 3 for
$4p$.

**Where marks are lost.** Counting the electron itself in its own group (it is excluded
in Slater's method); using $0.35$ for the $n - 1$ shell.

### 26. Molecular orbital description of $\ce{NO}$ — [Ch. 3]

**Strategy.** Count 11 valence electrons, fill the MO scheme, then compute the bond
order and the spin.

**Working.**

$$
\ce{NO}: \sigma_{2s}^{2}\sigma_{2s}^{*2}\sigma_{2p}^{2}\pi_{2p}^{4}\pi_{2p}^{*1}
$$

$$
\text{BO} = \frac{8 - 3}{2} = 2.5
$$

The single $\pi^{*}$ electron is unpaired, so the molecule is paramagnetic.

For $\ce{NO+}$, removing one electron removes the $\pi^{*}$ electron:

$$
\ce{NO+}: \sigma_{2s}^{2}\sigma_{2s}^{*2}\sigma_{2p}^{2}\pi_{2p}^{4},
\qquad \text{BO} = \frac{8-2}{2} = 3.0
$$

**Answer.** $\ce{NO}$: bond order 2.5, one unpaired electron, paramagnetic.
$\ce{NO+}$: bond order 3.0, diamagnetic, and with a shorter bond.

**Check.** The bond order rises on ionisation, so the bond must shorten; this is
observed, and it is the opposite of the usual behaviour of a cation formed by removing
a bonding electron.

**Where marks are lost.** Placing the eleventh electron in $\sigma_{2p}$ rather than
$\pi^{*}$; using the $\ce{O2}$ ordering for NO without checking where the $\sigma_{2p}$ level
lies.

### 27. Thermal decomposition of calcium carbonate — [Ch. 4]

**Strategy.** Combine formation enthalpies and standard entropies, then solve
$\Delta G^{\circ} = 0$ for the crossover temperature.

**Working.**

$$
\Delta H^{\circ} = [(-635.1) + (-393.5)] - (-1206.9) = +178.3\ \text{kJ mol}^{-1}
$$

$$
\Delta S^{\circ} = (39.8 + 213.8) - 92.9 = +160.7\ \text{J K}^{-1}\ \text{mol}^{-1}
$$

$$
\Delta G^{\circ}_{298} = 178.3 - (298.15)(0.1607) = 178.3 - 47.9
= +130.4\ \text{kJ mol}^{-1}
$$

$$
T = \frac{\Delta H^{\circ}}{\Delta S^{\circ}}
= \frac{178\,300\ \text{J mol}^{-1}}{160.7\ \text{J K}^{-1}\ \text{mol}^{-1}}
= 1110\ \text{K}
$$

**Answer.** $\Delta H^{\circ} = +178.3\ \text{kJ mol}^{-1}$;
$\Delta S^{\circ} = +160.7\ \text{J K}^{-1}\ \text{mol}^{-1}$;
$\Delta G^{\circ}_{298} = +130.4\ \text{kJ mol}^{-1}$; decomposition becomes spontaneous
above about $1110\ \text{K}$ (837 °C).

**Check.** Both terms have the same sign pattern as a typical calcination: endothermic
and entropy-increasing, so the reaction is driven by temperature. Industrial lime kilns
operate above $1100\ \text{K}$, just above the calculated crossover.

**Where marks are lost.** Forgetting that $\Delta G^{\circ}$ at 298 K is not zero just
because the crossover exists; using $\Delta S^{\circ}$ in $\text{kJ}$.

### 28. Temperature dependence of $K$ — [Ch. 4]

**Strategy.** Integrate the van 't Hoff equation between the two temperatures.

**Working.**

$$
\ln\frac{K_2}{K_1} = -\frac{\Delta H^{\circ}}{R}
\left(\frac{1}{T_2} - \frac{1}{T_1}\right)
$$

$$
\ln\frac{K_2}{K_1} = -\frac{50\,000}{8.314}
\left(\frac{1}{350} - \frac{1}{298}\right)
= -6014(-4.987\times10^{-4}) = +3.00
$$

$$
K_2 = (1.0\times10^{-5})(e^{3.00}) = (1.0\times10^{-5})(20.1)
= 2.0\times10^{-4}
$$

**Answer.** $K(350\ \text{K}) = 2.0\times10^{-4}$.

**Check.** The reaction is endothermic, so heating must increase $K$; it rises by a
factor of about 20 over 52 K, consistent with a moderate $\Delta H^{\circ}$.

**Where marks are lost.** Sign errors in the temperature difference; using Celsius
temperatures; forgetting the assumption that $\Delta H^{\circ}$ is constant.

### 29. First-order rate constant at a second temperature — [Ch. 5]

**Strategy.** Use the two-point Arrhenius equation, then the integrated first-order law
for 90 % conversion.

**Working.**

$$
\ln\frac{k_2}{k_1} = -\frac{E_a}{R}\left(\frac{1}{320} - \frac{1}{300}\right)
= \frac{75\,000}{8.314}(2.083\times10^{-4}) = 1.879
$$

$$
k_2 = (4.5\times10^{-3})(e^{1.879}) = (4.5\times10^{-3})(6.55)
= 2.95\times10^{-2}\ \text{s}^{-1}
$$

$$
t_{90} = \frac{\ln(10)}{k_2} = \frac{2.303}{2.95\times10^{-2}} = 78.1\ \text{s}
$$

**Answer.** $k(320\ \text{K}) = 2.95\times10^{-2}\ \text{s}^{-1}$;
$t_{90} = 78.1\ \text{s}$.

**Check.** A 20 K rise increases $k$ by a factor of 6.6; with
$E_a = 75\ \text{kJ mol}^{-1}$ the rough rule $2^{2} = 4$ underestimates, as expected
for a high activation energy.

**Where marks are lost.** Using $\ln(0.9)$ instead of $\ln(10)$ for 90 % conversion
($\ln(1/0.1) = \ln 10$); forgetting that $t_{90}$ depends on $k$ only for first order.

### 30. Steady-state rate law for a dimerisation mechanism — [Ch. 5]

**Strategy.** Apply the steady-state approximation to $\ce{A2}$, solve for its
concentration, then substitute into the rate of the slow step.

**Working.**

$$
\ce{2A(g) <=>[k_1][k_{-1}] A2(g)}, \qquad \ce{A2(g) + B(g) ->[k_2] P(g)}
$$

The rate of product formation is $v = k_2[\ce{A2}][\ce{B}]$. For the intermediate:

$$
\frac{\mathrm{d}[\ce{A2}]}{\mathrm{d}t} = k_1[\ce{A}]^{2} - k_{-1}[\ce{A2}] - k_2[\ce{A2}][\ce{B}] \approx 0
$$

$$
[\ce{A2}] = \frac{k_1[\ce{A}]^{2}}{k_{-1} + k_2[\ce{B}]}
$$

$$
v = \frac{k_1k_2[\ce{A}]^{2}[\ce{B}]}{k_{-1} + k_2[\ce{B}]}
$$

When $k_{-1} \gg k_2[\ce{B}]$ the denominator is $k_{-1}$ and

$$
v \approx \frac{k_1k_2}{k_{-1}}[\ce{A}]^{2}[\ce{B}]
$$

so the reaction is second order in $\ce{A}$ and first order in $\ce{B}$. When
$k_2[\ce{B}] \gg k_{-1}$ the denominator is $k_2[\ce{B}]$ and $v \approx k_1[\ce{A}]^{2}$,
zero order in $\ce{B}$.

With the given values:

$$
v = \frac{(2.0\times10^{-2})(1.0\times10^{-3})(0.10)^{2}(0.050)}
{5.0\times10^{-3} + (1.0\times10^{-3})(0.050)}
$$

$$
v = \frac{1.0\times10^{-8}}{5.05\times10^{-3}} = 2.0\times10^{-6}
$$

**Answer.** $v = \dfrac{k_1k_2[\ce{A}]^{2}[\ce{B}]}{k_{-1} + k_2[\ce{B}]}$; second order
in $\ce{A}$ and first order in $\ce{B}$ in the pre-equilibrium limit; numerical value
$2.0\times10^{-6}$ in the units of $k$ used.

**Check.** The correction factor
$k_{-1}/(k_{-1} + k_2[\ce{B}]) = 5.0/5.05 = 0.99$, so the pre-equilibrium limit is
accurate to 1 % here.

**Where marks are lost.** Omitting the reverse step in the steady-state equation;
reporting the pre-equilibrium rate law as first order in $\ce{A}$.

### 31. Michaelis–Menten parameters — [Ch. 6]

**Strategy.** Substitute into the Michaelis–Menten equation, then use the definitions
of $k_{\text{cat}}$ and of the catalytic efficiency.

**Working.**

$$
v = \frac{V_{\text{max}}[\ce{S}]}{K_{\text{M}} + [\ce{S}]}
= \frac{(2.0\times10^{-6})(2.0\times10^{-3})}{(5.0\times10^{-3}) + (2.0\times10^{-3})}
= 5.71\times10^{-7}\ \text{mol dm}^{-3}\ \text{s}^{-1}
$$

$$
k_{\text{cat}} = \frac{V_{\text{max}}}{[\ce{E}]_0}
= \frac{2.0\times10^{-6}}{2.0\times10^{-8}} = 100\ \text{s}^{-1}
$$

$$
\frac{k_{\text{cat}}}{K_{\text{M}}} = \frac{100}{5.0\times10^{-3}}
= 2.0\times10^{4}\ \text{dm}^{3}\ \text{mol}^{-1}\ \text{s}^{-1}
$$

**Answer.** $v = 5.7\times10^{-7}\ \text{mol dm}^{-3}\ \text{s}^{-1}$;
$k_{\text{cat}} = 100\ \text{s}^{-1}$; catalytic efficiency
$2.0\times10^{4}\ \text{dm}^{3}\ \text{mol}^{-1}\ \text{s}^{-1}$.

**Check.** $[\ce{S}] = 0.4K_{\text{M}}$, so $v$ should be
$0.4/1.4 = 0.286$ of $V_{\text{max}}$, that is $5.7\times10^{-7}$; correct.

**Where marks are lost.** Using $V_{\text{max}}$ instead of $v$; omitting the enzyme
concentration when calculating $k_{\text{cat}}$.

### 32. Preparing an acetate buffer — [Ch. 7]

**Strategy.** Use the Henderson–Hasselbalch equation to obtain the ratio, then split
the total acetate between the two forms.

**Working.**

$$
\frac{[\ce{A-}]}{[\ce{HA}]} = 10^{\mathrm{pH} - \mathrm{p}K_a}
= 10^{5.00 - 4.76} = 10^{0.24} = 1.738
$$

Let the total be $0.200\ \text{mol dm}^{-3}$:

$$
[\ce{HA}] = \frac{0.200}{1 + 1.738} = 0.0731\ \text{mol dm}^{-3}, \qquad
[\ce{A-}] = 0.200 - 0.0731 = 0.1269\ \text{mol dm}^{-3}
$$

In $0.5000\ \text{dm}^{3}$:

$$
n(\ce{NaA}) = (0.1269)(0.5000) = 6.345\times10^{-2}\ \text{mol}
$$

$$
m(\ce{NaA}) = (6.345\times10^{-2})(82.034) = 5.21\ \text{g}
$$

$$
n(\ce{HA}) = (0.0731)(0.5000) = 3.655\times10^{-2}\ \text{mol}
$$

$$
m(\ce{HA}) = (3.655\times10^{-2})(60.052) = 2.19\ \text{g}
$$

**Answer.** $5.21\ \text{g}$ of sodium acetate and $2.19\ \text{g}$ of acetic acid
(about $2.09\ \text{cm}^{3}$ of glacial acid, density $1.05\ \text{g cm}^{-3}$).

**Check.** The ratio $0.1269/0.0731 = 1.74$, which reproduces pH 5.00; the masses sum
to the expected total acetate of $0.100\ \text{mol}$.

**Where marks are lost.** Using the ratio as a mole fraction; forgetting to multiply by
the flask volume.

### 33. Solubility of magnesium hydroxide at fixed pH — [Ch. 7]

**Strategy.** The hydroxide concentration is fixed by the pH, so the common-ion form of
$K_{sp}$ applies directly.

**Working.**

$$
\mathrm{pOH} = 14.00 - 9.50 = 4.50
\qquad\Longrightarrow\qquad
[\ce{OH-}] = 10^{-4.50} = 3.16\times10^{-5}\ \text{mol dm}^{-3}
$$

$$
\ce{Mg(OH)2(s) <=> Mg^2+(aq) + 2OH-(aq)}
$$

$$
s = [\ce{Mg^2+}] = \frac{K_{sp}}{[\ce{OH-}]^{2}}
= \frac{5.6\times10^{-12}}{(3.16\times10^{-5})^{2}}
= \frac{5.6\times10^{-12}}{1.00\times10^{-9}} = 5.6\times10^{-3}\ \text{mol dm}^{-3}
$$

In pure water, where $[\ce{OH-}] = 2s$:

$$
s = \sqrt[3]{\frac{K_{sp}}{4}} = \sqrt[3]{1.40\times10^{-12}}
= 1.12\times10^{-4}\ \text{mol dm}^{-3}
$$

**Answer.** $s = 5.6\times10^{-3}\ \text{mol dm}^{-3}$ at pH 9.50, against
$1.1\times10^{-4}\ \text{mol dm}^{-3}$ in pure water; the solubility is about fifty
times larger in the buffered solution.

**Check.** The common ion here is hydroxide, and lowering $[\ce{OH-}]$ by raising the
pH from the natural value increases solubility, as the calculation shows.

**Where marks are lost.** Using $K_{sp} = 4s^{3}$ when the hydroxide concentration is
fixed externally; forgetting that pH 9.50 means pOH 4.50 at 25 °C.

### 34. Nernst equation for the Daniell cell at non-standard concentrations — [Ch. 8]

**Strategy.** Write the cell reaction, identify $z$ and $Q$, then apply the 298 K form
of the Nernst equation.

**Working.**

$$
\ce{Zn(s) + Cu^2+(aq) -> Zn^2+(aq) + Cu(s)}
$$

$$
z = 2, \qquad Q = \frac{[\ce{Zn^2+}]}{[\ce{Cu^2+}]} = \frac{0.010}{0.100} = 0.100
$$

$$
E = E^{\circ} - \frac{0.0592}{z}\log_{10}Q
= 1.10 - \frac{0.0592}{2}\log_{10}(0.100)
$$

$$
E = 1.10 - (0.0296)(-1.000) = 1.13\ \text{V}
$$

**Answer.** $E = 1.13\ \text{V}$ at $298\ \text{K}$.

**Check.** $[\ce{Zn^2+}]$ is lower than $[\ce{Cu^2+}]$, which favours the forward
reaction, so $E$ must exceed $E^{\circ}$; it does.

**Where marks are lost.** Omitting the factor $z = 2$; inverting $Q$ and obtaining
$1.07\ \text{V}$.

### 35. Crystal-field splitting from an absorption maximum — [Ch. 9]

**Strategy.** For a $d^{1}$ ion the single absorption corresponds to the full
$\Delta_o$, so convert wavelength to energy and wavenumber.

**Working.**

$$
\tilde{\nu} = \frac{1}{\lambda} = \frac{1}{500\times10^{-7}\ \text{cm}}
= 2.00\times10^{4}\ \text{cm}^{-1}
$$

$$
\Delta_o = \frac{hc}{\lambda}
= \frac{(6.626\times10^{-34})(2.998\times10^{8})}{500\times10^{-9}}
= 3.973\times10^{-19}\ \text{J}
$$

$$
\Delta_o = (3.973\times10^{-19})(6.022\times10^{23})
= 2.39\times10^{5}\ \text{J mol}^{-1}
$$

**Answer.** $\Delta_o = 20\,000\ \text{cm}^{-1} = 239\ \text{kJ mol}^{-1}$.

**Check.** $20\,000\ \text{cm}^{-1}$ is the value quoted for
$\ce{[Ti(H2O)6]^3+}$ in the chapter, so the arithmetic reproduces the expected
magnitude.

**Where marks are lost.** Using $\lambda$ in nanometres in $hc/\lambda$; forgetting that
the wavenumber must be in $\text{cm}^{-1}$, not $\text{m}^{-1}$.

### 36. Force constant of a carbonyl bond — [Ch. 10]

**Strategy.** Use the harmonic-oscillator relation
$\tilde{\nu} = (1/2\pi c)\sqrt{k/\mu}$ and solve for $k$.

**Working.**

$$
\mu = \frac{m_1m_2}{m_1 + m_2}
= \frac{(12.011)(15.999)}{12.011 + 15.999}\ \text{u}
= 6.860\ \text{u}
$$

$$
\mu = (6.860)(1.661\times10^{-27}) = 1.139\times10^{-26}\ \text{kg}
$$

$$
k = (2\pi c\tilde{\nu})^{2}\mu
$$

$$
2\pi c\tilde{\nu} = 2\pi(2.998\times10^{10}\ \text{cm s}^{-1})(1700\ \text{cm}^{-1})
= 3.202\times10^{14}\ \text{rad s}^{-1}
$$

$$
k = (3.202\times10^{14})^{2}(1.139\times10^{-26})
= 1.17\times10^{3}\ \text{N m}^{-1}
$$

**Answer.** $k = 1.17\times10^{3}\ \text{N m}^{-1}$.

**Check.** Carbonyl force constants are typically
$1.0$–$1.5\times10^{3}\ \text{N m}^{-1}$, so the result is in the expected range.

**Where marks are lost.** Using $c$ in $\text{m s}^{-1}$ with $\tilde{\nu}$ in
$\text{cm}^{-1}$; forgetting to convert the reduced mass from atomic mass units.

---

## Part D — Advanced problems

### 37. Electronic structure and magnetism of iron ions — [Ch. 2]

**Strategy.** Remove electrons from the highest-energy orbitals, then apply Hund's rule
and the spin-only formula.

**Working.** (a) Neutral iron is $[\ce{Ar}]3d^{6}4s^{2}$. Removing the two $4s$
electrons gives

$$
\ce{Fe^3+}: [\ce{Ar}]3d^{5}
$$

(b) For a half-filled $d$ shell, $S = 5/2$ and $L = 0$, so the term symbol is
$^{2S+1}L_J = {}^{6}S_{5/2}$.

(c) All five $3d$ orbitals are singly occupied:

$$
n = 5, \qquad \mu = \sqrt{5(5+2)} = 5.92\ \mu_{\text{B}}
$$

(d) High-spin $\ce{Fe^2+}$ is $[\ce{Ar}]3d^{6}$ with four unpaired electrons
($t_{2g}^{4}e_{g}^{2}$ in an octahedral field):

$$
n = 4, \qquad \mu = \sqrt{4(4+2)} = 4.90\ \mu_{\text{B}}
$$

**Answer.** (a) $[\ce{Ar}]3d^{5}$; (b) ${}^{6}S_{5/2}$; (c) five unpaired electrons,
$\mu = 5.92\ \mu_{\text{B}}$; (d) four unpaired electrons,
$\mu = 4.90\ \mu_{\text{B}}$.

**Check.** The two moments differ by about $1\ \mu_{\text{B}}$, which is the
characteristic magnetic signature used to distinguish iron(III) from iron(II) in
susceptibility measurements.

**Where marks are lost.** Writing $[\ce{Ar}]3d^{3}4s^{2}$ for $\ce{Fe^3+}$ by removing
$3d$ electrons; using $n(n+2)$ without the square root.

### 38. Dioxygen, dioxygenyl and superoxide compared — [Ch. 3]

**Strategy.** Add or remove electrons from the $\pi^{*}$ level of the $\ce{O2}$ scheme
and recompute bond order, spin and length.

**Working.** The valence configuration of $\ce{O2}$ is
$\sigma_{2s}^{2}\sigma_{2s}^{*2}\sigma_{2p}^{2}\pi_{2p}^{4}\pi_{2p}^{*2}$.

$$
\ce{O2}: \text{BO} = \frac{8-4}{2} = 2.0,\quad 2\ \text{unpaired},\ \text{paramagnetic}
$$

$$
\ce{O2+}: \pi^{*1},\quad \text{BO} = \frac{8-3}{2} = 2.5,\quad 1\ \text{unpaired},\ \text{paramagnetic}
$$

$$
\ce{O2-}: \pi^{*3},\quad \text{BO} = \frac{8-5}{2} = 1.5,\quad 1\ \text{unpaired},\ \text{paramagnetic}
$$

Bond length decreases as bond order increases:

$$
\ce{O2+} < \ce{O2} < \ce{O2-}
$$

**Answer.** Bond orders 2.5, 2.0 and 1.5 for $\ce{O2+}$, $\ce{O2}$ and $\ce{O2-}$;
all three are paramagnetic; bond lengths increase in the order
$\ce{O2+} < \ce{O2} < \ce{O2-}$.

**Check.** The $\pi^{*}$ orbital is antibonding, so adding an electron must weaken and
lengthen the bond, while removing one must strengthen and shorten it; the calculated
orders do exactly that.

**Where marks are lost.** Assuming $\ce{O2-}$ is diamagnetic because it has an even
number of electrons (Hund's rule leaves one unpaired); ranking bond lengths by charge
rather than by bond order.

### 39. Gibbs energy, equilibrium constant and reaction quotient — [Ch. 4]

**Strategy.** Use $\Delta G^{\circ} = -RT\ln K$ and
$\Delta G = \Delta G^{\circ} + RT\ln Q$.

**Working.** (a)

$$
\ln K = -\frac{\Delta G^{\circ}}{RT}
= \frac{25\,000}{(8.314)(298.15)} = 10.086
$$

$$
K = e^{10.086} = 2.4\times10^{4}
$$

(b)

$$
\Delta G = \Delta G^{\circ} + RT\ln Q
= -25.0 + \frac{(8.314)(298.15)\ln(10.0)}{1000}
$$

$$
\Delta G = -25.0 + 5.71 = -19.3\ \text{kJ mol}^{-1}
$$

(c) $\Delta G < 0$, so the forward reaction is spontaneous under these conditions, and
the system moves towards products until $Q = K$.

**Answer.** (a) $K = 2.4\times10^{4}$; (b) $\Delta G = -19.3\ \text{kJ mol}^{-1}$;
(c) net change towards products.

**Check.** $Q = 10 \ll K = 2.4\times10^{4}$, so the reaction quotient is far below
equilibrium and the forward direction is expected; the sign of $\Delta G$ agrees with
that comparison.

**Where marks are lost.** Using $\log_{10}$ instead of $\ln$; forgetting that $Q = 10$
does not make $\Delta G$ equal to $\Delta G^{\circ}$.

### 40. Activation Gibbs energy from transition-state theory — [Ch. 5]

**Strategy.** Rearrange $k = (k_{\text{B}}T/h)\exp(-\Delta G^{\ddagger}/RT)$ for
$\Delta G^{\ddagger}$.

**Working.**

$$
\frac{k_{\text{B}}T}{h} = \frac{(1.381\times10^{-23})(298)}{6.626\times10^{-34}}
= 6.21\times10^{12}\ \text{s}^{-1}
$$

$$
\frac{k}{k_{\text{B}}T/h} = \frac{1.0\times10^{-3}}{6.21\times10^{12}}
= 1.61\times10^{-16}
$$

$$
\Delta G^{\ddagger} = -RT\ln(1.61\times10^{-16})
= -(8.314)(298)(-36.37)
= 9.01\times10^{4}\ \text{J mol}^{-1}
$$

**Answer.** $\Delta G^{\ddagger} = 90.1\ \text{kJ mol}^{-1}$ at $298\ \text{K}$.

**Check.** For a first-order reaction at room temperature, each
$5.7\ \text{kJ mol}^{-1}$ of $\Delta G^{\ddagger}$ changes $k$ by a factor of ten,
since $2.303RT = 5.71\ \text{kJ mol}^{-1}$; $90.1/5.71 = 15.8$, and
$10^{-15.8} \approx 1.6\times10^{-16}$, consistent.

**Where marks are lost.** Omitting the $k_{\text{B}}T/h$ prefactor, which changes the
answer by about $70\ \text{kJ mol}^{-1}$; using $h$ instead of $\hbar$ in the prefactor.

### 41. Rate enhancement and turnover frequency — [Ch. 6]

**Strategy.** Use the exponential relation between rate ratio and barrier lowering,
then the definition of turnover frequency.

**Working.** (a)

$$
\frac{k_{\text{cat}}}{k_{\text{uncat}}}
= \exp\!\left(\frac{\Delta\Delta G^{\ddagger}}{RT}\right)
= \exp\!\left(\frac{30\,000}{(8.314)(298.15)}\right)
= e^{12.10}
$$

$$
\frac{k_{\text{cat}}}{k_{\text{uncat}}} = 1.8\times10^{5}
$$

(b)

$$
\mathrm{TOF} = \frac{n_{\text{product}}}{n_{\text{sites}}\,t}
= \frac{0.500\ \text{mol}}{(1.00\times10^{-4}\ \text{mol})(7200\ \text{s})}
= 0.694\ \text{s}^{-1}
$$

**Answer.** (a) $1.8\times10^{5}$; (b) $\mathrm{TOF} = 0.694\ \text{s}^{-1}$.

**Check.** A $30\ \text{kJ mol}^{-1}$ lowering corresponds to about twelve
$RT$ units, and $e^{12}$ is of order $10^{5}$; the answer is consistent.

**Where marks are lost.** Using $\log_{10}$ rather than $\ln$; reporting TOF in
$\text{mol s}^{-1}$ instead of $\text{s}^{-1}$.

### 42. Buffer pH after addition of strong acid — [Ch. 7]

**Strategy.** Convert the added acid into a stoichiometric change in the amounts of
$\ce{HA}$ and $\ce{A-}$, then apply the Henderson–Hasselbalch equation to the new
ratio.

**Working.** Initial amounts:

$$
n(\ce{HA}) = (0.100)(0.2500) = 2.50\times10^{-2}\ \text{mol}
$$

$$
n(\ce{A-}) = (0.150)(0.2500) = 3.75\times10^{-2}\ \text{mol}
$$

$$
n(\ce{H+})_{\text{added}} = (1.00)(0.0100) = 1.00\times10^{-2}\ \text{mol}
$$

After reaction:

$$
n(\ce{HA}) = 2.50\times10^{-2} + 1.00\times10^{-2} = 3.50\times10^{-2}\ \text{mol}
$$

$$
n(\ce{A-}) = 3.75\times10^{-2} - 1.00\times10^{-2} = 2.75\times10^{-2}\ \text{mol}
$$

$$
\mathrm{pH} = 5.00 + \log_{10}\frac{2.75}{3.50}
= 5.00 - 0.105 = 4.90
$$

The same amount of acid in $250.0\ \text{cm}^{3}$ of water would give, after dilution
to $260.0\ \text{cm}^{3}$,

$$
[\ce{H+}] = \frac{1.00\times10^{-2}}{0.2600} = 3.85\times10^{-2}\ \text{mol dm}^{-3},
\qquad \mathrm{pH} = 1.41
$$

**Answer.** Buffer pH $4.90$; the pH of the unbuffered solution would be $1.41$, a
change of about $3.5$ units.

**Check.** The buffer ratio changed from $1.50$ to $0.786$, and
$\log_{10}(0.786) = -0.105$, exactly the shift observed.

**Where marks are lost.** Adding the acid to both concentrations; forgetting to convert
the volume to $\text{dm}^{3}$ when computing the initial amounts.

### 43. Electrode potential, Gibbs energy and a concentration cell — [Ch. 8]

**Strategy.** Apply the Nernst equation to a single electrode, convert to $\Delta G$
with $z = 1$, then combine two silver electrodes of different concentration.

**Working.** (a) For $\ce{Ag+ + e- -> Ag}$ with $z = 1$:

$$
E = E^{\circ} + 0.0592\log_{10}[\ce{Ag+}]
= 0.80 + 0.0592\log_{10}(1.0\times10^{-3})
$$

$$
E = 0.80 - 0.178 = 0.622\ \text{V}
$$

(b)

$$
\Delta G = -zFE = -(1)(96\,485)(0.622) = -6.00\times10^{4}\ \text{J mol}^{-1}
$$

(c) For the concentration cell, the standard potential cancels and

$$
E = \frac{0.0592}{1}\log_{10}\frac{[\ce{Ag+}]_{\text{concentrated}}}{[\ce{Ag+}]_{\text{dilute}}}
= 0.0592\log_{10}\frac{1.0}{1.0\times10^{-3}}
= 0.178\ \text{V}
$$

**Answer.** (a) $E = 0.622\ \text{V}$; (b) $\Delta G = -60.0\ \text{kJ mol}^{-1}$;
(c) $E_{\text{cell}} = 0.178\ \text{V}$.

**Check.** The dilute electrode is the anode (oxidation of Ag to $\ce{Ag+}$), so the
cell drives the concentrations towards equality; the potential is the same magnitude as
the Nernst shift of the single electrode, as it must be.

**Where marks are lost.** Using $z = 2$ for a one-electron couple; adding the standard
potentials in part (c), which are identical and cancel.

### 44. High-spin against low-spin iron(III) complexes — [Ch. 9]

**Strategy.** Compare $\Delta_o$ with $P$ for each complex, compute the CFSE from
$(-0.4n_{t_{2g}} + 0.6n_{e_g})\Delta_o + n_{\text{pairs}}P$, then convert $\Delta_o$ to
a wavelength.

**Working.** (a) For $\ce{[Fe(CN)6]^3-}$, $\Delta_o = 24\,000\ \text{cm}^{-1} > P$,
so the complex is low-spin ($t_{2g}^{5}$, one unpaired electron). For
$\ce{[Fe(H2O)6]^3+}$, $\Delta_o = 14\,000\ \text{cm}^{-1} < P$, so it is high-spin
($t_{2g}^{3}e_{g}^{2}$, five unpaired electrons).

(b) High-spin $d^{5}$:

$$
\text{CFSE} = [3(-0.4) + 2(+0.6)]\Delta_o = 0
$$

Low-spin $d^{5}$:

$$
\text{CFSE} = 5(-0.4\Delta_o) + 2P = -2.0(24\,000) + 2(21\,000)
= -48\,000 + 42\,000 = -6.0\times10^{3}\ \text{cm}^{-1}
$$

(c)

$$
\lambda_{\max} = \frac{1}{24\,000\ \text{cm}^{-1}} = 4.17\times10^{-5}\ \text{cm}
= 417\ \text{nm}
$$

The complex absorbs in the violet, so it appears yellow.

**Answer.** (a) Cyanide complex low-spin, aqua complex high-spin;
(b) CFSE $= 0$ for the high-spin ion and $-6.0\times10^{3}\ \text{cm}^{-1}$ for the
low-spin ion; (c) $\lambda_{\max} = 417\ \text{nm}$, yellow solution.

**Check.** The low-spin form is stabilised by $6.0\times10^{3}\ \text{cm}^{-1}$ relative
to the high-spin form, which is consistent with $\Delta_o - P = 3000\ \text{cm}^{-1}$
per electron pair formed (two pairs give $6000$).

**Where marks are lost.** Counting the pairing energy once instead of twice for the
low-spin $d^{5}$ case; forgetting that a $d^{5}$ high-spin ion has zero CFSE.

### 45. Beer–Lambert law with dilution — [Ch. 10]

**Strategy.** Test the linearity of $A$ with concentration, then convert absorbance to
concentration and concentration to mass.

**Working.** (a) A fivefold dilution should reduce the absorbance fivefold:

$$
\frac{0.450}{5} = 0.090
$$

which is the measured value, so the solution obeys the Beer–Lambert law over this
range.

(b) From $A = \varepsilon bc$ for the original solution:

$$
c = \frac{A}{\varepsilon b}
= \frac{0.450}{(2.50\times10^{4})(1.00)}
= 1.80\times10^{-5}\ \text{mol dm}^{-3}
$$

(c)

$$
n = cV = (1.80\times10^{-5})(0.2500) = 4.50\times10^{-6}\ \text{mol}
$$

$$
m = nM = (4.50\times10^{-6})(180) = 8.10\times10^{-4}\ \text{g}
$$

**Answer.** (a) linear within the data; (b)
$c = 1.80\times10^{-5}\ \text{mol dm}^{-3}$; (c) $m = 0.810\ \text{mg}$.

**Check.** The diluted solution gives
$c = 0.090/(2.50\times10^{4}) = 3.6\times10^{-6}\ \text{mol dm}^{-3}$, and
$5 \times 3.6\times10^{-6} = 1.8\times10^{-5}$, consistent.

**Where marks are lost.** Using the diluted absorbance for the original concentration;
forgetting that absorbance is dimensionless and $\varepsilon$ carries the units.

### 46. Aluminium electrolysis: mass, energy and specific energy — [Ch. 8]

**Strategy.** Convert charge to amount of aluminium with $z = 3$, then compute the
electrical energy from $Q$ and the applied voltage.

**Working.**

$$
Q = It = (5.00\ \text{A})(3.00 \times 3600\ \text{s}) = 5.40\times10^{4}\ \text{C}
$$

$$
n(\ce{Al}) = \frac{Q}{zF} = \frac{5.40\times10^{4}}{(3)(96\,485)}
= 0.1866\ \text{mol}
$$

$$
m(\ce{Al}) = (0.1866)(26.982) = 5.03\ \text{g}
$$

$$
E_{\text{electrical}} = QV = (5.40\times10^{4})(5.0) = 2.70\times10^{5}\ \text{J}
$$

$$
\frac{E}{m} = \frac{2.70\times10^{5}\ \text{J}}{5.03\times10^{-3}\ \text{kg}}
= 5.4\times10^{7}\ \text{J kg}^{-1}
$$

**Answer.** (a) $m = 5.03\ \text{g}$; (b) $270\ \text{kJ}$;
(c) $54\ \text{MJ kg}^{-1}$.

**Check.** Real Hall–Héroult cells consume roughly
$13$–$15\ \text{kWh kg}^{-1}$, which is $47$–$54\ \text{MJ kg}^{-1}$; the calculation
reproduces the industrial figure, which is why aluminium production is sited near cheap
electricity.

**Where marks are lost.** Using $z = 2$ from the oxide stoichiometry instead of the
three electrons per aluminium; omitting the cell voltage and reporting charge instead
of energy.

---

## Part E — Calculation problems

### 47. Uncertainty principle for a confined electron — [Ch. 1]

**Strategy.** Use $\sigma_x\sigma_p \ge \hbar/2$ with $\Delta x$ as the confinement
width, then convert momentum to speed.

**Working.**

$$
\Delta p \ge \frac{\hbar}{2\Delta x}
= \frac{1.055\times10^{-34}}{2(1.0\times10^{-10})}
= 5.27\times10^{-25}\ \text{kg m s}^{-1}
$$

$$
\Delta v = \frac{\Delta p}{m_e}
= \frac{5.27\times10^{-25}}{9.109\times10^{-31}}
= 5.79\times10^{5}\ \text{m s}^{-1}
$$

**Answer.** $\Delta p \ge 5.3\times10^{-25}\ \text{kg m s}^{-1}$;
$\Delta v \ge 5.8\times10^{5}\ \text{m s}^{-1}$ (about $580\ \text{km s}^{-1}$).

**Check.** An electron confined to an atomic diameter cannot be at rest; the estimated
speed is of the order of $10^{6}\ \text{m s}^{-1}$, which is the scale of electron
motion in atoms.

**Where marks are lost.** Using $h$ instead of $\hbar$; using $\Delta x = 2\times10^{-10}$
without noting that the width definition changes the numerical prefactor.

### 48. Emission of $\ce{He+}$ — [Ch. 2]

**Strategy.** Use the hydrogenic energy levels with $Z = 2$.

**Working.**

$$
\Delta E = Z^{2}R_{\text{H}}\left(\frac{1}{1^{2}} - \frac{1}{2^{2}}\right)
= 4(2.1799\times10^{-18})(0.7500)
= 6.540\times10^{-18}\ \text{J}
$$

$$
\lambda = \frac{hc}{\Delta E}
= \frac{(6.626\times10^{-34})(2.998\times10^{8})}{6.540\times10^{-18}}
= 3.04\times10^{-8}\ \text{m}
$$

**Answer.** $\Delta E = 6.54\times10^{-18}\ \text{J}$; $\lambda = 30.4\ \text{nm}$.

**Check.** The hydrogen Lyman-$\alpha$ line is at $121.6\ \text{nm}$; dividing by
$Z^{2} = 4$ gives $30.4\ \text{nm}$, exactly as found.

**Where marks are lost.** Omitting $Z^{2}$; using the Rydberg constant in
$\text{cm}^{-1}$ with $h$ in $\text{J s}$.

### 49. Entropy and Gibbs energy of ammonia synthesis — [Ch. 4]

**Strategy.** Sum standard entropies with stoichiometric coefficients, then combine with
the given enthalpy.

**Working.**

$$
\Delta S^{\circ} = 2(192.8) - [191.6 + 3(130.7)]
= 385.6 - 583.7 = -198.1\ \text{J K}^{-1}\ \text{mol}^{-1}
$$

$$
\Delta G^{\circ} = -92.4 - (298.15)(-0.1981) = -92.4 + 59.1
= -33.3\ \text{kJ mol}^{-1}
$$

$$
T_{\text{cross}} = \frac{-92.4}{-0.1981} = 466\ \text{K}
$$

**Answer.** $\Delta S^{\circ} = -198.1\ \text{J K}^{-1}\ \text{mol}^{-1}$;
$\Delta G^{\circ}_{298} = -33.3\ \text{kJ mol}^{-1}$; the reaction becomes
non-spontaneous above about $466\ \text{K}$.

**Check.** At $700\ \text{K}$,
$\Delta G^{\circ} = -92.4 + 700(0.1981) = +46.3\ \text{kJ mol}^{-1}$, so the industrial
compromise at about $700\ \text{K}$ accepts a thermodynamically unfavourable reaction
because high pressure and continuous removal of ammonia drive it.

**Where marks are lost.** Subtracting the product entropy; forgetting that $\Delta S^{\circ}$
must be in $\text{kJ K}^{-1}\ \text{mol}^{-1}$ before combining with $\Delta H^{\circ}$.

### 50. Pre-exponential factor and activation Gibbs energy — [Ch. 5]

**Strategy.** Obtain $A$ from the Arrhenius equation at one temperature, then use the
Eyring equation for $\Delta G^{\ddagger}$.

**Working.**

$$
A = k\exp\!\left(\frac{E_a}{RT}\right)
= (2.0\times10^{-4})\exp\!\left(\frac{80\,000}{(8.314)(298.15)}\right)
$$

$$
\frac{80\,000}{(8.314)(298.15)} = 32.27, \qquad e^{32.27} = 1.03\times10^{14}
$$

$$
A = (2.0\times10^{-4})(1.03\times10^{14}) = 2.1\times10^{10}\ \text{s}^{-1}
$$

$$
\Delta G^{\ddagger} = -RT\ln\!\left(\frac{kh}{k_{\text{B}}T}\right)
= -(8.314)(298.15)\ln\!\left(\frac{2.0\times10^{-4}}{6.21\times10^{12}}\right)
$$

$$
\Delta G^{\ddagger} = -(8.314)(298.15)(-38.08) = 9.41\times10^{4}\ \text{J mol}^{-1}
$$

**Answer.** $A = 2.1\times10^{10}\ \text{s}^{-1}$;
$\Delta G^{\ddagger} = 94.1\ \text{kJ mol}^{-1}$.

**Check.** The pre-exponential factor is about two orders of magnitude below
$k_{\text{B}}T/h = 6.2\times10^{12}\ \text{s}^{-1}$, which implies a negative entropy of
activation, as expected for a unimolecular step with a tight transition state.

**Where marks are lost.** Using $\log_{10}$ in the Eyring expression; mixing
$\text{kJ}$ and $\text{J}$ in the exponential.

### 51. Langmuir–Hinshelwood rate — [Ch. 6]

**Strategy.** Compute each fractional coverage from the Langmuir isotherm with a shared
denominator, then multiply by $k$.

**Working.**

$$
K_{\text{A}}p_{\text{A}} = (5.0\times10^{-5})(1.0\times10^{4}) = 0.50
$$

$$
K_{\text{B}}p_{\text{B}} = (2.0\times10^{-5})(1.0\times10^{4}) = 0.20
$$

$$
\theta_{\text{A}} = \frac{0.50}{1 + 0.50 + 0.20} = 0.294
$$

$$
\theta_{\text{B}} = \frac{0.20}{1.70} = 0.118
$$

$$
r = k\theta_{\text{A}}\theta_{\text{B}}
= (1.5\times10^{-3})(0.294)(0.118)
= 5.2\times10^{-5}\ \text{mol m}^{-2}\ \text{s}^{-1}
$$

**Answer.** $\theta_{\text{A}} = 0.294$, $\theta_{\text{B}} = 0.118$;
$r = 5.2\times10^{-5}\ \text{mol m}^{-2}\ \text{s}^{-1}$.

**Check.** The two coverages sum to $0.41$, leaving 59 % of the surface free, so the
low-coverage approximation is reasonable but not exact; the full isotherm was used, so
the result is valid.

**Where marks are lost.** Using separate denominators for the two coverages; forgetting
that the sites are shared, which is the whole content of the competitive isotherm.

### 52. pH of an amphiprotic hydrogen carbonate solution — [Ch. 7]

**Strategy.** For an amphiprotic species with no other source of acid or base,
$\mathrm{pH} \approx \tfrac{1}{2}(\mathrm{p}K_{a1} + \mathrm{p}K_{a2})$.

**Working.**

$$
\mathrm{pH} = \frac{1}{2}(6.35 + 10.33) = \frac{16.68}{2} = 8.34
$$

**Answer.** $\mathrm{pH} = 8.34$.

**Check.** The value lies between the two $\mathrm{p}K_a$ values and is basic, as
expected for a solution of sodium hydrogen carbonate; the approximation requires
$c \gg K_{a1}$ and $K_{a2}c \gg K_w$, both satisfied at
$0.100\ \text{mol dm}^{-3}$. Treating the ion as a simple weak acid with $K_{a2}$ alone
would give pH 5.67, which shows why both equilibria must be combined.

**Where marks are lost.** Using only $\mathrm{p}K_{a2}$ and treating the ion as a weak
base, which gives about 8.3 by a different route but for the wrong reason; averaging the
$K_a$ values instead of the $\mathrm{p}K_a$ values.

### 53. Electrolysis of water: amount, volume and efficiency — [Ch. 8]

**Strategy.** Convert charge to amount of hydrogen with $z = 2$, then compare the
electrical energy with the enthalpy stored.

**Working.**

$$
Q = It = (10.0)(7200) = 7.20\times10^{4}\ \text{C}
$$

$$
n(\ce{H2}) = \frac{Q}{zF} = \frac{7.20\times10^{4}}{(2)(96\,485)}
= 0.3731\ \text{mol}
$$

$$
V = nV_{\text{m}} = (0.3731)(22.71) = 8.47\ \text{dm}^{3}
$$

$$
E_{\text{electrical}} = QV_{\text{applied}} = (7.20\times10^{4})(2.00)
= 1.44\times10^{5}\ \text{J}
$$

$$
E_{\text{stored}} = n\Delta H = (0.3731)(285.8) = 106.6\ \text{kJ}
$$

$$
\eta = \frac{106.6}{144.0} \times 100\,\% = 74.1\,\%
$$

**Answer.** (a) $n(\ce{H2}) = 0.373\ \text{mol}$, $V = 8.47\ \text{dm}^{3}$ at STP;
(b) $144\ \text{kJ}$; (c) $\eta = 74.1\,\%$.

**Check.** The thermoneutral voltage is $\Delta H/(zF) = 285\,800/192\,970 = 1.48\ \text{V}$,
and $1.48/2.00 = 74.1\,\%$, exactly the efficiency obtained; the reversible voltage of
$1.23\ \text{V}$ would give the Gibbs-energy efficiency, which is lower.

**Where marks are lost.** Using $z = 1$ for hydrogen; forgetting that the volume at STP
requires $22.71\ \text{dm}^{3}\ \text{mol}^{-1}$ and not $24.79$.

### 54. Colour from crystal-field splitting — [Ch. 9]

**Strategy.** Convert $\Delta_o$ in $\text{cm}^{-1}$ to wavelength, then to molar energy,
and use the complementary colour.

**Working.**

$$
\lambda = \frac{1}{\tilde{\nu}} = \frac{1}{22\,000\ \text{cm}^{-1}}
= 4.55\times10^{-5}\ \text{cm} = 455\ \text{nm}
$$

$$
E = (22\,000\ \text{cm}^{-1})(11.96\ \text{J mol}^{-1}\ \text{per cm}^{-1})
= 2.63\times10^{5}\ \text{J mol}^{-1}
$$

**Answer.** $\lambda = 455\ \text{nm}$; $E = 263\ \text{kJ mol}^{-1}$; the complex
absorbs blue light and therefore appears orange.

**Check.** $455\ \text{nm}$ lies in the blue-violet region of the visible spectrum, and
the complementary colour of blue is orange, consistent with the data given.

**Where marks are lost.** Using $1\ \text{cm}^{-1} = 11.96\ \text{kJ mol}^{-1}$ instead
of the per-$1000\ \text{cm}^{-1}$ conversion, which is a factor of 1000; quoting the
absorbed colour as the observed colour.

---

## Part F — Multiple-choice self-check

### 55. Energy ratio in a one-dimensional box — [Ch. 1]

**Strategy.** Use $E_n \propto n^{2}$ and form the ratio for the two levels.

**Answer.** **C.** $E_n \propto n^{2}$, so
$E_3/E_1 = 3^{2}/1^{2} = 9$.

**Check.** $E_3 = 9E_1$, so the $1 \to 3$ gap is eight times the $1 \to 2$ gap; the
quadratic scaling is the signature of the infinite well.

**Why the best distractor is wrong.** Option A, 3, confuses the linear dependence of the
quantum number with the quadratic dependence of the energy; the energy of a particle in
a box increases as $n^{2}$, not as $n$.

### 56. Bond order of superoxide — [Ch. 3]

**Strategy.** Count the valence electrons, place the extra one in a $\pi^{*}$ orbital,
and compute the bond order from the MO occupancy.

**Answer.** **B.** $\ce{O2-}$ has 13 valence electrons, one more than $\ce{O2}$; the
extra electron enters a $\pi^{*}$ orbital, so
$\text{BO} = (8-5)/2 = 1.5$.

**Check.** The bond order is below that of $\ce{O2}$, so the superoxide bond must be
longer and weaker; that is observed.

**Why the best distractor is wrong.** Option C, 2.0, is the bond order of neutral
$\ce{O2}$; adding an antibonding electron must lower the bond order, and the observed
lengthening of the O–O bond in superoxide confirms it.

### 57. The rate-determining step — [Ch. 5]

**Strategy.** Recall the definition of the rate-determining step and test each
statement against it.

**Answer.** **C.** The slowest step has the highest activation barrier and therefore the
smallest rate constant; it controls the flux through the mechanism and appears in the
overall rate law.

**Check.** The slowest step has the largest barrier, which need not be the first step
and need not be the most exothermic; only the barrier controls the flux.

**Why the best distractor is wrong.** Option D is plausible because the slow step often
releases the most energy in an exothermic reaction, but the height of the barrier, not
the depth of the subsequent well, determines the rate. Option A fails for mechanisms
with a fast first step, such as the dimerisation in item 30.

### 58. Buffer response to a small amount of acid — [Ch. 7]

**Strategy.** Compare the amount of acid added with the amounts of the two buffer
components, then estimate the change in the ratio.

**Answer.** **C.** The buffer contains comparable amounts of $\ce{HA}$ and $\ce{A-}$, so
$0.001\ \text{mol}$ of $\ce{HCl}$ converts only a small fraction of $\ce{A-}$ into
$\ce{HA}$; the ratio changes slightly and the pH falls by less than $0.1$ unit.

**Check.** $0.001\ \text{mol}$ against $0.100\ \text{mol}$ changes the ratio by about
1 %, and $\log_{10}(1.01) = 0.004$, so the pH shift is a few thousandths of a unit.

**Why the best distractor is wrong.** Option A treats the buffer as if it were pure
water; $0.001\ \text{mol}$ in $1\ \text{dm}^{3}$ would give pH 3 in water, but the
buffer consumes the added protons almost stoichiometrically.

### 59. Effect of increasing $[\ce{Zn^2+}]$ on the cell potential — [Ch. 8]

**Strategy.** Write the Nernst equation for the cell and inspect the sign of the term
containing $[\ce{Zn^2+}]$.

**Answer.** **B.** The Nernst equation for the cell is
$E = E^{\circ} - (0.0592/2)\log_{10}([\ce{Zn^2+}]/[\ce{Cu^2+}])$, so raising
$[\ce{Zn^2+}]$ increases the logarithmic term and decreases $E$. This is Le Châtelier's
principle applied to the cell reaction: product accumulates and the forward driving
force falls.

**Check.** A product of the cell reaction accumulating must reduce the driving force,
which is Le Châtelier's principle applied to an electrochemical cell.

**Why the best distractor is wrong.** Option A reverses the sign of the concentration
term, which is equivalent to assuming that zinc ions are reactants; zinc is oxidised, so
its ion is a product and its accumulation reduces the potential.

### 60. CFSE of an octahedral $d^{3}$ complex — [Ch. 9]

**Strategy.** Place three electrons in the $t_{2g}$ set and sum the contributions
$-0.4\Delta_o$ per electron.

**Answer.** **A.** All three electrons occupy $t_{2g}$ orbitals, each contributing
$-0.4\Delta_o$, so the CFSE is $3(-0.4\Delta_o) = -1.2\Delta_o$ and no pairing energy is
required.

**Check.** No pairing energy is needed, so the answer is purely the orbital term, and
the same formula gives $-0.8\Delta_o$ for $d^{2}$ and $-1.2\Delta_o$ only from $d^{3}$
onwards.

**Why the best distractor is wrong.** Option B, $-0.8\Delta_o$, results from filling two
$t_{2g}$ orbitals and promoting the third electron to $e_g$; that is not the $d^{3}$
ground state, because Hund's rule keeps the three electrons unpaired in the lower set.

---

## Top ten errors in this level

| # | Error | Why it costs marks | Correct habit |
|---|---|---|---|
| 1 | Treating $\Delta G$ and $\Delta G^{\circ}$ as the same quantity | Only $\Delta G^{\circ}$ fixes $K$; $\Delta G$ varies with composition | Write $\Delta G = \Delta G^{\circ} + RT\ln Q$ before substituting |
| 2 | Reversing the high-spin/low-spin criterion | Assigns the wrong configuration and magnetic moment | Low spin when $\Delta_o > P$; compare the numbers explicitly |
| 3 | Omitting $z$ from the Nernst equation | Potentials wrong by a factor of 2 or 3 | Identify the balanced electron count for the cell reaction first |
| 4 | Counting core electrons in MO bond orders | Bond order wrong by several units | Count valence electrons only |
| 5 | Reading a rate law from the stoichiometric equation | Only elementary steps have stoichiometric orders | Determine orders from experiment or from a steady-state derivation |
| 6 | Using concentrations in place of activities at high ionic strength | pH and $K$ values deviate systematically | State the ionic strength; use the Debye–Hückel correction beyond $0.01\ \text{mol dm}^{-3}$ |
| 7 | Mixing $\text{cm}^{-1}$, $\text{m}^{-1}$ and $\text{kJ mol}^{-1}$ | Answers out by factors of 100 or 1000 | Convert to SI before substituting, then convert back |
| 8 | Using the number of electrons as the box quantum number | Wrong HOMO and wrong absorption energy | Fill levels two electrons at a time and identify $n_{\text{HOMO}}$ |
| 9 | Combining $\Delta H$ in $\text{kJ}$ with $\Delta S$ in $\text{J K}^{-1}$ | Gibbs energy wrong by a factor of 1000 | Convert $\Delta S$ to $\text{kJ K}^{-1}$ first |
| 10 | Adding $E^{\circ}$ values when combining half-cells | Double-counts the driving force | Add $\Delta G^{\circ}$ values, then convert with the total $z$ |

