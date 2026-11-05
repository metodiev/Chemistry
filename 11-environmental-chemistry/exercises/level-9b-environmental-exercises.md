# Level 9b — Environmental Chemistry: Exercise Set

> **Level:** 9b — Environmental Chemistry (advanced undergraduate / applied)
> **Estimated time:** ≈ 300 minutes
> **Covers:** [Ch. 1 Green and Sustainable Chemistry](../01-green-and-sustainable-chemistry.md), [Ch. 2 Atmospheric Chemistry](../02-atmospheric-chemistry.md), [Ch. 3 Water Chemistry and Water Pollution](../03-water-chemistry-and-pollution.md), [Ch. 4 Waste Treatment and Circular Chemistry](../04-waste-treatment.md)
> **Structure:** 48 numbered exercises in Parts A–E plus six multiple-choice self-check items (F1–F6). **Total 250 marks.**

## How to use this set

Work through the bank in the order shown. Parts A and B test recall and single-step
fluency; Parts C and D require you to chain two or more relations; Part E is a
timed calculation set; Part F checks that you can recognise the correct statement
under exam conditions. Do not open the solutions file until you have written an
answer to every item you intend to attempt.

```mermaid
flowchart TD
    A["Read the four chapter summaries"] --> B["Part A: state each principle and mechanism aloud"]
    B --> C{"Can you explain it without notes?"}
    C -->|"No"| D["Re-read the named chapter section"]
    D --> B
    C -->|"Yes"| E["Part B: single-step drills"]
    E --> F["Part C: multi-step problems"]
    F --> G["Part D: open-ended synthesis"]
    G --> H["Part E: full calculations under time"]
    H --> I["Part F: multiple-choice self-check"]
    I --> J{"Any item below 80 percent?"}
    J -->|"Yes"| K["Log the error, then rework that item"]
    K --> F
    J -->|"No"| L["Move on to the next level"]
```

**Figure 1 — A route through the bank.** The loop back from the mistake log is the
part that matters: an item answered twice with the error explained is worth more
than three items answered once.

## Conventions used in this set

- Mixing ratios in air are **mole fractions**: ppm = $10^{-6}$, ppb = $10^{-9}$.
  Concentrations in water are **mass per volume**, with the basis stated.
- $R = 8.314462618\ \text{J mol}^{-1}\ \text{K}^{-1}$;
  $N_A = 6.02214076\times10^{23}\ \text{mol}^{-1}$;
  $h = 6.62607015\times10^{-34}\ \text{J s}$;
  $c = 2.99792458\times10^{8}\ \text{m s}^{-1}$;
  $k_B = 1.380649\times10^{-23}\ \text{J K}^{-1}$.
- Molar volume of an ideal gas is $22.71\ \text{dm}^{3}\ \text{mol}^{-1}$ at
  273.15 K and $10^{5}$ Pa. Standard pressure is $101.325$ kPa unless stated.
- Report every answer to the significant figures justified by the data, and state
  the assumption that dominates the uncertainty.

---

## Part A — Conceptual questions (10 items, 2 marks each)

**A1.** [Ch. 1] The twelve principles of green chemistry are commonly grouped under
three objectives: reduce hazard, reduce material, reduce energy.

(a) Assign each of the twelve principles to one of the three groups.
(b) Identify one principle that could sit in two groups and justify the choice.
(c) Give one concrete pair of principles that pull in opposite directions, and
state how the conflict is resolved in a real process rather than in a slogan.
(d) Explain why principle 1 (prevention) is a design instruction and not simply
"do not produce waste".

**A2.** [Ch. 1] For a single reaction, define atom economy, E-factor, process mass
intensity and reaction mass efficiency.

(a) State what question each metric answers and the boundary each one assumes.
(b) Explain how a route can have an atom economy of 100 % and an E-factor of
$40\ \text{kg kg}^{-1}$.
(c) State which single metric you would put first in a report to a plant manager,
and which you would put first in a report to a regulator. Justify both choices.

**A3.** [Ch. 1]

(a) Distinguish *bio-based*, *biodegradable* and *compostable*, and give one
example of a material that is bio-based but not biodegradable.
(b) Explain the design-for-degradation logic using EDTA and a biodegradable
chelating agent as the contrast.
(c) Explain why a substance that is "readily biodegradable" in a standard test may
still persist in a river.

**A4.** [Ch. 2]

(a) Name the four layers of the atmosphere in order and state where the tropopause
lies and why it is a temperature minimum.
(b) Explain why the stratosphere is statically stable while the troposphere is not,
and connect this to the vertical transport of pollutants.
(c) Explain why the tropopause acts as only a *partial* lid, and what that implies
for the residence time of a species emitted at the surface.

**A5.** [Ch. 2]

(a) Write the four reactions of the Chapman mechanism, with phases and with the
wavelength threshold for the photolysis step.
(b) Explain why the mechanism overpredicts the stratospheric ozone column by about
a factor of two.
(c) Name one reservoir species for chlorine and one for nitrogen, and explain what
converting a reservoir into an active species does to the rate of ozone loss.

**A6.** [Ch. 2]

(a) Explain why the Antarctic ozone hole is a spring phenomenon rather than a
year-round one.
(b) Write the two heterogeneous reactions that occur on polar stratospheric cloud
surfaces.
(c) Define denitrification in this context and explain why it prolongs ozone loss.

**A7.** [Ch. 2]

(a) Distinguish a VOC-limited from a NOx-limited regime.
(b) Explain the chemical reason why reducing NOx emissions in a VOC-limited city
can *increase* surface ozone.
(c) Explain the weekend effect in the same terms, and state the monitoring evidence
that would let you decide which regime a city is in.

**A8.** [Ch. 2]

(a) Compare the gas-phase and the aqueous oxidation routes of $\ce{SO2}$ and state
which route dominates inside cloud droplets.
(b) Define critical load and explain why it depends on bedrock geology.
(c) Explain why lake chemistry can continue to deteriorate after deposition has
fallen.

**A9.** [Ch. 3]

(a) Distinguish pH, alkalinity and hardness, giving the units of each.
(b) Distinguish an open from a closed carbonate system and give one field example
of each.
(c) Explain how a water at pH 7.0 can be poorly buffered.

**A10.** [Ch. 4]

(a) State the five levels of the waste hierarchy in order.
(b) Give two circumstances in which a lower-ranked option genuinely outperforms a
higher-ranked one on a life-cycle basis.
(c) Explain how extended producer responsibility changes a manufacturer's design
incentive, using packaging as the example.

---

## Part B — Basic problems (10 items, 3 marks each)

**B11.** [Ch. 1] Toluene is nitrated to mononitrotoluene:

$$
\ce{C7H8(l) + HNO3(aq) -> C7H7NO2(l) + H2O(l)}
$$

$M(\text{toluene}) = 92.14$, $M(\ce{HNO3}) = 63.01$,
$M(\text{mononitrotoluene}) = 137.14\ \text{g mol}^{-1}$.

Calculate the atom economy and state whether it is a property of the reaction or
of the process.

**B12.** [Ch. 1] A batch process produces $250\ \text{kg}$ of product and
$3000\ \text{kg}$ of waste, where the waste figure includes solvent and aqueous
streams inside the plant gate.

Calculate the E-factor and the process mass intensity, and state the boundary you
have assumed.

**B13.** [Ch. 2] The atmospheric burden of methane is $3500\ \text{Tg}$ and the
total source is $500\ \text{Tg yr}^{-1}$.

(a) Calculate the residence time.
(b) Explain why the same calculation applied to $\ce{CO2}$ does not give a
meaningful atmospheric lifetime.

**B14.** [Ch. 2] A monitoring station reports ozone at $40\ \text{ppb}$ (mole
fraction).

(a) Convert this to $\mu\text{g m}^{-3}$ at 298 K and $101.325$ kPa.
(b) Repeat at 273.15 K and $101.325$ kPa.
(c) Calculate the corresponding conversion factor for $\ce{NO2}$
($M = 46.01\ \text{g mol}^{-1}$) at 298 K and explain why the temperature must be
quoted alongside any $\text{ppb} \to \mu\text{g m}^{-3}$ conversion.

**B15.** [Ch. 3] A groundwater contains $1.50\ \text{mmol dm}^{-3}$ of
$\ce{Ca^{2+}}$ and $0.50\ \text{mmol dm}^{-3}$ of $\ce{Mg^{2+}}$.

Calculate the hardness in $\text{mg dm}^{-3}$ as $\ce{CaCO3}$, convert it to German
degrees ($1\ ^{\circ}\text{dH} = 17.85\ \text{mg dm}^{-3}$ as $\ce{CaCO3}$) and
classify the water.

**B16.** [Ch. 3] An unseeded BOD test is run on a sample diluted to
$2.5\ \%$ by volume. The initial dissolved oxygen of the diluted sample is
$8.4\ \text{mg dm}^{-3}$ and the final value is $4.9\ \text{mg dm}^{-3}$.

Calculate $\mathrm{BOD}_5$ and check whether the depletion lies inside the usual
validity window.

**B17.** [Ch. 3] A water at pH 7.8 contains $2.40\ \text{mmol dm}^{-3}$ of
bicarbonate, and the carbonate concentration is negligible at this pH.

Calculate the alkalinity in $\text{meq dm}^{-3}$ and in $\text{mg dm}^{-3}$ as
$\ce{CaCO3}$.

**B18.** [Ch. 4] A fly-ash extract gives the following congener concentrations.
Use the toxic equivalency factors supplied and calculate the TEQ.

| Congener | $c_i$ / $\text{ng g}^{-1}$ | TEF |
|---|---|---|
| 2,3,7,8-TCDD | 1.5 | 1.0 |
| 1,2,3,7,8-PeCDD | 4.0 | 1.0 |
| 2,3,4,7,8-PeCDF | 6.0 | 0.3 |
| 2,3,7,8-TCDF | 12 | 0.1 |
| 1,2,3,4,7,8-HxCDF | 9.0 | 0.1 |
| OCDD | 200 | 0.0003 |

**B19.** [Ch. 2]

(a) Calculate the radiative forcing for a $\ce{CO2}$ increase from 280 ppm to
420 ppm using $\Delta F = 5.35\ln(C/C_0)\ \text{W m}^{-2}$.
(b) Explain why the forcing is logarithmic in concentration rather than linear.
(c) Explain why $\ce{N2}$ and $\ce{O2}$ are not greenhouse gases while $\ce{CO2}$
and $\ce{CH4}$ are.

**B20.** [Ch. 4] A leachate has a strong-acid content equivalent to
$0.020\ \text{mol dm}^{-3}$ of $\ce{H+}$. A batch of $50\ \text{m}^{3}$ must be
neutralised with slaked lime, $M(\ce{Ca(OH)2}) = 74.09\ \text{g mol}^{-1}$.

(a) Calculate the stoichiometric lime mass.
(b) Calculate the mass required with $10\ \%$ excess.
(c) State why the plant dose is normally higher than either value.

---

## Part C — Intermediate problems (12 items, 5 marks each)

**C21.** [Ch. 1] Two routes make the same epoxide, $M = 58.08\ \text{g mol}^{-1}$.

*Route A*, stoichiometric chlorohydrin:

$$
\ce{C3H6(g) + Cl2(g) + Ca(OH)2(s) -> C3H6O(l) + CaCl2(aq) + H2O(l)}
$$

with $M(\ce{C3H6}) = 42.08$, $M(\ce{Cl2}) = 70.90$,
$M(\ce{Ca(OH)2}) = 74.09\ \text{g mol}^{-1}$.

*Route B*, catalytic epoxidation:

$$
\ce{C3H6(g) + H2O2(aq) ->[TS-1] C3H6O(l) + H2O(l)}
$$

with $M(\ce{H2O2}) = 34.01\ \text{g mol}^{-1}$.

Process data per $1000\ \text{kg}$ of product, plant-gate boundary:

| Item | Route A / kg | Route B / kg |
|---|---|---|
| Reactants charged (including excess) | 3400 | 1420 |
| Organic solvent | 8000 | 1500 |
| Process water | 2000 | 500 |
| Product | 1000 | 1000 |

(a) Calculate the atom economy of each route.
(b) Calculate the E-factor, the process mass intensity and the reaction mass
efficiency of each process.
(c) Which metric carries the decision, and which single number would mislead a
reader who saw it alone?

**C22.** [Ch. 1] A C10 feedstock is oxidatively cleaved to a C9 product, releasing
one mole of $\ce{CO2}$ per mole of product. The yield on the feedstock is
$85\ \%$.

(a) Calculate the carbon efficiency when unreacted feedstock is not recycled.
(b) Recalculate it when unreacted feedstock is recycled to extinction.
(c) Explain in one sentence why carbon efficiency and yield differ here, while they
coincide for an isomerisation.

**C23.** [Ch. 2] At noon, $J_{\ce{NO2}} = 6.0\times10^{-3}\ \text{s}^{-1}$ and
$k(\ce{NO + O3}) = 1.8\times10^{-14}\ \text{cm}^{3}\ \text{molecule}^{-1}\
\text{s}^{-1}$. The ratio $[\ce{NO2}]/[\ce{NO}] = 3.0$.

(a) Calculate $[\ce{O3}]$ in molecules $\text{cm}^{-3}$ from the Leighton
relationship and convert it to ppb at 298 K and $101.325$ kPa.
(b) Calculate the photolysis lifetime of $\ce{NO2}$.
(c) Calculate $[\ce{O3}]$ if the ratio $[\ce{NO2}]/[\ce{NO}]$ doubles, all else
equal.
(d) State the chemical reason why a measured urban ozone concentration can exceed
the Leighton value.

**C24.** [Ch. 2] In the lower stratosphere the dominant chlorine cycle is

$$
\ce{ClO(g) + ClO(g) + M(g) -> Cl2O2(g) + M(g)}
\qquad
\ce{Cl2O2(g) ->[h\nu] 2Cl(g) + O2(g)}
\qquad
\ce{Cl(g) + O3(g) -> ClO(g) + O2(g)}
$$

Take $T = 210\ \text{K}$ at 20 km, with
$[\ce{ClO}] = 1.0\times10^{10}$, $[\ce{Cl}] = 2.0\times10^{4}$,
$[\ce{O3}] = 4.0\times10^{12}$ and $[\ce{O}] = 1.0\times10^{6}$ molecules
$\text{cm}^{-3}$. Take
$k(\ce{ClO + ClO + M}) = 2.0\times10^{-14}\ \text{cm}^{3}\
\text{molecule}^{-1}\ \text{s}^{-1}$ (pseudo-second order, $M$ folded in),
$k(\ce{Cl + O3}) = 1.2\times10^{-11}$ and
$k(\ce{ClO + O}) = 3.8\times10^{-11}\ \text{cm}^{3}\
\text{molecule}^{-1}\ \text{s}^{-1}$.

(a) Derive the net reaction of the dimer cycle.
(b) Calculate the rate of ozone destruction by each of the three cycles.
(c) State the percentage of the total carried by the dimer cycle and the fractional
ozone loss per day.
(d) Recalculate the dimer rate when $[\ce{ClO}]$ is halved, and state the
implication for a chlorine-loading trend.

**C25.** [Ch. 2] Rain in an industrial region contains
$6.0\ \text{mg dm}^{-3}$ of sulfate (expressed as $\ce{SO4^{2-}}$),
$3.0\ \text{mg dm}^{-3}$ of nitrate (as $\ce{NO3^-}$) and
$0.9\ \text{mg dm}^{-3}$ of ammonium (as $\ce{NH4^+}$). Take
$M(\ce{SO4^{2-}}) = 96.06$, $M(\ce{NO3^-}) = 62.00$,
$M(\ce{NH4^+}) = 18.04\ \text{g mol}^{-1}$.

(a) Calculate the acid equivalent concentration from sulfate and nitrate.
(b) Calculate the pH before and after allowing for ammonium neutralisation.
(c) Compare with the pH of unpolluted rain in equilibrium with atmospheric
$\ce{CO2}$ (pH 5.6) and state how many times more acidic the sample is.
(d) State which anion you would expect to dominate dry deposition downwind, and
why.

**C26.** [Ch. 2] A 24-hour $\text{PM}_{2.5}$ filter sample from an urban site gives
the following composition.

| Component | Concentration / $\mu\text{g m}^{-3}$ |
|---|---|
| Sulfate (as $\ce{SO4^{2-}}$) | 5.2 |
| Nitrate (as $\ce{NO3^-}$) | 3.1 |
| Ammonium (as $\ce{NH4^+}$) | 2.4 |
| Organic carbon | 4.0 |
| Elemental carbon | 1.8 |
| Crustal and other | 1.9 |

(a) Calculate the total $\text{PM}_{2.5}$ mass and the mass fraction of secondary
inorganic aerosol.
(b) Test whether the ammonium is sufficient to neutralise the sulfate and nitrate
completely, and state what the result implies about aerosol acidity.
(c) State whether this concentration complies with an annual guideline of
$5\ \mu\text{g m}^{-3}$, and by what factor it exceeds it.
(d) Explain why the sulfate is not reported as $\ce{H2SO4}$ even when the aerosol is
acidic.

**C27.** [Ch. 3] A surface water at $25\ ^\circ\text{C}$ has pH 8.10 and a total
alkalinity of $1.80\ \text{meq dm}^{-3}$. Take
$K_{a1} = 4.3\times10^{-7}$, $K_{a2} = 4.7\times10^{-11}$ and
$K_H = 3.4\times10^{-2}\ \text{mol dm}^{-3}\ \text{atm}^{-1}$.

(a) Calculate $[\ce{HCO3^-}]$ and $[\ce{CO3^{2-}}]$.
(b) Calculate the total inorganic carbon $C_T$.
(c) Calculate the equilibrium partial pressure of $\ce{CO2}$ and compare it with
the present atmospheric value of $420\ \mu\text{atm}$.
(d) State whether the water will degas or absorb $\ce{CO2}$, and what that implies
for the downstream pH trend.

**C28.** [Ch. 3] Carbon dioxide is dissolved in pure water in a sealed vessel to
give $C_T = 2.0\ \text{mmol dm}^{-3}$ with no other source of alkalinity. Take
$K_{a1} = 4.3\times10^{-7}$ and $K_{a2} = 4.7\times10^{-11}$.

(a) Write the charge balance and show that it reduces to
$[\ce{H+}] \approx [\ce{HCO3^-}]$.
(b) Calculate the pH.
(c) Calculate the fraction of $C_T$ present as $\ce{HCO3^-}$ and as
$\ce{CO2(aq) + H2CO3}$.
(d) Explain why this pH is lower than the pH of a water at the same $C_T$ that is
open to the atmosphere.

**C29.** [Ch. 3] A wastewater is analysed twice.

*BOD:* diluted to $3.0\ \%$ by volume; initial dissolved oxygen of the diluted
sample $8.8\ \text{mg dm}^{-3}$, final $3.1\ \text{mg dm}^{-3}$; seed blank falls
from $8.5$ to $7.6\ \text{mg dm}^{-3}$; seed correction factor $f = 0.85$.

*COD:* $20.00\ \text{cm}^{3}$ of sample is refluxed with $10.00\ \text{cm}^{3}$ of
$0.04167\ \text{mol dm}^{-3}$ $\ce{K2Cr2O7}$; the excess is back-titrated with
$0.1000\ \text{mol dm}^{-3}$ iron(II) ammonium sulfate. The blank titre is
$24.60\ \text{cm}^{3}$ and the sample titre is $15.40\ \text{cm}^{3}$.

$$
\ce{Cr2O7^{2-}(aq) + 14H+(aq) + 6e^- -> 2Cr^{3+}(aq) + 7H2O(l)}
\qquad
\ce{Fe^{2+}(aq) -> Fe^{3+}(aq) + e^-}
$$

(a) Calculate $\mathrm{BOD}_5$.
(b) Calculate the COD in $\text{mg dm}^{-3}$ as $\ce{O2}$.
(c) Calculate the $\mathrm{BOD}_5/\mathrm{COD}$ ratio and interpret it.
(d) Explain why the two numbers differ.

**C30.** [Ch. 3] A water has $3.5\ \text{mg dm}^{-3}$ of dissolved organic carbon.
Chlorination converts $0.20\ \%$ of that carbon to chloroform,
$M = 119.37\ \text{g mol}^{-1}$.

(a) Estimate the chloroform concentration in $\mu\text{g dm}^{-3}$.
(b) Compare it with a total THM limit of $80\ \mu\text{g dm}^{-3}$ and calculate the
headroom as a percentage of the limit.
(c) Recalculate the concentration if coagulation removes $40\ \%$ of the dissolved
organic carbon before chlorination.
(d) State two operational changes, other than precursor removal, that would reduce
the chloroform concentration, and one penalty of each.

**C31.** [Ch. 3] A surface-water plant doses alum, $\ce{Al2(SO4)3}$,
$M = 342.15\ \text{g mol}^{-1}$, at an optimum jar-test dose of
$28\ \text{mg dm}^{-3}$. The raw-water alkalinity is $0.60\ \text{meq dm}^{-3}$.
Aluminium hydrolysis consumes three bicarbonate equivalents per aluminium.

Downstream, a reverse-osmosis unit treats $1000\ \text{m}^{3}\ \text{d}^{-1}$ at
$75\ \%$ recovery. The feed nitrate is $12\ \text{mg dm}^{-3}$ and the permeate
nitrate is $2.0\ \text{mg dm}^{-3}$.

(a) Calculate the aluminium dose in $\text{mg dm}^{-3}$.
(b) Calculate the alkalinity consumed by the coagulant, in
$\text{meq dm}^{-3}$ and in $\text{mg dm}^{-3}$ as $\ce{CaCO3}$, and the residual
alkalinity.
(c) Calculate the nitrate concentration in the concentrate and the concentration
factor relative to the feed.
(d) Explain why the concentrate, not the permeate, is the compliance problem.

**C32.** [Ch. 4] The biodegradable fraction of municipal waste in one landfill cell
is modelled as cellulose, $\ce{C6H10O5}$, $M = 162.14\ \text{g mol}^{-1}$. The cell
receives $1.0\ \text{t}$ of this material and reaches complete anaerobic conversion.
Use the Buswell stoichiometry and a molar volume of
$22.71\ \text{dm}^{3}\ \text{mol}^{-1}$.

(a) Balance the Buswell equation for $\ce{C6H10O5}$ and confirm the atom balance.
(b) Calculate the volume of methane produced per tonne at 273.15 K and $10^{5}$ Pa,
and the mass of methane.
(c) With a capture efficiency of $60\ \%$ and
$\mathrm{GWP}_{100} = 28$ for methane, calculate the $\ce{CO2}$-equivalent emission
from fugitive methane.
(d) If the captured gas is flared with $98\ \%$ destruction, calculate the residual
methane slip in $\ce{CO2}$-equivalent and comment.

---

## Part D — Advanced problems (8 items, 7 marks each)

**D33.** [Ch. 2] A one-dimensional stratospheric box at 20 km and 210 K contains
$[\ce{O3}] = 4.0\times10^{12}$ molecules $\text{cm}^{-3}$. Three loss cycles
operate, with the same rate data as C24.

(a) Calculate the ozone loss rate carried by each cycle.
(b) Calculate the total loss rate and the time to destroy the local ozone if
production ceased.
(c) Explain why the dimer cycle dominates in the lower stratosphere while the
$\ce{ClO + O}$ cycle dominates higher up.
(d) A model predicts that chlorine loading falls by $30\ \%$. Calculate the
resulting change in the dimer loss rate and explain why the response is
non-linear.
(e) State the two dominant uncertainties in this calculation.

**D34.** [Ch. 2] A simplified mechanism for propene oxidation in sunlight is

$$
\ce{C3H6(g) + OH(g) -> RO2(g)}
\qquad
\ce{RO2(g) + NO(g) -> RO(g) + NO2(g)}
\qquad
\ce{RO(g) + O2(g) -> RCHO(g) + HO2(g)}
$$

$$
\ce{HO2(g) + NO(g) -> OH(g) + NO2(g)}
\qquad
\ce{HCHO(g) ->[h\nu] H2(g) + CO(g)}
\qquad
\ce{HCHO(g) ->[h\nu] HCO(g) + H(g)}
$$

Each $\ce{NO2}$ produced photolyses to give one $\ce{O3}$. In the $\ce{HCO}$
branch of formaldehyde photolysis both fragments are oxidised to $\ce{HO2}$:
$\ce{HCO + O2 -> HO2 + CO}$ and $\ce{H + O2 + M -> HO2 + M}$.

(a) Count the $\ce{NO}$-to-$\ce{NO2}$ conversions per propene molecule and hence
the ozone molecules produced per propene molecule, assuming unlimited $\ce{NO}$.
(b) Calculate the ozone formed from $10\ \text{ppb}$ of propene.
(c) Using the Leighton parameters of C23 and $[\ce{NO2}]/[\ce{NO}] = 3.0$,
calculate the $\ce{NO_x}$-only baseline ozone. If the same city measures
$85\ \text{ppb}$ of ozone, calculate the excess that must be attributed to VOC
chemistry and compare it with your answer to (b).
(d) Explain why the same VOC loading produces much less ozone in a
$\ce{NO_x}$-limited rural atmosphere.

**D35.** [Ch. 2 and Ch. 4] A landfill releases $1.0\ \text{t}$ of methane as a
pulse. Use $\mathrm{GWP}_{20} = 80$ and $\mathrm{GWP}_{100} = 28$ for methane, a
lower heating value of $50.0\ \text{MJ kg}^{-1}$ for methane, a gas-engine
electrical efficiency of $40\ \%$ and an avoided grid intensity of
$0.35\ \text{kg CO2}\ \text{kWh}^{-1}$.

(a) Calculate the $\ce{CO2}$-equivalent of the methane over 20 and over 100 years.
(b) Calculate the electricity generated if the methane is burned, and the
$\ce{CO2}$ avoided by displacing grid power.
(c) Calculate the net $\ce{CO2}$ emission of the energy-recovery option, and the
percentage reduction in $\ce{CO2}$-equivalent relative to venting over 100 years.
(d) Explain why the choice of horizon changes the ranking of methane against
$\ce{CO2}$ but not the ranking against coal-fired electricity.

**D36.** [Ch. 3] A cadmium plume in a sandy aquifer has
$K_d = 45\ \text{dm}^{3}\ \text{kg}^{-1}$, aquifer bulk density
$1.6\ \text{kg dm}^{-3}$, porosity $0.35$ and a pore-water velocity of
$0.30\ \text{m d}^{-1}$.

(a) Calculate the retardation factor.
(b) Calculate the velocity of the cadmium front in $\text{m yr}^{-1}$.
(c) Calculate the time for the front to travel $150\ \text{m}$.
(d) The pH of the aquifer falls and $K_d$ drops to
$4.5\ \text{dm}^{3}\ \text{kg}^{-1}$. Recalculate the travel time and comment.
(e) Explain why a single $K_d$ is an inadequate description of metal transport, and
give one speciation change that would increase cadmium mobility.

**D37.** [Ch. 3] A clear-water tank must achieve 3-log inactivation of *Giardia*,
for which the design model requires $\mathrm{CT} = 150\ \text{mg min dm}^{-3}$ at
5 °C. Free chlorine is dosed at $2.0\ \text{mg dm}^{-3}$ and decays first-order
with $k = 0.010\ \text{min}^{-1}$, so that the effective contact integral is

$$
\mathrm{CT_{eff}} = \int_0^t C_0 e^{-kt'}\,\mathrm{d}t' = \frac{C_0}{k}\left(1-e^{-kt}\right).
$$

(a) Calculate $\mathrm{CT_{eff}}$ at a contact time of $60\ \text{min}$.
(b) Calculate the contact time required to reach the target.
(c) The total THM concentration approaches $120\ \mu\text{g dm}^{-3}$ asymptotically
with $k_2 = 0.008\ \text{min}^{-1}$. Calculate the THM concentration at 60 min and at
the contact time from (b), and compare both with an $80\ \mu\text{g dm}^{-3}$ limit.
(d) State the engineering options that break the trade-off, and one limitation of
each.

**D38.** [Ch. 3 and Ch. 4] Powdered activated carbon follows
$q = 45\,C^{0.40}$, with $q$ in $\mu\text{g g}^{-1}$ and $C$ in
$\mu\text{g dm}^{-3}$, for PFOA.

(a) Calculate the carbon dose needed to reduce PFOA from
$0.50\ \mu\text{g dm}^{-3}$ to a target of $0.10\ \mu\text{g dm}^{-3}$ in a
single-stage batch, and the daily carbon consumption for
$5000\ \text{m}^{3}\ \text{d}^{-1}$.
(b) Calculate the mass of PFOA removed per day and the loading on the spent carbon.
(c) Recalculate the dose for a target of $0.004\ \mu\text{g dm}^{-3}$ and state the
practical consequence.
(d) Explain why the spent carbon is a hazardous-waste problem rather than a
solution, and state what must happen to it.

**D39.** [Ch. 4] One tonne of post-consumer PET is considered for two options. PET
repeat unit $\ce{C10H8O4}$, $M = 192.17\ \text{g mol}^{-1}$.

*Option 1, mechanical recycling:* $75\ \%$ mass yield of flake; virgin PET displaced
at $2.3\ \text{kg CO2-eq kg}^{-1}$ and $70\ \text{MJ kg}^{-1}$; recycling process
emissions $0.40\ \text{t CO2-eq}$ per tonne of input.

*Option 2, incineration with energy recovery:* lower heating value
$23\ \text{MJ kg}^{-1}$; net electrical efficiency $25\ \%$; avoided grid intensity
$0.35\ \text{kg CO2}\ \text{kWh}^{-1}$.

(a) Calculate the $\ce{CO2}$ released by complete combustion of one tonne of PET.
(b) Calculate the net $\ce{CO2}$ avoided by recycling.
(c) Calculate the net $\ce{CO2}$ emitted by incineration with energy recovery.
(d) Calculate the difference between the options and the primary energy saved by
each, and state the caveat that limits repeated recycling.

**D40.** [Ch. 2] A city is modelled as a well-mixed box $30\ \text{km}$ by
$30\ \text{km}$ with a mixing height of $500\ \text{m}$. $\ce{NO_x}$ is emitted at
$120\ \text{t d}^{-1}$ (expressed as $\ce{NO2}$, $M = 46.01\ \text{g mol}^{-1}$)
and removed with a first-order lifetime of $12\ \text{h}$. Assume the background
concentration is negligible.

(a) Calculate the box volume and the emission rate in
$\text{mol m}^{-3}\ \text{s}^{-1}$.
(b) Calculate the steady-state $\ce{NO_x}$ concentration in
$\mu\text{g m}^{-3}$ and in ppb at 298 K and $101.325$ kPa.
(c) Compare with an annual limit value of $40\ \mu\text{g m}^{-3}$ and calculate the
emission reduction needed to comply.
(d) State the three assumptions of the box model and the one that dominates the
uncertainty for a city of this size.

---

## Part E — Calculation problems (8 items, 9 marks each)

**E41.** [Ch. 4] A municipal waste has the ultimate analysis (as received):
C $36.0\ \%$, H $4.8\ \%$, O $22.0\ \%$, S $0.5\ \%$, N $1.0\ \%$, moisture
$25.0\ \%$, ash $10.7\ \%$. The furnace runs at $50\ \%$ excess air and all sulfur
is oxidised to $\ce{SO2}$.

$$
\ce{C(s) + O2(g) -> CO2(g)}
\qquad
\ce{H2(g) + 1/2 O2(g) -> H2O(g)}
\qquad
\ce{S(s) + O2(g) -> SO2(g)}
$$

(a) Calculate the stoichiometric oxygen demand in $\text{mol kg}^{-1}$ and in
$\text{kg kg}^{-1}$ of waste.
(b) Calculate the stoichiometric and actual air requirement in
$\text{mol kg}^{-1}$ and $\text{kg kg}^{-1}$ (take air as $21.0\ \%$ $\ce{O2}$ and
$79.0\ \%$ $\ce{N2}$, $M = 28.97\ \text{g mol}^{-1}$).
(c) Calculate the dry flue-gas composition in mole per cent for $\ce{CO2}$,
$\ce{O2}$ and $\ce{N2}$, and the $\ce{SO2}$ concentration in ppm and in
$\text{mg m}^{-3}$ at 273.15 K and $10^{5}$ Pa.
(d) State whether the $\ce{SO2}$ concentration would comply with a
$50\ \text{mg m}^{-3}$ limit before scrubbing.

**E42.** [Ch. 3] A $50.00\ \text{cm}^{3}$ water sample is titrated with
$0.0200\ \text{mol dm}^{-3}$ $\ce{HCl}$. The phenolphthalein endpoint is at
$3.20\ \text{cm}^{3}$ and the methyl orange endpoint is at
$12.80\ \text{cm}^{3}$.

(a) Decide which carbonate species are present, using the relation between the two
titres.
(b) Calculate $[\ce{CO3^{2-}}]$ and $[\ce{HCO3^-}]$ in
$\text{mmol dm}^{-3}$.
(c) Calculate the total alkalinity in $\text{meq dm}^{-3}$ and in
$\text{mg dm}^{-3}$ as $\ce{CaCO3}$.
(d) State the assumption that fails if the sample contains phosphate or silicate.

**E43.** [Ch. 3] Sodium bicarbonate is dissolved in oxygen-free water to give
$C_T = 3.0\ \text{mmol dm}^{-3}$ in a sealed vessel. Take
$K_{a1} = 4.3\times10^{-7}$, $K_{a2} = 4.7\times10^{-11}$ and
$K_H = 3.4\times10^{-2}\ \text{mol dm}^{-3}\ \text{atm}^{-1}$.

(a) Write the charge balance and calculate the pH of the sealed solution.
(b) Calculate the fraction of $C_T$ present as $\ce{CO3^{2-}}$.
(c) The vessel is opened and the solution equilibrates with air at
$420\ \mu\text{atm}$ of $\ce{CO2}$ at constant alkalinity. Calculate the new pH and
$C_T$.
(d) Explain why the pH changes by less than one unit when the system is opened.

**E44.** [Ch. 3] A river receives a discharge with an initial BOD
$L_0 = 30\ \text{mg dm}^{-3}$, deoxygenation coefficient
$k_1 = 0.30\ \text{d}^{-1}$, reaeration coefficient $k_2 = 0.60\ \text{d}^{-1}$ and
an initial deficit $D_0 = 1.0\ \text{mg dm}^{-3}$. Saturated dissolved oxygen at
20 °C is $9.1\ \text{mg dm}^{-3}$.

$$
D = \frac{k_1L_0}{k_2-k_1}\left(e^{-k_1t}-e^{-k_2t}\right) + D_0e^{-k_2t}
$$

(a) Derive or state the time of the critical deficit and calculate it.
(b) Calculate the critical deficit and the minimum dissolved oxygen.
(c) Compare with a $5.0\ \text{mg dm}^{-3}$ criterion and calculate the fractional
reduction in $L_0$ needed to meet it, assuming the critical time is unchanged.
(d) State why the assumption in (c) is an approximation.

**E45.** [Ch. 1] Aspirin is made by acetylating salicylic acid with acetic
anhydride:

$$
\ce{C7H6O3(s) + C4H6O3(l) -> C9H8O4(s) + C2H4O2(l)}
$$

$M(\text{salicylic acid}) = 138.12$,
$M(\text{acetic anhydride}) = 102.09$,
$M(\text{aspirin}) = 180.16$,
$M(\text{acetic acid}) = 60.05\ \text{g mol}^{-1}$.

A batch charges $50.0\ \text{kg}$ of salicylic acid, $40.0\ \text{kg}$ of acetic
anhydride, $250\ \text{kg}$ of water and $150\ \text{kg}$ of ethanol, and isolates
$55.0\ \text{kg}$ of aspirin.

(a) Calculate the atom economy.
(b) Identify the limiting reagent and calculate the theoretical yield and the
percentage yield.
(c) Calculate the E-factor, the process mass intensity and the reaction mass
efficiency over the plant-gate boundary.
(d) State two changes that would lower the E-factor most, and the metric each one
improves.

**E46.** [Ch. 2] A basement room measures $10.0\ \text{m} \times 8.0\ \text{m}
\times 2.4\ \text{m}$. Radon-222 enters at a volumetric source strength of
$5.0\times10^{-3}\ \text{Bq m}^{-3}\ \text{s}^{-1}$; the room is ventilated at
$0.50$ air changes per hour. The half-life of $^{222}\text{Rn}$ is
$3.82\ \text{d}$.

(a) Calculate the decay constant of $^{222}\text{Rn}$ in $\text{s}^{-1}$.
(b) Calculate the steady-state activity concentration.
(c) Recalculate it at $0.25$ air changes per hour.
(d) Calculate the ventilation rate, in air changes per hour, needed to reach
$50\ \text{Bq m}^{-3}$.
(e) Calculate the total mass of radon in the room at the concentration from (b).

**E47.** [Ch. 4] An incinerator flue gas flows at
$1.00\times10^{5}\ \text{m}^{3}\ \text{h}^{-1}$ (dry, at reference conditions) and
contains $800\ \text{mg m}^{-3}$ of $\ce{SO2}$ and $400\ \text{mg m}^{-3}$ of
$\ce{HCl}$. The scrubber uses slaked lime with $20\ \%$ excess.

$$
\ce{Ca(OH)2(s) + SO2(g) -> CaSO3(s) + H2O(l)}
\qquad
\ce{Ca(OH)2(s) + 2HCl(g) -> CaCl2(aq) + 2H2O(l)}
$$

(a) Calculate the mass flow of each acid gas in $\text{kg h}^{-1}$.
(b) Calculate the stoichiometric lime requirement in $\text{kmol h}^{-1}$ and
$\text{kg h}^{-1}$, and the mass with $20\ \%$ excess.
(c) Calculate the mass flow of scrubber residue, including unreacted lime.
(d) Recalculate the residue if all the sulfite is oxidised to sulfate, and explain
why that oxidation matters for disposal.

**E48.** [Ch. 4] A plating rinse of $25\ \text{m}^{3}$ contains
$80\ \text{mg dm}^{-3}$ of $\ce{Cr(VI)}$. It is reduced with iron(II) sulfate
heptahydrate, $M = 278.01\ \text{g mol}^{-1}$, and the chromium is precipitated as
$\ce{Cr(OH)3}$.

$$
\ce{Cr2O7^{2-}(aq) + 6Fe^{2+}(aq) + 14H+(aq) -> 2Cr^{3+}(aq) + 6Fe^{3+}(aq) + 7H2O(l)}
\qquad
\ce{Cr^{3+}(aq) + 3OH^-(aq) -> Cr(OH)3(s)}
$$

(a) Calculate the moles of $\ce{Cr(VI)}$ and the stoichiometric mass of
$\ce{FeSO4.7H2O}$.
(b) Calculate the mass with $15\ \%$ excess.
(c) Calculate the dry mass of $\ce{Cr(OH)3}$ and $\ce{Fe(OH)3}$ sludge, and the
sludge mass per cubic metre.
(d) If the sulfate is precipitated with lime as $\ce{CaSO4}$, calculate the
additional sludge mass and comment on the disposal route.

---

## Part F — Multiple-choice self-check (6 items, 2 marks each)

**F1.** [Ch. 1] Which statement about atom economy is correct?

- A. Atom economy accounts for the yield and for solvent recovery.
- B. Atom economy is fixed by the balanced equation and is independent of yield.
- C. An atom economy of $100\ \%$ guarantees a low E-factor.
- D. Atom economy includes the mass of the catalyst and of the work-up reagents.

**F2.** [Ch. 2] The net reaction of the stratospheric chlorine dimer cycle is

- A. $\ce{O(g) + O3(g) -> 2O2(g)}$
- B. $\ce{2O3(g) -> 3O2(g)}$
- C. $\ce{ClO(g) + O(g) -> Cl(g) + O2(g)}$
- D. $\ce{Cl2O2(g) ->[h\nu] 2Cl(g) + O2(g)}$

**F3.** [Ch. 2] A city centre in summer is strongly VOC-limited. Reducing
$\ce{NO_x}$ emissions alone would most probably

- A. decrease ozone, because $\ce{NO_x}$ is the ozone precursor.
- B. increase ozone, because $\ce{NO_x}$ titration of ozone is reduced.
- C. leave ozone unchanged, because VOC is the limiting reagent.
- D. decrease ozone only if the VOC emission also falls.

**F4.** [Ch. 3] A water has pH 7.0 and a total alkalinity of
$0.50\ \text{meq dm}^{-3}$. Which statement is correct?

- A. It is well buffered, because pH 7 is neutral.
- B. Alkalinity is a measure of calcium and magnesium.
- C. It has a low acid-neutralising capacity despite its neutral pH.
- D. Its hardness must equal its alkalinity.

**F5.** [Ch. 4] De novo synthesis of polychlorinated dibenzo-p-dioxins in an
incinerator is suppressed mainly by

- A. raising the furnace temperature alone to $1200\ ^\circ\text{C}$.
- B. quenching rapidly through $250$–$450\ ^\circ\text{C}$ and removing fly ash.
- C. increasing the chlorine content of the feed.
- D. increasing the excess air above $100\ \%$.

**F6.** [Ch. 3 and Ch. 4] Granular activated carbon used for PFAS removal

- A. mineralises PFAS to fluoride and carbon dioxide.
- B. transfers PFAS to a spent adsorbent that must be destroyed or consigned to a
  secure landfill.
- C. destroys PFAS because the C–F bond breaks at $400\ ^\circ\text{C}$.
- D. is ineffective, so PFAS always pass through to the distribution system.

---

## Marks

| Part | Items | Type | Marks each | Total |
|---|---|---|---|---|
| A — Conceptual | A1–A10 | Short answer | 2 | 20 |
| B — Basic | B11–B20 | Single-step | 3 | 30 |
| C — Intermediate | C21–C32 | Multi-step | 5 | 60 |
| D — Advanced | D33–D40 | Open-ended synthesis | 7 | 56 |
| E — Calculation | E41–E48 | Full calculation | 9 | 72 |
| F — Multiple choice | F1–F6 | Self-check | 2 | 12 |
| **Total** | **54 items** | | | **250** |

**Total marks: 250.**

Solutions: [`../solutions/level-9b-environmental-solutions.md`](../solutions/level-9b-environmental-solutions.md)
