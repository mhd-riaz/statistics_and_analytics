<p align="left">
  <a href="./sampling-and-clt.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./hypothesis-testing.md"><b>Next →</b></a>
  </span>
</p>

---

## Estimation & Confidence

This section covers how we move from a sample to making claims about the population — starting with a single best guess (point estimate), expanding it into a range (confidence interval), and understanding the trade-off between confidence and risk (significance level).

```
Estimation & Confidence
├── 7. Point Estimates
│   ├── Sample Mean (x̄)
│   ├── Sample Proportion (p̂)
│   └── Key Terminology (Parameter, Statistic, Estimator, Estimate)
│
├── 8. Interval Estimates (Confidence Intervals)
│   ├── CI Formula: x̄ ± Z × σ/√n
│   ├── Common Z-Scores (90%, 95%, 99%)
│   ├── Margin of Error
│   └── Standard Error vs Critical Value
│
└── 9. Confidence & Significance Levels
    ├── Confidence Level (C)
    ├── Significance Level (α)
    ├── Relationship: C = 1 − α
    └── Type I Error Connection
```

---

### 7. Point Estimates

A **point estimate** is a single number (a "best guess") calculated from sample data to estimate an unknown population parameter. It's the simplest form of estimation — one value that represents the whole population.

Think of it like throwing a **single dart** at a dartboard. Your dart lands at one specific point — that's your point estimate. It might hit the bullseye (the true population value), or it might be close but slightly off.

```
Population (unknown true value)
┌───────────────────────────────────┐
│                                   │
│          μ = ???                   │
│          p = ???                   │
│                                   │
└──────────────┬────────────────────┘
               │
               │  Take a sample
               ▼
┌───────────────────────────────────┐
│         Sample Data               │
│    {x₁, x₂, x₃, ..., xₙ}       │
└──────────────┬────────────────────┘
               │
               │  Calculate
               ▼
┌───────────────────────────────────┐
│       Point Estimate              │
│    x̄  (estimates μ)              │
│    p̂  (estimates p)              │
└───────────────────────────────────┘
```

There are **two main types** of point estimates:

| Type                  |  Symbol   |      What It Estimates      | Formula                        |
| :-------------------- | :-------: | :-------------------------: | :----------------------------- |
| **Sample Mean**       | $\bar{x}$ |   Population mean ($\mu$)   | $\bar{x} = \frac{\sum x_i}{n}$ |
| **Sample Proportion** | $\hat{p}$ | Population proportion ($p$) | $\hat{p} = \frac{x}{n}$        |

#### Real-World Use Cases

- **Polls & Surveys**: Before an election, pollsters survey 1,000 voters and compute $\hat{p}$ to estimate the proportion of the entire population that supports a candidate.
- **Agriculture**: A farmer weighs 20 apples from an orchard and uses $\bar{x}$ to estimate the average weight of all apples produced.
- **Business / Inventory**: A factory samples 50 light bulbs to estimate the average lifespan ($\bar{x}$) of all bulbs manufactured.
- **Limitation**: A single number gives no indication of how _accurate_ the estimate might be — that's why we also need interval estimates (Section 8).

#### Steps

1. Identify the **population parameter** you want to estimate ($\mu$ or $p$).
2. Collect a **random sample** of size $n$ from the population.
3. Apply the appropriate formula:
   - For a **mean**: sum all values and divide by $n$.
   - For a **proportion**: count the successes ($x$) and divide by $n$.
4. Report the point estimate as your best single-number guess.

#### Formula — Sample Mean

$$
\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
$$

Where:

|      Symbol      | Pronunciation                  | Meaning                                                       |
| :--------------: | :----------------------------- | :------------------------------------------------------------ |
|    $\bar{x}$     | "x bar"                        | The sample mean — point estimate of the population mean $\mu$ |
| $\sum_{i=1}^{n}$ | "the sum from i equals 1 to n" | Add up all values from first to last                          |
|      $x_i$       | "x sub i"                      | The $i$-th individual value in the sample                     |
|       $n$        | "n"                            | The total number of values in the sample                      |

#### Formula — Sample Proportion

$$
\hat{p} = \frac{x}{n}
$$

Where:

|  Symbol   | Pronunciation | Meaning                                                                  |
| :-------: | :------------ | :----------------------------------------------------------------------- |
| $\hat{p}$ | "p hat"       | The sample proportion — point estimate of the population proportion $p$  |
|    $x$    | "x"           | The number of successes (items with the trait of interest) in the sample |
|    $n$    | "n"           | The total number of items in the sample                                  |
|    $p$    | "p"           | The true (unknown) population proportion                                 |

#### Key Terminology

- _Parameter_: A fixed, usually unknown numerical value that describes the entire **population** (e.g., $\mu$, $p$).
- _Statistic_: A numerical value calculated from **sample** data (e.g., $\bar{x}$, $\hat{p}$). It changes from sample to sample.
- _Estimator_: The **formula or rule** used to calculate a statistic (e.g., $\bar{x} = \frac{\sum x_i}{n}$ is the estimator for $\mu$).
- _Estimate_: The **specific number** you get after plugging in data (e.g., $\bar{x} = 153$ grams).
- _Unbiased Estimator_: An estimator whose expected value equals the true parameter. Both $\bar{x}$ and $\hat{p}$ are unbiased.

#### Examples

---

##### Example 1 — Estimating a Population Mean (Sample Mean)

A farmer randomly picks 5 apples from his orchard and weighs them. The weights (in grams) are: 150, 160, 145, 155, 155. Estimate the average weight of all apples in the orchard.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Dataset $= \{150, 160, 145, 155, 155\}$ | The weights of the 5 sampled apples (grams) |
> | $n = 5$ | Total number of apples in the sample |
> | Find: $\bar{x}$ | Point estimate of the population mean $\mu$ |

> **Step 1:** Write the formula.
>
> $$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$
>
> **Step 2:** Identify the values.
>
> $x_1 = 150,\ x_2 = 160,\ x_3 = 145,\ x_4 = 155,\ x_5 = 155$
>
> **Step 3:** Substitute into the formula.
>
> $$\bar{x} = \frac{150 + 160 + 145 + 155 + 155}{5}$$
>
> **Step 4:** Simplify the numerator.
>
> $$\bar{x} = \frac{765}{5}$$
>
> **Step 5:** Divide.
>
> $$\boxed{\bar{x} = 153 \text{ grams}}$$
>
> **Interpretation:** Our best single-number estimate for the average weight of _all_ apples in the orchard is **153 grams**.

---

##### Example 2 — Estimating a Population Proportion (Sample Proportion)

A teacher surveys 40 students, asking their favorite color. 18 students say "blue." Estimate the proportion of _all_ students in the school who prefer blue.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $x = 18$ | Number of students who chose blue (successes) |
> | $n = 40$ | Total number of students surveyed |
> | Find: $\hat{p}$ | Point estimate of the population proportion $p$ |

> **Step 1:** Write the formula.
>
> $$\hat{p} = \frac{x}{n}$$
>
> **Step 2:** Substitute the values.
>
> $$\hat{p} = \frac{18}{40}$$
>
> **Step 3:** Calculate.
>
> $$\boxed{\hat{p} = 0.45 = 45\%}$$
>
> **Interpretation:** Our best estimate is that **45%** of all students in the school prefer blue. Note this is a proportion (not a mean) — we're estimating how common a trait is, not an average quantity.

---

### 8. Interval Estimates (Confidence Intervals)

A **confidence interval (CI)** is a _range of values_ (not just a single number) that is likely to contain the true population parameter. It extends the point estimate by adding a **margin of error** on both sides.

If a point estimate is like throwing a single dart, a confidence interval is like drawing a **circle around the bullseye** — you're saying, _"I believe the true value is somewhere inside this circle."_

```
Point Estimate (single dart):

◄──────────────────●──────────────────►
                   x̄
     "My best guess is exactly here."


Interval Estimate (circle around the bullseye):

◄─────────[────────●────────]─────────►
        Lower      x̄      Upper
        Bound             Bound
  "I'm 95% sure the true value is in this range."
```

The **width** of the interval depends on the confidence level you choose:

```
90% CI:       [─────────●─────────]           Narrower (less sure)
95% CI:    [────────────●────────────]        Medium
99% CI: [───────────────●───────────────]     Wider (more sure)
◄───────────────────────●───────────────────────►
                        x̄

Higher confidence = Wider interval = Less precise
Lower confidence  = Narrower interval = More precise
```

#### Real-World Use Cases

- **Medicine**: "We are 95% confident that the new drug reduces blood pressure by 5 to 12 mmHg" — enables doctors to assess both effectiveness and uncertainty.
- **Manufacturing**: Quality engineers compute 99% CIs for product dimensions to ensure nearly all items fall within tolerance.
- **Political Polling**: "Candidate A has 52% support ± 3%" means the 95% CI is [49%, 55%].
- **Advantage over Point Estimates**: A CI communicates _how precise_ the estimate is — a narrow interval means high precision, a wide one means high uncertainty.
- **Trade-off**: Higher confidence levels produce wider (less precise) intervals. There's always a tension between certainty and precision.

#### Steps

1. Collect a random sample of size $n$ from the population.
2. Calculate the sample mean $\bar{x}$ (point estimate).
3. Determine the population standard deviation $\sigma$ (or estimate with $s$).
4. Choose a **confidence level** (e.g., 90%, 95%, 99%).
5. Find the corresponding **critical value** $Z$ from the table below.
6. Compute the **standard error**: $SE = \frac{\sigma}{\sqrt{n}}$.
7. Compute the **margin of error**: $ME = Z \times SE$.
8. Build the interval: $\text{CI} = \bar{x} \pm ME = [\bar{x} - ME,\ \bar{x} + ME]$.

**Common Critical Values (Z-scores):**

| Confidence Level | $\alpha$ | $Z_{\alpha/2}$ |
| :--------------: | :------: | :------------: |
|       90%        |   0.10   |     1.645      |
|       95%        |   0.05   |     1.960      |
|       99%        |   0.01   |     2.576      |

#### Formula

$$
\text{CI} = \bar{x} \pm Z_{\alpha/2} \times \frac{\sigma}{\sqrt{n}}
$$

Equivalently:

$$
\text{Lower Bound} = \bar{x} - Z_{\alpha/2} \times \frac{\sigma}{\sqrt{n}}
$$

$$
\text{Upper Bound} = \bar{x} + Z_{\alpha/2} \times \frac{\sigma}{\sqrt{n}}
$$

Where:

|                    Symbol                     | Pronunciation         | Meaning                                                             |
| :-------------------------------------------: | :-------------------- | :------------------------------------------------------------------ |
|                  $\text{CI}$                  | "confidence interval" | The range of values likely to contain the true population parameter |
|                   $\bar{x}$                   | "x bar"               | The sample mean (center of the interval)                            |
|                     $\pm$                     | "plus or minus"       | The interval extends equally above and below $\bar{x}$              |
|                $Z_{\alpha/2}$                 | "z alpha over two"    | The critical value — how many standard errors to go from the center |
|                   $\sigma$                    | "sigma"               | The population standard deviation                                   |
|                      $n$                      | "n"                   | The sample size                                                     |
|           $\frac{\sigma}{\sqrt{n}}$           | "sigma over root n"   | The standard error (SE) of the sampling distribution                |
| $Z_{\alpha/2} \times \frac{\sigma}{\sqrt{n}}$ | —                     | The margin of error (ME)                                            |

#### Key Terminology

- _Confidence Level ($C$)_: The probability that the interval contains the true parameter (e.g., 95%). See Section 9 for details.
- _Margin of Error (ME)_: The "± part" — how far the interval extends from the point estimate. $ME = Z_{\alpha/2} \times \frac{\sigma}{\sqrt{n}}$.
- _Standard Error (SE)_: A measure of how much the sample mean varies from sample to sample. $SE = \frac{\sigma}{\sqrt{n}}$.
- _Critical Value ($Z_{\alpha/2}$)_: The number of standard errors from the center to the edge of the confidence interval. Larger $Z$ → wider interval → higher confidence.

#### Examples

---

##### Example 1 — 95% Confidence Interval for Heights

A researcher measures the heights of 36 randomly selected 5th graders. The sample mean height is $\bar{x} = 140$ cm. The population standard deviation is known to be $\sigma = 12$ cm. Construct a **95% confidence interval** for the true mean height.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\bar{x} = 140$ cm | Sample mean height |
> | $\sigma = 12$ cm | Population standard deviation |
> | $n = 36$ | Sample size |
> | Confidence Level $= 95\%$ | Chosen confidence level |
> | $Z_{0.025} = 1.960$ | Critical value for 95% CI |
> | Find: CI | The 95% confidence interval for $\mu$ |

> **Step 1:** Write the formula.
>
> $$\text{CI} = \bar{x} \pm Z_{\alpha/2} \times \frac{\sigma}{\sqrt{n}}$$
>
> **Step 2:** Calculate the standard error.
>
> $$SE = \frac{\sigma}{\sqrt{n}} = \frac{12}{\sqrt{36}} = \frac{12}{6} = 2$$
>
> **Step 3:** Calculate the margin of error.
>
> $$ME = Z_{\alpha/2} \times SE = 1.960 \times 2 = 3.92$$
>
> **Step 4:** Compute the lower bound.
>
> $$\text{Lower} = \bar{x} - ME = 140 - 3.92 = 136.08$$
>
> **Step 5:** Compute the upper bound.
>
> $$\text{Upper} = \bar{x} + ME = 140 + 3.92 = 143.92$$
>
> **Step 6:** State the confidence interval.
>
> $$\boxed{\text{CI} = [136.08,\ 143.92] \text{ cm}}$$
>
> **Interpretation:** We are **95% confident** that the true mean height of all 5th graders is between **136.08 cm** and **143.92 cm**.

---

##### Example 2 — 99% Confidence Interval for Quiz Times

A teacher wants to estimate the average time students take to complete a quiz. She samples 64 students and finds $\bar{x} = 45$ seconds. The population standard deviation is $\sigma = 8$ seconds. Construct a **99% confidence interval**.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\bar{x} = 45$ seconds | Sample mean completion time |
> | $\sigma = 8$ seconds | Population standard deviation |
> | $n = 64$ | Sample size |
> | Confidence Level $= 99\%$ | Chosen confidence level |
> | $Z_{0.005} = 2.576$ | Critical value for 99% CI |
> | Find: CI | The 99% confidence interval for $\mu$ |

> **Step 1:** Write the formula.
>
> $$\text{CI} = \bar{x} \pm Z_{\alpha/2} \times \frac{\sigma}{\sqrt{n}}$$
>
> **Step 2:** Calculate the standard error.
>
> $$SE = \frac{\sigma}{\sqrt{n}} = \frac{8}{\sqrt{64}} = \frac{8}{8} = 1$$
>
> **Step 3:** Calculate the margin of error.
>
> $$ME = Z_{\alpha/2} \times SE = 2.576 \times 1 = 2.576$$
>
> **Step 4:** Compute the lower bound.
>
> $$\text{Lower} = \bar{x} - ME = 45 - 2.576 = 42.424$$
>
> **Step 5:** Compute the upper bound.
>
> $$\text{Upper} = \bar{x} + ME = 45 + 2.576 = 47.576$$
>
> **Step 6:** State the confidence interval.
>
> $$\boxed{\text{CI} = [42.42,\ 47.58] \text{ seconds}}$$
>
> **Interpretation:** We are **99% confident** that the true mean quiz completion time is between **42.42 seconds** and **47.58 seconds**. Notice this 99% CI is wider than a 95% CI would be — more confidence requires a wider interval.

---

### 9. Confidence & Significance Levels

The **confidence level** and **significance level** are two sides of the same coin. They always add up to **1** (or 100%).

- **Confidence Level ($C$)**: How sure you are that your interval contains the true parameter. _"I'm 95% confident"_ means 95 out of 100 times, the method produces an interval that captures the true value.
- **Significance Level ($\alpha$)**: How much risk of being wrong you're willing to accept. If $C = 95\%$, then $\alpha = 5\%$ — you accept a 5% chance of a false positive.

Think of it as stepping stones across a river:
- The **Confidence Level** is the percentage of stones that are _safe_ to step on.
- The **Significance Level** is the percentage of stones that are _wobbly_ and might make you fall.
- If 95% of stones are safe, then 5% are wobbly. Together: $95\% + 5\% = 100\%$.

```
The Confidence Level and Significance Level together = 100%

┌──────────────────────────────────────────────────────┐
│                                                      │
│     α/2          Confidence Level (C)        α/2     │
│   ┌─────┐  ┌─────────────────────────┐  ┌─────┐     │
│   │/////│  │                         │  │/////│     │
│   │/////│  │       95% safe zone     │  │/////│     │
│   │/////│  │                         │  │/////│     │
│   └─────┘  └─────────────────────────┘  └─────┘     │
│    2.5%              95%                  2.5%       │
│                                                      │
│                  α = 5% total                        │
│           (split into two tails)                     │
└──────────────────────────────────────────────────────┘
```

```
  Quick Reference:

  Confidence Level    Significance Level (α)    How sure?
  ─────────────────   ──────────────────────    ─────────
       90%                  0.10 (10%)          Pretty sure
       95%                  0.05  (5%)          Very sure
       99%                  0.01  (1%)          Extremely sure
```

#### Real-World Use Cases

- **Science Experiments**: Scientists typically set $\alpha = 0.05$ _before_ running an experiment, accepting a 5% risk of a false positive.
- **Medicine**: Drug trials often use 99% confidence ($\alpha = 0.01$) because the stakes are very high — a mistake could harm patients.
- **Key Rule**: You _choose_ the significance level **before** you run your experiment, not after!
- **Trade-off**: Higher confidence (like 99%) means you're less likely to make a Type I error, but you might also miss real discoveries because your bar is set so high.

#### Steps

1. **Choose** a confidence level $C$ (e.g., 90%, 95%, or 99%).
2. **Calculate** the significance level: $\alpha = 1 - C$.
3. **Interpret** the confidence level: "I am $C\%$ sure my result is correct."
4. **Interpret** the significance level: "I accept an $\alpha\%$ risk of being wrong."

Or, if given $\alpha$:

1. **Calculate** the confidence level: $C = 1 - \alpha$.

#### Formula

$$
C = 1 - \alpha
$$

$$
\alpha = 1 - C
$$

Where:

|  Symbol  | Pronunciation             | Meaning                                                                                 |
| :------: | :------------------------ | :-------------------------------------------------------------------------------------- |
|   $C$    | "C" or "confidence level" | The probability that your method gives a correct result (e.g., 0.95 or 95%)             |
| $\alpha$ | "alpha"                   | The significance level — the risk of a false positive / Type I error (e.g., 0.05 or 5%) |
|   $1$    | "one"                     | Represents 100% — total certainty                                                       |

**Comparison Table:**

| Feature               | Confidence Level ($C$)     | Significance Level ($\alpha$)         |
| :-------------------- | :------------------------- | :------------------------------------ |
| **What it measures**  | How sure you are           | How much risk you accept              |
| **Typical values**    | 90%, 95%, 99%              | 0.10, 0.05, 0.01                      |
| **Where it's used**   | Confidence Intervals       | Hypothesis Testing                    |
| **On the bell curve** | The big area in the middle | The small areas in the tails          |
| **Interpretation**    | "I am 95% confident"       | "I accept a 5% chance of being wrong" |

#### Key Terminology

- _Null Hypothesis ($H_0$)_: The default assumption that nothing special is happening (e.g., "this treatment has no effect"). Hypothesis testing decides whether to reject this.
- _Type I Error (False Positive)_: Concluding "something is happening!" when it's actually just random chance. The significance level $\alpha$ is exactly the risk of making this mistake.
- _Type II Error (False Negative)_: Concluding "nothing is happening" when something actually _is_. Controlled by a separate concept called _power_.
- _Critical Region_: The "danger zone" in the tails of the bell curve. If your test statistic falls here, you reject $H_0$.

#### Examples

---

##### Example 1 — From Confidence Level to Significance Level

You're doing a science fair project testing whether plants grow taller with music. You decide to be **95% confident** in your results. What is your significance level?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $C = 0.95$ | The chosen confidence level (95%) |
> | Find: $\alpha$ | The significance level |

> **Step 1:** Write the formula.
>
> $$\alpha = 1 - C$$
>
> **Step 2:** Plug in the confidence level.
>
> $$\alpha = 1 - 0.95$$
>
> **Step 3:** Calculate.
>
> $$\boxed{\alpha = 0.05 = 5\%}$$
>
> **Interpretation:** You are accepting a **5% risk** of incorrectly concluding that music helps plant growth when it actually doesn't. In other words, 5 times out of 100, you _might_ be fooled by random luck.

---

##### Example 2 — From Significance Level to Confidence Level

A doctor is testing a new medicine. Because this affects people's health, the doctor sets a very strict significance level of $\alpha = 0.01$. What is the confidence level?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\alpha = 0.01$ | The chosen significance level (1%) |
> | Find: $C$ | The confidence level |

> **Step 1:** Write the formula.
>
> $$C = 1 - \alpha$$
>
> **Step 2:** Plug in the significance level.
>
> $$C = 1 - 0.01$$
>
> **Step 3:** Calculate.
>
> $$\boxed{C = 0.99 = 99\%}$$
>
> **Interpretation:** The doctor is **99% confident** in the results. They only accept a tiny **1% risk** of being wrong — critical in medicine where decisions affect patient safety.

---

<p align="left">
  <a href="./sampling-and-clt.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./hypothesis-testing.md"><b>Next →</b></a>
  </span>
</p>
