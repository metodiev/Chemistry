# Level 9a — Worked Solutions: Materials and Industrial Chemistry

> **Level:** 9a (Materials and Industrial Chemistry)
> **Items:** 58
> **Exercise bank:** [`../exercises/level-9a-materials-exercises.md`](../exercises/level-9a-materials-exercises.md)

Each solution gives the **Strategy** (the kind of problem), the **Working** (symbols
first, then substitution with units), the **Answer** (significant figures and units)
and a **Check** that catches the usual error. Items marked **multi-step** require at
least three dependent decisions; 28 items are so marked. **Where marks are lost** is
given wherever a predictable slip costs credit.

Conventions. Constants and molar masses are those of the exercise data sheet;
intermediate values are carried at full precision and rounded only in the Answer.
Where an item needs an assumption, the assumption is stated before the arithmetic
and its failure mode is named. Equilibrium calculations use ideal gases, Faraday
conversions use $100\ \%$ current efficiency, and corrosion rates use the
uniform-thickness model; each of these is optimistic, and the size of the optimism
is stated where it matters.

---

## Part A — Conceptual questions

### 1. Why step-growth needs high conversion and chain-growth does not

**Strategy.** Compare the point in the reaction at which long chains appear, and
express it through the Carothers equation for the step-growth case.

**Working.** In step-growth polymerisation any two molecules carrying complementary
groups react, so monomer is consumed early into dimers, trimers and oligomers. The
number-average degree of polymerisation is

$$
X_n = \frac{1}{1-p},
$$

so $X_n = 100$ requires $p = 0.99$ and $X_n = 200$ requires $p = 0.995$. The last
per cent of conversion supplies almost all of the molar mass, and the mass average
diverges faster still. In chain-growth polymerisation an initiator creates a small
population of active centres; each centre adds monomer by successive insertion and
reaches full length in milliseconds to seconds. Molar mass is fixed by the ratio of
propagation to termination, not by how much monomer has been consumed, so high
polymer exists from the first seconds of the reaction while monomer concentration
falls steadily.

The two consequences for a step-growth reactor follow directly. First, purity and
stoichiometry must be exact, because a monofunctional impurity or a $1\ \%$ excess
caps $X_n$ permanently. Second, the condensate must be removed continuously, because
the equilibrium must be driven to $p > 0.99$; a reactor that cannot remove water or
HCl cannot reach the specification, however long it runs.

**Answer.** Step-growth molar mass is a function of conversion, $X_n = 1/(1-p)$, so
$99\ \%$ conversion is a requirement; chain-growth molar mass is a function of the
initiator-to-termination balance and is established early. Step-growth therefore
demands exact stoichiometry and condensate removal.

**Check.** The same conclusion follows from the Flory distribution: the mass average
diverges as $p \to 1$, so a step-growth resin at $p = 0.95$ ($X_n = 20$) is an
oligomer, not a plastic.

**Where marks are lost.** Saying "step-growth is slow" as the explanation. Rate is
not the issue; the functional-group statistics are.

### 2. Tacticity and the properties of polypropene

**Strategy.** Connect the configuration at each stereocentre to chain regularity,
then to packing and melting.

**Working.** In polypropene the backbone carbon bearing the methyl group is a
stereocentre. **Isotactic** chains have every centre in the same configuration, so
the diads are meso ($m$) and the triads $mm$; the chain adopts a regular helical
conformation and packs into a lattice, giving a melting point near
$165\ ^\circ\mathrm{C}$, useful stiffness and solvent resistance. **Atactic** chains
have a random sequence, dominated by $mr$ triads; no lattice can accommodate the
irregular arrangement of methyl groups, so the material is amorphous, with only a
glass transition and no melting point, and it is soft and tacky.

Stereocontrol is a catalyst property. Ziegler–Natta catalysts
($\ce{TiCl4}$ on $\ce{MgCl2}$ with triethylaluminium) and metallocenes hold the
monomer at a chiral metal centre and insert it with a fixed face, giving isotactic
or syndiotactic material according to ligand symmetry. Radical polymerisation gives
no such control: the growing radical is planar and the monomer can approach either
face, so the product is atactic.

**Answer.** Isotactic chains are regular and crystalline ($T_m \approx
165\ ^\circ\mathrm{C}$); atactic chains are irregular and amorphous. Ziegler–Natta
and metallocene catalysts give stereocontrol; radical polymerisation does not.

**Check.** Commercial polypropene is isotactic, with a density near
$0.90\ \mathrm{g\ cm^{-3}}$; atactic polypropene is a by-product of older processes
and has no structural use. The contrast is a packing argument, not a molar-mass
argument.

**Where marks are lost.** Writing "isotactic is stronger because the chains are
straighter". The chains are not straight in either case; the difference is the
regularity of side-group placement, which permits crystallisation.

### 3. Surface-to-volume ratio against quantum confinement

**Strategy.** Identify the two scaling laws and match each observation to the
effect that produces it.

**Working.** The surface fraction of a sphere scales as $4d_\text{atom}/D$: it rises
as $1/D$, because the number of surface atoms grows as $D^{2}$ while the total grows
as $D^{3}$. The consequences are thermodynamic and catalytic — higher surface
energy, lower sintering temperature, more exposed low-coordination sites. The
catalytic activity of $5\ \mathrm{nm}$ gold is a surface-fraction effect.

Quantum confinement appears when the particle is smaller than the exciton Bohr
radius. The lowest transition energy is approximately

$$
E(R) = E_g + \frac{h^{2}}{8\mu R^{2}} - \frac{1.8e^{2}}{4\pi\varepsilon_0\varepsilon R},
$$

so the confinement term scales as $1/R^{2}$ and the emission of CdSe is set by
diameter. The red colour of gold colloid belongs to neither effect: it is a surface
plasmon resonance, which depends on size, shape and the dielectric environment of
the particle. A further size-dependent property that belongs to neither list is
superparamagnetism below about $20\ \mathrm{nm}$, where thermal energy overcomes the
anisotropy barrier.

**Answer.** Surface fraction scales as $1/D$ and explains catalysis; confinement
scales as $1/R^{2}$ and explains size-tunable CdSe emission. The plasmon colour of
gold is a third, electromagnetic size effect; superparamagnetism is another.

**Check.** A $5\ \mathrm{nm}$ gold particle has roughly a quarter of its atoms at
the surface yet shows no confinement shift in its $d$-band absorption, because the
conduction electrons are not confined in the same way as an exciton.

**Where marks are lost.** Attributing the colour of gold to quantum confinement. The
plasmon is a collective oscillation, not a single-particle gap.

### 4. What each size method measures

**Strategy.** State the weighting and the environment of each measurement.

**Working.** Powder XRD with the Scherrer equation,

$$
D = \frac{K\lambda}{\beta\cos\theta},
$$

measures the size of coherently diffracting domains. It is volume-weighted, it sees
only crystalline material, and it is broadened by strain as well as by size, so a
strained sample appears too small. TEM measures projected particle outlines in
vacuum and is number-weighted by whatever particles the operator counts. DLS
measures the hydrodynamic diameter through the Stokes–Einstein relation,
$D_\mathrm{h} = k_\mathrm{B}T/(3\pi\eta D_\mathrm{d})$; it is intensity-weighted, so
a small number of aggregates dominates the average, and it includes the ligand
shell. BET measures the specific surface area of the dry powder and converts it to
an equivalent spherical diameter through $S = 6/(\rho D)$.

Disagreement is therefore expected. A sample with a $17\ \mathrm{nm}$ crystallite
size and a $34\ \mathrm{nm}$ BET-equivalent diameter is an aggregate of about eight
crystallites (item 38); a DLS diameter several times the TEM diameter indicates
aggregation or a thick adsorbed layer. Reporting one number without the method
hides the structure.

**Answer.** XRD gives crystalline domain size (volume-weighted), TEM gives particle
size in vacuum (number-weighted), DLS gives hydrodynamic size in liquid
(intensity-weighted), BET gives surface-area-equivalent size (dry state).
Disagreement diagnoses aggregation, non-sphericity or polydispersity.

**Check.** The units and the weighting explain the direction of each discrepancy:
aggregates raise DLS and BET diameters but leave the Scherrer size unchanged,
because the crystallites are still $17\ \mathrm{nm}$.

**Where marks are lost.** Writing "XRD measures particle size". It measures
crystallite size; a particle may contain many crystallites.

### 5. Direct and indirect band gaps

**Strategy.** Use conservation of crystal momentum and the strength of the resulting
optical transition.

**Working.** In a direct-gap material the conduction-band minimum and the
valence-band maximum occur at the same crystal momentum, so an electron can absorb
or emit a photon without a phonon. In an indirect-gap material they occur at
different momenta, so a photon transition must be accompanied by a phonon to
conserve momentum. The three-particle process is much less probable, so the
absorption coefficient near the gap is small and radiative recombination is slow. In
silicon the radiative lifetime is long enough that non-radiative channels —
defect recombination and Auger processes — dominate, which is why silicon is a poor
LED and laser material despite decades of effort. GaAs, GaN, InP and CdTe are direct
and are the optoelectronic materials.

The same distinction sets solar-cell thickness. Direct-gap GaAs absorbs strongly
within a few micrometres, so a thin film suffices; indirect silicon absorbs weakly
near $1.12\ \mathrm{eV}$ and needs hundreds of micrometres, which is why silicon
wafers are several hundred micrometres thick.

**Answer.** GaAs is direct: photon emission needs no phonon, so it emits efficiently.
Silicon is indirect: momentum conservation requires a phonon, radiative
recombination is slow and non-radiative processes win. The indirect gap also
explains the thick silicon wafer.

**Check.** The $1.42\ \mathrm{eV}$ gap of GaAs corresponds to $873\ \mathrm{nm}$
(item 17), in the near infrared; practical visible emitters use alloys with larger
gaps, such as $\ce{InGaN}$ near $2.7\ \mathrm{eV}$.

**Where marks are lost.** Saying silicon "cannot emit light". It can, weakly; the
issue is the competition with non-radiative recombination.

### 6. Why ALD, not CVD, for a gate dielectric

**Strategy.** Contrast a flux-limited deposition with a surface-saturated one.

**Working.** CVD decomposes or reacts precursors continuously, so the film grows as
long as precursor arrives. In a trench, the precursor is consumed at the mouth and
depleted down the sidewall, so the film is thicker at the top than at the bottom;
the profile is a reactor-engineering compromise, not a surface limit. ALD separates
the chemistry into two self-limiting half-reactions, each of which stops when the
surface sites are consumed. For alumina the overall reaction is

$$
\ce{2Al(CH3)3(g) + 3H2O(g) -> Al2O3(s) + 6CH4(g)}.
$$

In the first half-reaction, $\ce{Al(CH3)3}$ reacts with surface hydroxyls and
saturates at one monolayer of methylated aluminium; excess precursor does not react
because there are no sites left. In the second, water hydrolyses the methyl groups
and restores hydroxyls. The growth per cycle is fixed by the surface chemistry —
approximately $0.1\ \mathrm{nm}$ for alumina — not by flux or time, so the same
thickness is obtained at the top and the bottom of a high-aspect-ratio trench.

A gate dielectric must be pinhole-free, precisely thin and conformal over fin or
nanosheet geometries, because leakage depends exponentially on thickness. ALD gives
that control; a single CVD step gives a thickness gradient and, at the thinnest
point, a leakage path.

**Answer.** ALD is self-limiting in two half-reactions, so thickness is set by
surface saturation and is uniform on high-aspect-ratio features; CVD is flux-limited
and gives a thickness gradient. Gate dielectrics need pinhole-free, angstrom-level
uniformity.

**Check.** The characteristic ALD signature is a constant growth per cycle over a
range of dose times — the plateau in a saturation curve. CVD has no such plateau.

**Where marks are lost.** Describing ALD as "slow CVD". The defining feature is
self-limitation, not rate.

### 7. Capacity fade in lithium-ion cells

**Strategy.** Separate loss of lithium inventory, loss of active material and
impedance rise, then assign mechanisms.

**Working.** Four mechanisms are enough to organise the problem. **SEI growth**
consumes lithium and electrolyte at the anode; it is fastest at high state of charge
and high temperature and its rate falls roughly as the square root of time.
**Lithium plating** occurs when the anode potential falls below $0\ \mathrm{V}$
versus $\ce{Li/Li+}$, typically at high charge rate, low temperature or high
loading; the plated metal reacts with electrolyte and can form dendrites.
**Particle cracking** in nickel-rich NMC and NCA follows anisotropic volume change;
cracks expose fresh surface, which forms more SEI and isolates material.
**Transition-metal dissolution**, especially manganese and cobalt, migrates to the
anode and poisons the SEI. Electrolyte oxidation at high cathode potential and
current-collector corrosion complete the list.

At high state of charge and elevated temperature, SEI growth and electrolyte
oxidation dominate; plating dominates at low temperature and high rate. A single
capacity number cannot distinguish these, because loss of lithium inventory, loss of
active material and rising impedance all reduce delivered capacity. Diagnosis needs
impedance spectroscopy, differential capacity analysis and post-mortem microscopy.

**Answer.** SEI growth, lithium plating, particle cracking and transition-metal
dissolution are the four; SEI growth and electrolyte oxidation dominate at high
state of charge and high temperature. Capacity alone conflates three distinct losses.

**Check.** SEI growth gives the familiar square-root-of-time fade; plating gives a
sudden knee and is detectable as a voltage plateau near $0\ \mathrm{V}$ on charge.
The shapes differ, which is why the mechanism can be identified from data rather
than guessed.

**Where marks are lost.** Listing "degradation" as a single cause, or claiming that
capacity fade is always due to the cathode.

### 8. Reading a Pourbaix diagram

**Strategy.** Define the three regions thermodynamically, then state what the
diagram omits.

**Working.** A Pourbaix diagram plots equilibrium potential against pH for a
metal–water system. **Immunity** is the region where the metal itself is the stable
phase, so dissolution has a positive Gibbs energy and the metal does not corrode.
**Corrosion** is the region where a soluble ion such as $\ce{Fe^{2+}}$ is stable.
**Passivation** is the region where a sparingly soluble oxide or hydroxide is stable,
so a film can form and slow the reaction.

The diagram is thermodynamic. It gives no rate, so it cannot say whether a passive
film is $1\ \mathrm{nm}$ or $100\ \mathrm{nm}$, coherent or cracked. It also assumes
a bulk, uniform environment, so it cannot represent the local chemistry of a pit or
a crevice: chloride concentrates and hydrolyses inside a pit, the local pH can fall
below $2$, and the film breaks down at a potential the diagram labels passive. That
is why stainless steel can pit in chloride at potentials where the diagram predicts
passivity.

In sound concrete the pore solution is strongly alkaline, with pH near $12.5$ to
$13.5$, so iron lies in the passive region and the reinforcement is protected by a
film. Chloride from de-icing salt or seawater destroys the film locally, and
carbonation lowers the pH towards the corrosion region; both convert a passive
system into a pitting one.

**Answer.** Immunity: metal stable; corrosion: soluble ion stable; passivation:
oxide stable. The diagram is thermodynamic and bulk-averaged, so it cannot predict
pitting or crevice attack, which depend on local chemistry and film breakdown.
Concrete protects steel by alkalinity; chloride destroys passivity.

**Check.** The water stability lines bracket the diagram; a condition outside them
means water itself is reduced or oxidised, which changes the cathodic reaction and
the corrosion potential.

**Where marks are lost.** Treating passivation as immunity. A passive metal is
thermodynamically unstable but kinetically slow; it can still pit.

### 9. Galvanic series, area ratio and a small anode

**Strategy.** Distinguish the two series by what they measure, then apply the area
ratio to a specific couple.

**Working.** The electromotive force series lists standard electrode potentials for
half-reactions at unit activity, with no allowance for films, flow or alloy
composition. The galvanic series lists measured corrosion potentials of practical
materials in a specific environment, usually flowing seawater; it therefore
includes kinetic and film effects, which is why stainless steel appears noble in
seawater although the standard potential of chromium is relatively active. Only the
galvanic series should be used to rank materials in service.

When two metals are coupled, the more active one becomes the anode. The total
galvanic current is fixed by the potential difference and the circuit resistance,
but the **anodic current density** is that current divided by the anode area. A
small anode coupled to a large cathode therefore suffers a high current density and
rapid penetration, whereas a large anode coupled to a small cathode is barely
affected. A small aluminium rivet in a large stainless-steel plate is the bad case:
aluminium is anodic to stainless steel in seawater, and the rivet's area is small,
so the rivet dissolves rapidly and may fail structurally while the plate is
untouched. Prevention is to insulate the couple, use a compatible fastener, seal the
joint or apply cathodic protection.

**Answer.** The emf series is thermodynamic and standard-state; the galvanic series
is practical and environment-specific. A small anode against a large cathode gives
a high anodic current density. The aluminium rivet corrodes rapidly; the stainless
plate is cathodically protected by the couple.

**Check.** Reversing the areas — a large aluminium plate with a small stainless
bolt — greatly reduces the rivet problem, which is why the area ratio, not just the
potential difference, is the design variable.

**Where marks are lost.** Using the emf series to rank stainless steel. The alloy's
nobility comes from its passive film, which the standard potentials do not describe.

### 10. Octane number

**Strategy.** Define the scale, then connect structure to autoignition.

**Working.** The octane number of a fuel is defined by comparison with reference
blends of isooctane (2,2,4-trimethylpentane, assigned 100) and n-heptane (assigned
0) in a standard spark-ignition engine. The **research octane number** (RON) uses
milder conditions; the **motor octane number** (MON) uses higher speed and
temperature, so it is the more severe test. The average, $(\mathrm{RON} +
\mathrm{MON})/2$, is the anti-knock index used on fuel pumps. A higher octane number
permits a higher compression ratio and therefore higher thermodynamic efficiency.

Structure controls autoignition. Highly branched paraffins and aromatics resist
autoignition and have high octane numbers; straight-chain paraffins and olefins
ignite more readily and have lower ones. Ethanol has a high RON, near 109, because
its combustion chemistry and high latent heat suppress knock, and it adds oxygen,
which reduces CO and particulate emissions; the costs are higher volatility and
possible NOx effects under some calibration regimes. Tetraethyl lead was an
effective anti-knock agent but was withdrawn because lead is neurotoxic and poisons
the three-way catalyst.

**Answer.** RON and MON are defined by reference blends under different test
conditions; branching and aromaticity raise octane, chain length lowers it. Ethanol
raises octane through its combustion chemistry and oxygen content; tetraethyl lead
was withdrawn for toxicity and catalyst poisoning.

**Check.** The scale runs from n-heptane 0 to isooctane 100, and fuels can exceed
100 because the scale is extrapolated by reference-blend matching; ethanol's rating
above 100 is therefore meaningful rather than impossible.

**Where marks are lost.** Equating octane number with energy content. Octane
measures resistance to autoignition; it says nothing about the heating value.

---

## Part B — Basic problems

### 11. Number-average, mass-average and PDI

**Strategy.** Convert each mass fraction to moles, sum, and apply the definitions of
$M_n$ and $M_w$.

**Working.** The total mass is $100\ \mathrm{g}$, so each mass is also its mass
fraction in per cent. The mole numbers are

$$
n_i = \frac{m_i}{M_i} = \frac{5}{20\,000}, \frac{15}{40\,000}, \frac{30}{60\,000},
\frac{40}{100\,000}, \frac{10}{200\,000}
= 0.250, 0.375, 0.500, 0.400, 0.050\ \mathrm{mmol},
$$

total $1.575\ \mathrm{mmol}$. Hence

$$
M_n = \frac{100\ \mathrm{g}}{1.575\times10^{-3}\ \mathrm{mol}}
= 6.35\times10^{4}\ \mathrm{g\ mol^{-1}}.
$$

For the mass average, weight each molar mass by its mass fraction:

$$
M_w = 0.05(20\,000) + 0.15(40\,000) + 0.30(60\,000) + 0.40(100\,000) + 0.10(200\,000)
= 85\,000\ \mathrm{g\ mol^{-1}}.
$$

$$
\mathrm{PDI} = \frac{M_w}{M_n} = \frac{85\,000}{63\,492} = 1.34.
$$

**Answer.** $M_n = 6.35\times10^{4}\ \mathrm{g\ mol^{-1}}$,
$M_w = 8.50\times10^{4}\ \mathrm{g\ mol^{-1}}$, PDI $= 1.34$.

**Check.** $M_w$ exceeds $M_n$ because the $200\,000$ fraction contributes
$10\ \%$ of the mass but only $3.2\ \%$ of the molecules. A PDI between $1.3$ and
$2.0$ is consistent with conventional radical polymerisation and is too broad for
living anionic polymerisation, which would approach $1 + 1/X_n$.

**Where marks are lost.** Using the mass fractions as mole fractions, which gives
$M_n = M_w$ and PDI $= 1$.

### 12. Degree of polymerisation and extent of reaction for PET

**Strategy.** Divide the molar mass by the repeat-unit mass, then invert the
Carothers equation.

**Working.** With end groups neglected,

$$
X_n = \frac{M_n}{M_0} = \frac{30\,000}{192.17} = 156.1,
$$

and the Carothers equation $X_n = 1/(1-p)$ gives

$$
p = 1 - \frac{1}{X_n} = 1 - \frac{1}{156.1} = 0.9936.
$$

**Answer.** $X_n = 156$; $p = 0.994$ (three significant figures).

**Check.** An extent of $0.994$ means that about six functional groups in a thousand
remain unreacted, which is why industrial PET polymerisation removes ethylene glycol
under vacuum and finishes in the melt or in the solid state.

**Where marks are lost.** Forgetting to subtract from 1, which gives $p = 0.0064$;
or using the monomer mass rather than the repeat-unit mass, which for PET differs by
the mass of the eliminated water.

### 13. Glass transition of plasticised PVC

**Strategy.** Apply the Fox equation with mass fractions and absolute temperatures.

**Working.** With $w_\mathrm{PVC} = 0.70$, $T_{g1} = 354\ \mathrm{K}$,
$w_\mathrm{p} = 0.30$ and $T_{g2} = 200\ \mathrm{K}$,

$$
\frac{1}{T_g} = \frac{0.70}{354} + \frac{0.30}{200}
= 1.977\times10^{-3} + 1.500\times10^{-3}
= 3.477\times10^{-3}\ \mathrm{K^{-1}},
$$

so

$$
T_g = 287.6\ \mathrm{K} = 14.5\ ^\circ\mathrm{C}.
$$

**Answer.** $T_g = 288\ \mathrm{K}$, or $14.5\ ^\circ\mathrm{C}$.

**Check.** The blend is roughly $65\ \mathrm{K}$ below the $T_g$ of PVC, which is the
point of a plasticiser: flexible PVC at room temperature sits just above its glass
transition. The calculation treats the blend as miscible and single-phase; a
plasticiser that phase-separates would give two transitions, not one.

**Where marks are lost.** Using Celsius temperatures in the Fox equation. It is
derived for absolute temperature.

### 14. Specific surface area of titania spheres

**Strategy.** Use $S = 6/(\rho D)$ with consistent SI units, then compare the
equivalent diameter implied by the measured area.

**Working.** For spheres, the area-to-mass ratio is

$$
S = \frac{A}{m} = \frac{\pi D^{2}}{\rho \pi D^{3}/6} = \frac{6}{\rho D}.
$$

With $\rho = 3.89\times10^{3}\ \mathrm{kg\ m^{-3}}$ and
$D = 20\times10^{-9}\ \mathrm{m}$,

$$
S = \frac{6}{(3.89\times10^{3})(20\times10^{-9})}
= 7.71\times10^{4}\ \mathrm{m^{2}\ kg^{-1}} = 77.1\ \mathrm{m^{2}\ g^{-1}}.
$$

The measured $50\ \mathrm{m^{2}\ g^{-1}}$ corresponds to an equivalent diameter

$$
D_\mathrm{eq} = \frac{6}{\rho S} = \frac{6}{(3.89\times10^{3})(50\times10^{3})}
= 3.1\times10^{-8}\ \mathrm{m} = 31\ \mathrm{nm}.
$$

**Answer.** $S = 77\ \mathrm{m^{2}\ g^{-1}}$ for $20\ \mathrm{nm}$ spheres; the
measured area corresponds to about $31\ \mathrm{nm}$.

**Check.** The measured area is lower than the geometric prediction, so the powder
behaves as if it were coarser: it is aggregated, has a larger primary size than
$20\ \mathrm{nm}$, or the model over-counts area that nitrogen cannot access in
tight aggregates.

**Where marks are lost.** Mixing grams and kilograms. Using $\mathrm{g\ cm^{-3}}$
with $D$ in nanometres gives an answer wrong by $10^{3}$.

### 15. Crystallite size from the Scherrer equation

**Strategy.** Convert the width to radians, halve $2\theta$, and substitute.

**Working.** $\theta = 21.5^\circ$, $\cos\theta = 0.9304$, and
$\beta = 0.50\times\pi/180 = 8.727\times10^{-3}\ \mathrm{rad}$. Then

$$
D = \frac{K\lambda}{\beta\cos\theta}
= \frac{0.90(0.15406\times10^{-9})}{(8.727\times10^{-3})(0.9304)}
= 1.71\times10^{-8}\ \mathrm{m} = 17.1\ \mathrm{nm}.
$$

**Answer.** $D = 17.1\ \mathrm{nm}$.

**Check.** The value is plausible for a nanocrystalline oxide and matches the
BET-consistent particle size only if the particles are aggregates (item 38). Two
reasons for a difference from TEM: the Scherrer size is a volume-weighted coherent
domain, not a particle, and microstrain broadens the peak as well as finite size.
Instrumental broadening should be subtracted in quadrature before the calculation.

**Where marks are lost.** Using $2\theta$ instead of $\theta$ in the cosine, or
leaving $\beta$ in degrees.

### 16. Photon energy at 520 nm

**Strategy.** Use $E = hc/\lambda$ and convert with the electronvolt.

**Working.**

$$
E = \frac{hc}{\lambda}
= \frac{(6.62607015\times10^{-34})(2.99792458\times10^{8})}{520\times10^{-9}}
= 3.820\times10^{-19}\ \mathrm{J}.
$$

$$
E = \frac{3.820\times10^{-19}}{1.602176634\times10^{-19}}
= 2.384\ \mathrm{eV}.
$$

**Answer.** $E = 3.82\times10^{-19}\ \mathrm{J} = 2.38\ \mathrm{eV}$, in the green
part of the visible spectrum.

**Check.** The shortcut $1240/\lambda(\mathrm{nm})$ gives $1240/520 =
2.38\ \mathrm{eV}$, in agreement within the rounding of the constant.

**Where marks are lost.** Using $c$ in $\mathrm{nm\ s^{-1}}$ with $\lambda$ in
metres, or forgetting that $1\ \mathrm{eV}$ is $1.602\times10^{-19}\ \mathrm{J}$.

### 17. Wavelengths for GaAs and silicon

**Strategy.** Convert the gap in electronvolts to a wavelength with $\lambda = hc/E$.

**Working.** For GaAs, $E = 1.42\times1.602176634\times10^{-19} =
2.275\times10^{-19}\ \mathrm{J}$, so

$$
\lambda = \frac{hc}{E} = \frac{1.986\times10^{-25}}{2.275\times10^{-19}}
= 8.73\times10^{-7}\ \mathrm{m} = 873\ \mathrm{nm}.
$$

For silicon, $E = 1.12\ \mathrm{eV} = 1.794\times10^{-19}\ \mathrm{J}$, giving
$\lambda = 1.107\times10^{-6}\ \mathrm{m} = 1107\ \mathrm{nm}$.

**Answer.** GaAs: $873\ \mathrm{nm}$; silicon: $1107\ \mathrm{nm}$, both in the near
infrared.

**Check.** The $1240/E$ shortcut gives $873$ and $1107\ \mathrm{nm}$ directly. Both
wavelengths are outside the visible range, so neither material emits visible light
at its band edge; GaN at $3.40\ \mathrm{eV}$ gives $365\ \mathrm{nm}$, in the
ultraviolet, and blue LEDs use $\ce{InGaN}$ alloys at about $2.7\ \mathrm{eV}$.

**Where marks are lost.** Concluding that silicon could be a near-infrared LED
because $1107\ \mathrm{nm}$ is a convenient wavelength. The gap is indirect, so the
radiative rate is negligible.

### 18. Theoretical capacity of lithium cobalt oxide

**Strategy.** Apply Faraday's law per mole of active material.

**Working.**

$$
Q_\mathrm{sp} = \frac{nF}{3.6M}
= \frac{(1)(96\,485.33212)}{(3.6)(97.87)}
= 273.8\ \mathrm{mAh\ g^{-1}}.
$$

The utilisation is

$$
\frac{145}{273.8} = 0.530.
$$

**Answer.** $Q_\mathrm{sp} = 274\ \mathrm{mAh\ g^{-1}}$; utilisation $= 53.0\ \%$.

**Check.** The theoretical value is never reached because not all lithium can be
removed reversibly: LCO loses structural stability above about half delithiation,
and the practical electrode also contains binder and conductive additive. A
utilisation near $50\ \%$ is therefore the design point, not a failure of the
measurement.

**Where marks are lost.** Using $n = 2$ or the molar mass of the metal only. The
factor $3.6$ converts coulombs per gram to milliampere-hours per gram.

### 19. C-rate, current and time

**Strategy.** Normalise current to nominal capacity.

**Working.** $I = C_\mathrm{rate}Q_\mathrm{nom}$ and $t = Q_\mathrm{nom}/I$.

At C/5: $I = 2.5/5 = 0.50\ \mathrm{A}$, $t = 5.0\ \mathrm{h}$.
At 2C: $I = 2\times2.5 = 5.0\ \mathrm{A}$, $t = 0.50\ \mathrm{h} = 30\ \mathrm{min}$.

**Answer.** $0.50\ \mathrm{A}$ for $5.0\ \mathrm{h}$; $5.0\ \mathrm{A}$ for
$30\ \mathrm{min}$.

**Check.** The product $It$ returns $2.5\ \mathrm{Ah}$ in both cases, as it must by
definition. Real 2C discharge delivers less than the nominal capacity because
polarisation and transport limits intervene.

**Where marks are lost.** Treating C-rate as a current rather than a reciprocal
time, which gives $2.5\ \mathrm{A}$ at "C/5".

### 20. Corrosion rate from current density

**Strategy.** Use the Faraday conversion with the equivalent mass.

**Working.**

$$
\mathrm{CR} = 3.27\times10^{-3}\,\frac{i_\mathrm{corr}M_\mathrm{eq}}{\rho}
= 3.27\times10^{-3}\times\frac{25\times27.92}{7.87}
= 0.290\ \mathrm{mm\ yr^{-1}}.
$$

**Answer.** $\mathrm{CR} = 0.290\ \mathrm{mm\ yr^{-1}}$.

**Check.** A rate near $0.3\ \mathrm{mm\ yr^{-1}}$ is aggressive for quiet aerated
water (chapter worked example: $0.12\ \mathrm{mm\ yr^{-1}}$ at
$10\ \mu\mathrm{A\ cm^{-2}}$) and corresponds to about $1\ \mathrm{mm}$ in three and
a half years.

**Where marks are lost.** Using the atomic mass $55.85$ instead of the equivalent
mass $27.92$. The equivalent mass is $M/n$ for a single oxidation state, and iron
dissolves as $\ce{Fe^{2+}}$ here.

### 21. Pilling–Bedworth ratio for chromia

**Strategy.** Compare the oxide volume with the metal volume consumed.

**Working.** For

$$
\ce{4Cr(s) + 3O2(g) -> 2Cr2O3(s)},
$$

two chromium atoms give one formula unit of oxide, so $n = 2$ and

$$
\mathrm{PBR} = \frac{M_\mathrm{oxide}\,\rho_\mathrm{metal}}{nM_\mathrm{metal}\,\rho_\mathrm{oxide}}
= \frac{(151.99)(7.15)}{(2)(52.00)(5.22)} = 2.00.
$$

**Answer.** $\mathrm{PBR} = 2.00$.

**Check.** A ratio near $2$ is at the upper edge of the protective window: the film
is coherent but under growth stress, and it protects in practice because chromia has
low defect density and slow cation diffusion. The ratio is a guide, not a guarantee;
adhesion and defect structure matter as much as volume.

**Where marks are lost.** Using $n = 4$ from the balanced equation rather than the
number of metal atoms per oxide formula unit. The ratio is per atom of metal.

### 22. Atom economy of the Claus reaction

**Strategy.** Divide the mass of desired product by the total mass of reactants.

**Working.** For

$$
\ce{2H2S(g) + SO2(g) -> 3S(l) + 2H2O(g)},
$$

the reactant mass is $2(34.08) + 64.06 = 132.2\ \mathrm{g}$ and the sulfur mass is
$3(32.06) = 96.18\ \mathrm{g}$. Hence

$$
\mathrm{AE} = \frac{96.18}{132.2}\times100\ \% = 72.8\ \%.
$$

**Answer.** $\mathrm{AE} = 72.8\ \%$; the remaining $27.2\ \%$ is water,
$2\times18.015 = 36.03\ \mathrm{g}$.

**Check.** Mass balances: $96.18 + 36.03 = 132.21\ \mathrm{g}$, equal to the
reactant mass within rounding. Atom economy counts the water as waste even though it
is harmless, which is why atom economy alone is not an environmental verdict.

**Where marks are lost.** Counting sulfur as $\ce{S2}$ or forgetting the
stoichiometric coefficient 3, which changes the numerator by a factor of three.

---

## Part C — Intermediate problems

### 23. Stoichiometric imbalance in a step-growth polyester (multi-step)

**Strategy.** Apply the Carothers equation with imbalance at two extents of
reaction, then interpret the limiting case.

**Working.** For $r = N_A/N_B = 0.98$,

$$
X_n = \frac{1+r}{1+r-2rp}.
$$

At $p = 0.995$:

$$
X_n = \frac{1.98}{1.98 - 2(0.98)(0.995)}
= \frac{1.98}{1.98 - 1.9502} = \frac{1.98}{0.0298} = 66.4.
$$

At $p = 1.000$:

$$
X_n = \frac{1.98}{1.98 - 1.96} = \frac{1.98}{0.020} = 99.0.
$$

**Answer.** $X_n = 66.4$ at $p = 0.995$; $X_n = 99.0$ at complete conversion.

**Check.** The ceiling is $(1+r)/(1-r) = 1.98/0.02 = 99$, which is the value at
$p = 1$; no further conversion can raise it. The same calculation with $r = 0.99$
gives a ceiling of $199$, so a $1\ \%$ excess halves the achievable molar mass.

**Where marks are lost.** Using $X_n = 1/(1-p)$ and ignoring $r$. The imbalance, not
the conversion, is then the controlling variable and the answer is wrong by a factor
of three.

### 24. Gel point with a tetrafunctional monomer (multi-step)

**Strategy.** Insert $r$ and $f$ into the gel-point expression and compare with the
stoichiometric case.

**Working.** For $r \ne 1$,

$$
p_c = \frac{1}{1 + r(f-2)} = \frac{1}{1 + 0.90(4-2)} = \frac{1}{2.80} = 0.357.
$$

For $r = 1$ and $f = 4$,

$$
p_c = \frac{1}{f-1} = \frac{1}{3} = 0.333.
$$

**Answer.** $p_c = 0.357$ at $r = 0.90$, against $0.333$ for the stoichiometric
system: the imbalance delays gelation because some branch sites have no partner.

**Check.** The result is between $1/3$ and $1$; a value below $1/(f-1)$ would be
unphysical for a tetrafunctional network. Gelation at about $36\ \%$ conversion is
why branched step-growth systems must be formulated well below that conversion if a
soluble prepolymer is wanted.

**Where marks are lost.** Using $f = 3$ out of habit from the glycerol case, or
forgetting that $r$ multiplies $(f-2)$ rather than $f$.

### 25. Critical radius from classical nucleation theory (multi-step)

**Strategy.** Evaluate the surface and bulk terms at fixed temperature and
supersaturation, then test the sensitivity to $S$.

**Working.**

$$
r^{*} = \frac{2\gamma V_m}{RT\ln S}.
$$

The denominator at $298.15\ \mathrm{K}$ and $S = 10$ is

$$
RT\ln S = (8.314462618)(298.15)(2.302585)
= 5.707\times10^{3}\ \mathrm{J\ mol^{-1}}.
$$

Hence

$$
r^{*} = \frac{2(0.20)(2.00\times10^{-5})}{5.707\times10^{3}}
= 1.40\times10^{-9}\ \mathrm{m} = 1.40\ \mathrm{nm}.
$$

At $S = 100$, $\ln S = 4.605$ and the denominator is
$1.142\times10^{4}\ \mathrm{J\ mol^{-1}}$, so

$$
r^{*} = \frac{8.00\times10^{-6}}{1.142\times10^{4}} = 7.01\times10^{-10}\ \mathrm{m}
= 0.701\ \mathrm{nm}.
$$

**Answer.** $r^{*} = 1.40\ \mathrm{nm}$ at $S = 10$; $r^{*} = 0.701\ \mathrm{nm}$ at
$S = 100$.

**Check.** Raising the supersaturation tenfold halves the critical radius roughly
(doubling $\ln S$ halves $r^{*}$), so a burst of high supersaturation produces many
small stable nuclei. That is exactly the LaMer requirement: nucleate quickly, then
grow without further nucleation.

**Where marks are lost.** Using $\log_{10}S$ instead of $\ln S$, which changes the
answer by a factor of $2.303$; or inserting $V_m$ in $\mathrm{cm^{3}\ mol^{-1}}$
without converting.

### 26. Quantum-dot emission from the Brus equation (multi-step)

**Strategy.** Compute the confinement and Coulomb terms separately in electronvolts,
then convert the total to a wavelength.

**Working.** The reduced mass is

$$
\mu = \frac{m_e^{*}m_h^{*}}{m_e^{*}+m_h^{*}}m_e
= \frac{(0.13)(0.45)}{0.13+0.45}(9.109\times10^{-31})
= 9.19\times10^{-32}\ \mathrm{kg}.
$$

Confinement:

$$
\frac{h^{2}}{8\mu R^{2}}
= \frac{(6.626\times10^{-34})^{2}}
{8(9.19\times10^{-32})(1.8\times10^{-9})^{2}}
= 1.84\times10^{-19}\ \mathrm{J} = 1.15\ \mathrm{eV}.
$$

Coulomb:

$$
\frac{1.8e^{2}}{4\pi\varepsilon_0\varepsilon R}
= \frac{1.8(1.602\times10^{-19})^{2}}
{4\pi(8.854\times10^{-12})(10.6)(1.8\times10^{-9})}
= 2.18\times10^{-20}\ \mathrm{J} = 0.136\ \mathrm{eV}.
$$

Hence

$$
E = 1.74 + 1.15 - 0.136 = 2.755\ \mathrm{eV},
$$

$$
\lambda = \frac{hc}{E} = \frac{1.986\times10^{-25}}{(2.755)(1.602\times10^{-19})}
= 4.50\times10^{-7}\ \mathrm{m} = 450\ \mathrm{nm}.
$$

**Answer.** $E = 2.76\ \mathrm{eV}$; $\lambda = 450\ \mathrm{nm}$ (blue).

**Check.** The confinement term is about eight times the Coulomb term, so size
dominates the shift; the bulk gap of $1.74\ \mathrm{eV}$ would emit at
$713\ \mathrm{nm}$. A $1.8\ \mathrm{nm}$ CdSe dot emitting near $450\ \mathrm{nm}$ is
consistent with the trend in the chapter, where $2\ \mathrm{nm}$ gives about
$486\ \mathrm{nm}$.

**Where marks are lost.** Adding the Coulomb term instead of subtracting it; it is
attractive, so it lowers the transition energy.

### 27. Fermi level in p-type silicon

**Strategy.** Invert the hole concentration expression.

**Working.** With $p \approx N_A = 2.0\times10^{16}\ \mathrm{cm^{-3}}$,

$$
p = N_v\exp\left(-\frac{E_F - E_v}{k_\mathrm{B}T}\right),
$$

so

$$
E_F - E_v = k_\mathrm{B}T\ln\frac{N_v}{p}
= (0.02585)\ln\frac{1.04\times10^{19}}{2.0\times10^{16}}
= 0.02585(6.254) = 0.162\ \mathrm{eV}.
$$

**Answer.** $E_F - E_v = 0.162\ \mathrm{eV}$ above the valence-band edge.

**Check.** The gap is $1.12\ \mathrm{eV}$, so mid-gap is $0.56\ \mathrm{eV}$; the
Fermi level is far below mid-gap, which is what "p-type" means quantitatively. The
material is non-degenerate: the Fermi level is many $k_\mathrm{B}T$ from the band
edge and well inside the gap, so Boltzmann statistics remain valid.

**Where marks are lost.** Using $N_A$ in $\mathrm{m^{-3}}$ with $N_v$ in
$\mathrm{cm^{-3}}$, or omitting the $k_\mathrm{B}T$ factor and reporting an exponent.

### 28. Built-in potential of a p–n junction

**Strategy.** Use the equilibrium carrier relation with the mass-action law.

**Working.**

$$
V_\mathrm{bi} = \frac{k_\mathrm{B}T}{e}\ln\frac{N_A N_D}{n_i^{2}}
= 0.02585\ln\frac{(1.0\times10^{17})(1.0\times10^{16})}{(1.0\times10^{10})^{2}}
= 0.02585\ln(1.0\times10^{13}).
$$

$$
V_\mathrm{bi} = 0.02585(29.93) = 0.774\ \mathrm{V}.
$$

**Answer.** $V_\mathrm{bi} = 0.774\ \mathrm{V}$.

**Check.** The value lies in the $0.6$–$0.8\ \mathrm{V}$ range quoted for silicon
junctions. The assumption is complete ionisation of both dopants at
$300\ \mathrm{K}$, which is good for boron and phosphorus because their ionisation
energies are about $45\ \mathrm{meV}$, and an abrupt junction with no compensation.
At heavy doping the Fermi–Dirac integral replaces the exponential and the built-in
potential is slightly reduced.

**Where marks are lost.** Using $n_i^2$ as $(1.0\times10^{10})^2$ in
$\mathrm{cm^{-6}}$ but the dopants in $\mathrm{m^{-3}}$; the ratio must be
dimensionless and consistent.

### 29. Specific energy of an electrode pair (multi-step)

**Strategy.** Combine two capacities in series, multiply by voltage, then apply the
active-mass fraction.

**Working.** For two electrodes of specific capacity $Q_c$ and $Q_a$, the
active-material capacity of the pair is the series combination:

$$
Q_\mathrm{pair} = \left(\frac{1}{Q_c} + \frac{1}{Q_a}\right)^{-1}
= \left(\frac{1}{200} + \frac{1}{350}\right)^{-1}
= (0.00500 + 0.002857)^{-1} = 127.3\ \mathrm{mAh\ g^{-1}}.
$$

$$
E_\mathrm{pair} = Q_\mathrm{pair}V = (127.3)(3.7) = 471\ \mathrm{Wh\ kg^{-1}}.
$$

At $32\ \%$ active mass,

$$
E_\mathrm{cell} = 471 \times 0.32 = 151\ \mathrm{Wh\ kg^{-1}}.
$$

**Answer.** $471\ \mathrm{Wh\ kg^{-1}}$ on active materials;
$151\ \mathrm{Wh\ kg^{-1}}$ at cell level.

**Check.** The series combination is dominated by the smaller capacity: $127.3$ is
below $200$, as it must be, because the cathode limits the cell. The second
calculation omits current collectors, separator, electrolyte, tabs and packaging,
which is why the cell value is roughly one third of the active-material value.

**Where marks are lost.** Adding the capacities, which gives
$550\ \mathrm{mAh\ g^{-1}}$ and an impossible energy density; or applying the mass
fraction to the voltage instead of the energy.

### 30. Cell voltage from Gibbs energy and the Nernst slope (multi-step)

**Strategy.** Use $\Delta_\mathrm{r}G^\circ = -nFE^\circ$, then the logarithmic
term of the Nernst equation.

**Working.**

$$
E^\circ = -\frac{\Delta_\mathrm{r}G^\circ}{nF}
= \frac{370\times10^{3}}{(1)(96\,485.33212)} = 3.83\ \mathrm{V}.
$$

For a tenfold change in $Q$,

$$
\Delta E = \frac{RT}{nF}\ln 10
= \frac{(8.314462618)(298.15)}{(1)(96\,485.33212)}(2.302585)
= 0.0592\ \mathrm{V} = 59.2\ \mathrm{mV}.
$$

For $n = 2$ the shift is $29.6\ \mathrm{mV}$ per decade.

**Answer.** $E^\circ = 3.83\ \mathrm{V}$; $59.2\ \mathrm{mV}$ per decade for $n = 1$
and $29.6\ \mathrm{mV}$ for $n = 2$.

**Check.** The $59\ \mathrm{mV}$ decade is the standard result at $298\ \mathrm{K}$;
halving it for two electrons is required because the charge passed per mole of
reaction doubles. This is why intercalation cells with one-electron transitions show
a voltage that slides by tens of millivolts as the lithium activity changes.

**Where marks are lost.** Using a positive sign for $\Delta G = -nFE$; a negative
Gibbs energy must give a positive cell potential.

### 31. Mass of a sacrificial anode (multi-step)

**Strategy.** Convert current and time to charge, then divide by capacity and
utilisation.

**Working.** The charge passed is

$$
Q = It = (0.150\ \mathrm{A})(15\times8760\ \mathrm{h}) = 1.971\times10^{4}\ \mathrm{A\ h}.
$$

The usable anode capacity is $780 \times 0.85 = 663\ \mathrm{A\ h\ kg^{-1}}$, so

$$
m = \frac{1.971\times10^{4}}{663} = 29.7\ \mathrm{kg}.
$$

**Answer.** $m = 29.7\ \mathrm{kg}$ of zinc.

**Check.** The same charge spent on steel would consume about $21\ \mathrm{kg}$ of
iron ($Q = 7.10\times10^{7}\ \mathrm{C}$, hence $3.68\times10^{2}\ \mathrm{mol}$ of
$\ce{Fe^{2+}}$ and $20.5\ \mathrm{kg}$), which shows why the anode is sacrificed
deliberately. The assumptions are
$100\ \%$ current efficiency for zinc dissolution to $\ce{Zn^{2+}}$ (two electrons
per atom),
constant current over the whole life, and all protection current supplied by the
anodes. If the coating degrades, the current demand rises and the anode life falls
in proportion.

**Where marks are lost.** Omitting the $85\ \%$ utilisation, which underestimates
the mass; or using $8760\ \mathrm{h}$ for $15$ years but a current in
milliamperes.

### 32. Corrosion current from polarisation resistance (multi-step)

**Strategy.** Apply the Stern–Geary relation, then the Faraday conversion.

**Working.**

$$
i_\mathrm{corr} = \frac{B}{R_p} = \frac{0.026\ \mathrm{V}}{2.50\times10^{3}\ \Omega\ \mathrm{cm^{2}}}
= 1.04\times10^{-5}\ \mathrm{A\ cm^{-2}} = 10.4\ \mu\mathrm{A\ cm^{-2}}.
$$

$$
\mathrm{CR} = 3.27\times10^{-3}\,\frac{i_\mathrm{corr}M_\mathrm{eq}}{\rho}
= 3.27\times10^{-3}\times\frac{10.4\times27.92}{7.87}
= 0.121\ \mathrm{mm\ yr^{-1}}.
$$

**Answer.** $i_\mathrm{corr} = 10.4\ \mu\mathrm{A\ cm^{-2}}$;
$\mathrm{CR} = 0.121\ \mathrm{mm\ yr^{-1}}$.

**Check.** The rate is close to the chapter worked example at
$10\ \mu\mathrm{A\ cm^{-2}}$, as expected. The measurement window must be small —
about $10$ to $20\ \mathrm{mV}$ either side of $E_\mathrm{corr}$ — because the
Stern–Geary relation is a linearisation of the Tafel kinetics; beyond that, curvature
and mass-transport effects make $R_p$ depend on the perturbation amplitude.

**Where marks are lost.** Mixing $\mathrm{k\Omega}$ and $\Omega$, or quoting
$i_\mathrm{corr}$ in $\mathrm{A\ m^{-2}}$ and inserting it into a formula calibrated
for $\mu\mathrm{A\ cm^{-2}}$.

### 33. Temperature dependence of the contact-process equilibrium (multi-step)

**Strategy.** Use the van't Hoff form of the equilibrium constant with a constant
reaction enthalpy.

**Working.**

$$
\ln\frac{K_2}{K_1} = -\frac{\Delta_\mathrm{r}H^\circ}{R}
\left(\frac{1}{T_2} - \frac{1}{T_1}\right).
$$

$$
\ln\frac{K_2}{9.0\times10^{4}}
= -\frac{-198\times10^{3}}{8.314462618}
\left(\frac{1}{750} - \frac{1}{700}\right)
= (2.381\times10^{4})(-9.524\times10^{-5}) = -2.268.
$$

$$
K_2 = 9.0\times10^{4}\,e^{-2.268} = 9.0\times10^{4}(0.1035)
= 9.3\times10^{3}\ \mathrm{bar^{-1}}.
$$

**Answer.** $K_p(750\ \mathrm{K}) = 9.3\times10^{3}\ \mathrm{bar^{-1}}$, a factor of
about ten below the value at $700\ \mathrm{K}$.

**Check.** The reaction is exothermic, so $K$ must fall as temperature rises. The
converter is therefore designed with interstage cooling and with the last beds at
the lowest temperature that still keeps the catalyst above its ignition temperature;
raising the inlet temperature to increase rate costs conversion.

**Where marks are lost.** Sign error in the van't Hoff equation, which gives
$K$ rising with temperature for an exothermic reaction; or using Celsius temperatures
in the reciprocal.

### 34. Process mass intensity and E-factor with solvent recovery (multi-step)

**Strategy.** Apply the definitions on a gross basis, then redefine the boundary for
the recovered solvent.

**Working.** On a gross-input basis,

$$
\mathrm{PMI} = \frac{m_\mathrm{input}}{m_\mathrm{product}} = \frac{120}{15.0} = 8.00,
$$

and since PMI $= E + 1$,

$$
E = 8.00 - 1 = 7.00\ \mathrm{kg\ kg^{-1}}.
$$

With $72\ \mathrm{kg}$ of solvent returned, the fresh input is
$120 - 72 = 48\ \mathrm{kg}$, so

$$
\mathrm{PMI}_\mathrm{net} = \frac{48}{15.0} = 3.20.
$$

**Answer.** Gross PMI $= 8.00\ \mathrm{kg\ kg^{-1}}$,
$E = 7.00\ \mathrm{kg\ kg^{-1}}$; net PMI with recovery
$= 3.20\ \mathrm{kg\ kg^{-1}}$.

**Check.** The difference between $8.00$ and $3.20$ is entirely a boundary
decision, not a chemical improvement; the same plant produces both numbers. A PMI
quoted without stating whether recycled solvent is credited cannot be compared with
any other figure, which is why green-chemistry claims must name the boundary, the
yield and the basis.

**Where marks are lost.** Reporting PMI as $7.00$ by confusing it with the E-factor;
the two differ by exactly $1$ only when both are mass ratios on the same boundary.

---

## Part D — Advanced problems

### 35. Radical polymerisation rate, chain length and the effect of initiator (multi-step)

**Strategy.** Apply the steady-state rate law, divide by the initiation rate, then
scale with $[I]^{1/2}$.

**Working.** The initiation rate is

$$
R_i = 2fk_dc_\mathrm{I} = 2(0.55)(1.2\times10^{-5})(0.020)
= 2.64\times10^{-7}\ \mathrm{mol\ dm^{-3}\ s^{-1}}.
$$

The steady-state radical concentration follows from
$fk_dc_\mathrm{I}/k_t$:

$$
\frac{fk_dc_\mathrm{I}}{k_t}
= \frac{(0.55)(1.2\times10^{-5})(0.020)}{1.5\times10^{7}}
= 8.80\times10^{-15}\ \mathrm{mol\ dm^{-3}},
$$

$$
\left(\frac{fk_dc_\mathrm{I}}{k_t}\right)^{1/2} = 9.38\times10^{-8}.
$$

$$
R_p = k_pc_\mathrm{M}\left(\frac{fk_dc_\mathrm{I}}{k_t}\right)^{1/2}
= (1.8\times10^{3})(4.0)(9.38\times10^{-8})
= 6.75\times10^{-4}\ \mathrm{mol\ dm^{-3}\ s^{-1}}.
$$

$$
\nu = \frac{R_p}{R_i} = \frac{6.75\times10^{-4}}{2.64\times10^{-7}} = 2.56\times10^{3}.
$$

For combination termination, $X_n = 2\nu = 5.12\times10^{3}$, so

$$
M_n = X_nM_0 = (5.12\times10^{3})(104.15) = 5.33\times10^{5}\ \mathrm{g\ mol^{-1}}.
$$

Doubling $[I]$ at constant temperature multiplies $R_p$ by $\sqrt{2} = 1.41$ and
divides $X_n$ by $\sqrt{2}$:

$$
R_p' = 9.55\times10^{-4}\ \mathrm{mol\ dm^{-3}\ s^{-1}}, \qquad
X_n' = 3.62\times10^{3}, \qquad M_n' = 3.77\times10^{5}\ \mathrm{g\ mol^{-1}}.
$$

**Answer.** $R_p = 6.75\times10^{-4}\ \mathrm{mol\ dm^{-3}\ s^{-1}}$,
$\nu = 2.56\times10^{3}$, $X_n = 5.12\times10^{3}$,
$M_n = 5.33\times10^{5}\ \mathrm{g\ mol^{-1}}$. Doubling the initiator gives
$R_p' = 9.55\times10^{-4}\ \mathrm{mol\ dm^{-3}\ s^{-1}}$ and
$M_n' = 3.77\times10^{5}\ \mathrm{g\ mol^{-1}}$.

**Check.** The rate is typical for bulk styrene at $60\ ^\circ\mathrm{C}$, and a
molar mass near $5\times10^{5}\ \mathrm{g\ mol^{-1}}$ is plausible before transfer
limits it. The $\sqrt{2}$ scaling is the fingerprint of bimolecular termination: a
first-order termination would make $R_p \propto [I]$ and leave $X_n$ unchanged.

**Where marks are lost.** Forgetting the factor $2$ in $R_i$ (it is $2fk_d[I]$), or
doubling $X_n$ when the question asks for the change with doubled initiator.

### 36. Stoichiometric imbalance for a target molar mass (multi-step)

**Strategy.** Convert the target molar mass to $X_n$, then invert the imbalance
equation at $p = 1$.

**Working.**

$$
X_n = \frac{M_n}{M_0} = \frac{32\,000}{226.32} = 141.4.
$$

At complete conversion,

$$
X_n = \frac{1+r}{1-r}
\quad\Longrightarrow\quad
r = \frac{X_n - 1}{X_n + 1} = \frac{140.4}{142.4} = 0.9860.
$$

If $r = n_\mathrm{diacid}/n_\mathrm{diamine}$, the diamine is in excess by

$$
\frac{1}{r} - 1 = \frac{1}{0.9860} - 1 = 0.0142,
$$

that is $1.4\ \%$.

**Answer.** $X_n = 141$; $r = 0.986$; the diamine must be in $1.4\ \%$ excess.

**Check.** A small excess caps the molar mass, so the recipe is a deliberate
compromise between the target and the need to avoid a stoichiometric excess of
either monomer. Note that the excess is relative to the limiting diacid; expressing
it relative to the diamine gives a slightly different percentage, which is why the
basis must be stated.

**Where marks are lost.** Using the Carothers equation without imbalance; it would
predict $p = 0.993$ and miss the point that at $p = 1$ the imbalance alone sets the
molar mass.

### 37. Recycled PET viscosity-average molar mass (multi-step)

**Strategy.** Invert the Mark–Houwink relation at two intrinsic viscosities.

**Working.**

$$
M_v = \left(\frac{[\eta]}{K}\right)^{1/a}.
$$

For virgin PET, $[\eta] = 0.78\ \mathrm{dL\ g^{-1}}$:

$$
M_v = \left(\frac{0.78}{2.1\times10^{-4}}\right)^{1/0.82}
= (3.71\times10^{3})^{1.220} = 2.26\times10^{4}\ \mathrm{g\ mol^{-1}}.
$$

For recycled PET, $[\eta] = 0.62$:

$$
M_v = \left(\frac{0.62}{2.1\times10^{-4}}\right)^{1.220}
= (2.95\times10^{3})^{1.220} = 1.71\times10^{4}\ \mathrm{g\ mol^{-1}}.
$$

The loss is

$$
\frac{2.26 - 1.71}{2.26}\times100\ \% = 24.5\ \%.
$$

**Answer.** $M_v = 2.26\times10^{4}$ for virgin and
$1.71\times10^{4}\ \mathrm{g\ mol^{-1}}$ for recycled PET, a loss of $24.5\ \%$.

**Check.** A $24\ \%$ drop in $M_v$ is consistent with chain scission during melt
reprocessing: each melt pass shortens the chains, and the Mark–Houwink exponent below
$1$ means a modest viscosity change corresponds to a larger molar-mass change. The
consequence for bottle-to-bottle recycling is that the regranulate must be
chain-extended or solid-state polycondensed to restore intrinsic viscosity, or
blended with virgin resin; otherwise the parison cannot be blow-moulded with adequate
melt strength.

**Where marks are lost.** Using $a$ as a multiplier rather than an exponent, or
quoting a percentage loss calculated from intrinsic viscosities rather than molar
masses.

### 38. BET diameter, crystallite size and aggregation number (multi-step)

**Strategy.** Convert surface area to an equivalent spherical diameter, compare with
the Scherrer size, then convert the volume ratio to a count.

**Working.** With
$S = 45\ \mathrm{m^{2}\ g^{-1}} = 4.5\times10^{4}\ \mathrm{m^{2}\ kg^{-1}}$ and
$\rho = 3.89\times10^{3}\ \mathrm{kg\ m^{-3}}$,

$$
D_\mathrm{eq} = \frac{6}{\rho S}
= \frac{6}{(3.89\times10^{3})(4.5\times10^{4})}
= 3.43\times10^{-8}\ \mathrm{m} = 34.3\ \mathrm{nm}.
$$

The Scherrer size from item 15 is $17.1\ \mathrm{nm}$, so

$$
\frac{D_\mathrm{eq}}{D_\mathrm{XRD}} = \frac{34.3}{17.1} = 2.01.
$$

For equal cubes, the number per particle is the volume ratio:

$$
N = \left(\frac{34.3}{17.1}\right)^{3} = 8.1.
$$

**Answer.** $D_\mathrm{eq} = 34.3\ \mathrm{nm}$; ratio $2.01$; about eight
crystallites per particle.

**Check.** Eight crystallites of $17\ \mathrm{nm}$ make a $34\ \mathrm{nm}$ particle
if they pack without porosity, so the powder is a mesostructured aggregate rather
than a collection of single crystals. The assumptions are that the particles are
smooth, non-porous spheres, that all the BET area is external, and that the
crystallites are equal cubes with no strain broadening. Internal porosity would make
the true particle smaller than $34\ \mathrm{nm}$, and strain would make the
crystallite size appear smaller, so the two errors partially cancel.

**Where marks are lost.** Comparing diameters rather than volumes when calculating
the number of crystallites, which gives $2$ instead of $8$.

### 39. Doping, conductivity and resistivity (multi-step)

**Strategy.** Compute the acceptor concentration from the site fraction, then apply
the conductivity sum.

**Working.** The acceptor concentration is

$$
N_A = \frac{5.00\times10^{22}}{5.0\times10^{5}} = 1.00\times10^{17}\ \mathrm{cm^{-3}}.
$$

With complete ionisation, $p = N_A$, so

$$
\sigma = e(n\mu_n + p\mu_p) \approx ep\mu_p
= (1.602\times10^{-19})(1.00\times10^{17})(450)
= 7.21\ \mathrm{S\ cm^{-1}}.
$$

$$
\rho = \frac{1}{\sigma} = 0.139\ \Omega\ \mathrm{cm}.
$$

**Answer.** $N_A = 1.0\times10^{17}\ \mathrm{cm^{-3}}$;
$\sigma = 7.21\ \mathrm{S\ cm^{-1}}$; $\rho = 0.139\ \Omega\ \mathrm{cm}$.

**Check.** The electron term is negligible because $n = n_i^{2}/N_A =
(1.0\times10^{10})^{2}/1.0\times10^{17} = 1.0\times10^{3}\ \mathrm{cm^{-3}}$, seven
orders of magnitude below $p$, and $\mu_n$ is only about three times $\mu_p$. A
resistivity of $0.14\ \Omega\ \mathrm{cm}$ is a typical heavily doped p-type
contact layer.

**Where marks are lost.** Using the atomic density as the carrier density, which
gives a resistivity four orders of magnitude too low.

### 40. Carrier density from the Hall effect (multi-step)

**Strategy.** Rearrange $V_\mathrm{H} = IB/(net)$ for the carrier density.

**Working.**

$$
n = \frac{IB}{etV_\mathrm{H}}
= \frac{(2.0\times10^{-3})(0.80)}
{(1.602\times10^{-19})(0.30\times10^{-3})(3.5\times10^{-3})}
= 9.51\times10^{21}\ \mathrm{m^{-3}}.
$$

In reciprocal cubic centimetres,

$$
n = 9.51\times10^{21}\times10^{-6} = 9.51\times10^{15}\ \mathrm{cm^{-3}}.
$$

**Answer.** $n = 9.5\times10^{21}\ \mathrm{m^{-3}}$
$= 9.5\times10^{15}\ \mathrm{cm^{-3}}$.

**Check.** The density is typical of a lightly doped epitaxial layer. For the stated
geometry a positive Hall voltage indicates holes; a negative voltage indicates
electrons, which is why the sign of $V_\mathrm{H}$ identifies the carrier type.
Mobility requires the sheet resistance as well, which is why Hall measurements
normally report resistivity, mobility and carrier density together.

**Where marks are lost.** Leaving the thickness in millimetres, which gives a
density wrong by $10^{3}$; or using volts and millivolts inconsistently.

### 41. Sizing a 75 kWh pack (multi-step)

**Strategy.** Fix the series count from the voltage, then the parallel count from
the charge, and round each to an integer.

**Working.** Series count:

$$
N_s = \frac{400\ \mathrm{V}}{3.7\ \mathrm{V}} = 108.1 \rightarrow 108,
\qquad V_\mathrm{pack} = 108(3.7) = 399.6\ \mathrm{V}.
$$

Required capacity:

$$
Q_\mathrm{req} = \frac{75\,000\ \mathrm{Wh}}{400\ \mathrm{V}} = 187.5\ \mathrm{Ah}.
$$

Parallel strings:

$$
N_p = \frac{187.5}{5.0} = 37.5 \rightarrow 38,
\qquad Q_\mathrm{pack} = 38(5.0) = 190\ \mathrm{Ah}.
$$

$$
E_\mathrm{pack} = (399.6)(190) = 7.59\times10^{4}\ \mathrm{Wh} = 75.9\ \mathrm{kWh}.
$$

The cell count is $108\times38 = 4104$.

**Answer.** $108$ series and $38$ parallel; $399.6\ \mathrm{V}$,
$190\ \mathrm{Ah}$, $75.9\ \mathrm{kWh}$; $4104$ cells.

**Check.** The result exceeds the specification by $1.2\ \%$, which is an acceptable
design margin. The parallel count is rounded up because a fractional string cannot be
built and rounding down would fail the energy target; the overshoot is cheaper than
a redesign.

**Where marks are lost.** Rounding the series count to the nearest integer rather
than to a value that meets or exceeds the voltage, or multiplying the two counts
before rounding.

### 42. Pipeline life and the effect of cathodic protection (multi-step)

**Strategy.** Divide the available wall loss by the corrosion rate, then invert the
Faraday conversion.

**Working.** The allowable loss is $8.0 - 3.0 = 5.0\ \mathrm{mm}$, so

$$
t = \frac{5.0\ \mathrm{mm}}{0.18\ \mathrm{mm\ yr^{-1}}} = 27.8\ \mathrm{yr}.
$$

Rearranging the corrosion-rate formula,

$$
i_\mathrm{corr} = \frac{\mathrm{CR}\,\rho}{3.27\times10^{-3}M_\mathrm{eq}}
= \frac{(0.18)(7.87)}{(3.27\times10^{-3})(27.92)}
= 15.5\ \mu\mathrm{A\ cm^{-2}}.
$$

With cathodic protection reducing $i_\mathrm{corr}$ by a factor of $20$, the rate
falls to $0.0090\ \mathrm{mm\ yr^{-1}}$ and the uniform life becomes

$$
t' = \frac{5.0}{0.0090} = 5.6\times10^{2}\ \mathrm{yr}.
$$

**Answer.** $27.8\ \mathrm{yr}$ unprotected;
$i_\mathrm{corr} = 15.5\ \mu\mathrm{A\ cm^{-2}}$;
$5.6\times10^{2}\ \mathrm{yr}$ with protection at one-twentieth of the current.

**Check.** The protected life is not a prediction. It assumes uniform attack, a
single oxidation state, $100\ \%$ current efficiency and protection over the whole
surface; in practice pitting, stress-corrosion cracking, coating disbondment and
interference currents can fail a pipeline long before the average wall loss is
significant, and the cathodic-protection criterion is a potential, not a rate.

**Where marks are lost.** Applying the factor of $20$ to the life rather than to the
rate, which gives $560\ \mathrm{yr}$ by a different and incorrect route; or using
$8.0\ \mathrm{mm}$ rather than the allowance.

### 43. Haber–Bosch equilibrium conversion (multi-step)

**Strategy.** Write the mole fractions in terms of one extent, substitute into
$K_p$, and solve the resulting polynomial.

**Working.** Let $\alpha$ be the conversion of nitrogen with a $1:3$ feed. The total
moles are $4 - 2\alpha$, so

$$
y_\mathrm{N2} = \frac{1-\alpha}{4-2\alpha}, \qquad
y_\mathrm{H2} = \frac{3(1-\alpha)}{4-2\alpha}, \qquad
y_\mathrm{NH3} = \frac{2\alpha}{4-2\alpha}.
$$

For

$$
\ce{N2(g) + 3H2(g) <=> 2NH3(g)},
$$

$$
K_p = \frac{p_\mathrm{NH3}^{2}}{p_\mathrm{N2}p_\mathrm{H2}^{3}}
= \frac{y_\mathrm{NH3}^{2}}{y_\mathrm{N2}y_\mathrm{H2}^{3}P^{2}}.
$$

Substituting gives

$$
K_pP^{2} = \frac{4\alpha^{2}(4-2\alpha)^{2}}{27(1-\alpha)^{4}}.
$$

At $P = 200\ \mathrm{bar}$, $K_pP^{2} = (1.0\times10^{-4})(4.0\times10^{4}) = 4.0$,
so

$$
4\alpha^{2}(4-2\alpha)^{2} = 108(1-\alpha)^{4}.
$$

Taking the positive square root,

$$
2\alpha(4-2\alpha) = 10.39(1-\alpha)^{2},
$$

which rearranges to

$$
14.39\alpha^{2} - 28.78\alpha + 10.39 = 0,
$$

giving $\alpha = 0.473$ (the other root, $1.53$, is unphysical).

The mole fractions are

$$
y_\mathrm{N2} = 0.173, \qquad y_\mathrm{H2} = 0.518, \qquad y_\mathrm{NH3} = 0.310.
$$

At $300\ \mathrm{bar}$, $K_pP^{2} = 9.0$ and the same procedure gives
$\alpha = 0.548$.

**Answer.** At $200\ \mathrm{bar}$: $\alpha = 0.473$; $y_\mathrm{N2} = 0.173$,
$y_\mathrm{H2} = 0.518$, $y_\mathrm{NH3} = 0.310$. At $300\ \mathrm{bar}$:
$\alpha = 0.548$.

**Check.** The mole fractions sum to $1.000$, and back-substitution returns
$K_p = 1.0\times10^{-4}\ \mathrm{bar^{-2}}$. A per-pass conversion of about
$47\ \%$ is consistent with industrial operation at $400$–$500\ ^\circ\mathrm{C}$ and
$150$–$300\ \mathrm{bar}$; raising the pressure from $200$ to $300\ \mathrm{bar}$
gains about eight percentage points but costs compression energy.

**Where marks are lost.** Using partial pressures directly without converting to
mole fractions, or forgetting that $K_p$ has units of $\mathrm{bar^{-2}}$ and
therefore that $P^{2}$ must appear. The ideal-gas assumption overstates the
conversion: at $200$–$300\ \mathrm{bar}$ fugacity coefficients differ from unity by
tens of per cent, and a real design predicts several percentage points less.

### 44. Turnover frequency on a supported platinum catalyst (multi-step)

**Strategy.** Convert the catalyst loading to moles of platinum, apply the
dispersion, then divide the reaction rate by the number of surface sites.

**Working.** The mass of platinum is $3.0 \times 0.020 = 0.060\ \mathrm{g}$, so

$$
n_\mathrm{Pt} = \frac{0.060}{195.08} = 3.08\times10^{-4}\ \mathrm{mol}.
$$

The surface fraction is $0.25$, so

$$
n_\mathrm{surf} = 0.25(3.08\times10^{-4}) = 7.69\times10^{-5}\ \mathrm{mol},
$$

$$
N_\mathrm{sites} = (7.69\times10^{-5})(6.022\times10^{23}) = 4.63\times10^{19}.
$$

The reaction rate in molecules per second is

$$
(1.2\times10^{-4})(6.022\times10^{23}) = 7.23\times10^{19}\ \mathrm{s^{-1}},
$$

so

$$
\mathrm{TOF} = \frac{7.23\times10^{19}}{4.63\times10^{19}} = 1.56\ \mathrm{s^{-1}}.
$$

**Answer.** $N_\mathrm{sites} = 4.6\times10^{19}$;
$\mathrm{TOF} = 1.6\ \mathrm{s^{-1}}$.

**Check.** A turnover frequency of order $1\ \mathrm{s^{-1}}$ is typical of an
oxide-supported metal catalyst near $500\ \mathrm{K}$, where each surface atom
converts a molecule every second. The calculation assumes that all surface platinum
atoms are active, that the dispersion is measured correctly, and that the rate is
differential — no heat or mass transfer limitation. A pellet-scale reactor with a
strong exotherm would show an apparent TOF lower than the intrinsic value.

**Where marks are lost.** Forgetting the $2.0\ \mathrm{wt\%}$ loading and using the
whole catalyst mass as platinum, which inflates the site count by a factor of $50$.

---

## Part E — Calculation problems

### 45. Full molar-mass distribution of polyethylene (multi-step)

**Strategy.** Build a table of masses and moles, then compute both averages from the
definitions; convert $M_n$ to a degree of polymerisation at the end.

**Working.** Taking $100\ \mathrm{g}$ of sample:

| $M_i$ / $\mathrm{g\ mol^{-1}}$ | $m_i$ / $\mathrm{g}$ | $n_i$ / $\mathrm{mmol}$ | mass fraction |
|---:|---:|---:|---:|
| $15\,000$ | $4$ | $0.2667$ | $0.04$ |
| $30\,000$ | $8$ | $0.2667$ | $0.08$ |
| $50\,000$ | $18$ | $0.3600$ | $0.18$ |
| $80\,000$ | $35$ | $0.4375$ | $0.35$ |
| $120\,000$ | $25$ | $0.2083$ | $0.25$ |
| $250\,000$ | $10$ | $0.0400$ | $0.10$ |
| **Total** | **$100$** | **$1.5792$** | **$1.00$** |

$$
M_n = \frac{100}{1.5792\times10^{-3}} = 6.33\times10^{4}\ \mathrm{g\ mol^{-1}}.
$$

$$
M_w = \sum_i w_iM_i = 0.04(15\,000) + 0.08(30\,000) + 0.18(50\,000)
+ 0.35(80\,000) + 0.25(120\,000) + 0.10(250\,000)
$$
$$
= 600 + 2400 + 9000 + 28\,000 + 30\,000 + 25\,000
= 9.50\times10^{4}\ \mathrm{g\ mol^{-1}}.
$$

$$
\mathrm{PDI} = \frac{95\,000}{63\,325} = 1.50, \qquad
X_n = \frac{63\,325}{28.05} = 2.26\times10^{3}.
$$

**Answer.** $M_n = 6.33\times10^{4}\ \mathrm{g\ mol^{-1}}$,
$M_w = 9.50\times10^{4}\ \mathrm{g\ mol^{-1}}$, PDI $= 1.50$,
$X_n = 2.26\times10^{3}$.

**Check.** A PDI of exactly $1.50$ is the signature of radical polymerisation with
termination by combination, so the distribution is not consistent with living
anionic polymerisation, which would give PDI $\approx 1 + 1/X_n \approx 1.0004$.
The mass average is $50\ \%$ above the number average because the $250\,000$ fraction
carries $10\ \%$ of the mass but only $2.5\ \%$ of the molecules.

**Where marks are lost.** Averaging the six molar masses arithmetically
($90\,833\ \mathrm{g\ mol^{-1}}$), which is neither $M_n$ nor $M_w$; or dividing the
total mass by the total moles expressed in grams rather than moles.

### 46. Crystallinity by density and by DSC (multi-step)

**Strategy.** Apply the two-phase density relation and the enthalpy ratio, then
compare.

**Working.** Density method:

$$
\chi_c = \frac{1/\rho - 1/\rho_a}{1/\rho_c - 1/\rho_a}
= \frac{1/0.930 - 1/0.855}{1/1.004 - 1/0.855}
= \frac{1.0753 - 1.1696}{0.9960 - 1.1696}
= \frac{-0.0943}{-0.1736} = 0.543.
$$

DSC method: the specific enthalpy is

$$
\Delta H_f = \frac{0.170\ \mathrm{J}}{4.80\times10^{-3}\ \mathrm{g}}
= 35.4\ \mathrm{J\ g^{-1}},
$$

$$
\chi_c = \frac{\Delta H_f}{\Delta H_f^\circ} = \frac{35.4}{293} = 0.121.
$$

The ratio is $0.543/0.121 = 4.50$.

**Answer.** $\chi_c = 0.543$ by density and $0.121$ by DSC; the ratio is $4.5$.

**Check.** Both numbers are internally consistent; they describe different samples
or different thermal histories. The density value is a bulk average that includes
slowly cooled, well-annealed material with thick lamellae; the DSC value comes from
$4.80\ \mathrm{mg}$ and, if that subsample was cooled faster, reflects small,
imperfect crystallites and a lower heat of fusion. Reporting crystallinity without
the method
and the cooling programme is meaningless, and the discrepancy is evidence of
heterogeneity, not an arithmetic error.

**Where marks are lost.** Using $\rho_c/\rho$ as the crystallinity, or forgetting to
convert milligrams to grams before dividing the endotherm.

### 47. Size dependence of CdSe emission (multi-step)

**Strategy.** Evaluate the three Brus terms at two radii and convert each total to a
wavelength.

**Working.** With $\mu = 9.19\times10^{-32}\ \mathrm{kg}$ and $\varepsilon = 10.6$,
the terms are $h^{2}/(8\mu R^{2})$ and $1.8e^{2}/(4\pi\varepsilon_0\varepsilon R)$.
At $R = 1.5\ \mathrm{nm}$:

$$
E_\mathrm{conf} = \frac{(6.626\times10^{-34})^{2}}{8(9.19\times10^{-32})(1.5\times10^{-9})^{2}}
= 2.66\times10^{-19}\ \mathrm{J} = 1.66\ \mathrm{eV},
$$

$$
E_\mathrm{Coulomb} = \frac{1.8(1.602\times10^{-19})^{2}}
{4\pi(8.854\times10^{-12})(10.6)(1.5\times10^{-9})}
= 2.61\times10^{-20}\ \mathrm{J} = 0.163\ \mathrm{eV}.
$$

At $R = 3.0\ \mathrm{nm}$ both terms fall by factors of $4$ and $2$ respectively:

$$
E_\mathrm{conf} = 0.414\ \mathrm{eV}, \qquad E_\mathrm{Coulomb} = 0.0815\ \mathrm{eV}.
$$

The table lists both as magnitudes; the total is
$E = E_g + E_\mathrm{conf} - E_\mathrm{Coulomb}$.

| $R$ / nm | $E_\mathrm{conf}$ / eV | $E_\mathrm{Coulomb}$ / eV | $E$ / eV | $\lambda$ / nm |
|---:|---:|---:|---:|---:|
| $1.5$ | $1.657$ | $0.163$ | $3.234$ | $383$ |
| $3.0$ | $0.414$ | $0.082$ | $2.073$ | $598$ |

**Answer.** $R = 1.5\ \mathrm{nm}$: $E = 3.23\ \mathrm{eV}$,
$\lambda = 383\ \mathrm{nm}$ (ultraviolet edge). $R = 3.0\ \mathrm{nm}$:
$E = 2.07\ \mathrm{eV}$, $\lambda = 598\ \mathrm{nm}$ (orange).

**Check.** The bulk gap of $1.74\ \mathrm{eV}$ corresponds to $713\ \mathrm{nm}$, so
both dots are blue-shifted, and the smaller dot is shifted further. The confinement
term changes by a factor of four between the two radii while the Coulomb term changes
by a factor of two, so confinement dominates the size dependence — which is why the
emission colour can be tuned by growth time.

**Where marks are lost.** Dividing the confinement term by $R$ instead of $R^{2}$,
which reverses the relative sensitivity; or reporting the Coulomb term with a
positive sign.

The Brus model assumes spherical dots, infinite potential barriers and bulk
effective masses. At $1.5\ \mathrm{nm}$ the dot is only about five lattice constants
across, so the effective-mass approximation is at its limit and the $383\ \mathrm{nm}$
value is an estimate rather than a prediction; tight-binding or atomistic methods are
needed there.

### 48. Photon flux and current in a blue LED (multi-step)

**Strategy.** Convert optical power to photon rate, then photon rate to current.

**Working.**

$$
E_\mathrm{ph} = \frac{hc}{\lambda}
= \frac{(6.626\times10^{-34})(2.998\times10^{8})}{450\times10^{-9}}
= 4.41\times10^{-19}\ \mathrm{J} = 2.76\ \mathrm{eV}.
$$

$$
\dot N = \frac{P}{E_\mathrm{ph}} = \frac{1.0\times10^{-3}}{4.41\times10^{-19}}
= 2.27\times10^{15}\ \mathrm{s^{-1}}.
$$

One electron per photon corresponds to a current

$$
I = \dot Ne = (2.27\times10^{15})(1.602\times10^{-19}) = 3.63\times10^{-4}\ \mathrm{A}
= 0.363\ \mathrm{mA}.
$$

**Answer.** $E_\mathrm{ph} = 4.41\times10^{-19}\ \mathrm{J} = 2.76\ \mathrm{eV}$;
$\dot N = 2.3\times10^{15}\ \mathrm{s^{-1}}$; $I = 0.36\ \mathrm{mA}$ at one electron
per emitted photon.

**Check.** The current is small because $1\ \mathrm{mW}$ of blue light is only about
$2\times10^{15}$ photons per second. A real device draws more: internal quantum
efficiency below unity and light extraction below unity mean that several electrons
are injected per photon leaving the package, and the forward voltage of about
$3\ \mathrm{V}$ sets the electrical power. The calculation therefore gives a lower
bound on current, not a design value.

**Where marks are lost.** Using the photon energy in electronvolts with a power in
watts, or forgetting the elementary charge when converting photons per second to
amperes.

### 49. Lithium–sulfur capacity and energy (multi-step)

**Strategy.** Apply Faraday's law per gram of sulfur and per gram of product, then
multiply by voltage and by the active-mass fraction.

**Working.** For

$$
\ce{2Li(s) + S(s) -> Li2S(s)},
$$

two electrons are transferred per sulfur atom, so per gram of sulfur

$$
Q_\mathrm{S} = \frac{nF}{3.6M_\mathrm{S}}
= \frac{2(96\,485.33212)}{3.6(32.06)} = 1.672\times10^{3}\ \mathrm{mAh\ g^{-1}}.
$$

Per gram of $\ce{Li2S}$ ($M = 45.95\ \mathrm{g\ mol^{-1}}$):

$$
Q_\mathrm{Li2S} = \frac{2(96\,485.33212)}{3.6(45.95)}
= 1.167\times10^{3}\ \mathrm{mAh\ g^{-1}}.
$$

The specific energy per gram of sulfur is

$$
E_\mathrm{S} = (1672)(2.1) = 3.51\times10^{3}\ \mathrm{Wh\ kg^{-1}},
$$

and at $30\ \%$ active mass,

$$
E_\mathrm{cell} = 3.51\times10^{3}\times0.30 = 1.05\times10^{3}\
\mathrm{Wh\ kg^{-1}}.
$$

**Answer.** $1672\ \mathrm{mAh\ g^{-1}}$ of sulfur;
$1167\ \mathrm{mAh\ g^{-1}}$ of $\ce{Li2S}$;
$3.51\times10^{3}\ \mathrm{Wh\ kg^{-1}}$ of sulfur;
$1.05\times10^{3}\ \mathrm{Wh\ kg^{-1}}$ at cell level.

**Check.** The capacity per gram falls when referred to the discharged product,
because the lithium mass is now included; that is why sulfur cathodes are quoted per
gram of sulfur. The cell-level figure is an upper bound: it assumes complete
two-electron conversion, no polysulfide shuttle, no excess electrolyte, no lithium
anode mass and no packaging. Practical cells are far below this because the anode and
electrolyte dominate the mass.

**Where marks are lost.** Using $n = 1$ for sulfur, which halves the capacity; or
dividing by the molar mass of $\ce{Li2S}$ while calling the result capacity per gram
of sulfur.

### 50. Sizing a 60 kWh pack and estimating specific energy (multi-step)

**Strategy.** Series count from voltage, parallel count from charge, then divide pack
energy by pack mass.

**Working.** Series:

$$
N_s = \frac{400}{3.7} = 108.1 \rightarrow 108, \qquad V = 108(3.7) = 399.6\ \mathrm{V}.
$$

Capacity required:

$$
Q_\mathrm{req} = \frac{60\,000}{400} = 150\ \mathrm{Ah}, \qquad
N_p = \frac{150}{4.8} = 31.25 \rightarrow 32.
$$

$$
Q_\mathrm{pack} = 32(4.8) = 153.6\ \mathrm{Ah}, \qquad
E_\mathrm{pack} = (399.6)(153.6) = 6.14\times10^{4}\ \mathrm{Wh} = 61.4\ \mathrm{kWh}.
$$

The cell count is $108\times32 = 3456$, and

$$
E_\mathrm{sp} = \frac{61.4\ \mathrm{kWh}}{420\ \mathrm{kg}} = 0.146\ \mathrm{kWh\ kg^{-1}}
= 146\ \mathrm{Wh\ kg^{-1}}.
$$

**Answer.** $108$ series, $32$ parallel; $399.6\ \mathrm{V}$, $153.6\ \mathrm{Ah}$,
$61.4\ \mathrm{kWh}$; $3456$ cells; $146\ \mathrm{Wh\ kg^{-1}}$ at pack level.

**Check.** Using the nominal $60\ \mathrm{kWh}$ target instead of the built
$61.4\ \mathrm{kWh}$ gives $143\ \mathrm{Wh\ kg^{-1}}$, so the rounding choice is
worth a few per cent. A pack-level value near $150\ \mathrm{Wh\ kg^{-1}}$ is
consistent with lithium-ion cells of this capacity class once cooling, structure and
management electronics are included.

**Where marks are lost.** Dividing the target energy by the cell voltage rather than
the pack voltage when calculating capacity, which inflates the parallel count by the
series factor.

### 51. Corrosion allowance and anode mass for a protected tank (multi-step)

**Strategy.** Treat the allowance as a thickness budget, then convert protection
current and time to charge and mass.

**Working.** The allowable loss is $10.0 - 4.0 = 6.0\ \mathrm{mm}$, so

$$
t = \frac{6.0\ \mathrm{mm}}{0.12\ \mathrm{mm\ yr^{-1}}} = 50.0\ \mathrm{yr}.
$$

The charge for $20$ years at $0.20\ \mathrm{A}$ is

$$
Q = (0.20)(20)(8760) = 3.504\times10^{4}\ \mathrm{A\ h}.
$$

With $780\ \mathrm{A\ h\ kg^{-1}}$ and $85\ \%$ utilisation,

$$
m = \frac{3.504\times10^{4}}{780\times0.85} = \frac{3.504\times10^{4}}{663}
= 52.9\ \mathrm{kg}.
$$

**Answer.** Allowance life $= 50.0\ \mathrm{yr}$; anode mass $= 52.9\ \mathrm{kg}$.

**Check.** The anode mass is set by the total charge, which is the product of the
protection current and the time; it does not follow from the steel area alone. The
current itself depends on the coated area, the coating quality, the soil resistivity
and the accepted current density, so a larger tank with a good coating may need less
current than a smaller uncoated one. The calculation also assumes that the anodes
remain active and that the current distribution does not leave shielded areas
unprotected.

**Where marks are lost.** Using the corrosion allowance time as the protection
period, or applying the utilisation factor to the current instead of the mass.

### 52. Steam reforming: hydrogen yield, duty and efficiency (multi-step)

**Strategy.** Use the stoichiometry of reforming plus shift, convert to mass, then
compare the hydrogen energy with the feed energy plus the reaction duty.

**Working.** Reforming,

$$
\ce{CH4(g) + H2O(g) -> CO(g) + 3H2(g)},
$$

gives $3\ \mathrm{kmol}$ of $\ce{H2}$; the shift,

$$
\ce{CO(g) + H2O(g) -> CO2(g) + H2(g)},
$$

adds $1\ \mathrm{kmol}$, so $4.00\ \mathrm{kmol}$ of $\ce{H2}$ is produced:

$$
m_\mathrm{H2} = 4.00(2.016) = 8.064\ \mathrm{kg}.
$$

Per kilogram of methane:

$$
\frac{8.064}{16.04} = 0.5027\ \mathrm{kg\ H2\ kg^{-1}\ CH4}.
$$

The duty per kilogram of methane is

$$
\frac{206\ \mathrm{kJ\ mol^{-1}}}{16.04\times10^{-3}\ \mathrm{kg\ mol^{-1}}}
= 1.284\times10^{4}\ \mathrm{kJ\ kg^{-1}} = 12.84\ \mathrm{MJ\ kg^{-1}}.
$$

The hydrogen energy is $0.5027(120) = 60.33\ \mathrm{MJ\ kg^{-1}}$ of methane, so

$$
\eta = \frac{60.33}{60.33 + 12.84} = 0.825.
$$

The stoichiometric carbon dioxide is one mole per mole of methane:

$$
\frac{44.01}{16.04} = 2.74\ \mathrm{kg\ CO2\ kg^{-1}\ CH4},
\qquad
\frac{2.74}{0.5027} = 5.46\ \mathrm{kg\ CO2\ kg^{-1}\ H2}.
$$

**Answer.** $4.00\ \mathrm{kmol}$ and $8.06\ \mathrm{kg}$ of $\ce{H2}$;
$0.503\ \mathrm{kg}$ of $\ce{H2}$ per kg of methane; duty
$12.8\ \mathrm{MJ\ kg^{-1}}$; efficiency $82.5\ \%$; $2.74\ \mathrm{kg}$ of
$\ce{CO2}$ per kg of methane, or $5.46\ \mathrm{kg}$ of $\ce{CO2}$ per kg of
hydrogen.

**Check.** The efficiency is an idealised upper bound: it counts only the reaction
duty and the hydrogen lower heating value, and ignores flue-gas losses, compression,
purification and steam export. Industrial plants reach $70$–$80\ \%$ on the same
basis. The $5.46\ \mathrm{kg}$ of $\ce{CO2}$ per kg of $\ce{H2}$ is the stoichiometric
minimum; a real plant emits more because natural gas is burned to supply the duty,
which is why the chapter quotes $9$–$10\ \mathrm{kg}$ of $\ce{CO2}$ per kg of
$\ce{H2}$ for unabated steam reforming. The two numbers differ by the fuel boundary,
not by the chemistry.

**Where marks are lost.** Counting only the three moles from reforming and missing
the shift, which gives $6.05\ \mathrm{kg}$ instead of $8.06\ \mathrm{kg}$; or
computing efficiency as hydrogen energy divided by duty only, which exceeds $100\ \%$.

---

## Part F — Multiple-choice self-check

### 53. PDI of a living anionic polymerisation

**Strategy.** Recall the dispersity of a Poisson distribution, then test each option
against it.

**Answer.** **A ($1.02$).**

**Working.** Ideal living anionic polymerisation has no termination and rapid
initiation, so the distribution is Poisson-like and
$\mathrm{PDI} \to 1 + 1/X_n$. At $X_n = 100$ that is $1.01$, and $1.02$ is the only
option close to it.

**Best distractor.** C ($2.00$) is the Flory limit for step-growth polymerisation,
and it is the value that students who remember "PDI equals two for step-growth"
select. It is a correct value for a different mechanism, not a narrow distribution.

**Check.** $1 + 1/100 = 1.01$, so $1.02$ is the only option of the right order; it
allows for a small amount of chain transfer, which is unavoidable in practice.

**Where marks are lost.** Choosing $1.50$, which is the combination-termination value
for radical polymerisation; it is a signature of a different process.

### 54. Which method gives a crystallite size?

**Strategy.** Ask what each technique weights and what physical dimension it reports.

**Answer.** **B (powder XRD with the Scherrer equation).**

**Working.** The Scherrer equation converts peak broadening into the size of
coherently diffracting domains, weighted by volume. It says nothing about the
external particle outline.

**Best distractor.** A (dynamic light scattering) gives a hydrodynamic diameter from
the diffusion coefficient; it is intensity-weighted and includes the ligand shell and
any aggregates, so it measures something larger and different in kind.

**Check.** A Scherrer size equal to the TEM size indicates single-crystal particles;
a Scherrer size much smaller than the TEM size indicates polycrystalline particles
or strain broadening.

**Where marks are lost.** Choosing C (BET), which gives a surface-area-equivalent
diameter, not a crystallite size.

### 55. Which semiconductor is direct-gap?

**Strategy.** Decide whether the conduction-band minimum and the valence-band maximum
share a crystal momentum, then check each material.

**Answer.** **C ($\ce{GaAs}$).**

**Working.** GaAs has its conduction-band minimum and valence-band maximum at the
same crystal momentum, so radiative transitions need no phonon. It is the standard
III–V emitter material.

**Best distractor.** A ($\ce{Si}$) has the more familiar band gap of
$1.12\ \mathrm{eV}$ and is the archetypal semiconductor, but it is indirect and
therefore a very poor emitter.

**Check.** A convenient gap is necessary but not sufficient: the
$1107\ \mathrm{nm}$ emission of silicon is a perfectly usable near-infrared
wavelength, yet its indirect gap makes the radiative rate negligible compared with
non-radiative channels.

**Where marks are lost.** Choosing $\ce{SiC}$, which has a wide gap of
$3.26\ \mathrm{eV}$ and is used in power devices, but is indirect.

### 56. Current at 5C

**Strategy.** Convert the C-rate to a current with $I = C_\mathrm{rate}Q_\mathrm{nom}$.

**Answer.** **D ($20\ \mathrm{A}$).**

**Working.** C-rate is a reciprocal time, so $I = C_\mathrm{rate}Q_\mathrm{nom} =
5 \times 4.0\ \mathrm{A} = 20\ \mathrm{A}$, which discharges the cell in
$60/5 = 12\ \mathrm{min}$.

**Best distractor.** B ($4.0\ \mathrm{A}$) is the 1C current; it is selected by
students who read "5C" as a capacity rather than a rate.

**Check.** The discharge time $60/5 = 12\ \mathrm{min}$ follows from the same
definition, and $20\ \mathrm{A} \times 0.20\ \mathrm{h} = 4.0\ \mathrm{Ah}$ returns
the nominal capacity.

**Where marks are lost.** Choosing $5.0\ \mathrm{A}$ by confusing the numeral 5 with
the current in amperes.

### 57. A small aluminium rivet in a stainless plate

**Strategy.** Identify the anodic member of the couple in seawater, then apply the
area ratio.

**Answer.** **A (the rivet corrodes rapidly).**

**Working.** Aluminium is anodic to stainless steel in seawater. The galvanic current
is set by the couple, but the anodic current density is that current divided by the
small rivet area, so the rivet penetrates quickly.

**Best distractor.** D (the rivet is cathodically protected by the plate) reverses
the polarity: cathodic protection of the rivet would require the rivet to be the
cathode, which is the case only if the coupled metal were more active than aluminium.

**Check.** Reversing the areas — a large aluminium plate with a small stainless
fastener — reduces the anodic current density by orders of magnitude, which confirms
that the area ratio, not the potential difference alone, sets the damage rate.

**Where marks are lost.** Choosing C (both passive) on the assumption that a passive
film prevents galvanic corrosion. The film raises the potential but does not stop the
couple, and the rivet's film is easily disrupted.

### 58. Catalyst for the contact process

**Strategy.** Match each catalyst to the plant in which it operates before choosing.

**Answer.** **B ($\ce{V2O5}$ on silica with potassium sulfate promoters).**

**Working.** The contact process oxidises $\ce{SO2}$ to $\ce{SO3}$ over a vanadia
catalyst at $400$–$450\ ^\circ\mathrm{C}$; the alkali promoters raise the activity
and the silica support gives a thermally stable, porous pellet.

**Best distractor.** C (a platinum–rhodium gauze) is the catalyst for ammonia
oxidation in the Ostwald process, a different plant and a different reaction.

**Check.** Vanadia is a selective oxidation catalyst and operates at
$400$–$450\ ^\circ\mathrm{C}$, above its ignition temperature and low enough to keep
the exothermic equilibrium favourable — the reason for the two-bed arrangement with
interstage cooling.

**Where marks are lost.** Choosing A (iron with potassium oxide, alumina and calcium
oxide promoters), which is the Haber–Bosch ammonia catalyst.

---

## Top ten errors in this level

| # | Error | Why it costs marks | Correct approach |
|---|---|---|---|
| 1 | Using $M_n$ and $M_w$ interchangeably | Melt viscosity and processing track $M_w$; osmotic and end-group methods give $M_n$ | State the average and the method; PDI is $M_w/M_n$ |
| 2 | Ignoring stoichiometric imbalance in step-growth | $X_n = 1/(1-p)$ is valid only for $r = 1$; a $1\ \%$ excess caps $X_n$ near $199$ | Use $X_n = (1+r)/(1+r-2rp)$ and quote $r$ |
| 3 | Treating $T_g$ as a melting point | $T_g$ is a kinetic transition that depends on rate and thermal history; $T_m$ is first-order | Report the heating and cooling rate with every $T_g$ |
| 4 | Confusing crystallite size with particle size | Scherrer sees coherent domains; a particle may contain many crystallites | Report method and weighting; compare XRD, TEM, DLS and BET |
| 5 | Using $E = hc/\lambda$ with mixed units | Nanometres, electronvolts and joules are the usual trap; errors of $10^{9}$ | Convert to SI first, or use $\lambda/\mathrm{nm} = 1240/(E/\mathrm{eV})$ |
| 6 | Describing an indirect-gap material as an emitter | Momentum conservation needs a phonon; the radiative rate is negligible | Check direct or indirect before proposing an LED or laser material |
| 7 | Using $n = 1$ for a multi-electron battery reaction | Capacity scales with $n$; Li–S and $\ce{LiFePO4}$ are not one-electron cases in the same sense | Write the balanced half-reaction and count electrons per formula unit |
| 8 | Quoting theoretical capacity as deliverable capacity | Binder, conductive additive, inactive phases and voltage limits reduce it | State the active-material basis and the utilisation |
| 9 | Using atomic mass instead of equivalent mass in Faraday's law | $M_\mathrm{eq} = M/n$; iron as $\ce{Fe^{2+}}$ gives $27.92$, not $55.85$ | Identify the oxidation state before dividing |
| 10 | Comparing equilibrium constants or conversions without the boundary | Ideal-gas $K_p$, fugacity-corrected $K$, per-pass and recycle conversions are different quantities | Declare ideal or real, per-pass or overall, and the pressure and temperature |

---

**Exercise bank:** [`../exercises/level-9a-materials-exercises.md`](../exercises/level-9a-materials-exercises.md)
