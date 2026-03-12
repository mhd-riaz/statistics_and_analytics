<p align="left">
  <a href="./zscore.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./cdf.md"><b>Next →</b></a>
  </span>
</p>

---

## Standard Deviation vs Standard Error

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

**Comparison Table:**

| Feature                  | Standard Deviation (SD)          | Standard Error (SE)            |
| :----------------------- | :------------------------------- | :----------------------------- |
| **What it measures**     | Spread of individual data points | Precision of the sample mean   |
| **Focus**                | Individual values                | The average                    |
| **As sample size grows** | Stays roughly the same           | Gets smaller (more precise)    |
| **Use case**             | Describe how varied a group is   | Predict the population average |

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

<p align="left">
  <a href="./zscore.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./cdf.md"><b>Next →</b></a>
  </span>
</p>
