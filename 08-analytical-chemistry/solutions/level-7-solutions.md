# Level 7 — Worked Solutions: Analytical Chemistry

> **Level:** Undergraduate and practising analyst (Level 7 — Analytical Chemistry)
> **Items:** 50
> **Exercise bank:** [`../exercises/level-7-exercises.md`](../exercises/level-7-exercises.md)

Each solution gives the **Strategy**, the **Working**, the **Answer** and a
**Check**. Items marked **multi-step** need at least three dependent operations.
Statistical decisions state the null hypothesis, the statistic, the degrees of freedom
and the critical value before the conclusion. Concentrations are quoted in the unit of
the item; no silent conversion between $\text{mg L}^{-1}$ and $\text{mol L}^{-1}$ is
made without showing the molar mass.

---

## Part A — Conceptual questions

### 1. Figures of merit and fitness for purpose

**Strategy.** Define each term by its equation, then distinguish the two detection-limit
conventions and finish with the operational meaning of fitness for purpose.

**Working.** **Sensitivity** is the slope of the calibration, $b = \partial y/\partial x$.
**Analytical sensitivity** is $\gamma = b/s_y$, the slope divided by the response
standard deviation: it is the change in response measured in units of noise.
**Selectivity** is the ability to produce a response for the analyte in the presence of
interferents, quantified by $k_{\text{sel}} = (\partial y/\partial c)_{\text{int}}/
(\partial y/\partial c)_{\text{analyte}}$; a value much below one indicates good
discrimination. The **limit of detection** is the concentration giving a signal
distinguishable from the blank at a stated error rate, commonly
$\text{LOD} = 3.3s_{y/x}/b$. The **limit of quantification** is the lowest
concentration that can be measured with acceptable precision,
$\text{LOQ} = 10s_{y/x}/b$. The **dynamic range** is the interval between LOQ and the
upper limit of linear response.

The factor $3.3$ in the LOD comes from the $t$ statistic at $\alpha = \beta = 0.05$: it
corresponds to a $5\ \%$ risk of a false positive and a $5\ \%$ risk of a false
negative, not to three times the standard deviation of one blank reading. Using a single blank
gives an estimate of the blank noise with very few degrees of freedom; the regression
residual $s_{y/x}$ pools the noise over all calibration points, and $3.3$ corresponds
to the one-sided 95 % probability of a false positive and a false negative
simultaneously. Multiplying a single blank standard deviation by 3 ignores both the
uncertainty of that estimate and the intercept uncertainty.

Fitness for purpose means that the method's uncertainty, detection limit and
selectivity are adequate for the decision the result will support. A method can have
excellent sensitivity and still be unfit if its LOQ exceeds the regulatory limit or if
its bias is larger than the decision threshold.

**Answer.** The definitions above; LOD uses $3.3s_{y/x}/b$ because the residual pools
all calibration noise and the multiplier fixes both error rates at 5 %; fitness for
purpose is adequacy relative to the decision, not excellence in the abstract.

**Check.** A method with $b = 0.045$, $s_{y/x} = 0.0021$ has
$\text{LOD} = 0.15\ \text{mg L}^{-1}$ and $\gamma = 21\ \text{L mg}^{-1}$; a method
with twice the slope and the same noise has half the LOD.

**Where marks are lost.** Defining sensitivity as the detection limit, or quoting
$3\sigma$ without saying whether $\sigma$ is the blank or the regression residual.

### 2. Sampling variance and the theory of sampling

**Strategy.** Separate the two variance components, then state the three variables in
Gy's fundamental error and the difference between compositing and replicating.

**Working.** The variance of a reported mean is

$$
\sigma_{\text{total}}^2 = \frac{\sigma_{\text{sampling}}^2}{n}
+ \sigma_{\text{analysis}}^2 .
$$

In trace analysis $\sigma_{\text{sampling}}$ is frequently several times
$\sigma_{\text{analysis}}$ because the analyte is heterogeneously distributed, so
increasing the number of increments reduces the total variance far more effectively
than improving the instrument. This is the central claim of the theory of sampling.

Gy's fundamental error is, in the simplified form used here,

$$
\sigma_{\text{FE}}^2 \approx \frac{K d^3}{M_s},
$$

so the three controlling variables are the material constant $K$ (density, shape and
composition variance), the nominal top particle size $d$, and the sample mass $M_s$.
The error falls with the cube of the particle size and inversely with mass; grinding is
therefore more powerful than adding increments when the material is coarse.

A **composite** sample combines many increments into one portion that is then
subsampled and analysed. It estimates the mean of the population but provides no
independent estimate of the sampling variance, because the increments are no longer
separate measurements. **Replicate** samples are analysed separately, so the
between-increment variance can be estimated directly: with $n$ replicates the sampling
variance of the mean is $s_{\text{sampling}}^2/n$. A composite analysed once confounds
sampling and analytical error and cannot separate them.

**Answer.** Sampling variance usually dominates; the controls are $K$, $d$ and $M_s$;
a composite estimates the mean but not the sampling variance, whereas replicates
estimate both.

**Check.** For a coarse ore with $d = 20\ \text{mm}$ and $M_s = 0.5\ \text{kg}$, the
fundamental error is a few tenths of a per cent; halving $d$ reduces it by a factor of
$2\sqrt{2} \approx 2.8$.

**Where marks are lost.** Claiming that a larger composite eliminates sampling error,
or quoting $d^2$ instead of $d^3$.

### 3. Random, systematic and gross error

**Strategy.** Define each error by its origin and its statistical signature, then map
each to the procedure that detects it.

**Working.** **Random error** arises from uncontrollable, independent fluctuations and
scatters results about their mean; it is described by the standard deviation and is
reduced by replication. **Systematic error** (bias) shifts every result in the same
direction; it is not reduced by replication and is detected by comparison with a
certified reference material, by a spike-recovery experiment, or by an independent
method. **Gross error** is a blunder such as a transcription mistake, a mis-set
pipette or a lost sample; it produces an outlier and is detected by outlier tests and
by inspection of the raw data.

**Accuracy** is the closeness of a result to the true value and contains both random
and systematic components. **Trueness** is the closeness of the mean to the true value,
so it is the systematic component alone. **Precision** is the closeness of replicates to
one another, the random component alone.

High precision with unacceptable trueness occurs when a pipette is consistently
mis-calibrated: the replicates agree to $0.1\ \%$ but every result is $2\ \%$ low.
Replication cannot reveal this; only a reference material or a gravimetric check can.

**Answer.** Random error is treated by replication and confidence intervals; systematic
error by reference materials, recovery and method comparison; gross error by outlier
tests. Accuracy includes both; trueness is the systematic part; precision the random
part.

**Check.** A method with a mean recovery of $92\ \%$ and $s = 4\ \%$ is precise but
biased; the confidence interval excludes $100\ \%$ even though the replicates agree.

**Where marks are lost.** Saying that replication improves accuracy, or using
"accuracy" and "precision" interchangeably.

### 4. Calibration strategies

**Strategy.** For each strategy, state the model and the assumption it relaxes.

**Working.** **External calibration** measures standards prepared in a simple solvent
and applies $y = a + bx$ to the sample. It corrects for instrument response and is
valid only when the sample matrix does not change the response.

**Internal-standard calibration** adds a fixed amount of a chemically similar species
to every standard and sample and uses the ratio $A_{\text{a}}/A_{\text{IS}} = F
C_{\text{a}}/C_{\text{IS}}$. It corrects for variations in injected volume, dilution
and instrument drift between runs, but it does not correct for a matrix effect that
changes the analyte response relative to the internal standard, and it fails if the
internal standard is present in the sample.

**Matrix-matched calibration** prepares standards in a matrix as close as possible to
the sample. It corrects for matrix effects, provided the matrix can be reproduced; it
cannot correct for an unknown or variable matrix.

**Standard addition** adds known amounts of analyte to portions of the sample and
extrapolates to zero response. It corrects for multiplicative matrix effects and for
recovery losses that affect native and added analyte equally. It does not correct for a
blank that differs between sample and standard, and it assumes that the added analyte
equilibrates with the native analyte.

**Answer.** External: instrument response only. Internal standard: volume and drift.
Matrix-matched: a reproducible matrix. Standard addition: multiplicative matrix effects
and proportional recovery.

**Check.** A sample with a $30\ \%$ suppression of slope but a linear response is
handled by standard addition; a sample with a constant positive intercept from the
matrix is not, because the blank differs.

**Where marks are lost.** Claiming that standard addition corrects a blank, or that an
internal standard corrects the matrix effect on the analyte.

### 5. The gravimetric factor

**Strategy.** Define the factor from the stoichiometry, then justify the requirements
of the weighing form and the preference for a large factor.

**Working.** For a weighing form containing $b$ formula units of analyte per formula
unit of precipitate,

$$
GF = \frac{a\,M_r(\text{analyte})}{b\,M_r(\text{weighing form})},
\qquad
w(\text{analyte}) = \frac{m_{\text{weighing form}}\,GF}{m_{\text{sample}}} .
$$

The coefficients $a$ and $b$ convert moles of weighing form to moles of analyte; for
example, in the determination of iron as $\ce{Fe2O3}$, two iron atoms occur in each
formula unit, so $a = 2$ and $b = 1$.

A weighing form must be pure, stoichiometric, insoluble under the precipitation and
washing conditions, easily filtered, and stable to drying or ignition so that its
composition is exactly known. It should also have a large molar mass relative to the
analyte.

A large $GF$ is preferred because the relative uncertainty of the mass fraction is
dominated by the relative uncertainty of the weighing:
$u(w)/w \approx u(m_{\text{product}})/m_{\text{product}}$. A larger factor means a
larger mass of product for the same amount of analyte, so a given absolute weighing
error corresponds to a smaller relative error on the analyte.

**Answer.** $GF = aM_r(\text{analyte})/bM_r(\text{weighing form})$; the weighing form
must be pure, stoichiometric, insoluble and of known composition; a large factor
improves the relative precision.

**Check.** For iron weighed as $\ce{Fe2O3}$, $GF = 2(55.845)/159.688 = 0.6994$; for
iron weighed as $\ce{FeO}$, $GF = 55.845/71.844 = 0.7773$, a larger factor and
therefore a slightly better relative precision for the same sample mass.

**Where marks are lost.** Inverting the factor, or forgetting the stoichiometric
coefficient 2 for iron in $\ce{Fe2O3}$.

### 6. Chromatographic detectors

**Strategy.** Classify each detector by universality, destructiveness and measurement
principle.

**Working.** The **flame ionisation detector (FID)** burns the eluate in a hydrogen
flame and measures the ion current from carbon-containing fragments. It is selective for
organic compounds, destructive, and almost blind to water, $\ce{CO2}$ and permanent
gases; its response is roughly proportional to the number of carbon atoms.

The **thermal conductivity detector (TCD)** measures the change in thermal conductivity
of the carrier gas caused by the analyte. It is universal, non-destructive and
concentration-sensitive, but its detection limit is far higher than that of the FID.

The **electron-capture detector (ECD)** measures the capture of thermal electrons by
electronegative analytes. It is highly selective for halogenated and nitro compounds
and extremely sensitive for them; because the analyte is not consumed, it is classed as
non-destructive, although the sample is usually not recovered.

In liquid chromatography, the **UV–visible absorbance detector** measures absorption by
chromophores. It is selective for absorbing species, non-destructive, and its
sensitivity depends on the molar absorptivity at the chosen wavelength. The **mass
spectrometer** ionises the eluate and separates ions by $m/z$; it is universal in the
sense that almost any ionisable molecule can be detected, destructive, and structurally
informative, which is why it is the preferred detector for confirmation and for
identity-based regulation.

**Answer.** FID: selective for organics, destructive. TCD: universal, non-destructive.
ECD: selective for electronegative analytes, sensitive, non-destructive. UV–visible:
selective for chromophores, non-destructive. MS: near-universal, destructive, confirmatory.

**Check.** A trace analysis of a halogenated pesticide in water would use GC–ECD or
GC–MS; a purity assay of a hydrocarbon stream would use GC–FID; a non-destructive
confirmation of a gas mixture would use GC–TCD.

**Where marks are lost.** Calling the FID universal, or claiming the UV detector is
destructive.

### 7. The van Deemter equation

**Strategy.** Identify the physical origin of each term, then explain the optimum and
the capillary case.

**Working.**

$$
H = A + \frac{B}{u} + Cu, \qquad
u_{\text{opt}} = \sqrt{\frac{B}{C}}, \qquad
H_{\min} = A + 2\sqrt{BC}.
$$

$A$ is eddy diffusion: molecules follow paths of different lengths through a packed bed,
so they spread. It is proportional to particle diameter and vanishes in an open
capillary. $B/u$ is longitudinal diffusion: the analyte diffuses along the column in the
direction of the concentration gradient, and the effect is larger at low velocity. $Cu$
is mass transfer resistance: the analyte takes finite time to equilibrate between the
mobile and stationary phases, and the effect grows with velocity.

Reducing the particle size lowers $A$ and shortens the diffusion path in the stationary
phase, which lowers $C$; both reduce $H$ and increase the plate number, at the cost of a
higher pressure drop. An optimum velocity exists because $B/u$ dominates at low $u$ and
$Cu$ at high $u$; differentiating gives $u_{\text{opt}} = (B/C)^{1/2}$.

In capillary GC there is no packed bed, so $A = 0$ and the Golay equation applies; $B$
and $C$ are smaller, and the optimum velocity is higher, which is why capillary columns
give much larger plate numbers per metre.

**Answer.** $A$ eddy diffusion, $B/u$ longitudinal diffusion, $Cu$ mass transfer;
$u_{\text{opt}} = (B/C)^{1/2}$; smaller particles reduce $A$ and $C$; capillary columns
have $A = 0$.

**Check.** With $A = 0.50\ \text{mm}$, $B = 0.60\ \text{mm cm s}^{-1}$ and
$C = 0.040\ \text{mm s cm}^{-1}$, $u_{\text{opt}} = 3.9\ \text{cm s}^{-1}$ and
$H_{\min} = 0.81\ \text{mm}$.

**Where marks are lost.** Assigning longitudinal diffusion to $A$, or claiming that
$H$ always falls as velocity increases.

### 8. Ion-selective electrodes and selectivity

**Strategy.** Write the Nikolsky–Eisenman equation, interpret the selectivity
coefficient, and explain the activity response.

**Working.**

$$
E = K + \frac{2.303RT}{z_iF}
\log_{10}\left(a_i + \sum_j K_{ij}^{\text{pot}}a_j^{z_i/z_j}\right).
$$

The coefficient $K_{ij}^{\text{pot}}$ measures the response of the electrode to ion $j$
relative to the primary ion $i$. If $K_{ij}^{\text{pot}} \ll 1$, the electrode is much
more selective for $i$; if it is of order one, $j$ interferes at comparable activity.
The interferent can be neglected when
$K_{ij}^{\text{pot}}a_j^{z_i/z_j} \ll a_i$, for example when its activity is below the
detection limit of the electrode for that ion.

The electrode responds to activity, not concentration, because the potential is fixed by
the electrochemical potential of the ion at the membrane–solution interface, which
contains $RT\ln a_i$. In dilute solution the activity coefficient is close to one and
concentration can be substituted, but in a sample of high ionic strength the activity
coefficient differs from one and a calibration in concentration is biased. Adding an
ionic-strength adjuster to both standards and samples is the standard remedy.

**Answer.** The equation above; $K_{ij}^{\text{pot}}$ is the relative response to the
interferent; interference is negligible when its weighted activity is much smaller than
$a_i$; the electrode measures activity because the potential depends on $\mu_i$.

**Check.** A fluoride electrode with $K_{\ce{F-,OH-}}^{\text{pot}} \approx 0.1$ tolerates
hydroxide only at activities below about one tenth of the fluoride activity, which is
why acidic buffers are used.

**Where marks are lost.** Treating $K_{ij}^{\text{pot}}$ as a concentration ratio
without the charge weighting, or calibrating in concentration at high ionic strength.

---

## Part B — Derivations

### 9. Propagation of uncertainty from a Taylor expansion

**Strategy.** Expand the function about the mean values to first order and take
variances.

**Working.** Let $y = f(x_1,\dots,x_n)$ and let each $x_i$ have mean $\bar x_i$ and
standard uncertainty $u(x_i)$. A first-order Taylor expansion about the means gives

$$
y - \bar y \approx \sum_i \left(\frac{\partial f}{\partial x_i}\right) (x_i - \bar x_i).
$$

Taking the variance of both sides, and using
$\operatorname{var}(x_i) = u^2(x_i)$,

$$
u^2(y) = \sum_i \left(\frac{\partial f}{\partial x_i}\right)^2 u^2(x_i)
+ 2\sum_{i<j}\left(\frac{\partial f}{\partial x_i}\right)
\left(\frac{\partial f}{\partial x_j}\right)\operatorname{cov}(x_i,x_j).
$$

For independent inputs the covariance terms vanish. For $y = a \pm b - c$ the
derivatives are $\pm 1$, so

$$
u^2(y) = u^2(a) + u^2(b) + u^2(c),
$$

independent of the signs: uncertainties always add in quadrature. For
$y = ab/c$,

$$
\frac{\partial y}{\partial a} = \frac{b}{c},\qquad
\frac{\partial y}{\partial b} = \frac{a}{c},\qquad
\frac{\partial y}{\partial c} = -\frac{ab}{c^2},
$$

so dividing $u^2(y)$ by $y^2 = a^2b^2/c^2$ gives

$$
\left(\frac{u(y)}{y}\right)^2
= \left(\frac{u(a)}{a}\right)^2
+ \left(\frac{u(b)}{b}\right)^2
+ \left(\frac{u(c)}{c}\right)^2 .
$$

The rules fail when the relative uncertainties are not small (the linear term no longer
dominates), when the inputs are correlated (the covariance terms are not zero), and
when the function is strongly non-linear over the uncertainty interval. They also fail
for a quantity that can approach zero, because the relative form diverges.

**Answer.** $u^2(y) = \sum_i(\partial f/\partial x_i)^2u^2(x_i)$ for independent inputs;
sums add variances, products add relative variances. The rules require small,
independent uncertainties and approximate linearity.

**Check.** For $y = a - b$ with $a = 10.0 \pm 0.1$ and $b = 9.0 \pm 0.1$, the absolute
uncertainty is $0.14$, which is large relative to $y = 1.0$; the relative form would
give $14\ \%$, correctly signalling that the subtraction is ill-conditioned.

**Where marks are lost.** Subtracting uncertainties in a difference, or adding relative
uncertainties linearly instead of in quadrature.

### 10. Confidence intervals and the $t$ distribution

**Strategy.** Define the $t$ statistic and invert the probability statement.

**Working.** For $n$ independent observations from a normal population with mean $\mu$,
the sample mean is distributed as
$\bar x \sim N(\mu,\sigma^2/n)$. If $\sigma$ were known, the standardised variable
$z = (\bar x - \mu)/(\sigma/\sqrt n)$ would be standard normal. In practice $\sigma$ is
estimated by $s$, and the ratio

$$
t = \frac{\bar x - \mu}{s/\sqrt n}
$$

follows Student's $t$ distribution with $\nu = n - 1$ degrees of freedom. The heavier
tails of the $t$ distribution account for the extra uncertainty in $s$; as $n$ grows,
$s \to \sigma$ and $t$ tends to $z$.

For a two-sided interval with confidence $1 - \alpha$,

$$
P\left(-t_{\alpha/2,\nu} \le \frac{\bar x - \mu}{s/\sqrt n}
\le t_{\alpha/2,\nu}\right) = 1 - \alpha .
$$

Rearranging the inequality for $\mu$ gives

$$
\bar x - t_{\alpha/2,\nu}\frac{s}{\sqrt n}
\le \mu \le
\bar x + t_{\alpha/2,\nu}\frac{s}{\sqrt n},
$$

which is the quoted interval. The quantity $s/\sqrt n$ is the standard error of the
mean; the interval width therefore falls as $\sqrt n$, so quadrupling the number of
replicates halves the interval.

**Answer.** $\bar x \pm t_{\alpha/2,n-1}s/\sqrt n$, with $n - 1$ degrees of freedom.

**Check.** For $n = 6$, $s = 0.0653$ and $\bar x = 12.467$, the $95\ \%$ interval is
$12.467 \pm 2.571(0.0653/\sqrt 6) = 12.467 \pm 0.069$, consistent with the direct
calculation.

**Where marks are lost.** Using $z = 1.96$ for small $n$, or quoting $n$ rather than
$n - 1$ degrees of freedom.

### 11. Least-squares slope and intercept

**Strategy.** Write the residual sum of squares, differentiate with respect to both
parameters, and solve the two normal equations.

**Working.** For the model $y_i = a + bx_i + \varepsilon_i$, minimise

$$
SS_{\text{res}} = \sum_{i=1}^{n}\left(y_i - a - bx_i\right)^2 .
$$

Setting the partial derivatives to zero,

$$
\frac{\partial SS}{\partial a} = -2\sum_i (y_i - a - bx_i) = 0
\quad\Longrightarrow\quad
na + b\sum_i x_i = \sum_i y_i,
$$

$$
\frac{\partial SS}{\partial b} = -2\sum_i x_i(y_i - a - bx_i) = 0
\quad\Longrightarrow\quad
a\sum_i x_i + b\sum_i x_i^2 = \sum_i x_i y_i .
$$

Solving the pair,

$$
b = \frac{n\sum x_iy_i - \sum x_i\sum y_i}
{n\sum x_i^2 - \left(\sum x_i\right)^2},
\qquad
a = \bar y - b\bar x .
$$

The estimates are unbiased when the model is linear, the errors are independent and
have zero mean, and the $x_i$ are known exactly. Their standard errors,
$s_b = s_{y/x}/[\sum(x_i-\bar x)^2]^{1/2}$ and
$s_{y/x} = [\sum(y_i-\hat y_i)^2/(n-2)]^{1/2}$, are valid when in addition the errors
have constant variance and are normally distributed. Weighted regression is required
when the variance depends on $x$.

**Answer.** The normal equations above, giving $b$ and $a = \bar y - b\bar x$.

**Check.** For the data of item 31, the unweighted fit gives $b = 2.10$ and
$a = -0.067$; the fitted line passes through $(\bar x,\bar y) = (2.00, 4.13)$, as any
least-squares line must.

**Where marks are lost.** Forgetting that the line passes through $(\bar x,\bar y)$, or
using $n$ instead of $n - 2$ in $s_{y/x}$.

### 12. The standard-addition equation

**Strategy.** Write the response before and after the spike with the same response
factor, then eliminate the factor.

**Working.** Let the sample volume be $V_x$, the native concentration $C_x$, the spike
concentration $C_s$ and spike volume $V_s$. For a linear response with a constant blank
and the same response factor $k$ for native and added analyte,

$$
A_1 = kC_x,
\qquad
A_2 = k\frac{C_xV_x + C_sV_s}{V_x + V_s}.
$$

Eliminating $k = A_1/C_x$ from the second equation,

$$
A_2(V_x + V_s) = \frac{A_1}{C_x}\left(C_xV_x + C_sV_s\right)
= A_1V_x + \frac{A_1C_sV_s}{C_x}.
$$

Solving for $C_x$,

$$
C_x = \frac{A_1C_sV_s}{A_2(V_x+V_s) - A_1V_x}.
$$

The assumptions are: linear response over the native-plus-added range; identical
response factors for native and added analyte; complete equilibration of the spike;
and a blank that is the same in both measurements. The last condition is why a
matrix blank cannot be corrected by standard addition alone.

**Answer.** The equation quoted, with the four assumptions.

**Check.** With $A_1 = 0.326$, $A_2 = 0.512$, $V_x = 25.00\ \text{mL}$,
$V_s = 2.00\ \text{mL}$ and $C_s = 10.0\ \text{mg L}^{-1}$,
$C_x = 6.52/(13.824 - 8.150) = 1.15\ \text{mg L}^{-1}$, a plausible trace level.

**Where marks are lost.** Using $V_x$ rather than $V_x + V_s$ in the denominator of
$A_2$, which ignores the dilution by the spike.

### 13. The resolution equation

**Strategy.** Express the retention-time difference and the peak width in terms of
$k$, $\alpha$ and $N$, then simplify for similar $k$.

**Working.** For two Gaussian peaks of similar width,

$$
R_s = \frac{2(t_{R,2}-t_{R,1})}{w_1+w_2}
\approx \frac{t_{R,2}-t_{R,1}}{\bar w},
\qquad
\bar w \approx 4\bar\sigma,
$$

using $w = 4\sigma$ for a Gaussian peak. The plate number is
$N = (t_R/\sigma)^2$, so $\sigma \approx t_R/\sqrt N$ and therefore
$\bar w \approx 4t_{R,2}/\sqrt N$ for peaks of similar retention.

The retention factor is $k = (t_R - t_M)/t_M$, so $t_R = t_M(1+k)$, and

$$
t_{R,2} - t_{R,1} = t_M(k_2 - k_1) = t_Mk_1(\alpha - 1),
$$

with $\alpha = k_2/k_1$. For similar $k$, write $k_1 \approx k_2 \approx k$ and
$t_{R,2} \approx t_M(1+k)$. Then

$$
R_s \approx \frac{t_Mk(\alpha-1)}{4t_M(1+k)/\sqrt N}
= \frac{\sqrt N}{4}(\alpha-1)\frac{k}{1+k}.
$$

The approximations are: Gaussian peaks of equal width, $k_1 \approx k_2$ (a good
selectivity with a small change in $k$), and $N$ the same for both peaks. The equation
shows that resolution can be improved by increasing $N$ (a longer or more efficient
column), by increasing $\alpha$ (a different stationary phase or temperature), or by
increasing $k$ (a weaker eluent), but the $k/(1+k)$ factor saturates as $k$ grows.

**Answer.** The derived equation and its three approximations.

**Check.** For $\alpha = 1.10$, $k = 4.0$ and $R_s = 1.5$, the equation gives
$N = 16(1.5)^2[5/(0.10\times4)]^2 = 5625$, a realistic plate count for a $150\ \text{mm}$
column.

**Where marks are lost.** Using $w_{1/2}$ in the definition without the factor
$1.18$, or omitting the $k/(1+k)$ term and overestimating the effect of selectivity.

### 14. The weak-acid titration curve

**Strategy.** Use the buffer equation in the buffer region and the conjugate-base
hydrolysis at equivalence.

**Working.** For a weak monoprotic acid $\ce{HA}$ of concentration $C_a$ and volume
$V_a$ titrated with strong base of concentration $C_b$, the charge balance is

$$
[\ce{H+}] + [\ce{B+}] = [\ce{OH-}] + [\ce{A-}],
$$

with $[\ce{B+}] = C_bV_b/(V_a+V_b)$. In the buffer region the amounts are
$n_{\ce{HA}} = C_aV_a - C_bV_b$ and $n_{\ce{A-}} = C_bV_b$, so

$$
\mathrm{pH} = \mathrm{p}K_a + \log_{10}
\frac{C_bV_b}{C_aV_a - C_bV_b}.
$$

At **half equivalence**, $C_bV_b = \tfrac{1}{2}C_aV_a$, so
$[\ce{A-}] = [\ce{HA}]$ and $\mathrm{pH} = \mathrm{p}K_a$.

At **equivalence**, all the acid has been converted to $\ce{A-}$ with concentration
$C_{\text{eq}} = C_aV_a/(V_a+V_{\text{eq}})$. The conjugate base hydrolyses with
$K_b = K_w/K_a$, and for $K_bC_{\text{eq}} \gg K_w$ and small hydrolysis,

$$
[\ce{OH-}] \approx \sqrt{K_bC_{\text{eq}}},
\qquad
\mathrm{pOH} = \tfrac{1}{2}\left(\mathrm{p}K_b - \log C_{\text{eq}}\right),
$$

$$
\mathrm{pH} = \mathrm{p}K_w - \mathrm{pOH}
= \tfrac{1}{2}\left(\mathrm{p}K_w + \mathrm{p}K_a + \log C_{\text{eq}}\right).
$$

The approximations are: activities replaced by concentrations; water autoionisation
neglected; the acid dissociation small compared with $C_a$; and, at equivalence, the
hydrolysis small compared with $C_b$. The buffer equation fails within about one pH
unit of equivalence, where the amount of free acid is no longer negligible against
$[\ce{H+}]$; the hydrolysis equation fails for very dilute or very strong weak acids.

**Answer.** $\mathrm{pH} = \mathrm{p}K_a$ at half equivalence;
$\mathrm{pH} = \tfrac{1}{2}(\mathrm{p}K_w + \mathrm{p}K_a + \log C_{\text{eq}})$ at
equivalence.

**Check.** For acetic acid, $\mathrm{p}K_a = 4.76$; a $0.100\ \text{mol L}^{-1}$
solution at equivalence has $C_b \approx 0.050\ \text{mol L}^{-1}$ and
$\mathrm{pH} \approx \tfrac{1}{2}(14.00 + 4.76 - 1.30) = 8.73$, in the
phenolphthalein range.

**Where marks are lost.** Using $\mathrm{pH} = 7$ at equivalence for a weak acid, or
inserting concentrations rather than amounts into the buffer ratio.

### 15. The conditional formation constant of EDTA

**Strategy.** Separate the free metal–EDTA equilibrium from the acid–base side
reactions of EDTA.

**Working.** For the 1:1 complex,

$$
K_f = \frac{[\ce{MY^{n-4}}]}{[\ce{M^{n+}}][\ce{Y^{4-}}]} .
$$

EDTA is distributed among $\ce{H4Y}$, $\ce{H3Y-}$, $\ce{H2Y^2-}$, $\ce{HY^3-}$ and
$\ce{Y^4-}$, so the total uncomplexed EDTA is
$[\ce{Y'}] = \sum_{i=0}^{4}[\ce{H_iY^{i-4}}]$. Define

$$
\alpha_{\ce{Y^4-}} = \frac{[\ce{Y^{4-}}]}{[\ce{Y'}]} .
$$

Then $[\ce{Y^{4-}}] = \alpha_{\ce{Y^4-}}[\ce{Y'}]$, and substituting into $K_f$ gives

$$
K' = \frac{[\ce{MY}]}{[\ce{M}][\ce{Y'}]} = K_f\alpha_{\ce{Y^4-}} .
$$

The fraction is obtained from the acid dissociation constants:

$$
\alpha_{\ce{Y^4-}} =
\frac{K_{a1}K_{a2}K_{a3}K_{a4}}
{[\ce{H+}]^4 + K_{a1}[\ce{H+}]^3 + K_{a1}K_{a2}[\ce{H+}]^2
+ K_{a1}K_{a2}K_{a3}[\ce{H+}] + K_{a1}K_{a2}K_{a3}K_{a4}} .
$$

At low pH, $\alpha$ is small and the conditional constant is small; at high pH,
$\alpha \to 1$ and $K' \to K_f$. The titration is quantitative when
$K'C_{\text{M}} \ge 10^{6}$, which sets the minimum pH for a given metal.

**Answer.** $K' = K_f\alpha_{\ce{Y^4-}}$ with the fraction above.

**Check.** For magnesium, $K_f = 4.9\times10^{8}$ and $\alpha = 0.35$ at pH 10, so
$K' = 1.7\times10^{8}$ and $K'C = 1.7\times10^{6}$ for $C = 0.0100\ \text{mol L}^{-1}$:
just quantitative.

**Where marks are lost.** Multiplying by $\alpha$ instead of dividing, or using
$[\ce{H+}]$ in mol L⁻¹ with $K_a$ in mol L⁻¹ without consistent units.

### 16. The Nernst slope

**Strategy.** Start from the Nernst equation and convert the natural logarithm to
base 10 at 298.15 K.

**Working.** For the half-reaction $\ce{Ox + $n$e- <=> Red}$,

$$
E = E^\circ - \frac{RT}{nF}\ln\frac{a_{\text{Red}}}{a_{\text{Ox}}} .
$$

Converting to base-10 logarithms, $\ln x = 2.303\log_{10}x$, and for a monovalent
cation electrode responding to $a_i$ with $n = 1$,

$$
E = \text{const} + \frac{2.303RT}{F}\log_{10}a_i .
$$

At $T = 298.15\ \text{K}$,

$$
\frac{2.303RT}{F}
= \frac{(2.302585)(8.314462618)(298.15)}{96\,485.33212}
= 0.05916\ \text{V} = 59.16\ \text{mV}.
$$

For a divalent ion $n = 2$ and the slope is $29.58\ \text{mV}$ per decade.

**Answer.** $59.16\ \text{mV}$ per decade for $z = 1$; $29.58\ \text{mV}$ for $z = 2$.

**Check.** A tenfold change in fluoride activity changes a fluoride electrode potential
by $59.2\ \text{mV}$, and a tenfold change in calcium activity by $29.6\ \text{mV}$, as
observed in calibration.

**Where marks are lost.** Using $\log_{10}$ with the natural-log coefficient $RT/F$, or
forgetting the charge number in the denominator.

## Part C — Basic calculations

### 17. Detection and quantification limits

**Strategy.** Apply the calibration-based definitions and divide the slope by the
residual standard deviation.

**Working.**

$$
\text{LOD} = \frac{3.3s_{y/x}}{b}
= \frac{3.3(0.00210)}{0.0450} = 0.154\ \text{mg L}^{-1},
$$

$$
\text{LOQ} = \frac{10s_{y/x}}{b}
= \frac{10(0.00210)}{0.0450} = 0.467\ \text{mg L}^{-1},
$$

$$
\gamma = \frac{b}{s_y} = \frac{0.0450}{0.00210}
= 21.4\ \text{L mg}^{-1}.
$$

**Answer.** LOD $= 0.154\ \text{mg L}^{-1}$, LOQ $= 0.467\ \text{mg L}^{-1}$,
$\gamma = 21.4\ \text{L mg}^{-1}$.

**Check.** The LOQ is about three times the LOD, as the ratio $10/3.3 = 3.0$ requires;
both lie well above the calibration intercept of a typical trace method.

**Where marks are lost.** Using $3s_{y/x}$ instead of $3.3s_{y/x}$, or reporting the
LOD in the response unit.

### 18. Number of increments

**Strategy.** Invert the variance-of-the-mean expression for $n$.

**Working.**

$$
n = \left(\frac{s_b}{u}\right)^2 .
$$

For $u = 0.50\ \text{mg kg}^{-1}$:
$n = (2.5/0.50)^2 = 25$.
For $u = 0.25\ \text{mg kg}^{-1}$: $n = (2.5/0.25)^2 = 100$.

**Answer.** $25$ increments for $0.50\ \text{mg kg}^{-1}$ and $100$ for
$0.25\ \text{mg kg}^{-1}$.

**Check.** Halving the target uncertainty quadruples the required number of increments,
because $u \propto n^{-1/2}$.

**Where marks are lost.** Rounding down, which fails to meet the target, or using
$u$ in the numerator.

### 19. Internal-standard concentration

**Strategy.** Rearrange the response-ratio equation for the analyte concentration.

**Working.** From

$$
\frac{A_{\text{a}}}{A_{\text{IS}}} = F\frac{C_{\text{a}}}{C_{\text{IS}}},
$$

$$
C_{\text{a}} = \frac{1}{F}\frac{A_{\text{a}}}{A_{\text{IS}}}C_{\text{IS}}
= \frac{1.24}{0.850}(5.00) = 7.29\ \text{mg L}^{-1}.
$$

**Answer.** $C_{\text{a}} = 7.29\ \text{mg L}^{-1}$.

**Check.** The ratio of responses is greater than one and $F < 1$, so the analyte
concentration exceeds the internal-standard concentration, as found.

**Where marks are lost.** Multiplying by $F$ instead of dividing, or inverting the
response ratio.

### 20. Mean, standard deviation and confidence interval

**Strategy.** Compute the mean, the sample standard deviation with $n - 1$ degrees of
freedom, then the $t$ interval.

**Working.** **Multi-step.**

$$
\bar x = \frac{12.45+12.52+12.38+12.49+12.55+12.41}{6}
= 12.4667\ \%.
$$

The deviations are $-0.0167$, $+0.0533$, $-0.0867$, $+0.0233$, $+0.0833$ and
$-0.0567$; their squares sum to $0.021333$, so

$$
s = \sqrt{\frac{0.021333}{5}} = 0.06532\ \%,
\qquad
\frac{s}{\sqrt n} = \frac{0.06532}{\sqrt 6} = 0.02667\ \%.
$$

With $t_{0.025,5} = 2.571$,

$$
\bar x \pm t\frac{s}{\sqrt n} = 12.4667 \pm (2.571)(0.02667)
= 12.4667 \pm 0.0686\ \% .
$$

**Answer.** $\bar x = 12.47\ \%$, $s = 0.065\ \%$, standard error
$0.027\ \%$, $95\ \%$ confidence interval $12.40$–$12.53\ \%$.

**Check.** The interval spans about two standard errors on each side, as expected for
$n = 6$; it contains the individual values except the lowest, which is normal.

**Where marks are lost.** Dividing by $n$ instead of $n - 1$ in $s$, or using
$z = 1.96$ in place of $t = 2.571$.

### 21. Uncertainty of a dilution

**Strategy.** Write the concentration as a product of mass and volume ratios, then add
relative variances.

**Working.** **Multi-step.** The mass concentration is

$$
c = \frac{m}{V_1}\cdot\frac{V_2}{V_3}
= \frac{512.3\ \text{mg}}{250.0\ \text{mL}}
\cdot\frac{5.00\ \text{mL}}{100.0\ \text{mL}}
= 0.10246\ \text{mg mL}^{-1} = 102.46\ \text{mg L}^{-1}.
$$

The relative standard uncertainties are:

| Quantity | Value | $u$ | $u/x$ |
|---|---|---|---|
| $m$ | $512.3\ \text{mg}$ | $0.2\ \text{mg}$ | $3.90\times10^{-4}$ |
| $V_1$ | $250.0\ \text{mL}$ | $0.12\ \text{mL}$ | $4.80\times10^{-4}$ |
| $V_2$ | $5.00\ \text{mL}$ | $0.02\ \text{mL}$ | $4.00\times10^{-3}$ |
| $V_3$ | $100.0\ \text{mL}$ | $0.08\ \text{mL}$ | $8.00\times10^{-4}$ |

$$
\frac{u(c)}{c}
= \sqrt{(3.90\times10^{-4})^2 + (4.80\times10^{-4})^2
+ (4.00\times10^{-3})^2 + (8.00\times10^{-4})^2}
= 4.13\times10^{-3}.
$$

Thus $u(c) = 4.13\times10^{-3}\times102.46 = 0.423\ \text{mg L}^{-1}$. The pipette
term contributes $1.60\times10^{-5}$ of the total variance $1.70\times10^{-5}$, that is
$94\ \%$: the $5.00\ \text{mL}$ aliquot dominates.

**Answer.** $c = 102.5 \pm 0.4\ \text{mg L}^{-1}$ (standard uncertainty), relative
standard uncertainty $0.41\ \%$; the pipette is the dominant contribution.

**Check.** The uncertainty is dominated by the smallest volume, as expected; improving
the balance or the flask would not materially improve the result.

**Where marks are lost.** Adding the percentage uncertainties arithmetically, or
treating the dilution factor as exact.

### 22. Single-point standard addition

**Strategy.** Use the standard-addition equation with the spike volume included in the
final volume.

**Working.** The denominator is $A_2(V_x+V_s) - A_1V_x$:

$$
A_2(27.00) = 0.512\times27.00 = 13.824,
\qquad
A_1(25.00) = 0.326\times25.00 = 8.150,
$$

so the difference is $5.674$. The numerator is
$A_1C_sV_s = 0.326\times10.0\times2.00 = 6.52$. Hence

$$
C_x = \frac{6.52}{5.674} = 1.149\ \text{mg L}^{-1}.
$$

**Answer.** $C_x = 1.15\ \text{mg L}^{-1}$.

**Check.** The spike adds $20.0\ \mu\text{g}$ to $25.00\ \text{mL}$, that is
$0.800\ \text{mg L}^{-1}$ before dilution; the absorbance rises by a factor
$0.512/0.326 = 1.57$, consistent with a native concentration of about
$1.15\ \text{mg L}^{-1}$ plus the spike.

**Where marks are lost.** Using $25.00\ \text{mL}$ rather than $27.00\ \text{mL}$ as
the final volume after the spike.

### 23. Gravimetric factor and iron content

**Strategy.** Build the factor from the stoichiometry, then multiply by the mass ratio.

**Working.** **Multi-step.** Two iron atoms occur in each $\ce{Fe2O3}$ formula unit, so

$$
GF = \frac{2M(\ce{Fe})}{M(\ce{Fe2O3})}
= \frac{2(55.845)}{159.688} = 0.69943 .
$$

The mass fraction is

$$
w(\ce{Fe}) = \frac{m(\ce{Fe2O3})\,GF}{m_{\text{sample}}}
= \frac{(0.3420)(0.69943)}{0.5000} = 0.47841,
$$

or $47.84\ \%$.

**Answer.** $GF = 0.6994$; $w(\ce{Fe}) = 47.8\ \%$.

**Check.** The result is below the iron content of pure $\ce{Fe2O3}$
($69.94\ \%$), as it must be for an ore, and the factor times the product mass
($0.2392\ \text{g}$) is less than the sample mass.

**Where marks are lost.** Using $M(\ce{Fe})/M(\ce{Fe2O3})$ without the factor 2, which
halves the answer.

### 24. Purity of potassium hydrogen phthalate

**Strategy.** Convert the titre to moles of base, use the 1:1 stoichiometry, then
compare the mass with the sample mass.

**Working.** **Multi-step.** The reaction is

$$
\ce{C8H5KO4 + NaOH -> C8H4KNaO4 + H2O}
$$

The amount of base is

$$
n(\ce{NaOH}) = cV = (0.1000)(25.06\times10^{-3})
= 2.506\times10^{-3}\ \text{mol}.
$$

Since $\ce{KHP}$ reacts 1:1 with hydroxide,
$n(\ce{KHP}) = 2.506\times10^{-3}\ \text{mol}$ and

$$
m(\ce{KHP}) = n M = (2.506\times10^{-3})(204.22)
= 0.51178\ \text{g}.
$$

The mass fraction is

$$
w = \frac{0.51178}{0.5120}\times100\ \% = 99.96\ \% .
$$

**Answer.** $w(\ce{KHP}) = 99.96\ \%$.

**Check.** The titre corresponds almost exactly to the sample mass, and a purity just
below $100\ \%$ is typical of a dried primary standard.

**Where marks are lost.** Forgetting to convert the titre to dm³, or using a 1:2
stoichiometry that does not apply to a monoprotic acid.

### 25. Retention, selectivity and resolution

**Strategy.** Compute the retention factors from the dead time, then the selectivity,
resolution and plate numbers.

**Working.** **Multi-step.**

$$
k_1 = \frac{5.40-1.20}{1.20} = 3.50,
\qquad
k_2 = \frac{6.30-1.20}{1.20} = 4.25,
$$

$$
\alpha = \frac{k_2}{k_1} = \frac{4.25}{3.50} = 1.214,
$$

$$
R_s = \frac{2(6.30-5.40)}{0.42+0.48} = \frac{1.80}{0.90} = 2.00 .
$$

The plate numbers are

$$
N_1 = 16\left(\frac{5.40}{0.42}\right)^2 = 2.64\times10^{3},
\qquad
N_2 = 16\left(\frac{6.30}{0.48}\right)^2 = 2.76\times10^{3}.
$$

**Answer.** $k_1 = 3.50$, $k_2 = 4.25$, $\alpha = 1.21$, $R_s = 2.00$,
$N_1 = 2.6\times10^{3}$, $N_2 = 2.8\times10^{3}$.

**Check.** $R_s = 2.0$ exceeds the baseline-resolution criterion of $1.5$, consistent
with the visual separation of peaks whose widths are less than their separation.

**Where marks are lost.** Using $t_R$ rather than $t_R - t_M$ in the retention factor,
or omitting the factor 2 in the resolution definition.

### 26. Beer's law concentration and transmittance

**Strategy.** Invert $A = \varepsilon c l$ and convert absorbance to transmittance.

**Working.** **Multi-step.**

$$
c = \frac{A}{\varepsilon l}
= \frac{0.615}{(1.25\times10^{4})(1.00)}
= 4.92\times10^{-5}\ \text{mol dm}^{-3}.
$$

The transmittance is

$$
T = 10^{-A} = 10^{-0.615} = 0.243 .
$$

**Answer.** $c = 4.92\times10^{-5}\ \text{mol dm}^{-3}$, $T = 24.3\ \%$.

**Check.** An absorbance of $0.615$ corresponds to $T \approx 24\ \%$, and about
$76\ \%$ of the light is absorbed, consistent with a moderately strong chromophore at
this concentration.

**Where marks are lost.** Using $\ln$ rather than $\log_{10}$, or inverting the
Beer's law equation as $c = \varepsilon l/A$.

---

## Part D — Intermediate problems

### 27. Testing a mean against a certified value

**Strategy.** A one-sample $t$ test with $n - 1$ degrees of freedom.

**Working.** **Multi-step.** $H_0$: $\mu = 12.60\ \%$; $H_1$: $\mu \ne 12.60\ \%$.
The statistic is

$$
t = \frac{\bar x - \mu}{s/\sqrt n}
= \frac{12.47-12.60}{0.065/\sqrt 5}
= \frac{-0.130}{0.02907} = -4.472 .
$$

With $\nu = 4$, $t_{0.025,4} = 2.776$. Since $|t| = 4.47 > 2.776$, $H_0$ is rejected:
the method has a significant bias at $95\ \%$ confidence. The bias is
$-0.13\ \%$ absolute, or $-1.03\ \%$ relative.

**Answer.** $t = -4.47$, $\nu = 4$, $t_{\text{crit}} = 2.776$; significant negative
bias of $1.0\ \%$ relative. The method should not be used for compliance until the
source of the bias is found and corrected.

**Check.** The $95\ \%$ confidence interval for the mean is
$12.47 \pm 2.776(0.02907) = 12.47 \pm 0.081$, that is $12.39$–$12.55\ \%$, which
excludes $12.60\ \%$.

**Where marks are lost.** Using $n$ rather than $n - 1$ degrees of freedom, or
concluding "no bias" because the difference is numerically small without a test.

### 28. Comparing two methods: $F$ test and pooled $t$ test

**Strategy.** Test the variances first; if they are not significantly different, pool
them and compare the means.

**Working.** **Multi-step.** $H_0$ for the $F$ test: $\sigma_1^2 = \sigma_2^2$. With
the larger variance in the numerator,

$$
F = \frac{s_1^2}{s_2^2} = \frac{(1.8)^2}{(1.1)^2} = \frac{3.24}{1.21} = 2.68 .
$$

With $\nu_1 = \nu_2 = 5$, $F_{0.025}(5,5) = 5.05$; since $2.68 < 5.05$, the variances
do not differ significantly.

The pooled standard deviation is

$$
s_p = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}}
= \sqrt{\frac{5(3.24)+5(1.21)}{10}}
= \sqrt{2.225} = 1.492 .
$$

The $t$ statistic is

$$
t = \frac{|\bar x_1-\bar x_2|}{s_p\sqrt{1/n_1+1/n_2}}
= \frac{1.3}{1.492\sqrt{1/6+1/6}}
= \frac{1.3}{0.861} = 1.51 .
$$

With $\nu = 10$, $t_{0.025,10} = 2.228$; since $1.51 < 2.228$, there is no significant
difference between the means at $95\ \%$ confidence.

**Answer.** $F = 2.68 < 5.05$ (variances equal); $t = 1.51 < 2.228$ (means not
significantly different).

**Check.** The difference of $1.3\ \%$ is smaller than the pooled standard deviation
of $1.5\ \%$, so a non-significant result is expected.

**Where marks are lost.** Applying the pooled $t$ test without testing the variances,
or using $\nu = n_1 + n_2 - 1$.

### 29. One-way ANOVA

**Strategy.** Partition the total sum of squares into between-laboratory and
within-laboratory components, form mean squares, and compare $F$ with the critical
value.

**Working.** **Multi-step.** The laboratory means are $10.2$, $10.5$, $10.0$ and
$10.9$, and the grand mean is $10.4$. The between-laboratory sum of squares is

$$
SS_{\text{between}} = 3\left[(10.2-10.4)^2 + (10.5-10.4)^2
+ (10.0-10.4)^2 + (10.9-10.4)^2\right] = 1.38,
$$

with $\nu_{\text{between}} = 4 - 1 = 3$, so $MS_{\text{between}} = 0.460$.

Within each laboratory the three results have a sum of squared deviations of $0.02$,
so

$$
SS_{\text{within}} = 4(0.02) = 0.080,
\qquad
\nu_{\text{within}} = 4(3-1) = 8,
\qquad
MS_{\text{within}} = 0.0100 .
$$

Therefore

$$
F = \frac{MS_{\text{between}}}{MS_{\text{within}}} = \frac{0.460}{0.0100} = 46.0 .
$$

With $F_{0.05}(3,8) = 4.07$ and $46.0 \gg 4.07$, the laboratory means differ highly
significantly.

**Answer.** $F = 46.0$, $\nu_1 = 3$, $\nu_2 = 8$, $F_{\text{crit}} = 4.07$; the
laboratory means differ at $95\ \%$ confidence.

**Check.** Laboratory D is about $0.5$ above the grand mean while the within-laboratory
spread is only $0.1$, so a large $F$ is inevitable.

**Where marks are lost.** Using $n = 12$ instead of the number of groups in the
between-laboratory degrees of freedom, or comparing $F$ with $F(3,12)$.

### 30. Grubbs test

**Strategy.** Compute the largest standardised deviation and compare with the tabulated
critical value.

**Working.** **Multi-step.** The mean of the five values is

$$
\bar x = \frac{10.02+10.05+9.98+10.01+10.60}{5} = 10.132\ \%,
$$

and the sample standard deviation is $s = 0.2628\ \%$. The suspect value is $10.60$,
so

$$
G = \frac{|10.60-10.132|}{0.2628} = 1.781 .
$$

With $n = 5$, $G_{\text{crit}} = 1.715$ at $95\ \%$ confidence. Since
$1.781 > 1.715$, the value $10.60$ is rejected as an outlier at this confidence level.

After rejection, the remaining four values have mean $10.015\ \%$ and standard
deviation $0.0289\ \%$.

**Answer.** $G = 1.781 > 1.715$; reject $10.60\ \%$. The retained mean is
$10.02\ \%$ with $s = 0.029\ \%$.

**Check.** The rejected value lies $1.78s$ from the mean, which is not extreme in
absolute terms; the test rejects it because the remaining four values are unusually
concordant. This illustrates why outlier tests should be applied once and reported,
not iterated until the data look tidy.

**Where marks are lost.** Recomputing $G$ after removing the point and rejecting a
second value, or using the standard deviation of the trimmed data in the numerator.

### 31. Weighted and unweighted regression

**Strategy.** Form the weighted normal equations with $w_i = 1/s_i^2$, and compare with
the unweighted fit.

**Working.** **Multi-step.** The weights are $1/0.05^2 = 400$, $1/0.10^2 = 100$ and
$1/1.00^2 = 1$. Then

$$
\sum w = 501,\quad \sum wx = 700,\quad \sum wy = 1243,
\quad \sum wx^2 = 1300,\quad \sum wxy = 1983 .
$$

The weighted slope is

$$
b_w = \frac{(\sum w)(\sum wxy) - (\sum wx)(\sum wy)}
{(\sum w)(\sum wx^2) - (\sum wx)^2}
= \frac{501(1983) - 700(1243)}{501(1300) - 700^2}
= \frac{993\,483 - 870\,100}{651\,300 - 490\,000}
= \frac{123\,383}{161\,300} = 1.9086,
$$

and the intercept is

$$
a_w = \frac{\sum wy - b_w\sum wx}{\sum w}
= \frac{1243 - 1.9086(700)}{501} = 0.1904 .
$$

The unweighted fit gives $b = 2.100$ and $a = -0.0667$.

The weighted fit is appropriate because the standard deviations differ by a factor of
20 and the variances by a factor of 400. The unweighted fit gives the imprecise third
point the same influence as the precise first two and is pulled upwards: its residual
at $x = 3.00$ is only $0.067$ but at $x = 1.00$ it is $1.34\sigma$, and at $x = 2.00$
it is $1.33\sigma$. The weighted fit has residuals $0.02\sigma$, $0.08\sigma$ and
$0.38\sigma$, all acceptable.

**Answer.** Weighted: $b = 1.91$, $a = 0.190$. Unweighted: $b = 2.10$,
$a = -0.067$. Weighted least squares is correct here.

**Check.** The weighted line passes through the weighted centroid, and every weighted
residual is below one standard deviation, as a good fit requires.

**Where marks are lost.** Using $1/s_i$ instead of $1/s_i^2$ as the weight, or
reporting the unweighted fit because it is easier to compute.

### 32. Standard-addition calibration with dilution

**Strategy.** Regress absorbance on added concentration, extrapolate to zero absorbance,
then correct for the dilution from $25.00$ to $50.00\ \text{mL}$.

**Working.** **Multi-step.** For the five points,
$\sum x = 20.00$, $\sum y = 1.720$, $\sum x^2 = 120.0$, $\sum xy = 8.560$ and
$n = 5$. Hence

$$
b = \frac{5(8.560) - (20.00)(1.720)}{5(120.0) - (20.00)^2}
= \frac{42.80 - 34.40}{600.0 - 400.0}
= \frac{8.400}{200.0} = 0.0325,
$$

$$
a = \frac{1.720 - 0.0325(20.00)}{5} = 0.2140 .
$$

The $x$-intercept is

$$
x_0 = -\frac{a}{b} = -\frac{0.2140}{0.0325} = -6.585\ \text{mg L}^{-1},
$$

which is the concentration in the diluted solution. The sample was diluted from
$25.00$ to $50.00\ \text{mL}$, a factor of 2, so

$$
C_{\text{sample}} = 6.585\times\frac{50.00}{25.00} = 13.17\ \text{mg L}^{-1}.
$$

**Answer.** Slope $0.0325\ \text{L mg}^{-1}$, intercept $0.214$, $x$-intercept
$-6.59\ \text{mg L}^{-1}$ in the diluted solution, and
$C_{\text{sample}} = 13.2\ \text{mg L}^{-1}$.

**Check.** The intercept is the absorbance of the unspiked diluted sample, consistent
with the first data point; the extrapolation is only $6.6\ \text{mg L}^{-1}$ beyond the
origin, well within the calibrated range.

**Where marks are lost.** Reporting the $x$-intercept as the sample concentration and
forgetting the dilution factor, or using the wrong sign for the intercept.

### 33. Atomic absorption of soil

**Strategy.** Invert the calibration, convert the solution mass to the sample mass, and
express per kilogram.

**Working.** **Multi-step.**

$$
c = \frac{A - 0.004}{0.214} = \frac{0.276-0.004}{0.214}
= 1.271\ \text{mg L}^{-1}.
$$

The solution volume is $0.1000\ \text{L}$, so the mass in the digest is
$1.271\times0.1000 = 0.1271\ \text{mg}$. This came from $2.000\ \text{g}$ of soil,
that is $2.000\times10^{-3}\ \text{kg}$, so

$$
w = \frac{0.1271\ \text{mg}}{2.000\times10^{-3}\ \text{kg}}
= 63.55\ \text{mg kg}^{-1}.
$$

**Answer.** $63.6\ \text{mg kg}^{-1}$.

**Check.** The absorbance lies in the middle of the calibration range, and the result
is a plausible trace metal content for soil.

**Where marks are lost.** Forgetting the $100\ \text{mL}$ dilution, or using the sample
mass in grams and reporting $\text{mg g}^{-1}$.

### 34. Redox titration with cerium(IV)

**Strategy.** Use the iron couple before equivalence, the average of the two standard
potentials at equivalence, and the cerium couple after equivalence.

**Working.** **Multi-step.** The titration reaction is

$$
\ce{Fe^2+ + Ce^4+ -> Fe^3+ + Ce^3+}
$$

(a) The amounts are
$n(\ce{Fe^2+}) = 0.1000\times25.00\times10^{-3} = 2.500\times10^{-3}\ \text{mol}$,
and cerium(IV) reacts 1:1, so

$$
V_{\text{eq}} = \frac{2.500\times10^{-3}}{0.02000} = 0.1250\ \text{L} = 125.0\ \text{mL}.
$$

(b) At $50\ \%$, $[\ce{Fe^3+}] = [\ce{Fe^2+}]$, so the logarithmic term vanishes and
$E = E^\circ(\ce{Fe^3+/Fe^2+}) = +0.771\ \text{V}$.

(c) At equivalence both couples are present in comparable amounts and

$$
E_{\text{eq}} = \frac{n_1E_1^\circ + n_2E_2^\circ}{n_1+n_2}
= \frac{0.771+1.61}{2} = +1.191\ \text{V}.
$$

(d) At $100.1\ \%$ the excess cerium(IV) is $0.1\ \%$ of
$2.500\ \text{mmol}$, that is $2.5\times10^{-3}\ \text{mmol}$, while
$[\ce{Ce^3+}] = 2.500\ \text{mmol}$. The ratio
$[\ce{Ce^4+}]/[\ce{Ce^3+}] = 1.0\times10^{-3}$, so

$$
E = 1.61 + 0.05916\log_{10}(1.0\times10^{-3})
= 1.61 - 0.1775 = +1.433\ \text{V}.
$$

**Answer.** $V_{\text{eq}} = 125.0\ \text{mL}$; $E = +0.771\ \text{V}$ at $50\ \%$;
$E = +1.191\ \text{V}$ at equivalence; $E = +1.433\ \text{V}$ at $100.1\ \%$.

**Check.** The potential jumps by $0.66\ \text{V}$ between $50\ \%$ and equivalence and
by a further $0.24\ \text{V}$ in the next $0.1\ \%$, which is the steep jump an
indicator such as ferroin ($E^\circ = 1.06\ \text{V}$) detects.

**Where marks are lost.** Using the cerium potential at $50\ \%$, or averaging the
potentials without weighting by the number of electrons.

### 35. van Deemter optimum

**Strategy.** Differentiate $H(u)$ or use the standard results, then divide the column
length by $H_{\min}$.

**Working.** **Multi-step.**

$$
u_{\text{opt}} = \sqrt{\frac{B}{C}}
= \sqrt{\frac{0.60}{0.040}} = 3.87\ \text{cm s}^{-1},
$$

$$
H_{\min} = A + 2\sqrt{BC}
= 0.50 + 2\sqrt{(0.60)(0.040)}
= 0.50 + 0.310 = 0.810\ \text{mm}.
$$

The plate number is

$$
N = \frac{L}{H_{\min}} = \frac{250\ \text{mm}}{0.810\ \text{mm}} = 309 .
$$

**Answer.** $u_{\text{opt}} = 3.9\ \text{cm s}^{-1}$, $H_{\min} = 0.81\ \text{mm}$,
$N = 3.1\times10^{2}$.

**Check.** At $u = u_{\text{opt}}$ the $B/u$ and $Cu$ terms are equal, each
$0.155\ \text{mm}$, so $H = 0.50 + 0.31 = 0.81\ \text{mm}$ as required.

**Where marks are lost.** Using $H_{\min} = A + \sqrt{BC}$ (forgetting the factor 2), or
mixing millimetres and centimetres in $u_{\text{opt}}$.

### 36. Potentiometric pH

**Strategy.** Use the operational pH definition with the measured potentials and the
electrode slope.

**Working.** **Multi-step.** The cell potential changes by
$E_X - E_S = 0.148 - 0.206 = -0.058\ \text{V}$, so

$$
\mathrm{pH}(X) = \mathrm{pH}(S) + \frac{E_X - E_S}{0.05916}
= 4.00 + \frac{-0.058}{0.05916}
= 4.00 - 0.980 = 3.02 .
$$

**Answer.** $\mathrm{pH} = 3.02$.

**Check.** The sample potential is $58\ \text{mV}$ lower than the buffer, almost exactly
one pH unit, so a pH near $3.0$ is expected.

**Where marks are lost.** Reversing the sign, which gives pH $5.0$, or using
$59.16\ \text{V}$ instead of millivolts.

---

## Part E — Advanced problems

### 37. Sampling error, sample mass and combined uncertainty

**Strategy.** Apply Gy's fundamental-error expression, invert it for mass, then combine
the sampling variance of the composite with the analytical variance.

**Working.** **Multi-step.** (a) With $d = 20\ \text{mm} = 0.020\ \text{m}$ and
$M_s = 0.500\ \text{kg}$,

$$
\sigma_{\text{FE}}^2 = \frac{Kd^3}{M_s}
= \frac{(0.40)(0.020)^3}{0.500}
= 6.40\times10^{-6},
$$

so $\sigma_{\text{FE}} = 2.53\times10^{-3}$, or $0.253\ \%$.

(b) For a target $\sigma = 0.10\ \% = 1.0\times10^{-3}$,

$$
M_s = \frac{Kd^3}{\sigma^2}
= \frac{(0.40)(8.00\times10^{-6})}{(1.0\times10^{-3})^2}
= 3.20\ \text{kg}.
$$

(c) Eight increments of $0.500\ \text{kg}$ give a composite of $4.00\ \text{kg}$. Its
fundamental error is

$$
\sigma_{\text{sampling}}^2 = \frac{(0.40)(8.00\times10^{-6})}{4.00}
= 8.00\times10^{-7},
$$

that is $\sigma_{\text{sampling}} = 8.94\times10^{-4} = 0.0894\ \%$. Combining with the
analytical standard deviation of $0.150\ \%$,

$$
\sigma_{\text{total}}
= \sqrt{8.00\times10^{-7} + (1.50\times10^{-3})^2}
= \sqrt{3.05\times10^{-6}}
= 1.75\times10^{-3},
$$

or $0.175\ \%$.

**Answer.** (a) $0.253\ \%$; (b) $3.2\ \text{kg}$; (c) $0.175\ \%$.

**Check.** The composite of $4\ \text{kg}$ is above the $3.2\ \text{kg}$ required for
$0.10\ \%$ sampling error, yet the combined uncertainty is $0.175\ \%$ because the
analytical term ($0.150\ \%$) now dominates. Improving the sampling further would not
help.

**Where marks are lost.** Using $d$ in millimetres, which changes $d^3$ by $10^{9}$, or
adding standard deviations rather than variances.

### 38. Uncertainty budget and compliance

**Strategy.** Combine independent standard uncertainties in quadrature, expand with
$k = 2$, and compare the upper limit with the regulatory threshold.

**Working.** **Multi-step.** The combined standard uncertainty is

$$
u_c = \sqrt{1.2^2 + 0.8^2 + 0.6^2 + 0.3^2}
= \sqrt{1.44+0.64+0.36+0.09}
= \sqrt{2.53} = 1.59\ \text{mg kg}^{-1}.
$$

The expanded uncertainty for $k = 2$ is

$$
U = 2u_c = 3.18\ \text{mg kg}^{-1}.
$$

The result is therefore $45.3 \pm 3.2\ \text{mg kg}^{-1}$ (95 % coverage), with an
upper limit of $48.5\ \text{mg kg}^{-1}$.

**Answer.** $u_c = 1.59\ \text{mg kg}^{-1}$, $U = 3.18\ \text{mg kg}^{-1}$; the result
is $45.3 \pm 3.2\ \text{mg kg}^{-1}$. The upper limit $48.5\ \text{mg kg}^{-1}$ is below
the limit of $50\ \text{mg kg}^{-1}$, so compliance can be reported.

**Check.** The dominant term is calibration ($1.2$), contributing $1.44/2.53 = 57\ \%$
of the variance; the point estimate is $4.7\ \text{mg kg}^{-1}$ below the limit, which
is larger than $U$, so the decision is not marginal.

**Where marks are lost.** Adding the contributions linearly, which gives $2.9$ and
$U = 5.8$, or comparing the point estimate alone with the limit while ignoring the
uncertainty.

### 39. Validation: detection limit, recovery and fitness for purpose

**Strategy.** Use the calibration-based LOD and LOQ, test recovery with a one-sample
$t$ test, then compare the target concentration with the LOQ.

**Working.** **Multi-step.** (a)

$$
\text{LOD} = \frac{3.3(0.0040)}{0.250} = 0.0528\ \text{mg kg}^{-1},
\qquad
\text{LOQ} = \frac{10(0.0040)}{0.250} = 0.160\ \text{mg kg}^{-1}.
$$

(The blank standard deviation of $0.0035$ gives a similar LOD of
$3(0.0035)/0.250 = 0.042$; the regression value is the appropriate one when the
calibration is linear.)

(b) The recovery is

$$
R = \frac{C_{\text{spiked}} - C_{\text{native}}}{C_{\text{added}}}\times100\ \%
= \frac{1.66-1.20}{0.500}\times100\ \% = 92.0\ \%.
$$

Testing $H_0$: $R = 100\ \%$,

$$
t = \frac{|92.0-100|}{4.0/\sqrt 5} = \frac{8.0}{1.789} = 4.47 .
$$

With $\nu = 4$ and $t_{0.025,4} = 2.776$, the bias is significant: the method
under-recovers by $8\ \%$, and a correction or an improved extraction is required.

(c) The target concentration of $0.100\ \text{mg kg}^{-1}$ is above the LOD
($0.053$) but below the LOQ ($0.160$). At that level the method can detect the analyte
but cannot quantify it with acceptable precision, so it is **not** fit for purpose for
quantification at $0.100\ \text{mg kg}^{-1}$.

**Answer.** LOD $= 0.053\ \text{mg kg}^{-1}$, LOQ $= 0.16\ \text{mg kg}^{-1}$;
recovery $92.0\ \%$, $t = 4.47 > 2.776$ (significant bias); not fit for quantification
at $0.100\ \text{mg kg}^{-1}$.

**Check.** A recovery of $92\ \%$ with $s = 4\ \%$ would be acceptable for many
screening methods, but the significant $t$ shows that the shortfall is real, not
sampling noise.

**Where marks are lost.** Reporting the recovery as acceptable because it is "close to
100 %" without a test, or claiming fitness because the target is above the LOD.

### 40. Back-titration of calcium carbonate

**Strategy.** Subtract the unreacted acid from the total, convert to carbonate with the
2:1 stoichiometry, and express as a mass fraction.

**Working.** **Multi-step.** The total acid is

$$
n(\ce{HCl}) = (0.1000)(50.00\times10^{-3}) = 5.000\times10^{-3}\ \text{mol}.
$$

The excess acid is

$$
n(\ce{NaOH}) = (0.0980)(12.50\times10^{-3}) = 1.225\times10^{-3}\ \text{mol},
$$

so the acid consumed by the sample is
$5.000 - 1.225 = 3.775\ \text{mmol}$. From

$$
\ce{CaCO3(s) + 2HCl(aq) -> CaCl2(aq) + CO2(g) + H2O(l)}
$$

the stoichiometry gives

$$
n(\ce{CaCO3}) = \tfrac{1}{2}(3.775\times10^{-3}) = 1.8875\times10^{-3}\ \text{mol},
$$

$$
m(\ce{CaCO3}) = (1.8875\times10^{-3})(100.09) = 0.18892\ \text{g}.
$$

Hence

$$
w(\ce{CaCO3}) = \frac{0.18892}{0.2500}\times100\ \% = 75.57\ \% .
$$

**Answer.** $w(\ce{CaCO3}) = 75.6\ \%$.

**Check.** The acid consumed is $3.775\ \text{mmol}$, about three quarters of the
$5.000\ \text{mmol}$ added, consistent with a sample that is about three quarters
carbonate.

**Where marks are lost.** Forgetting the 2:1 stoichiometry, which doubles the result,
or subtracting the NaOH volume from the HCl volume without converting to moles.

### 41. Conditional constants and the minimum pH for an EDTA titration

**Strategy.** Multiply $K_f$ by $\alpha_{\ce{Y^4-}}$ at each pH, then apply the
quantitative criterion $K'C \ge 10^{6}$.

**Working.** **Multi-step.** At pH 10,

$$
K' = K_f\alpha = (4.9\times10^{8})(0.35) = 1.72\times10^{8},
\qquad
K'C = (1.72\times10^{8})(0.0100) = 1.72\times10^{6}.
$$

At pH 8,

$$
K' = (4.9\times10^{8})(5.4\times10^{-3}) = 2.65\times10^{6},
\qquad
K'C = 2.65\times10^{4}.
$$

The criterion $K'C \ge 10^{6}$ is satisfied at pH 10 but not at pH 8. The titration is
therefore quantitative at pH 10 and not at pH 8.

**Answer.** $K' = 1.72\times10^{8}$ at pH 10 ($K'C = 1.72\times10^{6}$, quantitative)
and $K' = 2.65\times10^{6}$ at pH 8 ($K'C = 2.65\times10^{4}$, not quantitative).

**Check.** The hundredfold fall in $\alpha$ between pH 10 and pH 8 lowers $K'$ by the
same factor, and $K'C$ falls below the criterion by a factor of nearly 40.

**Where marks are lost.** Using $K_f$ alone and concluding that both pH values work, or
multiplying $K'C$ by $\alpha$ twice.

### 42. Plate number and plate height for a required resolution

**Strategy.** Invert the resolution equation for $N$, then divide the column length by
$N$.

**Working.** **Multi-step.**

$$
N = 16R_s^2\left[\frac{1+k}{(\alpha-1)k}\right]^2
= 16(1.5)^2\left[\frac{5.0}{(0.10)(4.0)}\right]^2
= 36(12.5)^2 = 5.63\times10^{3}.
$$

The plate height on a $150\ \text{mm}$ column is

$$
H = \frac{L}{N} = \frac{150\ \text{mm}}{5625} = 0.0267\ \text{mm} = 26.7\ \mu\text{m}.
$$

If $k$ falls to $1.0$ at constant $\alpha$,

$$
N = 36\left[\frac{2.0}{(0.10)(1.0)}\right]^2 = 36(20)^2 = 1.44\times10^{4},
$$

so the required plate number rises by a factor of $2.56$.

**Answer.** $N = 5.6\times10^{3}$, $H = 26.7\ \mu\text{m}$; at $k = 1.0$,
$N = 1.4\times10^{4}$.

**Check.** The $k/(1+k)$ factor falls from $0.80$ to $0.50$, and $N$ scales as the
inverse square, giving $(0.80/0.50)^2 = 2.56$, as found.

**Where marks are lost.** Using $R_s = 1.0$ or omitting the factor 16, or reporting $H$
in millimetres when the column is in metres.

### 43. Simultaneous determination of two components

**Strategy.** Use the additivity of absorbance to write two linear equations and solve
the $2\times2$ system.

**Working.** **Multi-step.** With $b = 1.00\ \text{cm}$,

$$
0.856 = 1.20\times10^{4}c_X + 1.50\times10^{3}c_Y,
$$

$$
0.228 = 2.00\times10^{3}c_X + 9.00\times10^{3}c_Y .
$$

The determinant is

$$
\Delta = (1.20\times10^{4})(9.00\times10^{3})
- (1.50\times10^{3})(2.00\times10^{3})
= 1.08\times10^{8} - 3.00\times10^{6} = 1.05\times10^{8}.
$$

By Cramer's rule,

$$
c_X = \frac{(0.856)(9.00\times10^{3}) - (0.228)(1.50\times10^{3})}{1.05\times10^{8}}
= \frac{7704-342}{1.05\times10^{8}} = 7.01\times10^{-5}\ \text{mol dm}^{-3},
$$

$$
c_Y = \frac{(1.20\times10^{4})(0.228) - (2.00\times10^{3})(0.856)}{1.05\times10^{8}}
= \frac{2736-1712}{1.05\times10^{8}} = 9.75\times10^{-6}\ \text{mol dm}^{-3}.
$$

**Answer.** $c_X = 7.01\times10^{-5}\ \text{mol dm}^{-3}$,
$c_Y = 9.75\times10^{-6}\ \text{mol dm}^{-3}$.

**Check.** Substituting back,

$$
1.20\times10^{4}(7.011\times10^{-5}) + 1.50\times10^{3}(9.752\times10^{-6})
= 0.8413 + 0.0146 = 0.856,
$$

$$
2.00\times10^{3}(7.011\times10^{-5}) + 9.00\times10^{3}(9.752\times10^{-6})
= 0.1402 + 0.0878 = 0.228,
$$

both as measured.

**Where marks are lost.** Using the same wavelength twice, or solving the equations with
the absorptivities in the wrong units ($\text{cm}^{-1}$ versus
$\text{dm}^3\ \text{mol}^{-1}\ \text{cm}^{-1}$).

### 44. Voltammetric peak current

**Strategy.** Apply the Randles–Ševčík equation with concentration in
$\text{mol cm}^{-3}$, then scale with the square root of the scan rate.

**Working.** **Multi-step.** The concentration is
$1.0\times10^{-3}\ \text{mol dm}^{-3} = 1.0\times10^{-6}\ \text{mol cm}^{-3}$. Then

$$
i_p = 2.69\times10^{5}n^{3/2}AD^{1/2}Cv^{1/2}
$$

$$
= 2.69\times10^{5}(1)^{3/2}(0.020)(6.5\times10^{-6})^{1/2}
(1.0\times10^{-6})(0.100)^{1/2}
= 4.34\times10^{-6}\ \text{A}.
$$

Doubling the scan rate multiplies $i_p$ by $\sqrt 2$, giving
$6.13\times10^{-6}\ \text{A}$.

**Answer.** $i_p = 4.34\ \mu\text{A}$; at twice the scan rate, $6.13\ \mu\text{A}$.

**Check.** The current is proportional to $v^{1/2}$, the signature of a
diffusion-controlled process; a plot of $i_p$ against $v^{1/2}$ through the origin
confirms the mechanism.

**Where marks are lost.** Using concentration in $\text{mol dm}^{-3}$ in the
Randles–Ševčík equation, which is written for $\text{mol cm}^{-3}$ and gives a result
$10^{3}$ times too large.

---

## Part F — Multiple-choice self-check

### 45. Which is not a figure of merit

**Answer: C.** The retention index is a chromatographic identification parameter, not a
figure of merit of the method. Selectivity, LOD and dynamic range all describe the
analytical performance.

**Why A is wrong.** Selectivity is a figure of merit: it quantifies discrimination
against interferents.

**Why B is wrong.** The limit of detection is the most commonly quoted figure of merit.

**Why D is wrong.** The dynamic range defines the interval of valid quantification.

**Where marks are lost.** Treating every chromatographic descriptor as an analytical
figure of merit.

### 46. Degrees of freedom for a $t$ test

**Answer: B.** A one-sample $t$ test on $n = 6$ replicates uses $\nu = n-1 = 5$,
because one degree of freedom is spent estimating the mean.

**Why A is wrong.** Using $n = 6$ ignores the estimation of the mean and gives an
interval that is too narrow.

**Why C is wrong.** $\nu = 4$ would correspond to $n = 5$.

**Why D is wrong.** $\nu = 7$ exceeds the information in the data.

**Where marks are lost.** Confusing the number of observations with the degrees of
freedom.

### 47. Universal, non-destructive GC detector

**Answer: B.** The thermal conductivity detector responds to any species whose thermal
conductivity differs from the carrier gas, and it does not consume the analyte.

**Why A is wrong.** The FID is destructive and is insensitive to water, $\ce{CO2}$ and
permanent gases, so it is not universal.

**Why C is wrong.** The ECD is highly selective for electronegative compounds and is not
universal.

**Why D is wrong.** The flame photometric detector is selective for sulfur and
phosphorus compounds.

**Where marks are lost.** Assuming that the most sensitive detector is the most
universal one.

### 48. Why AAS uses a hollow-cathode lamp

**Answer: B.** Atomic absorption lines have widths of a few picometres, far narrower
than the bandpass of a conventional monochromator. A line source emits exactly the
analyte lines, so the measurement is made at the line centre and the calibration remains
linear.

**Why A is wrong.** Cost is not the reason; the hollow-cathode lamp is a precision
component.

**Why C is wrong.** The lamp emits a line spectrum, not a continuum.

**Why D is wrong.** A flame is still required for atomisation; the lamp does not replace
it.

**Where marks are lost.** Confusing the source with the atomiser, or ignoring the
line-width matching argument.

### 49. Negative deviation from Beer's law

**Answer: B.** At high concentration, molecules interact (association, aggregation) and
the refractive index of the solution changes, both of which reduce the apparent molar
absorptivity, giving a negative deviation.

**Why A is wrong.** Stray light causes a negative deviation, but it is most serious at
high absorbance and low concentration is not the issue; the item asks about high analyte
concentration.

**Why C is wrong.** The path length is a fixed instrumental parameter and does not cause
a deviation from the law.

**Why D is wrong.** Monochromatic radiation is an assumption of the law; polychromatic
radiation causes a deviation, not monochromatic radiation.

**Where marks are lost.** Attributing every deviation to stray light without considering
concentration-dependent chemistry.

### 50. Indicator for a weak acid–strong base titration

**Answer: B.** The equivalence pH is above 7 (about 8.7 for $0.1\ \text{mol L}^{-1}$
acetic acid), and phenolphthalein changes colour over pH 8.2–10.0, so the endpoint
coincides with the equivalence point.

**Why A is wrong.** Phenolphthalein is colourless below about pH 8.2, so its transition
range is basic, not acidic.

**Why C is wrong.** It is colourless in acid and pink in base; the two forms are
differently coloured, which is the point.

**Why D is wrong.** The indicator does not react stoichiometrically with the base; it
responds reversibly to pH.

**Where marks are lost.** Choosing an indicator whose transition range brackets pH 7
regardless of the equivalence pH.

---

## Top ten errors in this level

| Rank | Error | Why it costs marks | Correct habit |
|---|---|---|---|
| 1 | Dividing by $n$ instead of $n-1$ for $s$ | Every standard deviation and confidence interval is slightly too small | Use $n-1$ degrees of freedom for a sample |
| 2 | Using $z = 1.96$ instead of $t$ for small $n$ | Intervals too narrow; false significance | Use $t_{\alpha/2,n-1}$ and quote the degrees of freedom |
| 3 | Pooling variances without an $F$ test | The $t$ test is invalid when variances differ | Test $F$ first; use Welch's test if unequal |
| 4 | Confusing LOD and LOQ | Reporting a quantification below LOQ | LOD $= 3.3s/b$; LOQ $= 10s/b$; quantify only above LOQ |
| 5 | Forgetting the spike volume in the standard-addition denominator | $C_x$ too high by the dilution factor | Use $A_2(V_x+V_s) - A_1V_x$ |
| 6 | Omitting the stoichiometric coefficient in the gravimetric factor | Result wrong by the coefficient | Write the formula unit and count the analyte atoms |
| 7 | Using $t_R$ instead of $t_R - t_M$ in $k$ | Selectivity and resolution equations misapplied | Dead time is subtracted first |
| 8 | Mixing $N = 16(t_R/w)^2$ and $N = 5.54(t_R/w_{1/2})^2$ | Plate number wrong by a factor of 2.9 | Match the width definition to the constant |
| 9 | Reversing the sign in potentiometric pH | pH error of twice the potential difference | pH increases as $E$ decreases for a cation-responsive electrode |
| 10 | Using $\text{mol dm}^{-3}$ in the Randles–Ševčík equation | Peak current $10^{3}$ times too large | Convert to $\text{mol cm}^{-3}$ before substituting |

