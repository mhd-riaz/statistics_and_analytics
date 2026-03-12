<p align="left">
  <a href="./central-limit-theorem.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./interval-estimate.md"><b>Next →</b></a>
  </span>
</p>

---

## Point Estimate

A **Point Estimate** is a single number that is your "**best guess**" for something you can't measure directly about a huge group.

Imagine you want to know the average height of _every_ 5th grader in the whole country. You can't measure millions of kids! So you measure 50 kids from your school and calculate their average height. That single number — say, 140 cm — is your **point estimate**. It's one number, one point, your best shot at guessing the truth.

There are two main types of point estimates:
- **Sample Mean** ($\bar{x}$) — to estimate the average of the whole population
- **Sample Proportion** ($\hat{p}$) — to estimate the percentage of the whole population that has a certain trait

```
  The idea of a Point Estimate:

  Population (millions of 5th graders — you can't measure all of them)
  ┌─────────────────────────────────────────┐
  │  ?   ?   ?   ?   ?   ?   ?   ?   ?   ?  │
  │  ?   ?   ?   ?   ?   ?   ?   ?   ?   ?  │   True average μ = ???
  │  ?   ?   ?   ?   ?   ?   ?   ?   ?   ?  │
  └─────────────────────────────────────────┘
                    │
         Measure a small sample
                    ▼
  Sample of 50 kids → Average = 140 cm

  Point Estimate: x̄ = 140 cm  ← your BEST GUESS for μ
```

---

#### Real-World Use Cases

- **Polls & Surveys**: "62% of people surveyed like chocolate ice cream" — the 62% is a point estimate for the whole population's preference.
- **Agriculture**: A farmer weighs 20 apples to estimate the average weight of thousands of apples in the orchard.
- **Business**: A company surveys 500 customers and uses the sample average satisfaction score as a point estimate for all customers.
- **Advantage**: It's simple — one number, easy to understand and communicate.
- **Limitation**: A point estimate gives you **no idea how close** your guess might be to the truth. That's why we also need _interval estimates_ (coming next!).

---

#### Steps

**For estimating a population mean:**

1. Take a random sample from the population.
2. Add up all the values in the sample.
3. Divide by the number of items in the sample.
4. That number is your point estimate for the population mean.

**For estimating a population proportion:**

1. Take a random sample from the population.
2. Count how many items in the sample have the trait you're interested in.
3. Divide that count by the total number of items in the sample.
4. That fraction (or percentage) is your point estimate for the population proportion.

---

#### Formula

**For estimating the Population Mean ($\mu$):**

$$
\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
$$

**For estimating the Population Proportion ($p$):**

$$
\hat{p} = \frac{x}{n}
$$

Where:

|      Symbol      | Pronunciation                  | Meaning                                                                  |
| :--------------: | :----------------------------- | :----------------------------------------------------------------------- |
|    $\bar{x}$     | "x bar"                        | The sample mean — the point estimate for the population mean             |
| $\sum_{i=1}^{n}$ | "the sum from i equals 1 to n" | Add up all the sample values                                             |
|      $x_i$       | "x sub i"                      | Each individual value in the sample                                      |
|       $n$        | "n"                            | The number of items in the sample                                        |
|    $\hat{p}$     | "p hat"                        | The sample proportion — the point estimate for the population proportion |
|       $x$        | "x"                            | The number of "successes" (items with the trait you care about)          |
|       $p$        | "p"                            | The true population proportion (the unknown value you're guessing)       |

---

- _Parameter_: A number that describes the whole population (like $\mu$ or $p$). Usually unknown.
- _Statistic_: A number that describes a sample (like $\bar{x}$ or $\hat{p}$). Calculated from your data.
- _Estimator_: The formula or rule you use to calculate a point estimate (like the mean formula).
- _Estimate_: The actual number you get after plugging in your data (like 140 cm).
- _Unbiased_: A point estimator is "unbiased" if, over many samples, the average of all the estimates equals the true population value — it doesn't consistently miss high or low.

---

#### Examples

---

##### Example 1 — Estimating a Mean (Apple Weights)

A farmer picks 5 apples at random from a huge orchard and weighs them: **150, 155, 148, 160, 152** grams. What is the point estimate for the average weight of all apples in the orchard?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Dataset $= \{150, 155, 148, 160, 152\}$ | Weights of the 5 sampled apples (in grams) |
> | $n = 5$ | Number of apples in the sample |
> | Find: $\bar{x}$ | The point estimate for the population mean |

> **Step 1:** Write the formula.
>
> $$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$
>
> **Step 2:** Add up all the values.
>
> $$\sum x_i = 150 + 155 + 148 + 160 + 152 = 765$$
>
> **Step 3:** Divide by $n$.
>
> $$\bar{x} = \frac{765}{5}$$
>
> **Step 4:** Calculate.
>
> $$\boxed{\bar{x} = 153 \text{ grams}}$$
>
> **What this means:** The farmer's best single-number guess for the average weight of _all_ apples in the orchard is **153 grams**.

---

##### Example 2 — Estimating a Proportion (Favorite Color Survey)

You ask 40 kids in your school what their favorite color is. 18 of them say **blue**. What is the point estimate for the percentage of _all_ kids in the school who like blue?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $x = 18$ | Number of kids who said "blue" |
> | $n = 40$ | Total number of kids surveyed |
> | Find: $\hat{p}$ | The point estimate for the population proportion |

> **Step 1:** Write the formula.
>
> $$\hat{p} = \frac{x}{n}$$
>
> **Step 2:** Plug in the values.
>
> $$\hat{p} = \frac{18}{40}$$
>
> **Step 3:** Calculate.
>
> $$\boxed{\hat{p} = 0.45 = 45\%}$$
>
> **What this means:** Your best guess is that about **45%** of all kids in the school like blue. But remember, this is just one guess from one survey — the real number could be a bit higher or lower!

---

<p align="left">
  <a href="./central-limit-theorem.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./interval-estimate.md"><b>Next →</b></a>
  </span>
</p>
