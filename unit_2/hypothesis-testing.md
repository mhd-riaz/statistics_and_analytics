<p align="left">
  <a href="./estimation-and-confidence.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./anova.md"><b>Next →</b></a>
  </span>
</p>

---

## Hypothesis Testing

Hypothesis testing is a formal statistical procedure for making decisions about population parameters based on sample data. Instead of estimating a value (like confidence intervals do), hypothesis testing asks: _"Is there enough evidence to reject a claim about the population?"_

```
Hypothesis Testing
├── 10. Fundamentals of Hypothesis Testing
│   ├── Null & Alternative Hypotheses (H₀, H₁)
│   ├── Test Statistic
│   ├── P-Value
│   ├── Decision Rule (Reject or Fail to Reject)
│   ├── Type I & Type II Errors
│   └── One-Tailed vs Two-Tailed Tests
│
├── 11. Parametric Tests
│   ├── Z-Test (known σ, large n)
│   ├── One-Sample t-Test (unknown σ, small n)
│   └── When to Use Z vs t
│
└── 12. Non-Parametric Tests
    ├── Chi-Square Goodness-of-Fit Test
    ├── Mann-Whitney U Test
    └── Parametric vs Non-Parametric Comparison
```

---

### 10. Fundamentals of Hypothesis Testing

**Hypothesis testing** is a structured method to decide whether sample data provides sufficient evidence against a claim about the population. You start with a default assumption (null hypothesis), collect data, and determine whether the data is unusual enough to reject that assumption.

Think of it like a **courtroom trial**:
- The defendant is **assumed innocent** until proven guilty (that's $H_0$).
- The prosecution presents **evidence** (that's the sample data).
- The jury decides: is the evidence strong enough to declare guilty (reject $H_0$), or is there reasonable doubt (fail to reject $H_0$)?

```
  Hypothesis Testing as a Courtroom Trial

  ┌──────────────────────────────────────────────────┐
  │              H₀: Innocent (default)              │
  │              H₁: Guilty (alternative)            │
  ├──────────────────────────────────────────────────┤
  │                                                  │
  │   Collect Evidence (sample data)                 │
  │            │                                     │
  │            ▼                                     │
  │   Calculate Test Statistic                       │
  │            │                                     │
  │            ▼                                     │
  │   Compare to Critical Value or compute p-value   │
  │            │                                     │
  │       ┌────┴────┐                                │
  │       ▼         ▼                                │
  │   p ≤ α       p > α                             │
  │  Reject H₀   Fail to Reject H₀                  │
  │  ("Guilty")  ("Not enough evidence")             │
  └──────────────────────────────────────────────────┘
```

**Key components:**

| Component                  |       Symbol       | What It Is                                                                             |
| :------------------------- | :----------------: | :------------------------------------------------------------------------------------- |
| **Null Hypothesis**        |       $H_0$        | The default claim — "nothing is happening" or "no difference"                          |
| **Alternative Hypothesis** |  $H_1$ (or $H_a$)  | The opposing claim you want to test — "there IS an effect"                             |
| **Test Statistic**         | $Z$, $t$, $\chi^2$ | A number computed from sample data that measures how far the data is from $H_0$        |
| **P-value**                |        $p$         | The probability of observing data at least as extreme as yours, assuming $H_0$ is true |
| **Significance Level**     |      $\alpha$      | The threshold for "unusual enough" — typically 0.05                                    |
| **Decision**               |         —          | Reject $H_0$ if $p \leq \alpha$; fail to reject if $p > \alpha$                        |

**One-Tailed vs Two-Tailed Tests:**

```
  Two-Tailed Test (H₁: μ ≠ μ₀)         One-Tailed Test (H₁: μ > μ₀)

      Reject │           │ Reject            │                   │Reject
      ┌───┐  │           │  ┌───┐            │                   │ ┌───┐
      │///│  │           │  │///│            │                   │ │///│
  ────┴───┴──┴───────────┴──┴───┴──      ───┴───────────────────┴─┴───┴──
      α/2        1 − α       α/2                  1 − α              α
```

| Test Type    | $H_1$            | Rejection Region | When to Use                                     |
| :----------- | :--------------- | :--------------- | :---------------------------------------------- |
| Two-tailed   | $\mu \neq \mu_0$ | Both tails       | You care about any difference (higher OR lower) |
| Right-tailed | $\mu > \mu_0$    | Right tail only  | You only care if the value is _greater_         |
| Left-tailed  | $\mu < \mu_0$    | Left tail only   | You only care if the value is _less_            |

**Type I and Type II Errors:**

|                          |          $H_0$ is actually TRUE          |         $H_0$ is actually FALSE          |
| :----------------------- | :--------------------------------------: | :--------------------------------------: |
| **Reject $H_0$**         | Type I Error ($\alpha$) — False Positive |  Correct Decision (Power = $1 - \beta$)  |
| **Fail to Reject $H_0$** |             Correct Decision             | Type II Error ($\beta$) — False Negative |

- _Type I Error_: Rejecting $H_0$ when it's actually true (false alarm). Probability = $\alpha$.
- _Type II Error_: Failing to reject $H_0$ when it's actually false (missed detection). Probability = $\beta$.
- _Power_: The probability of correctly rejecting a false $H_0$. Power $= 1 - \beta$.

#### Real-World Use Cases

- **Medicine**: Testing whether a new drug lowers blood pressure more than a placebo ($H_0$: no difference, $H_1$: drug is better).
- **Manufacturing**: Checking if a machine's output has drifted from specification ($H_0$: mean = target, $H_1$: mean ≠ target).
- **Education**: Determining if a new teaching method improves test scores ($H_0$: no improvement, $H_1$: scores are higher).
- **Key Warning**: "Fail to reject $H_0$" does NOT mean $H_0$ is true — it means there isn't enough evidence against it. Just like "not guilty" doesn't mean "innocent."

#### Steps

1. State the **null hypothesis** $H_0$ and **alternative hypothesis** $H_1$.
2. Choose the **significance level** $\alpha$ (typically 0.05).
3. Select the appropriate **test** (Z-test, t-test, etc.) based on the data.
4. Compute the **test statistic** from the sample data.
5. Find the **p-value** (or compare to critical value).
6. **Decide**: If $p \leq \alpha$, reject $H_0$. If $p > \alpha$, fail to reject $H_0$.
7. **Interpret** the result in context.

#### Formula — General Test Statistic Structure

$$
\text{Test Statistic} = \frac{\text{Sample Statistic} - \text{Hypothesized Value}}{\text{Standard Error}}
$$

This general form applies to both Z-tests and t-tests:

|       Symbol       | Pronunciation | Meaning                                                                 |
| :----------------: | :------------ | :---------------------------------------------------------------------- |
|  Sample Statistic  | —             | The value computed from your sample (e.g., $\bar{x}$)                   |
| Hypothesized Value | —             | The value claimed by $H_0$ (e.g., $\mu_0$)                              |
|   Standard Error   | —             | A measure of how much the sample statistic varies from sample to sample |

#### Examples

---

##### Example 1 — Setting Up a Two-Tailed Test

A bottling company claims their bottles contain an average of $\mu_0 = 500$ mL. A quality inspector suspects the machines may have drifted (could be overfilling OR underfilling). She samples 40 bottles and finds $\bar{x} = 497$ mL with $\sigma = 10$ mL. Test at $\alpha = 0.05$.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\mu_0 = 500$ mL | The claimed population mean (from $H_0$) |
> | $\bar{x} = 497$ mL | The sample mean |
> | $\sigma = 10$ mL | The population standard deviation |
> | $n = 40$ | Sample size |
> | $\alpha = 0.05$ | Significance level |
> | Find: Reject or fail to reject $H_0$? | Decision |

> **Step 1:** State the hypotheses.
>
> $$H_0: \mu = 500 \quad \text{(bottles are on target)}$$
> $$H_1: \mu \neq 500 \quad \text{(bottles have drifted — two-tailed)}$$
>
> **Step 2:** Compute the test statistic (Z-test, since $\sigma$ is known).
>
> $$Z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}} = \frac{497 - 500}{10 / \sqrt{40}} = \frac{-3}{1.581} = -1.897$$
>
> **Step 3:** Find the p-value.
>
> For a two-tailed test: $p = 2 \times P(Z < -1.897)$.
> From the Z-table: $P(Z < -1.897) \approx 0.0289$.
>
> $$p = 2 \times 0.0289 = 0.0578$$
>
> **Step 4:** Compare p-value to $\alpha$.
>
> $$p = 0.0578 > \alpha = 0.05$$
>
> **Step 5:** Decision.
>
> $$\boxed{\text{Fail to reject } H_0}$$
>
> **Interpretation:** At the 5% significance level, there is **not enough evidence** to conclude that the bottling machines have drifted from 500 mL. The sample mean of 497 mL _could_ be due to random sampling variation.

---

##### Example 2 — Setting Up a One-Tailed Test

A school principal claims the average math score is at least $\mu_0 = 75$. A parent group suspects it's lower. They sample 25 students: $\bar{x} = 72$, $s = 8$. Test at $\alpha = 0.05$ using a t-test (since $\sigma$ is unknown and $n < 30$).

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\mu_0 = 75$ | The claimed population mean ($H_0$) |
> | $\bar{x} = 72$ | The sample mean |
> | $s = 8$ | The sample standard deviation |
> | $n = 25$ | Sample size |
> | $df = n - 1 = 24$ | Degrees of freedom |
> | $\alpha = 0.05$ | Significance level |
> | Find: Reject or fail to reject $H_0$? | Decision (left-tailed test) |

> **Step 1:** State the hypotheses.
>
> $$H_0: \mu \geq 75 \quad \text{(scores are at least 75)}$$
> $$H_1: \mu < 75 \quad \text{(scores are lower — left-tailed)}$$
>
> **Step 2:** Compute the test statistic (t-test, since $\sigma$ is unknown).
>
> $$t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} = \frac{72 - 75}{8 / \sqrt{25}} = \frac{-3}{1.6} = -1.875$$
>
> **Step 3:** Find the critical value.
>
> For a left-tailed test with $df = 24$ and $\alpha = 0.05$:
> $t_{\text{critical}} = -1.711$ (from the t-table).
>
> **Step 4:** Compare the test statistic to the critical value.
>
> $$t = -1.875 < t_{\text{critical}} = -1.711$$
>
> The test statistic falls in the rejection region.
>
> **Step 5:** Decision.
>
> $$\boxed{\text{Reject } H_0}$$
>
> **Interpretation:** At the 5% significance level, there **is** sufficient evidence to conclude that the average math score is less than 75. The parent group's concern appears justified.

---

### 11. Parametric Tests

**Parametric tests** are hypothesis tests that assume the population data follows a specific distribution (usually normal). They are powerful when assumptions are met, especially for continuous numerical data.

The two most common parametric tests for means are the **Z-test** and the **t-test**.

```
  Choosing Between Z-Test and t-Test

  Is σ (population std dev) known?
  ├── YES ─── Use Z-Test
  │            Z = (x̄ − μ₀) / (σ / √n)
  │
  └── NO ──── Is n ≥ 30?
              ├── YES ─── Z-Test is acceptable
              │            (s approximates σ for large n)
              │
              └── NO ──── Use t-Test
                           t = (x̄ − μ₀) / (s / √n)
                           df = n − 1
```

**Comparison Table:**

| Feature               | Z-Test                                     | One-Sample t-Test                     |
| :-------------------- | :----------------------------------------- | :------------------------------------ |
| **Population σ**      | Known                                      | Unknown (use $s$)                     |
| **Sample size**       | Any (typically $n \geq 30$)                | Any (especially $n < 30$)             |
| **Distribution used** | Standard Normal ($Z$)                      | Student's $t$ with $df = n-1$         |
| **Tails are**         | Thinner (fixed shape)                      | Heavier (wider, especially small $n$) |
| **Converges to Z**    | —                                          | Yes, as $n \to \infty$                |
| **Assumption**        | Population is normal (or large $n$ by CLT) | Population is approximately normal    |

#### Real-World Use Cases

- **Z-Test**: Quality control in factories where $\sigma$ is known from years of historical data and sample sizes are large.
- **t-Test**: Medical research where $\sigma$ is unknown and sample sizes are small (e.g., 15 patients in a pilot study).
- **Key Guidance**: When in doubt, use the t-test — it's more conservative and reduces to the Z-test for large $n$.

#### Steps — Z-Test for a Population Mean

1. State $H_0: \mu = \mu_0$ and $H_1$ (choose one- or two-tailed).
2. Choose $\alpha$.
3. Compute: $Z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}$.
4. Find the p-value from the standard normal table.
5. If $p \leq \alpha$, reject $H_0$.

#### Steps — One-Sample t-Test

1. State $H_0: \mu = \mu_0$ and $H_1$.
2. Choose $\alpha$.
3. Compute: $t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}$, where $df = n - 1$.
4. Find the p-value from the $t$-distribution table with $df$ degrees of freedom.
5. If $p \leq \alpha$, reject $H_0$.

#### Formula — Z-Test

$$
Z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}
$$

Where:

|  Symbol   | Pronunciation | Meaning                                                     |
| :-------: | :------------ | :---------------------------------------------------------- |
|    $Z$    | "z"           | The test statistic (number of standard errors from $\mu_0$) |
| $\bar{x}$ | "x bar"       | The sample mean                                             |
|  $\mu_0$  | "mu naught"   | The hypothesized population mean (from $H_0$)               |
| $\sigma$  | "sigma"       | The known population standard deviation                     |
|    $n$    | "n"           | The sample size                                             |

#### Formula — One-Sample t-Test

$$
t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}, \quad df = n - 1
$$

Where:

|  Symbol   | Pronunciation        | Meaning                                             |
| :-------: | :------------------- | :-------------------------------------------------- |
|    $t$    | "t"                  | The test statistic from the $t$-distribution        |
| $\bar{x}$ | "x bar"              | The sample mean                                     |
|  $\mu_0$  | "mu naught"          | The hypothesized population mean (from $H_0$)       |
|    $s$    | "s"                  | The sample standard deviation (estimates $\sigma$)  |
|    $n$    | "n"                  | The sample size                                     |
|   $df$    | "degrees of freedom" | $n - 1$; controls the shape of the $t$-distribution |

#### Examples

---

##### Example 1 — Z-Test (Known σ, Large Sample)

A cereal company claims their boxes contain $\mu_0 = 368$ grams. A consumer group samples $n = 50$ boxes and finds $\bar{x} = 365$ g. Historical data shows $\sigma = 12$ g. Test at $\alpha = 0.05$ (two-tailed).

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\mu_0 = 368$ g | Claimed mean weight ($H_0$) |
> | $\bar{x} = 365$ g | Sample mean |
> | $\sigma = 12$ g | Known population std dev |
> | $n = 50$ | Sample size |
> | $\alpha = 0.05$ | Significance level (two-tailed) |
> | Find: Reject or fail to reject $H_0$? | |

> **Step 1:** State the hypotheses.
>
> $$H_0: \mu = 368 \qquad H_1: \mu \neq 368$$
>
> **Step 2:** Compute the test statistic.
>
> $$Z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}} = \frac{365 - 368}{12 / \sqrt{50}} = \frac{-3}{1.697} = -1.768$$
>
> **Step 3:** Find the p-value (two-tailed).
>
> $P(Z < -1.768) \approx 0.0385$
>
> $$p = 2 \times 0.0385 = 0.0770$$
>
> **Step 4:** Compare to $\alpha$.
>
> $$p = 0.0770 > \alpha = 0.05$$
>
> **Step 5:** Decision.
>
> $$\boxed{\text{Fail to reject } H_0}$$
>
> **Interpretation:** At the 5% significance level, there is not enough evidence to conclude the boxes are under- or overfilled. The observed difference of 3 grams could be due to sampling variability.

---

##### Example 2 — t-Test (Unknown σ, Small Sample)

A coffee shop claims their large cup contains $\mu_0 = 16$ oz. A customer measures $n = 10$ cups and finds $\bar{x} = 15.4$ oz with $s = 0.8$ oz. Test at $\alpha = 0.05$ (left-tailed: is the shop _underfilling_?).

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\mu_0 = 16$ oz | Claimed mean volume ($H_0$) |
> | $\bar{x} = 15.4$ oz | Sample mean |
> | $s = 0.8$ oz | Sample standard deviation |
> | $n = 10$ | Sample size |
> | $df = 10 - 1 = 9$ | Degrees of freedom |
> | $\alpha = 0.05$ | Significance level (left-tailed) |
> | Find: Reject or fail to reject $H_0$? | |

> **Step 1:** State the hypotheses.
>
> $$H_0: \mu \geq 16 \qquad H_1: \mu < 16$$
>
> **Step 2:** Compute the test statistic.
>
> $$t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} = \frac{15.4 - 16}{0.8 / \sqrt{10}} = \frac{-0.6}{0.253} = -2.372$$
>
> **Step 3:** Find the critical value.
>
> For a left-tailed test, $df = 9$, $\alpha = 0.05$:
> $t_{\text{critical}} = -1.833$ (from the t-table).
>
> **Step 4:** Compare.
>
> $$t = -2.372 < t_{\text{critical}} = -1.833$$
>
> The test statistic falls in the rejection region.
>
> **Step 5:** Decision.
>
> $$\boxed{\text{Reject } H_0}$$
>
> **Interpretation:** At the 5% significance level, there **is** sufficient evidence that the coffee shop is underfilling their large cups. The average of 15.4 oz is significantly less than the claimed 16 oz.

---

### 12. Non-Parametric Tests

**Non-parametric tests** are hypothesis tests that do **not** assume the data follows a specific distribution. They are used when:
- Data is **ordinal** (ranked) rather than continuous
- The **normality assumption** is violated
- Sample sizes are **very small**
- Data contains **outliers** that would distort parametric tests

```
  When to Use Non-Parametric Tests

  Is the data normally distributed?
  ├── YES ─── Use parametric test (Z, t, etc.)
  │
  └── NO or UNSURE
      ├── Comparing frequencies/categories? ─── Chi-Square Test
      ├── Comparing 2 independent groups (ordinal/non-normal)? ─── Mann-Whitney U
      └── Comparing paired/related samples? ─── Wilcoxon Signed-Rank
```

**Parametric vs Non-Parametric Comparison:**

| Feature                     | Parametric Tests              | Non-Parametric Tests                      |
| :-------------------------- | :---------------------------- | :---------------------------------------- |
| **Distribution assumption** | Data is normally distributed  | No distribution assumed                   |
| **Data type**               | Continuous (interval/ratio)   | Ordinal, ranked, or non-normal continuous |
| **Central measure**         | Tests the mean ($\mu$)        | Tests the median or distribution shape    |
| **Statistical power**       | Higher (when assumptions met) | Lower (but robust to violations)          |
| **Sensitivity to outliers** | High                          | Low                                       |
| **Examples**                | Z-test, t-test, ANOVA         | Chi-Square, Mann-Whitney U, Wilcoxon      |

#### Real-World Use Cases

- **Customer Satisfaction**: Survey data on a 1–5 Likert scale is ordinal — use Mann-Whitney U to compare two groups, not a t-test.
- **Quality Inspection**: Testing if defect categories (scratch, dent, discoloration) occur equally often — use Chi-Square goodness-of-fit.
- **Medical Research**: Comparing pain levels (mild/moderate/severe) between two treatment groups — use Mann-Whitney U.
- **Key Advantage**: Non-parametric tests work when parametric assumptions fail, making them a "safer" choice for messy real-world data.

#### Formula — Chi-Square Goodness-of-Fit Test

The Chi-Square test checks whether observed frequencies match expected frequencies across categories.

$$
\chi^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i}
$$

Where:

|  Symbol  | Pronunciation        | Meaning                                              |
| :------: | :------------------- | :--------------------------------------------------- |
| $\chi^2$ | "chi squared"        | The test statistic                                   |
|  $O_i$   | "O sub i"            | The observed frequency in category $i$               |
|  $E_i$   | "E sub i"            | The expected frequency in category $i$ (under $H_0$) |
|   $k$    | "k"                  | The number of categories                             |
|   $df$   | "degrees of freedom" | $k - 1$                                              |

#### Steps — Chi-Square Goodness-of-Fit

1. State $H_0$: observed frequencies match expected frequencies (no preference / equal distribution).
2. State $H_1$: observed frequencies differ from expected.
3. Compute expected frequencies $E_i$ for each category (usually $E_i = \frac{N}{k}$ for equal distribution).
4. Compute $\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$.
5. Find the critical value from the $\chi^2$ table with $df = k - 1$.
6. If $\chi^2 \geq \chi^2_{\text{critical}}$, reject $H_0$.

#### Formula — Mann-Whitney U Test

The Mann-Whitney U test compares two independent groups by ranking all observations together.

$$
U = n_1 n_2 + \frac{n_1(n_1 + 1)}{2} - R_1
$$

Where:

| Symbol | Pronunciation | Meaning                          |
| :----: | :------------ | :------------------------------- |
|  $U$   | "U"           | The test statistic               |
| $n_1$  | "n sub one"   | Sample size of group 1           |
| $n_2$  | "n sub two"   | Sample size of group 2           |
| $R_1$  | "R sub one"   | Sum of ranks assigned to group 1 |

#### Steps — Mann-Whitney U Test

1. Combine all observations from both groups and **rank** them from smallest to largest.
2. Sum the ranks for group 1 ($R_1$) and group 2 ($R_2$).
3. Compute $U = n_1 n_2 + \frac{n_1(n_1 + 1)}{2} - R_1$.
4. Compare $U$ to the critical value from the Mann-Whitney U table (or compute a p-value).
5. If $U \leq U_{\text{critical}}$, reject $H_0$.

#### Examples

---

##### Example 1 — Chi-Square Goodness-of-Fit Test

A candy company claims their bags contain **equal proportions** of 4 colors: red, blue, green, yellow. A student counts 200 candies and records:

| Color                |  Red  | Blue  | Green | Yellow |
| :------------------- | :---: | :---: | :---: | :----: |
| **Observed ($O_i$)** |  60   |  45   |  55   |   40   |

Test at $\alpha = 0.05$ whether the distribution is truly equal.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $N = 200$ | Total number of candies |
> | $k = 4$ | Number of categories |
> | $E_i = 200/4 = 50$ | Expected count per color (if equal) |
> | $\alpha = 0.05$ | Significance level |
> | $df = k - 1 = 3$ | Degrees of freedom |
> | $\chi^2_{\text{critical}} = 7.815$ | Critical value for $df=3$, $\alpha=0.05$ |
> | Find: Reject or fail to reject $H_0$? | |

> **Step 1:** State the hypotheses.
>
> $$H_0: \text{All colors are equally distributed (each = 25\%)}$$
> $$H_1: \text{Colors are NOT equally distributed}$$
>
> **Step 2:** Compute the Chi-Square statistic.
>
> | Color | $O_i$ | $E_i$ | $O_i - E_i$ | $(O_i - E_i)^2$ | $\frac{(O_i - E_i)^2}{E_i}$ |
> |:---|:---:|:---:|:---:|:---:|:---:|
> | Red | 60 | 50 | 10 | 100 | 2.00 |
> | Blue | 45 | 50 | −5 | 25 | 0.50 |
> | Green | 55 | 50 | 5 | 25 | 0.50 |
> | Yellow | 40 | 50 | −10 | 100 | 2.00 |
>
> $$\chi^2 = 2.00 + 0.50 + 0.50 + 2.00 = 5.00$$
>
> **Step 3:** Compare to the critical value.
>
> $$\chi^2 = 5.00 < \chi^2_{\text{critical}} = 7.815$$
>
> **Step 4:** Decision.
>
> $$\boxed{\text{Fail to reject } H_0}$$
>
> **Interpretation:** At the 5% significance level, there is **not enough evidence** to conclude that the candy colors are unequally distributed. The observed variation from 50 per color could be due to random chance.

---

##### Example 2 — Mann-Whitney U Test

A researcher wants to test whether two study methods produce different exam scores. Because the data is from small groups and may not be normal, she uses the Mann-Whitney U test.

**Method A** scores: 78, 85, 90, 72, 88 ($n_1 = 5$)
**Method B** scores: 65, 70, 82, 68, 75 ($n_2 = 5$)

Test at $\alpha = 0.05$ (two-tailed).

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Method A: $\{78, 85, 90, 72, 88\}$ | Group 1 scores ($n_1 = 5$) |
> | Method B: $\{65, 70, 82, 68, 75\}$ | Group 2 scores ($n_2 = 5$) |
> | $\alpha = 0.05$ | Significance level (two-tailed) |
> | $U_{\text{critical}} = 2$ | Critical value for $n_1=5, n_2=5$, $\alpha=0.05$ two-tailed |
> | Find: Reject or fail to reject $H_0$? | |

> **Step 1:** State the hypotheses.
>
> $$H_0: \text{The two methods produce the same distribution of scores}$$
> $$H_1: \text{The two methods produce different distributions}$$
>
> **Step 2:** Combine and rank all 10 scores.
>
> | Rank | Score | Group |
> |:---:|:---:|:---|
> | 1 | 65 | B |
> | 2 | 68 | B |
> | 3 | 70 | B |
> | 4 | 72 | A |
> | 5 | 75 | B |
> | 6 | 78 | A |
> | 7 | 82 | B |
> | 8 | 85 | A |
> | 9 | 88 | A |
> | 10 | 90 | A |
>
> **Step 3:** Sum the ranks for each group.
>
> $$R_1 (\text{Method A}) = 4 + 6 + 8 + 9 + 10 = 37$$
> $$R_2 (\text{Method B}) = 1 + 2 + 3 + 5 + 7 = 18$$
>
> **Step 4:** Compute the U statistic.
>
> $$U_1 = n_1 n_2 + \frac{n_1(n_1+1)}{2} - R_1 = (5)(5) + \frac{5(6)}{2} - 37 = 25 + 15 - 37 = 3$$
>
> $$U_2 = n_1 n_2 - U_1 = 25 - 3 = 22$$
>
> Take the smaller: $U = \min(U_1, U_2) = \min(3, 22) = 3$.
>
> **Step 5:** Compare to critical value.
>
> $$U = 3 > U_{\text{critical}} = 2$$
>
> **Step 6:** Decision.
>
> $$\boxed{\text{Fail to reject } H_0}$$
>
> **Interpretation:** At the 5% significance level, there is **not enough evidence** to conclude that the two study methods produce significantly different exam scores. Although Method A scores appear higher on average, the difference is not statistically significant with these small sample sizes.

---

<p align="left">
  <a href="./estimation-and-confidence.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./anova.md"><b>Next →</b></a>
  </span>
</p>
