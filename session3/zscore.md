<p align="left">
  <a href="./readme.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./standard-deviation-vs-standard-error.md"><b>Next →</b></a>
  </span>
</p>

---

## Z-Score (Standard Score)

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

<p align="left">
  <a href="./readme.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./standard-deviation-vs-standard-error.md"><b>Next →</b></a>
  </span>
</p>
