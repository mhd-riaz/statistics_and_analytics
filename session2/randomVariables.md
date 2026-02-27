<p align="left">
  <a href="./conditionalProbability.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./distribution.md"><b>Next →</b></a>
  </span>
</p>

# Random Variables

```
Random Variables
├── Random Variable (Intro)
│   ├── Definition & Intuition
│   ├── Formula: X: S → ℝ
│   └── Worked Examples
│
├── Discrete Random Variable
│   ├── Definition & Intuition
│   ├── Probability Mass Function (PMF)
│   ├── Expected Value: E(X)
│   └── Worked Examples
│
└── Continuous Random Variable
    ├── Definition & Intuition
    ├── Probability Density Function (PDF)
    └── Worked Examples
```

---

## 1. What is a Random Variable?

When you play a game — flip a coin, roll a dice, or spin a wheel — you get results like "Heads," "Tails," or "Red." But math works with **numbers**, not words. A **Random Variable** is like a **score keeper** — it turns each result into a number so we can do math with it.

**Analogy:** Imagine you flip a coin. The coin says "Heads." Your score keeper (the random variable) says "That's **1** point!" If the coin says "Tails," the score keeper says "That's **0** points." Now instead of words, you have numbers you can add, average, and calculate with.

```
  Game Result          Score Keeper (X)         Number
  ┌──────────┐         ┌──────────────┐         ┌───────┐
  │  Heads   │ ──────► │  X(Heads)    │ ──────► │   1   │
  │  Tails   │ ──────► │  X(Tails)    │ ──────► │   0   │
  └──────────┘         └──────────────┘         └───────┘
     (words)            (score keeper)           (numbers)
```

There are **two types** of random variables:

```
  Random Variables
  ├── Discrete    → you COUNT things    (1, 2, 3, ...)     → uses P(X = x)  [PMF]
  └── Continuous  → you MEASURE things  (5.2, 5.21, ...)   → uses f(x)      [PDF]
```

#### Real-World Use Cases

- **Sports**: Counting goals scored in a game ($X$ = number of goals).
- **School**: Turning letter grades into numbers (A = 4, B = 3, C = 2).
- **Business**: Number of customers who visit a shop per hour.
- **Weather**: Temperature in degrees — turning a thermometer reading into a number.
- **Why it matters**: Without random variables, we can't use formulas to calculate averages, probabilities, or predictions.

#### Steps

1. Identify the experiment (e.g., flipping a coin, rolling a die).
2. List all possible outcomes — this is the **Sample Space** $S$.
3. Assign a **number** to each outcome — this mapping IS your random variable.
4. Find the **probability** of each number.
5. Write out the **probability distribution** (a table showing each value and its probability).

#### Formula

$$
X: S \to \mathbb{R}
$$

Where:

| Symbol | Pronunciation | Meaning |
|:---:|:---|:---|
| $X$ | "X" | The random variable (the score keeper) |
| $S$ | "S" | The **Sample Space** — all possible outcomes of the experiment |
| $\to$ | "maps to" | Means "turns into" or "assigns to" |
| $\mathbb{R}$ | "the real numbers" | The set of all numbers (whole numbers, decimals, negatives) |

> This reads: "$X$ is a function that takes each outcome in the sample space $S$ and maps it to a real number."

#### Examples

**Example 1** — Flipping one coin

You flip a fair coin once. Let $X = 1$ if you get Heads, and $X = 0$ if you get Tails. Write the probability distribution.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Experiment: flip 1 fair coin | One coin is flipped once |
> | $X = 1$ for Heads | Score keeper assigns 1 to Heads |
> | $X = 0$ for Tails | Score keeper assigns 0 to Tails |
> | Find: Probability distribution of $X$ | A table showing each value and its probability |

> **Step 1:** List the Sample Space.
>
> $S = \{\text{Heads}, \text{Tails}\}$
>
> **Step 2:** Assign numbers using $X$.
>
> $X(\text{Heads}) = 1, \quad X(\text{Tails}) = 0$
>
> **Step 3:** Find the probability of each value.
>
> The coin is fair, so each side has probability $\frac{1}{2}$.
>
> $P(X = 1) = \frac{1}{2}, \quad P(X = 0) = \frac{1}{2}$
>
> **Step 4:** Write the probability distribution table.
>
> | $x$ | 0 | 1 |
> |:---:|:---:|:---:|
> | $P(X = x)$ | $\frac{1}{2}$ | $\frac{1}{2}$ |
>
> **Step 5:** Verify — do all probabilities add up to 1?
>
> $$\boxed{\frac{1}{2} + \frac{1}{2} = 1 \checkmark}$$

**Example 2** — Flipping a coin twice

You flip a fair coin **two times**. Let $X$ = the number of Heads. Write the probability distribution of $X$.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Experiment: flip a coin twice | Two flips of a fair coin |
> | $X$ = number of Heads | Score keeper counts how many Heads appear |
> | Find: Probability distribution of $X$ | Each value of $X$ and its probability |

> **Step 1:** List the Sample Space.
>
> $S = \{TT,\ TH,\ HT,\ HH\}$ — there are **4** equally likely outcomes.
>
> **Step 2:** Assign numbers using $X$ (count the Heads).
>
> | Outcome | $X$ (number of Heads) |
> |:---:|:---:|
> | TT | 0 |
> | TH | 1 |
> | HT | 1 |
> | HH | 2 |
>
> **Step 3:** Find the probability of each value of $X$.
>
> $P(X = 0) = \frac{1}{4}$ — only TT gives 0 heads
>
> $P(X = 1) = \frac{2}{4} = \frac{1}{2}$ — TH and HT both give 1 head
>
> $P(X = 2) = \frac{1}{4}$ — only HH gives 2 heads
>
> **Step 4:** Write the probability distribution table.
>
> | $x$ | 0 | 1 | 2 |
> |:---:|:---:|:---:|:---:|
> | $P(X = x)$ | $\frac{1}{4}$ | $\frac{1}{2}$ | $\frac{1}{4}$ |
>
> **Step 5:** Verify — do all probabilities add up to 1?
>
> $$\boxed{\frac{1}{4} + \frac{2}{4} + \frac{1}{4} = \frac{4}{4} = 1 \checkmark}$$

---

## 2. Discrete Random Variable

A **Discrete Random Variable** is a random variable where you can **count** the possible values. Think of things you count on your fingers: number of apples, goals scored, correct answers on a test.

**Analogy:** Imagine a bag of marbles. You reach in and count how many **red marbles** you pull out. You might get 0, 1, 2, or 3 — but you can **NEVER** get 1.5 red marbles. That "in-between" value is impossible. That's what makes it **discrete** — the values jump from one number to the next with nothing in between.

```
  Discrete: Values are SEPARATE dots (you can count them)

        ●       ●       ●       ●       ●       ●
  ◄─────┼───────┼───────┼───────┼───────┼───────┼─────►
        1       2       3       4       5       6
              (like a die — only whole numbers)

  GAPS between values — you can NEVER land between dots!
  Can you roll 3.5? NO! → That's why it's discrete.
```

We use the **Probability Mass Function (PMF)** to find the probability of each value, and the **Expected Value** $E(X)$ to find the long-run average.

#### Real-World Use Cases

- **Education**: Number of students absent per day — you can count them (0, 1, 2, ...).
- **Manufacturing**: Number of defective items in a batch of 100.
- **Tech**: Number of bugs reported in a software release.
- **Sports**: Number of goals scored in a soccer match.
- **Limitation**: Cannot represent measurements like exact height or weight — those are continuous.

#### Steps

1. List all possible values $X$ can take (e.g., 0, 1, 2, 3, ...).
2. Find the probability of **each** value using $P(X = x)$.
3. Check: all probabilities must add up to **1**.
4. (Optional) Calculate the **Expected Value** $E(X)$ — multiply each value by its probability and add them all up.

#### Formula

**Probability Mass Function (PMF):**

$$
P(X = x) \quad \text{where} \quad \sum_{\text{all } x} P(X = x) = 1
$$

Where:

| Symbol | Pronunciation | Meaning |
|:---:|:---|:---|
| $P(X = x)$ | "P of X equals x" | The probability the random variable $X$ takes the exact value $x$ |
| $\sum$ | "the sum of" | Add up all the individual probabilities |
| $= 1$ | "equals one" | All probabilities together must total 100% |

**Expected Value (Mean):**

$$
E(X) = \sum_{i=1}^{n} x_i \cdot P(X = x_i)
$$

Where:

| Symbol | Pronunciation | Meaning |
|:---:|:---|:---|
| $E(X)$ | "E of X" or "expected value of X" | The **long-run average** if you repeated the experiment forever |
| $x_i$ | "x sub i" | Each possible value of $X$ |
| $P(X = x_i)$ | "P of X equals x-sub-i" | The probability of that value |
| $\sum_{i=1}^{n}$ | "sum from i equals 1 to n" | Add up all (value × probability) pairs |

> **Important:** The expected value is a **long-run average**. If $E(X) = 3.5$ for a die roll, it does NOT mean you'll ever roll a 3.5 — that's impossible! It means if you rolled a die **thousands** of times, the average would get closer and closer to 3.5.

#### Examples

**Example 1** — Rolling a fair die

You roll a standard 6-sided die. Let $X$ = the number that lands face up. Find the **expected value** $E(X)$.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $X = \{1, 2, 3, 4, 5, 6\}$ | Possible values of the die |
> | $P(X = x) = \frac{1}{6}$ for each | Each number is equally likely |
> | $n = 6$ | Total number of possible values |
> | Find: $E(X)$ | The expected (long-run average) value |

> **Step 1:** Write the formula.
>
> $$E(X) = \sum x_i \cdot P(X = x_i)$$
>
> **Step 2:** List all values and their probabilities.
>
> | $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> | $P(X = x)$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ |
>
> **Step 3:** Multiply each value by its probability and add.
>
> $$E(X) = 1 \cdot \frac{1}{6} + 2 \cdot \frac{1}{6} + 3 \cdot \frac{1}{6} + 4 \cdot \frac{1}{6} + 5 \cdot \frac{1}{6} + 6 \cdot \frac{1}{6}$$
>
> **Step 4:** Simplify.
>
> $$E(X) = \frac{1 + 2 + 3 + 4 + 5 + 6}{6} = \frac{21}{6}$$
>
> **Step 5:** Divide.
>
> $$\boxed{E(X) = 3.5}$$
>
> This means: if you roll a die thousands of times, the average will approach **3.5** (even though you can never roll a 3.5 on a single throw).

**Example 2** — Number of Heads in 2 coin flips

Flip a fair coin **twice**. Let $X$ = number of Heads. Find $E(X)$.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $X = \{0, 1, 2\}$ | Possible number of heads |
> | $P(X = 0) = \frac{1}{4}$ | Zero heads (TT) |
> | $P(X = 1) = \frac{1}{2}$ | One head (TH or HT) |
> | $P(X = 2) = \frac{1}{4}$ | Two heads (HH) |
> | Find: $E(X)$ | The expected number of heads |

> **Step 1:** Write the formula.
>
> $$E(X) = \sum x_i \cdot P(X = x_i)$$
>
> **Step 2:** Substitute each value.
>
> $$E(X) = 0 \cdot \frac{1}{4} + 1 \cdot \frac{1}{2} + 2 \cdot \frac{1}{4}$$
>
> **Step 3:** Multiply.
>
> $$E(X) = 0 + \frac{1}{2} + \frac{2}{4}$$
>
> **Step 4:** Simplify (convert to same denominator).
>
> $$E(X) = 0 + \frac{2}{4} + \frac{2}{4} = \frac{4}{4}$$
>
> **Step 5:** Final answer.
>
> $$\boxed{E(X) = 1}$$
>
> This means: if you flip a coin twice over and over, on average you'll get **1 Head** per pair of flips.

---

## 3. Continuous Random Variable

A **Continuous Random Variable** is a random variable where you **measure** things instead of counting them. Think of height, weight, temperature, or time — these can be any decimal value. Someone can be 5.1 feet, 5.12 feet, or 5.123 feet tall — the values flow smoothly like water, with no gaps.

**Analogy:** Imagine pouring water into a measuring cup. The water level could land **ANYWHERE** — at 250ml, at 250.3ml, at 250.37ml. Unlike counting marbles (where you can only have whole numbers), measurements have **infinite** possible values between any two points. That's what makes it continuous.

```
  Continuous: Values form a SMOOTH line (infinite points between any two)

  ◄────────────────────────────────────────────────────►
  150cm    155cm    160cm    165cm    170cm    175cm
         (like height — any decimal is possible)

  KEY DIFFERENCE from discrete:

  Discrete:    ●     ●     ●     ●     ●   (separate dots, gaps between)
  Continuous:  ━━━━━━━━━━━━━━━━━━━━━━━━━━━  (smooth line, no gaps)

  ⚠️  P(X = exactly 160.000...cm) = 0   ← can't hit ONE exact point!
  ✅  P(155 ≤ X ≤ 165) = area under curve ← THIS we can find!
```

We use the **Probability Density Function (PDF)** to describe the shape of the curve, and find probability by calculating the **area under the curve** between two points.

> **Key rule:** You can NEVER find the probability of one exact value for a continuous random variable — it's always **zero**. You can only find the probability of a **range** (like "between 155cm and 165cm"). Think of it this way: what are the chances of hitting **exactly** 160.0000000...cm with infinite decimal places? Basically zero!

#### Real-World Use Cases

- **Healthcare**: Patient weight, blood pressure, body temperature — all measured on smooth scales.
- **Engineering**: Response time of a website in milliseconds (could be 120.5ms, 120.51ms, ...).
- **Manufacturing**: Exact diameter of screws, bolts, or machine parts.
- **Weather**: Temperature readings, rainfall amount, wind speed.
- **Limitation**: You can never say "the probability of **exactly** 5.0000 feet" — only "the probability of being **between** 4.9 and 5.1 feet."

#### Steps

1. Identify that the variable is **measured** (not counted) — this tells you it's continuous.
2. Define the **range** of possible values (e.g., 0 to 10 minutes).
3. Know the **PDF** $f(x)$ — the formula that describes the shape of the curve.
4. To find a probability, calculate the **area under the curve** between two values $a$ and $b$.

#### Formula

**Probability Density Function (PDF):**

$$
P(a \le X \le b) = \int_{a}^{b} f(x) \, dx
$$

Where:

| Symbol | Pronunciation | Meaning |
|:---:|:---|:---|
| $P(a \le X \le b)$ | "probability that X is between a and b" | The chance the value falls in the range from $a$ to $b$ |
| $\int_{a}^{b}$ | "the integral from a to b" | Means "add up all the tiny slices" = **area under the curve** |
| $f(x)$ | "f of x" | The density function — tells you the **height** of the curve at each point |
| $dx$ | "dx" | A tiny slice of the x-axis |

> **Simplified version (Uniform Distribution):** When all values are **equally likely**, the area is just a rectangle, and the formula simplifies to:
>
> $$P(a \le X \le b) = \frac{b - a}{d - c}$$
>
> Where $[c, d]$ is the total range. This is just: **width you want** ÷ **total width**.

> **Rule:** The total area under the entire curve always equals 1:
> $$\int_{-\infty}^{\infty} f(x) \, dx = 1$$

#### Examples

**Example 1** — Bus waiting time (Uniform Distribution)

A bus arrives every **10 minutes**. You show up at a random time. What is the probability you wait between **2 and 5 minutes**?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Range $= [0, 10]$ minutes | You could wait anywhere from 0 to 10 min |
> | Uniform distribution | All wait times are equally likely |
> | $f(x) = \frac{1}{10} = 0.1$ | Height of the PDF (constant for uniform) |
> | Find: $P(2 \le X \le 5)$ | Probability of waiting between 2 and 5 min |

> **Step 1:** Since all times are equally likely, use the simplified uniform formula.
>
> $$P(a \le X \le b) = \frac{b - a}{d - c}$$
>
> **Step 2:** Identify the values.
>
> $a = 2$, $b = 5$ (the range we want)
> $c = 0$, $d = 10$ (the total range)
>
> **Step 3:** Substitute.
>
> $$P(2 \le X \le 5) = \frac{5 - 2}{10 - 0} = \frac{3}{10}$$
>
> **Step 4:** Simplify.
>
> $$\boxed{P(2 \le X \le 5) = 0.3 = 30\%}$$
>
> There's a **30%** chance you wait between 2 and 5 minutes.

**Example 2** — Spinner game (Uniform Distribution)

A game spinner is marked from **0 to 8**. It can land at any point with equal probability. What is the probability it lands between **1 and 6**?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Range $= [0, 8]$ | Spinner goes from 0 to 8 |
> | Uniform distribution | All positions are equally likely |
> | $f(x) = \frac{1}{8} = 0.125$ | Height of the PDF (constant) |
> | Find: $P(1 \le X \le 6)$ | Probability of landing between 1 and 6 |

> **Step 1:** Use the simplified uniform formula.
>
> $$P(a \le X \le b) = \frac{b - a}{d - c}$$
>
> **Step 2:** Identify the values.
>
> $a = 1$, $b = 6$ (the range we want)
> $c = 0$, $d = 8$ (the total range)
>
> **Step 3:** Substitute.
>
> $$P(1 \le X \le 6) = \frac{6 - 1}{8 - 0} = \frac{5}{8}$$
>
> **Step 4:** Simplify.
>
> $$\boxed{P(1 \le X \le 6) = \frac{5}{8} = 0.625 = 62.5\%}$$
>
> There's a **62.5%** chance the spinner lands between 1 and 6.

---

## Discrete vs Continuous — Quick Comparison

| Feature | Discrete | Continuous |
|:---|:---|:---|
| **What you do** | COUNT things | MEASURE things |
| **Values** | Separate, with gaps (0, 1, 2, 3...) | Smooth, no gaps (any decimal) |
| **Examples** | Goals, students, dice rolls | Height, weight, time, temperature |
| **Probability of exact value** | Can be > 0 (e.g., $P(X=3) = \frac{1}{6}$) | Always = 0 |
| **Probability function** | PMF: $P(X = x)$ | PDF: $f(x)$ → area under curve |
| **Probabilities add up to** | $\sum P(X = x) = 1$ | $\int f(x) \, dx = 1$ |
| **Notation** | Lowercase $p$ | Lowercase $f$ |

---

### Key Terms

- _Random Variable_: A function (score keeper) that turns experiment outcomes into numbers. Denoted by a capital letter like $X$.
- _Discrete Random Variable_: Values are **countable** with gaps between them (0, 1, 2, 3...). Uses the PMF.
- _Continuous Random Variable_: Values are **measurable** and flow smoothly (any decimal). Uses the PDF.
- _PMF (Probability Mass Function)_: Gives the probability of each **exact** value for a discrete random variable.
- _PDF (Probability Density Function)_: Gives the **height of the curve** for a continuous random variable. Area under the curve = probability.
- _Expected Value $E(X)$_: The long-run average — what you'd get if you repeated the experiment forever.
- _Sample Space ($S$)_: All possible outcomes of an experiment.

---

<p align="left">
  <a href="./conditionalProbability.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./distribution.md"><b>Next →</b></a>
  </span>
</p>