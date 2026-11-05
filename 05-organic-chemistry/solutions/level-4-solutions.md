# Level 4 — Worked Solutions: Organic Chemistry

> **Level:** Advanced (Level 4 — Organic Chemistry)
> **Items:** 58
> **Exercise bank:** [`../exercises/level-4-exercises.md`](../exercises/level-4-exercises.md)

Each solution gives the **Strategy** (what kind of problem it is), the **Working**
(the chemistry, step by step), the **Answer**, and a **Check** that catches the
usual error. Items marked **multi-step** require at least three dependent
decisions, and those are the ones where a single slip propagates.

Conventions used throughout. Structures are written as condensed formulae;
stereodescriptors are italicised as *(R)*, *(S)*, *(E)*, *(Z)*; curly-arrow
movements are described in words as "from X to Y". A phrase such as "inversion at
the carbon bearing the leaving group" is a claim about the stereochemical outcome
and must be justified, not asserted.

---

## Part A — Conceptual questions

### 1. Why carbon catenates and silicon does not

**Strategy.** A bond-enthalpy comparison, not a size argument. The question is
whether a chain survives in the presence of oxygen.

**Working.** The relevant mean bond enthalpies are $\ce{C-C}$ 348, $\ce{Si-Si}$ 222,
$\ce{C-O}$ 358 and $\ce{Si-O}$ 452 kJ mol⁻¹. Replacing a $\ce{C-C}$ bond by two
$\ce{C-O}$ bonds gains $2(358)-348 = +368\ \text{kJ mol}^{-1}$; replacing a
$\ce{Si-Si}$ bond by two $\ce{Si-O}$ bonds gains $2(452)-222 = +682\ \text{kJ mol}^{-1}$.
The silicon oxidation is nearly twice as exothermic. In addition, the $\ce{Si-O}$
bond is strong enough to make $\ce{SiO2}$ a three-dimensional network solid with a
very high lattice enthalpy, so the product is not a small molecule that can be
removed but an involatile solid that is thermodynamically terminal.

For carbon, the $\ce{C-O}$ and $\ce{C-C}$ bond enthalpies are almost equal (10 kJ mol⁻¹
apart), so carbon is not strongly driven to exchange its skeleton for oxygen bonds.
Carbon chains therefore survive, and the oxidation of carbon by dioxygen is slow at
room temperature for kinetic reasons (a high barrier to the initial radical step),
even though combustion is thermodynamically very favourable.

**Answer.** Carbon catenates because $\ce{C-C}$ and $\ce{C-O}$ are of comparable
strength, so there is no large thermodynamic gain in dismantling a carbon chain to
form oxides. Silicon does not, because $\ce{Si-O}$ is 230 kJ mol⁻¹ stronger than
$\ce{Si-Si}$ and the oxidation product is a network solid.

**Check.** The argument predicts that carbon chains are kinetically stable in air
but thermodynamically combustible (true), and that silicon hydrides ignite
spontaneously in air (true). It also predicts that silicon catenation is possible
when oxygen is excluded — the silanes — which is exactly what is observed.

**Where marks are lost.** Answering "silicon is larger, so $\pi$ bonds are weak".
That explains why $\ce{Si=O}$ and $\ce{Si=Si}$ are not like $\ce{C=O}$ and $\ce{C=C}$,
but it does not explain why $\ce{Si-Si}$ chains are not stable in air: the decisive
point is the $\ce{Si-O}$ bond enthalpy.

### 2. One suffix and the seniority order

**Strategy.** A nomenclature-principle question: invertibility plus a priority
ranking.

**Working.** A systematic name must map to exactly one structure and back again.
If two groups could both be expressed as suffixes, the same structure could be
named two ways, and the name would no longer identify the compound. IUPAC therefore
selects one **principal functional group**, expresses it as the suffix, and demotes
every other group to a prefix. The principal group is the most senior group present
according to the seniority order, which ranks by oxidation level at the group carbon
rather than by reactivity: carboxylic acid > ester > amide > nitrile > aldehyde >
ketone > alcohol > amine > alkene/alkyne > alkane.

For $\ce{HOCH2CH2CO2H}$ the two candidates are $\ce{-OH}$ (rank 7) and $\ce{-CO2H}$
(rank 1). The acid wins, so the suffix is *-oic acid* and the hydroxyl becomes the
prefix *hydroxy*. The chain is numbered to give the suffix the lowest locant, which
puts the carboxyl carbon at C1, so the hydroxyl is at C3.

**Answer.** 3-Hydroxypropanoic acid. It is not "1-hydroxypropan-3-oic acid" and not
"2-carboxyethan-1-ol", because only the senior group may carry the suffix and
numbering starts at that group.

**Check.** Read the name backwards: propanoic acid fixes a three-carbon acid;
3-hydroxy places the $\ce{OH}$ on the carbon remote from the carboxyl. One structure,
no ambiguity.

**Where marks are lost.** Numbering from the hydroxyl end, giving
"3-hydroxypropanoic acid" but with the locant measured the wrong way, or writing
"hydroxypropanoic acid" without a locant.

### 3. Enantiomers, diastereomers and separation

**Strategy.** Symmetry classification, then a physical-property argument.

**Working.** Enantiomers are non-superimposable mirror images. Because they have the
same constitution and the same distances between every pair of atoms, they have
identical scalar properties: boiling point, melting point, density, refractive index,
and identical IR and NMR spectra in an achiral solvent. They differ only in properties
that are odd under reflection — the sign of optical rotation, and behaviour towards
another chiral species.

Diastereomers are stereoisomers that are not mirror images. They differ in at least
one stereocentre and therefore in the through-space relationship of their atoms, so
they have different dipole moments, different packing energies and different
solvation energies: different melting points, boiling points and solubilities.

A racemate is a 50:50 mixture of enantiomers. Since the two components have the same
boiling point, fractional distillation cannot separate them. A mixture of
diastereomers has different boiling points and different polarities, so fractional
distillation or chromatography can separate them. Enantiomers are separated in
practice by converting them into diastereomers with a chiral resolving agent, or by
chromatography on a chiral stationary phase, which operates by forming
diastereomeric association complexes of different stability.

**Answer.** Enantiomers differ only in chirality-dependent properties; diastereomers
differ in scalar physical properties. A racemate cannot be distilled apart; a
diastereomeric mixture can be separated by any method that exploits the different
physical properties.

**Check.** The argument is self-consistent: it explains why resolution requires a
chiral agent (you must create a diastereomeric interaction) and why enantiomeric
drugs cannot be separated by ordinary recrystallisation.

**Where marks are lost.** Saying enantiomers have "identical physical properties"
without the exception for optical rotation; or claiming diastereomers have identical
NMR spectra.

### 4. Why the chair, and what a ring flip does

**Strategy.** Strain analysis, then a definition of configuration versus conformation.

**Working.** A planar cyclohexane would have C–C–C angles of 120°, which is 10.5°
wider than the tetrahedral value, and every C–H bond would be eclipsed with the C–H
bond on the adjacent carbon. The chair removes both penalties at once: the C–C–C
angles are close to 109.5°, and all adjacent C–H bonds are staggered. The residual
strain is essentially zero and the chair is the global minimum. The boat (about
29 kJ mol⁻¹ higher) retains eclipsing and adds a flagpole interaction; the twist-boat
(23 kJ mol⁻¹) is a local minimum; the half-chair (45 kJ mol⁻¹) is the transition state
for the ring flip.

A ring flip is a conformational change: the ring distorts through the half-chair,
twist-boat, boat and twist-boat and returns to the other chair, without any bond
being broken. Because no bond is broken, the configuration at every stereocentre is
unchanged. What changes is the orientation of each substituent relative to the ring:
every axial bond becomes equatorial and every equatorial bond becomes axial, while
the *up* or *down* face occupied by a substituent is preserved.

**Answer.** The chair relieves angle strain and torsional (eclipsing) strain, and it
also minimises 1,3-diaxial repulsion. A ring flip is a bond-rotation process, so it
changes conformation only.

**Check.** The test is whether an enantiomer could be generated by flipping. It
cannot: *cis*-1,4-dimethylcyclohexane remains the same achiral *cis* compound after
a flip, and a chiral substituted cyclohexane retains its configuration.

**Where marks are lost.** Writing that the chair has "no strain" absolutely (it has
a small residual strain, and the interconversion barrier is 45 kJ mol⁻¹), or claiming
that an axial methyl becomes a different stereoisomer on flipping.

### 5. Hammond postulate and halogen selectivity

**Strategy.** Apply the Hammond postulate to the hydrogen-abstraction step, which is
the step that sets the selectivity.

**Working.** The Hammond postulate states that the transition state of a reaction
resembles the species to which it is closest in energy — the reactant for a very
exothermic step, the product for a very endothermic one.

Hydrogen abstraction by a chlorine atom is exothermic ($\ce{C-H}$ 414 versus
$\ce{H-Cl}$ 431 kJ mol⁻¹ broken and formed). The transition state is therefore early
and has little radical character: the developing stability of the alkyl radical
barely influences the barrier. The result is a small spread of rates, measured as
about 5.0 : 3.8 : 1.0 : 1 for 3° : 2° : 1° : CH₃ per hydrogen.

Hydrogen abstraction by a bromine atom is endothermic ($\ce{C-H}$ 414 versus
$\ce{H-Br}$ 366 kJ mol⁻¹). The transition state is late and product-like: it has
substantial radical character, so the stability order of the radicals
(3° > 2° > 1° > CH₃) is strongly reflected in the barrier. Bromination is therefore
highly selective, about 1600 : 82 : 1 : 1.

**Answer.** Chlorine is unselective because its abstraction step is exothermic and
has an early, reactant-like transition state; bromine is selective because its
abstraction step is endothermic and has a late, radical-like transition state.

**Check.** The same argument predicts that fluorination is explosively unselective
(very exothermic, very early transition state) and that iodination is useless
(strongly endothermic, and reversible). Both are observed.

**Where marks are lost.** Explaining selectivity only by "radical stability" without
invoking the position of the transition state; or reversing the exothermicity
assignment for chlorine and bromine.

### 6. Regioselectivity and the peroxide effect

**Strategy.** Compare two competing carbocation pathways, then explain why the
radical chain is available only for HBr.

**Working.** In the ionic addition, the alkene $\pi$ bond attacks $\ce{H-X}$ and the
$\ce{H-X}$ bond breaks heterolytically. The proton adds to the carbon that gives the
more stable carbocation, because the transition state for protonation has partial
carbocation character. A tertiary carbocation is more stable than a secondary one,
which is more stable than a primary one, so the nucleophile ends up on the more
substituted carbon: Markovnikov addition.

In the presence of a peroxide, homolysis of the weak $\ce{O-O}$ bond gives alkoxyl
radicals, which abstract hydrogen from $\ce{HBr}$ to give $\ce{Br^{.}}$. The bromine
atom adds to the alkene to give the more stable carbon radical, which is the one at
the less substituted end (a radical is stabilised by alkyl groups, and the chain
propagates through the more stable radical). That radical then abstracts hydrogen
from another $\ce{HBr}$, giving the anti-Markovnikov alkyl bromide and a new bromine
atom.

The chain requires both propagation steps to be favourable. For $\ce{HCl}$ the first
step is favourable, but the second step, $\ce{R^{.} + HCl -> RH + Cl^{.}}$, is
endothermic by about $17\ \text{kJ mol}^{-1}$, because the $\ce{C-H}$ bond formed
(414 kJ mol⁻¹) is weaker than the $\ce{H-Cl}$ bond broken (431 kJ mol⁻¹). The alkyl
radical therefore does not abstract hydrogen from $\ce{HCl}$, and the chain stops. For
$\ce{HI}$ both propagation steps are exothermic, but the addition of $\ce{I^{.}}$ to the
alkene is reversible and the $\ce{C-I}$ bond is weak (234 kJ mol⁻¹), so the radical
pathway does not deliver a clean product; iodine is also a strong enough oxidant to
interfere.

**Answer.** Ionic addition gives the Markovnikov product through the more stable
carbocation. The peroxide effect gives the anti-Markovnikov product through the more
stable carbon radical, and it is observed only for $\ce{HBr}$ because only $\ce{HBr}$
supports both radical propagation steps.

**Check.** The prediction is that peroxide has no effect on $\ce{HCl}$ addition (true)
and that $\ce{HBr}$ with peroxide gives the opposite regiochemistry from $\ce{HBr}$
alone (true).

**Where marks are lost.** Writing "peroxide makes it anti-Markovnikov" without
showing the two propagation steps, or claiming the effect works for all hydrogen
halides.

### 7. Halogens: deactivating but *ortho*/*para* directing

**Strategy.** Separate the rate question (electronic demand of the ring) from the
orientation question (stability of the arenium ion).

**Working.** A halogen substituent withdraws electron density inductively through the
σ framework, because it is more electronegative than carbon, and this withdrawal is
strong because the halogen is directly attached to the ring. The ring is therefore
less nucleophilic than benzene and reacts more slowly: the halogens are deactivating.

At the same time, a halogen has lone pairs in a $p$ orbital that can overlap with the
ring $\pi$ system. When the electrophile attacks the *ortho* or *para* position, one
resonance form of the arenium ion places the positive charge on the carbon bearing
the halogen. That carbon can then be stabilised by donation of a halogen lone pair,
giving a structure in which the halogen bears a formal positive charge and is
doubly bonded to the ring. This extra resonance form is not available when attack is
*meta*, because the positive charge never reaches the substituted carbon. The
*ortho* and *para* transition states are therefore lower in energy than the *meta*
one, and the halogen directs *ortho*/*para*.

The two effects are not contradictory because they act on different quantities: the
inductive withdrawal lowers the energy of the starting material and of every
transition state, and so controls the rate; the resonance donation selectively
lowers the *ortho* and *para* transition states, and so controls the orientation.

**Answer.** Halogens deactivate by induction but direct *ortho*/*para* by resonance
stabilisation of the halonium-containing arenium ion.

**Check.** Fluorine is the extreme case: its inductive withdrawal is the strongest of the
halogens, yet its $2p$–$2p$ overlap with the ring is also the best, so it remains a
strong *ortho*/*para* director despite being deactivating. Iodine is the reverse: only
weakly deactivating but a poor director. Both are consistent with the two-effect model.

**Where marks are lost.** Saying halogens are "activating because of resonance" —
that contradicts the observed rate — or failing to draw the resonance form with the
positive charge on the halogen.

### 8. Substitution versus elimination

**Strategy.** Four-variable decision, then a steric argument for the failure of
$S_N2$ at a tertiary carbon.

**Working.** The four variables are:

1. **Substrate.** Methyl and primary favour $S_N2$; secondary is ambiguous; tertiary
   favours $S_N1$ or $E2$.
2. **Nucleophile or base.** A good nucleophile that is a weak base ($\ce{I-}$,
   $\ce{N3-}$, $\ce{CN-}$, $\ce{RS-}$) favours substitution; a strong base
   ($\ce{RO-}$, $\ce{NH2-}$, LDA) favours elimination; a bulky base
   ($\ce{KOtBu}$) favours the Hofmann alkene.
3. **Solvent.** Polar aprotic favours $S_N2$ (the nucleophile is not solvated);
   polar protic favours $S_N1$/$E1$ (it stabilises the carbocation and the leaving
   group).
4. **Temperature.** Heat favours elimination, because elimination increases the
   number of particles and therefore has a positive activation entropy.

$S_N2$ requires backside attack: the nucleophile must approach the carbon bearing the
leaving group along the axis opposite the $\ce{C-X}$ bond. At a tertiary carbon the
three alkyl groups occupy the space through which the nucleophile must pass, and the
five-coordinate transition state would be severely crowded. The activation energy is
therefore high, and the competing unimolecular ionisation to a stabilised tertiary
carbocation is much faster.

**Answer.** Substrate, reagent strength and bulk, solvent polarity, and temperature.
A tertiary substrate cannot undergo $S_N2$ because backside attack is sterically
blocked and the $S_N1$ alternative is fast.

**Check.** The model predicts that *tert*-butyl bromide with sodium methoxide gives
mainly elimination, not substitution (true), and that neopentyl bromide — primary but
neighbouring a *tert*-butyl group — is also very slow in $S_N2$ (true).

**Where marks are lost.** Listing the variables without saying which way each pushes,
or claiming a tertiary substrate is "too stable" to react.

### 9. Kinetic and thermodynamic enolates of 2-methylcyclohexanone

**Strategy.** Identify the two acidic sites, then match base strength and temperature
to the rate of deprotonation versus the stability of the enolate.

**Working.** 2-Methylcyclohexanone has two α-carbons: C2, which carries the methyl
group and is fully substituted, and C6, which is a $\ce{CH2}$ group. Deprotonation at
C6 gives the less substituted enolate (a trisubstituted alkene); deprotonation at C2
gives the more substituted enolate (a tetrasubstituted alkene) but requires removal of
a proton from a more hindered site.

With lithium diisopropylamide at −78 °C in tetrahydrofuran, deprotonation is fast,
irreversible and controlled by the accessibility of the proton. LDA is bulky, so it
removes the exposed proton at C6. The enolate is trapped before it can equilibrate.
This is the **kinetic enolate**, formed at C6.

With sodium hydride or sodium ethoxide at room temperature, deprotonation is
reversible and the system equilibrates. The more substituted enolate is the more
stable because alkyl substitution stabilises the carbon–carbon double bond, so the
**thermodynamic enolate** at C2 dominates.

**Answer.** Kinetic: LDA, −78 °C, enolate at C6. Thermodynamic: NaH or NaOEt,
room temperature, enolate at C2.

**Check.** Alkylation of the kinetic enolate gives 6-alkyl-2-methylcyclohexanone;
alkylation of the thermodynamic enolate gives 2,2-dialkylcyclohexanone. Both are
consistent with the assignment.

**Where marks are lost.** Reversing the two, or saying the thermodynamic enolate is
"more stable because it forms faster". Stability and rate are different criteria
here; that is the whole point of the distinction.

### 10. Synthon, reagent and umpolung

**Strategy.** Definitions, then a polarity check on the proposed disconnection.

**Working.** A **synthon** is an idealised fragment defined by the polarity and
functionality it must have in the forward reaction — for example the acyl anion
$\ce{RCO^-}$ or the enolate fragment $\ce{R-CH2-C(=O)R'}$. A **reagent** is the real
chemical that delivers that synthon — for example 1,3-dithiane plus a strong base,
or LDA plus a ketone.

In a ketone $\ce{R-CO-R'}$, the carbonyl carbon is electrophilic: it is $a^1$, because
the oxygen withdraws both the σ and the π electrons. Disconnecting the bond between
the carbonyl carbon and an alkyl group gives an acyl fragment and a carbanion. The
required acyl fragment is $\ce{RCO^-}$, a nucleophilic carbonyl carbon, which is the
opposite of the natural polarity. Reversing the polarity of a functional group is
**umpolung**, so this disconnection is only usable with a $d^1$ equivalent.

Two $d^1$ equivalents are:

- the **1,3-dithiane anion**, made by treating an aldehyde or ketone with
  propane-1,3-dithiol and then deprotonating between the two sulfurs; the dithiane is
  removed at the end with mercury(II) or an iodonium reagent to restore the carbonyl;
- the **cyanohydrin anion**, made by adding cyanide to an aldehyde or ketone and
  deprotonating the resulting $\ce{C-H}$; hydrolysis of the nitrile then gives an
  $\alpha$-hydroxy acid or, after further manipulation, a ketone.

**Answer.** Synthon: idealised fragment; reagent: real chemical. The acyl-anion
disconnection is umpolung because the carbonyl carbon is naturally electrophilic.
Dithiane anions and cyanohydrin anions are the two standard $d^1$ equivalents.

**Check.** A valid disconnection must correspond to a real forward reaction with the
right polarity. The dithiane route is real: dithiane anion + alkyl halide gives,
after deprotection, a ketone with the acyl carbon bonded to the alkyl group.

**Where marks are lost.** Using "synthon" and "reagent" interchangeably, or proposing
an acyl anion without naming an umpolung equivalent.

---

## Part B — Basic problems

### 11. Names from structures

**Strategy.** Apply the naming algorithm: identify the principal group, choose the
parent, number, then alphabetise substituents.

**Working.**

(a) $\ce{(CH3)2CHCH2CH2OH}$: the principal group is $\ce{-OH}$, so the suffix is
*-ol* and the parent chain must contain the carbon bearing it. The longest chain
containing that carbon is four carbons: $\ce{C1}$ bears $\ce{OH}$, $\ce{C2}$ is a
$\ce{CH2}$, $\ce{C3}$ bears a methyl, $\ce{C4}$ is a methyl. Numbering from the
$\ce{OH}$ end gives the substituent locant 3.

(b) $\ce{CH3CH2CO2CH(CH3)2}$: an ester, named as alkyl alkanoate. The group on oxygen
is propan-2-yl; the acyl part is propanoate.

(c) $\ce{CH3CH=C(CH3)CHO}$: an aldehyde, so the carbonyl carbon is C1. The chain is
four carbons with a double bond between C2 and C3 and a methyl at C2.

(d) $\ce{CH3CON(CH3)(CH2CH3)}$: an amide with the parent ethanamide; the nitrogen
carries a methyl and an ethyl, cited alphabetically.

**Answer.** (a) 3-Methylbutan-1-ol. (b) Propan-2-yl propanoate. (c) 2-Methylbut-2-enal.
(d) *N*-Ethyl-*N*-methylethanamide.

**Check.** Each name must regenerate the structure. For (c), 2-methylbut-2-enal gives
$\ce{CH3-CH=C(CH3)-CHO}$; the aldehyde hydrogen is implicit, so the formula is correct.
For (a), 3-methylbutan-1-ol gives a four-carbon chain with $\ce{OH}$ at C1 and methyl
at C3, which is isopentyl alcohol.

**Where marks are lost.** Naming (a) as "2-methylbutan-4-ol" (numbering from the wrong
end), naming (b) as "isopropyl propanoate" in a systematic answer, or omitting the
locant in (c).

### 12. Structures from names

**Strategy.** Parse the name from the suffix backwards: parent, then substituents,
then locants.

**Working.**

(a) 3-Ethyl-2,4-dimethylhexane: a six-carbon chain; methyls at C2 and C4; an ethyl at
C3. Skeleton $\ce{CH3-CH(CH3)-CH(CH2CH3)-CH(CH3)-CH2-CH3}$.

(b) 2-Methylbut-2-ene: a four-carbon chain with the double bond between C2 and C3 and
a methyl on C2: $\ce{CH3-C(CH3)=CH-CH3}$.

(c) Ethyl 2-hydroxypropanoate: the acyl part is a three-carbon acid with $\ce{OH}$ at
C2 and the ethyl ester: $\ce{CH3-CH(OH)-CO2CH2CH3}$.

(d) *N*,*N*-Dimethylbenzamide: benzamide with two methyl groups on nitrogen:
$\ce{C6H5-CON(CH3)2}$.

**Answer.** As the condensed formulae above.

**Check.** Count carbons against the name: (a) six in the chain plus an ethyl and two
methyl substituents = ten carbons, which is a $\ce{C10H22}$ alkane. (b) $\ce{C5H10}$,
one degree of unsaturation. (c) $\ce{C5H10O3}$. (d) $\ce{C9H11NO}$.

**Where marks are lost.** Putting the ethyl of (a) at C2, which would make it part of
a longer chain and change the parent; or writing the ester of (c) with the ethyl on
the acyl carbon.

### 13. Principal functional group and suffix

**Strategy.** Rank the groups present using the seniority table, then name.

**Working.**

(a) $\ce{CH3CH(OH)CH2CHO}$ contains an alcohol and an aldehyde. Aldehyde (rank 5)
outranks alcohol (rank 7), so the suffix is *-al* and the alcohol becomes *hydroxy*.
Four-carbon chain: 3-hydroxybutanal.

(b) $\ce{CH3CH2CN}$ is a nitrile; the nitrile carbon counts as part of the parent
chain, so the parent has three carbons: propanenitrile.

(c) $\ce{CH3COCH2CO2CH3}$ contains a ketone and an ester. Ester (rank 2) outranks
ketone (rank 6), so the suffix is *-oate* and the ketone becomes *oxo*. The ester
carbon is C1; the ketone is at C3: methyl 3-oxobutanoate.

(d) $\ce{C6H5CH2NH2}$ is a primary amine with a one-carbon parent bearing a phenyl
group: phenylmethanamine.

(e) $\ce{CH3CH2SO3H}$ is a sulfonic acid: ethanesulfonic acid.

**Answer.** (a) Aldehyde, *-al*, 3-hydroxybutanal. (b) Nitrile, *-nitrile*,
propanenitrile. (c) Ester, *-oate*, methyl 3-oxobutanoate. (d) Amine, *-amine*,
phenylmethanamine. (e) Sulfonic acid, *-sulfonic acid*, ethanesulfonic acid.

**Check.** In (c) the alternative name "methyl acetoacetate" is a trivial name, not
the systematic one. In (d) "benzylamine" is retained but phenylmethanamine is the
systematic form.

**Where marks are lost.** Making the ketone the suffix in (c) and calling it
"1-methoxybutane-1,3-dione", or treating the nitrile carbon of (b) as a substituent.

### 14. Degree of unsaturation

**Strategy.** Apply
$\text{DU} = \dfrac{2C + 2 + N - H - X}{2}$, counting halogens as hydrogens and
ignoring oxygen and sulfur.

**Working.**

(a) $\ce{C8H9ClO}$: $\text{DU} = \dfrac{2(8)+2-9-1}{2} = \dfrac{16+2-10}{2} = 4$.

(b) $\ce{C6H5NO2}$: $\text{DU} = \dfrac{2(6)+2+1-5}{2} = \dfrac{12+2+1-5}{2} = 5$.

(c) $\ce{C10H16}$: $\text{DU} = \dfrac{2(10)+2-16}{2} = \dfrac{20+2-16}{2} = 3$.

**Answer.** (a) 4; (b) 5; (c) 3.

**Check.** Nitrobenzene has a ring (4 degrees: three $\ce{C=C}$ plus the ring closure)
plus one $\ce{N=O}$, giving 5. Decalin, $\ce{C10H18}$, has DU 2; the extra degree in
(c) means one additional ring or double bond.

**Where marks are lost.** Forgetting to count the halogen in (a), which would give
DU 4.5 and flag an arithmetic error; or counting oxygen as if it contributed.

### 15. CIP priorities and the R/S rule

**Strategy.** Apply the priority rules, then the orientation rule.

**Working.**

(a) At C2 of 2-chlorobutane the four groups are $\ce{-Cl}$, $\ce{-CH2CH3}$,
$\ce{-CH3}$ and $\ce{-H}$. Priority is by atomic number at the first point of
difference: $\ce{Cl}$ (17) > $\ce{C}$ (6) > $\ce{H}$ (1). Between the two carbons,
ethyl has $\ce{C,H,H}$ at the next shell and methyl has $\ce{H,H,H}$, so ethyl
outranks methyl.

(b) With the lowest-priority group pointing away, the observed direction is the true
configuration. Anticlockwise is *S*.

(c) With the lowest-priority group pointing towards the viewer, the observed direction
must be reversed. Clockwise observed is therefore *S*.

**Answer.** (a) $\ce{Cl}$ 1, $\ce{C2H5}$ 2, $\ce{CH3}$ 3, $\ce{H}$ 4. (b) *(S)*.
(c) *(S)*.

**Check.** Case (c) is the classic trap: clockwise normally means *R*, so the answer
must be the opposite because the lowest-priority group is on the wrong side.

**Where marks are lost.** Forgetting the reversal in (c), or ranking ethyl and methyl
by chain length without checking the first point of difference.

### 16. E/Z assignment

**Strategy.** Apply CIP separately at each alkene carbon, then compare the sides.

**Working.**

(a) $\ce{CH3C(Br)=CHCl}$. At the left carbon, $\ce{Br}$ (35) outranks $\ce{CH3}$ (6).
At the right carbon, $\ce{Cl}$ (17) outranks $\ce{H}$ (1). The two high-priority
groups, $\ce{Br}$ and $\ce{Cl}$, are on the same side, so the descriptor is *Z*.

(b) $\ce{HO2CCH=CHCO2H}$. At each carbon the two groups are $\ce{CO2H}$ and $\ce{H}$;
the carboxyl group outranks hydrogen. The two carboxyl groups are on opposite sides,
so the descriptor is *E*.

(c) $\ce{ClCH=CHCl}$. The two chlorines are the high-priority groups on their
carbons and they are on the same side, so the descriptor is *Z*.

**Answer.** (a) *(Z)*-1-bromo-1-chloroprop-1-ene. (b) *(E)*-but-2-enedioic acid
(fumaric acid). (c) *(Z)*-1,2-dichloroethene.

**Check.** For (c), *cis* and *Z* coincide because the two substituents on each carbon
are different; for a 1,2-disubstituted ethene with identical groups, *cis* = *Z*.

**Where marks are lost.** Choosing the higher-priority group by size rather than by
atomic number, or applying *cis*/*trans* to a case where each carbon carries two
different groups.

### 17. Newman projections of butane

**Strategy.** Rotate about C2–C3 and classify by the dihedral angle between the two
methyl groups.

**Working.** Viewing along C2–C3, the front carbon carries $\ce{H}$, $\ce{H}$ and
$\ce{CH3}$; the back carbon carries the same three groups. In the **anti** conformer
the two methyl groups are 180° apart; in the two **gauche** conformers they are 60°
apart. In the eclipsed conformers the dihedral is 0°.

The anti conformer has no steric interaction between the methyls and is the global
minimum of the rotational profile: 0 kJ mol⁻¹ by definition. Each gauche conformer has
one methyl–methyl interaction and lies about 3.8 kJ mol⁻¹ higher. The eclipsed
conformers are higher still (the methyl–methyl eclipsed form is about 19–25 kJ mol⁻¹
above the anti), and they are transition states, not minima.

**Answer.** Anti, 0 kJ mol⁻¹; two equivalent gauche forms, +3.8 kJ mol⁻¹ each;
eclipsed forms substantially higher and not isolable.

**Check.** The Boltzmann populations at 298 K follow from
$K = \exp(-3800/RT) = 0.22$ for each gauche relative to anti, so the anti form is
about 70 % of the population and the two gauche forms about 15 % each. This is
consistent with the observed preference for the anti conformer of butane.

**Where marks are lost.** Drawing an eclipsed structure and calling it gauche, or
placing the methyls at 120° (that is not a staggered arrangement in a Newman
projection along a C–C bond).

### 18. Dimethylcyclohexanes: 1,3-relationship

**Strategy.** Use the up/down alternation of axial bonds around the ring.

**Working.** In a chair, the axial bonds alternate up, down, up, down. At C1 and C3
they point the same way (both up, or both down); at C1 and C2, and at C1 and C4, they
point opposite ways.

*cis*-1,3-Dimethylcyclohexane has both methyls on the same face. Because the axial
positions at C1 and C3 point the same way, both methyls can be axial together, or both
equatorial together. The (e,e) chair has both methyls equatorial and is strongly
preferred; the (a,a) chair has two axial methyls and is about 15 kJ mol⁻¹ higher.

*trans*-1,3-Dimethylcyclohexane has the methyls on opposite faces. One must be axial
and the other equatorial, in either chair; the two chairs are equivalent.

**Answer.** *cis*-1,3: (e,e), the stable chair. *trans*-1,3: (a,e) in both chairs.
The *cis* isomer is the more stable because it can place both methyls equatorial.

**Check.** This is the reverse of the 1,2- and 1,4-cases, where *trans* is the (e,e)
isomer. The rule follows from the alternation of axial directions: same face at 1,3
means same axial sense.

**Where marks are lost.** Applying the 1,2 rule to the 1,3 isomer, or forgetting that
the (a,a) chair of the *cis* isomer, although higher, is still a conformer of the same
compound.

### 19. Monochlorination of propane

**Strategy.** Statistical factor times reactivity factor, then normalise.

**Working.** Propane, $\ce{CH3CH2CH3}$, has six equivalent primary hydrogens and two
equivalent secondary hydrogens. The weighted contributions are
$6 \times 1.0 = 6.0$ for the primary positions and $2 \times 3.8 = 7.6$ for the
secondary position. The total is 13.6.

The percentages are $6.0/13.6 = 44.1\%$ for 1-chloropropane and
$7.6/13.6 = 55.9\%$ for 2-chloropropane.

**Answer.** 44.1 % 1-chloropropane and 55.9 % 2-chloropropane.

**Check.** The secondary product is in excess despite there being only two such
hydrogens, because each secondary hydrogen is 3.8 times more reactive. The result is
still a mixture, which is why chlorination is not a preparative method for a single
isomer.

**Where marks are lost.** Using the reactivity ratio as a product ratio without
multiplying by the number of hydrogens.

### 20. Alkene additions

**Strategy.** For each reagent, identify the electrophile, the intermediate and
whether the addition is *syn* or *anti*.

**Working.**

(a) $\ce{HBr}$ adds ionically. Protonation at C1 gives the secondary carbocation at
C2, which is captured by bromide: 2-bromopropane.

(b) With peroxide, the radical chain operates. $\ce{Br^{.}}$ adds to C1 to give the
more stable secondary radical at C2, which abstracts hydrogen from $\ce{HBr}$:
1-bromopropane.

(c) $\ce{Br2}$ in water forms the bromonium ion, which is opened by water. Water
attacks the more substituted carbon (C2), because that carbon bears more of the
positive charge in the bridged intermediate. The product is 3-bromo-2-methylbutan-2-ol,
formed by anti addition; C3 is a new stereocentre and the product is racemic.

(d) Hydroboration–oxidation gives anti-Markovnikov hydration with *syn* addition:
butan-1-ol.

**Answer.** (a) 2-Bromopropane. (b) 1-Bromopropane. (c) 3-Bromo-2-methylbutan-2-ol,
anti addition, racemic. (d) Butan-1-ol, *syn* addition.

**Check.** In (c) the regiochemistry is "Markovnikov for $\ce{OH}$": the hydroxyl ends
up on the more substituted carbon, which is the opposite of the bromine. In (a) and
(b) the two reagents give opposite regiochemistry from the same alkene, which is the
standard test of the peroxide effect.

**Where marks are lost.** Putting the $\ce{OH}$ on the less substituted carbon in (c),
or claiming (d) gives butan-2-ol.

### 21. Aromaticity

**Strategy.** Apply Hückel's rule: cyclic, planar, fully conjugated, $4n+2$ π
electrons. If $4n$, antiaromatic; if not fully conjugated or not planar,
non-aromatic.

**Working.**

(a) The cyclopentadienyl anion has five $p$ orbitals in a ring, and the lone pair on
the carbanion lies in a $p$ orbital, so the system is fully conjugated. It has
$4 + 2 = 6$ π electrons: $4n+2$ with $n = 1$. Aromatic.

(b) The cycloheptatrienyl (tropylium) cation has seven $p$ orbitals and a vacant
$p$ orbital at the carbocation; the ring is fully conjugated with 6 π electrons.
Aromatic.

(c) Cyclobutadiene has four $p$ orbitals and 4 π electrons: $4n$ with $n = 1$.
Antiaromatic.

(d) Cyclooctatetraene has 8 π electrons, which would be antiaromatic, but the ring
adopts a tub shape that breaks conjugation. Non-aromatic.

(e) [18]Annulene has 18 π electrons: $4n+2$ with $n = 4$. It is large enough to be
planar and is aromatic.

(f) Pyridine has six $p$ orbitals in the ring, each contributing one electron, and
the nitrogen lone pair lies in an $sp^2$ orbital in the ring plane, orthogonal to the
π system. Six π electrons: aromatic.

**Answer.** (a) Aromatic, 6 π. (b) Aromatic, 6 π. (c) Antiaromatic, 4 π.
(d) Non-aromatic, 8 π. (e) Aromatic, 18 π. (f) Aromatic, 6 π.

**Check.** The count for pyridine excludes the nitrogen lone pair — if it were
included the total would be 8 and the molecule would be antiaromatic, which is
plainly wrong. The lone pair is orthogonal to the π system.

**Where marks are lost.** Counting the nitrogen lone pair in pyridine, or calling
cyclooctatetraene antiaromatic without noting the tub distortion.

### 22. Oxidation levels

**Strategy.** Count bonds to more electronegative atoms as $+1$ each, bonds to
hydrogen as $-1$ each, bonds to carbon as zero.

**Working.**

(a) Ethanol, $\ce{CH3CH2OH}$, C1: two $\ce{C-H}$ ($-2$) and one $\ce{C-O}$ ($+1$)
gives $-2$.

(b) Methanal, $\ce{HCHO}$, carbonyl carbon: two $\ce{C-H}$ ($-2$) and one $\ce{C=O}$
counted twice ($+2$) gives $0$.

(c) Methanoic acid, $\ce{HCOOH}$, carboxyl carbon: one $\ce{C-H}$ ($-1$), one
$\ce{C=O}$ ($+2$) and one $\ce{C-O}$ ($+1$) gives $+2$.

(d) The methyl carbon of ethanoic acid, $\ce{CH3CO2H}$: three $\ce{C-H}$ ($-3$) and one
$\ce{C-C}$ (0) gives $-3$. The neighbouring carboxyl carbon is $+3$, and the average
over the two carbons is $0$.

(e) Tetrachloromethane, $\ce{CCl4}$: four $\ce{C-Cl}$ bonds, each $+1$, gives $+4$,
the maximum oxidation state of carbon.

(f) Propanone, $\ce{(CH3)2CO}$, carbonyl carbon: two $\ce{C-C}$ bonds (0) and one
$\ce{C=O}$ ($+2$) gives $+2$.

**Answer.** (a) $-2$; (b) $0$; (c) $+2$; (d) $-3$; (e) $+4$; (f) $+2$.

**Check.** Each value agrees with the oxidation ladder in Chapter 12: methanol $-2$,
methanal $0$, methanoic acid $+2$, carbon dioxide $+4$. Carbon tetrachloride at $+4$
is the halogen analogue of carbon dioxide, as it must be, because four $\ce{C-Cl}$
bonds replace four $\ce{C-H}$ bonds.

**Where marks are lost.** Forgetting that a double bond to oxygen counts twice, which
would turn (b) into $-2$ and (c) into $+1$; or counting the $\ce{C-C}$ bond of (d) as
if it contributed.

---

## Part C — Intermediate problems

### 23. Naming a hydroxy acid and counting stereoisomers **multi-step**

**Strategy.** Choose the senior group, number, name, then count stereocentres and
apply $2^n$ with a check for internal symmetry.

**Working.** The structure is
$\ce{HO2C-CH(CH3)-CH(OH)-CH3}$. The senior group is the carboxylic acid, so the
parent is butanoic acid and the carboxyl carbon is C1. Numbering along the chain
gives a methyl at C2 and a hydroxyl at C3: 3-hydroxy-2-methylbutanoic acid.

There are two stereocentres. C2 carries $\ce{H}$, $\ce{CH3}$, $\ce{CO2H}$ and C3;
C3 carries $\ce{H}$, $\ce{OH}$, $\ce{CH3}$ and C2. At each centre the four groups are
different, so both are stereogenic. Because the two centres are not equivalently
substituted, there is no *meso* possibility and the number of stereoisomers is
$2^2 = 4$, forming two pairs of enantiomers.

**Answer.** 3-Hydroxy-2-methylbutanoic acid; four stereoisomers.

**Check.** If the molecule had been 2,3-dihydroxybutanoic acid (identical groups at
C2 and C3 in the corresponding dibasic case) a *meso* form would reduce the count.
Here the substituent sets differ, so no *meso* form exists.

**Where marks are lost.** Numbering from the methyl end, giving "2-hydroxy-3-
methylbutanoic acid", or claiming two stereoisomers because "there are two
stereocentres".

### 24. Stereoisomers of 2,3-dibromobutane

**Strategy.** Enumerate the configurations, then test each for a mirror plane.

**Working.** The two stereocentres are equivalent, so the possible combinations are
*(2R,3R)*, *(2S,3S)* and *(2R,3S)* (which is the same compound as *(2S,3R)* by
rotation).

*(2R,3R)* and *(2S,3S)* are non-superimposable mirror images: a pair of enantiomers,
both optically active. *(2R,3S)* has the two bromines on opposite faces and possesses
a plane of symmetry perpendicular to the C2–C3 bond, relating the two halves. It is
therefore achiral — a *meso* compound.

A *meso* compound is optically inactive because the two stereocentres have equal and
opposite contributions to rotation; the molecule is its own mirror image, so a sample
cannot be optically active.

**Answer.** *(2R,3R)* and *(2S,3S)* (enantiomers) and *(2R,3S)* (the *meso* form);
three stereoisomers in total.

**Check.** Three is the correct count for a molecule with two equivalent stereocentres
and a *meso* form; four would require the centres to be inequivalent.

**Where marks are lost.** Counting four, or calling the *meso* form a racemate. A
*meso* compound is a single substance, not a mixture.

### 25. Polarimetry **multi-step**

**Strategy.** Use $[\alpha] = \alpha/(c\,l)$, then compare with the pure value, then
convert enantiomeric excess into composition.

**Working.** With $\alpha = +0.81^\circ$, $c = 0.100\ \text{g cm}^{-3}$ and
$l = 1.0\ \text{dm}$:

$$[\alpha]_{\mathrm{D}}^{20} = \frac{0.81}{0.100 \times 1.0} = +8.1^\circ$$

The enantiomeric excess is the observed rotation divided by the rotation of the pure
enantiomer:

$$\text{ee} = \frac{8.1}{13.5} = 0.600 = 60\%$$

The majority enantiomer is the one with the sign of the observed rotation, so the
sample is enriched in *(R)*. Its fraction is $0.5 + 0.5(0.60) = 0.80$, and the
*(S)* fraction is $0.20$.

**Answer.** $[\alpha]_{\mathrm{D}}^{20} = +8.1^\circ$; ee = 60 %; 80 % *(R)* and
20 % *(S)*.

**Check.** The mass balance is $80 + 20 = 100$ %, and the excess is
$80 - 20 = 60$ %, which matches. A sample of 100 % ee would give $+13.5^\circ$;
a racemate would give $0$.

**Where marks are lost.** Forgetting to divide by the concentration (giving
"ee = 6 %"), or reporting the composition as 60:40 rather than 80:20.

### 26. A-value and conformational population **multi-step**

**Strategy.** Convert the A-value into an equilibrium constant with the Boltzmann
distribution.

**Working.** The A-value is the Gibbs energy by which the axial conformer lies above the
equatorial conformer: $\Delta G^\circ_{\text{ax}\to\text{eq}} = -7.6\ \text{kJ mol}^{-1}$.
Taking the axial form as the reference, the ratio of the two populations is

$$\frac{p_{\text{eq}}}{p_{\text{ax}}} = \exp\!\left(-\frac{\Delta G^\circ_{\text{ax}\to\text{eq}}}{RT}\right)
= \exp\!\left(\frac{7600}{8.314 \times 298}\right) = \exp(3.067) = 21.5$$

The axial fraction is therefore

$$p_{\text{ax}} = \frac{1}{1 + 21.5} = 0.0445$$

and the equatorial fraction is $1 - 0.0445 = 0.955$.

**Answer.** 95.5 % equatorial at 298 K.

**Check.** This agrees with the tabulated "approximate equatorial population" of 95 %
in Chapter 4. A larger A-value (for example *tert*-butyl, >20 kJ mol⁻¹) gives a ratio
above 3000, i.e. essentially 100 % equatorial.

**Where marks are lost.** Using the A-value with the wrong sign, which gives 4.5 %
equatorial instead of 95.5 %; the A-value is the energetic *penalty* for the axial
position, so the equatorial conformer is the favoured one.

### 27. E2 stereochemistry in a substituted cyclohexane **multi-step**

**Strategy.** Find the chair in which the leaving group is axial, then check for an
anti-periplanar β-hydrogen.

**Working.** The *tert*-butyl group has an A-value above 20 kJ mol⁻¹, so it is
effectively locked equatorial. In 1-bromo-4-*tert*-butylcyclohexane this fixes the
ring conformation.

For the *cis* isomer, both substituents are on the same face. With *tert*-butyl
equatorial (up at C4), the bromine at C1 must also be up, and the up position at C1 is
axial. So the *cis* isomer places the bromine axial. The adjacent C2 and C6 hydrogens
then include a trans-diaxial hydrogen, and the H–C–C–Br dihedral is close to 180°.
E2 is fast, and the product is 4-*tert*-butylcyclohex-1-ene.

For the *trans* isomer, *tert*-butyl equatorial (up at C4) forces bromine down at C1,
which is equatorial. An equatorial leaving group has no trans-diaxial β-hydrogen: the
adjacent C–H bonds are either equatorial (syn-periplanar, about 60°) or axial but on
the same face. Elimination is therefore very slow, and it can only proceed through a
higher-energy chair in which the *tert*-butyl group is forced axial — which costs more
than 20 kJ mol⁻¹.

**Answer.** The *cis* isomer eliminates rapidly from the chair with an axial bromine;
the *trans* isomer is slow because its bromine is equatorial.

**Check.** This is the standard experimental test of the anti-periplanar requirement:
two diastereomers of the same constitution react at wildly different rates, which no
purely electronic argument can explain.

**Where marks are lost.** Saying "*cis* is axial" without specifying which chair, or
forgetting that the *tert*-butyl group is the conformational anchor.

### 28. Bromination of 2,3-dimethylbutane **multi-step**

**Strategy.** Identify the types of hydrogen, apply the statistical and reactivity
factors.

**Working.** 2,3-Dimethylbutane is $\ce{(CH3)2CH-CH(CH3)2}$. There are twelve
equivalent primary hydrogens (four methyl groups, all equivalent by symmetry) and two
equivalent tertiary hydrogens.

The weighted contributions are $12 \times 1 = 12$ for the primary positions and
$2 \times 1600 = 3200$ for the tertiary positions, total 3212.

The percentages are $12/3212 = 0.37\%$ and $3200/3212 = 99.63\%$.

**Answer.** 99.6 % 2-bromo-2,3-dimethylbutane and 0.4 % 1-bromo-2,3-dimethylbutane.

**Check.** The product is a single constitutional isomer in practical terms, which is
why bromination can be used preparatively where chlorination cannot. The calculation
also shows that the statistical factor of 12 is powerless against a reactivity factor
of 1600.

**Where marks are lost.** Using the tertiary:primary ratio directly (1600:1) and
forgetting to multiply by the hydrogen counts.

### 29. Alkyne reactions **multi-step**

**Strategy.** For each reagent, decide the stereochemistry of addition and whether
the reaction stops at the alkene.

**Working.** Hex-3-yne is $\ce{CH3CH2-C#C-CH2CH3}$, a symmetrical internal alkyne.

(a) Hydrogenation over Lindlar catalyst (palladium on calcium carbonate poisoned with
lead acetate and quinoline) delivers two hydrogen atoms from the same face. The
product is *(Z)*-hex-3-ene.

(b) Dissolving-metal reduction with sodium in liquid ammonia proceeds through a
radical anion and a vinyl radical, and the protonation steps give the
thermodynamically more stable trans arrangement. The product is *(E)*-hex-3-ene.

(c) One equivalent of $\ce{HBr}$ adds across the triple bond. The first addition gives
a vinyl bromide; because the alkyne is symmetrical there is no regiochemical issue,
but the alkene can be either *(E)* or *(Z)*, so the product is 3-bromohex-3-ene as a
mixture of geometrical isomers.

(d) Mercury(II)-catalysed hydration adds water across the triple bond with Markovnikov
regiochemistry. The first-formed enol tautomerises to a ketone. For the symmetrical
hex-3-yne there is no regiochemical ambiguity, and the product is hexan-3-one.

**Answer.** (a) *(Z)*-hex-3-ene. (b) *(E)*-hex-3-ene. (c) 3-Bromohex-3-ene
(*E*/*Z* mixture). (d) Hexan-3-one.

**Check.** The contrast between (a) and (b) is the standard test of *syn* versus
*anti* hydrogenation. In (d), the oxygen ends up on one of the two former alkyne
carbons and the product has the same carbon skeleton; the enol intermediate,
$\ce{CH3CH2-C(OH)=CH-CH2CH3}$, is not isolable and tautomerises immediately.

**Where marks are lost.** Giving hexane in (a) or (b) by over-reduction, or giving
hexane-3,4-dione in (d) by assuming oxidative cleavage rather than hydration.

### 30. Structure determination by ozonolysis **multi-step**

**Strategy.** Use the degree of unsaturation, then work backwards from the carbonyl
products to the alkene.

**Working.** $\ce{C6H12}$ has
$\text{DU} = (12 + 2 - 12)/2 = 1$, so the molecule contains exactly one ring or one
double bond. Ozonolysis cleaves $\ce{C=C}$, so the compound is an acyclic alkene.

Ozonolysis converts each alkene carbon into a carbonyl carbon: a $\ce{CH2}$ becomes
formaldehyde, a $\ce{CHR}$ becomes an aldehyde, and a $\ce{CR2}$ becomes a ketone. The
only carbonyl product observed is propanone, $\ce{(CH3)2CO}$. Each alkene carbon must
therefore have borne two methyl groups, so both alkene carbons are of the type
$\ce{C(CH3)2}$.

Joining the two halves gives $\ce{(CH3)2C=C(CH3)2}$, which is 2,3-dimethylbut-2-ene,
$\ce{C6H12}$.

**Answer.** 2,3-Dimethylbut-2-ene.

**Check.** Any other $\ce{C6H12}$ alkene would give at least one other carbonyl
product. For example, 2-methylpent-2-ene would give propanone and ethanal; hex-3-ene
would give propanal only. The single-product observation fixes the symmetric
tetramethylethylene structure.

**Where marks are lost.** Writing 2-methylbut-2-ene (five carbons), or forgetting that
formaldehyde would be a product if a terminal $\ce{CH2}$ were present.

### 31. Synthesis of *m*-bromonitrobenzene **multi-step**

**Strategy.** Work backwards from the substitution pattern; the last substituent
introduced must be the one whose director points to the target position.

**Working.** In *m*-bromonitrobenzene the two substituents are meta to each other.
Bromine is an *ortho*/*para* director and the nitro group is a *meta* director. If
bromination is carried out first, the nitro group will enter *ortho* and *para* to the
bromine, giving the wrong isomer. If nitration is carried out first, the nitro group
directs the incoming bromine to the *meta* position, giving the target.

Step 1: nitration with a mixture of concentrated nitric and sulfuric acids.

$$\ce{C6H6(l) + HNO3(aq) ->[H2SO4] C6H5NO2(l) + H2O(l)}$$

Step 2: bromination with bromine and iron(III) bromide, which is harsher than the
analogous reaction on benzene because the nitro group deactivates the ring.

$$\ce{C6H5NO2(l) + Br2(l) ->[FeBr3] C6H4BrNO2(s) + HBr(g)}$$

Note that a Friedel–Crafts reaction would fail on nitrobenzene, but halogenation
still proceeds under forcing conditions.

**Answer.** Nitrate first, then brominate: benzene → nitrobenzene → *m*-bromonitrobenzene.

**Check.** The directing effects are mutually inconsistent, so the order is forced.
The same logic gives *p*-bromonitrobenzene only if the sequence is reversed and the
*ortho*/*para* mixture is separated.

**Where marks are lost.** Reversing the order, or writing "bromination of nitrobenzene
with $\ce{Br2/FeBr3}$ gives the meta product" without explaining why.

### 32. Relative rates and orientation in EAS **multi-step**

**Strategy.** Separate the rate effect (activating or deactivating) from the
orientation effect (o/p or meta).

**Working.** The substituents in order of increasing activation are:
$\ce{-NO2}$ (strongly deactivating, meta), $\ce{-Cl}$ (weakly deactivating, o/p),
$\ce{-H}$ (reference), $\ce{-CH3}$ (weakly activating, o/p).

Relative rates of nitration are approximately: nitrobenzene $6\times10^{-8}$,
chlorobenzene $3.3\times10^{-2}$, benzene $1$, toluene $25$.

The orientation follows the arenium-ion argument. The nitro group withdraws by both
resonance and induction, destabilising the *ortho* and *para* arenium ions more than
the *meta*, so it directs meta. Chlorine withdraws inductively but donates by
resonance into the *ortho*/*para* positions, so it directs o/p. The methyl group
donates by hyperconjugation and induction, stabilising the *ortho* and *para*
arenium ions, so it directs o/p.

**Answer.** Increasing rate: nitrobenzene < chlorobenzene < benzene < toluene. Nitro
is meta-directing; chlorine and methyl are *ortho*/*para*-directing.

**Check.** The two effects are independent: chlorine is deactivating yet o/p, which is
the classic demonstration that rate and orientation are governed by different
features of the same substituent.

**Where marks are lost.** Ranking chlorobenzene as more reactive than benzene because
"chlorine donates by resonance", or giving the nitro group as o/p because it is
"electron-withdrawing".

### 33. Three reactions of a tertiary bromide **multi-step**

**Strategy.** Classify the reagent as nucleophile or base, note its bulk, and apply
the substrate rules for a tertiary halide.

**Working.** 2-Bromo-2-methylbutane is
$\ce{CH3-C(Br)(CH3)-CH2-CH3}$, a tertiary bromide. It cannot undergo $S_N2$.

(a) Sodium methoxide in methanol is a strong base and a moderate nucleophile, and the
substrate is tertiary. The reaction is $E2$, and the small base removes the more
accessible of the β-hydrogens to give the more substituted alkene (Zaitsev product):
2-methylbut-2-ene.

(b) Water at 25 °C is a weak nucleophile and a weak base in a polar protic solvent.
The bromide ionises slowly to the tertiary carbocation ($S_N1$), which is captured by
water to give 2-methylbutan-2-ol. A small amount of $E1$ elimination gives
2-methylbut-2-ene as a minor product.

(c) Potassium *tert*-butoxide in *tert*-butanol is a strong, very bulky base. It
cannot reach the more hindered internal β-hydrogen, so it removes a methyl hydrogen
and gives the less substituted alkene (Hofmann product): 2-methylbut-1-ene.

**Answer.** (a) $E2$, 2-methylbut-2-ene. (b) $S_N1$ (with some $E1$),
2-methylbutan-2-ol as the major product. (c) $E2$, 2-methylbut-1-ene.

**Check.** The three products differ as the theory predicts: the small strong base
gives the thermodynamic alkene, the weak nucleophile gives substitution, and the bulky
base gives the kinetic (Hofmann) alkene.

**Where marks are lost.** Predicting $S_N2$ in (a), or giving the Zaitsev alkene in
(c) because "elimination gives the more substituted alkene" — that rule applies only
to small bases.

### 34. Acidity, phenol and a Williamson ether synthesis **multi-step**

**Strategy.** Rank by conjugate-base stability; then use $K$ for the acid–base
equilibrium; then apply the $S_N2$ requirements to the ether synthesis.

**Working.**

(a) The order is ethanol (16.0) < water (15.7) < phenol (9.95) < 4-nitrophenol
(7.15) < ethanoic acid (4.76).

- Ethanol is less acidic than water because the ethyl group donates electron density
  inductively and destabilises the alkoxide.
- Phenol is about $10^6$ times more acidic than ethanol because the phenoxide negative
  charge is delocalised onto the *ortho* and *para* ring carbons by resonance.
- 4-Nitrophenol is more acidic still because the nitro group withdraws inductively and
  by resonance, and the para position is one that carries charge in the phenoxide.
- Ethanoic acid is far more acidic than any phenol because the carboxylate charge is
  shared equally by two oxygen atoms, which is a much larger stabilisation than
  delocalisation into a ring.

(b) The relevant equilibrium is $\ce{PhOH + OH^- <=> PhO^- + H2O}$, with
$K = 10^{15.7-9.95} = 10^{5.75} \approx 5.6\times10^{5}$, so deprotonation is
essentially complete and phenol dissolves. For ethanol,
$K = 10^{15.7-16.0} = 10^{-0.3} = 0.5$: at equal formal concentrations only about
40 % is deprotonated at equilibrium, the solution is still dominated by ethanol, and no
dissolution of a separate organic phase is observed.

(c) Phenol is first converted into sodium phenoxide with aqueous sodium hydroxide.
The phenoxide is then treated with bromoethane (or iodoethane) in a polar aprotic
solvent: the phenoxide oxygen attacks the primary carbon in an $S_N2$ reaction, with
bromide as the leaving group.

$$\ce{C6H5O^-(aq) + CH3CH2Br(l) -> C6H5OCH2CH3(l) + Br^-(aq)}$$

The aryl halide cannot be the electrophile because the carbon–halogen bond on an
$sp^2$ carbon is short and strong, backside attack is blocked by the ring, and the
$S_N2$ transition state would require the nucleophile to pass through the plane of the
aromatic ring. Nucleophilic aromatic substitution is possible only when the ring bears
strong electron-withdrawing groups that stabilise the Meisenheimer intermediate.

**Answer.** (a) As listed. (b) Phenol is deprotonated almost completely by hydroxide
($K \approx 5.6\times10^{5}$); ethanol is not ($K \approx 0.5$).
(c) Phenol → sodium phenoxide → ethoxybenzene with bromoethane; the aryl halide is
inert to $S_N2$.

**Check.** The $K$ values are consistent with the $\mathrm{p}K_a$ difference in each
case, and the phenol reaction is the standard test that distinguishes a phenol from an
alcohol.

**Where marks are lost.** Omitting the numerical $K$ comparison, or writing
"ethoxybenzene from bromobenzene and ethoxide", which fails.

### 35. Carbonyl reactions **multi-step**

**Strategy.** Classify each as nucleophilic addition, aldol, Grignard addition or
reduction, and check whether a dehydration is possible.

**Working.**

(a) Benzaldehyde has no α-hydrogen, so it can only act as the electrophile. Acetophenone forms an enolate at its methyl group, which attacks the benzaldehyde
carbonyl. The β-hydroxy ketone dehydrates under the basic conditions and on heating to
give the conjugated enone: 1,3-diphenylprop-2-en-1-one (chalcone).

(b) Propanal has α-hydrogens. Hydroxide removes one to give the enolate, which attacks
a second molecule of propanal. Protonation gives 3-hydroxy-2-methylpentanal. On
heating, a second enolate forms and hydroxide is eliminated to give the conjugated
enone: 2-methylpent-2-enal.

(c) Cyclohexanone is a ketone; one equivalent of methylmagnesium bromide adds to the
carbonyl carbon. Acidic work-up protonates the alkoxide: 1-methylcyclohexan-1-ol.

(d) Ethanal is reduced by sodium borohydride, which delivers hydride to the carbonyl
carbon; the alkoxide is protonated by methanol: ethanol.

**Answer.** (a) Chalcone, 1,3-diphenylprop-2-en-1-one. (b) 2-Methylpent-2-enal.
(c) 1-Methylcyclohexan-1-ol. (d) Ethanol.

**Check.** In (a) and (b) the product is conjugated, which is why dehydration occurs;
in (c) and (d) no dehydration is possible under the stated conditions. The carbon
count in (b) is six (two propanal units), matching 2-methylpent-2-enal.

**Where marks are lost.** Stopping at the β-hydroxy carbonyl in (a) or (b), or
attacking the ketone with hydride in (d) to give an alkane.

### 36. Acid derivatives and the reactivity ladder **multi-step**

**Strategy.** All five are nucleophilic acyl substitutions; the only question is which
nucleophile and which leaving group.

**Working.** Ethanoyl chloride is the most reactive member of the family because
chloride is an excellent leaving group and the carbonyl carbon is strongly
electrophilic. The mechanism is the same in every case: the nucleophile adds to the
carbonyl carbon to give a tetrahedral intermediate, which collapses by expelling
chloride.

(a) Ethanol in pyridine: the alcohol oxygen attacks, pyridine mops up the $\ce{HCl}$.
Product: ethyl ethanoate.

(b) Excess ammonia: the amine attacks, giving ethanamide after loss of $\ce{NH4Cl}$.
Excess ammonia is needed to neutralise the $\ce{HCl}$ produced.

(c) Methylamine: gives *N*-methylethanamide.

(d) Water: gives ethanoic acid and $\ce{HCl}$.

(e) Dimethylamine: gives *N*,*N*-dimethylethanamide.

**Answer.** (a) Ethanol/pyridine, ethyl ethanoate. (b) Excess $\ce{NH3}$, ethanamide.
(c) $\ce{CH3NH2}$, *N*-methylethanamide. (d) $\ce{H2O}$, ethanoic acid.
(e) $\ce{(CH3)2NH}$, *N*,*N*-dimethylethanamide.

**Check.** Each product is one rung down the reactivity ladder from the acid chloride,
which is why an acid chloride is the reagent of choice for making esters and amides:
the reaction is fast and irreversible.

**Where marks are lost.** Trying to make the amide from the ester and ammonia without
catalysis, or forgetting the pyridine in (a) — without it the $\ce{HCl}$ protonates
the alcohol and the yield falls.

---

## Part D — Advanced problems

### 37. Fischer projection to R/S **multi-step**

**Strategy.** Interpret the Fischer convention, assign priorities at each centre,
determine the observed sense, and reverse it for a horizontal lowest-priority group.

**Working.** In a Fischer projection the vertical bonds point away from the viewer and
the horizontal bonds point towards the viewer. The carbon chain is vertical, so the
$\ce{CH3}$ at the top and the adjacent carbon at the bottom are both behind the plane.

At C2 the groups are $\ce{-OH}$ (1; oxygen), C3 (2; carbon bearing Br, C and H),
$\ce{-CH3}$ (3) and $\ce{-H}$ (4). The OH is on the left, C3 below, CH3 above, and H on
the right, pointing towards the viewer. With the lowest-priority group pointing
towards the viewer, the observed sense must be reversed. The observed sequence
1 → 2 → 3 runs from the left substituent to the bottom to the top, which is
anticlockwise; reversing gives *(R)*.

At C3 the groups are $\ce{-Br}$ (1), C2 (2; carbon bearing O, C, H), $\ce{-CH3}$ (3)
and $\ce{-H}$ (4). The Br is on the left, C2 above, CH3 below, H on the right, again
pointing towards the viewer. The observed sequence 1 → 2 → 3 runs from the left to the
top to the bottom, which is clockwise; reversing gives *(S)*.

**Answer.** *(2R,3S)*-3-bromobutan-2-ol.

**Check.** A useful check is to rotate the molecule so that H is vertical in both
centres; the descriptors should not change. The two centres are inequivalent, so no
*meso* form exists and the molecule is chiral.

**Where marks are lost.** Forgetting the reversal for a horizontal H (the single most
common error in Fischer problems), or assigning priority by the position of the
substituent in the drawing rather than by CIP rules.

### 38. cis- and trans-1,2-dimethylcyclohexane **multi-step**

**Strategy.** Use the up/down alternation at C1 and C2, then apply the A-value.

**Working.** At C1 and C2 the axial bonds point in opposite senses (one up, one down).
Therefore:

- *cis*-1,2-Dimethylcyclohexane has both methyls on the same face, so one is axial and
  one is equatorial in either chair: (a,e).
- *trans*-1,2-Dimethylcyclohexane has the methyls on opposite faces, so both can be
  equatorial: (e,e). The alternative (a,a) chair is much higher in energy.

The energy of an axial methyl group relative to equatorial is the A-value,
7.6 kJ mol⁻¹. The *cis* isomer necessarily has one axial methyl; the *trans* isomer
can have none. The energy difference is therefore 7.6 kJ mol⁻¹, and the *trans* isomer
is more stable.

**Answer.** *cis*: (a,e). *trans*: (e,e) is the stable chair. The *trans* isomer is
more stable by 7.6 kJ mol⁻¹.

**Check.** At 298 K the equilibrium constant for *cis* ⇌ *trans* is
$K = \exp(7600/2478) = 21.5$, so the *trans* isomer predominates strongly — consistent
with the observed greater stability of *trans*-1,2-dimethylcyclohexane.

**Where marks are lost.** Assigning *cis*-1,2 as (e,e), which would require both
methyls to be on opposite faces.

### 39. Chlorination of 2-methylpropane **multi-step**

**Strategy.** Identify the hydrogen types, apply the statistical and reactivity
factors, then interpret the result.

**Working.** 2-Methylpropane (isobutane) is $\ce{(CH3)3CH}$. There are nine equivalent
primary hydrogens and one tertiary hydrogen.

The weighted contributions are $9 \times 1 = 9$ and $1 \times 5 = 5$, total 14.

The percentages are $9/14 = 64.3\%$ for 1-chloro-2-methylpropane and $5/14 = 35.7\%$
for 2-chloro-2-methylpropane.

The tertiary product is not major because the reactivity factor of 5 applies to one
hydrogen, whereas the statistical factor of 9 applies to nine hydrogens. The product
ratio is the product of the two factors, not the reactivity ratio alone.

**Answer.** 64.3 % 1-chloro-2-methylpropane and 35.7 % 2-chloro-2-methylpropane.

**Check.** The same substrate with bromine (1600 : 1) would give
$9 : 1600$, i.e. 99.4 % of the tertiary bromide, which is why bromination is the
preparative method for that compound.

**Where marks are lost.** Reporting 5:1 (83 % tertiary) by ignoring the nine primary
hydrogens.

### 40. Addition with rearrangement **multi-step**

**Strategy.** Protonate to give a carbocation, test whether a 1,2-shift can give a
more stable cation, then trap.

**Working.** 3,3-Dimethylbut-1-ene is $\ce{CH2=CH-C(CH3)3}$. Protonation at C1, the
terminal carbon, gives a secondary carbocation at C2:

$$\ce{CH2=CH-C(CH3)3 + H^+ -> CH3-CH^+-C(CH3)3}$$

This cation is adjacent to a quaternary carbon bearing three methyl groups. A
1,2-methyl shift moves one methyl group with its bonding pair from C3 to C2, leaving
the positive charge at C3:

$$\ce{CH3-CH^+-C(CH3)3 -> CH3-CH(CH3)-C^+(CH3)2}$$

The new cation is tertiary and therefore substantially more stable. Chloride attacks
it to give 2-chloro-2,3-dimethylbutane.

The unrearranged product, 2-chloro-3,3-dimethylbutane, would require capture of the
secondary cation before the shift. Rearrangement of a secondary to a tertiary cation
is fast and essentially irreversible, so the secondary cation is consumed by the shift
faster than it is trapped.

**Answer.** 2-Chloro-2,3-dimethylbutane, formed by a 1,2-methyl shift.

**Check.** The carbon skeleton has changed: the product has a $\ce{CH(CH3)-C(CH3)2Cl}$
unit, not the original quaternary centre. This is the diagnostic sign of a
rearrangement, and it is why the product is a single constitutional isomer.

**Where marks are lost.** Proposing a hydride shift from a carbon with no hydrogen, or
drawing the shift without showing that the new cation is tertiary.

### 41. Naphthalene: nitration and sulfonation **multi-step**

**Strategy.** Compare arenium-ion stability for attack at C1 and C2, then apply
kinetic versus thermodynamic control to the reversible sulfonation.

**Working.** Naphthalene has two distinct positions: C1 (the α position, adjacent to
the ring fusion) and C2 (the β position).

Attack at C1 gives an arenium ion that can be written with the positive charge at C2,
C4, and the fusion carbon C8a, while one benzene ring remains intact in two of the
resonance forms. Attack at C2 gives an arenium ion whose resonance forms disrupt the
π system of both rings in all but one contributor. The C1 transition state is
therefore lower in energy, and nitration — which is irreversible — gives
1-nitronaphthalene.

Sulfonation is reversible. At 160 °C the reaction reaches equilibrium, and the product
distribution is governed by thermodynamic stability. The 1-sulfonic acid suffers steric
repulsion between the sulfonic acid group and the peri hydrogen at C8; the 2-isomer
does not. The 2-isomer is therefore the more stable and dominates at high temperature.
At lower temperature (about 80 °C) the reaction is under kinetic control and the
1-isomer predominates.

**Answer.** Nitration: 1-nitronaphthalene, kinetic control, more stable arenium ion.
Sulfonation at 160 °C: naphthalene-2-sulfonic acid, thermodynamic control, less steric
strain.

**Check.** The two outcomes are not contradictory: they are the same molecule reacting
under kinetic and thermodynamic control respectively, which is exactly what the
reversibility of sulfonation allows.

**Where marks are lost.** Claiming that C2 is intrinsically more reactive, or
forgetting that sulfonation is reversible.

### 42. Solvolysis kinetics **multi-step**

**Strategy.** Recognise a first-order reaction, then use the integrated rate law.

**Working.** For a first-order reaction, $t_{1/2} = \ln 2/k$:

$$t_{1/2} = \frac{0.6931}{2.4\times10^{-5}\ \text{s}^{-1}} = 2.89\times10^{4}\ \text{s} = 8.0\ \text{h}$$

For 90 % conversion, $[A]/[A]_0 = 0.10$, so

$$t_{0.9} = \frac{\ln 10}{k} = \frac{2.303}{2.4\times10^{-5}} = 9.6\times10^{4}\ \text{s} = 26.7\ \text{h}$$

The mechanism is $S_N1$: the rate-determining step is ionisation of the
carbon–bromine bond to give a tertiary carbocation, so the rate law is first order in
the substrate and independent of the concentration of water or ethanol.

**Answer.** $t_{1/2} = 8.0\ \text{h}$; $t_{0.9} = 26.7\ \text{h}$; rate
$= k[(\ce{CH3})3\ce{CBr}]$.

**Check.** 90 % conversion takes about 3.3 half-lives ($3.32 \times 8.0 = 26.6$ h),
which is the standard rule of thumb.

**Where marks are lost.** Using $t_{1/2} = 1/k$, or quoting a second-order rate law
because "water is the nucleophile".

### 43. Malonic ester synthesis **multi-step**

**Strategy.** Build the α-substituted acid by two alkylations of diethyl malonate,
then hydrolyse and decarboxylate.

**Working.** Diethyl malonate is $\ce{CH2(CO2C2H5)2}$; its α-hydrogens are acidic
($\mathrm{p}K_a \approx 13$) because the resulting enolate is flanked by two ester
carbonyls.

Step 1: sodium ethoxide in ethanol removes one α-hydrogen to give the enolate.

Step 2: bromoethane alkylates the enolate by $S_N2$ to give diethyl ethylmalonate,
$\ce{CH(CH2CH3)(CO2C2H5)2}$.

Step 3: a second equivalent of sodium ethoxide and iodomethane give diethyl
ethyl(methyl)malonate, $\ce{C(CH3)(CH2CH3)(CO2C2H5)2}$.

Step 4: aqueous acid and heat hydrolyse both esters to the dicarboxylic acid,
2-ethyl-2-methylpropanedioic acid.

Step 5: continued heating decarboxylates the β-dicarboxylic acid. The mechanism
involves a six-membered cyclic transition state in which one carboxyl hydrogen is
transferred to the other carboxyl group as $\ce{CO2}$ leaves, giving an enol that
tautomerises to the acid. The product is 2-methylbutanoic acid,
$\ce{CH3CH2CH(CH3)CO2H}$.

**Answer.** 1. $\ce{NaOEt}$; 2. $\ce{CH3CH2Br}$; 3. $\ce{NaOEt}$, then $\ce{CH3I}$;
4. $\ce{H3O+}$, heat; 5. continued heat to decarboxylate. Product: 2-methylbutanoic
acid.

**Check.** The carbon count works: malonate contributes three carbons (the central
carbon plus two carboxyls, one of which is lost), ethyl adds two and methyl adds one,
giving five carbons in the acid.

**Where marks are lost.** Using only one alkylation, which gives 2-ethylbutanoic acid
after decarboxylation rather than the required 2-methylbutanoic acid; or attempting
decarboxylation without hydrolysis.

### 44. Grignard retrosynthesis and a failed preparation **multi-step**

**Strategy.** Disconnect the C–C bond to the carbinol carbon; check the reagent for
acidic hydrogens.

**Working.** 2-Methylpentan-2-ol is $\ce{(CH3)2C(OH)-CH2CH2CH3}$, a tertiary alcohol.
The two C–C bonds to the carbinol carbon that carry alkyl groups can be disconnected:

Route A: methylmagnesium bromide plus pentan-2-one,
$\ce{CH3COCH2CH2CH3}$.

Route B: propylmagnesium bromide plus propan-2-one, $\ce{(CH3)2CO}$.

Both are valid. After addition, aqueous acidic work-up protonates the alkoxide.

A Grignard reagent cannot be prepared from 4-bromobutan-2-ol because the molecule
contains an acidic $\ce{O-H}$ group. As soon as any Grignard forms, it is destroyed by
the alcohol proton in an acid–base reaction:

$$\ce{RMgX + R'OH -> RH + R'OMgX}$$

The alkoxide that results is not reactive towards magnesium, so the chain reaction
stops. The problem is solved by protecting the alcohol first — as a *tert*-
butyldimethylsilyl ether, a tetrahydropyranyl ether or a benzyl ether — then forming
the Grignard, adding the carbonyl, and removing the protecting group afterwards.

**Answer.** (a) $\ce{CH3MgBr}$ + pentan-2-one, or $\ce{CH3CH2CH2MgBr}$ + propan-2-one.
(b) The free hydroxyl group protonates the Grignard; protect it as a silyl, THP or
benzyl ether.

**Check.** The same argument explains why a Grignard cannot be made from a substrate
containing a carboxylic acid, an amine or a terminal alkyne — all have acidic protons.

**Where marks are lost.** Ignoring the hydroxyl group, or writing that the Grignard
"reacts with the oxygen" without specifying proton transfer.

### 45. Diels–Alder stereochemistry and regiochemistry **multi-step**

**Strategy.** Apply the *cis* principle, then the *endo* rule, then the "ortho" rule
for an electron-rich diene with an electron-poor dienophile.

**Working.**

(a) Cyclopentadiene is locked in the *s-cis* conformation and is a very reactive
diene. Methyl prop-2-enoate is an electron-poor dienophile. The product is a
bicyclo[2.2.1]heptene bearing the ester group at C2; the two new bonds form on the same
face of each component, so the relative configuration of the dienophile is retained.

Two diastereomers are possible: *endo*, with the ester group pointing towards the
bridging methylene, and *exo*, with it pointing away. Under kinetic control the *endo*
isomer dominates, because the ester carbonyl can overlap with the back lobes of the
diene in the transition state (secondary orbital interaction), which lowers the
activation energy. The *exo* isomer is thermodynamically more stable, so prolonged
heating or a reversible diene can invert the ratio.

(b) 1-Methoxybuta-1,3-diene is an electron-rich diene with a substituent at C1, and
methyl prop-2-enoate has its electron-withdrawing group at C1. The two substituents
end up on adjacent ring carbons — the "ortho" product — because that arrangement
maximises the coefficient match between the diene HOMO (largest at C4) and the
dienophile LUMO (largest at the substituted carbon). The *endo* preference still
operates.

**Answer.** (a) The *endo*-bicyclo[2.2.1]hept-5-ene-2-carboxylate dominates under
kinetic control because of secondary orbital overlap. (b) The "ortho" adduct, with the
methoxy and ester groups on adjacent carbons.

**Check.** The rules are consistent: the *cis* principle fixes relative configuration,
the *endo* rule fixes the diastereofacial outcome, and the ortho/para rule fixes
regiochemistry. Each is a separate question and must be answered separately.

**Where marks are lost.** Confusing *endo* with *trans*, or applying the *endo* rule as
if it were a statement about thermodynamic stability.

### 46. Retrosynthesis of 3-methyl-1-phenylpentan-3-ol **multi-step**

**Strategy.** Identify the target as a tertiary alcohol; disconnect the C–C bonds to
the carbinol carbon; compare the routes for availability and chemoselectivity.

**Working.** The target is $\ce{PhCH2CH2-C(OH)(CH3)-CH2CH3}$. The carbinol carbon C3
carries a phenyl-ethyl group, a methyl group and an ethyl group.

Disconnection 1: break the bond between C3 and C2, giving the synthons
$\ce{PhCH2CH2^-}$ ($d^1$) and $\ce{CH3COCH2CH3}$ ($a^1$). The reagent for the anion is
2-phenylethylmagnesium bromide, made from (2-bromoethyl)benzene and magnesium in dry
ether.

Disconnection 2: break the bond between C3 and the methyl group, giving $\ce{CH3^-}$
and $\ce{PhCH2CH2COCH2CH3}$ (1-phenylpentan-3-one). The reagent is methylmagnesium
bromide.

Both disconnections are "natural": a $d^1$ carbanion attacking an $a^1$ carbonyl.

Route 1: $\ce{PhCH2CH2Br + Mg -> PhCH2CH2MgBr}$; then add butan-2-one; then aqueous
$\ce{NH4Cl}$ work-up. Route 2: $\ce{CH3MgBr}$ plus 1-phenylpentan-3-one, which itself
has to be made (for example by Friedel–Crafts acylation or by a crossed aldol followed
by hydrogenation), adding at least one step.

Route 1 is preferable: the carbonyl component is cheap and the Grignard precursor is
commercially available, so the sequence is shorter and avoids building the ketone.

**Answer.** Disconnect at C3–C2: $\ce{PhCH2CH2MgBr}$ + butan-2-one, then acidic
work-up. Alternative: $\ce{CH3MgBr}$ + 1-phenylpentan-3-one. Choose the first for step
economy.

**Check.** Count carbons: phenethyl (8) + butan-2-one (4) = 12, matching the target
$\ce{C12H18O}$. The product is tertiary because the carbonyl carbon becomes the
carbinol carbon and already carries two carbon substituents.

**Where marks are lost.** Proposing a Grignard bearing a free $\ce{OH}$ or $\ce{NH2}$
group, or disconnecting to a carbocation at the tertiary centre (which is not a valid
synthon for a Grignard addition).

---

## Part E — Mechanism and diagram problems

### 47. Radical chlorination of 2-methylpropane

**Strategy.** Write the three phases, then connect the propagation steps to the
product ratio.

**Working.**

**Initiation.** Chlorine absorbs ultraviolet light and undergoes homolysis:

$$\ce{Cl2(g) ->[h\nu] 2Cl^{.}(g)}$$

Electron movement: the $\ce{Cl-Cl}$ σ bond breaks homolytically, one electron going to
each chlorine atom.

**Propagation, step 1 — hydrogen abstraction.** A chlorine atom abstracts a hydrogen
from 2-methylpropane. Electron movement: the $\ce{C-H}$ σ bond pair moves to form the
$\ce{H-Cl}$ bond, and the second electron of the pair is left on carbon.

$$\ce{Cl^{.} + (CH3)3CH -> HCl + (CH3)3C^{.}}$$

The same step at a methyl group gives the primary radical
$\ce{^{.}CH2C(CH3)2H}$.

**Propagation, step 2 — halogen transfer.** The alkyl radical abstracts a chlorine
atom from $\ce{Cl2}$. Electron movement: one electron of the $\ce{Cl-Cl}$ bond pairs
with the radical electron to form the new $\ce{C-Cl}$ bond, and the other electron
stays on the departing chlorine.

$$\ce{(CH3)3C^{.} + Cl2 -> (CH3)3CCl + Cl^{.}}$$

**Termination.** Any two radicals combine: $\ce{Cl^{.} + Cl^{.} -> Cl2}$,
$\ce{(CH3)3C^{.} + Cl^{.} -> (CH3)3CCl}$, and
$\ce{2(CH3)3C^{.} -> (CH3)3C-C(CH3)3}$.

**Stereochemistry.** Neither product contains a stereocentre: the tertiary chloride
has three identical methyl groups on the central carbon, and the primary chloride has
two identical methyl groups on C2. No stereochemical consequence arises.

**Connecting to the ratio.** The two competing hydrogen-abstraction steps have
different barriers and different statistical weights. The primary abstraction can
occur at nine equivalent hydrogens, the tertiary at one. With the relative rates
1 : 5 per hydrogen, the flux through the primary channel is $9 \times 1 = 9$ and
through the tertiary channel $1 \times 5 = 5$, giving 64.3 % and 35.7 % respectively.

**Answer.** As above; the mechanism accounts for the ratio through nine primary
hydrogens competing with one tertiary hydrogen.

**Check.** The propagation steps form a closed cycle: the chlorine atom consumed in
step 1 is regenerated in step 2, so a single initiation event can produce many
thousands of product molecules. Termination steps are rare because the steady-state
radical concentration is very low.

**Where marks are lost.** Omitting termination, or writing the propagation steps with
heterolytic arrow pushing.

### 48. Addition of HCl with rearrangement

**Strategy.** Protonate to give a carbocation, look for a 1,2-shift, then trap.

**Working.**

**Step 1 — protonation.** The alkene π bond attacks the hydrogen of $\ce{HCl}$.
Electron movement: the π pair forms the new $\ce{C-H}$ bond at C1, and the
$\ce{H-Cl}$ bond pair moves onto chlorine.

$$\ce{CH2=CH-C(CH3)3 + HCl -> CH3-CH^+-C(CH3)3 + Cl^-}$$

Intermediate: a secondary carbocation at C2, with the positive charge in an empty
$p$ orbital perpendicular to the plane of the adjacent $\ce{C-H}$ bonds.

**Step 2 — 1,2-methyl shift.** The $\ce{C3-C(methyl)}$ σ bond breaks and its pair
forms a new bond to C2. Electron movement: the σ pair migrates from the methyl carbon
to C2. The positive charge moves to C3.

$$\ce{CH3-CH^+-C(CH3)3 -> CH3-CH(CH3)-C^+(CH3)2}$$

Intermediate: a tertiary carbocation, more stable than the secondary cation because
three alkyl groups donate by induction and hyperconjugation.

**Step 3 — chloride attack.** The chloride ion donates a lone pair to the cationic
carbon. Electron movement: a chlorine lone pair forms the $\ce{C-Cl}$ bond at C3.

$$\ce{CH3-CH(CH3)-C^+(CH3)2 + Cl^- -> CH3-CH(CH3)-C(Cl)(CH3)2}$$

**Stereochemistry.** The tertiary carbocation is planar, so attack can occur from
either face. However, the product has two identical methyl groups on C3 and two
identical methyl groups on C2's substituent set, so no stereocentre is created and the
product is achiral. If a stereocentre had been created, the result would be a racemate.

**Answer.** 2-Chloro-2,3-dimethylbutane, via a 1,2-methyl shift from a secondary to a
tertiary carbocation.

**Check.** The rearranged cation has its positive charge on a carbon bearing three
carbon substituents; the unrearranged one has two. The driving force is the difference
in cation stability, about 15–20 kJ mol⁻¹.

**Where marks are lost.** Drawing a hydride shift (there is no hydride on C3), or
failing to state that the intermediate cation is planar and therefore gives both faces.

### 49. Nitration of toluene

**Strategy.** Generate the nitronium ion, then compare arenium ions for the three
positions.

**Working.**

**Step 1 — formation of the electrophile.** Sulfuric acid protonates nitric acid,
which loses water to give the nitronium ion:

$$\ce{HNO3(l) + 2H2SO4(l) -> NO2^+(g) + H3O^+(l) + 2HSO4^-(l)}$$

Electron movement: a nitrogen–oxygen π pair moves onto oxygen as the protonated
hydroxyl group leaves as water.

**Step 2 — attack at the *ortho* position.** The ring π bond attacks the nitrogen of
$\ce{NO2^+}$. Electron movement: the π pair forms the new $\ce{C-N}$ bond, and the
positive charge moves to the carbon bearing the methyl group (C1).

The arenium ion has three resonance contributors: positive charge at C1, at C3 and at
C5. The contributor with the charge at C1 is tertiary and is stabilised by
hyperconjugation from the methyl group (three $\ce{C-H}$ bonds can donate).

**Step 3 — attack at the *para* position.** The arenium ion has the charge at C1, C3
and C5 in the same way, again including the tertiary contributor at C1.

**Step 4 — attack at the *meta* position.** The arenium ion has the charge at C2, C4
and C6; none of these carries the methyl group, so no tertiary contributor is
available and no hyperconjugative stabilisation operates.

**Step 5 — deprotonation.** A hydrogen sulfate ion removes the new proton from the
carbon that bears it; the two electrons of the $\ce{C-H}$ bond return to the ring to
restore the aromatic sextet. The product is nitrotoluene and the acid catalyst is
regenerated.

**Explanation of orientation.** The *ortho* and *para* transition states are both
stabilised by the tertiary arenium-ion contributor; the *meta* is not. Toluene is
therefore *ortho*/*para* directing.

**Explanation of the ratio.** Statistically there are two *ortho* positions and one
*para*, so a purely statistical ratio would be 2:1. The observed ratio is about
58 % *ortho* to 37 % *para* (with about 5 % *meta*), because the *ortho* positions are
hindered by the methyl group. The small amount of *meta* product reflects the residual
reactivity of the unsubstituted positions.

**Answer.** Nitration gives mainly *ortho*- and *para*-nitrotoluene, in a ratio of
about 58:37, with 5 % *meta*.

**Check.** The mechanism predicts that a bulky alkyl group gives even more *para*
product, which is observed; and that a methyl group increases the overall rate, which
is also observed (about 25 times benzene).

**Where marks are lost.** Drawing only one resonance structure of the arenium ion, or
attributing the orientation to "electron density" without the arenium-ion argument.

### 50. SN2 and SN1 at the same substrate

**Strategy.** Two separate mechanisms, two separate stereochemical predictions.

**Working.**

**(a) $S_N2$ with hydroxide.**

The hydroxide lone pair attacks the carbon bearing bromine from the side opposite the
leaving group. Electron movement: a hydroxide lone pair forms the $\ce{C-O}$ bond,
and simultaneously the $\ce{C-Br}$ σ pair moves onto bromine. The transition state is
trigonal bipyramidal at carbon, with the three retained groups ($\ce{H}$, $\ce{CH3}$,
$\ce{C2H5}$) in a plane and $\ce{HO}$ and $\ce{Br}$ at the two apices.

Because the nucleophile enters opposite the leaving group, the configuration at the
carbon inverts. Starting from *(R)*-2-bromobutane the product is *(S)*-butan-2-ol.
The reaction is second order: rate $= k_2[\ce{RBr}][\ce{OH^-}]$.

**(b) $S_N1$ in aqueous ethanol.**

Step 1: the $\ce{C-Br}$ bond ionises heterolytically. Electron movement: the
$\ce{C-Br}$ σ pair stays on bromine, and the carbon is left with an empty $p$ orbital.
The intermediate is a planar secondary carbocation, stabilised by hyperconjugation
from the five adjacent $\ce{C-H}$ bonds.

$$\ce{CH3CH(Br)CH2CH3 -> CH3CH^+CH2CH3 + Br^-}$$

Step 2: water (or ethanol) donates a lone pair to the empty $p$ orbital. Because the
cation is planar, attack occurs from both faces at equal rates, giving equal amounts
of the two enantiomers. Electron movement: an oxygen lone pair forms the $\ce{C-O}$
bond.

Step 3: loss of a proton gives the alcohol.

The rate law is first order: rate $= k_1[\ce{RBr}]$, independent of the nucleophile
concentration.

**Why the optical purity is not exactly zero.** The leaving bromide ion remains close
to the carbocation as an ion pair and can return to the same face before it diffuses
away, which gives a small excess of the inverted product. Solvent attack also occurs
preferentially on the face from which the leaving group departed, for the same
reason. The result is racemisation with a slight inversion bias, not perfect
racemisation.

**Answer.** (a) $S_N2$, inversion, *(S)*-butan-2-ol, second order. (b) $S_N1$, planar
cation, racemisation with slight inversion bias, first order.

**Check.** The stereochemical predictions are opposite, which is the experimental
signature that distinguishes the two mechanisms. The rate laws differ in their
dependence on hydroxide concentration, which is the kinetic signature.

**Where marks are lost.** Saying that $S_N1$ gives "a racemic mixture" without the
ion-pair caveat, or drawing the $S_N2$ transition state with the nucleophile and
leaving group on the same side.

### 51. Base-catalysed aldol condensation of propanal

**Strategy.** Enolate formation, addition, protonation, then a second enolate and
elimination.

**Working.**

**Step 1 — enolate formation.** Hydroxide removes an α-hydrogen from propanal.
Electron movement: the $\ce{C-H}$ σ pair becomes the $\ce{C=C}$ π bond, and the
$\ce{C=O}$ π pair moves onto oxygen.

$$\ce{CH3CH2CHO + OH^- <=> [CH3CHCHO]^- + H2O}$$

Intermediate: the enolate, a resonance hybrid with negative charge on carbon and on
oxygen.

**Step 2 — nucleophilic addition.** The enolate carbon attacks the carbonyl carbon of
a second propanal molecule. Electron movement: the enolate $\ce{C=C}$ π pair forms the
new $\ce{C-C}$ bond, and the second carbonyl's π pair moves onto its oxygen.

Intermediate: an alkoxide with the new $\ce{C-C}$ bond and a $\ce{C-O^-}$ group.

**Step 3 — protonation.** Water protonates the alkoxide. Electron movement: an oxygen
lone pair of water forms the $\ce{O-H}$ bond, and the $\ce{O-H}$ pair of water returns
to water.

Product: 3-hydroxy-2-methylpentanal, a β-hydroxy aldehyde.

**Step 4 — second enolate and elimination.** Hydroxide removes the α-hydrogen at C2
(the carbon between the two carbonyl-derived centres). Electron movement: the
$\ce{C-H}$ σ pair forms the $\ce{C=C}$ π bond, and the $\ce{C-O}$ σ pair of the
hydroxyl departs onto oxygen, expelling hydroxide.

Product: 2-methylpent-2-enal, an α,β-unsaturated aldehyde.

**Why elimination is favourable.** The product is conjugated: the $\ce{C=C}$ and
$\ce{C=O}$ π systems overlap, which lowers the energy by roughly 30 kJ mol⁻¹ relative to
an isolated enol. In addition, two molecules become three (the eliminated water is a
separate particle), so the entropy change is positive, and hydroxide is a competent
leaving group because the resulting enolate is stabilised.

**Stereochemistry.** The carbon at C3 of the aldol adduct is a stereocentre, because it
bears $\ce{H}$, $\ce{OH}$, the methyl-bearing carbon and the ethyl group. It is formed
as a racemate, because the enolate can attack either face of the planar carbonyl group
of the second propanal molecule. The stereocentre is destroyed in the dehydration step,
so the final enone is achiral apart from the alkene geometry, which is fixed as *(E)*
by the preference for the larger groups to be opposite.

**Answer.** Propanal → 3-hydroxy-2-methylpentanal → 2-methylpent-2-enal.

**Check.** Carbon count: two propanal units give six carbons, which matches
2-methylpent-2-enal ($\ce{C6H10O}$). The degree of unsaturation rises from 1 to 2,
consistent with the loss of water.

**Where marks are lost.** Forming the enolate at the wrong carbon (propanal has only
one α-carbon, so this is not possible — but students often try to deprotonate the
aldehyde hydrogen), or omitting the protonation step and writing an alkoxide as the
final product.

### 52. Conrotatory ring opening of a cyclobutene

**Strategy.** Count the π electrons, apply the Woodward–Hoffmann rule, then track the
substituents through the rotation.

**Working.** Cyclobutene ring opening is an electrocyclic process involving four π
electrons (the ring σ bond plus one π bond). This is a $4n$ system with $n = 1$. The
Woodward–Hoffmann table gives **conrotatory** motion for a $4n$ system under thermal
conditions.

**Why conrotatory: the orbital argument.** The σ bond that breaks is formed from the
in-phase combination of the $p$ orbitals at C3 and C4. In the highest occupied
molecular orbital of the four-electron system, the terminal lobes at C3 and C4 have
opposite phases on the same face of the molecule. To convert the σ bond into the two
new π bonds of the diene, the lobes that overlap must be of the same phase. If the two
termini rotate in opposite directions (disrotatory), lobes of opposite phase meet.
If they rotate in the same direction (conrotatory), the lobes of the same phase come
together. The reaction is therefore conrotatory.

**Tracking the methyl groups.** In *cis*-3,4-dimethylcyclobutene both methyl groups
are on the same face. Conrotatory opening rotates both termini in the same direction,
so one methyl group moves upwards and the other moves downwards. The two methyl groups
therefore end up on opposite sides of the diene framework.

In the product, the double bonds are between C2–C3 and C4–C5. One methyl is on the
same side as the adjacent chain, the other is on the opposite side. The result is
*(2E,4Z)*-hexa-2,4-diene: one double bond has its two high-priority groups opposite
(*E*), the other has them together (*Z*).

**Answer.** Thermal conrotatory opening of *cis*-3,4-dimethylcyclobutene gives
*(2E,4Z)*-hexa-2,4-diene. The *trans* isomer, by the same motion, gives
*(2E,4E)*-hexa-2,4-diene.

**Check.** The *cis* principle of the Diels–Alder reaction and the conrotatory rule of
the electrocyclic reaction are both consequences of orbital symmetry; a stepwise
radical mechanism would give a mixture of *E*/*Z* isomers, which is not observed.

**Where marks are lost.** Applying the $4n+2$ rule (disrotatory) to a four-electron
system, or saying "both methyls rotate the same way so they stay on the same side" —
that is precisely the error the question is testing.

---

## Part F — Multiple-choice self-check

### 53. Name of $\ce{(CH3)3CCH2CH2CH3}$

**Strategy.** Find the longest chain, number it from the end that gives the lower locant
set, and name the substituents alphabetically.

**Working.** The longest chain contains five carbons. Numbering from the end nearest
the branch gives the two methyl groups locants 2 and 2; numbering from the other end
would give 4 and 4, which is higher. The locant set 2,2 is therefore preferred.

**Answer: A.** 2,2-Dimethylpentane.

**Why B is wrong.** 3,3-Dimethylpentane would require the quaternary carbon to be the
middle carbon of a five-carbon chain, which is a different constitution.

**Why D is wrong.** 4,4-Dimethylpentane numbers from the wrong end: reading the same
structure from the other terminus gives locants 2,2, which are lower and therefore
preferred.

**Why C is wrong.** It has the wrong parent length; the longest chain is five, not six.

**Check.** Reading the name back gives $\ce{CH3-C(CH3)2-CH2-CH2-CH3}$, which is the
given structure, so the name is invertible.

**Where marks are lost.** Choosing D by counting from the written left-hand end
without comparing locant sets.

### 54. Stereoisomers of 2,3-dichlorobutane

**Strategy.** Enumerate the configuration at each of the two equivalent stereocentres
and test each combination for internal symmetry.

**Working.** The possible combinations are *(2R,3R)*, *(2S,3S)* and *(2R,3S)*, which is
the same compound as *(2S,3R)*. The *(2R,3R)* and *(2S,3S)* forms are non-superimposable
mirror images; the *(2R,3S)* form has a mirror plane and is *meso*.

**Answer: C (three).** Two enantiomers plus one *meso* compound.

**Why D is wrong.** Four would be correct if the two stereocentres were inequivalent;
here the *meso* form reduces the count by one.

**Why B is wrong.** Two would ignore the *meso* diastereomer entirely.

**Why A is wrong.** One would ignore stereoisomerism altogether.

**Check.** The count can be verified by constructing the four arrangements and testing
each for superimposability; only three distinct compounds result.

**Where marks are lost.** Applying $2^n$ without checking for a *meso* form.

### 55. Which species is aromatic?

**Strategy.** Test each candidate against Hückel's criteria: cyclic, planar, fully
conjugated, and $4n+2$ π electrons.

**Working.** The cycloheptatrienyl cation has a seven-membered ring with seven $p$
orbitals, one of which is vacant, and six π electrons: $4n+2$ with $n = 1$. The ring is
planar, so it is aromatic.

**Answer: C.** The cycloheptatrienyl cation.

**Why A is wrong.** Cyclooctatetraene has eight π electrons and distorts into a tub
that breaks conjugation; it is non-aromatic, not aromatic.

**Why B is wrong.** The cyclopentadienyl cation has four π electrons, $4n$ with
$n = 1$, and is antiaromatic.

**Why D is wrong.** Cyclobutadiene also has four π electrons and is antiaromatic.

**Check.** All four species are cyclic and conjugated, so the discriminator is the
electron count and the planarity — which is exactly what Hückel's rule tests.

**Where marks are lost.** Counting electrons without checking planarity and
conjugation.

### 56. Fastest SN2 reaction of 1-bromobutane

**Strategy.** Match the substrate, the nucleophile, the solvent and the temperature to
the requirements of a one-step concerted $S_N2$ displacement.

**Working.** 1-Bromobutane is primary, so $S_N2$ is available. The best nucleophile
among the options is iodide, and acetone is a polar aprotic solvent that leaves the
nucleophile unsolvated. The reaction is the Finkelstein exchange, and the precipitation
of sodium bromide drives it to completion.

**Answer: B.** Sodium iodide in acetone.

**Why A is wrong.** Water is a weak nucleophile and a polar protic solvent, so
solvolysis by $S_N1$ is slow and $S_N2$ is disfavoured.

**Why C is wrong.** Potassium *tert*-butoxide is a strong, bulky base; with a primary
substrate it gives mainly $E2$ elimination.

**Why D is wrong.** Ethanol at reflux is a solvolysis medium (weak nucleophile, protic
solvent), so substitution is slow.

**Check.** The choice satisfies all four variables simultaneously: primary substrate,
good nucleophile, polar aprotic solvent, moderate temperature. Changing any one of them
would weaken the case for $S_N2$.

**Where marks are lost.** Choosing the strongest base rather than the best
nucleophile.

### 57. Fastest reaction with ethanol and pyridine

**Strategy.** Rank the four acid derivatives by leaving-group ability and by the
electrophilicity of the carbonyl carbon.

**Working.** The reactivity ladder is acid chloride > anhydride > ester > amide. Chloride
is an excellent leaving group and withdraws inductively, making the carbonyl carbon
strongly electrophilic; the amide nitrogen donates its lone pair into the carbonyl and
is a very poor leaving group. Ethanoyl chloride therefore reacts fastest with ethanol.

**Answer: C.** Ethanoyl chloride.

**Why B is wrong.** Ethyl ethanoate is an ester; reaction with ethanol would be a
transesterification, which requires acid or base catalysis and is an equilibrium.

**Why D is wrong.** Ethanoic acid reacts with ethanol only under acid catalysis
(Fischer esterification), and the equilibrium is unfavourable without removal of
water.

**Why A is wrong.** Ethanamide is the least reactive derivative: the nitrogen lone
pair delocalises into the carbonyl, and amide is a very poor leaving group.

**Check.** The ranking matches the relative hydrolysis rates in Chapter 11, which span
sixteen orders of magnitude from the acid chloride ($10^{11}$) to the amide
($10^{-5}$) relative to the ester.

**Where marks are lost.** Ranking by "acidity" rather than by leaving-group ability
and carbonyl electrophilicity.

### 58. Selective reduction of a ketone in the presence of an ester

**Strategy.** Compare the reducing power and the functional-group selectivity of the
four reagents.

**Working.** Sodium borohydride delivers hydride to aldehydes and ketones but is not
reactive enough to attack the less electrophilic carbonyl of an ester, an amide or a
carboxylate. Lithium aluminium hydride is far more reactive and reduces all of them.
Hydrogen over palladium reduces carbon–carbon π bonds, and permanganate is an oxidant.

**Answer: B.** $\ce{NaBH4}$ in methanol.

**Why A is wrong.** Lithium aluminium hydride is a strong reductant and reduces
esters to primary alcohols as well as ketones to secondary alcohols.

**Why C is wrong.** Catalytic hydrogenation over palladium does not reduce isolated
ketones under mild conditions; it reduces alkenes and alkynes.

**Why D is wrong.** Hot aqueous permanganate is an oxidant and would oxidise the
ketone further (cleaving it) rather than reduce it.

**Check.** The selectivity is the standard one used in synthesis: a molecule containing
both a ketone and an ester can be reduced at the ketone with $\ce{NaBH4}$ and at the
ester later with $\ce{LiAlH4}$, in either order.

**Where marks are lost.** Forgetting that $\ce{LiAlH4}$ also reduces esters.

---

## Top ten errors in this level

| Rank | Error | Why it costs marks | Correct habit |
|---|---|---|---|
| 1 | Omitting the reversal when the lowest-priority group points towards the viewer | Inverts every *(R)/(S)* assignment | Mark the H direction before deciding; reverse if it is towards you |
| 2 | Reporting a reactivity ratio as a product ratio | Ignores the statistical factor | Always multiply by the number of equivalent hydrogens |
| 3 | Counting four stereoisomers when a *meso* form exists | Overcounts by one | Check for a mirror plane in the *(R,S)* combination |
| 4 | Reversing kinetic and thermodynamic enolates | Wrong regioisomer in every alkylation | Kinetic = bulky base, low temperature, less substituted |
| 5 | Drawing an arenium ion with only one resonance structure | Cannot explain orientation | Draw all contributors and locate the positive charge |
| 6 | Giving the Zaitsev alkene with a bulky base | Wrong Hofmann product | Bulky base removes the accessible β-H |
| 7 | Applying *cis*/*trans* where each alkene carbon bears two different groups | Ambiguous or wrong descriptor | Use *(E)/(Z)* whenever the four groups are not paired |
| 8 | Treating the ring flip as a change of configuration | Wrong stereoisomer | A flip breaks no bond; only axial/equatorial labels swap |
| 9 | Using $S_N2$ conditions on a tertiary substrate | No reaction, or elimination instead | Tertiary carbon: $S_N1$ or $E2$ only |
| 10 | Forgetting the ion-pair caveat in $S_N1$ | "Perfectly racemic" is marked wrong | $S_N1$ gives racemisation with a slight inversion bias |
