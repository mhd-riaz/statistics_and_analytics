<p align="left">
  <a href="./standardization.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./estimation-and-confidence.md"><b>Next →</b></a>
  </span>
</p>

---

```
Sampling & Central Limit Theorem
├── 4. Sampling Mean
│   ├── Population vs Sample Mean
│   ├── Unbiased Estimator Property
│   └── Formula: x̄ = Σxᵢ / n
│
├── 5. Sampling Distribution
│   ├── Concept: Distribution of Sample Means
│   ├── Standard Error: SE = σ / √n
│   └── Effect of Sample Size on Spread
│
└── 6. Central Limit Theorem (CLT)
    ├── Core Idea: Sample Means → Normal
    ├── Conditions: n ≥ 30 Rule of Thumb
    ├── CLT Z-Score Formula
    └── Probability Calculations with CLT
```

---

## Sampling & Central Limit Theorem

This file covers the journey from computing a single sample average to understanding how those averages behave when sampling is repeated many times. The **Sampling Mean** (Section 4) shows how to compute a point estimate; the **Sampling Distribution** (Section 5) describes the pattern those estimates form; and the **Central Limit Theorem** (Section 6) explains why that pattern is always approximately normal — the key insight that makes most of inferential statistics possible.

---

### 4. Sampling Mean

The **Sampling Mean** (also called the **Sample Mean**) is the **average** of a subset drawn from a larger population. When you cannot measure every member of a population, you draw a random sample, compute its mean, and use that value as your best estimate of the true population mean $\mu$.

The sample mean is an **unbiased estimator**: if you could repeat the sampling process infinitely, the long-run average of all those sample means would equal $\mu$ exactly — it neither systematically overshoots nor undershoots.

```
Population (all N items):
┌─────────────────────────────────────┐
│  3  7  5  2  9  4  6  8  1  5  ...  │  True average (μ) = ???
│  6  4  7  3  8  5  2  9  4  7  ...  │
│ ...                             ... │
└─────────────────────────────────────┘
                  │
          Pick n items randomly
                  ▼
Sample:  [3, 7, 5, 2, 9, 4, 6, 8, 1, 5]

Sample Mean (x̄) = (3+7+5+2+9+4+6+8+1+5) / 10 = 5.0

x̄ = 5.0 is our BEST GUESS for the true average μ
```

| Notation        |  Symbol   | Pronunciation | Refers To                               |
| :-------------- | :-------: | :------------ | :-------------------------------------- |
| Population mean |   $\mu$   | "mew"         | Average of **all** $N$ items            |
| Sample mean     | $\bar{x}$ | "x bar"       | Average of the **sampled** $n$ items    |
| Population size |    $N$    | "big N"       | Total number of items in the population |
| Sample size     |    $n$    | "little n"    | Number of items drawn into the sample   |

#### Real-World Use Cases

- **Farming**: A farmer weighs a random sample of 20 apples to estimate the average weight of the entire harvest.
- **Healthcare**: Doctors measure blood pressure in a patient sample to estimate the community average.
- **Education**: A school surveys 30 students to estimate the average satisfaction score campus-wide.
- **Advantage**: The sample mean is **unbiased** — on average, it equals $\mu$.
- **Limitation**: Any single sample mean is just one estimate. It can be too high or too low; larger samples reduce this uncertainty.

#### Steps

1. Select a **random sample** of $n$ items from the population.
2. **Sum** all observed values.
3. **Divide** the sum by $n$.
4. The result $\bar{x}$ is the sample mean — your best point estimate for $\mu$.

#### Formula

$$
\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
$$

Where:

|      Symbol      | Pronunciation                  | Meaning                                   |
| :--------------: | :----------------------------- | :---------------------------------------- |
|    $\bar{x}$     | "x bar"                        | The sample mean (average of the sample)   |
| $\sum_{i=1}^{n}$ | "the sum from i equals 1 to n" | Add up all values from first to last      |
|      $x_i$       | "x sub i"                      | The $i$-th individual value in the sample |
|       $n$        | "n"                            | Total number of values in the sample      |

- _Population Mean ($\mu$)_: The true average of the entire population — usually **unknown** and what we aim to estimate.
- _Unbiased Estimator_: The sample mean does not systematically over- or under-estimate $\mu$.
- _Representative Sample_: For $\bar{x}$ to be useful, every population member must have an equal chance of being selected.

#### Examples

---

##### Example 1 — Counting Candy per Bag

You buy 6 bags of candy and count the pieces in each: **12, 14, 10, 13, 15, 14**. What is the average number of candies per bag?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Dataset $= \{12, 14, 10, 13, 15, 14\}$ | Number of candies in each bag |
> | $n = 6$ | Total number of bags |
> | Find: $\bar{x}$ | The sample mean |

> **Step 1:** Write the formula.
>
> $$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$
>
> **Step 2:** Add up all values.
>
> $$\sum x_i = 12 + 14 + 10 + 13 + 15 + 14 = 78$$
>
> **Step 3:** Divide by $n$.
>
> $$\bar{x} = \frac{78}{6}$$
>
> **Step 4:** Calculate.
>
> $$\boxed{\bar{x} = 13 \text{ candies}}$$
>
> **Interpretation:** On average each bag contains about **13 candies**, which is our best estimate for the true population mean across all bags the company produces.

---

##### Example 2 — Library Page Counts

A librarian picks 8 books at random and records their page counts: **120, 200, 180, 150, 220, 170, 190, 160**. What is the average number of pages?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Dataset $= \{120, 200, 180, 150, 220, 170, 190, 160\}$ | Page counts of sampled books |
> | $n = 8$ | Number of books in the sample |
> | Find: $\bar{x}$ | The sample mean |

> **Step 1:** Write the formula.
>
> $$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$
>
> **Step 2:** Add up all values.
>
> $$\sum x_i = 120 + 200 + 180 + 150 + 220 + 170 + 190 + 160 = 1390$$
>
> **Step 3:** Divide by $n$.
>
> $$\bar{x} = \frac{1390}{8}$$
>
> **Step 4:** Calculate.
>
> $$\boxed{\bar{x} = 173.75 \text{ pages}}$$
>
> **Interpretation:** The sampled books average about **174 pages**, giving the librarian a useful estimate for the entire shelf or section.

---

### 5. Sampling Distribution

A **Sampling Distribution** describes the pattern formed by a statistic (here, the sample mean) when you repeat the sampling process many times. Take a random sample of size $n$, compute $\bar{x}$, put the items back, and repeat. The collection of all those $\bar{x}$ values forms the **sampling distribution of the mean**.

Key properties:

1. **Center** — The mean of the sampling distribution equals the population mean: $\mu_{\bar{x}} = \mu$.
2. **Spread** — The standard deviation of the sampling distribution is called the **Standard Error (SE)**: $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$.
3. **Shape** — As $n$ increases, the sampling distribution becomes more normal (a preview of the CLT in Section 6).

```
Take many samples of size n from the population,
compute x̄ each time, and plot all the x̄ values:

Small samples (n = 5):    Wide, short bell
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
◄────────────────┼────────────────────►
                 μ

Large samples (n = 100):   Narrow, tall bell
                ▄████▄
◄────────────────┼────────────────────►
                 μ

Bigger n → Smaller SE → Narrower curve → More precise estimates!
```

| Property                      |                   Formula                    | Effect of Increasing $n$ |
| :---------------------------- | :------------------------------------------: | :----------------------- |
| Mean of sampling distribution |            $\mu_{\bar{x}} = \mu$             | Stays the same           |
| Standard Error                | $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$ | Decreases (more precise) |
| Shape                         |              Approaches normal               | Becomes more bell-shaped |

#### Real-World Use Cases

- **Polling / Elections**: Pollsters survey ~1,000 people and predict how millions will vote. The sampling distribution justifies this leap.
- **Quality Control**: A factory tests 50 batteries and uses the average lifespan to estimate the production-line average.
- **Medicine**: Researchers test a drug on 200 patients and generalize to the wider population.
- **Key Rule**: The standard error shrinks with $\sqrt{n}$ — quadrupling the sample size halves the SE.
- **Limitation**: Requires random sampling; biased samples produce misleading distributions regardless of size.

#### Steps

1. Identify the population mean $\mu$ and standard deviation $\sigma$.
2. Choose a sample size $n$.
3. Compute the **Standard Error**: $\text{SE} = \frac{\sigma}{\sqrt{n}}$.
4. The sampling distribution of $\bar{x}$ is centered at $\mu$ with spread equal to the SE.
5. Use the SE to judge how far a particular $\bar{x}$ is likely to fall from $\mu$.

#### Formula

$$
\mu_{\bar{x}} = \mu
$$

$$
\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}
$$

Where:

|          Symbol           | Pronunciation       | Meaning                                          |
| :-----------------------: | :------------------ | :----------------------------------------------- |
|      $\mu_{\bar{x}}$      | "mew sub x bar"     | Mean of the sampling distribution (equals $\mu$) |
|    $\sigma_{\bar{x}}$     | "sigma sub x bar"   | Standard Error — spread of the sample means      |
|         $\sigma$          | "sigma"             | Standard deviation of the original population    |
|            $n$            | "n"                 | Number of items in each sample                   |
| $\frac{\sigma}{\sqrt{n}}$ | "sigma over root n" | Formula for the Standard Error                   |

- _Standard Error (SE)_: The standard deviation of the sampling distribution — it measures how much sample means bounce around $\mu$.
- _Law of Large Numbers_: As $n$ grows, any single $\bar{x}$ converges toward $\mu$.

#### Examples

---

##### Example 1 — Jellybean Weights (Standard Error)

A jar of 10,000 jellybeans has mean weight $\mu = 5$ grams and standard deviation $\sigma = 2$ grams. You scoop out 36 jellybeans and find their average weight. What is the standard error?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\mu = 5$ grams | Population mean weight |
> | $\sigma = 2$ grams | Population standard deviation |
> | $n = 36$ | Number of jellybeans per sample |
> | Find: $\sigma_{\bar{x}}$ | The standard error |

> **Step 1:** Write the standard error formula.
>
> $$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$$
>
> **Step 2:** Compute $\sqrt{n}$.
>
> $$\sqrt{36} = 6$$
>
> **Step 3:** Divide $\sigma$ by $\sqrt{n}$.
>
> $$\sigma_{\bar{x}} = \frac{2}{6}$$
>
> **Step 4:** Calculate.
>
> $$\boxed{\sigma_{\bar{x}} = 0.333 \text{ grams}}$$
>
> **Interpretation:** If you repeatedly scooped 36 jellybeans, most sample means would fall within about **0.33 grams** of the true mean of 5 grams.

---

##### Example 2 — Comparing Two Sample Sizes

Using the same jellybean jar ($\mu = 5$, $\sigma = 2$), compare the standard error for $n = 16$ vs $n = 64$.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\sigma = 2$ grams | Population standard deviation |
> | $n_1 = 16$ | Small sample size |
> | $n_2 = 64$ | Large sample size |
> | Find: $\sigma_{\bar{x}}$ for each | Compare standard errors |

> **Step 1:** Standard error for $n_1 = 16$.
>
> $$\sigma_{\bar{x}_1} = \frac{2}{\sqrt{16}} = \frac{2}{4} = 0.50 \text{ grams}$$
>
> **Step 2:** Standard error for $n_2 = 64$.
>
> $$\sigma_{\bar{x}_2} = \frac{2}{\sqrt{64}} = \frac{2}{8} = 0.25 \text{ grams}$$
>
> **Step 3:** Compare.
>
> | Sample Size ($n$) | Standard Error ($\sigma_{\bar{x}}$) |
> |:---:|:---:|
> | 16 | 0.50 grams |
> | 64 | 0.25 grams |
>
> $$\boxed{\text{Quadrupling } n \text{ (16 → 64) halves the SE (0.50 → 0.25)}}$$
>
> **Interpretation:** The SE shrinks proportionally to $\sqrt{n}$. To cut the SE in half, you need four times as many observations — a fundamental trade-off in study design.

---

### 6. Central Limit Theorem (CLT)

The **Central Limit Theorem** is the foundational result that connects sample statistics to probability. It states:

> If you take random samples of size $n$ from **any** population with mean $\mu$ and finite standard deviation $\sigma$, the distribution of the sample means $\bar{X}$ approaches a **normal distribution** as $n$ increases — regardless of the shape of the original population.

This is powerful because it means we can use **Z-score methods** and **normal probability tables** for inference about means even when the underlying data is skewed, uniform, or irregularly shaped.

**Rule of thumb:** $n \ge 30$ is generally sufficient. If the population is already normal, smaller samples work fine.

```
Original population (can be ANY shape):

Skewed:       ████
              ██████
              ████████
              ██████████
              ██████████████
◄──────────────────────────────────────►

              │  Take many samples of size n ≥ 30
              │  and compute each sample's mean
              ▼

Sampling Distribution of Means (always approximately normal!):

                    ▄▄▄▄
                 ▄▄██████▄▄
              ▄▄██████████████▄▄
           ▄▄██████████████████████▄▄
◄──────────────────┼──────────────────►
                   μ
             (population mean)
```

**CLT Summary Table:**

| Feature                   | Without CLT               | With CLT ($n \ge 30$)        |
| :------------------------ | :------------------------ | :--------------------------- |
| Population shape required | Must be known / normal    | Any shape                    |
| Distribution of $\bar{X}$ | Unknown                   | $\approx N(\mu, \sigma^2/n)$ |
| Probability calculations  | Difficult or impossible   | Use Z-tables                 |
| Standard Error            | Still $\sigma / \sqrt{n}$ | Still $\sigma / \sqrt{n}$    |

#### Real-World Use Cases

- **A/B Testing**: Product teams compare average conversion rates between two website variants; CLT justifies treating those averages as normally distributed.
- **Manufacturing**: Quality engineers sample 50 batteries and use the mean lifespan to make probability statements about the whole production run.
- **Healthcare**: Researchers estimate average recovery time from a sample and build confidence intervals using the normal approximation.
- **Polling**: Analysts generalize from ~1,000 survey respondents to millions of voters.
- **Limitation**: CLT does **not** fix biased sampling. Non-random or dependent samples can produce misleading results regardless of sample size.

#### Steps

1. Identify the population parameters $\mu$ and $\sigma$.
2. Determine or choose the sample size $n$ (verify $n \ge 30$ or population is normal).
3. Compute the **Standard Error**: $\text{SE} = \frac{\sigma}{\sqrt{n}}$.
4. Model the sample mean: $\bar{X} \approx N\!\left(\mu,\; \frac{\sigma^2}{n}\right)$.
5. Convert a particular $\bar{x}$ to a **Z-score**: $Z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}}$.
6. Use the **standard normal table** to find the required probability.

#### Formula

$$
\bar{X} \approx N\!\left(\mu,\; \frac{\sigma^2}{n}\right), \qquad Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}
$$

Where:

|          Symbol           | Pronunciation          | Meaning                                            |
| :-----------------------: | :--------------------- | :------------------------------------------------- |
|         $\bar{X}$         | "X bar"                | Random variable representing the sample mean       |
|        $\approx N$        | "approximately normal" | Distribution is approximately normal for large $n$ |
|           $\mu$           | "mew"                  | Population mean                                    |
|         $\sigma$          | "sigma"                | Population standard deviation                      |
|            $n$            | "n"                    | Number of observations per sample                  |
|   $\frac{\sigma^2}{n}$    | "sigma squared over n" | Variance of the sampling distribution              |
| $\frac{\sigma}{\sqrt{n}}$ | "sigma over root n"    | Standard error of the sample mean                  |
|            $Z$            | "Z"                    | Standardized score for probability lookup          |

- _Approximate normality_: The sample mean behaves like a normal random variable when CLT conditions are met.
- _Sampling distribution_: The distribution of a statistic over many repeated samples.
- _Standard error_: The standard deviation of the sampling distribution — quantifies precision of the sample mean.

#### Examples

---

##### Example 1 — Skewed Wait Times (Probability of High Mean)

Customer support wait times are strongly right-skewed with $\mu = 18$ minutes and $\sigma = 9$ minutes. A manager samples $n = 36$ calls. What is the probability the sample mean exceeds 20 minutes?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\mu = 18$ minutes | Population mean wait time |
> | $\sigma = 9$ minutes | Population standard deviation |
> | $n = 36$ | Sample size (≥ 30, so CLT applies) |
> | Find: $P(\bar{X} > 20)$ | Probability sample mean exceeds 20 |

> **Step 1:** Write the CLT Z-score formula.
>
> $$Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}$$
>
> **Step 2:** Compute the standard error.
>
> $$\text{SE} = \frac{9}{\sqrt{36}} = \frac{9}{6} = 1.5$$
>
> **Step 3:** Compute $Z$ for $\bar{X} = 20$.
>
> $$Z = \frac{20 - 18}{1.5} = \frac{2}{1.5} \approx 1.33$$
>
> **Step 4:** Look up $P(Z > 1.33)$ in the standard normal table.
>
> $$P(Z > 1.33) \approx 0.0918$$
>
> **Step 5:** State the answer.
>
> $$\boxed{P(\bar{X} > 20) \approx 0.0918 \approx 9.2\%}$$
>
> **Interpretation:** There is about a **9.2% chance** the sample mean exceeds 20 minutes. Even though wait times are skewed, CLT lets us use normal probability because $n = 36 \ge 30$.

---

##### Example 2 — Snack Factory Fill Weight (Probability of Range)

A snack factory fills packets with $\mu = 50$ grams and $\sigma = 8$ grams. A quality inspector samples $n = 64$ packets. What is the probability the sample mean is between 48 and 52 grams?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\mu = 50$ grams | Population mean fill weight |
> | $\sigma = 8$ grams | Population standard deviation |
> | $n = 64$ | Sample size |
> | Find: $P(48 < \bar{X} < 52)$ | Probability sample mean is in the range |

> **Step 1:** Compute the standard error.
>
> $$\text{SE} = \frac{8}{\sqrt{64}} = \frac{8}{8} = 1$$
>
> **Step 2:** Convert both bounds to Z-scores.
>
> $$Z_{48} = \frac{48 - 50}{1} = -2 \qquad Z_{52} = \frac{52 - 50}{1} = 2$$
>
> **Step 3:** Look up $P(-2 < Z < 2)$ in the standard normal table.
>
> $$P(-2 < Z < 2) \approx 0.9545$$
>
> **Step 4:** State the answer.
>
> $$\boxed{P(48 < \bar{X} < 52) \approx 0.9545 \approx 95.5\%}$$
>
> **Interpretation:** There is about a **95.5% chance** the sample mean falls between 48 and 52 grams. The narrow SE of 1 gram (from a large sample) makes it very likely the sample mean stays close to $\mu = 50$.

---

<p align="left">
  <a href="./standardization.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./estimation-and-confidence.md"><b>Next →</b></a>
  </span>
</p>
