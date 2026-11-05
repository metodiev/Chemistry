# Level 5 — Worked Solutions: Inorganic Chemistry

> **Level:** Advanced (Level 5 — Inorganic Chemistry)
> **Items:** 58
> **Exercise bank:** [`../exercises/level-5-exercises.md`](../exercises/level-5-exercises.md)

Each solution gives the **Strategy**, the **Working**, the **Answer** and a
**Check**. Items marked **multi-step** require at least three dependent operations.
Electron counts are shown in full because a bare total conceals the two errors that
actually occur: mixing the ionic and covalent conventions, and miscounting a
polydentate or bridging ligand.

Conventions: $\Delta_o = 10Dq$; CFSE is quoted as a multiple of $\Delta_o$ with the
barycentre as zero; magnetic moments are spin-only unless the item says otherwise;
"labile" and "inert" are kinetic terms and have nothing to do with thermodynamic
stability.

---

## Part A — Conceptual questions

### 1. Constant $Z_{\text{eff}}$ and falling ionisation energy

**Strategy.** Separate the screening argument (which controls $Z_{\text{eff}}$) from
the size argument (which controls the ionisation energy).

**Working.** Slater's rules give, for the valence $s$ electron of sodium
($Z = 11$, $[\ce{Ne}]3s^1$):

$$S = 8(0.85) + 2(1.00) = 8.80, \qquad Z_{\text{eff}} = 11 - 8.80 = 2.20$$

For potassium ($Z = 19$, $[\ce{Ar}]4s^1$):

$$S = 8(0.85) + 10(1.00) = 16.80, \qquad Z_{\text{eff}} = 19 - 16.80 = 2.20$$

The extra shell contributes eight protons and eight electrons, all in the $n = 3$
shell, and each of those electrons screens the $4s$ electron by 0.85. The added
nuclear charge is therefore almost exactly cancelled by the added screening, so
$Z_{\text{eff}}$ is unchanged: from sodium to potassium the shielding rises from
8.80 to 16.80 while the nuclear charge rises from 11 to 19.

The ionisation energy, however, depends on the distance of the electron from the
nucleus as well as on the net charge attracting it. The $4s$ orbital of potassium is
larger and more diffuse than the $3s$ orbital of sodium, so the electron is farther
from the nucleus and the Coulomb attraction is weaker. The first ionisation energy
therefore falls from 496 to $419\ \text{kJ mol}^{-1}$ even though $Z_{\text{eff}}$ is
the same.

**Answer.** $Z_{\text{eff}}$ is constant because each new shell adds as much screening
as nuclear charge; the ionisation energy falls because the valence orbital is larger
and the electron is farther from the nucleus.

**Check.** The same argument applies down Group 1 and Group 17: $Z_{\text{eff}}$ is
roughly constant down a group, while ionisation energy falls and atomic radius rises.
If $Z_{\text{eff}}$ were the only variable, ionisation energies would be constant down
a group, which they are not.

**Where marks are lost.** Saying that "the nucleus holds the electron less tightly
because there are more electrons" without distinguishing nuclear charge from
screening, or claiming $Z_{\text{eff}}$ decreases down the group.

### 2. The inert-pair effect

**Strategy.** Compare the cost of removing the $ns^2$ pair with the bond energy that
the higher oxidation state can recover.

**Working.** The inert-pair effect is the observation that, for the heavier $p$-block
elements, the $ns^2$ pair becomes increasingly reluctant to participate in bonding, so
the oxidation state two below the group maximum becomes the more stable one.

For thallium ($[\ce{Xe}]4f^{14}5d^{10}6s^26p^1$), the $6s$ electrons are stabilised by
two effects. First, the $4f$ and $5d$ electrons screen the nuclear charge poorly, so
the $6s$ orbital is drawn in and its energy is lowered. Second, relativistic
contraction of the $6s$ orbital — the inner electrons move faster and their mass
increases — further stabilises it. Removing the $6s^2$ pair therefore costs much more
than the trend in ionisation energy would suggest. The result is that Tl(I), with a
$6s^2$ configuration, is the stable oxidation state in water and in most salts, and
Tl(III) is a strong oxidant ($\ce{Tl^3+/Tl+}$ is about $+1.25\ \text{V}$).

For aluminium ($[\ce{Ne}]3s^23p^1$), the $3s$ pair is not inert: the third ionisation
energy is high but accessible (about $2745\ \text{kJ mol}^{-1}$), and the $+3$ state is
stabilised by the high lattice enthalpies and hydration enthalpies of the small
$\ce{Al^3+}$ ion. Aluminium(III) is therefore the normal state, and Al(I) is not
accessible in ordinary chemistry.

**Answer.** Tl(I) is stabilised by the inert $6s^2$ pair; Al(III) is stabilised by the
high charge density and lattice/hydration enthalpies, and its $3s^2$ pair is not inert.

**Check.** The effect grows down each $p$ block: Ga(I) and In(I) are both known but
Tl(I) is the extreme case; Pb(II) is more stable than Pb(IV), whereas Sn(IV) is more
stable than Sn(II). The trend is consistent.

**Where marks are lost.** Attributing the effect only to "poor shielding by $d$
electrons", which is part of the story, and ignoring the relativistic contribution
and the lattice-energy term.

### 3. Variable oxidation states and the maximum at manganese

**Strategy.** Energy-gap argument for variability; contraction argument for the
post-manganese fall.

**Working.** The $3d$, $4s$ and $4p$ orbitals of the first transition series are close
in energy (within a few hundred kilojoules per mole), and the $3d$ electrons are
valence electrons that can be removed or shared without prohibitive cost. Because the
energy required to remove successive electrons is comparable with the extra bond
energy that the higher oxidation state can recover from ligands, several oxidation
states are accessible for each element. The availability of $d$ orbitals also allows
the metal to form bonds of different order and coordination number, which further
widens the range.

The maximum oxidation state rises from $+3$ at scandium to $+7$ at manganese because
the number of valence electrons ($3d^n4s^2$) rises from three to seven, and all of
them can be used in bonding.

After manganese the maximum falls (iron $+6$ is rare, cobalt $+4$ and nickel $+4$
require stabilising ligands) even though the nuclear charge continues to rise. The
reason is that the $3d$ orbitals become progressively more contracted and more
strongly bound as the series is crossed; the additional $d$ electrons are core-like
and removing them costs more than the higher oxidation state can recover in bond
energy. In the heavier $4d$ and $5d$ series the orbitals are larger and more diffuse,
so the higher oxidation states are stabilised again — osmium(VIII) and ruthenium(VIII)
are stable, whereas iron(VIII) is not.

**Answer.** Variability follows from the small $3d$/$4s$/$4p$ energy gap and the
availability of $d$ electrons for bonding. The maximum is $+7$ at manganese because
manganese has seven valence electrons; it falls afterwards because the $3d$ orbitals
contract and become core-like.

**Check.** The argument correctly predicts that the highest oxidation states are found
in oxides and fluorides (the most electronegative ligands), and that low oxidation
states are stabilised by $\pi$-acceptor ligands such as $\ce{CO}$.

**Where marks are lost.** Saying "the maximum falls because there are more electrons
to pair", which confuses electron count with orbital contraction.

### 4. $\Delta_o$ against the pairing energy

**Strategy.** Define both quantities, then compare them for a $d^n$ case where the
choice is real.

**Working.** $\Delta_o$ is the energy gap between the $t_{2g}$ and $e_g$ sets in an
octahedral field. The barycentre is unchanged, so the $t_{2g}$ set lies
$-0.4\Delta_o$ below it and the $e_g$ set $+0.6\Delta_o$ above it.

The spin-pairing energy $P$ is the energy cost of placing two electrons in the same
orbital. It has two parts: the Coulomb repulsion between two electrons in the same
region of space, and the loss of exchange stabilisation that accompanies the
destruction of a parallel-spin arrangement.

For a $d^4$ ion the fourth electron has two choices: enter the higher $e_g$ orbital
(costing $\Delta_o$ but gaining exchange stabilisation) or pair in a $t_{2g}$ orbital
(costing $P$). If $\Delta_o < P$ the electron enters $e_g$ and the complex is
**high-spin**; if $\Delta_o > P$ it pairs and the complex is **low-spin**. For
$d^5$, $d^6$ and $d^7$ the same competition recurs, and the crossover is what makes
the spin state ligand-dependent.

**Answer.** $\Delta_o$ is the crystal-field splitting; $P$ is the energy penalty for
pairing two electrons in one orbital. High spin results when $\Delta_o < P$, low spin
when $\Delta_o > P$.

**Check.** The model explains why $\ce{[Fe(H2O)6]^2+}$ is high spin ($\Delta_o$ for
water is moderate) and $\ce{[Fe(CN)6]^4-}$ is low spin (cyanide is at the strong-field
end of the spectrochemical series). It also explains why $d^1$, $d^2$, $d^3$, $d^8$,
$d^9$ and $d^{10}$ have no spin-state ambiguity.

**Where marks are lost.** Describing $P$ as "the energy needed to pair spins" without
mentioning electron–electron repulsion, or claiming that low spin is always more
stable.

### 5. The chelate effect

**Strategy.** A Gibbs-energy decomposition; identify which term dominates.

**Working.** The relevant equilibria are

$$\ce{[Ni(H2O)6]^2+(aq) + 6NH3(aq) <=> [Ni(NH3)6]^2+(aq) + 6H2O(l)}
\qquad \log\beta_6 \approx 8.6$$

$$\ce{[Ni(H2O)6]^2+(aq) + 3en(aq) <=> [Ni(en)3]^2+(aq) + 6H2O(l)}
\qquad \log\beta_3 \approx 18.3$$

The chelate complex is about ten orders of magnitude more stable even though the donor
atoms are the same (nitrogen) and the enthalpy change is similar. The difference is
entropic. In the first reaction six ligands replace six water molecules, so the number
of independent particles is unchanged ($\Delta S^\circ \approx 0$). In the second,
three ligands replace six water molecules, so the number of independent particles
increases from four to seven. The translational entropy therefore rises substantially,
and since $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$, a positive
$\Delta S^\circ$ makes $\Delta G^\circ$ more negative. The $-T\Delta S^\circ$ term
contributes several tens of kilojoules per mole, which corresponds to the observed
difference in $\log\beta$.

**Answer.** The chelate effect is predominantly entropic: a polydentate ligand releases
more solvent molecules than the number of ligand particles it contributes, increasing
the translational entropy. The enthalpy term is small.

**Check.** The effect is larger for higher denticity and smaller for rigid ligands that
lose internal entropy on binding — which is exactly what the entropic model predicts,
and it is why macrocyclic ligands (the macrocyclic effect) bind even more strongly.

**Where marks are lost.** Attributing the effect to "stronger bonds" — the Ni–N bond
strength is essentially the same in both complexes.

### 6. The 18-electron rule and its systematic failures

**Strategy.** State the rule, define the conventions, then explain two structural
classes that disobey it.

**Working.** A complex is most stable when the metal has 18 valence electrons,
corresponding to a filled $ns^2(n-1)d^{10}np^6$ shell. In the **ionic convention** the
ligands are removed with their bonding pairs and the metal oxidation state is
calculated; in the **covalent convention** each metal–ligand bond is split equally and
the metal is treated as neutral. Both give the same total, but the intermediate numbers
differ and the two must never be mixed.

$\ce{[PtCl4]^2-}$: platinum(II) is $d^8$ and contributes 8 electrons; four chlorides
contribute 8; the total is 16. The complex is square planar, and the vacant $p_z$
orbital is accessible, so the metal can accept a fifth ligand readily. That is why
16-electron $d^8$ complexes are stable and why they are catalysts: the vacant site is
the reactive feature, not a defect.

$\ce{[Ni(C5H5)2]}$: nickel(II) is $d^8$ and contributes 8; two cyclopentadienyl anions
contribute 12; the total is 20. The extra two electrons must occupy antibonding
orbitals, which weakens the metal–ligand bonds. Nickelocene is therefore less stable
than ferrocene, is readily oxidised to the 18-electron cation $\ce{[Ni(C5H5)2]+}$, and
has longer Ni–C bonds.

**Answer.** The rule states that 18 valence electrons give the most stable complex.
16-electron square-planar $d^8$ complexes are stable because they have an accessible
vacant $p_z$ orbital; 20-electron metallocenes are destabilised because the extra
electrons enter antibonding orbitals.

**Check.** The rule also fails for early metals in high oxidation states
($\ce{[TiCl4]}$, 8 electrons) because there are no low-lying $d$ electrons to fill, and
for 17-electron radicals, which are reactive by construction.

**Where marks are lost.** Mixing conventions (for example counting $\ce{Cl-}$ as a
neutral radical donor while treating the metal as an ion), which produces a total that
is wrong by the charge.

### 7. Radius-ratio rules and their failures

**Strategy.** State the geometric limits, then give two chemical reasons why the
hard-sphere model fails.

**Working.** If a structure is modelled as a close-packed array of large anions with
small cations in the interstices, the preferred coordination number is fixed by the
ratio $r_+/r_-$. The limiting values are derived by requiring the cation and anion to
touch while the anions remain in contact:

- $0.225$–$0.414$: tetrahedral, CN 4;
- $0.414$–$0.732$: octahedral, CN 6;
- $0.732$–$1.000$: cubic, CN 8.

Two classes of failure are important.

**Substantial covalency.** The model treats the ions as rigid spheres with a purely
ionic interaction. When the bonding has significant covalent character, the
coordination number is set by orbital overlap rather than by packing. Zinc sulfide is
tetrahedral even at ratios that would suggest octahedral coordination, and $\ce{BeF2}$
is tetrahedral rather than octahedral; both are consequences of directional covalent
bonding.

**Polarisable ions and lone pairs.** Large, soft anions such as iodide are easily
polarised, and the induced dipole favours lower coordination numbers and more covalent
structures; AgI and CuCl adopt the zinc blende structure for this reason. A
stereochemically active lone pair on the cation also distorts the coordination
geometry: PbO and SnO adopt layered structures rather than the rock-salt arrangement.

A third, milder failure is that borderline ratios (near 0.414 or 0.732) are decided by
lattice-energy differences of only a few kilojoules per mole, so the rule is unreliable
exactly where it is most needed.

**Answer.** The limits are 0.225–0.414 (CN 4), 0.414–0.732 (CN 6) and 0.732–1.000
(CN 8). The rules fail when bonding is substantially covalent (ZnS, $\ce{BeF2}$) and
when the ions are polarisable or carry a stereochemically active lone pair (AgI, PbO).

**Check.** The rules work well for the alkali halides, where the ions are hard and the
bonding is ionic — which is exactly the regime the model was designed for.

**Where marks are lost.** Quoting the limits without saying which ratio range gives
which coordination number, or offering "the ions are not spheres" as the only
explanation without a chemical example.

### 8. Trans influence and trans effect

**Strategy.** Separate the thermodynamic quantity from the kinetic one, then apply each
to the two syntheses.

**Working.** The **trans influence** is a ground-state thermodynamic effect: a strong
σ-donor competes with the ligand opposite it for the same metal orbital, so it
lengthens and weakens that metal–ligand bond. It can be measured by X-ray
crystallography in the resting complex.

The **trans effect** proper is a kinetic effect: the same ligand stabilises the
five-coordinate transition state for substitution, lowering the activation energy for
replacement of the ligand opposite it. It is measured by rates.

Both effects follow the series $\ce{CN-} \approx \ce{CO} \approx \ce{C2H4} \approx \ce{PR3} > \ce{H-} > \ce{CH3-} > \ce{Cl-} > \ce{NH3} > \ce{H2O}$.

In the synthesis from $\ce{[PtCl4]^2-}$, the first ammonia replaces one chloride at,
say, position 1. The complex is now $\ce{[PtCl3(NH3)]-}$, with chlorides at positions
2, 3 and 4. The chloride at position 3 is *trans* to the ammonia and is therefore only
weakly labilised, because ammonia has a low trans effect. The chlorides at positions 2
and 4 are each *trans* to another chloride, and chloride has a high trans effect, so
those two positions are strongly labilised. The second ammonia therefore attacks at
position 2 or 4, which places it *cis* to the first ammonia. The product is
*cis*-$\ce{[PtCl2(NH3)2]}$, cisplatin.

In the synthesis from $\ce{[Pt(NH3)4]^2+}$, the first chloride replaces an ammonia at
position 1. The complex is now $\ce{[PtCl(NH3)3]+}$, and the ligand *trans* to the new
chloride is an ammonia at position 3. Chloride has a higher trans effect than ammonia,
so that ammonia is strongly labilised and is the one displaced by the second chloride.
The second chloride therefore enters *trans* to the first, giving the *trans* isomer.

**Answer.** Trans influence is thermodynamic and describes bond weakening in the ground
state; the trans effect is kinetic and describes transition-state stabilisation. The
trans effect makes the two routes stereochemically complementary.

**Check.** The two routes use the same stoichiometry and the same two ligands but give
opposite isomers, which is only possible if the order of addition determines the
outcome — the signature of kinetic control through the trans effect.

**Where marks are lost.** Using the two terms interchangeably, or failing to state
which ligand is trans to which after the first substitution.

### 9. The lanthanide contraction

**Strategy.** Explain the origin (poor $4f$ shielding) and then list consequences that
follow directly.

**Working.** Across the lanthanide series each element adds one proton and one $4f$
electron. The $4f$ radial distribution lies inside the $5s$ and $5p$ shells, so the
$4f$ electrons screen the nuclear charge poorly. The effective nuclear charge felt by
the outer shells therefore rises steadily, and the ions contract. The six-coordinate
radius of $\ce{La^3+}$ is 103.2 pm and that of $\ce{Lu^3+}$ is 86.1 pm, a contraction
of 17.1 pm (16.6 %) across fourteen elements.

Consequences:

1. **Yttrium behaves as a heavy lanthanide.** The radius of $\ce{Y^3+}$ (90.0 pm)
   matches that of $\ce{Ho^3+}$ (90.1 pm), so yttrium is found with the heavy
   lanthanides in minerals and is separated with them.
2. **Zirconium and hafnium are almost identical in size.** $\ce{Zr^4+}$ (72 pm) and
   $\ce{Hf^4+}$ (71 pm) differ by about 1 pm because the contraction cancels the
   expected increase from the fourth to the fifth period. Hafnium is therefore always
   found with zirconium and is very difficult to separate.
3. **Density and basicity trends.** The increasing charge density across the series
   raises the density and the polarising power of the ions, so the hydroxides become
   progressively less basic from lanthanum to lutetium.
4. **Coordination numbers fall.** Early lanthanides reach CN 9–12; the later, smaller
   ions typically reach 6–8.

**Answer.** The contraction is the steady decrease in radius across the series caused
by poor $4f$ shielding. Its consequences include the yttrium/heavy-lanthanide
association, the near-identity of $\ce{Zr^4+}$ and $\ce{Hf^4+}$, increasing density and
decreasing hydroxide basicity, and falling coordination numbers.

**Check.** The magnitude — about 1.2 pm per element — is small for one step but
cumulative, which is why a separation method based on small differences in radius
(ion-exchange with EDTA) is needed rather than simple precipitation.

**Where marks are lost.** Saying the contraction is caused by "the filling of the $4f$
subshell" without saying that the $4f$ electrons shield poorly.

### 10. The logic of Group I–V qualitative analysis

**Strategy.** Explain the principle (class reagents), then the specific sulphur
equilibria.

**Working.** Classical qualitative analysis does not test for each cation separately.
It uses a sequence of class reagents, each of which precipitates a whole group under
controlled conditions, so that a complex mixture is divided into a few manageable
fractions. The groups are:

| Group | Reagent | Cations |
|---|---|---|
| I | dilute $\ce{HCl}$ | $\ce{Ag+}$, $\ce{Pb^2+}$, $\ce{Hg2^2+}$ |
| II | $\ce{H2S}$ in acid | $\ce{Pb^2+}$, $\ce{Bi^3+}$, $\ce{Cu^2+}$, $\ce{Cd^2+}$, $\ce{Hg^2+}$, $\ce{As^3+}$, $\ce{Sb^3+}$, $\ce{Sn^2+}$ |
| III | $\ce{NH3}$/$\ce{NH4Cl}$ | $\ce{Al^3+}$, $\ce{Cr^3+}$, $\ce{Fe^3+}$ |
| IV | $\ce{H2S}$ in alkali | $\ce{Zn^2+}$, $\ce{Mn^2+}$, $\ce{Ni^2+}$, $\ce{Co^2+}$ |
| V | $\ce{(NH4)2CO3}$ | $\ce{Ba^2+}$, $\ce{Sr^2+}$, $\ce{Ca^2+}$ |

The separation of Group II from Group IV is a solubility-product effect, not an
intrinsic difference in "reactivity towards sulphur". The sulphide precipitation
equilibrium is

$$\ce{M^2+(aq) + H2S(aq) <=> MS(s) + 2H+(aq)}$$

In acidic solution the high hydrogen-ion concentration suppresses the second
dissociation of $\ce{H2S}$ ($\mathrm{p}K_{a2} \approx 14$), so $[\ce{S^2-}]$ is
extremely low. Only sulphides with very small $K_{sp}$ — the Group II sulphides, with
$K_{sp}$ of order $10^{-30}$ or smaller — exceed saturation and precipitate. Group IV
sulphides such as ZnS and MnS have much larger $K_{sp}$ ($10^{-25}$ to $10^{-10}$) and
remain in solution at that $[\ce{S^2-}]$. When the solution is made alkaline with
ammonia, the hydrogen-ion concentration falls by many orders of magnitude, $[\ce{S^2-}]$
rises correspondingly, and the Group IV sulphides now precipitate.

**Answer.** The scheme separates cations by class reagents, each exploiting a
solubility threshold. $\ce{H2S}$ in acid gives a very low $[\ce{S^2-}]$ and precipitates
only the most insoluble (Group II) sulphides; alkaline conditions raise $[\ce{S^2-}]$
enough to precipitate the more soluble Group IV sulphides.

**Check.** The scheme also explains why Group III is precipitated as hydroxides before
Group IV sulphides: the ammonia buffer removes the ions that would otherwise interfere,
and the amphoteric hydroxides of aluminium and chromium can then be separated from
iron by excess alkali.

**Where marks are lost.** Saying "Group II sulphides are insoluble and Group IV
sulphides are soluble" without the $[\ce{S^2-}]$ control, which is the actual chemical
variable.

---

## Part B — Basic problems

### 11. First ionisation energies across Period 3

**Strategy.** Recall the trend, then identify the two subshell effects.

**Working.** The values are Na 496, Mg 738, Al 578, Si 786, P 1012, S 1000,
Cl 1251 and Ar $1521\ \text{kJ mol}^{-1}$.

The general increase arises because the nuclear charge rises across the period while
the electrons enter the same shell ($n = 3$), so $Z_{\text{eff}}$ increases and the
radius falls.

Two anomalies occur. Between Mg and Al the ionisation energy falls (738 → 578) because
the electron removed from aluminium is a $3p$ electron, which is higher in energy and
better shielded than the $3s$ electron removed from magnesium. Between P and S the
ionisation energy falls (1012 → 1000) because phosphorus has a half-filled $3p^3$
subshell: removing an electron from the doubly occupied $3p$ orbital of sulfur relieves
electron–electron repulsion, so the process costs slightly less than the trend
predicts.

**Answer.** Na < Al < Mg < Si < S < P < Cl < Ar.

**Check.** The same two anomalies occur in Period 2 (Be → B and N → O), which confirms
that they are subshell effects rather than peculiarities of the third period.

**Where marks are lost.** Placing Mg below Al because "ionisation energy increases
across a period" is the simplified rule; the rule has exceptions that must be applied.

### 12. Configurations and $d$ counts

**Strategy.** Remove the $4s$ electrons first, then count the $3d$ electrons.

**Working.** For a first-row transition metal, the $4s$ electrons are removed before
the $3d$ electrons, because once the $3d$ subshell is occupied it lies lower in energy
than $4s$.

- $\ce{Fe}$ is $[\ce{Ar}]3d^64s^2$; $\ce{Fe^3+}$ is $[\ce{Ar}]3d^5$ ($d^5$).
- $\ce{Cr}$ is $[\ce{Ar}]3d^54s^1$; $\ce{Cr^3+}$ is $[\ce{Ar}]3d^3$ ($d^3$).
- $\ce{Cu}$ is $[\ce{Ar}]3d^{10}4s^1$; $\ce{Cu+}$ is $[\ce{Ar}]3d^{10}$ ($d^{10}$).
- $\ce{Mn}$ is $[\ce{Ar}]3d^54s^2$; $\ce{Mn^2+}$ is $[\ce{Ar}]3d^5$ ($d^5$).
- $\ce{Co}$ is $[\ce{Ar}]3d^74s^2$; $\ce{Co^2+}$ is $[\ce{Ar}]3d^7$ ($d^7$).

**Answer.** $\ce{Fe^3+}$ $d^5$; $\ce{Cr^3+}$ $d^3$; $\ce{Cu+}$ $d^{10}$;
$\ce{Mn^2+}$ $d^5$; $\ce{Co^2+}$ $d^7$.

**Check.** The electron count balances the charge in every case: iron (Z = 26) with
charge +3 has 23 electrons, which is $18 + 5$; that is $d^5$.

**Where marks are lost.** Writing $\ce{Fe^3+}$ as $3d^34s^2$ by removing the $3d$
electrons first.

### 13. Oxidation states

**Strategy.** Assign the ligand charges first, then solve for the metal.

**Working.** Cyanide is $-1$: $\ce{[Fe(CN)6]^4-}$ gives $x - 6 = -4$, so $x = +2$.
Permanganate: $\ce{MnO4-}$ gives $x - 8 = -1$, so $x = +7$. Dichromate:
$\ce{Cr2O7^2-}$ gives $2x - 14 = -2$, so $x = +6$. Tetraamminecopper(II) is given as
$+2$. In $\ce{Fe(CO)5}$ and $\ce{[Ni(CO)4]}$ the carbonyl ligand is neutral, so the
metals are in oxidation state 0.

**Answer.** Fe +2; Mn +7; Cr +6; Cu +2; Fe 0; Ni 0.

**Check.** The metal oxidation state must be consistent with a sensible $d$ count:
manganese(VII) is $d^0$, and the intense purple colour of permanganate is a
charge-transfer band rather than a $d$–$d$ transition, which is exactly what a $d^0$
assignment requires.

**Where marks are lost.** Treating $\ce{CO}$ as an anionic ligand and assigning iron
$+5$ in $\ce{Fe(CO)5}$.

### 14. Naming complexes

**Strategy.** Apply the Red Book rules in order: cation, ligands alphabetically, metal
with oxidation state, then the anion.

**Working.**

(a) The cation contains four ammines and two chlorides and carries a charge of $+1$,
so cobalt is $+3$. Alphabetically ammine precedes chlorido:
tetraamminedichloridocobalt(III) chloride.

(b) Six cyanides and a charge of $-3$ give iron $+3$; the complex is anionic, so iron
becomes ferrate: potassium hexacyanidoferrate(III).

(c) Platinum(II) with two ammines and two chlorides; the *cis* prefix is italicised and
placed first: *cis*-diamminedichloridoplatinum(II).

(d) Six waters on chromium(III): hexaaquachromium(III) chloride.

**Answer.** As above.

**Check.** The charge balance in (a) is $+3 - 2 - 1 = 0$, matching the chloride
counter-ion; in (b) it is $+3 - 6 = -3$, matching three potassium ions.

**Where marks are lost.** Writing "chloro" instead of "chlorido", or omitting the
oxidation state.

### 15. Formulae from names

**Strategy.** Parse the name into cation and anion, then assemble with charge balance.

**Working.**

(a) Tetraamminecopper(II) is $\ce{[Cu(NH3)4]^2+}$; sulfate is $\ce{SO4^2-}$, so the
formula is $\ce{[Cu(NH3)4]SO4}$.

(b) Hexachloridoplatinate(IV) is $\ce{[PtCl6]^2-}$ with potassium:
$\ce{K2[PtCl6]}$.

(c) Tris(ethane-1,2-diamine)cobalt(III) is $\ce{[Co(en)3]^3+}$ with three chlorides:
$\ce{[Co(en)3]Cl3}$.

(d) Tetrahydroxidozincate(II) is $\ce{[Zn(OH)4]^2-}$ with two sodiums:
$\ce{Na2[Zn(OH)4]}$.

**Answer.** As above.

**Check.** Charge balance: (a) $+2 - 2 = 0$; (b) $2(+1) - 2 = 0$; (c) $+3 - 3 = 0$;
(d) $2(+1) - 2 = 0$.

**Where marks are lost.** Writing $\ce{[Cu(NH3)4]SO4}$ as $\ce{[Cu(NH3)4SO4]}$, which
places the sulfate inside the coordination sphere.

### 16. Isomer counts

**Strategy.** For each complex, enumerate the geometrical arrangements and test each
for chirality.

**Working.**

(a) $\ce{[Co(NH3)4Cl2]+}$: the two chlorides may be adjacent (*cis*) or opposite
(*trans*). Two geometrical isomers. Neither is chiral: the *trans* isomer has a centre
of symmetry, and the *cis* isomer has a mirror plane containing the two chlorides and
the metal.

(b) $\ce{[Co(en)2Cl2]+}$: *cis* and *trans*. The *trans* isomer has a plane of
symmetry and is achiral. The *cis* isomer has no mirror plane or centre of inversion;
it exists as $\Delta$ and $\Lambda$ enantiomers. Three stereoisomers in total.

(c) $\ce{[Co(NH3)3Cl3]}$: the three chlorides may occupy one triangular face (*fac*) or
a meridian (*mer*). Two geometrical isomers, neither chiral.

(d) $\ce{[Pt(NH3)2Cl2]}$: square planar, *cis* and *trans*. Two isomers; neither is
chiral (both are planar).

**Answer.** (a) 2; (b) 3; (c) 2; (d) 2.

**Check.** The only case with optical activity is (b), which is the standard example of
a chiral *cis*-bis(bidentate) complex.

**Where marks are lost.** Counting 4 for (b) by assuming that *cis* and *trans* each
give a pair of enantiomers; *trans* is achiral.

### 17. Electron counts

**Strategy.** Use the neutral-atom (covalent) convention: group number plus ligand
electrons, adjusted for charge.

**Working.**

- $\ce{[Ni(CO)4]}$: Ni is group 10, contributing 10; four carbonyls contribute 8;
  total 18.
- $\ce{[Fe(CO)5]}$: Fe is group 8, contributing 8; five carbonyls contribute 10;
  total 18.
- $\ce{[Cr(CO)6]}$: Cr is group 6; six carbonyls contribute 12; total 18.
- Ferrocene, $\ce{[Fe(C5H5)2]}$: Fe is group 8, but the complex is conventionally
  treated with $\ce{Fe^2+}$ ($d^6$, 6 electrons) and two cyclopentadienyl anions
  (6 each); total $6 + 12 = 18$.
- $\ce{[Co(CO)4]-}$: Co is group 9; the negative charge adds one electron to the metal
  count, giving 10; four carbonyls contribute 8; total 18.

**Answer.** All five are 18-electron complexes.

**Check.** In the ionic convention the same totals are obtained: $\ce{Ni(0)}$ $d^{10}$
+ 8 = 18; $\ce{Fe(0)}$ $d^8$ + 10 = 18; $\ce{Cr(0)}$ $d^6$ + 12 = 18; $\ce{Fe^2+}$
$d^6$ + 12 = 18; $\ce{Co(-I)}$ $d^{10}$ + 8 = 18.

**Where marks are lost.** Counting the cyclopentadienyl ligand as 5 electrons (one per
carbon) instead of 6 (the aromatic sextet).

### 18. Carbonyl stretching frequencies

**Strategy.** Relate $\tilde{\nu}(\ce{CO})$ to the amount of metal-to-ligand
back-donation.

**Working.** Back-donation populates the $\pi^*$ orbital of $\ce{CO}$, which weakens the
C–O bond and lowers the stretching frequency. Anything that increases electron density
at the metal increases back-donation and lowers $\tilde{\nu}$; anything that withdraws
electron density raises it.

The series is $\ce{[V(CO)6]-}$ (1860) < $\ce{[Cr(CO)6]}$ (2000) <
$\ce{[Mn(CO)6]+}$ (2090) < free $\ce{CO}$ (2143). The metal charge becomes more
positive across the series (V is $-1$, Cr is 0, Mn is $+1$), so back-donation decreases
and the C–O bond becomes stiffer.

**Answer.** $\ce{[V(CO)6]-}$ < $\ce{[Cr(CO)6]}$ < $\ce{[Mn(CO)6]+}$ < $\ce{CO}$.

**Check.** The free ligand has the highest frequency because there is no back-donation
at all; every complex lowers it, and the anionic complex lowers it most.

**Where marks are lost.** Reversing the trend by treating back-donation as strengthening
the C–O bond; back-donation populates an antibonding orbital, so it weakens it.

### 19. Formula units per unit cell

**Strategy.** Count the ions on corners, edges, faces and in the body, applying the
sharing rules.

**Working.** Rock salt: four cations and four anions per cell, $Z = 4$. Caesium
chloride: one caesium and one chloride per cell, $Z = 1$. Zinc blende: four zinc and
four sulfide, $Z = 4$. Fluorite: four calcium and eight fluoride, $Z = 4$ formula
units. Perovskite $\ce{SrTiO3}$: one strontium, one titanium and three oxygens,
$Z = 1$.

**Answer.** 4, 1, 4, 4, 1.

**Check.** The $Z$ values are consistent with the densities: rock salt and zinc blende
both have $Z = 4$ because both are based on a close-packed anion array with the
cations distributed over the holes.

**Where marks are lost.** Counting a corner atom as one rather than one-eighth, which
multiplies the count by eight.

### 20. Radius-ratio predictions

**Strategy.** Compute $r_+/r_-$ and compare with the limits 0.414 and 0.732.

**Working.**

- NaCl: $102/181 = 0.563$ → octahedral, CN 6, rock salt.
- KBr: $138/196 = 0.704$ → octahedral, CN 6, rock salt.
- CsI: $167/220 = 0.759$ → cubic, CN 8, caesium chloride.
- MgO: $72/140 = 0.514$ → octahedral, CN 6, rock salt.

**Answer.** NaCl rock salt, KBr rock salt, CsI caesium chloride, MgO rock salt.

**Check.** All four predictions agree with experiment. The borderline cases are near
0.73 (for example RbCl at 0.74), where the rule becomes unreliable.

**Where marks are lost.** Comparing the radii in the wrong order ($r_-/r_+$), which
gives a ratio above 1 and an absurd prediction.

### 21. Spin-only moments

**Strategy.** Count unpaired electrons from the $d^n$ configuration, then apply
$\mu = \sqrt{n(n+2)}$.

**Working.** High-spin configurations maximise $n$:

- $\ce{Mn^2+}$ $d^5$: $n = 5$, $\mu = \sqrt{35} = 5.92$.
- $\ce{Fe^3+}$ $d^5$: $n = 5$, $\mu = 5.92$.
- $\ce{Co^2+}$ $d^7$: $n = 3$, $\mu = \sqrt{15} = 3.87$.
- $\ce{Ni^2+}$ $d^8$: $n = 2$, $\mu = \sqrt{8} = 2.83$.
- $\ce{Cu^2+}$ $d^9$: $n = 1$, $\mu = \sqrt{3} = 1.73$.
- $\ce{Zn^2+}$ $d^{10}$: $n = 0$, $\mu = 0$.

**Answer.** 5.92, 5.92, 3.87, 2.83, 1.73 and $0\ \mu_{\text{B}}$.

**Check.** The values match the table in Chapter 7, and they are consistent with the
observed paramagnetism: $\ce{Zn^2+}$ complexes are diamagnetic, $\ce{Cu^2+}$ complexes
have one unpaired electron.

**Where marks are lost.** Using $n(n+2)$ without the square root, or counting the
$d^5$ ion as having one unpaired electron by pairing all five orbitals.

### 22. $4f^n$ configurations of the anomalous lanthanide ions

**Strategy.** Count the $f$ electrons remaining after ionisation, and identify the
special stability of the empty, half-filled or filled subshell.

**Working.** The neutral atoms lose the $6s$ electrons first, and usually the $5d$
electron as well, leaving the $4f^n$ core.

- $\ce{Ce}$ is $[\ce{Xe}]4f^15d^16s^2$; $\ce{Ce^4+}$ is $4f^0$, an empty subshell.
- $\ce{Eu}$ is $[\ce{Xe}]4f^76s^2$; $\ce{Eu^2+}$ is $4f^7$, a half-filled subshell.
- $\ce{Tb}$ is $[\ce{Xe}]4f^96s^2$; $\ce{Tb^4+}$ is $4f^7$, a half-filled subshell.
- $\ce{Yb}$ is $[\ce{Xe}]4f^{14}6s^2$; $\ce{Yb^2+}$ is $4f^{14}$, a filled subshell.

**Answer.** $\ce{Ce^4+}$ $4f^0$; $\ce{Eu^2+}$ $4f^7$; $\ce{Tb^4+}$ $4f^7$;
$\ce{Yb^2+}$ $4f^{14}$.

**Check.** The pattern is consistent: the accessible non-+3 states are exactly those
that reach $f^0$, $f^7$ or $f^{14}$. $\ce{Ce^4+}$ is an oxidant (it wants an electron),
$\ce{Eu^2+}$ and $\ce{Yb^2+}$ are reductants.

**Where marks are lost.** Counting the $6s$ electrons as $4f$ electrons, which shifts
every configuration by two.

---

## Part C — Intermediate problems

### 23. Slater's rules for chlorine and chloride **multi-step**

**Strategy.** Group the electrons, apply the shielding coefficients, then compare.

**Working.** Chlorine ($Z = 17$) is $[\ce{Ne}]3s^23p^5$. For a $3p$ electron, the
other electrons in the same group ($3s^23p^4$) contribute $0.35$ each; the $n = 2$
shell contributes $0.85$ each; the $1s$ shell contributes $1.00$ each.

$$S = 6(0.35) + 8(0.85) + 2(1.00) = 2.10 + 6.80 + 2.00 = 10.90$$

$$Z_{\text{eff}} = 17 - 10.90 = 6.10$$

For the chloride ion, the configuration is $[\ce{Ar}]$, that is $3s^23p^6$. The same
group now contains seven electrons:

$$S = 7(0.35) + 8(0.85) + 2(1.00) = 2.45 + 6.80 + 2.00 = 11.25$$

$$Z_{\text{eff}} = 17 - 11.25 = 5.75$$

The extra electron increases the screening by $0.35$ without changing the nuclear
charge, so $Z_{\text{eff}}$ falls by $0.35$.

**Answer.** $\ce{Cl}$: $Z_{\text{eff}} = 6.10$; $\ce{Cl-}$: $Z_{\text{eff}} = 5.75$.
The neutral atom holds its valence electrons more tightly.

**Check.** The result is consistent with the size difference: the chloride ion is much
larger than the chlorine atom (181 versus 99 pm covalent radius), which is what a lower
$Z_{\text{eff}}$ and an extra electron predict.

**Where marks are lost.** Applying the 0.35 coefficient to all seven $3s3p$ electrons
in the atom (which would count the electron itself) or omitting the $1s$ contribution.

### 24. Disproportionation of copper(I) **multi-step**

**Strategy.** Combine two half-reactions, compute $E^\circ_{\text{cell}}$, then convert
to $\Delta G^\circ$ and $K$.

**Working.** The disproportionation is

$$\ce{2Cu+(aq) -> Cu^2+(aq) + Cu(s)}$$

This is the sum of the oxidation $\ce{Cu+ -> Cu^2+ + e-}$ (the reverse of the
$\ce{Cu^2+/Cu+}$ couple) and the reduction $\ce{Cu+ + e- -> Cu}$. The standard cell
potential is therefore

$$E^\circ_{\text{cell}} = E^\circ(\text{reduction}) - E^\circ(\text{oxidation})
= 0.52 - 0.15 = +0.37\ \text{V}$$

A positive cell potential means a negative Gibbs energy:

$$\Delta G^\circ = -nFE^\circ = -2(96\,485)(0.37) = -71.4\ \text{kJ mol}^{-1}$$

The equilibrium constant follows from $\Delta G^\circ = -RT\ln K$:

$$\ln K = \frac{2(96\,485)(0.37)}{8.314 \times 298} = 28.8, \qquad K = 3.3\times10^{12}$$

**Answer.** $E^\circ_{\text{cell}} = +0.37\ \text{V}$;
$\Delta G^\circ = -71.4\ \text{kJ mol}^{-1}$; $K = 3.3\times10^{12}$. Copper(I)
disproportionates essentially completely in water.

**Check.** The rule of thumb from the Latimer diagram is that a species
disproportionates when the potential to its right is greater than the potential to its
left: $0.52 > 0.15$, so disproportionation is favourable. The calculation confirms it.

**Where marks are lost.** Using $n = 1$ in $\Delta G^\circ$ — two electrons are
transferred per two copper(I) ions — which halves the magnitude of $\Delta G^\circ$.

### 25. CFSE of high-spin and low-spin iron(II) **multi-step**

**Strategy.** Assign the $d^6$ electrons under each spin state, then apply
$\text{CFSE} = (-0.4n_{t_{2g}} + 0.6n_{e_g})\Delta_o$.

**Working.** Iron(II) is $d^6$.

High spin: the electrons occupy $t_{2g}^4e_g^2$, because the fourth and fifth electrons
prefer the higher $e_g$ orbital to pairing. Then

$$\text{CFSE} = \left[-0.4(4) + 0.6(2)\right]\Delta_o = (-1.6 + 1.2)\Delta_o = -0.4\Delta_o$$

The number of unpaired electrons is 4, so $\mu = \sqrt{24} = 4.90\ \mu_{\text{B}}$.

Low spin: the electrons occupy $t_{2g}^6$, and

$$\text{CFSE} = -0.4(6)\Delta_o = -2.4\Delta_o$$

There are no unpaired electrons, so $\mu = 0$.

The difference in CFSE is $2.0\Delta_o$ in favour of the low-spin form, before the
pairing energy is counted. Two extra pairs cost $2P$, so the low-spin form is favoured
only when $2.0\Delta_o > 2P$, that is $\Delta_o > P$.

**Answer.** High spin: $t_{2g}^4e_g^2$, $n = 4$, $\mu = 4.90\ \mu_{\text{B}}$,
CFSE $= -0.4\Delta_o$. Low spin: $t_{2g}^6$, $n = 0$, $\mu = 0$,
CFSE $= -2.4\Delta_o$. The difference is $2.0\Delta_o$.

**Check.** The high-spin moment of $4.90\ \mu_{\text{B}}$ matches the observed value for
$\ce{[Fe(H2O)6]^2+}$ (about 5.3), and the low-spin complex
$\ce{[Fe(CN)6]^4-}$ is diamagnetic. The slight excess over the spin-only value in the
aqua complex is a spin–orbit contribution.

**Where marks are lost.** Using $+0.4$ and $-0.6$ with the wrong signs, which gives a
positive CFSE; the $t_{2g}$ set is stabilised, so its coefficient is negative.

### 26. Stereoisomers of $\ce{[Co(en)2Cl2]+}$ **multi-step**

**Strategy.** Enumerate *cis* and *trans*, then test each for symmetry.

**Working.** With two bidentate en ligands and two chlorides, the chlorides can be
adjacent (*cis*) or opposite (*trans*).

The *trans* isomer has the two chlorides on the $z$ axis and the two en ligands in the
equatorial plane. It possesses a plane of symmetry containing the two chlorides and
bisecting the en chelate rings, and also a centre of inversion. It is achiral.

The *cis* isomer has the two chlorides adjacent. The two en chelate rings form a
propeller-like arrangement, and the complex has a $C_2$ axis but no mirror plane and no
centre of inversion. It is therefore chiral and exists as $\Delta$ and $\Lambda$
enantiomers, which are non-superimposable mirror images.

**Answer.** Three stereoisomers: *cis*-$\Delta$, *cis*-$\Lambda$ (a pair of
enantiomers, both optically active) and *trans* (achiral).

**Check.** The result is consistent with the general rule that *tris*(bidentate) and
*cis*-bis(bidentate) complexes are chiral, whereas the *trans*-bis(bidentate) complex
is not.

**Where marks are lost.** Counting two isomers by ignoring optical isomerism, or
claiming the *cis* isomer is achiral because it "looks symmetric".

### 27. Electron counts and a 20-electron complex **multi-step**

**Strategy.** Use the ionic convention, since two of the complexes carry charges that
are most simply handled that way.

**Working.**

- $\ce{[Mn(CO)5]-}$: manganese is group 7; with an overall charge of $-1$ the metal is
  Mn(-I), which is $d^8$, contributing 8. Five carbonyls contribute 10. Total 18.
- $\ce{[Fe(CO)4]^2-}$: iron is group 8; Fe(-II) is $d^{10}$, contributing 10. Four
  carbonyls contribute 8. Total 18.
- $\ce{[Co(C5H5)2]+}$: cobalt is group 9; Co(III) is $d^6$, contributing 6. Two
  cyclopentadienyl anions contribute 12. Total 18.
- $\ce{[Ni(C5H5)2]}$: nickel is group 10; Ni(II) is $d^8$, contributing 8. Two
  cyclopentadienyl anions contribute 12. Total 20.

Nickelocene is the violator. The two electrons in excess of 18 must occupy
metal–ligand antibonding orbitals, which lengthens the Ni–C bonds and lowers the
barrier to oxidation. Nickelocene is therefore readily oxidised to the 18-electron
cation and is less thermally stable than ferrocene.

**Answer.** 18, 18, 18 and 20 respectively; nickelocene violates the rule.

**Check.** The isoelectronic relationship is instructive: $\ce{[Co(C5H5)2]+}$ (18 e) and
$\ce{[Ni(C5H5)2]}$ (20 e) differ by one electron, and the extra electron is exactly the
one that occupies the antibonding orbital.

**Where marks are lost.** Counting a cyclopentadienyl ligand as 5 electrons, which
would give nickelocene 18 and hide the violation.

### 28. The carbonyl stretching trend **multi-step**

**Strategy.** Treat $\tilde{\nu}(\ce{CO})$ as a probe of metal electron density, and
explain the density by the charge on the complex.

**Working.** Carbon monoxide binds by σ donation from its carbon lone pair into an empty
metal orbital and by π back-donation from a filled metal $d$ orbital into its $\pi^*$
orbital. The two effects are synergic.

Back-donation populates the $\pi^*$ orbital, which lowers the C–O bond order and
therefore lowers $\tilde{\nu}$. All four complexes are 18-electron species and, in the
ionic convention, all four metal centres are $d^6$: titanium(-II), vanadium(-I),
chromium(0) and manganese(I) each retain six $d$ electrons after the ligands are
removed. What differs is the formal charge on the metal, which falls from $+1$ at
manganese to $-2$ at titanium. The more negative the metal, the more electron-rich it
is and the more it donates into the $\ce{CO}$ $\pi^*$ orbital:

- $\ce{[Ti(CO)6]^2-}$: Ti(-II), $d^6$, the most electron-rich metal, the strongest
  back-donation, the lowest frequency (1748).
- $\ce{[V(CO)6]-}$: V(-I), $d^6$ — 1860.
- $\ce{Cr(CO)6}$: Cr(0), $d^6$ — 2000.
- $\ce{[Mn(CO)6]+}$: Mn(I), $d^6$, the least electron-rich metal, the weakest
  back-donation, the highest frequency (2090).

**Answer.** The frequency rises as the metal charge becomes more positive, because the
metal becomes less able to donate into the $\ce{CO}$ $\pi^*$ orbital.

**Check.** The trend extends to the free ligand (2143), which has no back-donation at
all, and to bridging carbonyls (1700–1860), which accept electron density from two
metals and therefore have the lowest frequencies of all.

**Where marks are lost.** Explaining the trend by σ donation alone, which would predict
the opposite order (a more positive metal is a better σ acceptor, which would raise
$\tilde{\nu}$ — but the dominant effect here is π back-donation).

### 29. Carbon monoxide toxicity and the distal histidine **multi-step**

**Strategy.** Compare binding affinities, then explain the discrimination and its
limit.

**Working.** Carbon monoxide binds to the iron(II) of haemoglobin with an affinity
roughly 200–250 times that of dioxygen. It forms carboxyhaemoglobin, which cannot carry
oxygen; more importantly, binding of CO to one subunit shifts the remaining subunits
into the high-affinity R state, so the oxygen dissociation curve becomes
hyperbolic and shifted far to the left. Oxygen is still bound in the lungs but is not
released in the tissues. The result is tissue hypoxia at a carboxyhaemoglobin level far
below the level that would matter if the only effect were the loss of one binding site.

The distal histidine (E7) sits on the far side of the haem pocket. Dioxygen binds in a
bent Fe–O–O geometry, and the terminal oxygen forms a hydrogen bond to the imidazole
nitrogen of the distal histidine. Carbon monoxide prefers a linear Fe–C–O geometry, and
in that geometry the carbon and oxygen clash sterically with the histidine. The
discrimination is therefore a combination of a hydrogen bond that stabilises the
$\ce{O2}$ complex and a steric penalty that destabilises the CO complex.

The discrimination is incomplete because the intrinsic Fe–CO bond is much stronger than
the Fe–$\ce{O2}$ bond. The protein can reduce the CO affinity by a factor of a few
hundred, which is enough to make oxygen transport possible in air, but not enough to
make the protein immune to CO at the concentrations produced by incomplete combustion.

**Answer.** CO binds about 200–250 times more strongly than $\ce{O2}$ and locks the
protein in the R state. The distal histidine hydrogen-bonds to bent $\ce{O2}$ and
sterically disfavours linear Fe–CO, which gives a modest discrimination that is
overcome by the intrinsic strength of the Fe–CO bond.

**Check.** The model explains why myoglobin mutants lacking the distal histidine show
much lower $\ce{O2}$/CO discrimination, which is observed experimentally.

**Where marks are lost.** Saying only "CO binds irreversibly" — the binding is
reversible, just much stronger — or ignoring the allosteric shift.

### 30. Oxygen-carrying capacity of blood **multi-step**

**Strategy.** Multiply the haemoglobin concentration by its oxygen capacity, then
convert volume to amount.

**Working.** The oxygen bound per cubic decimetre at full saturation is

$$150\ \text{g dm}^{-3} \times 1.34\ \text{cm}^{3}\ \text{g}^{-1}
= 201\ \text{cm}^{3}\ \text{dm}^{-3}$$

At SATP the molar volume is $24.79\ \text{dm}^{3}\ \text{mol}^{-1}$, so

$$n(\ce{O2}) = \frac{0.201\ \text{dm}^{3}}{24.79\ \text{dm}^{3}\ \text{mol}^{-1}}
= 8.11\times10^{-3}\ \text{mol} = 8.11\ \text{mmol}$$

**Answer.** $201\ \text{cm}^{3}$ of $\ce{O2}$ per $\text{dm}^{3}$ of blood, equivalent to
$8.11\ \text{mmol}$.

**Check.** The result corresponds to about $8.1\ \text{mmol}$ of $\ce{O2}$ per litre,
which is close to the amount dissolved in plasma (about $0.15\ \text{mmol}$) multiplied
by a factor of about 50 — the reason haemoglobin is essential for oxygen transport.

**Where marks are lost.** Using the molar volume at STP ($22.71\ \text{dm}^{3}\ \text{mol}^{-1}$)
when the question specifies SATP, or forgetting that 1.34 is per gram of haemoglobin
and not per decilitre.

### 31. Density of copper **multi-step**

**Strategy.** Count the atoms in the fcc cell, compute the cell volume and apply
$\rho = ZM/(N_{\text{A}}a^3)$.

**Working.** An fcc cell contains $8(1/8) + 6(1/2) = 4$ atoms, so $Z = 4$. The cell
edge is $a = 361.5\ \text{pm} = 3.615\times10^{-8}\ \text{cm}$, so

$$V = a^3 = (3.615\times10^{-8})^3 = 4.724\times10^{-23}\ \text{cm}^{3}$$

The mass of one cell is

$$m = \frac{ZM}{N_{\text{A}}} = \frac{4 \times 63.55}{6.022\times10^{23}}
= 4.221\times10^{-22}\ \text{g}$$

Therefore

$$\rho = \frac{4.221\times10^{-22}}{4.724\times10^{-23}} = 8.94\ \text{g cm}^{-3}$$

**Answer.** $8.94\ \text{g cm}^{-3}$, against an experimental value of
$8.96\ \text{g cm}^{-3}$ (0.2 % difference).

**Check.** The agreement confirms both the fcc assignment and $Z = 4$. A body-centred
cell ($Z = 2$) would give half the density, and a simple cubic cell ($Z = 1$) a quarter.

**Where marks are lost.** Using $Z = 1$ for fcc, or forgetting to convert picometres
to centimetres before cubing.

### 32. Bragg angle for the (111) reflection **multi-step**

**Strategy.** Compute $d_{hkl}$ from the cubic relation, then apply Bragg's law.

**Working.** For a cubic lattice,

$$d_{hkl} = \frac{a}{\sqrt{h^2+k^2+l^2}} = \frac{361.5}{\sqrt{3}} = 208.7\ \text{pm}$$

Bragg's law gives

$$\sin\theta = \frac{\lambda}{2d} = \frac{154.06}{2 \times 208.7} = 0.3691$$

$$\theta = 21.66^\circ, \qquad 2\theta = 43.3^\circ$$

**Answer.** $d_{111} = 208.7\ \text{pm}$ and $2\theta = 43.31^\circ$.

**Check.** The value is the first reflection of copper in a standard powder pattern,
and the observed $2\theta$ for the (111) reflection of Cu with Cu $K\alpha$ radiation is
about $43.3^\circ$.

**Where marks are lost.** Using $d = a\sqrt{3}$ instead of $a/\sqrt{3}$, or reporting
$\theta$ instead of $2\theta$.

### 33. Moment to configuration **multi-step**

**Strategy.** Invert $\mu = \sqrt{n(n+2)}$ and then identify configurations that give
that $n$.

**Working.** Squaring the moment gives $n(n+2) = 4.90^2 = 24.0$. Solving
$n^2 + 2n - 24 = 0$ gives $n = 4$ (the negative root is unphysical).

Four unpaired electrons correspond to several octahedral configurations:

- high-spin $d^4$ ($t_{2g}^3e_g^1$), as in $\ce{Cr^2+}$ or $\ce{Mn^3+}$;
- high-spin $d^6$ ($t_{2g}^4e_g^2$), as in $\ce{Fe^2+}$;
- tetrahedral $d^4$ or high-spin tetrahedral $d^6$, which have the same counts with
  the orbital labels reversed.

A measured moment can differ from the spin-only value because the spin-only formula
assumes that the orbital angular momentum is completely quenched. In octahedral
complexes with $T_{1g}$ or $T_{2g}$ ground terms (for example high-spin $\ce{Co^2+}$,
$d^7$), spin–orbit coupling mixes excited states into the ground state and the moment
is larger than spin-only. Antiferromagnetic coupling between centres, or a small
temperature-independent paramagnetism, can also shift the value.

**Answer.** $n = 4$; possible configurations are high-spin $d^4$ or high-spin $d^6$.
Orbital contribution and spin–orbit coupling explain deviations from the spin-only
value.

**Check.** The observed moment of $\ce{[Fe(H2O)6]^2+}$ is about $5.3\ \mu_{\text{B}}$
against a spin-only $4.90$, and that of high-spin $\ce{[Co(H2O)6]^2+}$ is about
$4.9$–$5.0$ against a spin-only $3.87$; both deviations are in the direction predicted
by an orbital contribution.

**Where marks are lost.** Reporting $n = 4.90$, or assuming that the spin-only formula
is exact.

### 34. Curie–Weiss analysis **multi-step**

**Strategy.** Linearise $1/\chi$ against $T$, extract slope and intercept, then convert.

**Working.** The Curie–Weiss law is

$$\frac{1}{\chi_{\text{m}}} = \frac{T - \theta}{C}$$

At 200 K, $1/\chi = 1/(2.50\times10^{-2}) = 40.0\ \text{mol cm}^{-3}$. At 300 K,
$1/\chi = 100\ \text{mol cm}^{-3}$.

The slope is

$$\frac{1}{C} = \frac{100 - 40.0}{300 - 200} = 0.600\ \text{cm}^{-3}\ \text{K}^{-1}\ \text{mol}$$

so $C = 1.667\ \text{cm}^{3}\ \text{K mol}^{-1}$.

Using the 300 K point:

$$100 = \frac{300 - \theta}{1.667} \quad\Longrightarrow\quad 300 - \theta = 166.7
\quad\Longrightarrow\quad \theta = +133\ \text{K}$$

The effective moment is

$$\mu_{\text{eff}} = 2.828\sqrt{C} = 2.828\sqrt{1.667} = 3.65\ \mu_{\text{B}}$$

A positive $\theta$ indicates ferromagnetic coupling (or, in a paramagnet with no
ordering, a ferromagnetic contribution to the exchange).

**Answer.** $C = 1.67\ \text{cm}^{3}\ \text{K mol}^{-1}$; $\theta = +133\ \text{K}$;
$\mu_{\text{eff}} = 3.65\ \mu_{\text{B}}$; ferromagnetic coupling dominates.

**Check.** A moment of $3.65\ \mu_{\text{B}}$ corresponds to about three unpaired
electrons ($\sqrt{15} = 3.87$) or a $d^2$/$d^7$ ion with an orbital contribution. The
sign of $\theta$ is consistent with the positive deviation from the Curie law.

**Where marks are lost.** Using $\chi$ rather than $1/\chi$ for the slope, which gives
a meaningless intercept.

### 35. Labile and inert complexes **multi-step**

**Strategy.** Use the $d$-electron configuration, not the charge or the formation
constant.

**Working.** Lability is kinetic: a complex is labile if substitution is complete within
about a minute at 25 °C. The pattern is that $d^0$, $d^1$, $d^2$, high-spin $d^5$ and
$d^{10}$ ions are labile, while $d^3$ and low-spin $d^6$ are inert.

- $\ce{[Co(NH3)6]^3+}$: cobalt(III) low-spin $d^6$ ($t_{2g}^6$). The $t_{2g}$ shell is
  filled and the $e_g$ orbitals are empty, so there is no low-energy pathway for
  forming a seven-coordinate intermediate, and ligand-field activation is large.
  **Inert.**
- $\ce{[Cr(H2O)6]^3+}$: chromium(III) $d^3$ ($t_{2g}^3$). The half-filled $t_{2g}$ set
  gives a large ligand-field activation energy and no accessible $e_g$ electron.
  **Inert.**
- $\ce{[Ni(H2O)6]^2+}$: nickel(II) $d^8$ ($t_{2g}^6e_g^2$). The two $e_g$ electrons
  occupy antibonding orbitals, which weakens the metal–ligand bonds and lowers the
  barrier to substitution. **Labile.**
- $\ce{[Cu(NH3)4]^2+}$: copper(II) $d^9$. One $e_g$ electron (or hole) plus a strong
  Jahn–Teller distortion gives a weakly bound axial ligand that exchanges rapidly.
  **Labile.**

**Answer.** Inert: $\ce{[Co(NH3)6]^3+}$ and $\ce{[Cr(H2O)6]^3+}$. Labile:
$\ce{[Ni(H2O)6]^2+}$ and $\ce{[Cu(NH3)4]^2+}$.

**Check.** The classification explains why cobalt(III) ammine chemistry is
stereochemically stable (the complexes can be resolved) while nickel(II) complexes
equilibrate instantly.

**Where marks are lost.** Confusing lability with thermodynamic stability: a complex
can be very stable and still labile, or moderately stable and inert.

### 36. Free-ion moment of gadolinium(III) **multi-step**

**Strategy.** Identify the ground term, then apply the Landé formula and show the
cancellation.

**Working.** $\ce{Gd^3+}$ is $4f^7$. A half-filled $f$ shell with seven parallel spins
has $S = 7/2$ and, because the seven electrons occupy seven different orbitals with
$m_l = -3$ to $+3$, $L = 0$. The ground term is $^8S_{7/2}$, so $J = S = 7/2$.

The Landé $g$ factor is

$$g_J = 1 + \frac{J(J+1) + S(S+1) - L(L+1)}{2J(J+1)} = 1 + \frac{63/4 + 63/4 - 0}{2(63/4)} = 2$$

Therefore

$$\mu_{\text{eff}} = g_J\sqrt{J(J+1)} = 2\sqrt{\frac{7}{2}\cdot\frac{9}{2}}
= 2\sqrt{15.75} = 7.94\ \mu_{\text{B}}$$

The spin-only formula with $n = 7$ gives $\sqrt{7 \times 9} = 7.94\ \mu_{\text{B}}$,
identical because $L = 0$ makes the orbital contribution vanish.

**Answer.** $7.94\ \mu_{\text{B}}$, equal to the spin-only value for seven unpaired
electrons.

**Check.** Gadolinium(III) is the one lanthanide for which the spin-only formula works
exactly, which is why it is used as a calibration standard for magnetic susceptibility.
Its long electron spin-relaxation time is also why gadolinium chelates are MRI contrast
agents.

**Where marks are lost.** Applying the spin-only formula to a lanthanide with $L \neq 0$
and expecting agreement; for example $\ce{Dy^3+}$ has a free-ion moment of
$10.65\ \mu_{\text{B}}$ against a spin-only value of $10.63$ — close, but for the wrong
reason.

---

## Part D — Advanced problems

### 37. Born–Haber cycle for sodium chloride **multi-step**

**Strategy.** Write the cycle, sum the terms, and solve for the lattice enthalpy.

**Working.** The formation reaction is
$\ce{Na(s) + 1/2 Cl2(g) -> NaCl(s)}$ with
$\Delta H^{\circ}_{\text{f}} = -411\ \text{kJ mol}^{-1}$. The cycle is

$$\ce{Na(s) ->[{\Delta H_{\text{sub}} = +107}] Na(g) ->[{I_1 = +496}] Na+(g)}$$

$$\ce{1/2 Cl2(g) ->[{1/2 D = +122}] Cl(g) ->[{\Delta_{\text{ea}}H = -349}] Cl-(g)}$$

$$\ce{Na+(g) + Cl-(g) ->[{\Delta H_{\text{latt}}}] NaCl(s)}$$

By Hess's law,

$$\Delta H^{\circ}_{\text{f}} = \Delta H_{\text{sub}} + I_1 + \tfrac12 D
+ \Delta_{\text{ea}}H + \Delta H_{\text{latt}}$$

so

$$\Delta H_{\text{latt}} = -411 - (107 + 496 + 122 - 349) = -411 - 376
= -787\ \text{kJ mol}^{-1}$$

**Answer.** $\Delta H_{\text{latt}} = -787\ \text{kJ mol}^{-1}$ (formation direction).

**Check.** The value is close to the literature lattice enthalpy of about
$-787\ \text{kJ mol}^{-1}$ (or $+787$ for dissociation), and it lies between the values
for KBr and MgO as the ionic radii and charges require.

**Where marks are lost.** Using the second electron affinity of chlorine as negative
(it is positive, because adding an electron to an already negative ion costs energy),
or forgetting the $\tfrac12$ in the chlorine dissociation.

### 38. Stability of manganese dioxide **multi-step**

**Strategy.** Write the disproportionation as two half-reactions and combine the
potentials in the correct order.

**Working.** The disproportionation is

$$\ce{2MnO2(s) + 4H+(aq) -> MnO4-(aq) + Mn^2+(aq) + 2H2O(l)}$$

This is the sum of the oxidation $\ce{MnO2 -> MnO4- + 3e-}$ (reverse of the
$\ce{MnO4-/MnO2}$ couple) and the reduction $\ce{MnO2 + 2e- -> Mn^2+}$ (the
$\ce{MnO2/Mn^2+}$ couple). Two MnO2 units supply the three and two electrons:

$$E^\circ_{\text{cell}} = 1.23 - 1.68 = -0.45\ \text{V}$$

A negative cell potential means a positive Gibbs energy:

$$\Delta G^\circ = -nFE^\circ = -2(96\,485)(-0.45) = +86.8\ \text{kJ mol}^{-1}$$

The reaction is therefore not spontaneous and $\ce{MnO2}$ is stable with respect to
disproportionation in acid.

The overall $\ce{MnO4-/Mn^2+}$ potential is the weighted average of the two steps:

$$E^\circ = \frac{3(1.68) + 2(1.23)}{5} = \frac{5.04 + 2.46}{5} = 1.50\ \text{V}$$

**Answer.** $\ce{MnO2}$ is stable ($E^\circ = -0.45\ \text{V}$,
$\Delta G^\circ = +86.8\ \text{kJ mol}^{-1}$); $E^\circ(\ce{MnO4-/Mn^2+}) = +1.50\ \text{V}$.

**Check.** The Latimer rule agrees: the potential to the right of $\ce{MnO2}$ (1.23) is
less than the potential to its left (1.68), so $\ce{MnO2}$ does not disproportionate;
it is the stable intermediate.

**Where marks are lost.** Averaging the two potentials without weighting by the number
of electrons, which gives 1.455 V instead of 1.50 V.

### 39. CFSE and Jahn–Teller distortion **multi-step**

**Strategy.** Assign the configurations, compute the CFSE, count unpaired electrons, and
test for a degenerate ground state.

**Working.** $\ce{[Cu(H2O)6]^2+}$: copper(II) is $d^9$, configuration $t_{2g}^6e_g^3$,
with one unpaired electron. The CFSE is

$$\text{CFSE} = \left[-0.4(6) + 0.6(3)\right]\Delta_o = (-2.4 + 1.8)\Delta_o
= -0.6\Delta_o$$

The moment is $\sqrt{3} = 1.73\ \mu_{\text{B}}$. The $e_g$ set is unequally occupied
(two electrons in one orbital, one in the other), so the ground state is degenerate and
the complex distorts strongly — a tetragonal elongation along $z$, with the two axial
ligands much further away than the four equatorial ones. This is the classic
Jahn–Teller case.

$\ce{[Cr(H2O)6]^3+}$: chromium(III) is $d^3$, configuration $t_{2g}^3$, with three
unpaired electrons. The CFSE is

$$\text{CFSE} = -0.4(3)\Delta_o = -1.2\Delta_o$$

The moment is $\sqrt{15} = 3.87\ \mu_{\text{B}}$. The $t_{2g}$ set is half-filled and
the $e_g$ set is empty; the ground state is non-degenerate ($^4A_{2g}$), so there is no
first-order Jahn–Teller distortion.

**Answer.** $\ce{[Cu(H2O)6]^2+}$: $d^9$, $t_{2g}^6e_g^3$, CFSE $= -0.6\Delta_o$,
$n = 1$, $\mu = 1.73\ \mu_{\text{B}}$, strong Jahn–Teller elongation.
$\ce{[Cr(H2O)6]^3+}$: $d^3$, $t_{2g}^3$, CFSE $= -1.2\Delta_o$, $n = 3$,
$\mu = 3.87\ \mu_{\text{B}}$, no Jahn–Teller distortion.

**Check.** The CFSE of the $d^3$ ion is twice that of the $d^9$ ion because the $d^9$
configuration has three electrons in the destabilising $e_g$ set, which cancels most of
the $t_{2g}$ stabilisation.

**Where marks are lost.** Forgetting the $+0.6$ contribution of the $e_g$ electrons,
which makes the $d^9$ CFSE wrongly $-2.4\Delta_o$.

### 40. Electron counting through a hydroformylation cycle **multi-step**

**Strategy.** Count at every stage with the neutral-ligand convention, and check that
each step changes the count by the number of electrons added or removed.

**Working.** The resting state is $\ce{HCo(CO)4}$. In the ionic convention the hydride
is $\ce{H-}$ (a 2-electron donor), the four carbonyls are neutral 2-electron donors, and
cobalt is Co(I), $d^8$. The count is $8 + 2 + 8 = 18$.

The cycle, written with the ionic convention throughout:

| Stage | Species | Metal | Count |
|---|---|---|---|
| Resting state | $\ce{HCo(CO)4}$ | Co(I) $d^8$ | $8 + 2 + 8 = 18$ |
| CO dissociation | $\ce{HCo(CO)3}$ | Co(I) $d^8$ | $8 + 2 + 6 = 16$ |
| Alkene coordination | $\ce{HCo(CO)3(alkene)}$ | Co(I) $d^8$ | $8 + 2 + 6 + 2 = 18$ |
| Migratory insertion | $\ce{Co(CO)3(alkyl)}$ | Co(I) $d^8$ | $8 + 6 + 2 = 16$ |
| CO coordination | $\ce{Co(CO)4(alkyl)}$ | Co(I) $d^8$ | $8 + 8 + 2 = 18$ |
| CO insertion | $\ce{Co(CO)4(acyl)}$ | Co(I) $d^8$ | $8 + 8 + 2 = 18$ |
| CO dissociation | $\ce{Co(CO)3(acyl)}$ | Co(I) $d^8$ | $8 + 6 + 2 = 16$ |
| Oxidative addition of $\ce{H2}$ | $\ce{H2Co(CO)3(acyl)}$ | Co(III) $d^6$ | $6 + 4 + 6 + 2 = 18$ |
| Reductive elimination | $\ce{HCo(CO)3}$ + aldehyde | Co(I) $d^8$ | $8 + 2 + 6 = 16$ |
| CO coordination | $\ce{HCo(CO)4}$ | Co(I) $d^8$ | $8 + 2 + 8 = 18$ |

The carbon monoxide insertion step leaves the count unchanged because the alkyl ligand
and a carbonyl combine to give an acyl ligand: one 2-electron donor replaces another.
The oxidative addition of $\ce{H2}$ adds two hydride ligands and raises the oxidation
state from Co(I) to Co(III), which removes two $d$ electrons and adds four electrons
from the two hydrides, so the total rises by two to 18. Reductive elimination reverses
both changes at once.

The reason CO must dissociate before the alkene binds is that the resting state is
already 18-electron and coordinatively saturated. An incoming alkene would have to enter
an antibonding orbital, which is energetically prohibitive. Dissociation of CO opens a
coordination site and gives a 16-electron, coordinatively unsaturated species that can
accept the alkene in a bonding orbital.

**Answer.** Counts: 18 → 16 → 18 → 16 → 18 → 18 → 16 → 18 → 16 → 18, with cobalt
remaining Co(I) until the oxidative addition, when it becomes Co(III) ($d^6$). CO
dissociation is required to create a vacant site on an 18-electron complex.

**Check.** Every step satisfies the 18-electron rule or is a deliberate 16-electron
intermediate; the oxidation state changes only at the oxidative addition and the
reductive elimination, which is the signature of a cycle that conserves electrons
overall.

**Where marks are lost.** Changing the oxidation state at the migratory insertion
(it does not change: the alkyl and the hydride are both anionic in the ionic
convention), or forgetting that the acyl ligand is a 2-electron donor.

### 41. Haemoglobin saturation at two oxygen pressures **multi-step**

**Strategy.** Apply the Hill equation at each pressure and compare.

**Working.** The Hill equation is

$$Y = \frac{p^n}{p_{50}^n + p^n}$$

with $p_{50} = 26\ \text{mmHg}$ and $n = 2.8$.

At $p\ce{O2} = 40\ \text{mmHg}$:

$$\left(\frac{40}{26}\right)^{2.8} = (1.538)^{2.8} = 3.34$$

$$Y = \frac{3.34}{1 + 3.34} = 0.770$$

At $p\ce{O2} = 100\ \text{mmHg}$:

$$\left(\frac{100}{26}\right)^{2.8} = (3.846)^{2.8} = 43.4$$

$$Y = \frac{43.4}{1 + 43.4} = 0.978$$

**Answer.** 77 % saturation at 40 mmHg and 98 % at 100 mmHg.

**Check.** The difference of 21 percentage points is what makes haemoglobin an effective
transporter: it loads almost fully in the lungs and unloads a substantial fraction in
the tissues. Myoglobin, with a hyperbolic curve and a much lower $p_{50}$, would be
about 95 % saturated at 40 mmHg and would not release oxygen.

**Where marks are lost.** Using $n = 1$ (the simple Langmuir isotherm), which gives
61 % and 79 % and destroys the physiological point of the calculation.

### 42. Indexing a cubic powder pattern **multi-step**

**Strategy.** Compute $d$ from Bragg's law for each reflection, then find the integers
$h^2+k^2+l^2$ that make $a$ constant.

**Working.** For a cubic lattice, $\sin^2\theta \propto (h^2+k^2+l^2)$. Using
$\lambda = 154.06\ \text{pm}$:

| $2\theta$ | $\theta$ | $\sin\theta$ | $d = \lambda/(2\sin\theta)$ / pm | $h^2+k^2+l^2$ | $a = d\sqrt{N}$ / pm |
|---|---|---|---|---|---|
| 43.31 | 21.66 | 0.3691 | 208.7 | 3 | 361.5 |
| 50.46 | 25.23 | 0.4263 | 180.7 | 4 | 361.4 |
| 74.12 | 37.06 | 0.6027 | 127.8 | 8 | 361.5 |

The ratios of $\sin^2\theta$ are $3 : 4 : 8$, which is the signature of a
face-centred cubic lattice: the allowed reflections have $h$, $k$ and $l$ all even or
all odd, so $N = 3, 4, 8, 11, 12, \ldots$ and the forbidden values 1, 2, 5, 6, 7, 9, 10
are absent. A primitive cubic lattice would show $N = 1, 2, 3, 4, \ldots$ and a
body-centred cubic lattice $N = 2, 4, 6, 8, \ldots$

**Answer.** The reflections are (111), (200) and (220); $a = 361.5\ \text{pm}$; the
lattice is face-centred cubic.

**Check.** The value of $a$ agrees with the accepted lattice parameter of copper
(361.5 pm), and the indexing is self-consistent: all three reflections give the same
cell edge.

**Where marks are lost.** Assuming a primitive lattice and assigning $N = 1, 2, 3$,
which gives a cell edge that drifts from reflection to reflection.

### 43. Saturation magnetisation of magnetite **multi-step**

**Strategy.** Convert the moment per formula unit into a moment per unit volume.

**Working.** The number of formula units per cubic metre is

$$\frac{\rho N_{\text{A}}}{M} = \frac{5.17\times10^{6}\ \text{g m}^{-3}
\times 6.022\times10^{23}\ \text{mol}^{-1}}{231.5\ \text{g mol}^{-1}}
= 1.345\times10^{28}\ \text{m}^{-3}$$

The moment per formula unit is $4.0\ \mu_{\text{B}} = 4.0 \times 9.274\times10^{-24} = 3.710\times10^{-23}\ \text{A m}^{2}$. Therefore

$$M_{\text{s}} = 1.345\times10^{28} \times 3.710\times10^{-23}
= 4.99\times10^{5}\ \text{A m}^{-1}$$

**Answer.** $M_{\text{s}} = 4.99\times10^{5}\ \text{A m}^{-1}$ (experimental about
$4.8\times10^{5}\ \text{A m}^{-1}$). The net moment is 4 rather than 14 $\mu_{\text{B}}$
because the tetrahedral and octahedral sublattices are antiferromagnetically coupled,
so the net moment is the difference $|5 + 4 - 5| = 4\ \mu_{\text{B}}$, not the sum
$5 + 4 + 5 = 14\ \mu_{\text{B}}$.

**Why the difference and not the sum.** In the inverse spinel structure one third of
the iron is $\ce{Fe^3+}$ on tetrahedral sites and two thirds are
$\ce{Fe^3+}$/$\ce{Fe^2+}$ on octahedral sites. Per formula unit there are two octahedral
cations (one $\ce{Fe^3+}$, 5 $\mu_{\text{B}}$, and one $\ce{Fe^2+}$, 4 $\mu_{\text{B}}$)
and one tetrahedral $\ce{Fe^3+}$ (5 $\mu_{\text{B}}$). The tetrahedral moments are
antiparallel to the octahedral moments, so the net moment is $5 + 4 - 5 = 4\ \mu_{\text{B}}$. This is ferrimagnetism: two opposed sublattices of unequal moment.

**Check.** The calculation reproduces the experimental value to within about 4 %, which
is as good as the local-moment model allows. The same model explains why
$\ce{NiFe2O4}$ has a smaller net moment than magnetite: $\ce{Ni^2+}$ (2 $\mu_{\text{B}}$)
replaces $\ce{Fe^2+}$ (4 $\mu_{\text{B}}$) on the octahedral sites, so the net moment
falls from 4 to $5 + 2 - 5 = 2\ \mu_{\text{B}}$.

**Where marks are lost.** Adding all the moments (14 $\mu_{\text{B}}$), which describes
a ferromagnet, not a ferrimagnet.

### 44. Marcus barrier and the inverted region **multi-step**

**Strategy.** Apply the Marcus relation at three driving forces and identify the
turning point.

**Working.** The Marcus relation is

$$\Delta G^\ddagger = \frac{\lambda}{4}\left(1 + \frac{\Delta G^\circ}{\lambda}\right)^2$$

With $\lambda = 80\ \text{kJ mol}^{-1}$:

- $\Delta G^\circ = 0$: $\Delta G^\ddagger = 20(1)^2 = 20\ \text{kJ mol}^{-1}$.
- $\Delta G^\circ = -40$: $\Delta G^\ddagger = 20(1 - 0.5)^2 = 5\ \text{kJ mol}^{-1}$.
- $\Delta G^\circ = -160$: $\Delta G^\ddagger = 20(1 - 2)^2 = 20\ \text{kJ mol}^{-1}$.

The barrier falls to zero at $\Delta G^\circ = -\lambda = -80\ \text{kJ mol}^{-1}$ and
then rises again. The region beyond $-\lambda$ is the **Marcus inverted region**.

**Physical origin.** The reactants and products have different equilibrium geometries
and solvation shells. Before the electron can transfer, the nuclei must reorganise to a
configuration in which the two states are degenerate. The reorganisation costs
$\lambda$, and the driving force pays for it. When the driving force greatly exceeds
$\lambda$, the crossing point moves to the high-energy side of the product parabola, so
the barrier rises again: the reaction is so exergonic that the product is formed in a
vibrationally excited state, and the electron must climb out of that well.

**Answer.** 20, 5 and $20\ \text{kJ mol}^{-1}$; the third case is in the inverted
region.

**Check.** The parabola construction predicts the maximum rate at
$\Delta G^\circ = -\lambda$ and a symmetric fall-off on either side. The inverted region
was confirmed experimentally with excited-state electron donors, and its observation was
a decisive test of the theory.

**Where marks are lost.** Assuming that a more negative $\Delta G^\circ$ always gives a
faster reaction; the whole point of the inverted region is that it does not.

### 45. Specific activity of uranium-238 **multi-step**

**Strategy.** Convert the half-life to seconds, then use $A = \lambda N$.

**Working.** The decay constant is

$$\lambda = \frac{\ln 2}{t_{1/2}} = \frac{0.6931}{4.468\times10^{9} \times 3.156\times10^{7}\ \text{s}}
= \frac{0.6931}{1.410\times10^{17}\ \text{s}} = 4.916\times10^{-18}\ \text{s}^{-1}$$

One gram of $\ce{^{238}U}$ contains $1/238.05 = 4.201\times10^{-3}\ \text{mol}$, that
is $4.201\times10^{-3} \times 6.022\times10^{23} = 2.530\times10^{21}$ atoms.

$$A = \lambda N = 4.916\times10^{-18} \times 2.530\times10^{21}
= 1.24\times10^{4}\ \text{Bq}$$

**Answer.** $1.24\times10^{4}\ \text{Bq g}^{-1}$, or $12.4\ \text{kBq g}^{-1}$.

The mass required for $1.00\ \text{GBq}$ is

$$m = \frac{1.00\times10^{9}}{1.24\times10^{4}} = 8.04\times10^{4}\ \text{g}
= 80.4\ \text{kg}$$

**Check.** The value is the standard specific activity of natural uranium metal
(about $12.4\ \text{kBq g}^{-1}$), and the mass for 1 GBq — about 80 kg — is consistent
with the low specific activity of a nuclide with a $4.5\times10^{9}$-year half-life.

**Where marks are lost.** Forgetting to convert years to seconds, which gives an answer
wrong by a factor of $3.2\times10^{7}$.

### 46. Identification of an unknown white solid **multi-step**

**Strategy.** Use each observation to eliminate classes of cation, then confirm with a
specific test.

**Working.** The absence of a flame colour rules out the alkali and alkaline-earth
cations that give strong flames (Na, K, Ca, Sr, Ba, Cu). Effervescence with dilute acid
indicates a carbonate or hydrogencarbonate, so the solid is a carbonate of a cation that
does not colour the flame.

The solution gives a white precipitate with aqueous ammonia that dissolves in excess.
That is the behaviour of zinc(II): $\ce{Zn^2+ + 2OH^- -> Zn(OH)2 v}$, and
$\ce{Zn(OH)2 + 4NH3 -> [Zn(NH3)4]^2+ + 2OH^-}$. Aluminium(III) also gives a white
hydroxide with ammonia, but it does *not* dissolve in excess ammonia, only in excess
hydroxide. The ammonia test therefore distinguishes zinc from aluminium.

With sodium hydroxide the solution gives a white precipitate that dissolves in excess:
$\ce{Zn(OH)2}$ is amphoteric, $\ce{Zn(OH)2 + 2OH^- -> [Zn(OH)4]^2-}$. Adding solid
ammonium chloride to that solution reprecipitates the hydroxide, because ammonium
chloride buffers the solution to a pH at which the zincate ion is no longer stable and
the equilibrium shifts back towards the insoluble hydroxide.

**Answer.** Y is zinc carbonate, $\ce{ZnCO3}$.

Equations:

$$\ce{ZnCO3(s) + 2HCl(aq) -> ZnCl2(aq) + CO2(g) + H2O(l)}$$

$$\ce{Zn^2+(aq) + 2OH^-(aq) -> Zn(OH)2(s)}$$

$$\ce{Zn(OH)2(s) + 4NH3(aq) -> [Zn(NH3)4]^2+(aq) + 2OH^-(aq)}$$

$$\ce{Zn(OH)2(s) + 2OH^-(aq) -> [Zn(OH)4]^2-(aq)}$$

$$\ce{[Zn(OH)4]^2-(aq) + 2NH4+(aq) -> Zn(OH)2(s) + 2NH3(aq) + 2H2O(l)}$$

**Check.** The ammonium chloride test is decisive: it distinguishes a zincate solution
from an aluminate solution, because aluminium hydroxide is not reprecipitated by
ammonium chloride under the same conditions (the aluminium species is more stable as the
hydroxide at that pH). The absence of a flame colour is consistent with zinc.

**Where marks are lost.** Identifying the solid as aluminium carbonate, which is
inconsistent with the solubility of the hydroxide in excess ammonia.

---

## Part E — Mechanism and diagram problems

### 47. $S_N1$CB base hydrolysis of $\ce{[Co(NH3)5Cl]^2+}$

**Strategy.** Recognise the conjugate-base mechanism: deprotonation first, then
rate-determining dissociation, then fast capture.

**Working.**

**Step 1 — conjugate-base formation (fast equilibrium).** Hydroxide removes a proton
from one coordinated ammonia. Electron movement: a hydroxide lone pair forms the
$\ce{O-H}$ bond, and the $\ce{N-H}$ σ pair becomes the nitrogen lone pair.

$$\ce{[Co(NH3)5Cl]^2+ + OH^- <=> [Co(NH2)(NH3)4Cl]+ + H2O}$$

Intermediate: the **amido** complex, in which one ligand is $\ce{NH2-}$ rather than
$\ce{NH3}$. The amide is a strong σ donor and has a large trans effect.

**Step 2 — rate-determining dissociation.** The $\ce{Co-Cl}$ bond breaks. Electron
movement: the $\ce{Co-Cl}$ σ pair goes to chlorine, which leaves as $\ce{Cl-}$. The
amido ligand labilises the position trans to itself, so the chloride that departs is
the one opposite the amide.

$$\ce{[Co(NH2)(NH3)4Cl]+ -> [Co(NH2)(NH3)4]^2+ + Cl^-}$$

Intermediate: a five-coordinate, 16-electron cobalt(III) species
($d^6$, square pyramidal or trigonal bipyramidal).

**Step 3 — fast capture.** Water or hydroxide donates a lone pair to the vacant site.
Electron movement: an oxygen lone pair forms the $\ce{Co-O}$ bond.

$$\ce{[Co(NH2)(NH3)4]^2+ + H2O -> [Co(NH2)(NH3)4(H2O)]^2+}$$

**Step 4 — reprotonation.** The amido ligand is protonated by water, restoring the
ammine and regenerating hydroxide.

$$\ce{[Co(NH2)(NH3)4(H2O)]^2+ + H2O -> [Co(NH3)5(H2O)]^3+ + OH^-}$$

The overall reaction is therefore
$\ce{[Co(NH3)5Cl]^2+ + H2O -> [Co(NH3)5(H2O)]^3+ + Cl-}$, with hydroxide acting as a
catalyst.

**Rate law.** The rate-determining step is unimolecular in the amido complex, and the
amido complex is in equilibrium with the starting complex and hydroxide:

$$\text{rate} = k[\ce{[Co(NH2)(NH3)4Cl]+}] = kK[\ce{[Co(NH3)5Cl]^2+}][\ce{OH^-}]$$

so the observed rate law is second order overall, first order in complex and first order
in hydroxide.

**Stereochemistry.** The metal centre retains its configuration throughout. The amido
ligand stays in place during the rate-determining step, and the entering water molecule
occupies the coordination site vacated by chloride. The five-coordinate intermediate is
short-lived and is captured before any rearrangement of the remaining ligands, so a
resolved cobalt(III) complex undergoes base hydrolysis with retention at cobalt rather
than with inversion. This is in direct contrast to $S_N2$ at a saturated carbon, where
the nucleophile attacks from the back face and inverts the centre.

**Answer.** As above; rate $= k_{\text{obs}}[\text{complex}][\ce{OH^-}]$.

**Check.** The mechanism accounts for the observed second-order kinetics, the positive
activation entropy (charge is dispersed in the transition state), the kinetic isotope
effect when N–H is replaced by N–D, and the absence of base catalysis for complexes
that have no amine protons.

**Where marks are lost.** Writing an associative mechanism (hydroxide attacking the
metal directly), which would not explain the isotope effect or the magnitude of the
rate enhancement.

### 48. Inner-sphere electron transfer

**Strategy.** Build the bridged intermediate, transfer the electron through the bridge,
then separate the products with the lability inversion.

**Working.**

**Step 1 — bridge formation.** $\ce{[Cr(H2O)6]^2+}$ is labile, so it loses a water
molecule and the chloride of $\ce{[Co(NH3)5Cl]^2+}$ binds to chromium, forming a
chloride bridge:

$$\ce{[Co(NH3)5Cl]^2+ + [Cr(H2O)6]^2+ -> [Co(NH3)5(\mu-Cl)Cr(H2O)5]^4+ + H2O}$$

Electron movement: a lone pair on chloride forms the $\ce{Cr-Cl}$ bond; the
$\ce{Cr-OH2}$ bond pair returns to the departing water molecule.

**Step 2 — electron transfer through the bridge.** An electron moves from chromium(II)
to cobalt(III) through the chloride bridge. Electron movement: a chromium $d$ electron
delocalises onto the bridging chloride and then onto cobalt. The bridged species is
unchanged in composition, but the oxidation states have swapped: cobalt is now
cobalt(II) and chromium is now chromium(III).

**Step 3 — separation.** Cobalt(II) is labile, so it loses its ammine ligands;
chromium(III) is inert, so it retains the chloride that was the bridge.

$$\ce{[Co(NH3)5(\mu-Cl)Cr(H2O)5]^4+ + 5H2O -> [Co(H2O)6]^2+ + [Cr(H2O)5Cl]^2+ + 5NH3}$$

The overall reaction is therefore

$$\ce{[Co(NH3)5Cl]^2+ + [Cr(H2O)6]^2+ + 5H2O -> [Co(H2O)6]^2+ + [Cr(H2O)5Cl]^2+ + 5NH3}$$

**The observation that established the mechanism.** Taube's 1953 experiment used
$\ce{^{36}Cl}$-labelled $\ce{[Co(NH3)5Cl]^2+}$. If the reaction were outer-sphere, the
labelled chloride would be released to solution as free $\ce{Cl-}$. Instead, the label
appeared in the chromium product, $\ce{[Cr(H2O)5Cl]^2+}$, which can only happen if the
chloride was transferred directly from cobalt to chromium — that is, through a bridge.

**Why the bridging ligand ends up on chromium.** The oxidant (cobalt(III)) is inert
before the reaction and becomes labile when reduced; the reductant (chromium(II)) is
labile before the reaction and becomes inert when oxidised. The lability inversion
traps the bridge on the chromium centre.

**Answer.** Bridge formation, electron transfer, separation; the isotopic label in the
chromium product is the diagnostic evidence.

**Check.** Charge: left $+2 + 2 = +4$; right $+2 + 2 = +4$. Atoms: Co 1 = 1, Cr 1 = 1,
Cl 1 = 1, N 5 = 5; hydrogen $15 + 12 + 10 = 37$ on the left and $12 + 10 + 15 = 37$ on
the right; oxygen $6 + 5 = 11$ on both sides. The equation is balanced, and no proton
is consumed because the reaction is written in neutral water.

**Where marks are lost.** Writing an outer-sphere mechanism, which cannot explain the
transfer of the label.

### 49. Trans-effect synthesis of the two isomers of $\ce{[PtCl2(NH3)2]}$

**Strategy.** At each step, identify which ligand is trans to the site that will be
substituted, and apply the trans-effect series.

**Working.**

**Cisplatin from $\ce{[PtCl4]^2-}$.**

*Step 1.* Ammonia attacks the square-planar platinum(II) complex. Electron movement: the
ammonia lone pair forms the $\ce{Pt-N}$ bond, and the $\ce{Pt-Cl}$ bond pair leaves with
chloride. The first ammonia can enter at any of the four equivalent positions.

$$\ce{[PtCl4]^2- + NH3 -> [PtCl3(NH3)]- + Cl^-}$$

*Step 2.* The complex now has one ammonia at position 1 and chlorides at positions 2, 3
and 4. The chloride at position 3 is *trans* to the ammonia and is only weakly
labilised, whereas the chlorides at positions 2 and 4 are each *trans* to another
chloride and are strongly labilised. Nucleophilic attack therefore occurs at position 2
or 4, and the second ammonia enters *cis* to the first.

$$\ce{[PtCl3(NH3)]- + NH3 -> cis-[PtCl2(NH3)2] + Cl^-}$$

**Transplatin from $\ce{[Pt(NH3)4]^2+}$.**

*Step 1.* Chloride attacks and displaces an ammonia. Electron movement: a chloride lone
pair forms the $\ce{Pt-Cl}$ bond, and the $\ce{Pt-N}$ bond pair leaves with ammonia.

$$\ce{[Pt(NH3)4]^2+ + Cl^- -> [PtCl(NH3)3]+ + NH3}$$

*Step 2.* Now the ligand *trans* to the new chloride is an ammonia, and that position is
labilised because chloride has the higher trans effect. The second chloride therefore
enters *trans* to the first.

$$\ce{[PtCl(NH3)3]+ + Cl^- -> trans-[PtCl2(NH3)2] + NH3}$$

**Answer.** The order of addition determines the isomer, because the trans effect
directs each incoming ligand opposite the ligand with the greater trans effect.

**Check.** The two routes use the same two ligands in the same stoichiometry and give
opposite isomers, which is the classic demonstration of kinetic control. The *cis*
isomer is the anticancer drug; the *trans* isomer is inactive because it cannot form the
required intrastrand cross-link with DNA.

**Where marks are lost.** Forgetting that it is the ligand *trans* to the *new* ligand
that is labilised in step 2, and reversing the two routes.

### 50. Catalytic cycle of carbonic anhydrase

**Strategy.** Follow the zinc coordination sphere through the cycle, identifying the
nucleophile at each stage.

**Working.** The resting enzyme has a tetrahedral zinc(II) centre coordinated by three
histidine nitrogens and one water molecule (or hydroxide, depending on pH).

**Step 1 — activation of water.** The zinc ion polarises the bound water, lowering its
$\mathrm{p}K_a$ from about 15.7 to about 7. A significant fraction of the enzyme is
therefore present as the zinc hydroxide at physiological pH. Electron movement: a water
lone pair coordinates to zinc; the zinc withdraws electron density, weakening the
$\ce{O-H}$ bond, and a buffer base removes the proton.

$$\ce{Zn-OH2^2+ <=> Zn-OH+ + H+}$$

**Step 2 — nucleophilic attack.** The zinc-bound hydroxide attacks the carbon of carbon
dioxide. Electron movement: a hydroxide lone pair forms the $\ce{C-O}$ bond, and the
$\ce{C=O}$ π pair moves onto the carbonyl oxygen, giving a bicarbonate intermediate
still coordinated to zinc.

$$\ce{Zn-OH+ + CO2 -> Zn-OCO2H+}$$

**Step 3 — product release.** A water molecule displaces the bicarbonate. Electron
movement: a water lone pair forms the $\ce{Zn-O}$ bond, and the $\ce{Zn-O}$ bond pair
returns to the bicarbonate oxygen, releasing $\ce{HCO3-}$.

$$\ce{Zn-OCO2H+ + H2O -> Zn-OH2^2+ + HCO3-}$$

**Step 4 — regeneration.** The bound water is deprotonated again (step 1), returning the
enzyme to the zinc hydroxide form and completing the cycle. A proton-transfer shuttle
(a histidine side chain and a buffer) removes the proton to the bulk solvent, which is
the rate-limiting step at high substrate concentration.

**The role of zinc in each stage.** Zinc is a Lewis acid that (i) lowers the
$\mathrm{p}K_a$ of bound water so that a hydroxide is available at neutral pH, (ii)
polarises the $\ce{C=O}$ bond of carbon dioxide, making the carbon more electrophilic,
and (iii) holds the bicarbonate in place long enough for it to be displaced by water
rather than diffusing away. In none of these steps does zinc change oxidation state:
it is a catalytic Lewis acid, not a redox centre.

**Answer.** The cycle is Zn–OH₂ → Zn–OH⁻ → Zn–OCO₂H⁻ → Zn–OH₂, with bicarbonate
released and water rebound.

**Check.** The catalytic constant is about $10^{6}\ \text{s}^{-1}$ per site, a rate
enhancement of about $10^{7}$ over the uncatalysed hydration, which is consistent with a
mechanism in which the only barrier is proton transfer.

**Where marks are lost.** Writing zinc as a redox centre, or omitting the regeneration
of the hydroxide nucleophile.

### 51. Born–Haber cycle for magnesium oxide

**Strategy.** Write every term with its sign, sum to the enthalpy of formation, and
solve for the lattice enthalpy.

**Working.** The formation reaction is
$\ce{Mg(s) + 1/2 O2(g) -> MgO(s)}$ with
$\Delta H^{\circ}_{\text{f}} = -602\ \text{kJ mol}^{-1}$.

The terms, in the order in which the cycle uses them, are:

| Step | Process | $\Delta H$ / kJ mol⁻¹ |
|---|---|---|
| Sublimation of Mg | $\ce{Mg(s) -> Mg(g)}$ | $+148$ |
| First ionisation | $\ce{Mg(g) -> Mg+(g) + e-}$ | $+738$ |
| Second ionisation | $\ce{Mg+(g) -> Mg^2+(g) + e-}$ | $+1451$ |
| Dissociation of $\ce{O2}$ | $\tfrac12\ce{O2(g) -> O(g)}$ | $+249$ |
| First electron affinity | $\ce{O(g) + e- -> O-(g)}$ | $-141$ |
| Second electron affinity | $\ce{O-(g) + e- -> O^2-(g)}$ | $+798$ |
| Lattice enthalpy | $\ce{Mg^2+(g) + O^2-(g) -> MgO(s)}$ | $x$ |

The sum of the endothermic terms is

$$148 + 738 + 1451 + 249 - 141 + 798 = 3243\ \text{kJ mol}^{-1}$$

so

$$-602 = 3243 + x \quad\Longrightarrow\quad x = -3845\ \text{kJ mol}^{-1}$$

**Answer.** $\Delta H_{\text{latt}} = -3845\ \text{kJ mol}^{-1}$.

**Diagram.** The energy-level diagram has the elements at zero on the left, rises
through sublimation and the two ionisation energies (total $+2337$), rises through
oxygen dissociation ($+249$), falls by the first electron affinity ($-141$), rises by
the second electron affinity ($+798$, because adding an electron to a negative ion
costs energy), and then falls steeply by the lattice enthalpy ($-3845$) to the product
at $-602$.

**Check.** The magnitude is about five times that of NaCl ($-787$), which is consistent
with the product of the charges ($2 \times 2 = 4$) and the smaller internuclear
distance. The second electron affinity is positive, as it must be for every element;
a negative value would make the oxide ion unstable in the gas phase.

**Where marks are lost.** Making the second electron affinity negative, which would make
the lattice enthalpy about $1596\ \text{kJ mol}^{-1}$ too small in magnitude.

### 52. Separation and identification of $\ce{Ag+}$, $\ce{Ba^2+}$ and $\ce{Cu^2+}$

**Strategy.** Use group reagents in order: chloride for silver, sulphide in acid for
copper, carbonate for barium.

**Working.**

**Stage 1 — add dilute hydrochloric acid.** Silver(I) precipitates as white silver
chloride; barium and copper remain in solution.

$$\ce{Ag+(aq) + Cl-(aq) -> AgCl(s)}$$

Filter. Confirm silver by dissolving the precipitate in aqueous ammonia
($\ce{AgCl + 2NH3 -> [Ag(NH3)2]+ + Cl-}$) and reprecipitating with nitric acid.

**Stage 2 — pass hydrogen sulphide through the acidic filtrate.** Copper(II)
precipitates as black copper(II) sulphide; barium remains in solution because barium
sulphide is soluble and, more importantly, because the low $[\ce{S^2-}]$ in acid is
insufficient to exceed the solubility product of BaS.

$$\ce{Cu^2+(aq) + H2S(aq) -> CuS(s) + 2H+(aq)}$$

Filter. Confirm copper by the deep blue colour with excess ammonia
($\ce{Cu^2+ + 4NH3 -> [Cu(NH3)4]^2+}$).

**Stage 3 — add ammonium carbonate to the filtrate.** Barium precipitates as white
barium carbonate.

$$\ce{Ba^2+(aq) + CO3^2-(aq) -> BaCO3(s)}$$

Confirm barium by a flame test (apple-green) and by the insolubility of the carbonate in
dilute ammonia.

**Answer.** $\ce{Ag+}$ as AgCl (Group I), $\ce{Cu^2+}$ as CuS (Group II),
$\ce{Ba^2+}$ as $\ce{BaCO3}$ (Group V).

**Check.** The sequence follows the standard group scheme: Group I (dilute HCl) before
Group II ($\ce{H2S}$ in acid) before Group V (ammonium carbonate). Reversing the first
two stages would precipitate copper sulphide together with silver chloride and make the
separation ambiguous.

**Where marks are lost.** Using ammonia before acidifying, which precipitates copper and
silver hydroxides together, or omitting the confirmatory tests.

---

## Part F — Multiple-choice self-check

### 53. The $d^5$ ion

**Strategy.** Write the neutral-atom configuration of each element, remove the $4s$
electrons first, and count the remaining $3d$ electrons.

**Working.** Manganese is $[\ce{Ar}]3d^54s^2$. Removing the two $4s$ electrons leaves
$3d^5$, so $\ce{Mn^2+}$ is $d^5$.

**Answer: B.** $\ce{Mn^2+}$.

**Why A is wrong.** $\ce{Fe^2+}$ is $d^6$. Iron is $[\ce{Ar}]3d^64s^2$, and removing
two $4s$ electrons gives $d^6$.

**Why C is wrong.** $\ce{Cr^3+}$ is $d^3$; chromium is $[\ce{Ar}]3d^54s^1$ and loses
three electrons.

**Why D is wrong.** $\ce{Cu^2+}$ is $d^9$; copper is $[\ce{Ar}]3d^{10}4s^1$.

**Check.** Each count satisfies the electron bookkeeping: Mn (Z = 25) with charge +2
has 23 electrons, which is $18 + 5$, that is $d^5$.

**Where marks are lost.** Counting the $4s$ electrons as $3d$ electrons, which makes
$\ce{Fe^2+}$ look like $d^8$.

### 54. CFSE of a high-spin $d^5$ octahedral complex

**Strategy.** Write the high-spin $d^5$ occupancy, then apply
$\text{CFSE} = (-0.4n_{t_{2g}} + 0.6n_{e_g})\Delta_o$.

**Working.** A high-spin $d^5$ ion has the configuration $t_{2g}^3e_g^2$, so

$$\text{CFSE} = \left[-0.4(3) + 0.6(2)\right]\Delta_o = (-1.2 + 1.2)\Delta_o = 0$$

The stabilisation of the three $t_{2g}$ electrons is exactly cancelled by the
destabilisation of the two $e_g$ electrons.

**Answer: C.** Zero.

**Why A is wrong.** $-0.4\Delta_o$ is the CFSE of high-spin $d^6$, not $d^5$.

**Why B is wrong.** $-2.0\Delta_o$ does not correspond to any simple $d^n$
configuration: low-spin $d^6$ is $-2.4\Delta_o$ and high-spin $d^6$ is $-0.4\Delta_o$.

**Why D is wrong.** $-1.2\Delta_o$ is the CFSE of $d^3$, not $d^5$.

**Check.** The result explains the observed properties of high-spin manganese(II): it is
almost colourless (every $d$–$d$ transition would need a spin flip) and shows no
ligand-field preference for octahedral over tetrahedral geometry.

**Where marks are lost.** Assuming that a $d^5$ ion must have a large CFSE because it
has five $d$ electrons.

### 55. The 18-electron complex

**Strategy.** Count the valence electrons with a single stated convention and compare
each total with 18.

**Working.** In the ionic convention, iron(0) contributes 8 electrons and five
carbonyls contribute 10, giving 18.

**Answer: C.** $\ce{[Fe(CO)5]}$.

**Why A is wrong.** $\ce{[Ni(C5H5)2]}$ has $8 + 12 = 20$ electrons; the extra pair
occupies antibonding orbitals.

**Why B is wrong.** $\ce{[PtCl4]^2-}$ has $8 + 8 = 16$ electrons and is a stable
square-planar $d^8$ complex, but it does not obey the 18-electron rule.

**Why D is wrong.** $\ce{[TiCl4]}$ has $0 + 8 = 8$ electrons; titanium(IV) is $d^0$
and there are no low-lying $d$ electrons to fill.

**Check.** The three failures are the three systematic exceptions described in
Chapter 4: 16-electron $d^8$ square planar, 20-electron metallocene, and early metal in
a high oxidation state.

**Where marks are lost.** Counting each cyclopentadienyl carbon as a separate donor.

### 56. Formula units in the rock-salt cell

**Strategy.** Apply the sharing rules to each ion site and sum the contributions.

**Working.** For one ion, eight corners at $1/8$ and six face centres at $1/2$ give
$1 + 3 = 4$. For the other, twelve edges at $1/4$ and one body centre at 1 give
$3 + 1 = 4$.

**Answer: C (four).** Four formula units per cell.

**Why A is wrong.** One formula unit per cell describes the caesium chloride structure,
not rock salt.

**Why B is wrong.** Two is the value of $Z$ for the tetragonal rutile cell of
$\ce{TiO2}$, not for a cubic rock-salt cell.

**Why D is wrong.** Eight is the number of corners, not the number of formula units.

**Check.** The value is confirmed by the density calculation: using $Z = 4$ reproduces
the measured density of NaCl to within 0.05 %.

**Where marks are lost.** Counting corner ions as whole ions.

### 57. Spin-only moment of high-spin $\ce{Fe^3+}$

**Strategy.** Determine the $d$ count, then apply $\mu = \sqrt{n(n+2)}$.

**Working.** $\ce{Fe^3+}$ is $d^5$, so $n = 5$ and
$\mu = \sqrt{5 \times 7} = \sqrt{35} = 5.92\ \mu_{\text{B}}$.

**Answer: D.** $5.92\ \mu_{\text{B}}$.

**Why C is wrong.** $3.87\ \mu_{\text{B}}$ corresponds to three unpaired electrons
($d^3$ or high-spin $d^7$).

**Why B is wrong.** $2.83\ \mu_{\text{B}}$ corresponds to two unpaired electrons
($d^8$).

**Why A is wrong.** $1.73\ \mu_{\text{B}}$ corresponds to one unpaired electron ($d^9$).

**Check.** The five unpaired electrons of the high-spin $d^5$ configuration give the
largest spin-only moment of the first-row ions, which is why high-spin manganese(II)
and iron(III) are the most strongly paramagnetic common ions.

**Where marks are lost.** Using $n = 3$ by confusing $\ce{Fe^3+}$ with $\ce{Cr^3+}$.

### 58. Why base hydrolysis is second order

**Strategy.** Derive the rate law from the mechanism: identify the rate-determining step
and express the concentration of the intermediate in terms of the reactants.

**Working.** The mechanism is $S_N1$CB: hydroxide first deprotonates a coordinated
ammonia in a fast equilibrium (constant $K$), and the resulting amido complex then
dissociates chloride in the rate-determining step (constant $k$). The rate is therefore
$k[\text{amido}] = kK[\text{complex}][\ce{OH^-}]$.

**Answer: B.** The conjugate base forms before the rate-determining step.

**Why A is wrong.** The mechanism is dissociative, not associative; the incoming ligand
does not attack the metal in the rate-determining step.

**Why C is wrong.** A good leaving group would make the reaction faster but would not
change the order with respect to hydroxide.

**Why D is wrong.** Water is the entering ligand, but it enters after the
rate-determining step and therefore does not appear in the rate law.

**Check.** The mechanism also predicts a kinetic isotope effect when N–H is replaced by
N–D, which is observed — a second-order rate law alone would not distinguish an
associative pathway from the conjugate-base one.

**Where marks are lost.** Concluding that second-order kinetics implies an associative
mechanism; the conjugate-base pathway is second order and dissociative.

---

## Top ten errors in this level

| Rank | Error | Why it costs marks | Correct habit |
|---|---|---|---|
| 1 | Mixing the ionic and covalent electron-counting conventions | The total is wrong by the charge on the complex | Choose one convention, state it, and keep it for the whole calculation |
| 2 | Counting a cyclopentadienyl ligand as 5 electrons | Every metallocene count is wrong by 2 | $\eta^5$-$\ce{C5H5}$ is a 6-electron donor (aromatic sextet) |
| 3 | Omitting the $+0.6$ term for $e_g$ electrons in CFSE | Overestimates CFSE; $d^5$ high spin wrongly non-zero | $\text{CFSE} = (-0.4n_{t_{2g}} + 0.6n_{e_g})\Delta_o$ |
| 4 | Making the second electron affinity negative | Lattice enthalpy wrong by hundreds of kJ mol⁻¹ | Adding an electron to an anion always costs energy |
| 5 | Weighting an average potential equally instead of by electron count | $E^\circ$ for a multi-step couple is wrong | $E^\circ = \sum n_iE_i^\circ / \sum n_i$ |
| 6 | Counting corner atoms as whole atoms | $Z$ wrong by a factor of 8 | Corner 1/8, edge 1/4, face 1/2, body 1 |
| 7 | Assuming a more exergonic electron transfer is always faster | Misses the Marcus inverted region | Barrier is a parabola with a minimum at $\Delta G^\circ = -\lambda$ |
| 8 | Confusing lability with thermodynamic stability | Wrong classification of inert complexes | Lability is kinetic; check the $d$ configuration |
| 9 | Reporting $\theta$ instead of $2\theta$ in Bragg calculations | Angle wrong by a factor of 2 | Bragg's law gives $\theta$; the diffractometer reports $2\theta$ |
| 10 | Forgetting to convert years to seconds in decay calculations | Activity wrong by $3\times10^{7}$ | $1\ \text{year} = 3.156\times10^{7}\ \text{s}$ |
