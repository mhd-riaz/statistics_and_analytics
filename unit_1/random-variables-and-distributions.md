<p align="left">
  <a href="./probability-fundamentals.md"><b>← Previous</b></a>
</p>

---

# Random Variables and Distributions

```
Random Variables and Distributions
├── Random Variables
│   ├── Random Variable Mapping
│   ├── Discrete vs Continuous Random Variables
│   ├── Probability Distribution Representation
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

A **random variable** is a rule that assigns a numerical value to each outcome in a sample space. This is the bridge between probability language such as "Heads," "Tails," or "3 arrivals" and the mathematics needed to build distributions, compute averages, and study long-run behavior.

Random variables are usually grouped into two main types:

- **Discrete random variables**: values are counted, such as the number of heads, customers, or defects.
- **Continuous random variables**: values are measured, such as waiting time, height, or temperature.

Once probabilities are attached to the values of a random variable, we obtain a **probability distribution**. From that distribution, we can compute the **expected value**, which is the probability-weighted long-run average.

```
Outcome in sample space S      Random variable X         Numerical value
┌────────────────────────┐     ┌──────────────────┐      ┌──────────────┐
│ Heads                  │ ──► │ X(Heads)         │ ──►  │ 1            │
│ Tails                  │ ──► │ X(Tails)         │ ──►  │ 0            │
└────────────────────────┘     └──────────────────┘      └──────────────┘

Discrete values:     ●    ●    ●    ●
                     0    1    2    3

Continuous values:   ─────────────────
                     0         5      10
```

#### Real-World Use Cases

- **Manufacturing**: Let $X$ be the number of defective items in a box, then use its distribution to estimate the average number of defects.
- **Service Operations**: Let $X$ be customer waiting time, then model the chance of delays longer than a target threshold.
- **Finance**: Let $X$ be profit or loss from an investment decision, then compare strategies using expected return.
- **Healthcare**: Let $X$ be patient response time to treatment, modeled as a measured continuous variable.
- **Limitation**: The expected value is a long-run average, so it may be a value that never appears in one individual observation.

#### Steps

1. Define the experiment and list the relevant outcomes in the sample space.
2. Assign a numerical value to each outcome to create the random variable $X$.
3. Decide whether $X$ is **discrete** or **continuous**.
4. Write the probability distribution using a PMF for discrete data or a PDF for continuous data.
5. Compute the expected value by weighting each value by its probability or density.

#### Formula

$$
X : S \to \mathbb{R}
$$

$$
E(X) = \sum x_i P(X = x_i)
\qquad \text{for a discrete random variable}
$$

$$
E(X) = \int_{-\infty}^{\infty} x f(x) \, dx
\qquad \text{for a continuous random variable}
$$

Where:
|    Symbol    | Pronunciation           | Meaning                                           |
| :----------: | :---------------------- | :------------------------------------------------ |
|     $X$      | "X"                     | Random variable                                   |
|     $S$      | "S"                     | Sample space                                      |
| $\mathbb{R}$ | "real numbers"          | Numerical output space                            |
|    $E(X)$    | "expected value of X"   | Long-run average of the random variable           |
|    $x_i$     | "x sub i"               | One possible discrete value of $X$                |
| $P(X = x_i)$ | "P of X equals x sub i" | Probability attached to the value $x_i$           |
|    $f(x)$    | "f of x"                | Probability density function for a continuous $X$ |

#### Discrete vs Continuous Random Variables

| Feature                       | Discrete Random Variable | Continuous Random Variable |
| :---------------------------- | :----------------------- | :------------------------- |
| Nature of values              | Counted values           | Measured values            |
| Typical values                | $0, 1, 2, 3, \dots$      | Any value in an interval   |
| Distribution form             | PMF, $P(X=x)$            | PDF, $f(x)$                |
| Probability at an exact value | Can be positive          | Always $0$                 |
| Expected value formula        | Sum                      | Integral                   |

- _Probability mass function (PMF)_: a rule that gives the probability for each exact discrete value.
- _Probability density function (PDF)_: a curve whose area over an interval gives probability for a continuous variable.
- _Expected value_: the probability-weighted center or long-run average of a random variable.

#### Examples

**Example 1:** Number of heads in one coin toss

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Sample space $S = \{H, T\}$ | Outcomes are Heads or Tails |
> | $X(H)=1$, $X(T)=0$ | Random variable counts heads |
> | $P(X=1)=0.5$, $P(X=0)=0.5$ | Probabilities |
> | Find: $E(X)$ | Expected number of heads |
>
> **Step 1:** Write the discrete expectation formula.
>
> $$E(X) = \sum x_i P(X=x_i)$$
>
> **Step 2:** Write the probability distribution table.
>
> | $x_i$ | 0 | 1 |
> |:---:|:---:|:---:|
> | $P(X=x_i)$ | 0.5 | 0.5 |
>
> **Step 3:** Substitute the possible values.
>
> $$E(X) = 1(0.5) + 0(0.5)$$
>
> **Step 4:** Multiply the terms.
>
> $$E(X) = 0.5 + 0$$
>
> **Step 5:** Add and state the result.
>
> $$\boxed{E(X) = 0.5}$$

**Example 2:** Expected waiting time for a uniform continuous variable

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $X \sim \text{Uniform}(0,10)$ | Waiting time is anywhere from 0 to 10 minutes |
> | $f(x)=\frac{1}{10}$ for $0 \le x \le 10$ | Constant density on the interval |
> | Find: $E(X)$ | Expected waiting time |
>
> **Step 1:** Write the continuous expectation formula.
>
> $$E(X) = \int_{-\infty}^{\infty} x f(x) \, dx$$
>
> **Step 2:** Restrict the integral to the interval where the density is nonzero.
>
> $$E(X) = \int_0^{10} x \left(\frac{1}{10}\right) dx$$
>
> **Step 3:** Factor out the constant density.
>
> $$E(X) = \frac{1}{10}\int_0^{10} x \, dx$$
>
> **Step 4:** Integrate.
>
> $$E(X) = \frac{1}{10}\left[\frac{x^2}{2}\right]_0^{10} = \frac{1}{10}\left(\frac{100}{2}\right)$$
>
> **Step 5:** Simplify and state the result.
>
> $$\boxed{E(X) = 5 \text{ minutes}}$$

---

### 2. Bernoulli and Binomial Distributions

A **Bernoulli distribution** models a single trial with only two possible outcomes: **success** or **failure**. A **Binomial distribution** builds on that idea by repeating the same Bernoulli trial a fixed number of times and counting how many successes occur.

```
Bernoulli: one trial

Success (1)   Failure (0)
     │             │
     └──────┬──────┘
            ▼
        one outcome

Binomial: n independent Bernoulli trials

1   0   1   1   0   0   1
└── count the number of successes ──┘
X = 4
```

The key difference is that Bernoulli answers "what happens on one trial?" while Binomial answers "how many successes happen across $n$ identical trials?"

#### Real-World Use Cases

- **A/B Testing**: A single visitor either converts or does not convert in a Bernoulli trial; a group of visitors gives a Binomial count of conversions.
- **Quality Inspection**: One item is defective or not defective in Bernoulli form; a batch inspection uses Binomial counting.
- **Clinical Studies**: A patient either responds or does not respond, and the total number of responses in a study can be modeled with a Binomial distribution.
- **Reliability Testing**: Each automated check either passes or fails, while the total passes across several checks follow a Binomial model.
- **Limitation**: The Binomial model breaks down if trials are not independent or if the success probability changes from one trial to the next.

#### Steps

1. Define what counts as **success** and what counts as **failure**.
2. Determine the success probability $p$ and the failure probability $q = 1-p$.
3. If there is only one trial, use the Bernoulli model.
4. If there are $n$ independent trials with the same $p$, use the Binomial model.
5. For Binomial problems, identify whether the question asks for exactly, at least, at most, or between certain numbers of successes.

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

#### Bernoulli vs Binomial

| Feature                | Bernoulli Distribution     | Binomial Distribution        |
| :--------------------- | :------------------------- | :--------------------------- |
| Number of trials       | 1                          | Fixed number $n$             |
| Possible values of $X$ | $0$ or $1$                 | $0,1,2,\dots,n$              |
| Main question          | Did success happen?        | How many successes happened? |
| Mean                   | $E(X)=p$                   | $E(X)=np$                    |
| Variance               | $\operatorname{Var}(X)=pq$ | $\operatorname{Var}(X)=npq$  |

#### Conditions for a Binomial Model

| Condition              | Meaning                                                 |
| :--------------------- | :------------------------------------------------------ |
| Fixed number of trials | The value of $n$ is known in advance                    |
| Two outcomes per trial | Each trial is success or failure                        |
| Independence           | One trial does not affect another                       |
| Constant probability   | The same success probability $p$ applies on every trial |

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
> **Step 2:** Substitute $x=1$ to compute the success probability.
>
> $$P(X=1)=0.03^1(0.97)^0=0.03$$
>
> **Step 3:** Substitute $x=0$ to compute the failure probability.
>
> $$P(X=0)=0.03^0(0.97)^1=0.97$$
>
> **Step 4:** Write the Bernoulli distribution table.
>
> | $x$ | 0 | 1 |
> |:---:|:---:|:---:|
> | $P(X=x)$ | 0.97 | 0.03 |
>
> **Step 5:** Check that the probabilities sum to 1.
>
> $$0.03+0.97=1$$
>
> $$\boxed{P(X=1)=0.03,\ P(X=0)=0.97}$$

**Example 2:** Binomial probability of at least 5 passed checks

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $n = 6$ | Number of automated checks |
> | $p = 0.8$ | Probability that one check passes |
> | $q = 0.2$ | Probability that one check fails |
> | Find: $P(X \ge 5)$ | Probability that at least 5 checks pass |
>
> **Step 1:** Interpret "at least 5" as two cases.
>
> $$P(X \ge 5)=P(X=5)+P(X=6)$$
>
> **Step 2:** Write the Binomial formula.
>
> $$P(X=k)=\binom{n}{k}p^k q^{n-k}$$
>
> **Step 3:** Compute $P(X=5)$.
>
> $$P(X=5)=\binom{6}{5}(0.8)^5(0.2)^1=6(0.32768)(0.2)=0.393216$$
>
> **Step 4:** Compute $P(X=6)$.
>
> $$P(X=6)=\binom{6}{6}(0.8)^6(0.2)^0=1(0.262144)(1)=0.262144$$
>
> **Step 5:** Add the two probabilities and state the result.
>
> $$P(X \ge 5)=0.393216+0.262144=0.65536$$
>
> $$\boxed{P(X \ge 5) \approx 0.6554}$$

---

### 3. Poisson Distribution

A **Poisson distribution** models the number of events that occur in a fixed interval of time, space, area, or volume when events happen independently and at a constant average rate $\lambda$. It is especially useful for **counting rare or scattered events** rather than tracking a fixed number of trials.

```
Fixed interval

0 ├───────────────────────────────┤ 1 hour
    ●      ●   ●        ●   ●

Count the events in the interval
Average rate = λ events per interval
```

Poisson questions usually sound like "how many arrivals, calls, failures, or defects happen in this window?" The interval stays fixed, while the count varies.

#### Real-World Use Cases

- **Call Centers**: Number of calls received per hour when arrivals are irregular but average out over time.
- **Traffic Flow**: Number of cars passing a checkpoint in a short interval.
- **Reliability**: Number of machine failures in a month or defects per unit length of material.
- **Healthcare**: Number of patients arriving at an emergency room during a shift.
- **Limitation**: The average rate must stay approximately constant within the interval, and clustered or time-dependent arrivals can make the Poisson model inaccurate.

#### Steps

1. Identify the fixed interval and the average event rate for that interval.
2. Express the rate as $\lambda$ for the exact window you are analyzing.
3. Choose the target count $k$.
4. Substitute into the Poisson probability formula.
5. Interpret the answer as the chance of exactly $k$ events in that interval.

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

#### When a Poisson Model Fits

| Requirement           | Meaning                                      |
| :-------------------- | :------------------------------------------- |
| Events are counts     | The variable records 0, 1, 2, 3, ... events  |
| Fixed interval        | Time, distance, area, or volume is specified |
| Independent events    | One event does not force another to happen   |
| Constant average rate | The mean rate is stable across the interval  |

#### Poisson Summary Properties

$$
E(X)=\lambda
\qquad
\operatorname{Var}(X)=\lambda
$$

Where:
|         Symbol          | Pronunciation         | Meaning                                           |
| :---------------------: | :-------------------- | :------------------------------------------------ |
|         $E(X)$          | "expected value of X" | Average number of events per interval             |
| $\operatorname{Var}(X)$ | "variance of X"       | Spread in the event counts                        |
|        $\lambda$        | "lambda"              | Both the mean and the variance in a Poisson model |

This is a distinctive feature of the Poisson distribution: the **mean and variance are equal**.

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
> **Step 2:** Substitute $\lambda = 4$ and $k = 2$.
>
> $$P(X=2)=\frac{e^{-4}4^2}{2!}$$
>
> **Step 3:** Simplify the powers and factorial.
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

**Example 2:** Converting a rate before applying Poisson

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Average rate = 6 emails per hour | Original rate information |
> | Interval of interest = 30 minutes | Half an hour |
> | $k = 4$ | Exactly 4 emails |
> | Find: $P(X=4)$ | Probability of exactly 4 emails in 30 minutes |
>
> **Step 1:** Convert the rate to the correct interval.
>
> $$\lambda = 6 \times \frac{30}{60} = 3$$
>
> **Step 2:** Write the Poisson formula.
>
> $$P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!}$$
>
> **Step 3:** Substitute $\lambda = 3$ and $k = 4$.
>
> $$P(X=4)=\frac{e^{-3}3^4}{4!}$$
>
> **Step 4:** Simplify the expression.
>
> $$P(X=4)=\frac{81e^{-3}}{24}=3.375e^{-3}$$
>
> **Step 5:** Approximate numerically and state the result.
>
> $$P(X=4) \approx 3.375(0.04979) \approx 0.1680$$
>
> $$\boxed{P(X=4) \approx 0.1680}$$

---

### 4. Normal Distribution and Central Limit Theorem

The **Normal distribution** is a symmetric bell-shaped distribution described by its mean $\mu$ and standard deviation $\sigma$. The **Central Limit Theorem (CLT)** explains why the distribution of sample means becomes approximately normal when random samples are large enough, even if the original population is not perfectly normal.

```
                 ┌──────── 99.7% ────────┐
                 │   ┌───── 95% ─────┐   │
                 │   │   ┌─ 68% ─┐   │   │
                 │   │   │  ██   │   │   │
                 │   │  ████████ │   │   │
  ◄──────────────┼───┼───┼── μ ──┼───┼───┼──────────────►
               -3σ  -2σ  -1σ     +1σ +2σ +3σ

Raw data can be skewed  →  sample means become bell-shaped
```

For a normal model, the center is controlled by $\mu$ and the spread is controlled by $\sigma$. Standardization converts any normal value to a **Z-score**, which tells us how many standard deviations above or below the mean the value lies.

The CLT shifts the focus from a single observation $X$ to the sample mean $\bar{X}$. The original population may be skewed, but repeated sample means still tend toward a normal shape under suitable sampling conditions.

#### Real-World Use Cases

- **Manufacturing**: Model part dimensions, fill weights, or battery life around a target mean.
- **Education and Testing**: Convert exam scores into Z-scores to compare performance across different scales.
- **Polling and Surveys**: Use the CLT to justify normal approximations for sample means and confidence procedures.
- **Healthcare**: Evaluate whether a patient's measurement is unusual relative to a reference population.
- **Limitation**: A raw dataset does not automatically follow a normal distribution, and the CLT applies to sample means, not to every kind of statistic.

#### Steps

1. Identify whether the question is about a single observation $X$ or a sample mean $\bar{X}$.
2. Record the mean $\mu$, standard deviation $\sigma$, and sample size $n$ if applicable.
3. For one observation, standardize with $Z=\frac{x-\mu}{\sigma}$.
4. For a sample mean, compute the standard error $\frac{\sigma}{\sqrt{n}}$ and then standardize.
5. Use the normal distribution or Z-table to interpret the probability or unusualness of the result.

#### Formula

$$
Z = \frac{x-\mu}{\sigma}
$$

$$
\bar{X} \approx N\left(\mu, \frac{\sigma^2}{n}\right)
\qquad
Z = \frac{\bar{X}-\mu}{\sigma / \sqrt{n}}
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

#### Normal Model vs CLT View

| Idea            | Raw Observation          | Sample Mean                             |
| :-------------- | :----------------------- | :-------------------------------------- |
| Random variable | $X$                      | $\bar{X}$                               |
| Center          | $\mu$                    | $\mu$                                   |
| Spread          | $\sigma$                 | $\sigma / \sqrt{n}$                     |
| Standardization | $Z=\frac{x-\mu}{\sigma}$ | $Z=\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}$ |
| Main use        | Individual values        | Averages from repeated samples          |

#### CLT Conditions and Interpretation

| Item                           | Interpretation                                             |
| :----------------------------- | :--------------------------------------------------------- |
| Random or independent sampling | Prevents systematic bias in the sampling process           |
| Large enough sample size       | Often $n \ge 30$ is a practical rule of thumb              |
| Same center                    | The sampling distribution stays centered at $\mu$          |
| Smaller spread                 | The spread shrinks to the standard error $\sigma/\sqrt{n}$ |

- _Standardization_: converting a value into a Z-score so it can be compared on the standard normal scale.
- _Standard normal distribution_: a normal distribution with mean $0$ and standard deviation $1$.
- _Standard error_: the standard deviation of the sampling distribution of the mean.

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
> **Step 5:** Interpret and state the result.
>
> $$\boxed{Z = 1.5}$$
>
> The score is **1.5 standard deviations above the mean**.

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
> **Step 3:** State the approximate sampling distribution.
>
> $$\bar{X} \approx N(50, 2^2)$$
>
> **Step 4:** Set up the Z-score for a sample mean target, for example $\bar{X}=53$.
>
> $$Z = \frac{53-50}{2} = 1.5$$
>
> **Step 5:** State the final result.
>
> $$\boxed{\sigma_{\bar{X}} = 2,\ \bar{X} \approx N(50,4),\ Z_{\bar{X}=53}=1.5}$$

---

<p align="left">
  <a href="./probability-fundamentals.md"><b>← Previous</b></a>
</p>