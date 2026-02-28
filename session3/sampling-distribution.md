<p align="left">
  <a href="./sampling-mean.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./point-estimate.md"><b>Next →</b></a>
  </span>
</p>

---

## Sampling Distribution & Central Limit Theorem

### What is a Sampling Distribution?

A **Sampling Distribution** is what you get when you take _many_ samples from a population, calculate the mean of each sample, and then look at how all those means are spread out.

Think of it this way: you grab 10 jellybeans from a giant jar and find the average weight. Then you put them back, grab 10 _different_ jellybeans, and find _that_ average. Do this 100 times. Now you have 100 averages. If you line up all those averages on a number line, that's the **sampling distribution of the mean**.

### What is the Central Limit Theorem (CLT)?

The **Central Limit Theorem** is like a magic rule in statistics. It says:

> _No matter what the original data looks like (lopsided, flat, weird shapes), if you take **big enough samples** (usually 30 or more) and calculate their averages, those averages will always form a **bell curve** (normal distribution)._

This is incredible because it means you can use "bell curve math" on _any_ dataset, as long as your sample is large enough!

```
  Original population (could be ANY shape):

  Skewed:     ████
              ██████
              ████████
              ██████████
              ██████████████
  ◄──────────────────────────────►

              │  Take many samples of size n ≥ 30
              │  and compute each sample's mean
              ▼

  Sampling Distribution of Means (always a bell curve!):

                    ▄▄▄▄
                 ▄▄██████▄▄
              ▄▄██████████████▄▄
           ▄▄██████████████████████▄▄
  ◄────────────────────┼────────────────────►
                       μ
                 (population mean)
```

```
  How sample size affects the sampling distribution:

  Small samples (n = 5):    Wide, short bell curve
           ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ◄────────────────┼────────────────────►

  Large samples (n = 100):   Narrow, tall bell curve
                  ▄████▄
  ◄────────────────┼────────────────────►
                   μ

  Bigger samples → Narrower curve → More precise estimates!
```

---

#### Real-World Use Cases

- **Polling / Elections**: Pollsters survey ~1,000 people and predict how millions will vote. CLT is the reason this works!
- **Quality Control**: A factory tests 50 batteries and uses the average lifespan to predict the average for the entire production line.
- **Medicine**: Doctors test a drug on 200 patients and use CLT to estimate the drug's average effect on the whole population.
- **Key Rule**: Sample size should be **at least 30** for CLT to kick in. If the population is already bell-shaped, even smaller samples work.
- **Precision**: The more items in each sample, the _narrower_ the bell curve of averages becomes — meaning your estimate is more precise.

---

#### Steps

1. Have a population with a mean ($\mu$) and standard deviation ($\sigma$).
2. Take a random sample of size $n$ (ideally $n \ge 30$).
3. Calculate the **sample mean** ($\bar{x}$).
4. Repeat steps 2–3 many times.
5. The collection of all those sample means forms a **bell curve** centered at $\mu$.
6. The spread of that bell curve (the **Standard Error**) is $\frac{\sigma}{\sqrt{n}}$.

---

#### Formula

The sampling distribution of the mean follows:

$$
\bar{X} \sim N\left(\mu,\ \frac{\sigma^2}{n}\right)
$$

The mean and standard error of the sampling distribution:

$$
\mu_{\bar{x}} = \mu
$$

$$
\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}
$$

Where:

|          Symbol           | Pronunciation                           | Meaning                                              |
| :-----------------------: | :-------------------------------------- | :--------------------------------------------------- |
|         $\bar{X}$         | "X bar"                                 | The random variable representing the sample mean     |
|         $\sim N$          | "follows a normal distribution"         | The sample means are normally distributed            |
|           $\mu$           | "mew"                                   | The mean of the original population                  |
|      $\mu_{\bar{x}}$      | "mew sub x bar"                         | The mean of the sampling distribution (equals $\mu$) |
|         $\sigma$          | "sigma"                                 | The standard deviation of the original population    |
|    $\sigma_{\bar{x}}$     | "sigma sub x bar"                       | The standard error — the spread of the sample means  |
|            $n$            | "n"                                     | The number of items in each sample                   |
| $\frac{\sigma}{\sqrt{n}}$ | "sigma divided by the square root of n" | How to calculate the standard error                  |

---

- _Normal Distribution / Bell Curve_: A symmetric, mountain-shaped curve where most values are near the middle and fewer are at the edges.
- _Standard Error_: The standard deviation of the sampling distribution — it tells you how much sample means bounce around.
- _Law of Large Numbers_: A related idea — as your sample size grows, the sample mean gets closer and closer to the true population mean.

---

#### Examples

---

##### Example 1 — Jellybean Jar

A giant jar of 10,000 jellybeans has an average weight of $\mu = 5$ grams with a standard deviation of $\sigma = 2$ grams. You grab a handful of 36 jellybeans and find their average weight. What is the standard error (how much will your handtful's average bounce around)?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\mu = 5$ grams | The population mean weight |
> | $\sigma = 2$ grams | The population standard deviation |
> | $n = 36$ | Number of jellybeans in each sample |
> | Find: $\sigma_{\bar{x}}$ | The standard error of the sampling mean |

> **Step 1:** Write the formula for standard error.
>
> $$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$$
>
> **Step 2:** Find the square root of $n$.
>
> $$\sqrt{36} = 6$$
>
> **Step 3:** Divide $\sigma$ by $\sqrt{n}$.
>
> $$\sigma_{\bar{x}} = \frac{2}{6}$$
>
> **Step 4:** Calculate.
>
> $$\boxed{\sigma_{\bar{x}} = 0.333 \text{ grams}}$$
>
> **What this means:** If you keep grabbing groups of 36 jellybeans and finding the average, most of those averages will be within about **0.33 grams** of the true mean of 5 grams. The sampling distribution is centered at 5 and has a very small spread!

---

##### Example 2 — Battery Lifespan (Using Z-Score with CLT)

A battery company claims their batteries last $\mu = 500$ hours on average with $\sigma = 40$ hours. A tester samples 64 batteries and gets an average of 490 hours. How unusual is this result?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\mu = 500$ hours | The claimed population mean |
> | $\sigma = 40$ hours | The population standard deviation |
> | $n = 64$ | Number of batteries sampled |
> | $\bar{x} = 490$ hours | The observed sample mean |
> | Find: $Z$ and the probability | How unusual is this result? |

> **Step 1:** Calculate the Standard Error.
>
> $$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{40}{\sqrt{64}} = \frac{40}{8} = 5 \text{ hours}$$
>
> **Step 2:** Calculate the Z-Score for the sample mean.
>
> $$Z = \frac{\bar{x} - \mu}{\sigma_{\bar{x}}} = \frac{490 - 500}{5} = \frac{-10}{5}$$
>
> **Step 3:** Simplify.
>
> $$\boxed{Z = -2}$$
>
> **Step 4:** Look up $Z = -2$ — this corresponds to about **2.28%**.
>
> **What this means:** There's only a **2.28% chance** of getting an average as low as 490 if the batteries truly last 500 hours on average. That's pretty unlikely! The tester might suspect the company's claim is wrong.

---

<p align="left">
  <a href="./sampling-mean.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./point-estimate.md"><b>Next →</b></a>
  </span>
</p>
