<p align="left">
  <a href="./cdf.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./sampling-distribution.md"><b>Next →</b></a>
  </span>
</p>

---

## Sampling Mean

The **Sampling Mean** (also called the **Sample Mean**) is simply the **average** of a small group picked from a bigger group.

Imagine there are 500 marbles in a jar, each with a number on it. You can't check all 500, so you grab a handful of 10 marbles and find the average of those 10 numbers. That average is your **sample mean**. It's your best guess for what the average of _all_ 500 marbles might be.

The cool part: if you picked your handful **randomly** (no cheating!), the sample mean is usually a pretty good guess for the real average of the whole jar.

```
  Population (all 500 marbles):
  ┌─────────────────────────────────────┐
  │  3  7  5  2  9  4  6  8  1  5  ...  │  True average (μ) = ???
  │  6  4  7  3  8  5  2  9  4  7  ...  │
  │ ...                             ... │
  └─────────────────────────────────────┘
                    │
            Pick 10 randomly
                    ▼
  Sample:  [3, 7, 5, 2, 9, 4, 6, 8, 1, 5]

  Sample Mean (x̄) = (3+7+5+2+9+4+6+8+1+5) / 10 = 5.0

  x̄ = 5.0 is our BEST GUESS for the true average μ
```

---

#### Real-World Use Cases

- **School Cafeteria**: A cafeteria manager can't ask every student what they want for lunch. They survey 30 students and use the sample mean to estimate which meal is most popular.
- **Farming**: A farmer can't weigh every apple. They weigh a sample of 20 apples to estimate the average weight of the whole harvest.
- **Hospitals**: Doctors measure the blood pressure of a group of patients to estimate the average blood pressure of the whole community.
- **Advantage**: It is an **unbiased estimator** — if you took many, many samples and averaged _all_ the sample means, you'd get exactly the true population mean.
- **Limitation**: A single sample mean is just a guess. It could be too high or too low. The more items in your sample, the better the guess.

---

#### Steps

1. Select a **random sample** from the population.
2. **Count** the number of items in your sample ($n$).
3. **Add up** all the values in the sample.
4. **Divide** the sum by $n$.
5. The result is the sample mean — your best guess for the population mean.

---

#### Formula

$$
\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
$$

Where:

|      Symbol      | Pronunciation                  | Meaning                                          |
| :--------------: | :----------------------------- | :----------------------------------------------- |
|    $\bar{x}$     | "x bar"                        | The sample mean (the average of the sample)      |
| $\sum_{i=1}^{n}$ | "the sum from i equals 1 to n" | Add up all the values from the first to the last |
|      $x_i$       | "x sub i"                      | The $i$-th individual value in the sample        |
|       $n$        | "n"                            | The total number of values in the sample         |

---

- _Population Mean ($\mu$)_: The true average of the entire population. This is usually **unknown** — it's what we're trying to estimate.
- _Sample_: A smaller group chosen from the population to represent it.
- _Unbiased Estimator_: The sample mean is "unbiased" because, on average across many samples, it hits the true population mean — it doesn't systematically overshoot or undershoot.
- _Representative Sample_: For the sample mean to be useful, the sample must be chosen **randomly**, so every member of the population has an equal chance of being picked.

---

#### Examples

---

##### Example 1 — Fun Size: Counting Candy

You buy 6 bags of candy and count the number of pieces in each bag: **12, 14, 10, 13, 15, 14**. What is the average (sample mean) number of candies per bag?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Dataset $= \{12, 14, 10, 13, 15, 14\}$ | Number of candies in each bag |
> | $n = 6$ | Total number of bags |
> | Find: $\bar{x}$ | The sample mean (average) |

> **Step 1:** Write the formula.
>
> $$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$
>
> **Step 2:** Add up all the values.
>
> $$\sum x_i = 12 + 14 + 10 + 13 + 15 + 14 = 78$$
>
> **Step 3:** Divide by the number of bags.
>
> $$\bar{x} = \frac{78}{6}$$
>
> **Step 4:** Calculate.
>
> $$\boxed{\bar{x} = 13 \text{ candies}}$$
>
> **What this means:** On average, each bag has about **13 candies**. If the company makes millions of bags, our best guess is that the typical bag has around 13 pieces.

---

##### Example 2 — Classroom: Page Counts

A librarian picks 8 books off a shelf at random and counts their pages: **120, 200, 180, 150, 220, 170, 190, 160**. What is the average number of pages?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Dataset $= \{120, 200, 180, 150, 220, 170, 190, 160\}$ | Page counts of sampled books |
> | $n = 8$ | Total number of books in the sample |
> | Find: $\bar{x}$ | The sample mean |

> **Step 1:** Write the formula.
>
> $$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$
>
> **Step 2:** Add up all the values.
>
> $$\sum x_i = 120 + 200 + 180 + 150 + 220 + 170 + 190 + 160 = 1390$$
>
> **Step 3:** Divide by the number of books.
>
> $$\bar{x} = \frac{1390}{8}$$
>
> **Step 4:** Calculate.
>
> $$\boxed{\bar{x} = 173.75 \text{ pages}}$$
>
> **What this means:** The average book on that shelf has about **174 pages**. The librarian can use this to estimate the average for the whole library section.

---

<p align="left">
  <a href="./cdf.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./sampling-distribution.md"><b>Next →</b></a>
  </span>
</p>
