<p align="left">
  <a href="./point-estimate.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./confidence-and-significance.md"><b>Next →</b></a>
  </span>
</p>

---

## Interval Estimate (Confidence Interval)

An **Interval Estimate** (also called a **Confidence Interval**) is a **range** of values that you believe contains the true population value. Instead of saying "I think the answer is exactly 50," you say "I'm pretty sure the answer is **between 47 and 53**."

Think of it like a game of darts:
- A **point estimate** is like throwing _one_ dart and hoping it hits the bullseye.
- An **interval estimate** is like drawing a _circle_ around where you think the bullseye is. A bigger circle is more likely to contain the bullseye, but it's less precise.

The **confidence level** (like 95%) tells you how sure you are that your range caught the true value. A 95% confidence interval means: _"If I did this experiment 100 times, about 95 of those intervals would contain the true answer."_

```
  Point Estimate vs Interval Estimate:

  Point Estimate:      Just one number
                            ▼
  ◄─────────────────────── 50 ────────────────────────►


  Interval Estimate:   A range with cushion on both sides
                    ┌──────────┼──────────┐
  ◄─────────────── 47          50         53 ────────────────►
                    └── Margin of Error ──┘

  The TRUE value is probably somewhere in that range!
```

```
  How confidence level affects the width:

  90% Confidence:      ┌────┼────┐        Narrower, less sure
  ◄────────────────── 48   50   52 ───────────────────►

  95% Confidence:    ┌──────┼──────┐      Medium
  ◄────────────────47      50      53─────────────────►

  99% Confidence:  ┌────────┼────────┐    Wider, more sure
  ◄──────────────45        50        55───────────────►

  More confidence → Wider interval (bigger safety net)
```

---

#### Real-World Use Cases

- **News Polls**: "The candidate has 52% support, with a margin of error of ±3%." This means the interval estimate is 49% to 55%.
- **Medicine**: "The average recovery time is between 5 and 7 days" — doctors use interval estimates to report treatment effects.
- **Manufacturing**: A factory reports "Our bolts are 10mm ± 0.05mm" — an interval estimate for the true average length.
- **Advantage over Point Estimate**: An interval tells you _how precise_ your guess is. A point estimate alone gives no sense of uncertainty.
- **Trade-off**: If you want to be _more_ confident (say 99% instead of 95%), your interval gets _wider_ (less precise). You can't have both high confidence and high precision without increasing your sample size.

---

#### Steps

1. Calculate the **sample mean** ($\bar{x}$) — this is the center of your interval.
2. Find or calculate the **standard deviation** ($\sigma$ or $s$).
3. Determine the **sample size** ($n$).
4. Choose a **confidence level** (e.g., 95%) and find the corresponding **Z-score** (e.g., 1.96 for 95%).
5. Calculate the **Standard Error**: $SE = \frac{\sigma}{\sqrt{n}}$.
6. Calculate the **Margin of Error**: $ME = Z \times SE$.
7. **Subtract** the ME from $\bar{x}$ to get the **lower bound**.
8. **Add** the ME to $\bar{x}$ to get the **upper bound**.

---

#### Formula

$$
CI = \bar{x} \pm Z \times \frac{\sigma}{\sqrt{n}}
$$

Which means:

$$
\text{Lower Bound} = \bar{x} - Z \times \frac{\sigma}{\sqrt{n}}
$$

$$
\text{Upper Bound} = \bar{x} + Z \times \frac{\sigma}{\sqrt{n}}
$$

Where:

|               Symbol               | Pronunciation                     | Meaning                                                      |
| :--------------------------------: | :-------------------------------- | :----------------------------------------------------------- |
|                $CI$                | "confidence interval"             | The range (lower bound to upper bound)                       |
|             $\bar{x}$              | "x bar"                           | The sample mean — the center of the interval                 |
|               $\pm$                | "plus or minus"                   | Subtract for lower bound, add for upper bound                |
|                $Z$                 | "Z score" or "critical value"     | The number from the Z-table for your chosen confidence level |
|              $\sigma$              | "sigma"                           | The population standard deviation (or $s$ for sample)        |
|                $n$                 | "n"                               | The sample size                                              |
|     $\frac{\sigma}{\sqrt{n}}$      | "sigma over the square root of n" | The Standard Error — how much the sample mean bounces around |
| $Z \times \frac{\sigma}{\sqrt{n}}$ | "Z times the standard error"      | The Margin of Error — the cushion added on each side         |

**Common Z-Scores:**

| Confidence Level | Z-Score |
| :--------------: | :-----: |
|       90%        |  1.645  |
|       95%        |  1.960  |
|       99%        |  2.576  |

---

- _Confidence Level_: How sure you are that the interval contains the true value. **Not** the probability that the true value is in _this specific_ interval.
- _Margin of Error (ME)_: The "cushion" added on both sides of the sample mean. Smaller ME = more precise.
- _Standard Error (SE)_: Measures how wobbly the sample mean is. More data = smaller SE.
- _Critical Value_: The Z-score that corresponds to your desired confidence level.

---

#### Examples

---

##### Example 1 — Average Height (95% Confidence)

A teacher measures the height of 36 randomly chosen 5th graders. The average height is **140 cm** with a standard deviation of **12 cm**. Build a 95% confidence interval for the true average height of all 5th graders.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\bar{x} = 140$ cm | The sample mean height |
> | $\sigma = 12$ cm | The standard deviation |
> | $n = 36$ | The number of students measured |
> | $Z = 1.96$ | The Z-score for 95% confidence |
> | Find: $CI$ | The 95% confidence interval |

> **Step 1:** Calculate the Standard Error.
>
> $$SE = \frac{\sigma}{\sqrt{n}} = \frac{12}{\sqrt{36}} = \frac{12}{6} = 2 \text{ cm}$$
>
> **Step 2:** Calculate the Margin of Error.
>
> $$ME = Z \times SE = 1.96 \times 2 = 3.92 \text{ cm}$$
>
> **Step 3:** Calculate the Lower Bound.
>
> $$\text{Lower} = \bar{x} - ME = 140 - 3.92 = 136.08 \text{ cm}$$
>
> **Step 4:** Calculate the Upper Bound.
>
> $$\text{Upper} = \bar{x} + ME = 140 + 3.92 = 143.92 \text{ cm}$$
>
> **Step 5:** Write the confidence interval.
>
> $$\boxed{CI = [136.08 \text{ cm},\ 143.92 \text{ cm}]}$$
>
> **What this means:** We are **95% confident** that the true average height of _all_ 5th graders is somewhere between **136.08 cm** and **143.92 cm**. That's a pretty tight range because we measured 36 students!

---

##### Example 2 — Test Completion Time (99% Confidence)

64 students took a timed quiz. The average completion time was **45 seconds** with a standard deviation of **8 seconds**. Build a 99% confidence interval for the true average time.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\bar{x} = 45$ seconds | The sample mean time |
> | $\sigma = 8$ seconds | The standard deviation |
> | $n = 64$ | The number of students |
> | $Z = 2.576$ | The Z-score for 99% confidence |
> | Find: $CI$ | The 99% confidence interval |

> **Step 1:** Calculate the Standard Error.
>
> $$SE = \frac{\sigma}{\sqrt{n}} = \frac{8}{\sqrt{64}} = \frac{8}{8} = 1 \text{ second}$$
>
> **Step 2:** Calculate the Margin of Error.
>
> $$ME = Z \times SE = 2.576 \times 1 = 2.576 \text{ seconds}$$
>
> **Step 3:** Calculate the Lower Bound.
>
> $$\text{Lower} = 45 - 2.576 = 42.424 \text{ seconds}$$
>
> **Step 4:** Calculate the Upper Bound.
>
> $$\text{Upper} = 45 + 2.576 = 47.576 \text{ seconds}$$
>
> **Step 5:** Write the confidence interval.
>
> $$\boxed{CI = [42.42 \text{ seconds},\ 47.58 \text{ seconds}]}$$
>
> **What this means:** We are **99% confident** that the true average completion time for all students is between **42.42 and 47.58 seconds**. The interval is a bit wider than a 95% one would be, because we asked for _more_ confidence (99%), which needs a bigger safety net.

---

<p align="left">
  <a href="./point-estimate.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./confidence-and-significance.md"><b>Next →</b></a>
  </span>
</p>
