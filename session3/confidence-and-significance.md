<p align="left">
  <a href="./interval-estimate.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./readme.md"><b>Back to Index →</b></a>
  </span>
</p>

---

## Confidence Level vs Significance Level

These are two sides of the **same coin**. They always add up to **1** (or 100%).

**Confidence Level** is how sure you are that your result is correct. Think of it like this: if you say _"I'm 95% confident,"_ you're saying _"I'm really, really sure — 95 out of 100 times, I'd be right."_

**Significance Level** ($\alpha$, pronounced "alpha") is how much risk of being wrong you're willing to accept. If you're 95% confident, that means you accept a 5% chance of being wrong. That 5% is your significance level.

Here's a simple analogy: Imagine you're crossing a river on stepping stones.
- The **Confidence Level** is the percentage of stones that are _safe_ to step on.
- The **Significance Level** is the percentage of stones that are _wobbly_ and might make you fall.
- If 95% of stones are safe, then 5% are wobbly. Together: 95% + 5% = 100%.

```
  The Confidence Level and Significance Level together = 100%

  ┌──────────────────────────────────────────────────────┐
  │                                                      │
  │     α/2          Confidence Level (C)        α/2     │
  │   ┌─────┐  ┌─────────────────────────┐  ┌─────┐      │
  │   │/////│  │                         │  │/////│      │
  │   │/////│  │       95% safe zone     │  │/////│      │
  │   │/////│  │                         │  │/////│      │
  │   └─────┘  └─────────────────────────┘  └─────┘      │
  │    2.5%              95%                  2.5%       │
  │                                                      │
  │                  α = 5% total                        │
  │           (split into two tails)                     │
  └──────────────────────────────────────────────────────┘
```

```
  Quick Reference:

  Confidence Level    Significance Level (α)    How sure?
  ─────────────────   ──────────────────────    ─────────
       90%                  0.10 (10%)          Pretty sure
       95%                  0.05  (5%)          Very sure
       99%                  0.01  (1%)          Extremely sure
```

---

#### Real-World Use Cases

- **Science Experiments**: Scientists usually set $\alpha = 0.05$ before running an experiment. This means they accept a 5% risk of thinking they found something when they actually didn't.
- **Medicine**: Drug trials often use 99% confidence (α = 0.01) because the stakes are very high — a mistake could harm patients.
- **School Projects**: If you're testing whether a new study method helps kids learn faster, you might use 95% confidence — you want to be quite sure before telling everyone about it.
- **Key Rule**: You _choose_ the significance level **before** you run your experiment, not after!
- **Trade-off**: Higher confidence (like 99%) means you're less likely to make a mistake, but you might also miss real discoveries because your bar is set so high.

---

#### Steps

1. **Choose** a confidence level (like 90%, 95%, or 99%).
2. **Calculate** the significance level: $\alpha = 1 - C$.
3. **Interpret** the confidence level: "I am $C$% sure my result is correct."
4. **Interpret** the significance level: "I accept an $\alpha$% risk of being wrong."

Or, if given $\alpha$:

1. **Calculate** the confidence level: $C = 1 - \alpha$.

---

#### Formula

$$
C = 1 - \alpha
$$

$$
\alpha = 1 - C
$$

Where:

|  Symbol  | Pronunciation             | Meaning                                                                                 |
| :------: | :------------------------ | :-------------------------------------------------------------------------------------- |
|   $C$    | "C" or "confidence level" | The probability that your method gives a correct result (e.g., 0.95 or 95%)             |
| $\alpha$ | "alpha"                   | The significance level — the risk of a false positive / Type I error (e.g., 0.05 or 5%) |
|   $1$    | "one"                     | Represents 100% — total certainty                                                       |

---

**Comparison Table:**

| Feature               | Confidence Level ($C$)     | Significance Level ($\alpha$)         |
| :-------------------- | :------------------------- | :------------------------------------ |
| **What it measures**  | How sure you are           | How much risk you accept              |
| **Typical values**    | 90%, 95%, 99%              | 0.10, 0.05, 0.01                      |
| **Where it's used**   | Confidence Intervals       | Hypothesis Testing                    |
| **On the bell curve** | The big area in the middle | The small areas in the tails          |
| **Interpretation**    | "I am 95% confident"       | "I accept a 5% chance of being wrong" |

---

- _Null Hypothesis_: The default assumption that nothing special is happening (e.g., "this new method has no effect"). Hypothesis testing tries to decide whether to reject this.
- _Type I Error (False Positive)_: Saying "something is happening!" when actually it's just random chance. The significance level ($\alpha$) is exactly the risk of making this mistake.
- _Type II Error (False Negative)_: Saying "nothing is happening" when something actually _is_. This is a different kind of mistake, controlled by the concept of _power_.
- _Critical Region_: The "danger zone" in the tails of the bell curve. If your test result falls here, you reject the null hypothesis.

---

#### Examples

---

##### Example 1 — From Confidence Level to Significance Level

You're doing a science fair project testing whether plants grow taller with music. You decide to be **95% confident** in your results. What is your significance level?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $C = 0.95$ | The chosen confidence level (95%) |
> | Find: $\alpha$ | The significance level |

> **Step 1:** Write the formula.
>
> $$\alpha = 1 - C$$
>
> **Step 2:** Plug in the confidence level.
>
> $$\alpha = 1 - 0.95$$
>
> **Step 3:** Calculate.
>
> $$\boxed{\alpha = 0.05 = 5\%}$$
>
> **What this means:** You are accepting a **5% risk** of incorrectly concluding that music helps plant growth when it actually doesn't. In other words, 5 times out of 100, you _might_ be fooled by random luck.

---

##### Example 2 — From Significance Level to Confidence Level

A doctor is testing a new medicine. Because this affects people's health, the doctor sets a very strict significance level of $\alpha = 0.01$. What is the confidence level?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $\alpha = 0.01$ | The chosen significance level (1%) |
> | Find: $C$ | The confidence level |

> **Step 1:** Write the formula.
>
> $$C = 1 - \alpha$$
>
> **Step 2:** Plug in the significance level.
>
> $$C = 1 - 0.01$$
>
> **Step 3:** Calculate.
>
> $$\boxed{C = 0.99 = 99\%}$$
>
> **What this means:** The doctor is **99% confident** in the results. They only accept a tiny **1% risk** of being wrong. This is important in medicine — you need to be _very_ sure a drug works before giving it to patients!

---

<p align="left">
  <a href="./interval-estimate.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./readme.md"><b>Back to Index →</b></a>
  </span>
</p>
