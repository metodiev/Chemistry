# Level 2 — Worked Solutions

> **Level:** Intermediate (Level 2 — Intermediate Chemistry)
> **Companion to:** [`../exercises/level-2-exercises.md`](../exercises/level-2-exercises.md)
> **Items:** 60

Every solution follows the same order: the relation is written in symbols first, the
substitution carries its units, and the answer is rounded only at the end. Where an
approximation is used, the check that licenses it is shown explicitly. Temperatures
are stated wherever a pH, $K_w$ or $E^{\circ}$ value depends on them; all pH values
below are at 25 °C unless the item says otherwise.

---

## Part A — Conceptual questions

### 1. The Avogadro constant and the Avogadro number — [Ch. 1]

**Strategy.** Separate the constant (a physical quantity with a unit) from the pure
number, then explain what the 2019 redefinition changed and why.

**Answer.** The Avogadro constant is $N_{\text{A}} = 6.022\,140\,76\times10^{23}\ \text{mol}^{-1}$;
the Avogadro number is the same digits without the unit, $6.022\,140\,76\times10^{23}$.
The constant is the number of entities per mole, so its unit is essential: it is what
converts a count into an amount. Before 2019 the mole was defined by fixing the mass
of $0.012\ \text{kg}$ of carbon-12, which made $N_{\text{A}}$ an experimentally
determined quantity tied to the kilogram artefact. Since 2019 the mole is defined by
fixing $N_{\text{A}}$ exactly, so a mole is simply a specified number of entities and
the molar mass constant is no longer exactly $1\ \text{g mol}^{-1}$ (it departs by
about $3\times10^{-10}$). The change decoupled the definition of amount of substance
from any particular isotope, which is why the mole now survives any future revision of
the mass standard.

**Check.** The distinction matters numerically: writing $6.022\times10^{23}$ as a pure
number and then using it as $\text{mol}^{-1}$ is dimensionally wrong.

### 2. Limiting reactant, yield and atom economy — [Ch. 2]

**Strategy.** Identify what each metric is referenced to: the limiting reactant for
yield, the balanced equation for atom economy.

**Answer.** The theoretical yield is the amount of product the stoichiometry permits,
and it is set by the reactant that runs out first: any reactant present in excess
cannot increase the product beyond the amount the limiting reactant can supply.
Percentage yield compares the mass actually isolated with that theoretical mass, so it
measures the efficiency of the laboratory or plant operation — losses in filtration,
side reactions, incomplete conversion. Atom economy compares the molar mass of the
desired product with the total molar mass of all reactants, so it measures how much of
the reactant mass ends up in the target by construction of the equation. The two are
independent: an addition reaction such as $\ce{C2H4(g) + H2(g) -> C2H6(g)}$ has
100 % atom economy because every atom appears in the product, yet a poor isolation can
give a 40 % yield. Conversely, a substitution that produces a large mass of by-product
can run to 100 % conversion and still have a low atom economy.

**Check.** "Yield" never exceeds 100 % for a correct calculation; "atom economy" is a
property of the equation alone and does not depend on how the reaction was run.

### 3. Molarity, molality and temperature — [Ch. 3]

**Strategy.** Compare the denominators: volume of solution against mass of solvent.

**Answer.** Molarity is amount of solute per unit volume of solution,
$c = n/V$, in $\text{mol dm}^{-3}$; molality is amount of solute per unit mass of
solvent, $b = n/m_{\text{solvent}}$, in $\text{mol kg}^{-1}$. The volume of a solution
expands on heating, so a molarity fixed at one temperature corresponds to a different
concentration at another; the mass of solvent does not change with temperature, so
molality is temperature-independent. Colligative properties depend on the ratio of
solute particles to solvent molecules, which is exactly what molality measures; using
molarity would introduce a spurious temperature dependence into
$\Delta T_{\text{f}} = K_{\text{f}}bi$. Precise physical-chemistry work also uses
molality because the solvent mass can be weighed to high accuracy, whereas a solution
volume must be measured in a volumetric flask with a calibration uncertainty.

**Check.** For dilute aqueous solutions at room temperature the two are numerically
almost equal, which is why the distinction is easy to miss.

### 4. Assumptions of the ideal-gas model — [Ch. 4]

**Strategy.** Name the two assumptions, then match each van der Waals term to the
assumption it repairs.

**Answer.** The ideal-gas equation assumes that the particles occupy negligible volume
compared with the container and that there are no intermolecular forces between them.
The parameter $b$ is the excluded volume per mole, so $V - nb$ replaces $V$ and
corrects for finite molecular size; it raises the predicted pressure because the free
volume is smaller than the container volume. The parameter $a$ measures the strength of
attractive forces, so $an^{2}/V^{2}$ is added to the measured pressure and the term
$(p + an^{2}/V^{2})$ corrects for the fact that attractions reduce the pressure exerted
on the walls. Both corrections vanish as $V \to \infty$, which is why real gases become
ideal at low pressure and high temperature.

**Check.** For helium $a$ is very small and $b$ is small; for carbon dioxide both are
large, so deviations appear at modest pressures.

### 5. Boiling points of the hydrogen halides — [Ch. 5]

**Strategy.** Separate the trend governed by dispersion from the anomaly governed by
hydrogen bonding.

**Answer.** From $\ce{HCl}$ to $\ce{HBr}$ to $\ce{HI}$ the boiling point rises
(−85.1, −66.8, −35.4 °C), because the number of electrons increases from 18 to 36 to 54
and the dispersion (London) interaction strengthens with polarisability. All three have
dipole–dipole interactions, but the dispersion term dominates the trend. $\ce{HF}$ breaks
the pattern: with only 10 electrons it should boil far below $\ce{HCl}$, yet it boils at
19.5 °C. The F–H bond is short and the fluorine atom is small and very
electronegative, so the molecules form strong intermolecular $\ce{F-H\bond{...}F}$
hydrogen bonds; each molecule can both donate and accept, giving a three-dimensional
network that must be broken before vaporisation.

**Check.** The anomaly is not caused by the dipole moment alone: $\ce{HCl}$ has a
substantial dipole moment of its own but no hydrogen bonding, and boils roughly 100 K
lower.

### 6. $\ce{SF4}$ and $\ce{XeF4}$ geometries — [Ch. 6]

**Strategy.** Count domains, then place lone pairs to minimise repulsion.

**Answer.** Sulfur in $\ce{SF4}$ has four bonding pairs and one lone pair, giving five
electron domains and a trigonal-bipyramidal electron-domain geometry; the lone pair
occupies an equatorial position because that position has only two nearest neighbours
at 90°, whereas an axial lone pair would have three. The resulting molecular geometry
is see-saw. Xenon in $\ce{XeF4}$ has four bonding pairs and two lone pairs, six electron
domains and an octahedral electron-domain geometry; the two lone pairs are placed
trans to one another (180° apart) to minimise lone-pair–lone-pair repulsion, leaving the
four fluorines in a square plane. The difference is therefore not "lone pairs bend
things" but the number of domains and the geometry from which the lone pairs are
removed.

**Check.** $\ce{XeF4}$ is non-polar, because the four Xe–F bond dipoles cancel in the
square plane; $\ce{SF4}$ is polar.

### 7. Why $\ce{CO2}$ is non-polar but $\ce{H2O}$ is polar — [Ch. 7]

**Strategy.** Treat the bond dipoles as vectors and add them with the geometry.

**Answer.** Carbon in $\ce{CO2}$ is $sp$ hybridised and the molecule is linear, so the
two C=O bond dipoles are equal and exactly opposed at 180°; their vector sum is zero
and the molecule has no net dipole moment. Oxygen in $\ce{H2O}$ is approximately
$sp^{3}$ hybridised with two lone pairs, giving a bent molecule with an H–O–H angle of
about 104.5°; the two O–H bond dipoles point from H towards O and add at 104.5° to give
a resultant of about $1.85\ \text{D}$, further increased by the lone-pair contribution.
Polarity therefore requires both polar bonds and a geometry that does not cancel them:
$\ce{CCl4}$ and $\ce{BF3}$ are also non-polar for the same reason, despite strongly
polar bonds.

**Check.** Symmetry alone is not enough; the bonds must also be polar. $\ce{CH4}$ is
non-polar and has zero bond dipoles by symmetry plus near-zero C–H polarity.

### 8. Formation enthalpies versus mean bond enthalpies — [Ch. 8]

**Strategy.** Contrast exact, substance-specific data with averaged, state-specific
data.

**Answer.** Standard enthalpies of formation are measured for the actual compound in
its actual physical state, so a Hess calculation from them uses data that already
include every structural feature of the substance, including strain, hydrogen bonding
and phase. Mean bond enthalpies are averages over many different compounds containing
that bond, so they cannot reproduce the specific environment of a bond in one molecule;
they also refer to gaseous species, so any change of state must be added separately.
Consequently a Hess cycle from formation enthalpies is exact within the tabulated data,
whereas a bond-enthalpy calculation typically carries an error of 5–15 %, as the
methane comparison in item 41 shows. Bond enthalpies remain useful for estimating
reaction enthalpies when formation data are unavailable, and for comparing the
strengths of bonds between similar compounds.

**Check.** A bond-enthalpy calculation for a reaction in solution ignores solvation
enthalpies entirely, which is a second, independent source of error.

### 9. Strong and weak acids at the same concentration — [Ch. 11]

**Strategy.** Compare the degree of ionisation and the number of charge carriers.

**Answer.** Hydrochloric acid is a strong acid and is essentially fully ionised, so
$[\ce{H3O+}] = 0.100\ \text{mol dm}^{-3}$ and $\mathrm{pH} = 1.00$. Acetic acid has
$K_a = 1.8\times10^{-5}$, so
$[\ce{H3O+}] \approx \sqrt{(1.8\times10^{-5})(0.100)} = 1.34\times10^{-3}\ \text{mol dm}^{-3}$
and $\mathrm{pH} = 2.87$; only about 1.3 % of the molecules are ionised. The
conductivity of the hydrochloric acid solution is therefore much higher, because
conductivity depends on the concentration of mobile ions rather than on the formal
concentration of acid. On tenfold dilution the strong acid remains fully ionised, so
its pH rises by exactly one unit; the weak acid ionises to a greater fraction because
dilution lowers $[\ce{H3O+}]$ and the equilibrium
$\ce{CH3COOH + H2O <=> H3O+ + CH3COO-}$ shifts right, but its pH rises by only about
half a unit, since $[\ce{H3O+}] \propto \sqrt{c}$.

**Check.** Both solutions have the same titratable acidity, so they require the same
volume of standard base despite their different pH values.

### 10. Comparing $K_{sp}$ values of different stoichiometries — [Ch. 13]

**Strategy.** Convert each $K_{sp}$ into a molar solubility before comparing.

**Answer.** For $\ce{AgCl}$, $K_{sp} = s^{2}$, so
$s = \sqrt{1.8\times10^{-10}} = 1.3\times10^{-5}\ \text{mol dm}^{-3}$. For
$\ce{Ag2CrO4}$, $K_{sp} = (2s)^{2}s = 4s^{3}$, so
$s = (1.1\times10^{-12}/4)^{1/3} = 6.5\times10^{-5}\ \text{mol dm}^{-3}$, which is about
five times larger despite the smaller $K_{sp}$. The exponent differs because the
chromate salt releases three ions per formula unit, so its expression contains the cube
of a concentration and a factor of four. Two $K_{sp}$ values may be compared directly
only when the salts have the same stoichiometry, for example two 1:1 salts; otherwise
the comparison must pass through the calculated solubility. The comparison also assumes
no common ion, no hydrolysis and no complex formation.

**Check.** A salt with a very small $K_{sp}$ but a 1:3 stoichiometry, such as
$\ce{Fe(OH)3}$, can still be more soluble than a 1:1 salt with a larger $K_{sp}$.

---

## Part B — Basic problems

### 11. Amount and number of molecules in glucose — [Ch. 1]

**Strategy.** Convert mass to amount with the molar mass, then amount to number with
$N_{\text{A}}$.

**Working.**

$$
M(\ce{C6H12O6}) = 6(12.011) + 12(1.008) + 6(15.999)
= 72.066 + 12.096 + 95.994 = 180.156\ \text{g mol}^{-1}
$$

$$
n = \frac{m}{M} = \frac{25.0\ \text{g}}{180.156\ \text{g mol}^{-1}} = 0.1388\ \text{mol}
$$

$$
N = nN_{\text{A}} = (0.1388\ \text{mol})(6.022\times10^{23}\ \text{mol}^{-1})
= 8.36\times10^{22}
$$

**Answer.** $n = 0.139\ \text{mol}$ (3 s.f.); $N = 8.36\times10^{22}$ molecules.

**Check.** $25.0\ \text{g}$ is about one seventh of a mole, so about one seventh of
$6.02\times10^{23}$ is expected, namely $8.6\times10^{22}$; the result agrees.

**Where marks are lost.** Using $M = 180\ \text{g mol}^{-1}$ and quoting five figures;
forgetting that the entity asked for is the molecule, not the atom.

### 12. Mass of a given number of carbon dioxide molecules — [Ch. 1]

**Strategy.** Reverse item 11: divide by $N_{\text{A}}$, multiply by $M$.

**Working.**

$$
n = \frac{N}{N_{\text{A}}} = \frac{3.00\times10^{22}}{6.022\times10^{23}\ \text{mol}^{-1}}
= 4.982\times10^{-2}\ \text{mol}
$$

$$
m = nM = (4.982\times10^{-2}\ \text{mol})(44.009\ \text{g mol}^{-1}) = 2.19\ \text{g}
$$

**Answer.** $m = 2.19\ \text{g}$ (3 s.f.).

**Check.** $3.00\times10^{22}$ is one twentieth of $6.02\times10^{23}$, and one
twentieth of $44\ \text{g}$ is $2.2\ \text{g}$; the answer is consistent.

**Where marks are lost.** Using $M = 44.0$ but dividing by $10^{22}$ instead of
$10^{23}$, which gives an answer 10 times too large.

### 13. Mass of aluminium chloride from aluminium — [Ch. 2]

**Strategy.** Convert the mass of the limiting reactant to amount, apply the 2:2 mole
ratio, convert back to mass.

**Working.**

$$
\ce{2Al(s) + 3Cl2(g) -> 2AlCl3(s)}
$$

$$
n(\ce{Al}) = \frac{5.40\ \text{g}}{26.982\ \text{g mol}^{-1}} = 0.2001\ \text{mol}
$$

$$
n(\ce{AlCl3}) = n(\ce{Al}) \times \frac{2}{2} = 0.2001\ \text{mol}
$$

$$
M(\ce{AlCl3}) = 26.982 + 3(35.45) = 133.33\ \text{g mol}^{-1}
$$

$$
m = (0.2001\ \text{mol})(133.33\ \text{g mol}^{-1}) = 26.7\ \text{g}
$$

**Answer.** $m(\ce{AlCl3}) = 26.7\ \text{g}$ (3 s.f.).

**Check.** The 1:1 ratio of aluminium to aluminium chloride means the product mass
must exceed the reactant mass by the mass of chlorine incorporated, which it does.

**Where marks are lost.** Using the 2:3 ratio from aluminium to chlorine instead of the
2:2 ratio to product; using $M(\ce{Al}) = 27.0$ but carrying five figures through.

### 14. Limiting reactant in ammonia synthesis — [Ch. 2]

**Strategy.** Compute the limiting-reactant quotient $q_i = n_i/\nu_i$ for each
reactant; the smaller quotient identifies the limiting reactant.

**Working.**

$$
\ce{N2(g) + 3H2(g) -> 2NH3(g)}
$$

$$
n(\ce{N2}) = \frac{10.0}{28.014} = 0.3570\ \text{mol}, \qquad
q(\ce{N2}) = \frac{0.3570}{1} = 0.3570\ \text{mol}
$$

$$
n(\ce{H2}) = \frac{2.00}{2.016} = 0.9921\ \text{mol}, \qquad
q(\ce{H2}) = \frac{0.9921}{3} = 0.3307\ \text{mol}
$$

Hydrogen has the smaller quotient and is limiting.

$$
n(\ce{NH3}) = \frac{2}{3}(0.9921) = 0.6614\ \text{mol}, \qquad
m = (0.6614)(17.031) = 11.3\ \text{g}
$$

$$
n(\ce{N2})_{\text{consumed}} = \frac{1}{3}(0.9921) = 0.3307\ \text{mol}
$$

$$
n(\ce{N2})_{\text{remaining}} = 0.3570 - 0.3307 = 0.0263\ \text{mol}, \qquad
m = (0.0263)(28.014) = 0.736\ \text{g}
$$

**Answer.** $\ce{H2}$ is limiting; $m(\ce{NH3}) = 11.3\ \text{g}$;
$m(\ce{N2})$ remaining $= 0.736\ \text{g}$.

**Check.** Mass balance: $10.0 + 2.00 = 12.00\ \text{g}$ in, and
$11.26 + 0.74 = 12.00\ \text{g}$ out, as conservation of mass requires.

**Where marks are lost.** Comparing moles rather than quotients, which wrongly makes
$\ce{N2}$ limiting; reporting the excess as the amount consumed rather than the amount
remaining.

### 15. Dilution of hydrochloric acid — [Ch. 3]

**Strategy.** The solute is conserved, so $c_1V_1 = c_2V_2$.

**Working.**

$$
c_2 = \frac{c_1V_1}{V_2}
= \frac{(2.00\ \text{mol dm}^{-3})(25.0\ \text{cm}^{3})}{250.0\ \text{cm}^{3}}
= 0.200\ \text{mol dm}^{-3}
$$

**Answer.** $c_2 = 0.200\ \text{mol dm}^{-3}$ (3 s.f.).

**Check.** The volume increased tenfold, so the concentration must fall tenfold; the
dilution factor is $250.0/25.0 = 10$.

**Where marks are lost.** Using volumes in different units on the two sides — harmless
here because the ratio is dimensionless, but fatal when one side is in $\text{dm}^{3}$.

### 16. Molarity of a sodium chloride solution — [Ch. 3]

**Strategy.** Convert mass to amount, convert volume to $\text{dm}^{3}$, divide.

**Working.**

$$
M(\ce{NaCl}) = 22.990 + 35.45 = 58.44\ \text{g mol}^{-1}
$$

$$
n = \frac{5.85\ \text{g}}{58.44\ \text{g mol}^{-1}} = 0.1001\ \text{mol}
$$

$$
V = 250.0\ \text{cm}^{3} = 0.2500\ \text{dm}^{3}
$$

$$
c = \frac{n}{V} = \frac{0.1001\ \text{mol}}{0.2500\ \text{dm}^{3}} = 0.400\ \text{mol dm}^{-3}
$$

**Answer.** $c = 0.400\ \text{mol dm}^{-3}$ (3 s.f.).

**Check.** $5.85\ \text{g}$ is about $0.1\ \text{mol}$ in a quarter of a litre, so
$0.4\ \text{mol dm}^{-3}$ is the expected magnitude.

**Where marks are lost.** Forgetting to convert $\text{cm}^{3}$ to $\text{dm}^{3}$,
which gives an answer 1000 times too large.

### 17. Volume of an ideal gas — [Ch. 4]

**Strategy.** Rearrange $pV = nRT$ for $V$ and use SI units throughout.

**Working.**

$$
V = \frac{nRT}{p}
= \frac{(0.250\ \text{mol})(8.314\ \text{J mol}^{-1}\ \text{K}^{-1})(298.15\ \text{K})}{1.00\times10^{5}\ \text{Pa}}
$$

$$
V = \frac{619.7\ \text{J}}{1.00\times10^{5}\ \text{Pa}} = 6.197\times10^{-3}\ \text{m}^{3}
= 6.20\ \text{dm}^{3}
$$

**Answer.** $V = 6.20\ \text{dm}^{3}$ (3 s.f.).

**Check.** At SATP one mole occupies $24.79\ \text{dm}^{3}$, so a quarter of a mole
should occupy about $6.2\ \text{dm}^{3}$; the result matches.

**Where marks are lost.** Using $R = 8.314$ with $p$ in kPa, which gives a volume
1000 times too large; forgetting that $1\ \text{m}^{3} = 1000\ \text{dm}^{3}$.

### 18. Combined gas law — [Ch. 4]

**Strategy.** For a fixed amount of gas, $p_1V_1/T_1 = p_2V_2/T_2$.

**Working.**

$$
V_2 = V_1\frac{p_1}{p_2}\frac{T_2}{T_1}
= (200\ \text{cm}^{3})\left(\frac{100\ \text{kPa}}{95.0\ \text{kPa}}\right)
\left(\frac{250\ \text{K}}{273\ \text{K}}\right)
$$

$$
V_2 = (200)(1.0526)(0.9158) = 193\ \text{cm}^{3}
$$

**Answer.** $V_2 = 193\ \text{cm}^{3}$ (3 s.f.).

**Check.** The pressure falls slightly, which would expand the gas, but the temperature
falls by more, which contracts it; the net effect is a small decrease, consistent with
$193 < 200$.

**Where marks are lost.** Using Celsius temperatures, which makes the ratio
$250/273$ instead of $523/546$ and produces a badly wrong answer.

### 19. VSEPR predictions for three species — [Ch. 6]

**Strategy.** Count $\sigma$ bonds and lone pairs on the central atom, then apply the
repulsion ordering lone pair > multiple bond > bonding pair.

**Working.**

(a) $\ce{SO2}$: S has two $\sigma$ bonds and one lone pair, so three domains. The
electron-domain geometry is trigonal planar and the molecular geometry is bent. The
double bonds occupy more space than a single bond, so the angle is slightly less than
120°, about 119°.

(b) $\ce{PF5}$: P has five $\sigma$ bonds and no lone pair, so five domains. The
electron-domain and molecular geometries are both trigonal bipyramidal, with angles of
90° and 120°.

(c) $\ce{BrF5}$: Br has five $\sigma$ bonds and one lone pair, so six domains. The
electron-domain geometry is octahedral and the molecular geometry is square pyramidal,
with the four basal F–Br–F angles compressed to about 85° by the lone pair.

**Answer.** (a) 3 domains, bent, ≈119°; (b) 5 domains, trigonal bipyramidal, 90°/120°;
(c) 6 domains, square pyramidal, ≈85°.

**Check.** In each case the number of domains equals the steric number and the lone
pairs occupy the positions with the fewest 90° neighbours.

**Where marks are lost.** Giving the electron-domain geometry when the question asks
for the molecular geometry; describing $\ce{BrF5}$ as octahedral.

### 20. Heat required to warm water — [Ch. 8]

**Strategy.** Use $q = mc\Delta T$ with the mass in grams and $c$ in
$\text{J g}^{-1}\ \text{K}^{-1}$.

**Working.**

$$
\Delta T = 45.0 - 21.0 = 24.0\ \text{K}
$$

$$
q = mc\Delta T = (150\ \text{g})(4.18\ \text{J g}^{-1}\ \text{K}^{-1})(24.0\ \text{K})
= 1.50\times10^{4}\ \text{J}
$$

**Answer.** $q = +15.0\ \text{kJ}$ absorbed by the water (3 s.f.).

**Check.** $150\ \text{g}$ is $8.32\ \text{mol}$ of water, and
$(8.32)(75.3\ \text{J K}^{-1}\ \text{mol}^{-1})(24.0\ \text{K}) = 15.0\ \text{kJ}$, in
agreement with the direct calculation.

**Where marks are lost.** Sign confusion: the water absorbs heat, so $q$ is positive for
the water and negative for the surroundings.

### 21. pH and pOH of a strong acid and a strong base — [Ch. 11]

**Strategy.** Strong acids and bases are fully ionised, so the analytical concentration
equals the ion concentration; use $\mathrm{pH} + \mathrm{pOH} = 14.00$ at 25 °C.

**Working.**

(a)

$$
[\ce{H3O+}] = 0.0150\ \text{mol dm}^{-3}, \qquad
\mathrm{pH} = -\log_{10}(0.0150) = 1.82
$$

$$
\mathrm{pOH} = 14.00 - 1.82 = 12.18
$$

(b)

$$
[\ce{OH-}] = 0.0150\ \text{mol dm}^{-3}, \qquad
\mathrm{pOH} = 1.82, \qquad \mathrm{pH} = 12.18
$$

**Answer.** (a) pH 1.82, pOH 12.18; (b) pOH 1.82, pH 12.18.

**Check.** Both solutions are $0.0150\ \text{mol dm}^{-3}$ in the ion that controls the
pH, and their pH values are symmetric about 7.00, as they must be at 25 °C.

**Where marks are lost.** Using $\mathrm{pH} = 7$ neutrality at a temperature other
than 25 °C, or applying the weak-acid square-root expression to a strong acid.

### 22. Oxidation numbers — [Ch. 12]

**Strategy.** Apply the rules in order: free element, monatomic ion, Group 1 and 2,
fluorine, hydrogen, oxygen, halogen, then the sum rule.

**Working.**

(a) $\ce{K2Cr2O7}$: $2(+1) + 2x + 7(-2) = 0$, so $2x = +12$ and $x = +6$.

(b) $\ce{MnO4-}$: $x + 4(-2) = -1$, so $x = +7$.

(c) $\ce{Na2S2O3}$: $2(+1) + 2x + 3(-2) = 0$, so $2x = +4$ and $x = +2$.

(d) $\ce{NH4NO3}$: the cation $\ce{NH4+}$ gives $x + 4(+1) = +1$, so $x = -3$; the
anion $\ce{NO3-}$ gives $x + 3(-2) = -1$, so $x = +5$.

(e) $\ce{H2O2}$: hydrogen is $+1$, so $2(+1) + 2x = 0$ and $x = -1$, the peroxide rule.

**Answer.** Cr $+6$; Mn $+7$; S $+2$; N $-3$ and $+5$; O $-1$.

**Check.** Every set sums to the overall charge of the species. The two nitrogen
environments in ammonium nitrate are a reminder that one formula unit can contain the
same element in two oxidation states.

**Where marks are lost.** Assigning a single average value to both nitrogen atoms;
taking oxygen as $-2$ in a peroxide.

---

## Part C — Intermediate problems

### 23. Percentage yield from an impure carbonate — [Ch. 2]

**Strategy.** Correct the sample mass for purity, convert to amount, apply the 1:1
ratio, then compare the actual mass with the theoretical mass.

**Working.**

$$
m(\ce{CaCO3}) = 0.850 \times 25.0\ \text{g} = 21.25\ \text{g}
$$

$$
n(\ce{CaCO3}) = \frac{21.25}{100.086} = 0.2123\ \text{mol}
= n(\ce{CaO})
$$

$$
m_{\text{theoretical}}(\ce{CaO}) = (0.2123\ \text{mol})(56.077\ \text{g mol}^{-1})
= 11.91\ \text{g}
$$

$$
\text{percentage yield} = \frac{10.8}{11.91} \times 100\,\% = 90.7\,\%
$$

**Answer.** Theoretical mass $11.9\ \text{g}$; yield $90.7\,\%$ (3 s.f.).

**Check.** Mass balance: $21.25\ \text{g}$ of carbonate loses $0.2123 \times 44.009 =
9.34\ \text{g}$ of carbon dioxide, leaving $11.91\ \text{g}$ of oxide, correct.

**Where marks are lost.** Using $25.0\ \text{g}$ instead of $21.25\ \text{g}$ as the
carbonate mass; treating the impurity as reacting.

### 24. Titration of sulfuric acid with sodium hydroxide — [Ch. 3]

**Strategy.** Use the 1:2 stoichiometry of acid to base, then divide by the acid volume.

**Working.**

$$
\ce{H2SO4(aq) + 2NaOH(aq) -> Na2SO4(aq) + 2H2O(l)}
$$

$$
n(\ce{NaOH}) = (0.1000\ \text{mol dm}^{-3})(23.40\times10^{-3}\ \text{dm}^{3})
= 2.340\times10^{-3}\ \text{mol}
$$

$$
n(\ce{H2SO4}) = \tfrac{1}{2}(2.340\times10^{-3}) = 1.170\times10^{-3}\ \text{mol}
$$

$$
c(\ce{H2SO4}) = \frac{1.170\times10^{-3}\ \text{mol}}{25.0\times10^{-3}\ \text{dm}^{3}}
= 0.0468\ \text{mol dm}^{-3}
$$

$$
m(\ce{H2SO4}) = (1.170\times10^{-3}\ \text{mol})(98.079\ \text{g mol}^{-1})
= 0.115\ \text{g}
$$

**Answer.** $c = 0.0468\ \text{mol dm}^{-3}$; $m = 0.115\ \text{g}$ in
$25.0\ \text{cm}^{3}$.

**Check.** The acid is diprotic, so the base volume would be twice that needed for a
monoprotic acid of the same concentration; the low molarity is consistent with a
dilute acid.

**Where marks are lost.** Using a 1:1 ratio and doubling the answer; omitting the
second acidic hydrogen.

### 25. Gas collected over water — [Ch. 4]

**Strategy.** Subtract the water vapour pressure to obtain the partial pressure of the
dry gas, then apply the ideal-gas equation.

**Working.**

$$
\ce{Zn(s) + 2HCl(aq) -> ZnCl2(aq) + H2(g)}
$$

$$
n(\ce{Zn}) = \frac{2.65\ \text{g}}{65.38\ \text{g mol}^{-1}} = 0.04053\ \text{mol}
= n(\ce{H2})
$$

$$
p(\ce{H2}) = 101.3 - 3.17 = 98.13\ \text{kPa} = 9.813\times10^{4}\ \text{Pa}
$$

$$
V = \frac{nRT}{p}
= \frac{(0.04053)(8.314)(298.15)}{9.813\times10^{4}}
= 1.024\times10^{-3}\ \text{m}^{3}
$$

**Answer.** $V = 1.02\ \text{dm}^{3}$ (3 s.f.).

**Check.** $0.0405\ \text{mol}$ at SATP would occupy about $1.00\ \text{dm}^{3}$, and
the pressure is slightly below $10^{5}\ \text{Pa}$, so a slightly larger volume is
expected.

**Where marks are lost.** Using the total pressure as the gas pressure, which
underestimates the volume by about 3 %; forgetting the 1:1 ratio.

### 26. Bond angle from dipole moments — [Ch. 7]

**Strategy.** For two equal bond dipoles $\mu_b$ at angle $\theta$, the resultant is
$\mu = 2\mu_b\cos(\theta/2)$.

**Working.**

$$
\cos\!\left(\frac{\theta}{2}\right) = \frac{\mu}{2\mu_b}
= \frac{1.85\ \text{D}}{2(1.51\ \text{D})} = 0.6126
$$

$$
\frac{\theta}{2} = \cos^{-1}(0.6126) = 52.2^\circ
\qquad\Longrightarrow\qquad
\theta = 104.4^\circ
$$

**Answer.** $\theta \approx 104^\circ$ (3 s.f.).

**Check.** The experimental H–O–H angle is 104.5°, so the vector model reproduces the
geometry to better than 1 %; the small difference arises because the lone pairs also
contribute to the observed dipole moment.

**Where marks are lost.** Forgetting the factor of two and reporting 52°; using degrees
and radians interchangeably.

### 27. Enthalpy of vaporisation from two vapour pressures — [Ch. 5]

**Strategy.** Apply the integrated Clausius–Clapeyron equation between the two points.

**Working.**

$$
\ln\!\left(\frac{p_2}{p_1}\right) = -\frac{\Delta H_{\text{vap}}}{R}
\left(\frac{1}{T_2} - \frac{1}{T_1}\right)
$$

$$
\ln\!\left(\frac{20.0}{8.00}\right) = 0.9163
$$

$$
\frac{1}{370} - \frac{1}{350} = 2.703\times10^{-3} - 2.857\times10^{-3}
= -1.544\times10^{-4}\ \text{K}^{-1}
$$

$$
\Delta H_{\text{vap}} = \frac{(8.314)(0.9163)}{1.544\times10^{-4}}
= 4.93\times10^{4}\ \text{J mol}^{-1}
$$

**Answer.** $\Delta H_{\text{vap}} = 49.3\ \text{kJ mol}^{-1}$ (3 s.f.).

**Check.** The vapour pressure roughly doubles over 20 K, which for a normal liquid
corresponds to a few tens of $\text{kJ mol}^{-1}$; the magnitude is reasonable.

**Where marks are lost.** Using $T$ in Celsius; inverting the temperature difference;
omitting the assumption that $\Delta H_{\text{vap}}$ is constant over 350–370 K.

### 28. Hybridisation and polarity — [Ch. 7]

**Strategy.** Count domains to obtain hybridisation, remove lone pairs to obtain
geometry, then add bond dipoles as vectors.

**Working.**

(a) $\ce{BeCl2}$: two domains, $sp$; linear; the two Be–Cl dipoles are equal and
opposed, so the molecule is non-polar.

(b) $\ce{BF3}$: three domains, $sp^{2}$; trigonal planar at 120°; the three B–F dipoles
cancel, so non-polar.

(c) $\ce{NF3}$: four domains with one lone pair, $sp^{3}$; trigonal pyramidal; the three
N–F dipoles add with a component along the lone-pair direction, so polar.

(d) $\ce{CH2Cl2}$: four domains, $sp^{3}$; tetrahedral; the C–Cl dipoles are not
cancelled by the two C–H bonds, so polar.

**Answer.** (a) $sp$, linear, non-polar; (b) $sp^{2}$, trigonal planar, non-polar;
(c) $sp^{3}$, trigonal pyramidal, polar; (d) $sp^{3}$, tetrahedral, polar.

**Check.** Polarity appears only when the geometry leaves a resultant; the two
non-polar cases both have a symmetric arrangement of identical bond dipoles.

**Where marks are lost.** Calling $\ce{NF3}$ non-polar by analogy with $\ce{NH3}$;
giving the electron-domain geometry for a molecule with lone pairs.

### 29. Combustion enthalpy of ethanol from formation enthalpies — [Ch. 8]

**Strategy.** Apply Hess's law with the stoichiometric coefficients, remembering that
$\Delta H^{\circ}_{\text{f}}$ of an element in its standard state is zero.

**Working.**

$$
\ce{C2H5OH(l) + 3O2(g) -> 2CO2(g) + 3H2O(l)}
$$

$$
\Delta H^{\circ}_{\text{rxn}} = \sum \nu\Delta H^{\circ}_{\text{f}}(\text{products})
- \sum \nu\Delta H^{\circ}_{\text{f}}(\text{reactants})
$$

$$
\Delta H^{\circ}_{\text{rxn}} = [2(-393.5) + 3(-285.8)] - [(-277.7) + 3(0)]
$$

$$
\Delta H^{\circ}_{\text{rxn}} = (-787.0 - 857.4) + 277.7 = -1366.7\ \text{kJ mol}^{-1}
$$

**Answer.** $\Delta H^{\circ} = -1367\ \text{kJ mol}^{-1}$ (4 s.f.).

**Check.** Ethanol is a fuel with roughly two-thirds the specific energy of octane on a
mass basis; $-1367\ \text{kJ}$ per $46\ \text{g}$ gives about
$-29.7\ \text{kJ g}^{-1}$, close to the tabulated $29.7\ \text{kJ g}^{-1}$.

**Where marks are lost.** Omitting the coefficient 3 on water; forgetting that
$\ce{O2}$ contributes zero; reversing the products and reactants.

### 30. Enthalpy of neutralisation by calorimetry — [Ch. 8]

**Strategy.** Compute the heat released from the temperature rise, then divide by the
amount of water formed.

**Working.**

$$
\ce{HCl(aq) + NaOH(aq) -> NaCl(aq) + H2O(l)}
$$

$$
q = mc\Delta T = (100.0\ \text{g})(4.18\ \text{J g}^{-1}\ \text{K}^{-1})(6.80\ \text{K})
= 2.842\times10^{3}\ \text{J}
$$

$$
n(\ce{H2O}) = n(\ce{HCl}) = (1.00\ \text{mol dm}^{-3})(0.0500\ \text{dm}^{3})
= 5.00\times10^{-2}\ \text{mol}
$$

$$
\Delta H = -\frac{q}{n} = -\frac{2.842\times10^{3}\ \text{J}}{5.00\times10^{-2}\ \text{mol}}
= -5.68\times10^{4}\ \text{J mol}^{-1}
$$

**Answer.** $\Delta H_{\text{neut}} = -56.8\ \text{kJ mol}^{-1}$ (3 s.f.).

**Check.** The accepted value for a strong acid and strong base is about
$-57.1\ \text{kJ mol}^{-1}$, so the result is within 1 %; the small deficit is heat lost
to the calorimeter.

**Where marks are lost.** Forgetting the negative sign (the reaction releases heat);
using the total mass of both solutions but the moles of only one reactant where the
equation is not 1:1.

### 31. Rate law from initial rates — [Ch. 9]

**Strategy.** Compare experiments in which one concentration changes while the other is
held constant; the ratio of rates gives the order.

**Working.** Comparing 1 and 2, $[\ce{B}]$ is constant and $[\ce{A}]$ doubles:

$$
\frac{r_2}{r_1} = \frac{8.0\times10^{-3}}{2.0\times10^{-3}} = 4
= 2^{m} \qquad\Longrightarrow\qquad m = 2
$$

Comparing 1 and 3, $[\ce{A}]$ is constant and $[\ce{B}]$ doubles:

$$
\frac{r_3}{r_1} = \frac{4.0\times10^{-3}}{2.0\times10^{-3}} = 2
= 2^{n} \qquad\Longrightarrow\qquad n = 1
$$

$$
\text{rate} = k[\ce{A}]^{2}[\ce{B}]
$$

$$
k = \frac{r}{[\ce{A}]^{2}[\ce{B}]}
= \frac{2.0\times10^{-3}}{(0.10)^{2}(0.10)}
= 2.0\ \text{dm}^{6}\ \text{mol}^{-2}\ \text{s}^{-1}
$$

**Answer.** Second order in $\ce{A}$, first order in $\ce{B}$, third order overall;
$k = 2.0\ \text{dm}^{6}\ \text{mol}^{-2}\ \text{s}^{-1}$.

**Check.** Substituting experiment 2, $k(0.20)^{2}(0.10) = 2.0\times10^{-3}$, which
reproduces the measured rate.

**Where marks are lost.** Reading the orders from the coefficients of the equation;
giving $k$ without units or with the units of a first-order constant.

### 32. Half-life and remaining fraction — [Ch. 9]

**Strategy.** Use the first-order integrated law and $t_{1/2} = \ln 2/k$.

**Working.**

$$
t_{1/2} = \frac{\ln 2}{k} = \frac{0.6931}{1.20\times10^{-3}\ \text{s}^{-1}}
= 5.78\times10^{2}\ \text{s}
$$

$$
\ln\frac{[\ce{A}]}{[\ce{A}]_0} = -kt = -(1.20\times10^{-3})(2000) = -2.400
$$

$$
\frac{[\ce{A}]}{[\ce{A}]_0} = e^{-2.400} = 9.07\times10^{-2}
$$

**Answer.** $t_{1/2} = 578\ \text{s}$ (9.63 min); $9.07\,\%$ remains after
$2000\ \text{s}$.

**Check.** $2000\ \text{s}$ is $3.46$ half-lives, and
$(1/2)^{3.46} = 0.091$, consistent.

**Where marks are lost.** Using $t_{1/2} = 1/(k[\ce{A}]_0)$, which applies to second
order; treating the percentage remaining as a concentration without dividing by
$[\ce{A}]_0$.

### 33. Equilibrium concentrations for the hydrogen–iodine system — [Ch. 10]

**Strategy.** Build an ICE table with one extent variable, substitute into $K_c$, and
take the positive root.

**Working.**

| | $\ce{H2}$ | $\ce{I2}$ | $\ce{HI}$ |
|---|---|---|---|
| **I** | 0.500 | 0.500 | 0 |
| **C** | $-x$ | $-x$ | $+2x$ |
| **E** | $0.500-x$ | $0.500-x$ | $2x$ |

$$
K_c = \frac{(2x)^{2}}{(0.500-x)^{2}} = 54.6
$$

$$
\frac{2x}{0.500-x} = \sqrt{54.6} = 7.389
$$

$$
2x = 7.389(0.500 - x) = 3.695 - 7.389x
\qquad\Longrightarrow\qquad
9.389x = 3.695
$$

$$
x = 0.3935\ \text{mol dm}^{-3}
$$

$$
[\ce{HI}] = 2x = 0.787\ \text{mol dm}^{-3}, \qquad
[\ce{H2}] = [\ce{I2}] = 0.500 - 0.3935 = 0.107\ \text{mol dm}^{-3}
$$

**Answer.** $[\ce{HI}] = 0.787$, $[\ce{H2}] = [\ce{I2}] = 0.107\ \text{mol dm}^{-3}$.

**Check.** Substituting back, $(0.787)^{2}/(0.107)^{2} = 54.1$, within rounding of 54.6.

**Where marks are lost.** Writing the change in $\ce{HI}$ as $x$ rather than $2x$;
using initial concentrations in $K_c$; discarding the physically meaningful root.

### 34. Reaction quotient and the effect of temperature — [Ch. 10]

**Strategy.** Evaluate $Q_c$ with the instantaneous concentrations and compare it with
$K_c$; then use the enthalpy sign to decide the effect of temperature on $K$.

**Working.**

$$
\ce{N2(g) + 3H2(g) <=> 2NH3(g)}
$$

$$
Q_c = \frac{[\ce{NH3}]^{2}}{[\ce{N2}][\ce{H2}]^{3}}
= \frac{(0.0500)^{2}}{(0.200)(0.300)^{3}}
= \frac{2.50\times10^{-3}}{5.40\times10^{-3}} = 0.463
$$

$Q_c < K_c$, so the reaction proceeds to the right, forming more ammonia.

**Answer.** $Q_c = 0.463$; the net change is towards products; because the forward
reaction is exothermic, raising the temperature decreases $K_c$ and shifts the
equilibrium to the left.

**Check.** The magnitude is close to $K_c$, so the composition is near equilibrium and
the shift will be modest.

**Where marks are lost.** Inverting the expression for $Q_c$; saying that a catalyst
would change $K_c$; confusing "shift left" with "decrease in rate".

### 35. Exact pH of a weak acid — [Ch. 11]

**Strategy.** Test the small-$x$ approximation first; if $x$ exceeds about 5 % of $c$,
solve the quadratic.

**Working.**

$$
\ce{HF(aq) + H2O(l) <=> H3O+(aq) + F-(aq)}
$$

Approximation:

$$
[\ce{H3O+}] \approx \sqrt{K_a c} = \sqrt{(6.8\times10^{-4})(0.0500)}
= \sqrt{3.40\times10^{-5}} = 5.83\times10^{-3}\ \text{mol dm}^{-3}
$$

The fraction ionised is $5.83\times10^{-3}/0.0500 = 11.7\,\%$, far above 5 %, so the
approximation is not acceptable. Exact treatment with $x = [\ce{H3O+}]$:

$$
K_a = \frac{x^{2}}{c-x}
\qquad\Longrightarrow\qquad
x^{2} + K_a x - K_a c = 0
$$

$$
x = \frac{-6.8\times10^{-4} + \sqrt{(6.8\times10^{-4})^{2} + 4(6.8\times10^{-4})(0.0500)}}{2}
$$

$$
x = \frac{-6.8\times10^{-4} + \sqrt{1.365\times10^{-4}}}{2}
= \frac{-6.8\times10^{-4} + 1.168\times10^{-2}}{2}
= 5.50\times10^{-3}
$$

$$
\mathrm{pH} = -\log_{10}(5.50\times10^{-3}) = 2.26, \qquad
\alpha = \frac{5.50\times10^{-3}}{0.0500} \times 100\,\% = 11.0\,\%
$$

**Answer.** $\mathrm{pH} = 2.26$; percentage ionisation $11.0\,\%$ (3 s.f.).

**Check.** The exact value is 6 % lower than the approximate one, which is the expected
direction: neglecting $x$ in the denominator overestimates the ionisation.

**Where marks are lost.** Using the approximation without the 5 % test; reporting pH to
four figures from a three-figure $K_a$.

### 36. Solubility of lead(II) iodide — [Ch. 13]

**Strategy.** Write $K_{sp}$ in terms of $s$ for a 1:2 salt, then solve for $s$ and
convert to mass concentration.

**Working.**

$$
\ce{PbI2(s) <=> Pb^2+(aq) + 2I-(aq)}
$$

$$
K_{sp} = [\ce{Pb^2+}][\ce{I-}]^{2} = (s)(2s)^{2} = 4s^{3}
$$

$$
s = \sqrt[3]{\frac{K_{sp}}{4}} = \sqrt[3]{\frac{7.1\times10^{-9}}{4}}
= \sqrt[3]{1.775\times10^{-9}} = 1.21\times10^{-3}\ \text{mol dm}^{-3}
$$

$$
\rho_{\text{solute}} = (1.21\times10^{-3}\ \text{mol dm}^{-3})(461.0\ \text{g mol}^{-1})
= 0.558\ \text{g dm}^{-3}
$$

**Answer.** $s = 1.21\times10^{-3}\ \text{mol dm}^{-3}$;
$0.558\ \text{g dm}^{-3}$ (3 s.f.).

**Check.** $[\ce{I-}]$ must be twice $[\ce{Pb^2+}]$, and
$(1.21\times10^{-3})(2.42\times10^{-3})^{2} = 7.1\times10^{-9}$, as required.

**Where marks are lost.** Using $s = \sqrt{K_{sp}}$ for a 1:2 salt; omitting the factor
4 in $4s^{3}$.

---

## Part D — Advanced problems

### 37. The thermite reaction: limiting reactant, yield and mass balance — [Ch. 2]

**Strategy.** Compare quotients, convert the limiting amount into each product, then
close the mass balance as a check.

**Working.**

$$
\ce{Fe2O3(s) + 2Al(s) -> 2Fe(l) + Al2O3(s)}
$$

$$
n(\ce{Fe2O3}) = \frac{25.0}{159.69} = 0.15655\ \text{mol}, \qquad
q(\ce{Fe2O3}) = 0.15655\ \text{mol}
$$

$$
n(\ce{Al}) = \frac{10.0}{26.982} = 0.37062\ \text{mol}, \qquad
q(\ce{Al}) = \frac{0.37062}{2} = 0.18531\ \text{mol}
$$

Iron(III) oxide has the smaller quotient and is limiting.

$$
n(\ce{Fe}) = 2(0.15655) = 0.31311\ \text{mol}, \qquad
m(\ce{Fe}) = (0.31311)(55.845) = 17.49\ \text{g}
$$

$$
\text{percentage yield} = \frac{15.2}{17.49} \times 100\,\% = 86.9\,\%
$$

$$
n(\ce{Al2O3}) = 0.15655\ \text{mol}, \qquad
m(\ce{Al2O3}) = (0.15655)(101.961) = 15.96\ \text{g}
$$

$$
n(\ce{Al})_{\text{consumed}} = 2(0.15655) = 0.31311\ \text{mol}, \qquad
m = (0.31311)(26.982) = 8.45\ \text{g}
$$

$$
m(\ce{Al})_{\text{remaining}} = 10.0 - 8.45 = 1.55\ \text{g}
$$

**Answer.** (a) $\ce{Fe2O3}$ is limiting; (b) $17.5\ \text{g}$ Fe;
(c) $86.9\,\%$; (d) $16.0\ \text{g}$ $\ce{Al2O3}$ and $1.55\ \text{g}$ Al remaining.

**Check.** Mass balance: $25.0 + 10.0 = 35.0\ \text{g}$ of reactants;
$17.49 + 15.96 + 1.55 = 35.00\ \text{g}$ of products plus excess, as required.

**Where marks are lost.** Comparing moles (which would wrongly make aluminium
limiting); calculating the yield against the aluminium; forgetting that the aluminium
remaining must be subtracted at the stoichiometric ratio, not simply as
$10.0 - 15.2$.

### 38. Concentrated sulfuric acid: molarity, dilution and titration — [Ch. 3]

**Strategy.** Convert mass percentage and density to a molarity for $1\ \text{dm}^{3}$
of solution, then apply $c_1V_1 = c_2V_2$ and the 1:2 stoichiometry.

**Working.** (a) $1.000\ \text{dm}^{3}$ of solution has mass $1840\ \text{g}$, of which
$0.980 \times 1840 = 1803\ \text{g}$ is $\ce{H2SO4}$:

$$
n = \frac{1803\ \text{g}}{98.079\ \text{g mol}^{-1}} = 18.385\ \text{mol}
\qquad\Longrightarrow\qquad
c = 18.4\ \text{mol dm}^{-3}
$$

(b)

$$
V_1 = \frac{c_2V_2}{c_1}
= \frac{(0.500\ \text{mol dm}^{-3})(500.0\ \text{cm}^{3})}{18.385\ \text{mol dm}^{-3}}
= 13.6\ \text{cm}^{3}
$$

(c) In $25.0\ \text{cm}^{3}$ of $0.500\ \text{mol dm}^{-3}$ acid:

$$
n(\ce{H2SO4}) = (0.500)(0.0250) = 1.25\times10^{-2}\ \text{mol}
$$

$$
n(\ce{NaOH}) = 2(1.25\times10^{-2}) = 2.50\times10^{-2}\ \text{mol}
$$

$$
V(\ce{NaOH}) = \frac{2.50\times10^{-2}\ \text{mol}}{0.250\ \text{mol dm}^{-3}}
= 0.100\ \text{dm}^{3}
$$

**Answer.** (a) $18.4\ \text{mol dm}^{-3}$; (b) $13.6\ \text{cm}^{3}$;
(c) $100\ \text{cm}^{3}$ of $0.250\ \text{mol dm}^{-3}$ $\ce{NaOH}$.

**Check.** The dilution factor is $500/13.6 = 36.8$, and
$18.4/36.8 = 0.50$, as intended. The base volume is twice the acid volume because the
base is half as concentrated and the acid is diprotic.

**Where marks are lost.** Forgetting the density, which makes the molarity 1000 times
smaller if grams are mistaken for kilograms; adding water to acid rather than acid to
water is a safety error as well as a chemistry one.

### 39. Carbon dioxide: ideal gas against van der Waals — [Ch. 4]

**Strategy.** Evaluate $pV = nRT$ first, then the two corrections, then express the
result as a compressibility factor.

**Working.** (a)

$$
p_{\text{ideal}} = \frac{nRT}{V}
= \frac{(1.00)(8.314)(300)}{1.00\times10^{-3}}
= 2.494\times10^{6}\ \text{Pa} = 2494\ \text{kPa}
$$

(b)

$$
\left(p + \frac{an^{2}}{V^{2}}\right)(V - nb) = nRT
$$

$$
p = \frac{nRT}{V - nb} - \frac{an^{2}}{V^{2}}
= \frac{(1.00)(8.314)(300)}{1.00\times10^{-3} - 4.27\times10^{-5}}
- \frac{(0.364)(1.00)^{2}}{(1.00\times10^{-3})^{2}}
$$

$$
p = 2.606\times10^{6} - 3.64\times10^{5} = 2.241\times10^{6}\ \text{Pa}
= 2241\ \text{kPa}
$$

(c)

$$
Z = \frac{pV}{nRT} = \frac{2.241\times10^{6}}{2.494\times10^{6}} = 0.899
$$

**Answer.** (a) $2494\ \text{kPa}$; (b) $2241\ \text{kPa}$;
(c) $Z = 0.899 < 1$, so attractive forces dominate over the excluded-volume effect.

**Check.** At $1\ \text{dm}^{3}\ \text{mol}^{-1}$ carbon dioxide is about 45 times denser
than at STP, so a 10 % deviation is expected; the sign of $Z - 1$ is negative, as it is
for most gases at moderate pressure.

**Where marks are lost.** Using $V$ in $\text{dm}^{3}$ with $a$ in
$\text{Pa m}^{6}\ \text{mol}^{-2}$; omitting the $n^{2}$ and $n$ factors in the
correction terms.

### 40. Hydrogen bonding in water and hydrogen sulfide — [Ch. 5]

**Strategy.** Compare the intermolecular forces available, then convert the enthalpy of
vaporisation into an energy per hydrogen bond.

**Working.** (a) Oxygen is more electronegative and much smaller than sulfur, so the
O–H bond is strongly polar and the oxygen lone pairs can interact with a neighbouring
O–H hydrogen at short range. Water therefore forms a three-dimensional hydrogen-bonded
network, whereas $\ce{H2S}$ has only weak dipole–dipole and dispersion interactions;
sulfur is also a poor hydrogen-bond acceptor because its lone pairs are diffuse.

(b) Each molecule makes 3.4 hydrogen bonds, and each bond is shared between two
molecules, so the number of bonds per mole of molecules is $3.4/2 = 1.7\ \text{mol}$:

$$
\Delta H_{\text{H-bond}} \approx \frac{40.7\ \text{kJ mol}^{-1}}{1.7}
= 23.9\ \text{kJ mol}^{-1}
$$

(c) The estimate is an upper bound because $\Delta H_{\text{vap}}$ also includes the
dispersion and dipole–dipole contributions and the work of expansion against the
atmosphere; dividing the whole enthalpy by the number of hydrogen bonds therefore
attributes too much energy to each bond.

**Answer.** (a) Hydrogen bonding in water, absent in $\ce{H2S}$;
(b) $\approx 24\ \text{kJ mol}^{-1}$ per hydrogen bond; (c) the value is an upper bound
because non-hydrogen-bond contributions are included in $\Delta H_{\text{vap}}$.

**Check.** Typical hydrogen-bond enthalpies are 10–40 $\text{kJ mol}^{-1}$, so
$24\ \text{kJ mol}^{-1}$ is plausible; it is about 5 % of a covalent O–H bond, which is
why hydrogen bonds break reversibly on heating.

**Where marks are lost.** Forgetting to halve the bond count, which doubles the answer;
claiming that $\ce{H2S}$ hydrogen bonds because sulfur is in the same group.

### 41. Methane combustion: bond enthalpies and internal energy — [Ch. 8]

**Strategy.** Count bonds broken and formed for the gaseous reaction, compare with the
calorimetric value, then convert $\Delta H$ to $\Delta U$.

**Working.** (a)

$$
\ce{CH4(g) + 2O2(g) -> CO2(g) + 2H2O(g)}
$$

Bonds broken:

$$
4\,E(\ce{C-H}) + 2\,E(\ce{O=O}) = 4(414) + 2(498) = 2652\ \text{kJ mol}^{-1}
$$

Bonds formed:

$$
2\,E(\ce{C=O}) + 4\,E(\ce{O-H}) = 2(799) + 4(463) = 3450\ \text{kJ mol}^{-1}
$$

$$
\Delta H \approx 2652 - 3450 = -798\ \text{kJ mol}^{-1}
$$

(b) The calorimetric value for gaseous water is $-802.3\ \text{kJ mol}^{-1}$; the
difference is $4\ \text{kJ mol}^{-1}$, or 0.5 %. Mean bond enthalpies are averages over
many compounds, and the C–H bonds in methane are not identical to the average C–H bond,
so the estimate is good but not exact.

(c)

$$
\Delta n_{\text{g}} = 1 - 3 = -2
$$

$$
\Delta U^{\circ} = \Delta H^{\circ} - \Delta n_{\text{g}}RT
= -890.3 - (-2)(8.314)(298.15)/1000
= -890.3 + 4.96 = -885.3\ \text{kJ mol}^{-1}
$$

**Answer.** (a) $-798\ \text{kJ mol}^{-1}$; (b) within 0.5 % of $-802.3\ \text{kJ mol}^{-1}$,
which is the precision expected of mean bond enthalpies; (c)
$\Delta U^{\circ} = -885.3\ \text{kJ mol}^{-1}$.

**Check.** $\Delta U$ is less negative than $\Delta H$ because the system contracts
($\Delta n_{\text{g}} < 0$) and the surroundings do work on it.

**Where marks are lost.** Using liquid water in a bond-enthalpy calculation, which
mixes two different data sets; using $\Delta n_{\text{g}} = +2$.

### 42. Activation energy and pre-exponential factor — [Ch. 9]

**Strategy.** Use the two-point Arrhenius equation for $E_a$, then one point to obtain
$A$.

**Working.**

$$
\ln\!\left(\frac{k_2}{k_1}\right) = -\frac{E_a}{R}
\left(\frac{1}{T_2} - \frac{1}{T_1}\right)
$$

$$
\ln\!\left(\frac{1.10\times10^{-2}}{2.50\times10^{-3}}\right) = \ln(4.40) = 1.482
$$

$$
\frac{1}{300} - \frac{1}{320} = 3.333\times10^{-3} - 3.125\times10^{-3}
= 2.083\times10^{-4}\ \text{K}^{-1}
$$

$$
E_a = \frac{(8.314)(1.482)}{2.083\times10^{-4}} = 5.91\times10^{4}\ \text{J mol}^{-1}
$$

$$
A = k_1\exp\!\left(\frac{E_a}{RT_1}\right)
= (2.50\times10^{-3})\exp\!\left(\frac{5.91\times10^{4}}{(8.314)(300)}\right)
$$

$$
A = (2.50\times10^{-3})\exp(23.71) = 4.93\times10^{7}\ \text{s}^{-1}
$$

**Answer.** $E_a = 59.1\ \text{kJ mol}^{-1}$;
$A = 4.9\times10^{7}\ \text{s}^{-1}$.

**Check.** A 20 K rise increases $k$ by a factor of 4.4; the rule of thumb that a
10 K rise doubles the rate predicts $2^{2} = 4$, consistent.

**Where marks are lost.** Sign errors in the temperature difference; quoting $A$ without
units; assuming $E_a$ is in $\text{kJ}$ when $R$ is in $\text{J}$.

### 43. Dinitrogen tetroxide dissociation: $K_c$ and $K_p$ — [Ch. 10]

**Strategy.** Use the ICE table to find both equilibrium concentrations, evaluate
$K_c$, then convert with $K_p = K_c(RT)^{\Delta n}$ using bar-based $R$.

**Working.**

| | $\ce{N2O4}$ | $\ce{NO2}$ |
|---|---|---|
| **I** | 0.100 | 0 |
| **C** | $-0.0600$ | $+0.120$ |
| **E** | 0.0400 | 0.120 |

$$
K_c = \frac{[\ce{NO2}]^{2}}{[\ce{N2O4}]} = \frac{(0.120)^{2}}{0.0400} = 0.360
$$

$$
\Delta n = 2 - 1 = +1
$$

$$
K_p = K_c(RT)^{\Delta n}
= (0.360)(0.08314\ \text{L bar K}^{-1}\ \text{mol}^{-1})(350\ \text{K})
= 10.5\ \text{bar}
$$

**Answer.** $K_c = 0.360$; $K_p = 10.5\ \text{bar}$ at $350\ \text{K}$.

**Check.** $K_p > K_c$ because the reaction produces more gas moles, so the pressure
factor must be greater than one; $RT = 29.1\ \text{bar}$ at 350 K, consistent.

**Where marks are lost.** Using $R = 8.314$ with litres and bar, which gives a factor of
100 wrong; forgetting that the amount dissociated is $0.100 - 0.0400$, not $0.0400$.

### 44. Buffer response to added strong acid — [Ch. 11]

**Strategy.** Use the Henderson–Hasselbalch equation before and after addition, treating
the added strong acid as converting base into acid stoichiometrically.

**Working.** (a)

$$
\mathrm{pH} = \mathrm{p}K_a + \log_{10}\frac{[\ce{A-}]}{[\ce{HA}]}
= 4.76 + \log_{10}\frac{0.100}{0.100} = 4.76
$$

(b) $0.0100\ \text{mol}$ of $\ce{HCl}$ reacts with $0.0100\ \text{mol}$ of
$\ce{A-}$:

$$
[\ce{HA}] = 0.100 + 0.0100 = 0.110\ \text{mol dm}^{-3}, \qquad
[\ce{A-}] = 0.100 - 0.0100 = 0.0900\ \text{mol dm}^{-3}
$$

$$
\mathrm{pH} = 4.76 + \log_{10}\frac{0.0900}{0.110} = 4.76 - 0.087 = 4.67
$$

(c) In $1.00\ \text{dm}^{3}$ of water, $0.0100\ \text{mol}$ of $\ce{HCl}$ gives
$[\ce{H3O+}] = 0.0100\ \text{mol dm}^{-3}$:

$$
\mathrm{pH} = -\log_{10}(0.0100) = 2.00
$$

**Answer.** (a) 4.76; (b) 4.67; (c) 2.00. The buffer changes by 0.09 of a pH unit,
whereas the same amount of acid in water changes the pH by 5.00 units.

**Check.** The buffer ratio changed from 1.00 to 0.818, and
$\log_{10}(0.818) = -0.087$, exactly the shift observed.

**Where marks are lost.** Adding the acid to $[\ce{HA}]$ but forgetting to subtract it
from $[\ce{A-}]$; assuming the pH falls to that of the strong acid.

### 45. Daniell cell: Gibbs energy and Faraday calculation — [Ch. 12]

**Strategy.** Use $\Delta G^{\circ} = -zFE^{\circ}$ with $z = 2$, then convert charge to
amount of zinc.

**Working.** (a)

$$
\ce{Zn(s) + Cu^2+(aq) -> Zn^2+(aq) + Cu(s)}
$$

$$
z = 2, \qquad
\Delta G^{\circ} = -zFE^{\circ} = -(2)(96\,485)(1.10)
= -2.12\times10^{5}\ \text{J mol}^{-1}
$$

(b)

$$
Q = It = (0.500\ \text{A})(2.00 \times 3600\ \text{s}) = 3600\ \text{C}
$$

$$
n(\ce{Zn}) = \frac{Q}{zF} = \frac{3600}{(2)(96\,485)} = 1.866\times10^{-2}\ \text{mol}
$$

$$
m(\ce{Zn}) = (1.866\times10^{-2})(65.38) = 1.22\ \text{g}
$$

**Answer.** (a) $\Delta G^{\circ} = -212\ \text{kJ mol}^{-1}$;
(b) $m(\ce{Zn}) = 1.22\ \text{g}$.

**Check.** $2F = 192\,970\ \text{C mol}^{-1}$, so $3600\ \text{C}$ corresponds to
$1.87\times10^{-2}\ \text{mol}$; the mass follows directly.

**Where marks are lost.** Using $z = 1$; forgetting that $\Delta G^{\circ}$ is per mole
of reaction as written, in which two electrons are transferred.

### 46. Precipitation of silver chloride from mixed solutions — [Ch. 13]

**Strategy.** Account for dilution on mixing, calculate $Q$, compare with $K_{sp}$, then
use the equilibrium expression with the common ion in excess.

**Working.** (a) Mixing equal volumes halves each concentration:

$$
[\ce{Ag+}]_0 = [\ce{Cl-}]_0 = 0.00500\ \text{mol dm}^{-3}
$$

$$
Q = [\ce{Ag+}][\ce{Cl-}] = (0.00500)(0.00500) = 2.5\times10^{-5}
$$

(b) $Q = 2.5\times10^{-5} \gg K_{sp} = 1.8\times10^{-10}$, so precipitation occurs.

(c) Chloride is in large excess relative to the tiny amount that precipitates, so

$$
[\ce{Ag+}] = \frac{K_{sp}}{[\ce{Cl-}]} = \frac{1.8\times10^{-10}}{0.00500}
= 3.6\times10^{-8}\ \text{mol dm}^{-3}
$$

$$
\text{fraction removed} = \frac{0.00500 - 3.6\times10^{-8}}{0.00500} = 0.999\,993
$$

**Answer.** (a) $Q = 2.5\times10^{-5}$; (b) a precipitate forms;
(c) $[\ce{Ag+}] = 3.6\times10^{-8}\ \text{mol dm}^{-3}$, so $99.9993\,\%$ of the silver
is removed.

**Check.** The mass balance for chloride is unchanged to four figures, so treating
$[\ce{Cl-}]$ as $0.00500$ is self-consistent.

**Where marks are lost.** Forgetting the dilution factor of two; using $K_{sp}$ as if
it were a concentration; reporting "all the silver precipitates" without a number.

---

## Part E — Calculation problems

### 47. Molar mass and water content of a hydrate — [Ch. 1]

**Strategy.** Sum the anhydrous salt and seven water units, then take the water
fraction.

**Working.**

$$
M(\ce{MgSO4}) = 24.305 + 32.06 + 4(15.999) = 120.365\ \text{g mol}^{-1}
$$

$$
7M(\ce{H2O}) = 7(18.015) = 126.105\ \text{g mol}^{-1}
$$

$$
M(\ce{MgSO4.7H2O}) = 120.365 + 126.105 = 246.470\ \text{g mol}^{-1}
$$

$$
w(\ce{H2O}) = \frac{126.105}{246.470} \times 100\,\% = 51.16\,\%
$$

$$
m(\ce{MgSO4}) = 10.0\ \text{g} \times \frac{120.365}{246.470} = 4.88\ \text{g}
$$

**Answer.** $M = 246.47\ \text{g mol}^{-1}$; $51.2\,\%$ water;
$4.88\ \text{g}$ of anhydrous salt from $10.0\ \text{g}$ of hydrate.

**Check.** The mass lost on heating is $5.12\ \text{g}$, which is
$5.12/18.015 = 0.284\ \text{mol}$, and $10.0/246.47 = 0.0406\ \text{mol}$ of hydrate;
$0.284/0.0406 = 7.0$, the correct hydration number.

**Where marks are lost.** Omitting the seven waters from the molar mass; treating the
percentage of water as the mass of anhydrous salt.

### 48. Atom economy and yield in fermentation — [Ch. 2]

**Strategy.** Atom economy uses the balanced equation and molar masses; yield uses the
actual and theoretical masses.

**Working.**

$$
\ce{C6H12O6(aq) -> 2C2H5OH(aq) + 2CO2(g)}
$$

(a)

$$
\text{AE} = \frac{2M(\ce{C2H5OH})}{M(\ce{C6H12O6})} \times 100\,\%
= \frac{2(46.069)}{180.156} \times 100\,\% = 51.1\,\%
$$

(b)

$$
n(\ce{C6H12O6}) = \frac{100\ \text{g}}{180.156\ \text{g mol}^{-1}} = 0.5551\ \text{mol}
$$

$$
n(\ce{C2H5OH})_{\text{theoretical}} = 2(0.5551) = 1.110\ \text{mol}
$$

$$
m_{\text{theoretical}} = (1.110)(46.069) = 51.1\ \text{g}
$$

$$
\text{percentage yield} = \frac{40.0}{51.1} \times 100\,\% = 78.2\,\%
$$

**Answer.** Atom economy $51.1\,\%$; yield $78.2\,\%$.

**Check.** The theoretical mass equals the atom-economy mass by construction, because
$100\ \text{g}$ of glucose was used; the two answers must therefore be consistent, and
they are.

**Where marks are lost.** Using the mass of carbon dioxide as the desired product;
dividing by the total mass of products rather than reactants in the atom economy.

### 49. Molality and mole fraction — [Ch. 3]

**Strategy.** Molality uses the mass of solvent in kilograms; mole fraction uses
amounts of both components.

**Working.**

$$
n(\ce{NaCl}) = \frac{20.0}{58.44} = 0.3422\ \text{mol}
$$

$$
n(\ce{H2O}) = \frac{180}{18.015} = 9.992\ \text{mol}
$$

$$
b = \frac{0.3422\ \text{mol}}{0.180\ \text{kg}} = 1.90\ \text{mol kg}^{-1}
$$

$$
x(\ce{NaCl}) = \frac{0.3422}{0.3422 + 9.992} = 0.0331
$$

**Answer.** $b = 1.90\ \text{mol kg}^{-1}$; $x(\ce{NaCl}) = 0.0331$.

**Check.** Molality exceeds molarity here because $20\ \text{g}$ of salt in
$180\ \text{g}$ of water gives a solution whose volume is about $0.19\ \text{dm}^{3}$,
so $c \approx 1.8\ \text{mol dm}^{-3}$; the two are of the same order, as expected.

**Where marks are lost.** Using the mass of solution instead of solvent; using
$20.0\ \text{g}$ rather than $0.180\ \text{kg}$ in the denominator.

### 50. Root-mean-square speed of nitrogen — [Ch. 4]

**Strategy.** Use $u_{\text{rms}} = \sqrt{3RT/M}$ with $M$ in $\text{kg mol}^{-1}$.

**Working.**

$$
M = 28.014\ \text{g mol}^{-1} = 2.8014\times10^{-2}\ \text{kg mol}^{-1}
$$

$$
u_{\text{rms}} = \sqrt{\frac{3RT}{M}}
= \sqrt{\frac{3(8.314)(300)}{2.8014\times10^{-2}}}
= \sqrt{2.671\times10^{5}}
= 5.17\times10^{2}\ \text{m s}^{-1}
$$

**Answer.** $u_{\text{rms}} = 517\ \text{m s}^{-1}$ (3 s.f.).

**Check.** The speed of sound in nitrogen at 300 K is about
$353\ \text{m s}^{-1}$, and $u_{\text{rms}}$ is predicted to be about
$\sqrt{3/2}$ times larger, which it is.

**Where marks are lost.** Leaving $M$ in $\text{g mol}^{-1}$, which makes the answer
$\sqrt{1000}$ too large; using $T$ in Celsius.

### 51. Kirchhoff's law for the Haber reaction — [Ch. 8]

**Strategy.** Integrate the constant-$\Delta C_p$ form over the temperature interval.

**Working.**

$$
\Delta H(T_2) = \Delta H(T_1) + \Delta C_p(T_2 - T_1)
$$

$$
\Delta H(700) = -92.4\ \text{kJ mol}^{-1}
+ (-60\times10^{-3}\ \text{kJ K}^{-1}\ \text{mol}^{-1})(700 - 298)\ \text{K}
$$

$$
\Delta H(700) = -92.4 - 24.1 = -116.5\ \text{kJ mol}^{-1}
$$

**Answer.** $\Delta H^{\circ}(700\ \text{K}) = -117\ \text{kJ mol}^{-1}$.

**Check.** The reaction is exothermic and $\Delta C_p$ is negative, so the magnitude
must increase with temperature; $-116.5$ is more negative than $-92.4$, as required.

**Where marks are lost.** Using $\Delta C_p$ in $\text{J}$ with $\Delta H$ in
$\text{kJ}$; reversing the temperature difference.

### 52. Converting $K_c$ to $K_p$ for ammonia synthesis — [Ch. 10]

**Strategy.** Identify $\Delta n$ from the gaseous species only, then apply
$K_p = K_c(RT)^{\Delta n}$ with $R = 0.08314\ \text{L bar K}^{-1}\ \text{mol}^{-1}$.

**Working.**

$$
\ce{N2(g) + 3H2(g) <=> 2NH3(g)}
$$

$$
\Delta n = 2 - (1 + 3) = -2
$$

$$
K_p = K_c(RT)^{-2} = \frac{0.500}{[(0.08314)(800)]^{2}}
= \frac{0.500}{(66.51)^{2}} = \frac{0.500}{4424}
= 1.13\times10^{-4}
$$

**Answer.** $K_p = 1.1\times10^{-4}\ \text{bar}^{-2}$ at $800\ \text{K}$.

**Check.** Because $\Delta n < 0$, $K_p$ must be smaller than $K_c$, and it is smaller by
a factor of about $4.4\times10^{3}$.

**Where marks are lost.** Using $R = 8.314$ with litres and bars; taking $\Delta n = -4$
by counting nitrogen as four species.

### 53. Mass of silver deposited by electrolysis — [Ch. 12]

**Strategy.** Convert current and time to charge, then charge to amount with $z = 1$ for
$\ce{Ag+}$.

**Working.**

$$
Q = It = (2.50\ \text{A})(1.50 \times 3600\ \text{s}) = 1.35\times10^{4}\ \text{C}
$$

$$
n(\ce{Ag}) = \frac{Q}{zF} = \frac{1.35\times10^{4}}{(1)(96\,485)}
= 0.1399\ \text{mol}
$$

$$
m(\ce{Ag}) = (0.1399\ \text{mol})(107.87\ \text{g mol}^{-1}) = 15.1\ \text{g}
$$

**Answer.** $m(\ce{Ag}) = 15.1\ \text{g}$.

**Check.** One mole of electrons deposits one mole of silver; $13\,500\ \text{C}$ is
about $0.14$ of a faraday, so $0.14 \times 108\ \text{g} \approx 15\ \text{g}$.

**Where marks are lost.** Using $z = 2$ for silver; failing to convert hours to
seconds, which gives an answer 3600 times too small.

### 54. Solubility of iron(III) hydroxide — [Ch. 13]

**Strategy.** For a 1:3 salt, $K_{sp} = 27s^{4}$; solve for $s$, then convert to mass
concentration.

**Working.**

$$
\ce{Fe(OH)3(s) <=> Fe^3+(aq) + 3OH-(aq)}
$$

$$
K_{sp} = (s)(3s)^{3} = 27s^{4}
$$

$$
s = \sqrt[4]{\frac{K_{sp}}{27}} = \sqrt[4]{\frac{2.8\times10^{-39}}{27}}
= \sqrt[4]{1.037\times10^{-40}} = 1.01\times10^{-10}\ \text{mol dm}^{-3}
$$

$$
\rho = (1.01\times10^{-10})(106.87) = 1.08\times10^{-8}\ \text{g dm}^{-3}
= 1.08\times10^{-5}\ \text{mg dm}^{-3}
$$

**Answer.** $s = 1.01\times10^{-10}\ \text{mol dm}^{-3}$, equivalent to
$1.08\times10^{-5}\ \text{mg dm}^{-3}$ (about $10.8\ \text{ng dm}^{-3}$).

**Check.** $[\ce{OH-}] = 3s = 3.03\times10^{-10}$, and
$(1.01\times10^{-10})(3.03\times10^{-10})^{3} = 2.8\times10^{-39}$, as required.

**Where marks are lost.** Using $4s^{3}$ from the 1:2 formula; taking a square root
instead of a fourth root.

---

## Part F — Multiple-choice self-check

### 55. Atoms in one gram — [Ch. 1]

**Strategy.** Convert each mass to amount, multiply by the number of atoms per entity,
and compare the four results.

**Answer.** **A.** $1.00\ \text{g}$ of $\ce{H2}$ contains
$1.00/2.016 = 0.496\ \text{mol}$ of molecules, hence $0.992\ \text{mol}$ of atoms. The
other samples contain $0.250\ \text{mol}$ (He), $0.0833\ \text{mol}$ (C) and
$0.0625\ \text{mol}$ ($\ce{O2}$, two atoms per molecule), all far smaller.

**Check.** $1.00\ \text{g}$ of $\ce{H2}$ corresponds to about $0.5\ \text{mol}$ of
molecules and hence about $1\ \text{mol}$ of atoms, more than any other sample of
$1.00\ \text{g}$.

**Why the best distractor is wrong.** Option B is tempting because helium has the
smallest molar mass of any atom, so $1\ \text{g}$ contains the largest number of
*particles* for a monatomic substance: $0.250\ \text{mol}$. But hydrogen gas is
diatomic and has a molar mass of $2.016\ \text{g mol}^{-1}$, half that of helium, so
$1\ \text{g}$ of $\ce{H2}$ contains twice as many molecules as $1\ \text{g}$ of He
contains atoms, and four times as many atoms.

### 56. Square-planar geometry — [Ch. 6]

**Strategy.** Count electron domains, then place the lone pairs in the positions that
minimise repulsion.

**Answer.** **B.** $\ce{XeF4}$ has four bonding pairs and two lone pairs, six electron
domains, and an octahedral electron-domain geometry. Placing the two lone pairs trans
leaves the four fluorines at the corners of a square.

**Check.** Only $\ce{XeF4}$ has two lone pairs on an octahedral centre, and only a trans
arrangement of those pairs leaves the four ligands coplanar.

**Why the best distractor is wrong.** $\ce{SF4}$ also has four fluorines, so it looks
similar, but sulfur has only one lone pair and five domains; the lone pair occupies an
equatorial site of a trigonal bipyramid and the molecule is see-saw, not square planar.

### 57. Units of a second-order rate constant — [Ch. 9]

**Strategy.** Write the rate law for overall order two, rearrange for $k$, and cancel
the concentration units.

**Answer.** **C.** For an overall order of two,
$\text{rate} = k[\ce{A}][\ce{B}]$, so
$k = \text{rate}/[\ce{A}][\ce{B}]$ with units
$(\text{mol dm}^{-3}\ \text{s}^{-1})/(\text{mol dm}^{-3})^{2}
= \text{dm}^{3}\ \text{mol}^{-1}\ \text{s}^{-1}$.

**Check.** Substituting the units of option C back into
$v = k[\ce{A}][\ce{B}]$ returns $\text{mol dm}^{-3}\ \text{s}^{-1}$, as a rate must.

**Why the best distractor is wrong.** Option A, $\text{s}^{-1}$, is the unit for a
first-order reaction; it is the most common slip because the numerical value of $k$ is
often quoted without units. Option D belongs to third order.

### 58. pH of ammonium chloride — [Ch. 11]

**Strategy.** Recognise the salt as the conjugate acid of a weak base, then use the
square-root approximation for a weak acid.

**Answer.** **B.** The ammonium ion is the conjugate acid of a weak base, so
$K_a = 5.6\times10^{-10}$ and

$$
[\ce{H3O+}] \approx \sqrt{K_a c} = \sqrt{(5.6\times10^{-10})(0.100)}
= 7.5\times10^{-6}\ \text{mol dm}^{-3}
$$

giving $\mathrm{pH} = 5.13$.

**Check.** The result is below 7, as a salt of a weak base and a strong acid must be,
and it lies two units below the $\mathrm{p}K_a$ of the ammonium ion, consistent with
$[\ce{NH3}] \approx [\ce{H3O+}]$.

**Why the best distractor is wrong.** Option D, 8.87, is the pH of a solution of
ammonia of the same concentration; it results from treating the salt as a base rather
than recognising that the ammonium ion is acidic. Option C, 7.00, ignores hydrolysis
altogether.

### 59. Strongest oxidising agent — [Ch. 12]

**Strategy.** Compare standard reduction potentials; the most positive value marks the
strongest oxidising agent.

**Answer.** **D.** $\ce{F2}$ has the most positive standard reduction potential in the
data sheet, $+2.87\ \text{V}$, so it has the greatest tendency to accept electrons and is
the strongest oxidising agent listed.

**Check.** $\ce{F2}$ oxidises chloride to chlorine and water to oxygen, which is exactly
what its position at the top of the table requires.

**Why the best distractor is wrong.** $\ce{Ag+(aq)}$ at $+0.80\ \text{V}$ is the
strongest of the metal ions listed and will oxidise copper and zinc, so it looks
plausible; but a more positive potential means a stronger oxidant, and
$+2.87 > +0.80$. $\ce{Zn^2+}$ is the weakest oxidant of the four and is easily reduced
only by very strong reductants.

### 60. Common-ion suppression of silver chloride solubility — [Ch. 13]

**Strategy.** Calculate the solubility in pure water and in the common ion, then take
the ratio.

**Answer.** **B.** In pure water $s = \sqrt{K_{sp}} = 1.34\times10^{-5}\ \text{mol dm}^{-3}$.
In $0.100\ \text{mol dm}^{-3}$ chloride,
$s = K_{sp}/[\ce{Cl-}] = 1.8\times10^{-9}\ \text{mol dm}^{-3}$. The ratio is
$1.34\times10^{-5}/1.8\times10^{-9} = 7.5\times10^{3}$, so the solubility falls by about
three and a half orders of magnitude.

**Check.** The suppression factor is $0.100/1.34\times10^{-5} = 7.5\times10^{3}$, the
same number obtained from the ratio of the two solubilities.

**Why the best distractor is wrong.** Option D applies the ratio twice, as though the
solubility depended on the square of the concentration ratio; it is the kind of error
produced by confusing $K_{sp}$ with $s^{2}$ after the common ion has been introduced.
Option C confuses a constant $K_{sp}$ with constant solubility: $K_{sp}$ is constant, but
the solubility is not.

---

## Top ten errors in this level

| # | Error | Why it costs marks | Correct habit |
|---|---|---|---|
| 1 | Using $22.4\ \text{dm}^{3}\ \text{mol}^{-1}$ at $100\ \text{kPa}$ | Wrong standard; the value belongs to $101.325\ \text{kPa}$ | Use $22.71$ at STP and $24.79$ at SATP |
| 2 | Taking mole ratios from formula subscripts | The balanced equation, not the formula, fixes the ratio | Balance first, then read coefficients |
| 3 | Mixing $\text{cm}^{3}$ and $\text{dm}^{3}$ | Answers wrong by factors of 1000 | Convert every volume to $\text{dm}^{3}$ before dividing |
| 4 | Using total pressure for a gas collected over water | Ignores the water vapour contribution | $p_{\text{gas}} = p_{\text{total}} - p_{\ce{H2O}}$ |
| 5 | Reading rate orders from the stoichiometric equation | Orders are experimental, not stoichiometric | Determine orders from initial rates or integrated laws |
| 6 | Substituting initial concentrations into $K$ | $K$ is defined at equilibrium | Build an ICE table and use the E row |
| 7 | Applying $[\ce{H3O+}] = \sqrt{K_a c}$ without a check | Fails when more than about 5 % ionises | Test $x/c$; solve the quadratic if it fails |
| 8 | Using $\mathrm{pH} + \mathrm{pOH} = 14.00$ at any temperature | The sum is $\mathrm{p}K_w$, which depends on $T$ | State 25 °C, or use the $\mathrm{p}K_w$ for that temperature |
| 9 | Ranking solubility by $K_{sp}$ across different stoichiometries | The exponents differ | Convert to molar solubility first |
| 10 | Sign errors in $\Delta H$, $\Delta G$ and electrode potentials | Reverses the meaning of exothermic, spontaneous or galvanic | Write the sign convention beside the equation before substituting |

