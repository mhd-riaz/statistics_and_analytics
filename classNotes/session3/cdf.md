<p align="left">
  <a href="./standard-deviation-vs-standard-error.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./sampling-mean.md"><b>Next →</b></a>
  </span>
</p>

---

## Cumulative Distribution Function (CDF)

The **Cumulative Distribution Function (CDF)** answers the question: _"What is the chance that the thing I'm measuring will be **this value or less**?"_

Imagine you have a bag of candies of different weights. The CDF at 10 grams tells you the chance of randomly picking a candy that is **10 grams or lighter**. As you go to heavier and heavier values, the chance keeps going **up** (you're including more and more candies), until eventually it reaches 100% — because _every_ candy weighs _something_.

The key idea: The CDF **adds up** (accumulates) probabilities. It always starts at **0** (impossible to be less than the smallest possible value) and climbs up to **1** (or 100%) on the right side. It can _never_ go down — it only stays flat or goes up.

```
  CDF: Probability piling up as you move right

  Probability
  1.0 |                          ●●●●●●●●●●●●
      |                     ●●●●
      |                 ●●●●
  0.5 |            ●●●●
      |        ●●●●
      |    ●●●●
  0.0 |●●●●
      └──────────────────────────────────────► Values
         small                           large

  • At any point, CDF tells you: "What % of values are ≤ this?"
  • It ALWAYS goes from 0 up to 1 — never goes back down!
```

```
  Finding probability in a RANGE using CDF:

  P(a < X ≤ b) = F(b) - F(a)

         F(a)          F(b)
          │              │
  ◄───────┼──────████████┼──────────────►
          a    this area  b
               = F(b) - F(a)
```

---

#### Real-World Use Cases

- **Weather**: "What is the probability it will rain _30 mm or less_ today?" — that's a CDF question.
- **School**: "What percentage of students scored _75 or below_ on the test?" — CDF gives you the answer directly.
- **Manufacturing**: "What is the chance that a battery lasts _500 hours or less_?" — used for quality guarantees.
- **Gaming**: "What is the probability of rolling a total of _7 or less_ with two dice?" — adding up all probabilities from 2 through 7.
- **Advantage**: Unlike the PDF/PMF which gives the probability of one _exact_ value, the CDF gives you cumulative ("so far") probabilities, which is usually what we need in real life.

---

#### Steps

**For discrete data (countable things, like dice rolls):**

1. List all the possible outcomes and their probabilities.
2. Pick the value you're interested in.
3. **Add up** the probabilities of every outcome that is **equal to or less than** your value.
4. That sum is the CDF at that value.

**For continuous data (measurable things, like height or time):**

1. Know the probability density function (the curve that describes the data).
2. Pick the value you're interested in.
3. Calculate the **area under the curve** from the far left all the way up to your value.
4. That area is the CDF at that value.

---

#### Formula

**For a discrete random variable:**

$$
F(x) = P(X \le x) = \sum_{x_i \le x} P(X = x_i)
$$

**For a continuous random variable:**

$$
F(x) = P(X \le x) = \int_{-\infty}^{x} f(t)\, dt
$$

Where:

|        Symbol        | Pronunciation                                     | Meaning                                                              |
| :------------------: | :------------------------------------------------ | :------------------------------------------------------------------- |
|        $F(x)$        | "F of x"                                          | The CDF value at $x$ — the total probability up to and including $x$ |
|     $P(X \le x)$     | "probability that X is less than or equal to x"   | The chance that the random variable is at most $x$                   |
|  $\sum_{x_i \le x}$  | "the sum for all x sub i less than or equal to x" | Add up probabilities for every outcome up to $x$                     |
|     $P(X = x_i)$     | "probability that X equals x sub i"               | The probability of each individual outcome                           |
| $\int_{-\infty}^{x}$ | "the integral from negative infinity to x"        | The area under the curve from the very beginning up to $x$           |
|        $f(t)$        | "f of t"                                          | The Probability Density Function (the shape of the curve)            |
|         $dt$         | "d t"                                             | A tiny slice of the variable used for adding up the area             |

---

- _Monotonically Non-Decreasing_: A fancy way of saying the CDF can only stay the same or go up — it _never_ goes down.
- _PDF (Probability Density Function)_: For continuous data, this is the curve that shows how likely different values are. The CDF is the running total (area) under this curve.
- _PMF (Probability Mass Function)_: For discrete data, this gives the probability of each individual outcome. The CDF adds these up.

---

#### Examples

---

##### Example 1 — Discrete: Rolling a Die

You roll a fair 6-sided die. What is the probability of rolling a **4 or less**?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Outcomes $= \{1, 2, 3, 4, 5, 6\}$ | All possible results of rolling a fair die |
> | $P(X = k) = \frac{1}{6}$ for each $k$ | Each number has an equal chance |
> | Find: $F(4) = P(X \le 4)$ | Probability of rolling 4 or less |

> **Step 1:** Write the CDF formula for discrete data.
>
> $$F(4) = \sum_{x_i \le 4} P(X = x_i)$$
>
> **Step 2:** List the outcomes that are 4 or less: $1, 2, 3, 4$.
>
> $$F(4) = P(X=1) + P(X=2) + P(X=3) + P(X=4)$$
>
> **Step 3:** Plug in the probabilities.
>
> $$F(4) = \frac{1}{6} + \frac{1}{6} + \frac{1}{6} + \frac{1}{6}$$
>
> **Step 4:** Add them up.
>
> $$\boxed{F(4) = \frac{4}{6} = \frac{2}{3} \approx 0.667}$$
>
> **What this means:** There's about a **66.7%** chance of rolling a 4 or less on a single throw of a fair die. That makes sense — 4 out of 6 numbers are 4 or smaller!

---

##### Example 2 — Continuous: Uniform Distribution (Spinner Game)

Imagine a spinner that can land anywhere between **0 and 10** with equal chance (a _uniform_ distribution). What is the probability that the spinner lands on **7 or less**?

For a uniform distribution from $a$ to $b$, the CDF formula is:

$$F(x) = \frac{x - a}{b - a}$$

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $a = 0$ | The lowest value on the spinner |
> | $b = 10$ | The highest value on the spinner |
> | $x = 7$ | The value we want to check |
> | Find: $F(7)$ | Probability of landing on 7 or less |

> **Step 1:** Write the uniform CDF formula.
>
> $$F(x) = \frac{x - a}{b - a}$$
>
> **Step 2:** Plug in the values.
>
> $$F(7) = \frac{7 - 0}{10 - 0}$$
>
> **Step 3:** Simplify the numerator and denominator.
>
> $$F(7) = \frac{7}{10}$$
>
> **Step 4:** Calculate.
>
> $$\boxed{F(7) = 0.7}$$
>
> **What this means:** There's a **70% chance** the spinner lands on 7 or less. This makes intuitive sense — 7 out of 10 of the possible values are 7 or less!

---

<p align="left">
  <a href="./standard-deviation-vs-standard-error.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./sampling-mean.md"><b>Next →</b></a>
  </span>
</p>
