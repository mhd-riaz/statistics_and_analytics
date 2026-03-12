<p align="left">
  <a href="./probability-fundamentals.md"><b>← Previous</b></a>
</p>

---

# Random Variables and Distributions

```
Random Variables and Distributions
├── Random Variables
│   ├── Discrete Random Variables
│   ├── Continuous Random Variables
│   └── Expected Value
│
├── Discrete Distributions
│   ├── Bernoulli Distribution
│   ├── Binomial Distribution
│   └── Poisson Distribution
│
└── Continuous Distributions
    ├── Normal Distribution
    ├── Standardization
    └── Central Limit Theorem
```

---

## Random Variables and Distributions

### 1. Random Variables and Expected Value

A **random variable** assigns a number to each outcome of an experiment. Once outcomes are numerical, you can build probability distributions and compute long-run averages such as the **expected value**.

```
  Coin toss outcome -> random variable X
  Heads -> 1
  Tails -> 0

  Expected value = long-run average after many repetitions
```

#### Real-World Use Cases

- **Quality Control**: Let $X$ be the number of defective items in a sample.
- **Finance**: Let $X$ be the profit from a trade outcome.
- **Operations**: Let $X$ be the number of arrivals in a time window.
- **Limitation**: The expected value may be a non-observable average, not a value that appears in a single trial.

#### Steps

1. Define the experiment.
2. Assign numeric values to outcomes.
3. Determine the probability attached to each value.
4. Multiply each value by its probability and add them.

#### Formula

$$
X : S \to \mathbb{R}
\qquad
E(X) = \sum x_i P(X = x_i)
$$

Where:
|    Symbol    | Pronunciation         | Meaning                                 |
| :----------: | :-------------------- | :-------------------------------------- |
|     $X$      | "X"                   | Random variable                         |
|     $S$      | "S"                   | Sample space                            |
| $\mathbb{R}$ | "real numbers"        | Numerical output space                  |
|    $E(X)$    | "expected value of X" | Long-run average of the random variable |
|    $x_i$     | "x sub i"             | One possible value of $X$               |

#### Examples

**Example 1:** Number of heads in one coin toss

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $X = 1$ for Heads | Success value |
> | $X = 0$ for Tails | Failure value |
> | $P(X=1)=0.5$, $P(X=0)=0.5$ | Probabilities |
> | Find: $E(X)$ | Expected number of heads |
>
> **Step 1:** Write the expectation formula.
>
> $$E(X) = \sum x_i P(X=x_i)$$
>
> **Step 2:** Substitute the possible values.
>
> $$E(X) = 1(0.5) + 0(0.5)$$
>
> **Step 3:** Multiply the terms.
>
> $$E(X) = 0.5 + 0$$
>
> **Step 4:** Add.
>
> $$E(X) = 0.5$$
>
> **Step 5:** State the result.
>
> $$\boxed{E(X) = 0.5}$$

**Example 2:** Expected value of a fair die

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $X = \{1,2,3,4,5,6\}$ | Possible die values |
> | $P(X=x)=\frac{1}{6}$ | Each value is equally likely |
> | Find: $E(X)$ | Long-run average outcome |
>
> **Step 1:** Write the formula.
>
> $$E(X) = \sum x_i P(X=x_i)$$
>
> **Step 2:** Substitute the values.
>
> $$E(X) = \frac{1+2+3+4+5+6}{6}$$
>
> **Step 3:** Add the numerator.
>
> $$E(X) = \frac{21}{6}$$
>
> **Step 4:** Simplify.
>
> $$E(X) = 3.5$$
>
> **Step 5:** State the result.
>
> $$\boxed{E(X) = 3.5}$$

---

### 2. Bernoulli and Binomial Distributions

A **Bernoulli distribution** models one trial with two outcomes: success or failure. A **Binomial distribution** extends that idea to $n$ independent trials and counts how many successes occur.

```
  Bernoulli -> one trial -> 0 or 1
  Binomial  -> n trials  -> count total successes
```

#### Real-World Use Cases

- **A/B Testing**: A single user converts or does not convert in a Bernoulli trial.
- **Quality Inspection**: Count how many defective items appear in a batch using a Binomial model.
- **Clinical Trials**: Count the number of treatment responses out of a fixed sample size.
- **Limitation**: Binomial modeling requires independent trials with the same success probability.

#### Steps

1. Define success and failure.
2. Determine the success probability $p$ and failure probability $q=1-p$.
3. For one trial, use the Bernoulli model.
4. For $n$ independent trials and exactly $k$ successes, use the Binomial model.

#### Formula

$$
P(X=x) = p^x q^{1-x}, \quad x \in \{0,1\}
$$

$$
P(X=k) = \binom{n}{k}p^k q^{n-k}
$$

Where:
|     Symbol     | Pronunciation | Meaning                                                |
| :------------: | :------------ | :----------------------------------------------------- |
|      $p$       | "p"           | Probability of success                                 |
|      $q$       | "q"           | Probability of failure, equal to $1-p$                 |
|      $x$       | "x"           | Bernoulli outcome, 0 or 1                              |
|      $n$       | "n"           | Number of trials                                       |
|      $k$       | "k"           | Number of successes                                    |
| $\binom{n}{k}$ | "n choose k"  | Number of ways to place $k$ successes among $n$ trials |

#### Examples

**Example 1:** Bernoulli probability for one item

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Defect probability $p = 0.03$ | Success = defective item |
> | $q = 0.97$ | Failure = non-defective item |
> | Find: $P(X=1)$ and $P(X=0)$ | Bernoulli outcomes |
>
> **Step 1:** Write the Bernoulli formula.
>
> $$P(X=x)=p^x q^{1-x}$$
>
> **Step 2:** Compute the success probability.
>
> $$P(X=1)=0.03^1(0.97)^0=0.03$$
>
> **Step 3:** Compute the failure probability.
>
> $$P(X=0)=0.03^0(0.97)^1=0.97$$
>
> **Step 4:** Check that they sum to 1.
>
> $$0.03+0.97=1$$
>
> **Step 5:** State the result.
>
> $$\boxed{P(X=1)=0.03,\ P(X=0)=0.97}$$

**Example 2:** Binomial probability of exactly 3 conversions

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $n = 20$ | Number of users |
> | $p = 0.12$ | Conversion probability |
> | $q = 0.88$ | Non-conversion probability |
> | $k = 3$ | Desired number of conversions |
> | Find: $P(X=3)$ | Probability of exactly 3 conversions |
>
> **Step 1:** Write the Binomial formula.
>
> $$P(X=k)=\binom{n}{k}p^k q^{n-k}$$
>
> **Step 2:** Substitute the values.
>
> $$P(X=3)=\binom{20}{3}(0.12)^3(0.88)^{17}$$
>
> **Step 3:** Compute the combination.
>
> $$\binom{20}{3}=1140$$
>
> **Step 4:** Evaluate the product.
>
> $$P(X=3) \approx 1140(0.001728)(0.1138) \approx 0.2242$$
>
> **Step 5:** State the result.
>
> $$\boxed{P(X=3) \approx 0.2242}$$

---

### 3. Poisson Distribution

A **Poisson distribution** models the number of events that occur in a fixed interval when events happen independently at a constant average rate $\lambda$.

```
  Time interval -> count events
  ●   ● ●    ●      ●

  Average rate = λ events per interval
```

#### Real-World Use Cases

- **Call Centers**: Number of calls per hour.
- **Traffic Flow**: Number of cars crossing a checkpoint per minute.
- **Reliability**: Number of failures in a machine over a month.
- **Limitation**: The average rate must stay approximately constant over the interval.

#### Steps

1. Identify the interval and average rate $\lambda$.
2. Choose the exact count $k$ you want.
3. Substitute into the Poisson formula.
4. Compute the probability.

#### Formula

$$
P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}
$$

Where:
|  Symbol   | Pronunciation | Meaning                                    |
| :-------: | :------------ | :----------------------------------------- |
| $\lambda$ | "lambda"      | Average number of events per interval      |
|    $k$    | "k"           | Desired number of events                   |
|    $e$    | "e"           | Exponential constant                       |
|   $k!$    | "k factorial" | Product of positive integers from 1 to $k$ |

#### Examples

**Example 1:** Calls received in one hour

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\lambda = 4$ | Average 4 calls per hour |
> | $k = 2$ | Exactly 2 calls |
> | Find: $P(X=2)$ | Poisson probability |
>
> **Step 1:** Write the formula.
>
> $$P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!}$$
>
> **Step 2:** Substitute the values.
>
> $$P(X=2)=\frac{e^{-4}4^2}{2!}$$
>
> **Step 3:** Simplify.
>
> $$P(X=2)=\frac{16e^{-4}}{2}=8e^{-4}$$
>
> **Step 4:** Approximate numerically.
>
> $$P(X=2) \approx 8(0.018315) \approx 0.1465$$
>
> **Step 5:** State the result.
>
> $$\boxed{P(X=2) \approx 0.1465}$$

**Example 2:** Defects in a roll of fabric

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\lambda = 1.5$ | Average 1.5 defects per roll |
> | $k = 0$ | No defects |
> | Find: $P(X=0)$ | Probability of a perfect roll |
>
> **Step 1:** Write the Poisson formula.
>
> $$P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!}$$
>
> **Step 2:** Substitute the values.
>
> $$P(X=0)=\frac{e^{-1.5}(1.5)^0}{0!}$$
>
> **Step 3:** Simplify.
>
> $$P(X=0)=e^{-1.5}$$
>
> **Step 4:** Approximate numerically.
>
> $$P(X=0) \approx 0.2231$$
>
> **Step 5:** State the result.
>
> $$\boxed{P(X=0) \approx 0.2231}$$

---

### 4. Normal Distribution and Central Limit Theorem

The **Normal distribution** is a symmetric bell-shaped distribution determined by its mean and standard deviation. The **Central Limit Theorem (CLT)** explains why sample means tend to be normally distributed when sample sizes are large enough.

```
               ┌──────── 99.7% ──────┐
               │  ┌───── 95% ─────┐  │
               │  │  ┌── 68% ──┐  │  │
  ◄────────────┼──┼──┼────μ────┼──┼──┼────────────►
             -3σ -2σ -1σ      +1σ +2σ +3σ

  CLT: many sample means -> approximate bell curve
```

#### Real-World Use Cases

- **Manufacturing**: Model dimensions that fluctuate around a target value.
- **Testing**: Convert scores to Z-scores and compute cumulative probabilities.
- **Polling**: Use the CLT to justify normal approximations for sample means.
- **Limitation**: The normal model is not suitable for every raw dataset, though the CLT helps with sample means.

#### Steps

1. Identify the population mean $\mu$, standard deviation $\sigma$, and if needed the sample size $n$.
2. Standardize values with a Z-score.
3. Use the normal model or Z-table for probability statements.
4. For sample means, compute the standard error $\sigma/\sqrt{n}$.
5. Apply the CLT when the sample size is sufficiently large.

#### Formula

$$
Z = \frac{x-\mu}{\sigma}
\qquad
\bar{X} \approx N\left(\mu, \frac{\sigma^2}{n}\right)
$$

Where:
|  Symbol   | Pronunciation | Meaning                             |
| :-------: | :------------ | :---------------------------------- |
|    $Z$    | "Z"           | Standardized distance from the mean |
|    $x$    | "x"           | Observed value                      |
|   $\mu$   | "mew"         | Population mean                     |
| $\sigma$  | "sigma"       | Population standard deviation       |
| $\bar{X}$ | "X bar"       | Sample mean random variable         |
|    $n$    | "n"           | Sample size                         |

#### Examples

**Example 1:** Compute a Z-score

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $x = 90$ | Observed exam score |
> | $\mu = 75$ | Population mean |
> | $\sigma = 10$ | Population standard deviation |
> | Find: $Z$ | Standardized score |
>
> **Step 1:** Write the Z-score formula.
>
> $$Z = \frac{x-\mu}{\sigma}$$
>
> **Step 2:** Substitute the values.
>
> $$Z = \frac{90-75}{10}$$
>
> **Step 3:** Simplify the numerator.
>
> $$Z = \frac{15}{10}$$
>
> **Step 4:** Divide.
>
> $$Z = 1.5$$
>
> **Step 5:** State the result.
>
> $$\boxed{Z = 1.5}$$

**Example 2:** Use the CLT for a sample mean

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\mu = 50$ | Population mean |
> | $\sigma = 12$ | Population standard deviation |
> | $n = 36$ | Sample size |
> | Find: standard error and probability setup | Sampling distribution of the mean |
>
> **Step 1:** Write the CLT standard error formula.
>
> $$\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}$$
>
> **Step 2:** Substitute the values.
>
> $$\sigma_{\bar{X}} = \frac{12}{\sqrt{36}} = \frac{12}{6} = 2$$
>
> **Step 3:** State the sampling distribution.
>
> $$\bar{X} \approx N(50, 2^2)$$
>
> **Step 4:** Interpret the result.
>
> Sample means from samples of size 36 are centered at 50 with standard error 2.
>
> **Step 5:** State the final answer.
>
> $$\boxed{\sigma_{\bar{X}} = 2,\ \bar{X} \approx N(50,4)}$$

---

<p align="left">
  <a href="./probability-fundamentals.md"><b>← Previous</b></a>
</p>