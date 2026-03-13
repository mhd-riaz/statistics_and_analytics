<p align="left">
  <a href="./index.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./sampling-and-clt.md"><b>Next →</b></a>
  </span>
</p>

---

# Standardization

```
Standardization
├── 1. Z-Score (Standard Score)
│   ├── Population vs Sample formula
│   ├── Empirical Rule (68-95-99.7)
│   └── Outlier detection
│
├── 2. Standard Deviation vs Standard Error
│   ├── SD — spread of individual values
│   ├── SE — precision of the sample mean
│   ├── Comparison table
│   └── Bessel's Correction
│
└── 3. CDF (Cumulative Distribution Function)
    ├── Discrete CDF (summation)
    ├── Continuous CDF (integration)
    └── Using CDF for range probabilities
```

---

## 1. Z-Score (Standard Score)

A **Z-Score** tells you how far away a number is from the average, measured in "standard deviations." Think of it like a ruler that measures how normal or unusual a value is.

Imagine your class took a spelling test. The average score was 80 and most kids scored within about 5 points of 80. If you scored 90, your Z-Score tells you _exactly_ how many "steps" above average you are. A Z-Score of **0** means you got _exactly_ the average. A **positive** Z-Score means you're above average, and a **negative** Z-Score means you're below average.

When you calculate a Z-Score, you "**standardize**" the value — you convert it into a _Standard Normal Distribution_ which always has a mean of 0 and a standard deviation of 1. This lets you compare things that are normally measured on totally different scales (like test scores vs heights).

```
Where does your value sit?

Below average       Average       Above average
     ◄───────────────────┼──────────────────►
Z = -3   -2   -1         0       +1    +2   +3
          │              │              │
     Very unusual     Normal      Very unusual
```

```
         ┌────────────── 99.7% ──────────────┐
         │     ┌──────── 95% ────────┐       │
         │     │    ┌─── 68% ───┐    │       │
         │     │    │           │    │       │
◄────────┼─────┼────┼─────┼─────┼────┼───────┼────────►
       -3σ   -2σ  -1σ    x̄   +1σ  +2σ    +3σ

The Empirical Rule (68-95-99.7):
• 68% of values fall between Z = -1 and Z = +1
• 95% of values fall between Z = -2 and Z = +2
• 99.7% of values fall between Z = -3 and Z = +3
```

---

#### Real-World Use Cases

- **Education**: Comparing a student's score across different exams (e.g., did you do better in Math or English relative to the class?).
- **Healthcare**: Doctors use Z-Scores to check if a child's height or weight is normal for their age.
- **Finance**: Investors use Z-Scores to spot unusual stock price movements that may signal something important.
- **Quality Control**: Factories use Z-Scores to check if a manufactured part is within acceptable limits.
- **Limitation**: Z-Scores only work well when data follows a _normal distribution_ (bell curve). If data is very lopsided (skewed), the Z-Score can be misleading.

---

#### Steps

1. Find the **mean** (average) of the dataset.
2. Find the **standard deviation** (how spread out the data is).
3. **Subtract** the mean from your specific value.
4. **Divide** that result by the standard deviation.
5. The answer is the Z-Score — the number of standard deviations away from the mean.

---

#### Formula

**For a population:**

$$
Z = \frac{x - \mu}{\sigma}
$$

**For a sample:**

$$
Z = \frac{x - \bar{x}}{s}
$$

Where:

|  Symbol   | Pronunciation | Meaning                                                                |
| :-------: | :------------ | :--------------------------------------------------------------------- |
|    $Z$    | "Z score"     | The number of standard deviations a value is from the mean             |
|    $x$    | "x"           | The specific value you are looking at                                  |
|   $\mu$   | "mew"         | The population mean (average of the entire group)                      |
| $\sigma$  | "sigma"       | The population standard deviation (spread of the entire group)         |
| $\bar{x}$ | "x bar"       | The sample mean (average of a smaller group taken from the population) |
|    $s$    | "s"           | The sample standard deviation (spread of the smaller group)            |

---

#### Population vs Sample Notation

| Feature         | Population                              | Sample                                          |
| :-------------- | :-------------------------------------- | :---------------------------------------------- |
| **Formula**     | $Z = \frac{x - \mu}{\sigma}$            | $Z = \frac{x - \bar{x}}{s}$                     |
| **Mean symbol** | $\mu$                                   | $\bar{x}$                                       |
| **SD symbol**   | $\sigma$                                | $s$                                             |
| **When to use** | You know the full population parameters | Working with a sample drawn from the population |

---

- _Standard Normal Distribution_: A special bell curve where the mean is exactly 0 and the standard deviation is exactly 1. Every Z-Score lives on this curve.
- _Standardization_: The process of converting any normal distribution into the Standard Normal Distribution using the Z-Score formula.
- _Outlier_: A value with a Z-Score less than $-3$ or greater than $+3$ is considered very unusual and is often called an outlier.
- _Empirical Rule (68-95-99.7 Rule)_: In a normal distribution, about 68% of data falls within 1 SD, 95% within 2 SD, and 99.7% within 3 SD of the mean.

---

#### Examples

---

##### Example 1 — Test Scores (Population)

A class of students took a math test. The average score for the whole class is **75** with a standard deviation of **10**. Your friend scored **95**. How far above average is your friend?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $x = 95$ | Your friend's test score |
> | $\mu = 75$ | The average (mean) score of the class |
> | $\sigma = 10$ | The standard deviation of the scores |
> | Find: $Z$ | How many standard deviations above or below the mean |

> **Step 1:** Write down the formula.
>
> $$Z = \frac{x - \mu}{\sigma}$$
>
> **Step 2:** Plug in the values.
>
> $$Z = \frac{95 - 75}{10}$$
>
> **Step 3:** Subtract in the numerator.
>
> $$Z = \frac{20}{10}$$
>
> **Step 4:** Divide.
>
> $$\boxed{Z = 2.0}$$
>
> **What this means:** Your friend's score is exactly **2 standard deviations above** the average. Using the Empirical Rule, only about 2.5% of students scored higher than your friend — that's really great!

---

##### Example 2 — Heights (Sample)

You measure the height of 8 sunflowers in your garden. The average height is **120 cm** and the standard deviation is **15 cm**. One sunflower is only **90 cm** tall. What is its Z-Score?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $x = 90$ | The height of the short sunflower (in cm) |
> | $\bar{x} = 120$ | The sample mean height |
> | $s = 15$ | The sample standard deviation |
> | Find: $Z$ | How many standard deviations below or above the mean |

> **Step 1:** Write down the formula (sample version).
>
> $$Z = \frac{x - \bar{x}}{s}$$
>
> **Step 2:** Plug in the values.
>
> $$Z = \frac{90 - 120}{15}$$
>
> **Step 3:** Subtract in the numerator.
>
> $$Z = \frac{-30}{15}$$
>
> **Step 4:** Divide.
>
> $$\boxed{Z = -2.0}$$
>
> **What this means:** This sunflower is **2 standard deviations below** the average height. The negative sign tells us it is shorter than average. It's a pretty unusual sunflower!

---

## 2. Standard Deviation vs Standard Error

These two sound very similar, but they answer **completely different questions**.

**Standard Deviation (SD)** measures how spread out the individual values are in a dataset. Think of it like asking: _"How different are the kids in my class from each other?"_ If everyone got a similar score on a test, the SD is small. If scores were all over the place, the SD is big.

**Standard Error (SE)** measures how much the _average_ of a sample might jump around if you took many different samples. Think of it like asking: _"If I picked a different group of kids and calculated their average, how different would that new average be?"_ SE tells you how trustworthy your sample average is as a guess for the whole population.

Here's a simple way to remember:
- **SD** → How spread out are the _individual values_?
- **SE** → How reliable is the _average_?

```
Standard Deviation — spread of individual data points:

High SD:    ●       ●           ●       ●
◄──────────────────────┼──────────────────────►
                       x̄
(Scores are all over the place)

Low SD:            ● ● ● ●
◄──────────────────────┼──────────────────────►
                       x̄
(Scores are close together)
```

```
Standard Error — spread of sample averages:

Imagine taking 5 different random groups from the school:
Group 1 average: 78
Group 2 average: 81
Group 3 average: 79
Group 4 average: 80
Group 5 average: 77

These averages are close together → Small Standard Error
Your sample average is a GOOD guess for the whole school!
```

---

#### Real-World Use Cases

- **Education**: SD tells a teacher how varied the test scores are in the class. SE tells the teacher how much the class average might change if different students were tested.
- **Healthcare**: Doctors use SD to describe patient-to-patient variation in blood pressure. They use SE when reporting how precisely they know the _average_ blood pressure of a group.
- **Manufacturing**: SD describes how much individual bolts vary in size. SE describes how confident you are in the _average_ size of the batch.
- **Key Difference**: SD stays roughly the same no matter how many people you sample. SE gets _smaller_ the more people you measure — more data = more reliable average.
- **Advantage of SE**: It directly answers the question "How good is my estimate?" which is crucial for making decisions.

---

#### Steps

**To calculate Standard Deviation (sample):**

1. Find the mean ($\bar{x}$) of the dataset.
2. Subtract the mean from each value to get the **deviations**.
3. **Square** each deviation (to remove negatives).
4. **Add up** all the squared deviations.
5. **Divide** by $n - 1$ (the number of values minus one).
6. Take the **square root** of that result.

**To calculate Standard Error:**

1. First, calculate the Standard Deviation ($s$) using the steps above.
2. Find the sample size ($n$).
3. **Divide** the Standard Deviation by the square root of $n$.

---

#### Formula

**Standard Deviation (sample):**

$$
s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n - 1}}
$$

Where:

|       Symbol        | Pronunciation                  | Meaning                                                           |
| :-----------------: | :----------------------------- | :---------------------------------------------------------------- |
|         $s$         | "s"                            | The sample standard deviation                                     |
|      $\sqrt{}$      | "square root of"               | The square root, which undoes the squaring step                   |
|  $\sum_{i=1}^{n}$   | "the sum from i equals 1 to n" | Add up the values for every data point                            |
|        $x_i$        | "x sub i"                      | Each individual value in the dataset                              |
|      $\bar{x}$      | "x bar"                        | The mean (average) of the dataset                                 |
| $(x_i - \bar{x})^2$ | "x sub i minus x bar, squared" | The squared difference between each value and the mean            |
|       $n - 1$       | "n minus 1"                    | One less than the number of values (called _Bessel's correction_) |

---

**Standard Error:**

$$
SE = \frac{s}{\sqrt{n}}
$$

Where:

|   Symbol   | Pronunciation      | Meaning                                                             |
| :--------: | :----------------- | :------------------------------------------------------------------ |
|    $SE$    | "standard error"   | How much the sample mean might differ from the true population mean |
|    $s$     | "s"                | The sample standard deviation (spread of the data)                  |
| $\sqrt{n}$ | "square root of n" | The square root of the number of values in the sample               |
|    $n$     | "n"                | The total number of values in the sample                            |

---

#### Comparison Table

| Feature                  | Standard Deviation (SD)          | Standard Error (SE)            |
| :----------------------- | :------------------------------- | :----------------------------- |
| **What it measures**     | Spread of individual data points | Precision of the sample mean   |
| **Focus**                | Individual values                | The average                    |
| **As sample size grows** | Stays roughly the same           | Gets smaller (more precise)    |
| **Use case**             | Describe how varied a group is   | Predict the population average |

---

#### Population vs Sample Standard Deviation

| Feature            | Population SD ($\sigma$)                       | Sample SD ($s$)                                 |
| :----------------- | :--------------------------------------------- | :---------------------------------------------- |
| **Denominator**    | $N$ (total population size)                    | $n - 1$ (Bessel's correction)                   |
| **Formula**        | $\sigma = \sqrt{\frac{\sum (x_i - \mu)^2}{N}}$ | $s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}}$ |
| **When to use**    | You have _all_ the data                        | You have a _sample_ from a larger group         |
| **Why different?** | No correction needed — you see everything      | $n-1$ corrects for underestimating spread       |

> **Bessel's Correction**: When you only have a sample, the deviations from the sample mean tend to be _smaller_ than the deviations from the true population mean. Dividing by $n - 1$ instead of $n$ corrects this bias, giving a more accurate estimate of the population variance.

---

- _Variance_: The square of the standard deviation ($s^2$). SD is just the square root of variance.
- _Bessel's Correction_: Dividing by $n - 1$ instead of $n$ when calculating sample SD, which makes the estimate more accurate for small samples.
- _Margin of Error_: Closely related to SE — it tells you "plus or minus how much" your estimate could be off.

---

#### Examples

---

##### Example 1 — Standard Deviation (How spread out are the scores?)

Five friends measured how many minutes they spent reading yesterday: **10, 20, 15, 25, 30** minutes. How spread out are these reading times?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Dataset $= \{10, 20, 15, 25, 30\}$ | The reading times in minutes |
> | $n = 5$ | Total number of friends |
> | Find: $s$ | The sample standard deviation |

> **Step 1:** Find the mean.
>
> $$\bar{x} = \frac{10 + 20 + 15 + 25 + 30}{5} = \frac{100}{5} = 20$$
>
> **Step 2:** Subtract the mean from each value and square it.
>
> | $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
> |:---:|:---:|:---:|
> | 10 | $10 - 20 = -10$ | $100$ |
> | 20 | $20 - 20 = 0$ | $0$ |
> | 15 | $15 - 20 = -5$ | $25$ |
> | 25 | $25 - 20 = 5$ | $25$ |
> | 30 | $30 - 20 = 10$ | $100$ |
>
> **Step 3:** Add up all squared deviations.
>
> $$\sum (x_i - \bar{x})^2 = 100 + 0 + 25 + 25 + 100 = 250$$
>
> **Step 4:** Divide by $n - 1$.
>
> $$\frac{250}{5 - 1} = \frac{250}{4} = 62.5$$
>
> **Step 5:** Take the square root.
>
> $$\boxed{s = \sqrt{62.5} \approx 7.91 \text{ minutes}}$$
>
> **What this means:** On average, each friend's reading time differs from the group average by about **7.91 minutes**. That's a decent amount of spread!

---

##### Example 2 — Standard Error (How reliable is the average?)

Using the same data from Example 1 (mean = 20, SD ≈ 7.91, n = 5), how reliable is the group average of 20 minutes as a guess for the _whole school's_ average reading time?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $s = 7.91$ | The sample standard deviation from Example 1 |
> | $n = 5$ | Total number of friends |
> | Find: $SE$ | The standard error of the mean |

> **Step 1:** Write down the formula.
>
> $$SE = \frac{s}{\sqrt{n}}$$
>
> **Step 2:** Find the square root of $n$.
>
> $$\sqrt{5} \approx 2.236$$
>
> **Step 3:** Divide the standard deviation by $\sqrt{n}$.
>
> $$SE = \frac{7.91}{2.236}$$
>
> **Step 4:** Calculate.
>
> $$\boxed{SE \approx 3.54 \text{ minutes}}$$
>
> **What this means:** If you picked a _different_ group of 5 friends and found their average, that new average would probably be within about **3.54 minutes** of 20. If you asked **more** friends (say 50 instead of 5), the SE would shrink a lot, making your average a much better guess!

---

## 3. Cumulative Distribution Function (CDF)

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

#### CDF vs PDF/PMF Comparison

| Feature             | PMF / PDF                                          | CDF                                                |
| :------------------ | :------------------------------------------------- | :------------------------------------------------- |
| **Question**        | "What is the probability of _exactly_ this value?" | "What is the probability of _this value or less_?" |
| **Output range**    | 0 to 1 (PMF) or 0 to ∞ (PDF)                       | Always 0 to 1                                      |
| **Shape**           | Can go up and down                                 | Only goes up (monotonically non-decreasing)        |
| **Discrete type**   | $P(X = x)$                                         | $F(x) = \sum_{x_i \le x} P(X = x_i)$               |
| **Continuous type** | $f(x)$                                             | $F(x) = \int_{-\infty}^{x} f(t)\,dt$               |

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
  <a href="./index.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./sampling-and-clt.md"><b>Next →</b></a>
  </span>
</p>
