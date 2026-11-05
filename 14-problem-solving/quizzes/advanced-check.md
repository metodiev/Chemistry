# Advanced Check

> **Level 3 · 15 questions · 30 minutes**
> **Covers:** chapters 1–10 of [Level 3 — Advanced Chemistry](../../04-advanced-chemistry/README.md).
> **Use:** at the end of Level 3, or before starting Level 4.

Fifteen questions, several of them multi-step. A calculator is allowed; a data sheet is
not. Where a standard value is needed it is given in the question, so a wrong answer
indicates a conceptual or algebraic error rather than a memorisation gap.

---

**Q1.** Which set of quantum numbers is allowed for an electron in an atom?

- A. $n = 2$, $l = 2$, $m_l = 0$, $m_s = +\tfrac{1}{2}$
- B. $n = 3$, $l = 2$, $m_l = -2$, $m_s = +\tfrac{1}{2}$
- C. $n = 3$, $l = 1$, $m_l = 2$, $m_s = -\tfrac{1}{2}$
- D. $n = 2$, $l = 0$, $m_l = 1$, $m_s = +\tfrac{1}{2}$

<details><summary>Answer</summary>

**B.** The rules are $0 \le l \le n-1$ and $-l \le m_l \le +l$, and option B satisfies both. Option A violates the first rule with $l = n = 2$; option C violates the second with $m_l = 2 > l = 1$; option D also violates the second, since $m_l$ must be zero when $l = 0$.

</details>

---

**Q2.** How many radial nodes does a 3p orbital have?

- A. 0
- B. 1
- C. 2
- D. 3

<details><summary>Answer</summary>

**B.** The radial node count is $n - l - 1 = 3 - 1 - 1 = 1$. Option C uses $n - 1$ and counts angular nodes as well; option A confuses a radial node with a nodal plane through the nucleus, of which a p orbital has one.

</details>

---

**Q3.** Why is the 4s orbital occupied before the 3d orbital in potassium?

- A. The 4s orbital has the lower principal quantum number
- B. The 4s orbital has the lower $n + l$ value and, for potassium, the lower energy
- C. The 3d subshell is already full in argon
- D. The 4s orbital always lies closer to the nucleus than any 3d orbital

<details><summary>Answer</summary>

**B.** The Madelung rule orders by $n + l$ and then by $n$; 4s gives $4 + 0 = 4$ and 3d gives $3 + 2 = 5$, so 4s fills first. Option D is the attractive distractor: 4s penetrates the core and samples the nucleus, but its mean radius is larger than that of 3d, and once the 3d subshell begins to fill its energy drops below 4s — which is why transition metals lose 4s electrons first when they ionise.

</details>

---

**Q4.** According to molecular-orbital theory, what is the bond order of $\ce{O2}$?

- A. 1
- B. 2
- C. 3
- D. 2.5

<details><summary>Answer</summary>

**B.** The valence configuration is $\sigma_{2s}^2\sigma_{2s}^{*2}\sigma_{2p}^2\pi_{2p}^4\pi_{2p}^{*2}$, so there are eight bonding and four antibonding electrons and the bond order is $(8-4)/2 = 2$. Option C is the bond order of $\ce{N2}$, where the $\pi$ orbitals are lower in energy and the $\pi^*$ orbitals are empty.

</details>

---

**Q5.** Why is molecular oxygen paramagnetic?

- A. It has two unpaired electrons in the $\pi^*$ orbitals
- B. It has a double bond, and double bonds are paramagnetic
- C. It contains two unpaired protons in the nucleus
- D. Its bond order is 2, which requires unpaired electrons

<details><summary>Answer</summary>

**A.** The two $\pi^*$ electrons occupy degenerate orbitals singly, with parallel spins, so the molecule has a net magnetic moment. Option D is the common non sequitur: bond order counts net bonding electrons and says nothing about whether the remaining electrons are paired, so a bond order of 2 is no evidence either way.

</details>

---

**Q6.** A reaction has $\Delta H = +25\ \mathrm{kJ\ mol^{-1}}$ and $\Delta S = +100\ \mathrm{J\ K^{-1}\ mol^{-1}}$. Above what temperature does it become spontaneous?

- A. About 250 K
- B. About 4 K
- C. About 2500 K
- D. It is spontaneous at every temperature

<details><summary>Answer</summary>

**A.** Setting $\Delta G = 0$ gives $T = \Delta H/\Delta S = 25\,000/100 = 250$ K. Option B is the classic units error — dividing 25 by 100 without converting kilojoules to joules — and option D ignores the positive enthalpy term, which dominates below 250 K.

</details>

---

**Q7.** Which of these reactions has a positive entropy change?

- A. $\ce{N2(g) + 3H2(g) -> 2NH3(g)}$
- B. $\ce{2NH3(g) -> N2(g) + 3H2(g)}$
- C. $\ce{H2O(g) -> H2O(l)}$
- D. $\ce{CaO(s) + CO2(g) -> CaCO3(s)}$

<details><summary>Answer</summary>

**B.** Four moles of gas are produced from two, so the number of accessible microstates increases and $\Delta S > 0$. Options A and D reduce the gas mole count and option C condenses a gas to a liquid, so all three have $\Delta S < 0$.

</details>

---

**Q8.** For sodium chloride: $\Delta H_f^\circ = -411$, sublimation of Na $= +107$, ionisation energy of Na $= +496$, half the Cl–Cl bond enthalpy $= +122$, electron affinity of Cl $= -349$ (all in $\mathrm{kJ\ mol^{-1}}$). What is the lattice enthalpy for forming the solid from gaseous ions?

- A. $-787\ \mathrm{kJ\ mol^{-1}}$
- B. $+787\ \mathrm{kJ\ mol^{-1}}$
- C. $-1185\ \mathrm{kJ\ mol^{-1}}$
- D. $-37\ \mathrm{kJ\ mol^{-1}}$

<details><summary>Answer</summary>

**A.** The cycle gives $-411 = 107 + 496 + 122 - 349 + \Delta H_{\text{latt}}$, so $\Delta H_{\text{latt}} = -787\ \mathrm{kJ\ mol^{-1}}$. Option B has the right magnitude with the opposite sign, which would describe the reverse process of separating the lattice into gaseous ions. Option D forgets the lattice term altogether.

</details>

---

**Q9.** A mechanism is: $\ce{A + B <=> C}$ rapidly, then $\ce{C -> D}$ slowly. What is the rate law?

- A. $\text{rate} = k[\ce{A}][\ce{B}]$
- B. $\text{rate} = k[\ce{C}]$
- C. $\text{rate} = k[\ce{A}]^2[\ce{B}]$
- D. $\text{rate} = k[\ce{A}][\ce{B}]^2$

<details><summary>Answer</summary>

**A.** The slow step gives $\text{rate} = k_2[\ce{C}]$, and the fast pre-equilibrium gives $[\ce{C}] = K[\ce{A}][\ce{B}]$, so the observed rate is $k_2K[\ce{A}][\ce{B}]$. Option B is the attractive distractor: it is correct as an expression in the intermediate, but an intermediate concentration cannot appear in an experimental rate law because it is not a reactant you can control.

</details>

---

**Q10.** According to the Arrhenius equation, why does the rate constant increase with temperature?

- A. A larger fraction of collisions has energy above the activation energy
- B. The activation energy decreases as the temperature rises
- C. The pre-exponential factor decreases, which increases the rate
- D. The rate constant is independent of temperature for an elementary step

<details><summary>Answer</summary>

**A.** The exponential factor $e^{-E_a/RT}$ increases with $T$ because the Boltzmann distribution shifts towards higher energies. Option B is the common misconception: $E_a$ is a property of the reaction pathway and is essentially constant over ordinary temperature ranges, even though the *proportion* of successful collisions changes dramatically.

</details>

---

**Q11.** In heterogeneous catalysis, where does the reaction take place?

- A. On the surface of the catalyst, after adsorption of the reactants
- B. In the gas phase, with the catalyst unchanged and uninvolved
- C. Only in solution, because surfaces are inert
- D. Inside the bulk of the catalyst, which is consumed

<details><summary>Answer</summary>

**A.** The catalytic cycle involves adsorption, surface reaction and desorption, and the available surface area controls the rate. Option D confuses a catalyst with a reagent: the catalyst is not consumed, although it can be poisoned or sintered.

</details>

---

**Q12.** A buffer contains equal concentrations of ethanoic acid ($\mathrm{p}K_a = 4.76$) and sodium ethanoate. What is its pH?

- A. 4.76
- B. 7.00
- C. 9.24
- D. 2.38

<details><summary>Answer</summary>

**A.** When $[\ce{HA}] = [\ce{A-}]$, the Henderson–Hasselbalch equation gives $\mathrm{pH} = \mathrm{p}K_a + \log 1 = 4.76$. Option C computes $14 - \mathrm{p}K_a$, which would be the pH of an equally concentrated solution of the conjugate base alone, not of the buffer.

</details>

---

**Q13.** Solid sodium chloride is added to a saturated solution of silver chloride. What happens?

- A. The solubility of $\ce{AgCl}$ decreases because of the common ion effect
- B. The solubility of $\ce{AgCl}$ increases
- C. Nothing changes, because $\ce{AgCl}$ is already saturated
- D. The solubility product of $\ce{AgCl}$ increases

<details><summary>Answer</summary>

**A.** The added chloride raises $[\ce{Cl-}]$, so the ion product exceeds $K_{sp}$ and $\ce{AgCl}$ precipitates until the product is restored; the net effect is lower silver ion concentration. Option D is the standard misconception: $K_{sp}$ depends only on temperature, and it is the *ion product* that is displaced.

</details>

---

**Q14.** A cell has $E^\circ = +1.10$ V and $n = 2$. At 298 K, what happens to the cell potential when the reaction quotient rises from 1 to 100?

- A. It falls by about 0.059 V
- B. It rises by about 0.059 V
- C. It is unchanged, because $E^\circ$ is a constant
- D. It falls to zero

<details><summary>Answer</summary>

**A.** The Nernst equation gives $E = E^\circ - (0.0592/2)\log Q$; with $\log Q = 2$ the correction is $0.0592 \times 2/2 = 0.059$ V, and it is subtracted. Option B reverses the sign: a larger quotient means more product, which opposes the forward reaction and lowers the potential.

</details>

---

**Q15.** The complex $\ce{[Fe(CN)6]^{4-}}$ is diamagnetic, whereas $\ce{[Fe(H2O)6]^{2+}}$ has four unpaired electrons. Both contain iron(II). What explains the difference?

- A. Cyanide is a strong-field ligand, so the larger splitting gives a low-spin $\mathrm{d^6}$ configuration
- B. Water is a strong-field ligand and forces pairing
- C. The cyanide complex contains iron(III), which is always diamagnetic
- D. Cyanide reduces iron to the metal, which is diamagnetic

<details><summary>Answer</summary>

**A.** Both complexes are $\mathrm{d^6}$ iron(II). Cyanide produces a splitting large enough to overcome the pairing energy, so all six electrons occupy the $\mathrm{t_{2g}}$ set and the complex is diamagnetic; water is a weaker-field ligand and the high-spin arrangement leaves four unpaired electrons. Option C is wrong on the oxidation state: six cyanide ligands at $-1$ require $\ce{Fe^2+}$ for a $4-$ overall charge.

</details>

---

## Scoring

| Score | Meaning | Action | Equivalent |
|---|---|---|---|
| 14–15 / 15 | Secure | Move on to [Level 4](../../05-organic-chemistry/README.md); revisit in a month | 18–20 / 20 |
| 11–13 | Mostly secure with holes | Reread the Level 3 chapters behind the missed items | 15–17 / 20 |
| 8–10 | Fragile | Rework the Level 3 exercise bank | 11–14 / 20 |
| ≤ 7 | Not yet learned | Restart Level 3 with the study routine in the [learning path](../../00-learning-guide/learning-path.md) | ≤ 10 / 20 |

The bands mirror [section 3 of the quiz index](README.md), scaled from twenty items to
fifteen. The equivalent column is given so that a score on this quiz can be compared with
the other checks without rescaling in your head.
