# Level 8 — Worked Solutions: Biochemistry

> **Level:** 8 (Biochemistry)
> **Items:** 58
> **Exercise bank:** [`../exercises/level-8-exercises.md`](../exercises/level-8-exercises.md)

Each solution gives the **Strategy** (the kind of problem), the **Working** (symbols
first, then substitution with units), the **Answer** (significant figures and units) and
a **Check** that catches the usual error. Items marked **multi-step** require at least
three dependent decisions; 29 items are so marked. **Where marks are lost** is given
wherever a predictable slip costs credit.

Conventions. Amino-acid $\mathrm{p}K_\mathrm{a}$ values are the standard set used in
Chapter 2; peptide terminal values are model values ($9.60$ for the N-terminus and
$2.34$ for the C-terminus). ATP yields are quoted with their $\mathrm{P/O}$ assumptions,
because the same pathway gives different totals under different proton accounting.
Significant figures are carried through the working and rounded only in the answer.

---

## Part A — Conceptual questions

### 1. The hydrophobic effect is entropic

**Strategy.** Identify which species loses order when a non-polar group is transferred
from water to a non-polar environment, and decide which thermodynamic term carries the
favourable sign.

**Working.** A non-polar group cannot donate or accept hydrogen bonds. Water molecules
adjacent to it therefore adopt a more ordered arrangement, with fewer distinguishable
hydrogen-bond orientations, so the solvent entropy is lower than in bulk water. When the
group is buried — in a protein core or in a bilayer interior — those water molecules are
released to the bulk, and $\Delta S_\mathrm{water} > 0$. The enthalpy term is small and
may be of either sign because the hydrogen bonds lost by the released water are replaced
by new ones in bulk. The Gibbs energy is

$$
\Delta G = \Delta H - T\Delta S,
$$

so a large positive $\Delta S$ makes $\Delta G$ negative even when $\Delta H \approx 0$.
The effect is therefore a solvent effect, not an attractive force between non-polar
groups: the non-polar groups appear to attract one another because the system minimises
the non-polar surface exposed to water. In folding, burying hydrophobic side chains
reduces that surface; in membranes, the tails are sequestered in the bilayer interior for
the same reason.

**Answer.** The hydrophobic effect is entropic: burial releases ordered interfacial
water, so $-T\Delta S < 0$ dominates. It is not a force between non-polar groups; it is
the response of the hydrogen-bond network to non-polar surface. It drives folding by
burying hydrophobic residues and drives bilayer assembly by sequestering tails.

**Check.** An entropic effect should become stronger as temperature rises, and
hydrophobic association does become stronger up to the point at which protein unfolding
dominates. Non-polar solutes are sparingly soluble in water and their transfer from a
non-polar solvent into water is entropically unfavourable, both as predicted.

**Where marks are lost.** Writing "oil molecules attract each other by van der Waals
forces" or "like dissolves like". Neither identifies the ordered water that is released.

### 2. Why buffer capacity peaks at the $\mathrm{p}K_\mathrm{a}$

**Strategy.** Differentiate the buffer-capacity expression at fixed total buffer
concentration.

**Working.** The Henderson–Hasselbalch equation is

$$
\mathrm{pH} = \mathrm{p}K_\mathrm{a} + \log_{10}\frac{[\ce{A-}]}{[\ce{HA}]}.
$$

Buffer capacity is the amount of strong base needed to raise the pH by one unit,

$$
\beta = \frac{\mathrm{d}[\ce{B}]}{\mathrm{d}\,\mathrm{pH}}
= 2.303\,\frac{[\ce{HA}][\ce{A-}]}{[\ce{HA}]+[\ce{A-}]}.
$$

At fixed total concentration $C = [\ce{HA}]+[\ce{A-}]$, the product
$[\ce{HA}][\ce{A-}]$ is maximal when the two concentrations are equal, because for a
fixed sum the product is greatest at the midpoint. Equality means
$[\ce{A-}]/[\ce{HA}] = 1$, and the Henderson–Hasselbalch equation then gives
$\mathrm{pH} = \mathrm{p}K_\mathrm{a}$. Substituting $[\ce{HA}]=[\ce{A-}]=C/2$ gives

$$
\beta_\mathrm{max} = 2.303\frac{(C/2)(C/2)}{C} = 0.576\,C.
$$

One pH unit away, the ratio is $10:1$ or $1:10$, and
$\beta = 2.303\,C(10/121) = 0.190\,C$, only $33\%$ of the maximum. Further out, one
component is a minor species and is consumed quickly by added acid or base.

**Answer.** Capacity is maximal at $\mathrm{pH} = \mathrm{p}K_\mathrm{a}$ because that
is where $[\ce{HA}] = [\ce{A-}]$ and the product $[\ce{HA}][\ce{A-}]$ is maximal;
$\beta_\mathrm{max} = 0.576\,C$. At one pH unit away the capacity has fallen to about
one third of the maximum, which is why the useful range is quoted as
$\mathrm{p}K_\mathrm{a} \pm 1$.

**Check.** For a $0.100\ \mathrm{M}$ buffer, $\beta_\mathrm{max} = 0.0576\ \mathrm{M}$
per pH unit. Adding $1.00\ \mathrm{mmol}$ of strong acid to $1.00\ \mathrm{L}$ should
then change the pH by about $0.017$ unit, which is what the exact calculation in item 33
gives.

**Where marks are lost.** Saying "capacity is constant near the $\mathrm{p}K_\mathrm{a}$"
or omitting the factor $2.303$. The factor is $\ln 10$, not a conversion constant that
can be dropped.

### 3. Peptide-bond planarity and the Ramachandran plot

**Strategy.** Explain the electronic structure of the amide bond, then count the
backbone bonds that remain freely rotatable.

**Working.** The nitrogen lone pair of the peptide group is delocalised into the
carbonyl $\pi^*$ orbital. The resonance hybrid has partial double-bond character in the
$\ce{C-N}$ bond: its length is about $1.32\ \mathrm{\AA}$, between a single bond
($1.47\ \mathrm{\AA}$) and a double bond ($1.27\ \mathrm{\AA}$), and rotation about it
has a barrier of $75$–$85\ \mathrm{kJ\ mol^{-1}}$. The six atoms of the peptide group
therefore lie close to a plane, and the dihedral angle $\omega$ is close to $180^\circ$
(*trans*) for almost all peptide bonds. The exception is the bond preceding proline,
where *cis* is populated at several per cent.

With $\omega$ fixed, each residue has only two freely rotatable backbone bonds: $\phi$
about $\ce{N-C\alpha}$ and $\psi$ about $\ce{C\alpha-C}$. A plot of $\psi$ against
$\phi$ — the Ramachandran plot — therefore maps the steric allowance of the backbone.
Most combinations produce clashes between main-chain and side-chain atoms and are
forbidden; the allowed regions are discrete. The $\alpha$-helix lies near
$(\phi,\psi) = (-57^\circ,-47^\circ)$ and the $\beta$-sheet near
$(-139^\circ,+135^\circ)$. Glycine, with no side chain, can access much of the plot;
proline, with its pyrrolidine ring, is restricted to a narrow region near
$\phi \approx -60^\circ$.

**Answer.** The peptide bond is planar because resonance gives the $\ce{C-N}$ bond
partial double-bond character and a rotation barrier of $75$–$85\ \mathrm{kJ\ mol^{-1}}$.
Only $\phi$ and $\psi$ remain rotatable, so the backbone conformation is described by two
angles per residue; the Ramachandran plot shows the sterically allowed combinations, with
the $\alpha$-helix and $\beta$-sheet occupying distinct regions.

**Check.** At $298\ \mathrm{K}$, $RT = 2.48\ \mathrm{kJ\ mol^{-1}}$, so the fraction of
peptide bonds with enough thermal energy to rotate is
$e^{-80/2.48} \approx 10^{-14}$; planarity is preserved on biological timescales.

**Where marks are lost.** Saying "the peptide bond is a single bond, so rotation is
free". It is drawn as a single bond but behaves as a partial double bond.

### 4. Anfinsen's experiment and Levinthal's paradox

**Strategy.** State the conclusion of each experiment separately, then reconcile them
through the energy landscape.

**Working.** Anfinsen denatured ribonuclease A — 124 residues and four disulfide bonds —
in $8\ \mathrm{M}$ urea and $\beta$-mercaptoethanol, then removed both agents. The enzyme
spontaneously refolded and recovered activity with the correct disulfide pairing. The
conclusion is that the primary sequence contains the information needed to specify the
native structure, and that the native state is the thermodynamically most stable state
accessible under those conditions.

Levinthal noted that a 100-residue chain with three conformations per residue has
$3^{100} \approx 5\times10^{47}$ conformations. Sampling them at $10^{13}\ \mathrm{s^{-1}}$
would take about $10^{34}\ \mathrm{s}$, far longer than the age of the universe. A random
search cannot explain folding in milliseconds to seconds.

The two results are consistent because folding is not a random search. The energy
landscape is a funnel: many trajectories descend through a broad, rough surface toward a
deep global minimum. The native state is still the thermodynamic minimum, as Anfinsen
showed, but the path to it is biased by local interactions rather than sampled
exhaustively. Chaperones such as Hsp70 and GroEL/GroES improve the yield by suppressing
aggregation and competing pathways; they do not specify the final structure.

**Answer.** Anfinsen establishes that sequence specifies the native structure and that
the native state is thermodynamically favoured. Levinthal establishes that an exhaustive
random search is impossible. Both hold because folding follows a funnel-shaped energy
landscape with the native state at the global minimum, not a random search.

**Check.** Anfinsen's result does not require every protein to fold spontaneously
*in vivo*: folding competes with aggregation and degradation, which is exactly why
chaperones exist.

**Where marks are lost.** Concluding that Levinthal disproved spontaneous folding, or
that Anfinsen's experiment proves that chaperones are unnecessary *in vivo*.

### 5. $K_\mathrm{M}$, $K_\mathrm{d}$ and $k_\mathrm{cat}/K_\mathrm{M}$

**Strategy.** Use the definitions from the steady-state derivation and distinguish the
thermodynamic dissociation constant from the kinetic constant.

**Working.** For

$$
\ce{E + S <=>[k_1][k_{-1}] ES ->[k_2] E + P},
$$

the Michaelis constant is

$$
K_\mathrm{M} = \frac{k_{-1}+k_2}{k_1},
$$

whereas the dissociation constant of the enzyme–substrate complex is

$$
K_\mathrm{d} = \frac{k_{-1}}{k_1}.
$$

Thus $K_\mathrm{M} = K_\mathrm{d}$ only when $k_2 \ll k_{-1}$, that is, when the
catalytic step is much slower than dissociation. When $k_2$ is comparable to $k_{-1}$,
$K_\mathrm{M}$ overestimates $K_\mathrm{d}$ and is not a pure affinity measure.

The turnover number is $k_\mathrm{cat} = V_\mathrm{max}/[\ce{E}]_\mathrm{t}$, and

$$
\frac{k_\mathrm{cat}}{K_\mathrm{M}}
= \frac{k_1k_2}{k_{-1}+k_2}.
$$

At $[\ce{S}] \ll K_\mathrm{M}$, the Michaelis–Menten equation reduces to
$v = (k_\mathrm{cat}/K_\mathrm{M})[\ce{E}]_\mathrm{t}[\ce{S}]$, so
$k_\mathrm{cat}/K_\mathrm{M}$ is an apparent second-order rate constant for the encounter
of free enzyme and substrate. It combines binding and chemistry and is therefore the
relevant specificity constant when substrates compete. Its upper limit is the
diffusion-controlled encounter rate, about $10^8$–$10^9\ \mathrm{M^{-1}\ s^{-1}}$: a
reaction cannot proceed faster than the substrate can reach the enzyme.

**Answer.** $K_\mathrm{M} = K_\mathrm{d}$ only when $k_2 \ll k_{-1}$.
$k_\mathrm{cat}/K_\mathrm{M}$ is the apparent second-order rate constant at low substrate
concentration; it measures catalytic efficiency and is bounded by the diffusion-limited
encounter rate of about $10^8$–$10^9\ \mathrm{M^{-1}\ s^{-1}}$.

**Check.** Triose phosphate isomerase has
$k_\mathrm{cat}/K_\mathrm{M} \approx 2\times10^8\ \mathrm{M^{-1}\ s^{-1}}$, close to the
limit, and is described as catalytically perfect. An enzyme with
$k_\mathrm{cat}/K_\mathrm{M} \approx 10^4\ \mathrm{M^{-1}\ s^{-1}}$ is far from the
limit, so binding or chemistry, not encounter, limits it.

**Where marks are lost.** Saying "low $K_\mathrm{M}$ means high affinity" without the
condition $k_2 \ll k_{-1}$, or calling $k_\mathrm{cat}/K_\mathrm{M}$ a first-order rate
constant.

### 6. Anomeric carbons and reducing sugars

**Strategy.** Identify the anomeric carbon of each monosaccharide unit and test whether
it is free or committed to a glycosidic bond.

**Working.** The anomeric carbon is C1 of an aldose and C2 of a ketose. A free anomeric
carbon is in equilibrium with the open-chain carbonyl, so it can be oxidised by
Fehling's or Benedict's reagent; an anomeric carbon that is part of a glycosidic bond is
an acetal and cannot open.

- Sucrose is $\alpha$-D-glucopyranosyl-(1$\to$2)-$\beta$-D-fructofuranoside. The glucose
  C1 and the fructose C2 are both in the glycosidic bond. There is no free anomeric
  carbon, so sucrose is non-reducing.
- Lactose is $\beta$-D-galactopyranosyl-(1$\to$4)-D-glucopyranose. The galactose C1 is
  bonded, but the glucose C1 is free, so lactose is reducing.
- Maltose is $\alpha$-D-glucopyranosyl-(1$\to$4)-D-glucopyranose. The first glucose C1 is
  bonded and the second is free, so maltose is reducing.

**Answer.** Sucrose has two anomeric carbons and both are in the glycosidic bond, so it
is non-reducing. Lactose and maltose each have one free anomeric carbon (glucose C1), so
both are reducing.

**Check.** Sucrose gives a negative Benedict's test; lactose and maltose give positive
tests. The result is about the availability of the carbonyl, not about the number of
sugar units.

**Where marks are lost.** Saying sucrose "has no anomeric carbon". It has two; both are
simply bonded.

### 7. Cholesterol as a fluidity buffer

**Strategy.** Explain the effect separately below and above the transition temperature,
then combine them.

**Working.** Cholesterol is amphipathic: its $3\beta$-hydroxyl group sits near the
phospholipid head groups, and its rigid steroid ring intercalates between the acyl
chains.

Below the gel-to-liquid-crystalline transition temperature $T_\mathrm{m}$, the saturated
acyl chains are ordered and tightly packed. Cholesterol inserts between them and
disrupts that packing, increasing chain motion and fluidity. Above $T_\mathrm{m}$, the
chains are already disordered; the rigid steroid ring now restricts their motion and
decreases fluidity. The net effect is to broaden the transition and to make the membrane
less sensitive to temperature — a fluidity buffer rather than a rigidifier. The effect
depends on the phase, which is why the simple slogan "cholesterol makes membranes rigid"
is wrong.

**Answer.** Below $T_\mathrm{m}$ cholesterol increases fluidity by disrupting ordered
acyl-chain packing; above $T_\mathrm{m}$ it decreases fluidity by restricting chain
motion. It broadens the transition and buffers the membrane against temperature change.

**Check.** Animal plasma membranes contain cholesterol and most bacterial membranes do
not; bacteria adjust their fatty-acid composition instead. The cholesterol effect is
therefore a homeostatic adaptation to temperature fluctuation.

**Where marks are lost.** Giving only one half of the effect, or saying cholesterol
"stiffens" the membrane at all temperatures.

### 8. Alkaline hydrolysis of RNA

**Strategy.** Identify the intramolecular nucleophile that DNA lacks, then write the
phosphodiester cleavage.

**Working.** RNA contains a $2'$-hydroxyl group on every ribose. In dilute alkali, that
hydroxyl is deprotonated to an alkoxide, which is perfectly placed to attack the adjacent
phosphorus atom intramolecularly. The attack forms a pentacoordinate intermediate and
expels the $5'$-oxygen of the next nucleotide, leaving a $2',3'$-cyclic phosphate at the
cleavage site and a free $5'$-hydroxyl on the downstream fragment. The cyclic phosphate
is then hydrolysed to a mixture of $2'$- and $3'$-monophosphates:

$$
\ce{RNA-2'-OH(aq) + OH^{-}(aq) -> RNA-2',3'-cyclic\ phosphate(aq) + RNA-5'-OH(aq) + H2O(l)}
$$

DNA has $2'$-deoxyribose, so it has no adjacent hydroxyl to act as the intramolecular
nucleophile. Hydroxide can still attack the phosphodiester intermolecularly, but the
reaction is much slower, which is why DNA survives alkaline lysis and RNA does not.

**Answer.** The $2'$-hydroxyl of RNA is deprotonated and attacks the adjacent phosphate
intramolecularly, producing a $2',3'$-cyclic phosphate and chain cleavage. DNA lacks the
$2'$-hydroxyl and is therefore stable to alkali.

**Check.** The same $2'$-hydroxyl is why RNA adopts A-form geometry and why RNase H
recognises an RNA–DNA hybrid: the $2'$-substituent is chemically decisive in both cases.

**Where marks are lost.** Blaming uracil. Uracil is not the source of alkaline
lability; the $2'$-hydroxyl is.

### 9. Why $36$–$38$ became $30$–$32$

**Strategy.** Reconstruct both bookkeepings from the same pathway, then identify the
changed assumption.

**Working.** The pathway inventory is fixed. Per glucose: glycolysis gives a net
$2$ ATP and $2$ NADH; pyruvate dehydrogenase gives $2$ NADH; the Krebs cycle gives
$6$ NADH, $2$ FADH$_2$ and $2$ GTP. Substrate-level phosphorylation therefore gives
$4$ ATP equivalents (the two GTP count as ATP).

The historical integers used $\mathrm{P/O} = 3$ for NADH and $2$ for FADH$_2$:

$$
2 + 2(3) + 2(3) + 6(3) + 2(2) + 2 = 38\ \mathrm{ATP}.
$$

With the glycerol-3-phosphate shuttle, the two cytosolic NADH are delivered as
FADH$_2$, so the total falls by $2(3-2) = 2$ to $36$ ATP.

Modern proton accounting uses $10$ H$^+$ pumped per NADH and $6$ per FADH$_2$, with
about $4$ H$^+$ required per ATP in the simplified $c_{10}$ accounting (the $c$-ring
plus the phosphate carrier). That gives $\mathrm{P/O} = 10/4 = 2.5$ for NADH and
$6/4 = 1.5$ for FADH$_2$:

$$
2 + 2(2.5) + 2(2.5) + 6(2.5) + 2(1.5) + 2 = 32\ \mathrm{ATP},
$$

or $30$ ATP with the glycerol-3-phosphate shuttle. The difference is not a change in
the pathway; it is a change from integer chemical-coupling bookkeeping to chemiosmotic
proton accounting.

Neither number is universal. The $\mathrm{P/O}$ ratio depends on the $c$-ring subunit
number (about $8$ in mammals, $10$ in some organisms), on the shuttle used, on proton
leak, on the tissue and on whether the phosphate carrier is counted. Values quoted
without those assumptions are approximations, not constants.

**Answer.** $38$ ATP (or $36$ with the glycerol-3-phosphate shuttle) uses the historical
integers $\mathrm{P/O} = 3$ and $2$. $32$ ATP (or $30$) uses the modern values $2.5$ and
$1.5$ derived from $10$ and $6$ H$^+$ per reduced carrier and about $4$ H$^+$ per ATP.
The difference is a change in proton accounting, not in the pathway.

**Check.** $10(2.5) + 2(1.5) + 4 = 32$; the arithmetic is consistent with the
item-by-item tally in item 42. Both figures assume complete aerobic oxidation, GTP
equivalent to ATP, no proton leak and the shuttle named; they are not universal
constants.

**Where marks are lost.** Quoting $38$ as "the" answer without stating the integer
$\mathrm{P/O}$ assumption, or presenting $30$–$32$ as a range without saying which shuttle
gives which value.

### 10. Two photosystems and the ATP : NADPH balance

**Strategy.** Separate the redox problem (why two photosystems) from the stoichiometric
problem (why cyclic flow is needed).

**Working.** Photosystem II contains P680, which in its excited state is a strong enough
oxidant to take electrons from water at the oxygen-evolving Mn$_4$CaO$_5$ cluster.
Photosystem I contains P700, which in its excited state is a strong enough reductant to
pass electrons through ferredoxin to NADP$^+$. The two photosystems operate in series:
water $\to$ PSII $\to$ plastoquinone $\to$ cytochrome $b_6f$ $\to$ plastocyanin $\to$
PSI $\to$ ferredoxin $\to$ NADP$^+$. This is the Z-scheme. Splitting the work allows each
photosystem to use one photon per electron and avoids forcing a single photosystem to
span the whole water-to-NADP$^+$ redox range in one charge separation, which would
dissipate a larger fraction of the photon energy as heat.

Linear electron flow moves two electrons from water to NADP$^+$ per NADPH. It pumps
about $12$ H$^+$ per pair of electrons across the thylakoid membrane. The chloroplast
ATP synthase has a $c$-ring of $14$ subunits and needs about $4.7$ H$^+$ per ATP, so
linear flow supplies about $12/4.7 \approx 2.6$ ATP per $2$ NADPH. The Calvin cycle
requires $3$ ATP and $2$ NADPH per CO$_2$, so linear flow is short of ATP.

Cyclic electron flow around photosystem I solves the deficit. Electrons leave
ferredoxin and return to the plastoquinone pool/cytochrome $b_6f$ chain instead of
reducing NADP$^+$. The cycle makes no NADPH but pumps additional protons and therefore
makes extra ATP. The two modes together match the $3:2$ demand.

**Answer.** Two photosystems are needed because PSII supplies the strong oxidant for
water oxidation and PSI supplies the strong reductant for NADP$^+$ reduction; operating
them in series is the Z-scheme. Linear flow gives about $2.6$ ATP per $2$ NADPH, short of
the Calvin cycle's $3:2$ requirement; cyclic electron flow around PSI pumps extra protons
without making NADPH and tops up the ATP supply.

**Check.** A plant shifted to cyclic flow alone would stop fixing CO$_2$ for lack of
NADPH, which is why cyclic flow is a supplement, not a replacement.

**Where marks are lost.** Saying cyclic flow makes NADPH, or reversing the roles of PSI
and PSII.

---

## Part B — Structure and function

### 11. The water network and three anomalous properties

**Strategy.** Start from the $2+2$ hydrogen-bond functionality, then connect each property
to a specific structural consequence.

**Working.** Each water molecule has two O–H donors and two lone-pair acceptors. In
liquid water this produces a dynamic, nearly tetrahedral network: at $25\ ^\circ\mathrm{C}$
each molecule participates in about $3.4$ hydrogen bonds, the first coordination shell
contains about $4.5$ neighbours, and hydrogen bonds break and re-form on a
$1$–$10\ \mathrm{ps}$ timescale.

*High boiling point.* Vaporisation requires breaking roughly two hydrogen bonds per
molecule, giving $\Delta H_\mathrm{vap} = 44.0\ \mathrm{kJ\ mol^{-1}}$ at $25\ ^\circ\mathrm{C}$,
compared with $18.7\ \mathrm{kJ\ mol^{-1}}$ for $\ce{H2S}$. The result is a boiling point
of $100.0\ ^\circ\mathrm{C}$ at one atmosphere rather than the $-60\ ^\circ\mathrm{C}$ of
the heavier, less hydrogen-bonded analogue.

*Density maximum at $3.98\ ^\circ\mathrm{C}$.* Hexagonal ice Ih has an open tetrahedral
lattice with O–O distances of $2.76\ \mathrm{\AA}$ and a density of
$0.9167\ \mathrm{g\ cm^{-3}}$. On melting, the lattice collapses partially and the liquid
becomes denser. As the liquid is warmed from $0\ ^\circ\mathrm{C}$, two effects compete:
thermal expansion decreases the density, while further collapse and rearrangement of the
network increase it. The balance gives a maximum at $3.98\ ^\circ\mathrm{C}$. This is why
ice floats and lakes freeze from the top.

*High relative permittivity.* The dense network of polar O–H bonds reorients in an
electric field. The relative permittivity is $78.4$, so Coulomb forces between ions are
reduced by a factor of about $78$; this is why water dissolves salts whose lattice
enthalpy would otherwise prevent dissolution.

**Answer.** The $2+2$ hydrogen-bond functionality creates a dynamic tetrahedral network.
Its strength raises the boiling point; the competition between thermal expansion and
network collapse produces the density maximum at $3.98\ ^\circ\mathrm{C}$; and
reorientation of the dipole network gives $\varepsilon_\mathrm{r} = 78.4$.

**Check.** The same network explains the high surface tension ($72\ \mathrm{mN\ m^{-1}}$),
the high heat capacity ($75.3\ \mathrm{J\ K^{-1}\ mol^{-1}}$) and the large latent heats.
A single structural model accounts for all of them.

**Where marks are lost.** Saying ice is dense because solids are dense. Ice Ih is about
$9\%$ less dense than liquid water because its lattice is open.

### 12. $\alpha$-Helix and antiparallel $\beta$-sheet

**Strategy.** Compare the hydrogen-bond topology and the backbone geometry, not the side
chains.

**Working.**

| Feature | $\alpha$-Helix | Antiparallel $\beta$-sheet |
|---|---|---|
| Hydrogen-bond pattern | $i \to i+4$ within one chain; bonds nearly parallel to the helix axis | Between $\ce{N-H}$ and $\ce{C=O}$ of adjacent strands; bonds close to linear in the antiparallel case |
| Residues per turn or repeat | $3.6$ residues per turn | About $2$ residues per strand repeat; pleated |
| Rise per residue | $1.5\ \mathrm{\AA}$ | $3.2$–$3.5\ \mathrm{\AA}$ |
| Pitch | $5.4\ \mathrm{\AA}$ per turn | — |
| Ramachandran region | $\phi \approx -57^\circ$, $\psi \approx -47^\circ$ | $\phi \approx -139^\circ$, $\psi \approx +135^\circ$ |
| Side-chain disposition | Project outward from the helix; amphipathic helices have hydrophobic and polar faces | Alternate above and below the sheet plane |

The helix is a compact coil stabilised by local hydrogen bonds. The sheet is an extended
array stabilised by inter-strand hydrogen bonds; the antiparallel arrangement gives
linear bonds, whereas the parallel arrangement gives distorted ones. Both are defined by
their backbone hydrogen-bond pattern, not by the identity of the side chains.

**Answer.** The $\alpha$-helix has $3.6$ residues per turn, a $1.5\ \mathrm{\AA}$ rise per
residue and $i \to i+4$ hydrogen bonds; it lies at $(-57^\circ,-47^\circ)$ on the
Ramachandran plot. The antiparallel $\beta$-sheet has extended strands with a
$3.2$–$3.5\ \mathrm{\AA}$ rise per residue, inter-strand hydrogen bonds and lies at
$(-139^\circ,+135^\circ)$.

**Check.** A Ramachandran plot of a real protein shows clusters at exactly these two
regions, plus the glycine and proline outliers; the assignment is structural, not
sequence-based.

**Where marks are lost.** Saying the $\beta$-sheet is stabilised by hydrogen bonds
*within* one strand. The defining bonds are between strands.

### 13. Ionisable groups of Asp-His-Lys

**Strategy.** List the five groups, assign acid or base behaviour, and rank by
$\mathrm{p}K_\mathrm{a}$.

**Working.** The groups and their values are:

| Group | $\mathrm{p}K_\mathrm{a}$ | Behaviour as pH rises |
|---|---:|---|
| C-terminal $\ce{-CO2H}$ | $2.34$ | Loses a proton, becomes $-1$ |
| Asp side chain $\ce{-CO2H}$ | $3.86$ | Loses a proton, becomes $-1$ |
| His imidazole $\ce{-NH+}$ | $6.00$ | Loses a proton, becomes neutral |
| N-terminal $\ce{-NH3+}$ | $9.60$ | Loses a proton, becomes neutral |
| Lys side chain $\ce{-NH3+}$ | $10.53$ | Loses a proton, becomes neutral |

The order of deprotonation is therefore C-terminus, Asp, His, N-terminus, Lys. At pH
$1$, all groups are protonated and the net charge is $+3$ (N-terminus, His and Lys
positive; both carboxyl groups neutral). The charge falls to $+2$ after the C-terminus
deprotonates, to $+1$ after Asp, to $0$ after His, to $-1$ after the N-terminus and to
$-2$ after Lys.

At pH $7.4$, the C-terminus and Asp are fully negative, the N-terminus and Lys are
fully positive, and His is almost neutral: the fraction protonated is
$1/(1+10^{7.4-6.0}) = 0.038$, so only about $3.8\%$ of the imidazole is positive. The
net charge is therefore close to zero, with a small positive residue from histidine.

**Answer.** The deprotonation order is C-terminus ($2.34$), Asp ($3.86$), His ($6.00$),
N-terminus ($9.60$), Lys ($10.53$). At pH $7.4$ the C-terminus and Asp are $-1$ each, the
N-terminus and Lys are $+1$ each, and His is about $4\%$ protonated; the net charge is
approximately zero.

**Check.** The result is consistent with the calculation in item 24 for a related
peptide: histidine contributes only a few hundredths of a charge at pH $7.4$.

**Where marks are lost.** Ranking by "acidic, basic, neutral" instead of by
$\mathrm{p}K_\mathrm{a}$, or treating histidine as fully positive at pH $7.4$.

### 14. Competitive, uncompetitive and non-competitive inhibition

**Strategy.** Classify by the species the inhibitor binds, then translate that into the
apparent constants and the reciprocal plot.

**Working.**

| Type | Binds | $K_\mathrm{M}^\mathrm{app}$ | $V_\mathrm{max}^\mathrm{app}$ | Lineweaver–Burk |
|---|---|---|---|---|
| Competitive | Free enzyme, at the active site | Increases by $\alpha = 1+[\ce{I}]/K_\mathrm{i}$ | Unchanged | Lines intersect on the $y$-axis |
| Uncompetitive | Enzyme–substrate complex only | Decreases by $\alpha' = 1+[\ce{I}]/K_\mathrm{i}'$ | Decreases by $\alpha'$ | Parallel lines |
| Pure non-competitive | Free enzyme and ES complex equally | Unchanged | Decreases by $\alpha$ | Lines intersect on the $x$-axis |

Competitive inhibition is overcome by raising the substrate concentration, because
saturating substrate displaces the inhibitor; $V_\mathrm{max}$ is therefore unchanged.
Uncompetitive inhibition cannot be overcome by substrate, because the inhibitor binds
only after the substrate has bound; both $K_\mathrm{M}$ and $V_\mathrm{max}$ fall by the
same factor, so their ratio is unchanged and the reciprocal lines are parallel. Pure
non-competitive inhibition reduces the effective amount of active enzyme without changing
substrate binding, so $K_\mathrm{M}$ is unchanged and $V_\mathrm{max}$ falls.

**Answer.** Competitive: free enzyme, $K_\mathrm{M}$ increases, $V_\mathrm{max}$
unchanged, $y$-axis intersection. Uncompetitive: ES only, both constants decrease by the
same factor, parallel lines. Pure non-competitive: E and ES equally, $K_\mathrm{M}$
unchanged, $V_\mathrm{max}$ decreases, $x$-axis intersection.

**Check.** The diagnostic experiment is to raise $[\ce{S}]$: competitive inhibition
disappears, uncompetitive inhibition does not.

**Where marks are lost.** Saying a competitive inhibitor lowers $V_\mathrm{max}$, or
calling parallel lines "non-competitive". Parallel lines are the signature of
uncompetitive inhibition.

### 15. Glycosidic linkages and digestibility

**Strategy.** Name each linkage with both anomeric configurations and both carbon
numbers, then connect the linkage to the enzyme that hydrolyses it.

**Working.**

- Sucrose: $\alpha$-D-glucopyranosyl-(1$\to$2)-$\beta$-D-fructofuranoside. Both anomeric
  carbons (glucose C1 and fructose C2) are in the bond, so sucrose is non-reducing.
- Lactose: $\beta$-D-galactopyranosyl-(1$\to$4)-D-glucopyranose. Galactose C1 is bonded;
  glucose C1 is free, so lactose is reducing.
- Maltose: $\alpha$-D-glucopyranosyl-(1$\to$4)-D-glucopyranose. One glucose C1 is bonded
  and the other is free, so maltose is reducing.
- Cellulose: $\beta$-D-glucopyranosyl-(1$\to$4)-D-glucopyranose, a linear polymer. Each
  chain has one free anomeric carbon at its reducing end, so the polymer is formally
  reducing, but the effect is negligible for a chain of thousands of residues.

Human $\alpha$-amylase hydrolyses $\alpha(1\to4)$ bonds in starch and glycogen. Humans
do not produce a cellulase capable of hydrolysing $\beta(1\to4)$ bonds, and the
crystalline, extensively hydrogen-bonded cellulose microfibril is also physically
resistant to attack. Ruminants and termites rely on microbial cellulases in their guts.

**Answer.** Sucrose: $\alpha(1\to2)$, non-reducing. Lactose: $\beta(1\to4)$, reducing.
Maltose: $\alpha(1\to4)$, reducing. Cellulose: $\beta(1\to4)$, formally reducing at one
chain end but practically non-reducing. Humans digest $\alpha(1\to4)$ starch with
$\alpha$-amylase but lack a cellulase for $\beta(1\to4)$ cellulose.

**Check.** The anomeric-carbon count explains the Benedict's results: sucrose negative,
lactose and maltose positive. The enzyme specificity explains why a $\beta$-linkage
survives the human gut.

**Where marks are lost.** Calling cellulose "non-reducing" without qualification, or
saying humans cannot digest cellulose because it is a polysaccharide. Starch is also a
polysaccharide; the difference is the linkage and the enzyme.

### 16. Packing parameter and assembly shape

**Strategy.** Use $P = v/(a_0l_\mathrm{c})$ and the standard boundaries.

**Working.** The packing parameter compares the tail volume $v$ with the volume that the
head group can cover, $a_0l_\mathrm{c}$:

$$
P = \frac{v}{a_0l_\mathrm{c}}.
$$

The boundaries are $P < 1/3$ for spherical micelles, $1/3 < P < 1/2$ for cylindrical
micelles, $1/2 < P < 1$ for bilayers and vesicles, and $P > 1$ for inverted structures.

- A phospholipid has two tails, so $v$ is large, and a moderate head-group area; its
  $P \approx 0.9$ lies in the bilayer/vesicle range. This is why phosphatidylcholine
  forms bilayers.
- A lysophospholipid has one tail, so $v$ is roughly halved while $a_0$ is similar;
  $P \approx 0.4$ lies in the cylindrical-micelle range.
- A bile salt has a rigid steroid body, a small tail volume and a large, charged
  head-group area; $P \approx 0.2$ lies in the spherical-micelle range.

**Answer.** Phospholipid ($P \approx 0.9$): bilayer or vesicle. Lysophospholipid
($P \approx 0.4$): cylindrical micelle. Bile salt ($P \approx 0.2$): spherical micelle.
The controlling features are the number of tails (which sets $v$) and the head-group area
(which sets $a_0$).

**Check.** The prediction agrees with the behaviour of phosphatidylcholine (bilayer),
lysophosphatidylcholine (micelle) and bile salts (micelles that solubilise dietary fat).

**Where marks are lost.** Using $P < 1/2$ for bilayers, or ignoring the head-group area
and arguing from tail number alone.

### 17. A-, B- and Z-DNA

**Strategy.** Tabulate the helical parameters, then explain the RNA exception through
sugar pucker.

**Working.**

| Property | A-DNA | B-DNA | Z-DNA |
|---|---|---|---|
| Handedness | Right | Right | Left |
| Residues per turn | $11$ | $10.5$ | $12$ |
| Rise per residue | $0.26\ \mathrm{nm}$ | $0.34\ \mathrm{nm}$ | $0.37\ \mathrm{nm}$ |
| Pitch per turn | $2.9\ \mathrm{nm}$ | $3.6\ \mathrm{nm}$ | $4.4\ \mathrm{nm}$ |
| Diameter | $2.3\ \mathrm{nm}$ | $2.0\ \mathrm{nm}$ | $1.8\ \mathrm{nm}$ |
| Sugar pucker | C3$'$-*endo* | C2$'$-*endo* | C3$'$-*endo* and C2$'$-*endo* |
| Glycosidic angle | *anti* | *anti* | *anti* and *syn* |
| Major groove | Narrow, deep | Wide, deep | Flat |

B-DNA is the physiological form and has the wide major groove that most
sequence-specific proteins read. A-DNA is shorter and fatter, with the base pairs
displaced from the axis; it forms on dehydration and in some DNA–protein complexes.
Z-DNA is left-handed with a zig-zag backbone; it requires alternating purine–pyrimidine
sequence and is favoured by high salt and negative supercoiling.

An RNA–RNA duplex adopts A-form geometry because the $2'$-hydroxyl sterically enforces
C3$'$-*endo* sugar pucker. C3$'$-*endo* gives $11$ residues per turn, a $0.26\ \mathrm{nm}$
rise and a deep, narrow major groove. The same geometry appears in RNA–DNA hybrids, which
is why RNase H recognises an RNA–DNA hybrid rather than a DNA–DNA duplex.

**Answer.** A-DNA: right-handed, $11$ residues per turn, $0.26\ \mathrm{nm}$ rise, narrow
deep major groove. B-DNA: right-handed, $10.5$, $0.34\ \mathrm{nm}$, wide deep major
groove. Z-DNA: left-handed, $12$, $0.37\ \mathrm{nm}$, flat major groove. RNA adopts
A-form because its $2'$-hydroxyl forces C3$'$-*endo* pucker.

**Check.** The parameters are mutually consistent: pitch equals residues per turn times
rise per residue ($10.5 \times 0.34 = 3.57\ \mathrm{nm} \approx 3.6\ \mathrm{nm}$).

**Where marks are lost.** Saying Z-DNA is right-handed, or attributing the A-form of RNA
to the bases rather than to the ribose $2'$-hydroxyl.

### 18. Tracing one acetyl group through the Krebs cycle

**Strategy.** Follow carbon count and cofactor reduction at each step, not the names
alone.

**Working.** Pyruvate dehydrogenase converts the three-carbon pyruvate to the two-carbon
acetyl group of acetyl-CoA, releasing one $\ce{CO2}$ and reducing one $\ce{NAD+}$:

$$
\ce{CH3COCOO^{-} + CoA-SH + NAD+ -> CH3CO-S-CoA + CO2 + NADH}.
$$

The acetyl group enters the cycle by condensing with the four-carbon oxaloacetate to
give six-carbon citrate. The cycle then proceeds as follows.

| Step | Carbon count | Cofactor | Product |
|---|---:|---|---|
| Citrate $\to$ isocitrate | 6 | — | Isocitrate |
| Isocitrate $\to$ $\alpha$-ketoglutarate | 5 | $\ce{NAD+}$ | $\alpha$-KG, $\ce{CO2}$, $\ce{NADH}$ |
| $\alpha$-KG $\to$ succinyl-CoA | 4 | $\ce{NAD+}$ | Succinyl-CoA, $\ce{CO2}$, $\ce{NADH}$ |
| Succinyl-CoA $\to$ succinate | 4 | GDP, P$_i$ | Succinate, GTP |
| Succinate $\to$ fumarate | 4 | FAD | Fumarate, $\ce{FADH2}$ |
| Fumarate $\to$ malate | 4 | — | Malate |
| Malate $\to$ oxaloacetate | 4 | $\ce{NAD+}$ | OAA, $\ce{NADH}$ |

The two carbons released as $\ce{CO2}$ are not literally the two carbons that entered as
acetyl-CoA; the cycle scrambles them with the oxaloacetate pool. What is exact is the
accounting: one turn releases two $\ce{CO2}$, reduces three $\ce{NAD+}$ and one FAD, and
produces one GTP. Oxaloacetate is regenerated, so the cycle is catalytic in $C_4$.

Per glucose, two pyruvate molecules give two PDH reactions (two $\ce{NADH}$, two
$\ce{CO2}$) and two Krebs turns (four $\ce{CO2}$, six $\ce{NADH}$, two $\ce{FADH2}$, two
GTP).

**Answer.** Per acetyl-CoA: $2$ $\ce{CO2}$, $3$ $\ce{NADH}$, $1$ $\ce{FADH2}$ and
$1$ GTP, with oxaloacetate regenerated. Including PDH, each pyruvate gives an additional
$\ce{CO2}$ and $\ce{NADH}$; per glucose the totals are $6$ $\ce{CO2}$, $8$ $\ce{NADH}$,
$2$ $\ce{FADH2}$ and $2$ GTP from PDH plus the cycle.

**Check.** Carbon balance per turn: $2$ acetyl carbons + $4$ oxaloacetate carbons in;
$6$ carbons out as citrate intermediates, then $2$ $\ce{CO2}$ + $4$ oxaloacetate carbons.
The count closes.

**Where marks are lost.** Saying the cycle produces three $\ce{CO2}$ per turn, or
forgetting that succinyl-CoA synthetase makes GTP rather than ATP (they are equivalent
energetically, but the enzyme name matters).

### 19. The Z-scheme

**Strategy.** Follow one electron from water to NADP$^+$ and note the energy input at each
photosystem.

**Working.** The route is:

$$
\ce{H2O} \to \text{OEC} \to \text{P680} \to \text{pheophytin} \to \text{Q}_A \to
\text{Q}_B \to \text{PQH}_2 \to \text{cyt } b_6f \to \text{plastocyanin} \to
\text{P700} \to \text{A}_0 \to \text{A}_1 \to \text{ferredoxin} \to \text{FNR} \to
\ce{NADP+}.
$$

At photosystem II, excitation of P680 produces P680$^*$, which transfers an electron to
pheophytin within picoseconds. The resulting P680$^+$ is a very strong oxidant, strong
enough to oxidise water at the Mn$_4$CaO$_5$ oxygen-evolving complex. Water is therefore
the ultimate electron donor: it is abundant, and its oxidation potential is accessible
only to the highly oxidising P680$^+$. Four photochemical turnovers release one
$\ce{O2}$ and four $\ce{H+}$ into the lumen.

At photosystem I, excitation of P700 produces P700$^*$, a strong reductant that passes
electrons through A$_0$, A$_1$ and ferredoxin to ferredoxin–NADP$^+$ reductase, which
reduces $\ce{NADP+}$ to NADPH. The two photosystems are connected by plastoquinone,
cytochrome $b_6f$ and plastocyanin.

The proton gradient is generated at three points: water oxidation releases protons into
the lumen; plastoquinol oxidation releases protons into the lumen at cytochrome $b_6f$;
and the Q cycle contributes additional proton translocation. About $12$ $\ce{H+}$ are
translocated per pair of electrons, and the thylakoid ATP synthase uses about $4.7$
$\ce{H+}$ per ATP.

**Answer.** The Z-scheme runs water $\to$ PSII $\to$ plastoquinone $\to$ cytochrome
$b_6f$ $\to$ plastocyanin $\to$ PSI $\to$ ferredoxin $\to$ NADP$^+$. Water is the ultimate
donor because P680$^+$ is a strong enough oxidant to oxidise it. The proton gradient is
generated by water oxidation, plastoquinol oxidation and the Q cycle, giving about
$2.6$ ATP per $2$ NADPH from linear flow.

**Check.** The scheme explains the name: a plot of redox potential against reaction
coordinate has two upward photon-driven steps and two downward electron-transfer steps,
forming a Z.

**Where marks are lost.** Reversing the order (PSI before PSII) or saying water is
oxidised at PSI. Water is oxidised at the oxygen-evolving complex of PSII.

### 20. The *lac* and *trp* operons

**Strategy.** Treat each operon as a logic circuit and identify the signals that set the
switches.

**Working.** The *lac* operon is a catabolic operon. LacI repressor binds the operator
and blocks RNA polymerase when lactose is absent. When lactose is present, allolactose
binds LacI and releases it from the operator. But derepression alone is not enough:
CAP must also activate transcription. CAP binds cAMP, and cAMP is high only when glucose
is low. The operon is therefore expressed only when lactose is present **and** glucose is
absent — a logical AND gate. Either signal alone is insufficient. This makes metabolic
sense: the cell should not make lactose-utilising enzymes when a better carbon source is
available, nor when there is no lactose to use.

The *trp* operon is a biosynthetic operon and uses two layers. Repression is coarse:
TrpR, with bound tryptophan, binds the operator and blocks initiation. Attenuation is
fine: the leader region encodes a short peptide with tandem tryptophan codons. When
tryptophan is abundant, the ribosome translates the leader quickly and the RNA forms a
terminator hairpin, stopping transcription after initiation. When tryptophan is scarce,
the ribosome stalls at the Trp codons, allowing an antiterminator hairpin to form and
transcription to continue. Repression controls whether transcription starts; attenuation
controls whether it finishes.

**Answer.** *lac* is an AND gate: allolactose removes LacI and CAP–cAMP activates only
when glucose is low, so transcription requires lactose present and glucose absent. *trp*
uses repression (TrpR–Trp blocks initiation) plus attenuation (ribosome speed through
the leader sets terminator versus antiterminator). Two signals give both coarse and fine
control and avoid wasteful expression.

**Check.** A *lac* mutant that cannot make CAP would be unable to grow on lactose even
when lactose is present, which is the predicted AND-gate behaviour. A *trp* leader
mutation that removes the Trp codons would abolish attenuation but not repression.

**Where marks are lost.** Saying *lac* is induced by glucose (it is repressed by glucose
via low cAMP) or conflating attenuation with repression.

---

## Part C — Basic calculations

### 21. Preparing a phosphate buffer at pH 7.00

**Strategy.** Henderson–Hasselbalch gives the ratio of the two phosphate forms; the total
concentration gives the individual concentrations; the molar masses give the masses.

**Working.** Let $[\ce{HPO4^{2-}}]$ be the conjugate base and $[\ce{H2PO4-}]$ the acid:

$$
7.00 = 6.86 + \log_{10}\frac{[\ce{HPO4^{2-}}]}{[\ce{H2PO4-}]},
$$

$$
\frac{[\ce{HPO4^{2-}}]}{[\ce{H2PO4-}]} = 10^{0.14} = 1.38.
$$

Let $x = [\ce{H2PO4-}]$. Then $1.38x + x = 0.0500\ \mathrm{mol\ L^{-1}}$, so
$x = 0.0210\ \mathrm{mol\ L^{-1}}$ and $[\ce{HPO4^{2-}}] = 0.0290\ \mathrm{mol\ L^{-1}}$.

$$
m(\ce{Na2HPO4}) = (0.0290\ \mathrm{mol})(141.96\ \mathrm{g\ mol^{-1}})
= 4.12\ \mathrm{g},
$$

$$
m(\ce{NaH2PO4}) = (0.0210\ \mathrm{mol})(119.98\ \mathrm{g\ mol^{-1}})
= 2.52\ \mathrm{g}.
$$

**Answer.** $4.12\ \mathrm{g}$ of anhydrous $\ce{Na2HPO4}$ and $2.52\ \mathrm{g}$ of
anhydrous $\ce{NaH2PO4}$, dissolved in water and made up to $1.00\ \mathrm{L}$.

**Check.** The ratio $0.0290/0.0210 = 1.38$, and
$6.86 + \log_{10}1.38 = 7.00$. The masses sum to $6.64\ \mathrm{g}$, consistent with
$0.0500\ \mathrm{mol}$ of phosphate plus the sodium counterions.

**Where marks are lost.** Assigning $\ce{Na2HPO4}$ as the acid and $\ce{NaH2PO4}$ as the
base; using $\mathrm{p}K_{a1}$ instead of $\mathrm{p}K_{a2}$; or preparing the buffer by
adding the salts to $1.00\ \mathrm{L}$ of water rather than making the final volume
$1.00\ \mathrm{L}$.

### 22. Osmotic pressure of $0.154\ \mathrm{M}$ sodium chloride

**Strategy.** Convert to SI concentration, apply the van 't Hoff equation with $i=2$, and
compare at the two temperatures.

**Working.** $C = 0.154\ \mathrm{mol\ L^{-1}} = 154\ \mathrm{mol\ m^{-3}}$ and $i = 2$
for complete dissociation. With $R = 8.314\ \mathrm{J\ mol^{-1}\ K^{-1}}$:

$$
\pi(298.15\ \mathrm{K}) = iCRT
= 2(154)(8.314)(298.15)
= 7.63\times10^{5}\ \mathrm{Pa}
= 7.63\ \mathrm{bar},
$$

$$
\pi(310.15\ \mathrm{K}) = 2(154)(8.314)(310.15)
= 7.94\times10^{5}\ \mathrm{Pa}
= 7.94\ \mathrm{bar}.
$$

Plasma at $290\ \mathrm{mOsm\ L^{-1}} = 290\ \mathrm{mol\ m^{-3}}$ gives

$$
\pi_\mathrm{plasma} = (290)(8.314)(310.15)
= 7.48\times10^{5}\ \mathrm{Pa}
= 7.48\ \mathrm{bar}.
$$

**Answer.** $7.63\ \mathrm{bar}$ at $298.15\ \mathrm{K}$ and $7.94\ \mathrm{bar}$ at
$310.15\ \mathrm{K}$. At $310.15\ \mathrm{K}$ the saline is about $6\%$ more concentrated
than plasma, which is why $0.9\%$ saline is described as isotonic although it is
marginally hypertonic.

**Check.** The osmolarity is $2 \times 154 = 308\ \mathrm{mOsm\ L^{-1}}$, close to the
plasma value of about $290\ \mathrm{mOsm\ L^{-1}}$. The calculation assumes complete
dissociation and ideality, so it slightly overestimates the osmotic coefficient.

**Where marks are lost.** Using $9.0\ \mathrm{g\ L^{-1}}$ instead of $9.0\ \mathrm{g}$ per
$100\ \mathrm{mL}$ (which gives $90\ \mathrm{g\ L^{-1}}$), or forgetting $i=2$.

### 23. Isoelectric points of aspartate and lysine **(multi-step)**

**Strategy.** Identify the zwitterionic species and average the two $\mathrm{p}K_\mathrm{a}$
values that bracket it.

**Working.** Aspartate has $\mathrm{p}K_\mathrm{a}$ values $2.09$ ($\alpha$-$\ce{CO2H}$),
$3.86$ (side-chain $\ce{CO2H}$) and $9.82$ ($\alpha$-$\ce{NH3+}$). The neutral zwitterion
has both carboxyl groups deprotonated and the amino group protonated, so it lies between
the two lowest $\mathrm{p}K_\mathrm{a}$ values:

$$
\mathrm{pI}(\ce{Asp}) = \frac{2.09+3.86}{2} = 2.975 \approx 2.98.
$$

Lysine has $\mathrm{p}K_\mathrm{a}$ values $2.18$ ($\alpha$-$\ce{CO2H}$), $8.95$
($\alpha$-$\ce{NH3+}$) and $10.53$ (side-chain $\ce{NH3+}$). The neutral zwitterion has
the carboxyl deprotonated and both amino groups protonated, so it lies between the two
highest values:

$$
\mathrm{pI}(\ce{Lys}) = \frac{8.95+10.53}{2} = 9.74.
$$

**Answer.** $\mathrm{pI}(\ce{Asp}) = 2.98$ and $\mathrm{pI}(\ce{Lys}) = 9.74$ (both dimensionless).

**Check.** At pH $2.98$ aspartate has one carboxyl largely deprotonated, the other largely
protonated, and the amino group fully protonated, so the net charge crosses zero. At pH
$9.74$ lysine has the carboxyl fully negative, the $\alpha$-amino partly protonated and
the side chain partly protonated, again summing to zero.

**Where marks are lost.** Averaging all three $\mathrm{p}K_\mathrm{a}$ values, or using
the two highest for aspartate and the two lowest for lysine. The rule is always "the two
values that bracket the zwitterion".

### 24. Net charge of Ala-His-Asp at pH 7.40 **(multi-step)**

**Strategy.** Sum the fractional charges of the N-terminus, C-terminus and the two
ionisable side chains.

**Working.** For an acid group, the negative contribution is
$1/(1+10^{\mathrm{p}K_\mathrm{a}-\mathrm{pH}})$; for a base group, the positive
contribution is $1/(1+10^{\mathrm{pH}-\mathrm{p}K_\mathrm{a}})$. The groups are the
N-terminus ($9.60$, base), the C-terminus ($2.34$, acid), histidine ($6.00$, base) and
aspartate ($3.86$, acid):

$$
Q = \frac{1}{1+10^{7.40-9.60}}
+ \frac{1}{1+10^{7.40-6.00}}
- \frac{1}{1+10^{2.34-7.40}}
- \frac{1}{1+10^{3.86-7.40}}.
$$

$$
Q = 0.994 + 0.0383 - 0.99999 - 0.99971 = -0.968.
$$

**Answer.** $Q = -0.97\ e$ at pH $7.40$, where $e$ is the elementary charge.

**Check.** Two acidic groups are fully deprotonated ($-2$), one amino terminus is fully
protonated ($+1$) and histidine is only $3.8\%$ protonated ($+0.04$), so a net charge
near $-1$ is expected.

**Where marks are lost.** Counting histidine as fully $+1$ (which would give
$-0.03$ instead of $-0.97$), or reversing the acid and base formulas.

### 25. $K_\mathrm{M}$ and $V_\mathrm{max}$ from initial rates **(multi-step)**

**Strategy.** Transform to reciprocals, fit the Lineweaver–Burk line, and convert the
intercept and slope back to $V_\mathrm{max}$ and $K_\mathrm{M}$.

**Working.** The reciprocal pairs are:

| $[\ce{S}]$ / mM | $v$ / $\mu\mathrm{mol\ min^{-1}}$ | $1/[\ce{S}]$ / mM$^{-1}$ | $1/v$ / $\mathrm{min\ \mu mol^{-1}}$ |
|---:|---:|---:|---:|
| 0.50 | 0.24 | 2.00 | 4.167 |
| 1.0 | 0.40 | 1.00 | 2.500 |
| 2.0 | 0.60 | 0.500 | 1.667 |
| 4.0 | 0.80 | 0.250 | 1.250 |
| 8.0 | 0.96 | 0.125 | 1.042 |

The slope is

$$
\frac{4.167-1.042}{2.00-0.125}
= \frac{3.125}{1.875}
= 1.67\ \mathrm{mM\ min\ \mu mol^{-1}},
$$

and the intercept is

$$
4.167 - 1.67(2.00) = 0.833\ \mathrm{min\ \mu mol^{-1}}.
$$

Therefore

$$
V_\mathrm{max} = \frac{1}{0.833} = 1.20\ \mu\mathrm{mol\ min^{-1}},
\qquad
K_\mathrm{M} = \text{slope}\times V_\mathrm{max}
= (1.67)(1.20) = 2.0\ \mathrm{mM}.
$$

**Answer.** $V_\mathrm{max} = 1.20\ \mu\mathrm{mol\ min^{-1}}$ and
$K_\mathrm{M} = 2.0\ \mathrm{mM}$.

**Check.** At $[\ce{S}] = K_\mathrm{M} = 2.0\ \mathrm{mM}$, the Michaelis–Menten equation
gives $v = 1.20(2.0)/(2.0+2.0) = 0.60\ \mu\mathrm{mol\ min^{-1}}$, exactly half of
$V_\mathrm{max}$, as the definition requires.

**Where marks are lost.** Reciprocating the concentrations but not the rates; using
$\mathrm{mM}^{-1}$ and $\mathrm{min\ \mu mol^{-1}}$ inconsistently; or reading the
$x$-intercept as $K_\mathrm{M}$ instead of $-1/K_\mathrm{M}$.

### 26. Turnover number and catalytic efficiency **(multi-step)**

**Strategy.** Convert $V_\mathrm{max}$ to amount per second, divide by the amount of
enzyme, then divide by $K_\mathrm{M}$ in molar units.

**Working.** $V_\mathrm{max} = 1.20\ \mu\mathrm{mol\ min^{-1}}$ in the $1.00\ \mathrm{mL}$
assay:

$$
V_\mathrm{max} = \frac{1.20\times10^{-6}\ \mathrm{mol}}{60\ \mathrm{s}}
= 2.00\times10^{-8}\ \mathrm{mol\ s^{-1}}.
$$

The amount of enzyme is $n_\mathrm{E} = 0.50\ \mathrm{nmol} = 5.0\times10^{-10}\ \mathrm{mol}$, so

$$
k_\mathrm{cat} = \frac{V_\mathrm{max}}{n_\mathrm{E}}
= \frac{2.00\times10^{-8}}{5.0\times10^{-10}}
= 40\ \mathrm{s^{-1}}.
$$

With $K_\mathrm{M} = 2.0\ \mathrm{mM} = 2.0\times10^{-3}\ \mathrm{M}$,

$$
\frac{k_\mathrm{cat}}{K_\mathrm{M}}
= \frac{40}{2.0\times10^{-3}}
= 2.0\times10^{4}\ \mathrm{M^{-1}\ s^{-1}}.
$$

**Answer.** $k_\mathrm{cat} = 40\ \mathrm{s^{-1}}$ and
$k_\mathrm{cat}/K_\mathrm{M} = 2.0\times10^{4}\ \mathrm{M^{-1}\ s^{-1}}$.

**Check.** Each enzyme molecule turns over $40$ times per second. The catalytic
efficiency is four to five orders of magnitude below the diffusion limit
($10^8$–$10^9\ \mathrm{M^{-1}\ s^{-1}}$), so binding or chemistry, not encounter, limits
this enzyme.

**Where marks are lost.** Leaving $V_\mathrm{max}$ in $\mu\mathrm{mol\ min^{-1}}$ and
dividing by nanomoles without converting minutes to seconds; or using the assay volume
twice and turning $k_\mathrm{cat}$ into a concentration-dependent quantity.

### 27. Composition of a mutarotated glucose solution **(multi-step)**

**Strategy.** Treat the observed rotation as a linear mixture of the two anomer rotations.

**Working.** Let $x$ be the fraction of $\beta$-anomer. Then

$$
[\alpha]_\mathrm{eq} = x[\alpha]_\beta + (1-x)[\alpha]_\alpha,
$$

so

$$
x = \frac{[\alpha]_\alpha - [\alpha]_\mathrm{eq}}
{[\alpha]_\alpha - [\alpha]_\beta}
= \frac{112.2 - 75.0}{112.2 - 18.7}
= \frac{37.2}{93.5}
= 0.398.
$$

Therefore the mixture is $39.8\%$ $\beta$ and $60.2\%$ $\alpha$.

**Answer.** $39.8\%$ $\beta$-D-glucopyranose and $60.2\%$ $\alpha$-D-glucopyranose.

**Check.** The weighted rotation is
$0.398(18.7) + 0.602(112.2) = 7.44 + 67.54 = 75.0^\circ$, as given.

**Where marks are lost.** Using the standard equilibrium value $+52.7^\circ$ instead of
the value given in the question; or inverting the numerator so that the answer is the
$\alpha$ fraction.

### 28. Molar mass and hydrolysis yield of amylose **(multi-step)**

**Strategy.** Use the residue mass for the polymer and add one water for the terminal
groups; then convert the residue count to glucose mass.

**Working.** For a degree of polymerisation $n = 1500$ and a hexose residue mass of
$162.14\ \mathrm{g\ mol^{-1}}$:

$$
M = n M_\mathrm{res} + M_{\ce{H2O}}
= 1500(162.14) + 18.015
= 243\,228\ \mathrm{g\ mol^{-1}}
\approx 2.43\times10^{5}\ \mathrm{g\ mol^{-1}}.
$$

Complete hydrolysis converts each residue to glucose, so the mass yield is

$$
\frac{m(\ce{glucose})}{m(\ce{starch})}
= \frac{180.16}{162.14} = 1.111.
$$

For $1.00\ \mathrm{g}$ of polymer, $m(\ce{glucose}) = 1.111\ \mathrm{g}$.

**Answer.** $M \approx 2.43\times10^{5}\ \mathrm{g\ mol^{-1}}$ (about
$243\ \mathrm{kDa}$); complete hydrolysis of $1.00\ \mathrm{g}$ gives
$1.11\ \mathrm{g}$ of glucose.

**Check.** $1500$ residues of glucose would weigh $1500(180.16) = 270\,240\ \mathrm{g}$
per mole of chains; the polymer is lighter by $1499$ water molecules
($1499 \times 18.015 = 27\,004\ \mathrm{g}$), giving $243\,236\ \mathrm{g}$, consistent
with the result.

**Where marks are lost.** Adding $1500$ water molecules instead of one; or using
$180.16\ \mathrm{g\ mol^{-1}}$ as the residue mass and then multiplying by $1500$.

### 29. Iodine value of triolein

**Strategy.** Count the double bonds, convert to moles of iodine, and express per
$100\ \mathrm{g}$ of fat.

**Working.** Triolein has three *cis* double bonds, so one mole consumes three moles of
$\ce{I2}$:

$$
\mathrm{IV} = \frac{n_{\ce{I2}}M_{\ce{I2}}}{m_\mathrm{fat}}\times100
= \frac{3(253.8)}{885.4}\times100
= 86.0\ \mathrm{g\ I_2\ per\ 100\ g}.
$$

**Answer.** $\mathrm{IV} = 86.0\ \mathrm{g\ I_2\ per\ 100\ g}$ of triolein.

**Check.** The value lies in the range typical of a monounsaturated oil such as olive
oil ($80$–$90$). A fully saturated fat would give zero.

**Where marks are lost.** Using two moles of $\ce{I2}$ because "triolein" suggests three
fatty acids but only one double bond per chain is easy to miscount; or using the molar
mass of oleic acid ($282.46\ \mathrm{g\ mol^{-1}}$) instead of triolein.

### 30. DNA concentration from absorbance **(multi-step)**

**Strategy.** Correct for dilution, convert $A_{260}$ to mass concentration, divide by the
molar mass of the duplex, then convert to molecules per microlitre.

**Working.** For double-stranded DNA, $A_{260} = 1$ corresponds to
$50\ \mu\mathrm{g\ mL^{-1}}$. The measured dilution is $1:10$, so

$$
c_\mathrm{mass} = 0.310 \times 50\ \mu\mathrm{g\ mL^{-1}} \times 10
= 155\ \mu\mathrm{g\ mL^{-1}}.
$$

The molar mass of a $2000\ \mathrm{bp}$ duplex is approximately
$2000 \times 650 = 1.30\times10^{6}\ \mathrm{g\ mol^{-1}}$. Therefore

$$
c = \frac{155\times10^{-3}\ \mathrm{g\ L^{-1}}}{1.30\times10^{6}\ \mathrm{g\ mol^{-1}}}
= 1.19\times10^{-7}\ \mathrm{mol\ L^{-1}}.
$$

The number of molecules per microlitre is

$$
N = (1.19\times10^{-7}\ \mathrm{mol\ L^{-1}})(10^{-6}\ \mathrm{L})(6.022\times10^{23}\ \mathrm{mol^{-1}})
= 7.18\times10^{10}.
$$

**Answer.** $155\ \mu\mathrm{g\ mL^{-1}}$, $1.19\times10^{-7}\ \mathrm{M}$ and
$7.18\times10^{10}$ molecules per microlitre in the original sample.

**Check.** $155\ \mu\mathrm{g\ mL^{-1}}$ divided by $1.30\times10^{6}\ \mathrm{g\ mol^{-1}}$
is $1.19\times10^{-7}\ \mathrm{M}$; a $1\ \mu\mathrm{L}$ aliquot therefore contains
$1.19\times10^{-13}\ \mathrm{mol}$, which is $7.2\times10^{10}$ molecules. The order of
magnitude is typical of a plasmid preparation.

**Where marks are lost.** Forgetting the $1:10$ dilution; using the single-stranded DNA
factor $33\ \mu\mathrm{g\ mL^{-1}}$ or the RNA factor $40\ \mu\mathrm{g\ mL^{-1}}$; or
using $1000\ \mathrm{g\ mol^{-1}}$ per base pair instead of $650$.

### 31. Energy charge before and after stress **(multi-step)**

**Strategy.** Apply the energy-charge definition and recalculate with the new pool.

**Working.** The energy charge is

$$
\mathrm{EC} = \frac{[\ce{ATP}] + \tfrac12[\ce{ADP}]}
{[\ce{ATP}]+[\ce{ADP}]+[\ce{AMP}]}.
$$

Initial:

$$
\mathrm{EC} = \frac{3.0 + \tfrac12(0.50)}{3.0+0.50+0.10}
= \frac{3.25}{3.60} = 0.903.
$$

After stress:

$$
\mathrm{EC} = \frac{2.0 + \tfrac12(1.2)}{2.0+1.2+0.30}
= \frac{2.60}{3.50} = 0.743.
$$

**Answer.** $\mathrm{EC} = 0.903$ initially and $0.743$ after the ATP fall (dimensionless).

**Check.** The value lies between $0$ and $1$, and the direction is correct: a fall in ATP
with a rise in ADP and AMP lowers the energy charge. Healthy cells normally maintain
$0.80$–$0.95$, so the stressed value is below the normal range.

**Where marks are lost.** Counting ADP as a full ATP equivalent (using $[\ce{ADP}]$
rather than $\tfrac12[\ce{ADP}]$), or using AMP in the numerator.

### 32. Photon energy and photons per glucose **(multi-step)**

**Strategy.** Use $E = hc/\lambda$ for one photon, multiply by Avogadro's number for one
mole, then scale by the stoichiometry.

**Working.** With $h = 6.626\times10^{-34}\ \mathrm{J\ s}$, $c = 2.998\times10^{8}\ \mathrm{m\ s^{-1}}$
and $\lambda = 680\ \mathrm{nm} = 680\times10^{-9}\ \mathrm{m}$:

$$
E = \frac{hc}{\lambda}
= \frac{(6.626\times10^{-34})(2.998\times10^{8})}{680\times10^{-9}}
= 2.92\times10^{-19}\ \mathrm{J}.
$$

For one mole of photons:

$$
E_\mathrm{mol} = (2.92\times10^{-19})(6.022\times10^{23})
= 1.76\times10^{5}\ \mathrm{J\ mol^{-1}}
= 176\ \mathrm{kJ\ mol^{-1}}.
$$

One mole of glucose contains six moles of carbon, so fixing it requires
$6 \times 8 = 48\ \mathrm{mol}$ of photons:

$$
E_\mathrm{total} = 48(176\ \mathrm{kJ\ mol^{-1}})
= 8.44\times10^{3}\ \mathrm{kJ}
= 8.44\ \mathrm{MJ}.
$$

**Answer.** $2.92\times10^{-19}\ \mathrm{J}$ per photon, $176\ \mathrm{kJ\ mol^{-1}}$,
$48\ \mathrm{mol}$ of photons per mole of glucose, and $8.44\ \mathrm{MJ}$ of light
energy.

**Check.** The theoretical minimum of $8$ photons per $\ce{CO2}$ comes from four electrons
per $\ce{CO2}$ and two photons per electron (one at each photosystem). The factor of six
then gives $48$ photons per glucose.

**Where marks are lost.** Using $8$ photons per glucose instead of $8$ per $\ce{CO2}$;
converting nanometres to metres incorrectly; or forgetting to multiply by Avogadro's
number when asked for a mole of photons.

---

## Part D — Intermediate problems

### 33. Adding strong acid to a phosphate buffer **(multi-step)**

**Strategy.** Convert the added acid into a change in the ratio of the conjugate forms,
then compare the exact pH change with the capacity prediction.

**Working.** At pH $7.00$ and total phosphate $0.100\ \mathrm{M}$:

$$
\frac{[\ce{HPO4^{2-}}]}{[\ce{H2PO4-}]} = 10^{0.14} = 1.38,
$$

so $[\ce{HPO4^{2-}}] = 0.0580\ \mathrm{M}$ and $[\ce{H2PO4-}] = 0.0420\ \mathrm{M}$ in
$1.00\ \mathrm{L}$.

Adding $1.00\ \mathrm{mmol}$ $\ce{HCl}$ converts $1.00\ \mathrm{mmol}$ of
$\ce{HPO4^{2-}}$ to $\ce{H2PO4-}$:

$$
[\ce{HPO4^{2-}}] = 0.0570\ \mathrm{M},
\qquad
[\ce{H2PO4-}] = 0.0430\ \mathrm{M}.
$$

$$
\mathrm{pH} = 6.86 + \log_{10}\frac{0.0570}{0.0430}
= 6.86 + 0.122 = 6.982.
$$

The buffer capacity at the initial pH is

$$
\beta = 2.303\frac{(0.0580)(0.0420)}{0.100}
= 0.0561\ \mathrm{M\ pH^{-1}},
$$

so the predicted change is

$$
\Delta\mathrm{pH} = \frac{0.00100}{0.0561} = 0.0178.
$$

In $1.00\ \mathrm{L}$ of unbuffered water, $1.00\ \mathrm{mmol}$ $\ce{HCl}$ gives
$[\ce{H+}] = 1.00\times10^{-3}\ \mathrm{M}$ and pH $3.00$, a change of $4.00$ units.

**Answer.** The new pH is $6.982$ (a change of $0.018$ unit). The capacity is
$0.0561\ \mathrm{M\ pH^{-1}}$, predicting the same $0.018$-unit change. Unbuffered water
would fall to pH $3.00$, a change of $4.00$ units.

**Check.** The exact and capacity-predicted changes agree to two significant figures,
which is expected because the pH change is small relative to the buffer range. The
buffer reduces the pH change by a factor of about $225$.

**Where marks are lost.** Adding the acid to $\ce{H2PO4-}$ (the wrong direction, which
would raise the pH); using $1.00\ \mathrm{mmol}$ as a concentration without dividing by
$1.00\ \mathrm{L}$; or reporting the pH change as positive when the pH falls.

### 34. Charge and ion exchange of Asp-His-Lys-Gly **(multi-step)**

**Strategy.** Sum fractional charges at each pH, then locate the pH at which the sum is
zero.

**Working.** The groups are the N-terminus ($9.60$, base), C-terminus ($2.34$, acid), Asp
($3.86$, acid), His ($6.00$, base) and Lys ($10.53$, base).

At pH $7.40$:

$$
Q = \frac{1}{1+10^{7.40-9.60}}
+ \frac{1}{1+10^{7.40-6.00}}
+ \frac{1}{1+10^{7.40-10.53}}
- \frac{1}{1+10^{2.34-7.40}}
- \frac{1}{1+10^{3.86-7.40}},
$$

$$
Q = 0.994 + 0.0383 + 0.999 - 1.000 - 0.9997 = +0.031.
$$

At pH $6.00$:

$$
Q = 1.000 + 0.500 + 1.000 - 0.9995 - 0.9928 = +0.507.
$$

The charge falls through zero between pH $7.7$ and $7.8$; interpolation gives
$\mathrm{pI} \approx 7.78$. At pH $7.40$ the peptide is only $+0.03$, so a cation
exchanger would retain it very weakly at best and an anion exchanger would not retain it.
At pH $6.00$ it is net positive and binds a cation exchanger; above the $\mathrm{pI}$ it
becomes net negative and binds an anion exchanger.

**Answer.** $Q = +0.031\ e$ at pH $7.40$ and $Q = +0.507\ e$ at pH $6.00$;
$\mathrm{pI} \approx 7.78$ (dimensionless). At pH $7.40$ binding to a cation exchanger is very weak; at
pH $6.00$ the peptide binds a cation exchanger; above pH $7.78$ it binds an anion
exchanger.

**Check.** The pI is close to the average of the histidine and N-terminal pKa values,
$(6.00+9.60)/2 = 7.80$, which is the expected result when the Asp and Lys charges almost
cancel.

**Where marks are lost.** Omitting the lysine side chain (which would make the peptide
strongly negative), or treating histidine as fully protonated at pH $7.4$.

### 35. Competitive inhibition and the Cheng–Prusoff relation **(multi-step)**

**Strategy.** Use the Cheng–Prusoff relation to extract $K_\mathrm{i}$, then the
competitive-inhibition expression for $K_\mathrm{M}^\mathrm{app}$ and the
Michaelis–Menten equation.

**Working.** For a competitive inhibitor,

$$
K_\mathrm{i} = \frac{\mathrm{IC}_{50}}{1+[\ce{S}]/K_\mathrm{M}}
= \frac{12\ \mu\mathrm{M}}{1 + 2.0/2.0}
= 6.0\ \mu\mathrm{M}.
$$

At $[\ce{I}] = 18\ \mu\mathrm{M}$,

$$
\alpha = 1+\frac{[\ce{I}]}{K_\mathrm{i}} = 1+\frac{18}{6.0} = 4.0,
$$

$$
K_\mathrm{M}^\mathrm{app} = \alpha K_\mathrm{M} = 4.0(2.0\ \mathrm{mM})
= 8.0\ \mathrm{mM}.
$$

At $[\ce{S}] = 2.0\ \mathrm{mM}$:

$$
v = \frac{V_\mathrm{max}[\ce{S}]}{K_\mathrm{M}^\mathrm{app}+[\ce{S}]}
= \frac{(1.20)(2.0)}{8.0+2.0}
= 0.24\ \mu\mathrm{mol\ min^{-1}}.
$$

The uninhibited velocity at the same substrate concentration is
$1.20(2.0)/(2.0+2.0) = 0.60\ \mu\mathrm{mol\ min^{-1}}$, so the inhibited rate is
$0.24/0.60 = 0.40$, or $40\%$.

**Answer.** $K_\mathrm{i} = 6.0\ \mu\mathrm{M}$;
$K_\mathrm{M}^\mathrm{app} = 8.0\ \mathrm{mM}$ at $[\ce{I}] = 18\ \mu\mathrm{M}$;
$v = 0.24\ \mu\mathrm{mol\ min^{-1}}$, which is $40\%$ of the uninhibited rate.

**Check.** A competitive inhibitor can be displaced by substrate, so raising $[\ce{S}]$
from $2.0\ \mathrm{mM}$ towards saturation restores $V_\mathrm{max}$; $V_\mathrm{max}$ is
unchanged in the calculation.

**Where marks are lost.** Using $[\ce{S}] = 2.0$ without dividing by $K_\mathrm{M}$ in
the Cheng–Prusoff relation; using the uncompetitive expression
$K_\mathrm{M}/\alpha'$; or reporting the inhibited rate as a percentage of $V_\mathrm{max}$
rather than of the uninhibited rate at the same $[\ce{S}]$.

### 36. Hill coefficient and $K_\mathrm{d}$ from two points **(multi-step)**

**Strategy.** Use the linear form of the Hill equation and the two saturation points.

**Working.** The Hill equation is

$$
\frac{\theta}{1-\theta} = \left(\frac{[\ce{L}]}{K_\mathrm{d}}\right)^n.
$$

At $\theta = 0.10$, $[\ce{L}] = 1.0\ \mu\mathrm{M}$, so
$\theta/(1-\theta) = 0.1111$. At $\theta = 0.90$, $[\ce{L}] = 16\ \mu\mathrm{M}$, so
$\theta/(1-\theta) = 9.00$. Therefore

$$
n = \frac{\log_{10}(9.00/0.1111)}{\log_{10}(16/1.0)}
= \frac{\log_{10}81}{\log_{10}16}
= \frac{1.908}{1.204} = 1.58.
$$

Using the first point:

$$
0.1111 = \left(\frac{1.0}{K_\mathrm{d}}\right)^{1.58},
$$

$$
K_\mathrm{d} = \left(\frac{1}{0.1111}\right)^{1/1.58}
= 9^{0.633} = 4.0\ \mu\mathrm{M}.
$$

At $[\ce{L}] = 8.0\ \mu\mathrm{M}$:

$$
\left(\frac{8.0}{4.0}\right)^{1.58} = 2^{1.58} = 3.00,
\qquad
\theta = \frac{3.00}{1+3.00} = 0.75.
$$

**Answer.** $n = 1.58$ (dimensionless), $K_\mathrm{d} = 4.0\ \mu\mathrm{M}$ and
$\theta = 0.75$ (dimensionless) at $8.0\ \mu\mathrm{M}$.

**Check.** A Hill coefficient of $1.58$ indicates positive cooperativity but is not the
number of binding sites; the true site count must come from structure or binding
stoichiometry. The curve is steeper than a hyperbola but not infinitely sharp.

**Where marks are lost.** Using $90/10 = 9$ as the ratio without converting to
$\theta/(1-\theta)$ (which happens to give the same ratio here, but the method is wrong
in general); rounding $n$ to $2$ before calculating $K_\mathrm{d}$; or treating $K_\mathrm{d}$
as the concentration at half saturation for a cooperative system (it is, by definition of
this Hill form, but the Hill coefficient must be used consistently).

### 37. Concentration from optical rotation **(multi-step)**

**Strategy.** Rearrange the specific-rotation equation, convert units and scale to the
requested volume.

**Working.** The specific rotation is

$$
[\alpha]_\mathrm{D} = \frac{\alpha}{lc},
$$

so

$$
c = \frac{\alpha}{l[\alpha]_\mathrm{D}}
= \frac{3.16}{1.00 \times 52.7}
= 0.05996\ \mathrm{g\ mL^{-1}}.
$$

Converting to grams per litre:

$$
c = 0.05996\ \mathrm{g\ mL^{-1}} \times 1000\ \mathrm{mL\ L^{-1}}
= 59.96\ \mathrm{g\ L^{-1}} \approx 60.0\ \mathrm{g\ L^{-1}}.
$$

The mass in $250.0\ \mathrm{mL}$ is

$$
m = (59.96\ \mathrm{g\ L^{-1}})(0.2500\ \mathrm{L}) = 15.0\ \mathrm{g}.
$$

**Answer.** $c = 60.0\ \mathrm{g\ L^{-1}}$ and $m = 15.0\ \mathrm{g}$ in
$250.0\ \mathrm{mL}$.

**Check.** The concentration is close to the $50\ \mathrm{g\ L^{-1}}$ example in the
chapter, and the rotation scales linearly with concentration, as the equation requires.

**Where marks are lost.** Using $1.00\ \mathrm{cm}$ instead of $1.00\ \mathrm{dm}$ for
$l$ (a factor of $10$); or leaving the concentration in $\mathrm{g\ mL^{-1}}$ and
reporting $0.060\ \mathrm{g\ L^{-1}}$.

### 38. Starch hydrolysis and fermentation **(multi-step)**

**Strategy.** Convert starch mass to residue moles, then use the hydrolysis and
fermentation stoichiometry.

**Working.** Starch is a polymer of $\ce{C6H10O5}$ residues with
$M_\mathrm{res} = 162.14\ \mathrm{g\ mol^{-1}}$. For $5.00\ \mathrm{g}$:

$$
n_\mathrm{res} = \frac{5.00\ \mathrm{g}}{162.14\ \mathrm{g\ mol^{-1}}}
= 0.03084\ \mathrm{mol}.
$$

Hydrolysis adds one water per residue:

$$
m(\ce{glucose}) = (0.03084\ \mathrm{mol})(180.16\ \mathrm{g\ mol^{-1}})
= 5.56\ \mathrm{g}.
$$

Fermentation is

$$
\ce{C6H12O6 -> 2 C2H5OH + 2 CO2},
$$

so $n(\ce{ethanol}) = 2(0.03084) = 0.06168\ \mathrm{mol}$ and
$n(\ce{CO2}) = 0.06168\ \mathrm{mol}$:

$$
m(\ce{ethanol}) = (0.06168)(46.07) = 2.84\ \mathrm{g},
$$

$$
V(\ce{CO2}) = (0.06168\ \mathrm{mol})(22.414\ \mathrm{L\ mol^{-1}})
= 1.38\ \mathrm{L}.
$$

**Answer.** $5.56\ \mathrm{g}$ of glucose, $2.84\ \mathrm{g}$ of ethanol and
$1.38\ \mathrm{L}$ of $\ce{CO2}$ at STP.

**Check.** Carbon balance: $0.03084\ \mathrm{mol}$ of hexose contains
$0.1850\ \mathrm{mol}$ C; ethanol contains $2(0.06168) = 0.1234\ \mathrm{mol}$ C and
$\ce{CO2}$ contains $0.06168\ \mathrm{mol}$ C, total $0.1851\ \mathrm{mol}$, as required.

**Where marks are lost.** Using $180.16\ \mathrm{g\ mol^{-1}}$ as the starch residue
mass; forgetting the factor of two for ethanol and $\ce{CO2}$; or using the molar volume
at $25\ ^\circ\mathrm{C}$ ($24.5\ \mathrm{L\ mol^{-1}}$) while claiming STP.

### 39. Free-energy cost of the $\ce{Na+}$/$\ce{K+}$-ATPase **(multi-step)**

**Strategy.** Calculate the electrochemical free energy for each ion in the direction it
is pumped, multiply by the stoichiometry and sum.

**Working.** At $310\ \mathrm{K}$,

$$
RT = (8.314)(310) = 2.577\ \mathrm{kJ\ mol^{-1}}.
$$

For sodium export (inside to outside), the concentration term is
$RT\ln([\ce{Na+}]_\mathrm{out}/[\ce{Na+}]_\mathrm{in})$ and the electrical term is
$zF(\psi_\mathrm{out}-\psi_\mathrm{in}) = zF(0.070\ \mathrm{V})$:

$$
\Delta G_{\ce{Na}} = 2.577\ln\frac{150}{15} + (1)(96.485)(0.070)
= 5.935 + 6.754 = 12.69\ \mathrm{kJ\ mol^{-1}}.
$$

For three sodium ions: $3(12.69) = 38.07\ \mathrm{kJ}$.

For potassium import (outside to inside), the concentration term is
$RT\ln([\ce{K+}]_\mathrm{in}/[\ce{K+}]_\mathrm{out})$ and the electrical term is
$zF(\psi_\mathrm{in}-\psi_\mathrm{out}) = zF(-0.070\ \mathrm{V})$:

$$
\Delta G_{\ce{K}} = 2.577\ln\frac{150}{5} + (1)(96.485)(-0.070)
= 8.765 - 6.754 = 2.011\ \mathrm{kJ\ mol^{-1}}.
$$

For two potassium ions: $2(2.011) = 4.02\ \mathrm{kJ}$.

The total is $38.07 + 4.02 = 42.09\ \mathrm{kJ\ mol^{-1}}$ per cycle. The thermodynamic
efficiency is

$$
\eta = \frac{42.09}{50} = 0.842 = 84.2\%.
$$

**Answer.** $42.1\ \mathrm{kJ\ mol^{-1}}$ per pump cycle, with a thermodynamic efficiency
of $84.2\%$ relative to $\Delta G_\mathrm{ATP} = -50\ \mathrm{kJ\ mol^{-1}}$.

**Check.** The cost is less than the $50\ \mathrm{kJ\ mol^{-1}}$ released by ATP
hydrolysis, so one ATP can power the cycle. A negative total would mean the pump could
run backwards spontaneously, which is not the case.

**Where marks are lost.** Using the membrane potential with the wrong sign for sodium
export (which makes the pump look much cheaper); multiplying the potassium term by three;
or using $T = 298\ \mathrm{K}$ when the question specifies $310\ \mathrm{K}$.

### 40. Packing parameter and head-group area **(multi-step)**

**Strategy.** Evaluate $P = v/(a_0l_\mathrm{c})$ before and after the change and compare
with the boundary values.

**Working.** Initially,

$$
P = \frac{0.90\ \mathrm{nm^3}}{(0.60\ \mathrm{nm^2})(1.8\ \mathrm{nm})}
= \frac{0.90}{1.08} = 0.833.
$$

Since $0.5 < P < 1$, the lipid prefers a bilayer or vesicle. If the head-group area
doubles to $a_0 = 1.20\ \mathrm{nm^2}$,

$$
P = \frac{0.90}{(1.20)(1.8)} = 0.417.
$$

Since $1/3 < P < 1/2$, the preferred assembly is a cylindrical micelle.

**Answer.** Initially $P = 0.833$ (dimensionless), bilayer/vesicle; after doubling the
head-group area, $P = 0.417$ (dimensionless), cylindrical micelle.

**Check.** Increasing the head-group area increases the denominator and lowers $P$,
favouring higher curvature — exactly the trend expected when a bulky or charged head
group is introduced.

**Where marks are lost.** Inverting the ratio; using the bilayer boundary at $1/3$
instead of $1/2$; or treating $P$ as a length rather than a dimensionless number.

### 41. Base composition, hydrogen bonds and charge **(multi-step)**

**Strategy.** Use Chargaff's rules for a double-stranded molecule, then count base pairs
and phosphates.

**Working.** For double-stranded DNA, $A = T$ and $G = C$. If $A = 28.0\%$, then
$T = 28.0\%$ and the remaining $44.0\%$ is split equally between $G$ and $C$:

$$
G = C = 22.0\%.
$$

For $1000\ \mathrm{bp}$, there are $280$ A–T pairs and $220$ G–C pairs. Each A–T pair has
two hydrogen bonds and each G–C pair has three:

$$
N_{\ce{H}} = 280(2) + 220(3) = 560 + 660 = 1220.
$$

There are two phosphodiester linkages per base pair, so a $1000\ \mathrm{bp}$ duplex has
$2000$ phosphates. At pH $7.4$ each phosphodiester carries one negative charge, so the
net charge is $-2000$ (ignoring terminal groups).

**Answer.** $A = T = 28.0\%$, $G = C = 22.0\%$; $1220$ hydrogen bonds; net charge
$-2000\ e$ at pH $7.4$.

**Check.** The percentages sum to $100\%$. The hydrogen-bond count is dominated by the
G–C pairs even though they are fewer, which is why GC-rich DNA melts at higher
temperature.

**Where marks are lost.** Treating $1000\ \mathrm{bp}$ as $1000$ bases; using three
hydrogen bonds for A–T; or counting one phosphate per base pair instead of two.

### 42. ATP yield from glucose and glycogen **(multi-step)**

**Strategy.** Build a full inventory of substrate-level phosphorylation and reduced
cofactors, then apply the $\mathrm{P/O}$ values with the chosen shuttle.

**Working.** Per glucose:

| Stage | ATP/GTP | $\ce{NADH}$ | $\ce{FADH2}$ |
|---|---:|---:|---:|
| Glycolysis (net) | 2 | 2 | 0 |
| Pyruvate dehydrogenase | 0 | 2 | 0 |
| Krebs cycle | 2 | 6 | 2 |
| **Total** | **4** | **10** | **2** |

With the malate–aspartate shuttle, all $10$ $\ce{NADH}$ are counted at $2.5$ ATP:

$$
n_\mathrm{ATP} = 4 + 10(2.5) + 2(1.5) = 4 + 25 + 3 = 32.
$$

With the glycerol-3-phosphate shuttle, the two cytosolic $\ce{NADH}$ are delivered as
$\ce{FADH2}$, so there are $8$ $\ce{NADH}$ and $4$ $\ce{FADH2}$:

$$
n_\mathrm{ATP} = 4 + 8(2.5) + 4(1.5) = 4 + 20 + 6 = 30.
$$

For one glucose residue released from glycogen, the hexokinase step is bypassed, so
glycolysis yields $3$ ATP rather than $2$. The substrate-level total becomes
$3 + 2 = 5$ ATP equivalents, with the same $10$ $\ce{NADH}$ and $2$ $\ce{FADH2}$:

$$
n_\mathrm{ATP} = 5 + 25 + 3 = 33\ \text{(malate--aspartate)},
$$

$$
n_\mathrm{ATP} = 5 + 20 + 6 = 31\ \text{(glycerol-3-phosphate)}.
$$

**Assumptions.** Complete aerobic oxidation; $\mathrm{P/O} = 2.5$ for $\ce{NADH}$ and
$1.5$ for $\ce{FADH2}$; GTP is equivalent to ATP; the $\mathrm{P/O}$ values already
include the cost of phosphate transport; no proton leak, no alternative
NADH dehydrogenase, no substrate cycles and no transport costs for pyruvate or
adenine nucleotides. The malate–aspartate shuttle transfers cytosolic reducing power as
mitochondrial $\ce{NADH}$; the glycerol-3-phosphate shuttle transfers it as
$\ce{FADH2}$. The glycogen figure assumes that the residue is released as
glucose-1-phosphate from a non-reducing end and is not a branch-point glucose released
as free glucose; a branch-point residue would require hexokinase and would lose the
one-ATP saving.

**Answer.** $32$ ATP per glucose with the malate–aspartate shuttle, $30$ ATP with the
glycerol-3-phosphate shuttle; $33$ and $31$ ATP respectively per glucose residue from
glycogen.

**Check.** The difference between the two shuttles is exactly $2$ ATP, the difference
between two $\ce{NADH}$ at $2.5$ and two $\ce{FADH2}$ at $1.5$. Glycogen gives exactly
one more ATP because it saves one hexokinase ATP.

**Where marks are lost.** Using the gross $4$ ATP of glycolysis rather than the net $2$;
forgetting the two PDH $\ce{NADH}$; counting GTP separately from ATP without saying so;
or using $3$ and $2$ as $\mathrm{P/O}$ values while quoting the modern total.

### 43. Calvin-cycle stoichiometry for $10\ \mathrm{mol}$ $\ce{CO2}$ **(multi-step)**

**Strategy.** Scale the per-$\ce{CO2}$ requirements, then convert carbon to glucose and
photons.

**Working.** The Calvin cycle consumes $3$ ATP and $2$ NADPH per $\ce{CO2}$:

$$
n_\mathrm{ATP} = 10.0(3) = 30.0\ \mathrm{mol},
\qquad
n_\mathrm{NADPH} = 10.0(2) = 20.0\ \mathrm{mol}.
$$

Six $\ce{CO2}$ are needed per glucose, so

$$
n_\mathrm{glucose} = \frac{10.0}{6} = 1.667\ \mathrm{mol},
\qquad
m_\mathrm{glucose} = 1.667(180.16) = 300\ \mathrm{g}.
$$

At the theoretical minimum of $8$ photons per $\ce{CO2}$:

$$
n_\gamma = 8(10.0) = 80.0\ \mathrm{mol},
$$

$$
E_\gamma = 80.0(176\ \mathrm{kJ\ mol^{-1}})
= 1.41\times10^{4}\ \mathrm{kJ}
= 14.1\ \mathrm{MJ}.
$$

The free energy stored in $1.667\ \mathrm{mol}$ of glucose is

$$
\Delta G_\mathrm{stored} = 1.667(2870\ \mathrm{kJ\ mol^{-1}})
= 4.78\times10^{3}\ \mathrm{kJ}
= 4.78\ \mathrm{MJ}.
$$

The thermodynamic efficiency is

$$
\eta = \frac{4.78}{14.1} = 0.340 = 34.0\%.
$$

**Answer.** $30.0\ \mathrm{mol}$ ATP, $20.0\ \mathrm{mol}$ NADPH, $1.67\ \mathrm{mol}$
($300\ \mathrm{g}$) glucose, $80.0\ \mathrm{mol}$ of $680\ \mathrm{nm}$ photons and
$14.1\ \mathrm{MJ}$ of light; the maximum thermodynamic efficiency is $34.0\%$.

**Check.** The ATP : NADPH ratio is $30:20 = 3:2$, as required. The glucose mass is
$1.667 \times 180.16 = 300\ \mathrm{g}$, consistent with $10$ mol of carbon.

**Where marks are lost.** Using $3$ ATP and $2$ NADPH per glucose rather than per
$\ce{CO2}$; using $6$ photons per glucose instead of $8$ per $\ce{CO2}$; or quoting the
efficiency without converting both energies to the same basis.

### 44. Relative quantification by qPCR **(multi-step)**

**Strategy.** Calculate $\Delta C_t$ for each sample, subtract to get $\Delta\Delta C_t$,
then apply $2^{-\Delta\Delta C_t}$.

**Working.** For the control:

$$
\Delta C_{t,\mathrm{control}} = 24.0 - 18.0 = 6.0.
$$

For the treated sample:

$$
\Delta C_{t,\mathrm{treated}} = 26.0 - 18.5 = 7.5.
$$

Therefore

$$
\Delta\Delta C_t = 7.5 - 6.0 = 1.5,
$$

and the fold change is

$$
2^{-\Delta\Delta C_t} = 2^{-1.5} = 0.354.
$$

**Answer.** $\Delta\Delta C_t = 1.5$ cycles and the fold change is $0.354$
(dimensionless): the target is reduced to $35.4\%$ of the control, a $2.83$-fold
decrease.

**Check.** A $\Delta\Delta C_t$ of $1.5$ lies between one cycle (factor $2$) and two
cycles (factor $4$), so a $2.8$-fold change is reasonable. The reference gene corrects
for differences in input and amplification.

**Where marks are lost.** Subtracting in the wrong order (which gives $2^{+1.5} = 2.83$
and the wrong direction); using $C_t$ values without the reference correction; or
assuming equal efficiencies when the question does not state it.

---

## Part E — Advanced problems

### 45. Osmotic pressure from water activity **(multi-step)**

**Strategy.** Use the exact logarithmic relation between water activity and osmotic
pressure, then convert to osmolarity.

**Working.** With $a_\mathrm{w} = 0.980$, $V_\mathrm{m} = 1.8\times10^{-5}\ \mathrm{m^3\ mol^{-1}}$
and $T = 298.15\ \mathrm{K}$:

$$
RT = (8.314)(298.15) = 2.4788\times10^{3}\ \mathrm{J\ mol^{-1}},
$$

$$
\frac{RT}{V_\mathrm{m}}
= \frac{2.4788\times10^{3}}{1.8\times10^{-5}}
= 1.377\times10^{8}\ \mathrm{Pa}.
$$

$$
\ln(0.980) = -0.02020,
$$

$$
\pi = -\frac{RT}{V_\mathrm{m}}\ln a_\mathrm{w}
= -(1.377\times10^{8})(-0.02020)
= 2.78\times10^{6}\ \mathrm{Pa}
= 2.78\ \mathrm{MPa}
= 27.8\ \mathrm{bar}.
$$

The effective osmolarity is

$$
C_\mathrm{eff} = \frac{\pi}{RT}
= \frac{2.78\times10^{6}}{2.4788\times10^{3}}
= 1.12\times10^{3}\ \mathrm{mol\ m^{-3}}
= 1.12\ \mathrm{osmol\ L^{-1}}.
$$

**Answer.** $\pi = 2.78\ \mathrm{MPa} = 27.8\ \mathrm{bar}$, equivalent to an effective
osmolarity of $1.12\ \mathrm{osmol\ L^{-1}}$.

**Check.** $0.9\%$ $\ce{NaCl}$ has an osmolarity of $308\ \mathrm{mOsm\ L^{-1}}$, so
seawater is about $3.6$ times more concentrated. The pressure of $0.9\%$ saline at
$298\ \mathrm{K}$ is
$\pi = (308)(8.314)(298.15) = 7.63\times10^{5}\ \mathrm{Pa} = 0.763\ \mathrm{MPa}$,
about $3.6$ times smaller, consistent.

**Where marks are lost.** Dropping the minus sign and reporting a negative pressure;
using $\ln(1/a_\mathrm{w})$ but then treating the result as a concentration; or using
$V_\mathrm{m}$ in litres instead of cubic metres.

### 46. Two-state protein unfolding **(multi-step)**

**Strategy.** Use $\Delta G = \Delta H - T\Delta S$, $T_\mathrm{m} = \Delta H/\Delta S$
and $K = e^{-\Delta G/RT}$ for the fraction folded.

**Working.** For unfolding, $\Delta H^\circ = +220\ \mathrm{kJ\ mol^{-1}}$ and
$\Delta S^\circ = +650\ \mathrm{J\ K^{-1}\ mol^{-1}} = +0.650\ \mathrm{kJ\ K^{-1}\ mol^{-1}}$.

$$
T_\mathrm{m} = \frac{\Delta H^\circ}{\Delta S^\circ}
= \frac{220\ \mathrm{kJ\ mol^{-1}}}{0.650\ \mathrm{kJ\ K^{-1}\ mol^{-1}}}
= 338.5\ \mathrm{K}
= 65.3\ ^\circ\mathrm{C}.
$$

At $298.15\ \mathrm{K}$:

$$
\Delta G^\circ = 220 - (298.15)(0.650)
= 220 - 193.8 = 26.2\ \mathrm{kJ\ mol^{-1}}.
$$

The unfolding equilibrium constant is

$$
K = e^{-\Delta G^\circ/RT}
= e^{-26\,200/(8.314 \times 298.15)}
= e^{-10.57}
= 2.57\times10^{-5}.
$$

The fraction folded is

$$
f_\mathrm{folded} = \frac{1}{1+K} = \frac{1}{1+2.57\times10^{-5}} = 0.999974.
$$

At $310.15\ \mathrm{K}$:

$$
\Delta G^\circ = 220 - (310.15)(0.650) = 18.4\ \mathrm{kJ\ mol^{-1}},
$$

$$
K = e^{-18\,400/(8.314 \times 310.15)}
= e^{-7.14} = 7.95\times10^{-4},
$$

$$
f_\mathrm{folded} = \frac{1}{1+7.95\times10^{-4}} = 0.99921.
$$

**Answer.** $T_\mathrm{m} = 338.5\ \mathrm{K} = 65.3\ ^\circ\mathrm{C}$;
$\Delta G^\circ = 26.2\ \mathrm{kJ\ mol^{-1}}$ and $f_\mathrm{folded} = 0.99997$
(dimensionless) at $298.15\ \mathrm{K}$; $\Delta G^\circ = 18.4\ \mathrm{kJ\ mol^{-1}}$
and $f_\mathrm{folded} = 0.9992$ (dimensionless) at $310.15\ \mathrm{K}$.

**Check.** The protein is stable at both temperatures (positive $\Delta G$ for unfolding,
$T < T_\mathrm{m}$), but much closer to the melting point at $310\ \mathrm{K}$, so the
folded fraction falls. At $T_\mathrm{m}$, $\Delta G = 0$ and $f_\mathrm{folded} = 0.5$ by
definition.

**Where marks are lost.** Using degrees Celsius in $\Delta G = \Delta H - T\Delta S$;
setting $T_\mathrm{m} = \Delta H/\Delta S$ in joules but inserting $\Delta H$ in
kilojoules; or defining $K$ as folding rather than unfolding and inverting the fraction.

### 47. Identifying an inhibition type from data **(multi-step)**

**Strategy.** Calculate the Lineweaver–Burk slopes and intercepts for both data sets and
compare them.

**Working.** The reciprocal values are:

| $[\ce{S}]$ / mM | $1/[\ce{S}]$ | Control $v$ | Control $1/v$ | Inhibited $v$ | Inhibited $1/v$ |
|---:|---:|---:|---:|---:|---:|
| 1.0 | 1.00 | 0.400 | 2.50 | 0.267 | 3.75 |
| 2.0 | 0.500 | 0.600 | 1.667 | 0.343 | 2.917 |
| 4.0 | 0.250 | 0.800 | 1.250 | 0.400 | 2.500 |

Control slope:

$$
\frac{2.50-1.250}{1.00-0.250} = \frac{1.25}{0.75} = 1.667.
$$

Inhibited slope:

$$
\frac{3.75-2.50}{1.00-0.250} = \frac{1.25}{0.75} = 1.667.
$$

The slopes are equal, so the lines are parallel: the inhibition is **uncompetitive**.
The control intercept is $2.50 - 1.667(1.00) = 0.833$, giving
$V_\mathrm{max} = 1/0.833 = 1.20\ \mu\mathrm{mol\ min^{-1}}$. The inhibited intercept is
$3.75 - 1.667(1.00) = 2.083$, giving
$V_\mathrm{max}^\mathrm{app} = 0.480\ \mu\mathrm{mol\ min^{-1}}$ and
$K_\mathrm{M}^\mathrm{app} = \text{slope}\times V_\mathrm{max}^\mathrm{app} = (1.667)(0.480) = 0.800\ \mathrm{mM}$.

The uncompetitive factor is

$$
\alpha' = \frac{V_\mathrm{max}}{V_\mathrm{max}^\mathrm{app}}
= \frac{1.20}{0.480} = 2.50
= 1+\frac{[\ce{I}]}{K_\mathrm{i}'},
$$

so

$$
K_\mathrm{i}' = \frac{15\ \mu\mathrm{M}}{2.50-1} = 10.0\ \mu\mathrm{M}.
$$

At $[\ce{S}] = 4.0\ \mathrm{mM}$, the inhibited velocity is $0.400$ and the control is
$0.800$, so the fraction is $0.500$.

**Answer.** Uncompetitive inhibition; $K_\mathrm{i}' = 10.0\ \mu\mathrm{M}$;
$v = 0.400\ \mu\mathrm{mol\ min^{-1}}$ at $[\ce{S}] = 4.0\ \mathrm{mM}$, which is $50.0\%$
of the control.

**Check.** For uncompetitive inhibition, $V_\mathrm{max}/K_\mathrm{M}$ is unchanged:
$1.20/2.0 = 0.600$ and $0.480/0.800 = 0.600$. That is exactly why the reciprocal lines are
parallel.

**Where marks are lost.** Calling the pattern mixed because both $K_\mathrm{M}$ and
$V_\mathrm{max}$ changed; using the intercept ratio for $\alpha'$ instead of the
$V_\mathrm{max}$ ratio; or thinking that an uncompetitive inhibitor can be overcome by
raising $[\ce{S}]$ (it cannot).

### 48. Branching in amylopectin **(multi-step)**

**Strategy.** Convert residue count to branch points, use the tree relation between
branch points and chain ends, then compute molar mass.

**Working.** With one branch point per $25$ residues:

$$
B = \frac{10\,000}{25} = 400.
$$

A branched tree with $B$ branch points has $B+1$ chain ends that are not the reducing
end, so the number of non-reducing ends is $401$. There is exactly one reducing end per
molecule.

The molar mass is

$$
M = 10\,000(162.14) + 18.015
= 1\,621\,418\ \mathrm{g\ mol^{-1}}
\approx 1.62\times10^{6}\ \mathrm{g\ mol^{-1}}
\approx 1.62\ \mathrm{MDa}.
$$

**Answer.** $400$ branch points, $401$ non-reducing ends, one reducing end and
$M \approx 1.62\ \mathrm{MDa}$.

**Check.** A linear chain of $10\,000$ residues would have one non-reducing end and one
reducing end. Each branch adds one non-reducing end, so $400$ branches give $401$, as
required. The mass is about $10\,000 \times 162\ \mathrm{g\ mol^{-1}}$, consistent.

**Where marks are lost.** Reporting $400$ non-reducing ends (forgetting the main chain
end); counting $400$ reducing ends; or treating each branch point as a separate molecule.

**Glycogen.** Glycogen is more highly branched, with a branch point every $8$–$12$
residues rather than every $25$. For the same $10\,000$ residues it would have roughly
$800$–$1250$ branch points and therefore $800$–$1250$ non-reducing ends. More ends mean
more sites for glycogen phosphorylase and faster mobilisation, which suits the sudden
energy demand of muscle and liver.

### 49. Thermodynamic $T_\mathrm{m}$ and salt correction **(multi-step)**

**Strategy.** Use the two-state expression for $T_\mathrm{m}$, then $\Delta G = \Delta H - T\Delta S$,
then the empirical salt correction.

**Working.** Assume non-self-complementary strands, so the factor of $4$ in
$C_T/4$ applies. With $\Delta H^\circ = -400.0\ \mathrm{kJ\ mol^{-1}}$,
$\Delta S^\circ = -1100\ \mathrm{J\ K^{-1}\ mol^{-1}}$ and $C_T = 4.0\ \mu\mathrm{M}$:

$$
\frac{C_T}{4} = 1.0\times10^{-6}\ \mathrm{M},
\qquad
R\ln\frac{C_T}{4} = (8.314)\ln(1.0\times10^{-6})
= -114.9\ \mathrm{J\ K^{-1}\ mol^{-1}}.
$$

$$
T_\mathrm{m} = \frac{\Delta H^\circ}{\Delta S^\circ + R\ln(C_T/4)}
= \frac{-400\,000}{-1100 - 114.9}
= \frac{-400\,000}{-1214.9}
= 329.3\ \mathrm{K}
= 56.1\ ^\circ\mathrm{C}.
$$

At $310\ \mathrm{K}$:

$$
\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ
= -400\,000 - (310.15)(-1100)
= -58\,835\ \mathrm{J\ mol^{-1}}
= -58.8\ \mathrm{kJ\ mol^{-1}}.
$$

The negative $\Delta G^\circ$ means the duplex is stable at $310\ \mathrm{K}$, which is
below $T_\mathrm{m}$. At $0.050\ \mathrm{M}$ $\ce{NaCl}$:

$$
\Delta T_\mathrm{m} = 16.6\log_{10}(0.050) = 16.6(-1.301) = -21.6\ ^\circ\mathrm{C},
$$

$$
T_\mathrm{m}(0.050\ \mathrm{M}) = 56.1 - 21.6 = 34.5\ ^\circ\mathrm{C}.
$$

**Answer.** $T_\mathrm{m} = 329.3\ \mathrm{K} = 56.1\ ^\circ\mathrm{C}$ at
$1\ \mathrm{M}$ $\ce{NaCl}$; $\Delta G^\circ = -58.8\ \mathrm{kJ\ mol^{-1}}$ at
$310\ \mathrm{K}$; $T_\mathrm{m} = 34.5\ ^\circ\mathrm{C}$ at $0.050\ \mathrm{M}$
$\ce{NaCl}$.

**Check.** Lowering the salt concentration stabilises the separated strands by reducing
counterion screening, so $T_\mathrm{m}$ should fall; a $22\ ^\circ\mathrm{C}$ fall is
consistent with the empirical correction. The high-concentration limit
$\Delta H/\Delta S = 400\,000/1100 = 363.6\ \mathrm{K} = 90.5\ ^\circ\mathrm{C}$ is the
concentration-independent estimate; the $C_T$ term lowers it to $56\ ^\circ\mathrm{C}$,
as it must for a bimolecular duplex.

**Where marks are lost.** Adding the salt correction to $T_\mathrm{m}$ instead of
subtracting it; using $310\ \mathrm{K}$ instead of $310.15\ \mathrm{K}$ (a negligible
difference here, but inconsistent); or inserting $\Delta S$ in $\mathrm{kJ}$ while
$\Delta H$ is in $\mathrm{J}$.

### 50. ATP yield from glucose and palmitate **(multi-step)**

**Strategy.** Do the full inventory for each fuel, apply the $\mathrm{P/O}$ values,
subtract activation costs and compare on a per-gram basis.

**Working.** For glucose with the malate–aspartate shuttle, glycolysis gives a net
$2$ ATP and $2$ NADH, PDH gives $2$ NADH, and the Krebs cycle gives $6$ NADH,
$2$ FADH$_2$ and $2$ GTP. The substrate-level total is $4$ ATP equivalents, so

$$
n_\mathrm{ATP} = 4 + 10(2.5) + 2(1.5) = 32.
$$

For palmitate (16:0): activation to palmitoyl-CoA costs $2$ ATP equivalents.
Seven $\beta$-oxidation cycles give $7$ $\ce{FADH2}$, $7$ $\ce{NADH}$ and $8$ acetyl-CoA.
Each acetyl-CoA gives $10$ ATP ($3$ $\ce{NADH}$, $1$ $\ce{FADH2}$ and $1$ GTP):

$$
n_\mathrm{ATP} = 8(10) + 7(1.5) + 7(2.5) - 2
= 80 + 10.5 + 17.5 - 2 = 106.
$$

Per gram:

$$
\frac{32}{180.16} = 0.178\ \mathrm{ATP\ g^{-1}},
\qquad
\frac{106}{256.42} = 0.413\ \mathrm{ATP\ g^{-1}}.
$$

The ratio is $0.413/0.178 = 2.33$.

Historically, with $\mathrm{P/O} = 3$ and $2$, glucose gives $38$ ATP and palmitate
gives $129$ ATP:

$$
8(12) + 7(2) + 7(3) - 2 = 129.
$$

Per gram, $38/180.16 = 0.211$ and $129/256.42 = 0.503$, a ratio of $2.38$. The ratio is
almost unchanged because both fuels are affected by the same change in proton accounting;
the absolute values are not.

**Answer.** $32$ ATP per glucose and $106$ ATP per palmitate; $0.178$ and
$0.413\ \mathrm{ATP\ g^{-1}}$, so palmitate gives $2.33$ times more ATP per gram. The
historical values were $38$ and $129$ ATP, or $0.211$ and $0.503\ \mathrm{ATP\ g^{-1}}$.

**Check.** On a molar basis palmitate gives $106/32 = 3.31$ times as much ATP as glucose;
the per-gram advantage is smaller ($2.33$) because palmitate has a higher molar mass.
This is the expected order: fat is the denser fuel but not three times denser per gram.

**Where marks are lost.** Forgetting the $-2$ ATP activation cost; using $8$ $\beta$-oxidation
cycles instead of $7$; or quoting $129$ without saying that it uses integer $\mathrm{P/O}$
values.

### 51. Maximum efficiency of photosynthesis **(multi-step)**

**Strategy.** Compare the free energy stored in glucose with the energy of the photons
required, at two photon stoichiometries.

**Working.** One mole of glucose requires $6$ mol $\ce{CO2}$. At $8$ photons per
$\ce{CO2}$:

$$
n_\gamma = 6(8) = 48\ \mathrm{mol\ photons}.
$$

The energy of $48$ mol of $680\ \mathrm{nm}$ photons is

$$
E_\mathrm{in} = 48(176\ \mathrm{kJ\ mol^{-1}})
= 8.448\times10^{3}\ \mathrm{kJ}
= 8.45\ \mathrm{MJ}.
$$

The free energy stored is $2870\ \mathrm{kJ\ mol^{-1}} = 2.87\ \mathrm{MJ\ mol^{-1}}$.
Therefore

$$
\eta_8 = \frac{2870}{8448} = 0.340 = 34.0\%.
$$

At $10$ photons per $\ce{CO2}$:

$$
n_\gamma = 60\ \mathrm{mol},
\qquad
E_\mathrm{in} = 60(176) = 10\,560\ \mathrm{kJ} = 10.56\ \mathrm{MJ},
$$

$$
\eta_{10} = \frac{2870}{10\,560} = 0.272 = 27.2\%.
$$

Blue light at $430\ \mathrm{nm}$ has a larger photon energy:

$$
E = \frac{hc}{\lambda}
= \frac{(6.626\times10^{-34})(2.998\times10^{8})}{430\times10^{-9}}
= 4.62\times10^{-19}\ \mathrm{J}
= 278\ \mathrm{kJ\ mol^{-1}}.
$$

But the antenna pigments transfer excitation to the reaction centre, whose traps absorb
at about $680$ and $700\ \mathrm{nm}$. The excess energy of a blue photon is dissipated
as heat before charge separation, so it does not increase the free energy stored per
electron. Using the $430\ \mathrm{nm}$ energy in the numerator would overestimate the
efficiency; the correct basis is the energy delivered to the reaction centres, not the
energy absorbed by the antenna. In practice, excess blue light can also cause
photoinhibition.

**Answer.** $34.0\%$ at $8$ photons per $\ce{CO2}$ and $27.2\%$ at $10$ photons per
$\ce{CO2}$. Blue light does not increase the efficiency because the extra photon energy
is dissipated as heat during relaxation to the $680/700\ \mathrm{nm}$ reaction-centre
traps.

**Check.** The theoretical maximum of about one third agrees with the chapter's estimate
of $478\ \mathrm{kJ}$ stored per mole of $\ce{CO2}$ against $1.4\ \mathrm{MJ}$ of light
per mole of $\ce{CO2}$ at $8$ photons: $478/1408 = 0.34$.

**Where marks are lost.** Using $6$ photons per glucose instead of $48$; using
$430\ \mathrm{nm}$ photon energy together with $680\ \mathrm{nm}$ stoichiometry; or
forgetting that the stored energy is per mole of glucose while the input is per mole of
photons.

### 52. Time and energy cost of gene expression **(multi-step)**

**Strategy.** Divide gene and protein lengths by the respective rates, multiply residues
by the ATP cost, then use first-order turnover for the synthesis rate.

**Working.** The gene is $12\ \mathrm{kb} = 12\,000\ \mathrm{nt}$. At
$50\ \mathrm{nt\ s^{-1}}$:

$$
t_\mathrm{transcription} = \frac{12\,000\ \mathrm{nt}}{50\ \mathrm{nt\ s^{-1}}}
= 240\ \mathrm{s} = 4.00\ \mathrm{min}.
$$

For $400$ residues at $18$ residues per second:

$$
t_\mathrm{translation} = \frac{400}{18\ \mathrm{s^{-1}}}
= 22.2\ \mathrm{s}.
$$

The ATP-equivalent cost, at $4$ per residue, is

$$
n_\mathrm{ATP} = 4(400) = 1600.
$$

For a half-life of $4.0\ \mathrm{h}$, the first-order degradation constant is

$$
k_\mathrm{d} = \frac{\ln 2}{t_{1/2}}
= \frac{0.693}{4.0\ \mathrm{h}}
= 0.173\ \mathrm{h^{-1}}.
$$

At steady state, synthesis balances degradation:

$$
\frac{\mathrm{d}[P]}{\mathrm{d}t} = k_\mathrm{s} - k_\mathrm{d}[P] = 0,
\qquad
k_\mathrm{s} = k_\mathrm{d}[P]
= (0.173\ \mathrm{h^{-1}})(50\ \mu\mathrm{M})
= 8.66\ \mu\mathrm{M\ h^{-1}}.
$$

**Answer.** Transcription takes $240\ \mathrm{s}$ ($4.00\ \mathrm{min}$), translation
$22.2\ \mathrm{s}$, and the protein costs $1600$ ATP equivalents. To maintain
$50\ \mu\mathrm{M}$ with a $4.0\ \mathrm{h}$ half-life requires synthesis of
$8.66\ \mu\mathrm{M\ h^{-1}}$.

**Check.** The synthesis rate times the half-life gives
$8.66 \times 4.0 / \ln 2 = 50\ \mu\mathrm{M}$, as required. The transcription time is
much longer than the translation time because the gene is much longer than the protein.

**Where marks are lost.** Using $12\ \mathrm{kb}$ as $12\,000\ \mathrm{bp}$ but then
forgetting that only one strand is transcribed (the transcript is still $12\,000\ \mathrm{nt}$,
so this is a conceptual rather than numerical slip); using $2$ ATP per residue instead of
$4$; or treating the half-life as a rate constant without taking $\ln 2$.

---

## Part F — Multiple-choice self-check

### 53. Neutral pH at $37\ ^\circ\mathrm{C}$

**Strategy.** Use the temperature dependence of $K_\mathrm{w}$ and the definition of
neutrality, $[\ce{H+}] = [\ce{OH-}]$.

**Working.** At $37\ ^\circ\mathrm{C}$, $K_\mathrm{w} \approx 2.4\times10^{-14}$. For pure
water,

$$
[\ce{H+}] = [\ce{OH-}] = \sqrt{K_\mathrm{w}}
= \sqrt{2.4\times10^{-14}} = 1.55\times10^{-7}\ \mathrm{M},
$$

$$
\mathrm{pH} = -\log_{10}(1.55\times10^{-7}) = 6.81.
$$

Equivalently, $\mathrm{p}K_\mathrm{w} = 13.62$ and neutral pH is
$\tfrac12(13.62) = 6.81$.

**Answer.** **B**, pH $6.81$ (dimensionless).

**Check.** Autoprotolysis is endothermic, so $K_\mathrm{w}$ rises with temperature and
neutral pH falls below $7.00$; $6.81$ is therefore the expected direction and magnitude.

**Best distractor.** A ($7.00$) is correct only at $25\ ^\circ\mathrm{C}$, where
$K_\mathrm{w} = 1.0\times10^{-14}$. C ($7.40$) is normal blood pH, which is alkaline
relative to neutral at $37\ ^\circ\mathrm{C}$. D ($6.10$) is the $\mathrm{p}K_\mathrm{a}$
of the bicarbonate buffer at $37\ ^\circ\mathrm{C}$.

**Where marks are lost.** Using $7.00$ at every temperature, or confusing blood pH with
the neutral point.

### 54. Peptide with charge near $+2$ at pH $7.4$

**Strategy.** Sum the fractional charges of the termini and side chains; a net charge
near $+2$ requires three positive groups and one negative group.

**Working.** For Gly-Lys-Arg at pH $7.4$:

$$
Q = \frac{1}{1+10^{7.4-9.60}}
+ \frac{1}{1+10^{7.4-10.53}}
+ \frac{1}{1+10^{7.4-12.48}}
- \frac{1}{1+10^{2.34-7.4}},
$$

$$
Q = 0.994 + 0.999 + 0.999 - 1.000 = +1.99.
$$

The N-terminus and the two basic side chains are almost fully protonated; only the
C-terminus is negative.

**Answer.** **B** (Gly-Lys-Arg), net charge $+1.99$ (dimensionless).

**Check.** Gly-His-Lys gives $0.994 + 0.038 + 0.999 - 1.000 = +1.03$, not $+2$, because
histidine is only $3.8\%$ protonated at pH $7.4$. Gly-Asp-Lys and Gly-Lys-Glu each have
one acidic side chain and are near neutral.

**Best distractor.** C (Gly-His-Lys) looks dibasic, but histidine has
$\mathrm{p}K_\mathrm{a} = 6.00$, so it contributes about $+0.04$ rather than $+1$.

**Where marks are lost.** Counting histidine as fully protonated, or forgetting that the
C-terminus contributes $-1$.

### 55. Effect of a competitive inhibitor

**Strategy.** Classify by the species the inhibitor binds, then translate that into the
apparent constants and the reciprocal plot.

**Working.** A competitive inhibitor binds the free enzyme at the active site. Saturating
substrate displaces it, so $V_\mathrm{max}$ is unchanged. The apparent Michaelis constant
is

$$
K_\mathrm{M}^\mathrm{app} = K_\mathrm{M}\left(1+\frac{[\ce{I}]}{K_\mathrm{i}}\right),
$$

so $K_\mathrm{M}^\mathrm{app}$ increases. The Lineweaver–Burk lines intersect on the
$y$-axis because $1/V_\mathrm{max}$ is unchanged.

**Answer.** **B** — $K_\mathrm{M}^\mathrm{app}$ rises and $V_\mathrm{max}$ is unchanged
(both constants have their usual units of concentration and rate respectively).

**Check.** Raising $[\ce{S}]$ towards saturation restores the uninhibited rate, which is
the defining test of competitive inhibition.

**Best distractor.** A describes pure non-competitive inhibition, which lowers
$V_\mathrm{max}$ and leaves $K_\mathrm{M}$ unchanged. C describes uncompetitive
inhibition. D has no standard mechanism.

**Where marks are lost.** Saying a competitive inhibitor lowers $V_\mathrm{max}$, or
calling the $y$-axis intersection "uncompetitive".

### 56. Non-reducing carbohydrate

**Strategy.** Count free anomeric carbons, not glycosidic bonds or chain ends.

**Working.** Sucrose is
$\alpha$-D-glucopyranosyl-(1$\to$2)-$\beta$-D-fructofuranoside. Its two anomeric carbons
(glucose C1 and fructose C2) are both in the glycosidic bond, so neither can open to an
aldehyde; sucrose is non-reducing. Lactose, maltose and cellobiose each have one free
anomeric carbon at the second glucose unit, so all three are reducing.

**Answer.** **C** (sucrose); zero free anomeric carbons per molecule.

**Check.** Sucrose gives a negative Benedict's test; lactose, maltose and cellobiose give
positive tests.

**Best distractor.** A (lactose) is a disaccharide like sucrose, but only its galactose
C1 is committed to the glycosidic bond; its glucose C1 is free, so lactose is reducing.

**Where marks are lost.** Saying sucrose has no anomeric carbons. It has two; both are
bonded.

### 57. Melting temperature of a $150\ \mathrm{bp}$ duplex

**Strategy.** Apply the empirical $T_\mathrm{m}$ relation with the salt concentration,
GC content and length correction, then compare with the options.

**Working.** The empirical relation is

$$
T_\mathrm{m} = 81.5 + 16.6\log_{10}[\ce{Na+}] + 0.41(\%\,\mathrm{GC}) - \frac{675}{N}.
$$

Substituting $[\ce{Na+}] = 0.100\ \mathrm{M}$, $\%\,\mathrm{GC} = 60$ and $N = 150$:

$$
T_\mathrm{m} = 81.5 + 16.6(-1.000) + 0.41(60) - \frac{675}{150}
= 81.5 - 16.6 + 24.6 - 4.50
= 85.0\ ^\circ\mathrm{C}.
$$

**Answer.** **B**, $85.0\ ^\circ\mathrm{C}$ (three significant figures).

**Check.** A $150\ \mathrm{bp}$ duplex with $60\%$ GC at $0.1\ \mathrm{M}$ salt is
expected to melt in the mid $80$s; the length correction lowers $T_\mathrm{m}$ by
$4.5\ ^\circ\mathrm{C}$, less than for a shorter duplex.

**Best distractor.** A ($75.0\ ^\circ\mathrm{C}$) is exactly $10\ ^\circ\mathrm{C}$ lower,
the result of an arithmetic slip in the GC term ($0.41 \times 60$ evaluated as $14.6$
rather than $24.6$). C ($102\ ^\circ\mathrm{C}$) is the result of omitting the salt term.
D ($77.0\ ^\circ\mathrm{C}$) is the result of using $40\%$ GC rather than $60\%$.

**Where marks are lost.** Omitting the salt term or the $675/N$ length correction, or
using $N = 1500$ by confusing base pairs with bases.

### 58. Net ATP from glucose with the malate–aspartate shuttle

**Strategy.** Build the inventory of substrate-level phosphorylation and reduced
cofactors, then apply the $\mathrm{P/O}$ values.

**Working.** Glycolysis gives a net $2$ ATP and $2$ NADH; PDH gives $2$ NADH; the Krebs
cycle gives $6$ NADH, $2$ FADH$_2$ and $2$ GTP. With $\mathrm{P/O} = 2.5$ for NADH and
$1.5$ for FADH$_2$:

$$
n_\mathrm{ATP} = 2 + 2(2.5) + 2(2.5) + 6(2.5) + 2(1.5) + 2 = 32.
$$

**Answer.** **B**, $32$ ATP per glucose (units: mol ATP per mol glucose).

**Check.** The glycerol-3-phosphate shuttle gives $30$ ATP, exactly $2$ fewer because the
two cytosolic NADH are counted as FADH$_2$. The historical integers $3$ and $2$ give
$38$ (malate–aspartate) and $36$ (glycerol-3-phosphate).

**Best distractor.** A ($30$) is the glycerol-3-phosphate shuttle value, not the
malate–aspartate value. C ($36$) and D ($38$) are historical values obtained with integer
$\mathrm{P/O}$ ratios.

**Where marks are lost.** Using the gross $4$ ATP of glycolysis rather than the net $2$,
or quoting $36$/$38$ without the integer $\mathrm{P/O}$ assumption.

---

## Top ten errors in this level

| # | Error | Why it costs marks | Correct approach |
|---|---|---|---|
| 1 | Treating $K_\mathrm{M}$ as $K_\mathrm{d}$ | $K_\mathrm{M} = (k_{-1}+k_2)/k_1$ includes the catalytic step; they are equal only when $k_2 \ll k_{-1}$ | State the condition before calling $K_\mathrm{M}$ an affinity |
| 2 | Averaging all three $\mathrm{p}K_\mathrm{a}$ values for a $\mathrm{pI}$ | The zwitterion is bracketed by only two of them | For a neutral side chain use $\mathrm{p}K_{a1}$ and $\mathrm{p}K_{a2}$; for acidic use the two lowest; for basic the two highest |
| 3 | Counting the gross $4$ ATP of glycolysis | Two ATP are invested, so the net is $2$ | Subtract hexokinase and phosphofructokinase-1 consumption |
| 4 | Quoting $38$ ATP without the integer $\mathrm{P/O}$ assumption | The number depends on the proton accounting and the shuttle | State $\mathrm{P/O} = 2.5/1.5$ and the shuttle; give $32$ or $30$ |
| 5 | Counting $\ce{FADH2}$ as equal to $\ce{NADH}$ | $\ce{FADH2}$ enters at complex II and bypasses complex I | Use $1.5$ versus $2.5$ ATP (or $2$ versus $3$ in the historical scheme) |
| 6 | Forgetting the $-2$ ATP activation cost of palmitate | The yield is $106$, not $108$ | Subtract two ATP equivalents for fatty acyl-CoA formation |
| 7 | Using the dsDNA $A_{260}$ factor for RNA or single-stranded DNA | The factors are $50$, $33$ and $40\ \mu\mathrm{g\ mL^{-1}}$ respectively | Identify the nucleic acid type before converting absorbance |
| 8 | Omitting the salt term from the empirical $T_\mathrm{m}$ equation | A tenfold change in $[\ce{Na+}]$ shifts $T_\mathrm{m}$ by about $16.6\ ^\circ\mathrm{C}$ | Always quote the salt concentration with the melting temperature |
| 9 | Confusing a non-reducing end with a free anomeric carbon | A glycosidic bond consumes the anomeric carbon; the chain end may still be non-reducing | Count free anomeric carbons, not chain ends |
| 10 | Using the equilibrium rotation as if it belonged to a pure anomer | Mutarotation gives a mixture whose rotation is a weighted average | Set up $[\alpha]_\mathrm{eq} = x[\alpha]_\beta + (1-x)[\alpha]_\alpha$ and solve for $x$ |

---

**Exercise bank:** [`../exercises/level-8-exercises.md`](../exercises/level-8-exercises.md)
