<p align="left">
  <a href="./randomVariables.md"><b>← Previous</b></a>
</p>

# Probability Distributions

```
Probability Distributions
├── Discrete Distributions
│   ├── 1. Bernoulli Distribution
│   │      └── Single trial, two outcomes (success/failure)
│   │
│   ├── 2. Binomial Distribution
│   │      └── Sequence of Bernoulli trials (n trials, count successes)
│   │
│   └── 3. Poisson Distribution
│          └── Count of events in a fixed interval (when you know the rate)
│
└── Continuous Distributions
    └── 4. Normal Distribution
           └── Bell-shaped, symmetric around the mean
```

Before diving in, here are two symbols used throughout every distribution:

| Symbol | Pronunciation | Meaning                                                         |
| :----: | :------------ | :-------------------------------------------------------------- |
|  $p$   | "p"           | Probability of **success** on a single trial                    |
|  $q$   | "q"           | Probability of **failure** on a single trial, where $q = 1 - p$ |

---

## 1. Bernoulli Distribution

A **Bernoulli Distribution** models a single experiment (one trial) that has exactly **two possible outcomes** — typically called _success_ ($1$) and _failure_ ($0$). Think of it as a single yes-or-no question.

```
  One trial, two outcomes:

       p               q = 1 - p
  ┌─────────┐      ┌─────────┐
  │ Success │      │ Failure │
  │  X = 1  │      │  X = 0  │
  └─────────┘      └─────────┘

  PMF bar chart:

  P(X)
   │
 p ┤  ██
   │  ██
 q ┤  ██    ██
   │  ██    ██
   └──────────── X
      0     1
```

#### Real-World Use Cases

- **Quality Control**: Checking whether a single item off the assembly line is defective ($1$) or not ($0$).
- **Medicine**: A single patient either responds to a drug (success) or doesn't (failure).
- **Marketing**: A single user either clicks an ad ($1$) or doesn't ($0$).
- **Sports**: A single free-throw is either made ($1$) or missed ($0$).
- **Building Block**: Bernoulli is the foundation — repeat it $n$ times and you get the **Binomial Distribution**.

#### Steps

1. Identify the experiment — it must have **exactly two outcomes**.
2. Define which outcome is "success" ($X = 1$) and which is "failure" ($X = 0$).
3. Determine the probability of success $p$.
4. Calculate $q = 1 - p$.
5. Use the PMF formula to find the probability of a specific outcome.

#### Formula

$$
P(X = x) = p^x \cdot q^{1-x} \quad \text{where } x \in \{0, 1\}
$$

Where:

|   Symbol   | Pronunciation                 | Meaning                                       |
| :--------: | :---------------------------- | :-------------------------------------------- |
| $P(X = x)$ | "probability that X equals x" | The probability of getting outcome $x$        |
|    $x$     | "x"                           | The outcome: $1$ for success, $0$ for failure |
|    $p$     | "p"                           | Probability of success                        |
|    $q$     | "q"                           | Probability of failure ($q = 1 - p$)          |

> **Shortcut:** When $x = 1$: $P(X = 1) = p$. When $x = 0$: $P(X = 0) = q = 1 - p$.

**Expected Value and Variance:**

$$
E(X) = p \qquad \text{Var}(X) = p \cdot q
$$

#### Examples

**Example 1** — Flipping a fair coin (success = Heads)

A fair coin is flipped once. Let success ($X = 1$) be getting Heads. Find $P(X = 1)$ and $P(X = 0)$.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Experiment: flip 1 fair coin | Single trial with two outcomes |
> | $p = 0.5$ | Probability of Heads (success) |
> | $q = 1 - 0.5 = 0.5$ | Probability of Tails (failure) |
> | Find: $P(X = 1)$ and $P(X = 0)$ | Probability of each outcome |

> **Step 1:** Write the formula.
>
> $$P(X = x) = p^x \cdot q^{1-x}$$
>
> **Step 2:** Find $P(X = 1)$ — probability of success (Heads).
>
> $$P(X = 1) = (0.5)^1 \cdot (0.5)^{1-1} = 0.5 \cdot 1 = 0.5$$
>
> **Step 3:** Find $P(X = 0)$ — probability of failure (Tails).
>
> $$P(X = 0) = (0.5)^0 \cdot (0.5)^{1-0} = 1 \cdot 0.5 = 0.5$$
>
> **Step 4:** Verify probabilities sum to 1.
>
> $$0.5 + 0.5 = 1 \checkmark$$
>
> $$\boxed{P(X = 1) = 0.5, \quad P(X = 0) = 0.5}$$

**Example 2** — Defective item on a production line

A factory has a 3% defect rate. One item is randomly selected. Let success ($X = 1$) mean the item is defective. Find the probability the item is defective and the probability it is not.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Experiment: inspect 1 item | Single trial with two outcomes |
> | $p = 0.03$ | Probability of defective (success) |
> | $q = 1 - 0.03 = 0.97$ | Probability of non-defective (failure) |
> | Find: $P(X = 1)$ and $P(X = 0)$ | Probability of each outcome |

> **Step 1:** Write the formula.
>
> $$P(X = x) = p^x \cdot q^{1-x}$$
>
> **Step 2:** Find $P(X = 1)$ — probability the item is defective.
>
> $$P(X = 1) = (0.03)^1 \cdot (0.97)^0 = 0.03 \cdot 1 = 0.03$$
>
> **Step 3:** Find $P(X = 0)$ — probability the item is NOT defective.
>
> $$P(X = 0) = (0.03)^0 \cdot (0.97)^1 = 1 \cdot 0.97 = 0.97$$
>
> **Step 4:** Verify probabilities sum to 1.
>
> $$0.03 + 0.97 = 1 \checkmark$$
>
> $$\boxed{P(\text{defective}) = 0.03 = 3\%, \quad P(\text{not defective}) = 0.97 = 97\%}$$

---

## 2. Binomial Distribution

A **Binomial Distribution** models the number of successes in a **fixed number of independent Bernoulli trials**. While Bernoulli asks "did this one trial succeed?", Binomial asks "out of $n$ trials, how many succeeded?"

```
  Bernoulli → single trial          Binomial → n trials
  ┌───┐                             ┌───┬───┬───┬───┬───┐
  │ 1 │  (one flip)                 │ 1 │ 0 │ 1 │ 1 │ 0 │  (five flips)
  └───┘                             └───┴───┴───┴───┴───┘
                                     X = count of 1s = 3

  PMF shape (n=10, p=0.5):

  P(X)
   │        ██
   │      ██████
   │    ██████████
   │  ██████████████
   │████████████████████
   └──────────────────── X
   0  1  2  3  4  5  6  7  8  9  10
```

#### Real-World Use Cases

- **A/B Testing**: Out of 20 users shown a new variant, how many will convert? (from your session 3 raw notes!)
- **Quality Control**: Out of 10 knives drawn, how many are defective?
- **Medicine**: Out of 50 patients given a new treatment, how many recover?
- **Education**: Out of 30 multiple-choice questions guessed randomly, how many are correct?
- **Key Condition**: Each trial must be **independent** with the **same probability** $p$.

#### Steps

1. Confirm the experiment consists of **$n$ independent trials**, each with the same probability $p$.
2. Define what counts as "success."
3. Identify $n$ (number of trials), $p$ (probability of success), and $k$ (desired number of successes).
4. Calculate $q = 1 - p$.
5. Apply the Binomial PMF formula.

#### Formula

$$
P(X = k) = \binom{n}{k} \cdot p^k \cdot q^{n-k}
$$

Where:

|     Symbol     | Pronunciation                 | Meaning                                                                          |
| :------------: | :---------------------------- | :------------------------------------------------------------------------------- |
|   $P(X = k)$   | "probability that X equals k" | The probability of getting exactly $k$ successes                                 |
| $\binom{n}{k}$ | "n choose k"                  | The number of ways to pick which $k$ trials are successes: $\frac{n!}{k!(n-k)!}$ |
|      $n$       | "n"                           | The total number of trials                                                       |
|      $k$       | "k"                           | The desired number of successes                                                  |
|      $p$       | "p"                           | Probability of success on a single trial                                         |
|      $q$       | "q"                           | Probability of failure on a single trial ($q = 1 - p$)                           |

**Expected Value and Variance:**

$$
E(X) = n \cdot p \qquad \text{Var}(X) = n \cdot p \cdot q
$$

#### Examples

**Example 1** — A/B test conversions (from Session 3 notes)

During an online A/B experiment, each user converts independently with probability $0.12$. The new variant is shown to $20$ users. What is the probability that **exactly 3** conversions occur?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $n = 20$ | Number of users (trials) |
> | $p = 0.12$ | Probability each user converts (success) |
> | $q = 1 - 0.12 = 0.88$ | Probability a user does not convert |
> | $k = 3$ | Desired number of conversions |
> | Find: $P(X = 3)$ | Probability of exactly 3 conversions |

> **Step 1:** Write the Binomial PMF formula.
>
> $$P(X = k) = \binom{n}{k} \cdot p^k \cdot q^{n-k}$$
>
> **Step 2:** Calculate $\binom{20}{3}$.
>
> $$\binom{20}{3} = \frac{20!}{3! \cdot 17!} = \frac{20 \times 19 \times 18}{3 \times 2 \times 1} = \frac{6840}{6} = 1140$$
>
> **Step 3:** Substitute into the formula.
>
> $$P(X = 3) = 1140 \cdot (0.12)^3 \cdot (0.88)^{17}$$
>
> **Step 4:** Compute each part.
>
> $(0.12)^3 = 0.001728$
>
> $(0.88)^{17} \approx 0.1138$
>
> **Step 5:** Multiply.
>
> $$P(X = 3) = 1140 \times 0.001728 \times 0.1138 \approx 1140 \times 0.000196706 \approx 0.2242$$
>
> $$\boxed{P(X = 3) \approx 0.2242 = 22.42\%}$$
>
> There's approximately a **22.42%** chance that exactly 3 out of 20 users convert.

**Example 2** — Model validation checks (from Session 3 notes)

Before release, a model must pass multiple automated checks. Each check is passed independently with probability $0.8$. A total of $6$ checks are run. What is the probability that **at least 5** checks are passed?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $n = 6$ | Number of checks (trials) |
> | $p = 0.8$ | Probability each check is passed |
> | $q = 1 - 0.8 = 0.2$ | Probability a check is failed |
> | Find: $P(X \ge 5)$ | Probability of passing at least 5 checks |

> **Step 1:** "At least 5" means $P(X = 5) + P(X = 6)$. Calculate each separately.
>
> **Step 2:** Find $P(X = 5)$.
>
> $$P(X = 5) = \binom{6}{5} \cdot (0.8)^5 \cdot (0.2)^1$$
>
> $$\binom{6}{5} = 6$$
>
> $$P(X = 5) = 6 \cdot 0.32768 \cdot 0.2 = 6 \cdot 0.065536 = 0.393216$$
>
> **Step 3:** Find $P(X = 6)$.
>
> $$P(X = 6) = \binom{6}{6} \cdot (0.8)^6 \cdot (0.2)^0$$
>
> $$\binom{6}{6} = 1$$
>
> $$P(X = 6) = 1 \cdot 0.262144 \cdot 1 = 0.262144$$
>
> **Step 4:** Add them together.
>
> $$P(X \ge 5) = 0.393216 + 0.262144 = 0.65536$$
>
> $$\boxed{P(X \ge 5) \approx 0.6554 = 65.54\%}$$
>
> There's approximately a **65.54%** chance that at least 5 out of 6 checks pass.

---

## 3. Poisson Distribution

A **Poisson Distribution** models the number of events occurring in a **fixed interval** (of time, space, or volume) when you know the **average rate** ($\lambda$) at which events happen. Unlike Binomial, you don't need a fixed number of trials — just the average rate.

```
  "How many events in this window?"

  Time ──────────────────────────────►
       │  ●    ●  ●       ●     ●  │
       │                            │
       └────── fixed interval ──────┘
             λ = average rate

  PMF shape (λ = 4):

  P(X)
   │     ██
   │    ████
   │   ██████
   │  █████████
   │ ████████████
   │██████████████████
   └────────────────────── X
   0  1  2  3  4  5  6  7  8  9  10
```

#### Real-World Use Cases

- **Call Centers**: Number of calls received per hour (average 5 calls/hour — what's the probability of getting exactly 8?).
- **Traffic**: Number of cars passing a checkpoint in 10 minutes.
- **Healthcare**: Number of patients arriving at an ER per night.
- **IT**: Number of server crashes per month.
- **Manufacturing**: Number of defects found per 100 meters of fabric.
- **Key Condition**: Events must be **independent** and occur at a **constant average rate**.

#### Steps

1. Identify the fixed interval (time, area, volume, etc.).
2. Determine the average rate $\lambda$ for that interval.
3. Identify the desired count $k$.
4. Apply the Poisson PMF formula.

#### Formula

$$
P(X = k) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}
$$

Where:

|   Symbol   | Pronunciation                 | Meaning                                                          |
| :--------: | :---------------------------- | :--------------------------------------------------------------- |
| $P(X = k)$ | "probability that X equals k" | Probability of exactly $k$ events occurring                      |
|    $e$     | "Euler's number"              | The mathematical constant $\approx 2.71828$                      |
| $\lambda$  | "lambda"                      | The **average rate** — expected number of events in the interval |
|    $k$     | "k"                           | The specific number of events you want the probability for       |
|    $k!$    | "k factorial"                 | $k \times (k-1) \times \cdots \times 1$                          |

**Expected Value and Variance:**

$$
E(X) = \lambda \qquad \text{Var}(X) = \lambda
$$

> In Poisson, the mean and variance are **both equal to $\lambda$**.

#### Examples

**Example 1** — Call center (average rate given directly)

A call center receives an average of $\lambda = 5$ calls per hour. What is the probability of receiving **exactly 3** calls in one hour?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\lambda = 5$ | Average number of calls per hour |
> | $k = 3$ | Desired number of calls |
> | $e \approx 2.71828$ | Euler's number |
> | Find: $P(X = 3)$ | Probability of exactly 3 calls |

> **Step 1:** Write the Poisson PMF formula.
>
> $$P(X = k) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}$$
>
> **Step 2:** Substitute the values.
>
> $$P(X = 3) = \frac{e^{-5} \cdot 5^3}{3!}$$
>
> **Step 3:** Compute each part.
>
> $e^{-5} \approx 0.006738$
>
> $5^3 = 125$
>
> $3! = 6$
>
> **Step 4:** Multiply and divide.
>
> $$P(X = 3) = \frac{0.006738 \times 125}{6} = \frac{0.84225}{6} \approx 0.14038$$
>
> $$\boxed{P(X = 3) \approx 0.1404 = 14.04\%}$$
>
> There's approximately a **14.04%** chance of receiving exactly 3 calls in one hour.

**Example 2** — Server crashes (different interval)

A server crashes on average $2$ times per month. What is the probability of **zero** crashes next month?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\lambda = 2$ | Average number of crashes per month |
> | $k = 0$ | Desired number of crashes |
> | $e \approx 2.71828$ | Euler's number |
> | Find: $P(X = 0)$ | Probability of zero crashes |

> **Step 1:** Write the Poisson PMF formula.
>
> $$P(X = k) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}$$
>
> **Step 2:** Substitute the values.
>
> $$P(X = 0) = \frac{e^{-2} \cdot 2^0}{0!}$$
>
> **Step 3:** Simplify — recall $2^0 = 1$ and $0! = 1$.
>
> $$P(X = 0) = \frac{e^{-2} \cdot 1}{1} = e^{-2}$$
>
> **Step 4:** Compute.
>
> $$e^{-2} \approx 0.1353$$
>
> $$\boxed{P(X = 0) \approx 0.1353 = 13.53\%}$$
>
> There's approximately a **13.53%** chance of having zero server crashes next month.

---

## 4. Normal Distribution

The **Normal Distribution** (also called _Gaussian Distribution_) is the most important continuous distribution. It's the famous _bell curve_ — symmetric, centered around the mean, with data tapering off equally on both sides.

```
  The Bell Curve:

                        ┌─── 99.7% ───┐
                     ┌──┤── 95% ──├──┐
                  ┌──┤  ├── 68% ──┤  ├──┐
         ◄────────┼──┼──┼────┼────┼──┼──┼────────►
                -3σ -2σ -1σ  μ  +1σ +2σ +3σ

  Key properties:
  • Symmetric about the mean (μ)
  • Mean = Median = Mode
  • Total area under the curve = 1
  • Described entirely by μ (center) and σ (spread)
```

#### Real-World Use Cases

- **Height & Weight**: Human heights in a population follow an approximately normal distribution.
- **Test Scores**: Standardized exam scores (SAT, GRE) are designed to be normally distributed.
- **Manufacturing**: Measurements of machine-produced parts cluster around a target value.
- **Finance**: Daily stock returns are often modeled as approximately normal.
- **Central Limit Theorem**: The average of many independent random variables tends toward a normal distribution, regardless of the original distribution — this is why it appears everywhere.

#### Steps

1. Identify the mean $\mu$ and standard deviation $\sigma$ of the distribution.
2. To find probability, convert the value to a **Z-score**: $Z = \frac{X - \mu}{\sigma}$.
3. Use a Z-table (or calculator) to look up the probability corresponding to the Z-score.
4. Adjust for the type of question (less than, greater than, between).

#### Formula

The PDF of the Normal Distribution:

$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} \cdot e^{-\frac{1}{2}\left(\frac{x - \mu}{\sigma}\right)^2}
$$

Where:

|  Symbol  | Pronunciation    | Meaning                                                    |
| :------: | :--------------- | :--------------------------------------------------------- |
|  $f(x)$  | "f of x"         | The height of the curve (probability density) at value $x$ |
|  $\mu$   | "mu"             | The **mean** — center of the distribution                  |
| $\sigma$ | "sigma"          | The **standard deviation** — controls the spread/width     |
|  $\pi$   | "pi"             | The mathematical constant $\approx 3.14159$                |
|   $e$    | "Euler's number" | The mathematical constant $\approx 2.71828$                |

> In practice, you rarely compute $f(x)$ by hand. Instead, convert to Z-scores and use tables.

**Z-Score conversion:**

$$
Z = \frac{X - \mu}{\sigma}
$$

|  Symbol  | Pronunciation    | Meaning                                          |
| :------: | :--------------- | :----------------------------------------------- |
|   $Z$    | "Z" or "Z-score" | Number of standard deviations away from the mean |
|   $X$    | "X"              | The raw value you're interested in               |
|  $\mu$   | "mu"             | The mean of the distribution                     |
| $\sigma$ | "sigma"          | The standard deviation of the distribution       |

**Empirical Rule (68-95-99.7):**

|       Range       | Percentage of Data |
| :---------------: | :----------------: |
| $\mu \pm 1\sigma$ |   $\approx 68\%$   |
| $\mu \pm 2\sigma$ |   $\approx 95\%$   |
| $\mu \pm 3\sigma$ |  $\approx 99.7\%$  |

#### Examples

**Example 1** — Exam scores (finding probability below a value)

The scores of a statistics exam are normally distributed with mean $\mu = 70$ and standard deviation $\sigma = 10$. What is the probability that a randomly selected student scores **below 85**?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\mu = 70$ | Mean exam score |
> | $\sigma = 10$ | Standard deviation |
> | $X = 85$ | The score threshold |
> | Find: $P(X < 85)$ | Probability of scoring below 85 |

> **Step 1:** Convert $X = 85$ to a Z-score.
>
> $$Z = \frac{X - \mu}{\sigma} = \frac{85 - 70}{10} = \frac{15}{10} = 1.5$$
>
> **Step 2:** Look up $Z = 1.5$ in the Z-table.
>
> $P(Z < 1.5) = 0.9332$
>
> **Step 3:** Interpret the result.
>
> $$\boxed{P(X < 85) = 0.9332 = 93.32\%}$$
>
> There's a **93.32%** chance a randomly selected student scores below 85.

**Example 2** — Manufacturing (finding probability between two values)

The diameter of bolts produced by a machine is normally distributed with $\mu = 10\text{mm}$ and $\sigma = 0.2\text{mm}$. What is the probability a bolt has a diameter **between 9.8mm and 10.4mm**?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\mu = 10\text{mm}$ | Mean diameter |
> | $\sigma = 0.2\text{mm}$ | Standard deviation |
> | Find: $P(9.8 < X < 10.4)$ | Probability diameter is between 9.8mm and 10.4mm |

> **Step 1:** Convert both values to Z-scores.
>
> $$Z_1 = \frac{9.8 - 10}{0.2} = \frac{-0.2}{0.2} = -1.0$$
>
> $$Z_2 = \frac{10.4 - 10}{0.2} = \frac{0.4}{0.2} = 2.0$$
>
> **Step 2:** Look up both Z-scores in the Z-table.
>
> $P(Z < -1.0) = 0.1587$
>
> $P(Z < 2.0) = 0.9772$
>
> **Step 3:** Find the probability between the two values.
>
> $$P(9.8 < X < 10.4) = P(Z < 2.0) - P(Z < -1.0) = 0.9772 - 0.1587 = 0.8185$$
>
> $$\boxed{P(9.8 < X < 10.4) = 0.8185 = 81.85\%}$$
>
> There's an **81.85%** chance a randomly selected bolt has a diameter between 9.8mm and 10.4mm.

---

## Cumulative Distribution Function (CDF)

The **Cumulative Distribution Function** gives the probability that a random variable is **less than or equal to** a given value. It answers: "What's the probability of getting up to this value?"

$$
F(x) = P(X \le x)
$$

> The CDF is useful when you want to find probabilities in **reverse** — e.g., "What value has 90% of the data below it?"

---

## Distribution Comparison

| Feature                | Bernoulli        | Binomial                 | Poisson                        | Normal                    |
| :--------------------- | :--------------- | :----------------------- | :----------------------------- | :------------------------ |
| **Type**               | Discrete         | Discrete                 | Discrete                       | Continuous                |
| **Trials**             | 1                | $n$ (fixed)              | Not fixed (rate-based)         | N/A                       |
| **Outcomes per trial** | 2 (success/fail) | 2 (success/fail)         | Count of events                | Any real number           |
| **Parameters**         | $p$              | $n, p$                   | $\lambda$                      | $\mu, \sigma$             |
| **Mean**               | $p$              | $np$                     | $\lambda$                      | $\mu$                     |
| **Variance**           | $pq$             | $npq$                    | $\lambda$                      | $\sigma^2$                |
| **Use when…**          | One yes/no trial | Fixed # of yes/no trials | Counting events in an interval | Measuring continuous data |

---

### Key Terms

- _Bernoulli Distribution_: A distribution for a **single trial** with two outcomes (success/failure). The simplest discrete distribution.
- _Binomial Distribution_: A distribution for counting the number of successes in **$n$ independent Bernoulli trials**, each with the same probability $p$.
- _Poisson Distribution_: A distribution for counting events in a **fixed interval** when events occur at a known average rate $\lambda$.
- _Normal Distribution / Gaussian Distribution / Bell Curve_: A continuous, symmetric distribution entirely described by its mean $\mu$ and standard deviation $\sigma$.
- _PMF (Probability Mass Function)_: Gives the probability of each exact value for a discrete distribution.
- _PDF (Probability Density Function)_: Gives the height of the curve for a continuous distribution; area under the curve = probability.
- _CDF (Cumulative Distribution Function)_: Gives $P(X \le x)$ — the probability of getting a value up to $x$.
- _Empirical Rule (68-95-99.7)_: In a normal distribution, ~68% of data falls within 1σ, ~95% within 2σ, and ~99.7% within 3σ of the mean.
- _Z-score_: The number of standard deviations a value is from the mean. Converts any normal distribution to the **Standard Normal** ($\mu = 0$, $\sigma = 1$).

---

<p align="left">
  <a href="./randomVariables.md"><b>← Previous</b></a>
</p>
