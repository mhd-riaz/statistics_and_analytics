<p align="left">
  <a href="./sampling-distribution.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./point-estimate.md"><b>Next →</b></a>
  </span>
</p>

---

```
Central Limit Theorem
├── 1. Core Idea
│   ├── Repeated random samples
│   ├── Sample means
│   └── Approximate normal shape
│
├── 2. Conditions
│   ├── Random or independent sampling
│   ├── Large enough sample size
│   └── Finite population variability
│
└── 3. Practical Result
    ├── Center stays at μ
    ├── Spread becomes σ/√n
    └── Z-score methods become usable
```

---

## Central Limit Theorem

### 1. Central Limit Theorem

The **Central Limit Theorem (CLT)** says that if you repeatedly take **random samples** of size $n$ from a population with mean $\mu$ and standard deviation $\sigma$, then the **sample means** will form an approximately **normal distribution** when $n$ is large enough.

The important point is that the theorem is about the **distribution of the sample mean** $\bar{X}$, not about the original population becoming normal. The original data can be skewed, uneven, or messy, but the sample means still settle into a bell-shaped pattern when repeated sampling is done under the right conditions.

In practice, a common rule of thumb is $n \ge 30$, although highly skewed populations may need larger samples and already-normal populations can work with smaller samples.

```
Original population (can be skewed):

  ███████████
  ████████
  ██████
  ████
  ██
  █
  ◄──────────────────────────────►

Take many random samples of size n
and compute one mean from each sample

                ↓

Sampling distribution of the means:

              ▄▄██████▄▄
           ▄▄████████████▄▄
         ▄██████████████████▄
  ◄───────────────┼───────────────►
                  μ
```

#### Real-World Use Cases

- **A/B testing**: Product teams use average conversion metrics from samples to judge whether one variant performs better than another.
- **Manufacturing**: Quality teams inspect sample averages such as bottle fill volume or battery life instead of testing every unit.
- **Healthcare**: Researchers use sample means to estimate average blood pressure, recovery time, or treatment effect in a larger population.
- **Polling and surveys**: Analysts use sample averages and proportions to make statements about large groups without measuring everyone.
- **Limitation**: CLT does not fix bad sampling. If the sample is biased or dependent in the wrong way, the result can still be misleading.

#### Steps

1. Identify the population mean $\mu$, population standard deviation $\sigma$, and sample size $n$.
2. Check that sampling is random or reasonably independent.
3. Verify that the sample size is large enough for the CLT approximation to be reasonable.
4. Compute the standard error using $\frac{\sigma}{\sqrt{n}}$.
5. Model the sample mean with an approximate normal distribution centered at $\mu$.
6. Use a Z-score to find probabilities or judge how unusual a sample mean is.

#### Formula

$$
\bar{X} \approx N\left(\mu, \frac{\sigma^2}{n}\right),
\qquad
Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}
$$

Where:

|          Symbol           | Pronunciation              | Meaning                                                                        |
| :-----------------------: | :------------------------- | :----------------------------------------------------------------------------- |
|         $\bar{X}$         | "X bar"                    | The random variable representing the sample mean                               |
|        $\approx N$        | "approximately normal"     | The sample mean is approximately normally distributed for large enough $n$     |
|           $\mu$           | "mew"                      | The population mean                                                            |
|         $\sigma$          | "sigma"                    | The population standard deviation                                              |
|            $n$            | "n"                        | The number of observations in each sample                                      |
|   $\frac{\sigma^2}{n}$    | "sigma squared over n"     | The variance of the sampling distribution of the mean                          |
| $\frac{\sigma}{\sqrt{n}}$ | "sigma over square root n" | The standard error of the sample mean                                          |
|            $Z$            | "Z"                        | The standardized score used to find probabilities from the normal distribution |

---

- _Sampling distribution_: the distribution formed by a statistic, such as the mean, over many repeated samples.
- _Standard error_: the standard deviation of the sampling distribution.
- _Approximate normality_: the idea that the sample mean behaves like a normal random variable when the CLT conditions are met.

#### Examples

---

##### Example 1 — Skewed Wait Times

Customer support wait times are strongly right-skewed, but they have population mean $\mu = 18$ minutes and standard deviation $\sigma = 9$ minutes. A manager takes a random sample of $n = 36$ calls. What is the probability that the sample mean wait time is more than 20 minutes?

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $\mu = 18$ minutes | Population mean wait time |
> | $\sigma = 9$ minutes | Population standard deviation |
> | $n = 36$ | Sample size |
> | Find: $P(\bar{X} > 20)$ | Probability the sample mean exceeds 20 minutes |

> **Step 1:** Write the CLT model for the sample mean.
>
> $$
> Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}
> $$
>
> **Step 2:** Compute the standard error.
>
> $$
> \frac{\sigma}{\sqrt{n}} = \frac{9}{\sqrt{36}} = \frac{9}{6} = 1.5
> $$
>
> **Step 3:** Substitute $\bar{X} = 20$ into the Z-score formula.
>
> $$
> Z = \frac{20 - 18}{1.5} = \frac{2}{1.5} \approx 1.33
> $$
>
> **Step 4:** Use the standard normal table.
>
> $$
> P(\bar{X} > 20) = P(Z > 1.33) \approx 0.0918
> $$
>
> **Step 5:** State the final answer.
>
> $$
> \boxed{P(\bar{X} > 20) \approx 0.0918}
> $$

---

##### Example 2 — Average Fill Weight

A snack factory produces packets with population mean fill weight $\mu = 50$ grams and population standard deviation $\sigma = 8$ grams. A random sample of $n = 64$ packets is taken. What is the probability that the sample mean is between 48 grams and 52 grams?

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $\mu = 50$ grams | Population mean fill weight |
> | $\sigma = 8$ grams | Population standard deviation |
> | $n = 64$ | Sample size |
> | Find: $P(48 < \bar{X} < 52)$ | Probability the sample mean lies between 48 and 52 grams |

> **Step 1:** Write the Z-score formula for the sample mean.
>
> $$
> Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}
> $$
>
> **Step 2:** Compute the standard error.
>
> $$
> \frac{\sigma}{\sqrt{n}} = \frac{8}{\sqrt{64}} = \frac{8}{8} = 1
> $$
>
> **Step 3:** Convert both bounds to Z-scores.
>
> $$
> Z_{48} = \frac{48 - 50}{1} = -2
> \qquad
> Z_{52} = \frac{52 - 50}{1} = 2
> $$
>
> **Step 4:** Use the standard normal table.
>
> $$
> P(48 < \bar{X} < 52) = P(-2 < Z < 2) \approx 0.9545
> $$
>
> **Step 5:** State the final answer.
>
> $$
> \boxed{P(48 < \bar{X} < 52) \approx 0.9545}
> $$

---

<p align="left">
  <a href="./sampling-distribution.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./point-estimate.md"><b>Next →</b></a>
  </span>
</p>