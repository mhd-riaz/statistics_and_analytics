<p align="left">
  <a href="../session1/visualization.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./events.md"><b>Next →</b></a>
  </span>
</p>

# Probability Fundamentals

```
Probability Fundamentals
├── Probability
│   ├── Definition & Formula
│   ├── Fundamentals (Sample Space, Events, Complements, Independence)
│   └── Worked Examples
│
├── Experiment vs. Trial
│   ├── Definition
│   └── Worked Examples
│
├── P(A) vs. P(E) — Notation
│   ├── Definition
│   └── Worked Examples
│
└── Sample Space & Cardinalities
    ├── Identifying the Sample Space
    ├── Determining Cardinality
    ├── Fundamental Counting Principle
    └── Worked Examples
```

---

## 1. Probability

**Probability** is the branch of mathematics that quantifies uncertainty. It measures the likelihood of an **event** occurring, expressed as a number between 0 and 1, where 0 indicates impossibility and 1 indicates certainty.

```
  Impossible                                  Certain
       0 ─────────────────────────────────────── 1
       |           |           |           |
      0.0        0.25        0.50        0.75
   "No chance"  "Unlikely"  "Even odds" "Likely"

  Examples:
  ● Rolling a 7 on a standard die → P = 0
  ● Flipping heads on a fair coin → P = 0.5
  ● Sun rising tomorrow           → P ≈ 1
```

#### Real-World Use Cases

- **Finance**: Estimating the probability of a stock price increase to inform investment decisions.
- **Healthcare**: Calculating the likelihood of a patient testing positive for a disease given symptoms.
- **Insurance**: Determining the probability of claims to set premium prices.
- **Weather Forecasting**: Expressing the chance of rain, snow, or sunshine on a given day.
- **Limitation**: Probability calculations assume a well-defined sample space — real-world events can be harder to model precisely.

#### Steps

1. Identify the **experiment** being performed.
2. List all possible outcomes — this is the **sample space** ($S$).
3. Identify the **favorable outcomes** for the event in question.
4. Divide the number of favorable outcomes by the total number of outcomes.

#### Formula

$$
P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}} = \frac{n(A)}{n(S)}
$$

Where:

| Symbol | Pronunciation | Meaning                                          |
| :----: | :------------ | :----------------------------------------------- |
| $P(A)$ | "P of A"      | The probability of event A occurring             |
| $n(A)$ | "n of A"      | The number of outcomes favorable to event A      |
| $n(S)$ | "n of S"      | The total number of outcomes in the sample space |

#### Key Concepts

- _Sample Space_ ($S$): The set of all possible outcomes of an experiment. For a coin toss, $S = \{H, T\}$.
- _Event_ ($E$): A subset of the sample space. Rolling an even number on a die is an event: $E = \{2, 4, 6\}$.
- _Complementary Event_ ($A'$): The probability that an event does **not** occur: $P(A') = 1 - P(A)$.
- _Independent Events_: The outcome of one event does not affect the other (e.g., tossing two separate coins).
- _Dependent Events_: The outcome of one event affects the likelihood of the next (e.g., drawing cards without replacement).

#### Examples

**Example 1** — Drawing a marble from a bag

You have a bag containing **10 marbles**: 3 are red, 5 are blue, and 2 are green. If you reach in and grab one marble without looking, what is the probability of picking a red one?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Bag contains 3 red, 5 blue, 2 green marbles | The set of objects |
> | Total marbles $= 10$ | Total number of possible outcomes |
> | $n(A) = 3$ | Number of red marbles (favorable outcomes) |
> | Find: $P(\text{Red})$ | Probability of drawing a red marble |

> **Step 1:** Write down the formula.
>
> $$P(A) = \frac{n(A)}{n(S)}$$
>
> **Step 2:** Identify the values.
>
> Favorable outcomes: $n(A) = 3$ (red marbles)
> Total outcomes: $n(S) = 10$ (all marbles)
>
> **Step 3:** Substitute into the formula.
>
> $$P(\text{Red}) = \frac{3}{10}$$
>
> **Step 4:** Simplify.
>
> $$\boxed{P(\text{Red}) = 0.3 \text{ or } 30\%}$$

**Example 2** — Rolling a die for a number greater than 4

You roll a standard 6-sided die once. What is the probability that the number you roll is greater than 4?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Standard 6-sided die | The experiment |
> | $S = \{1, 2, 3, 4, 5, 6\}$ | Sample space |
> | $A = \{5, 6\}$ | Favorable outcomes (numbers > 4) |
> | $n(S) = 6$ | Total possible outcomes |
> | $n(A) = 2$ | Count of favorable outcomes |
> | Find: $P(A)$ | Probability of rolling greater than 4 |

> **Step 1:** Write down the formula.
>
> $$P(A) = \frac{n(A)}{n(S)}$$
>
> **Step 2:** Identify the values.
>
> Favorable outcomes: $A = \{5, 6\}$, so $n(A) = 2$
> Total outcomes: $n(S) = 6$
>
> **Step 3:** Substitute into the formula.
>
> $$P(A) = \frac{2}{6}$$
>
> **Step 4:** Simplify.
>
> $$P(A) = \frac{1}{3}$$
>
> **Step 5:** Express as a decimal.
>
> $$\boxed{P(A) \approx 0.333 \text{ or } 33.3\%}$$

---

## 2. Experiment vs. Trial

An **experiment** is a structured process or investigation intended to discover, verify, or demonstrate a particular fact. A **trial** is a single performance or observation within that experiment. Think of the experiment as the "whole project" and the trial as "one single attempt."

```
  Experiment (the whole process)
  ┌──────────────────────────────────────────────┐
  │  Trial 1   Trial 2   Trial 3   ...  Trial n  │
  │    ↓         ↓         ↓               ↓     │
  │    H         T         H        ...    T     │
  └──────────────────────────────────────────────┘
         Flip a coin n times → record results
```

#### Real-World Use Cases

- **Pharmaceutical Testing**: The clinical study is the experiment; each patient's response is a trial.
- **Manufacturing**: Quality testing a batch of products is the experiment; inspecting one unit is a trial.
- **Education**: A standardized exam session is the experiment; each student's attempt is a trial.
- **Sports Analytics**: A season of games is the experiment; each game is a trial.

#### Steps

1. Define the overall **experiment** (what are you investigating?).
2. Identify what constitutes a single **trial** (one repetition of the action).
3. Determine $n$ — the total number of trials.
4. Record the outcome of each trial.

#### Formula

$$
\text{Experiment} = \sum_{i=1}^{n} \text{Trial}_i
$$

Where:

|       Symbol        | Pronunciation                  | Meaning                                         |
| :-----------------: | :----------------------------- | :---------------------------------------------- |
| $\text{Experiment}$ | "experiment"                   | The total collection of all repeated attempts   |
|  $\sum_{i=1}^{n}$   | "the sum from i equals 1 to n" | Add up all trials from the first to the last    |
|  $\text{Trial}_i$   | "trial sub i"                  | The i-th single, individual attempt             |
|         $n$         | "n"                            | The total number of times the trial is repeated |

#### Examples

**Example 1** — Coin fairness test

You want to test whether a coin is fair, so you decide to flip it **50 times** and record the results. Identify the experiment and the trial in this scenario.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Flip a coin 50 times | The experiment |
> | Each single coin flip | One trial |
> | $n = 50$ | Total number of trials |
> | Find: What is the experiment and what is the trial? | Identify each component |

> **Step 1:** Identify the experiment.
>
> The **experiment** is the entire process of flipping a coin 50 times and recording results to determine if the coin is fair.
>
> **Step 2:** Identify the trial.
>
> Each individual coin flip is a **trial**. The 1st flip is Trial 1, the 2nd flip is Trial 2, ..., the 50th flip is Trial 50.
>
> **Step 3:** Express using the formula.
>
> $$\boxed{\text{Experiment} = \sum_{i=1}^{50} \text{Trial}_i = \text{Trial}_1 + \text{Trial}_2 + \dots + \text{Trial}_{50}}$$

**Example 2** — Battery lifespan test

A student is doing a science fair project to find out which of **3 brands** of batteries lasts the longest. She tests each battery by running it in a flashlight until it dies. Identify the experiment and the trial.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Test 3 brands of batteries | The experiment |
> | Running one battery until it dies | One trial |
> | $n = 3$ | Total number of trials (one per brand) |
> | Find: What is the experiment and what is the trial? | Identify each component |

> **Step 1:** Identify the experiment.
>
> The **experiment** is the entire investigation of testing which brand of battery lasts the longest by running each until depletion.
>
> **Step 2:** Identify the trial.
>
> Testing **one specific battery** until it dies is a single **trial**.
>
> **Step 3:** Express using the formula.
>
> $$\boxed{\text{Experiment} = \sum_{i=1}^{3} \text{Trial}_i = \text{Trial}_1 + \text{Trial}_2 + \text{Trial}_3}$$

---

## 3. P(A) vs. P(E) — Notation

In probability notation, **P(A)** and **P(E)** are functionally the same thing — they both represent the probability of a specific outcome occurring. The letter inside the parentheses is simply a label or "placeholder" for an event. Traditionally, **"E"** stands for **Event**, while **"A"** (along with B and C) is used as a generic variable to distinguish between different specific events in the same problem.

```
  Same formula, different labels:

  P(E) ─── "Let E = rolling an even number"  ──→ P(E) = 3/6 = 0.5
  P(A) ─── "Let A = rolling a 5"             ──→ P(A) = 1/6 ≈ 0.167
  P(B) ─── "Let B = rolling less than 3"     ──→ P(B) = 2/6 ≈ 0.333

  The letter is just a name tag — the math is identical.
```

#### Real-World Use Cases

- **Multi-event problems**: Using $P(A)$, $P(B)$, $P(C)$ to distinguish different outcomes in the same experiment.
- **Textbooks & exams**: Different authors may prefer $E$ vs. $A$ — understanding they are equivalent avoids confusion.
- **Conditional probability**: Expressions like $P(A|B)$ rely on distinct labels to separate the two events.
- **Communication**: Labeling events clearly makes complex probability problems readable and unambiguous.

#### Steps

1. Define the experiment and its sample space.
2. Assign a **label** (A, B, E, etc.) to each event of interest.
3. Count the favorable outcomes for each labeled event.
4. Apply the probability formula using the chosen label.

#### Formula

$$
P(A) = P(E) = \frac{n}{N}
$$

Where:

|   Symbol   | Pronunciation | Meaning                                                |
| :--------: | :------------ | :----------------------------------------------------- |
|    $P$     | "P"           | The probability function                               |
| $A$ or $E$ | "A" or "E"    | The specific event we are measuring (just a label)     |
|    $n$     | "n"           | Number of favorable/successful outcomes for that event |
|    $N$     | "capital N"   | Total possible outcomes in the sample space            |

#### Examples

**Example 1** — Using P(E) for rolling an even number

You roll a standard 6-sided die once. Let $E$ be the event of rolling an even number. What is $P(E)$?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Standard 6-sided die | The experiment |
> | $S = \{1, 2, 3, 4, 5, 6\}$ | Sample space |
> | $E = \{2, 4, 6\}$ | Event: rolling an even number |
> | $n = 3$ | Number of favorable outcomes |
> | $N = 6$ | Total possible outcomes |
> | Find: $P(E)$ | Probability of rolling an even number |

> **Step 1:** Write down the formula.
>
> $$P(E) = \frac{n}{N}$$
>
> **Step 2:** Identify the values.
>
> Favorable outcomes: $E = \{2, 4, 6\}$, so $n = 3$
> Total outcomes: $N = 6$
>
> **Step 3:** Substitute into the formula.
>
> $$P(E) = \frac{3}{6}$$
>
> **Step 4:** Simplify.
>
> $$\boxed{P(E) = \frac{1}{2} = 0.5 \text{ or } 50\%}$$

**Example 2** — Using P(A) for rolling a specific number

You roll a standard 6-sided die once. Let $A$ be the event of rolling a 5. What is $P(A)$?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Standard 6-sided die | The experiment |
> | $S = \{1, 2, 3, 4, 5, 6\}$ | Sample space |
> | $A = \{5\}$ | Event: rolling a 5 |
> | $n = 1$ | Number of favorable outcomes |
> | $N = 6$ | Total possible outcomes |
> | Find: $P(A)$ | Probability of rolling a 5 |

> **Step 1:** Write down the formula.
>
> $$P(A) = \frac{n}{N}$$
>
> **Step 2:** Identify the values.
>
> Favorable outcomes: $A = \{5\}$, so $n = 1$
> Total outcomes: $N = 6$
>
> **Step 3:** Substitute into the formula.
>
> $$P(A) = \frac{1}{6}$$
>
> **Step 4:** Simplify.
>
> $$\boxed{P(A) = \frac{1}{6} \approx 0.167 \text{ or } 16.7\%}$$

---

## 4. Sample Space and Cardinalities

**Sample Space** ($S$) is the set of all possible outcomes of a random experiment. <br>
**Cardinality**, denoted as $|S|$ or $n(S)$, is the total number of elements or outcomes contained within that sample space — it tells you "how many" possible results exist.

```
  Experiment          Sample Space (S)                    |S|
  ───────────         ────────────────                    ───
  Coin flip           {H, T}                               2
  Die roll            {1, 2, 3, 4, 5, 6}                   6
  Coin + Die          {(H,1),(H,2),...,(T,5),(T,6)}       12

  Fundamental Counting Principle:
  ┌────────────┐     ┌────────────┐
  │  Coin: 2   │  ×  │  Die: 6    │  =  12 total outcomes
  │  outcomes  │     │  outcomes  │
  └────────────┘     └────────────┘
```

#### Real-World Use Cases

- **Combinatorics**: Counting the number of possible passwords, PINs, or lottery combinations.
- **Game Design**: Determining the total number of possible game states or configurations.
- **Genetics**: Enumerating possible gene combinations in offspring (e.g., Punnett squares).
- **Survey Design**: Calculating total possible response combinations across multiple questions.
- **Advantage**: The Fundamental Counting Principle avoids having to list every outcome manually for large experiments.

#### Steps

1. Identify each **step** or component of the experiment.
2. Count the number of possible outcomes for each step ($n_1, n_2, \dots, n_k$).
3. If listing: write out every unique combination to form the sample space $S$.
4. If counting: multiply $n_1 \times n_2 \times \dots \times n_k$ for the cardinality $|S|$.

#### Formula

$$
|S| = n_1 \times n_2 \times \dots \times n_k
$$

Where:

|         Symbol         | Pronunciation                    | Meaning                                                  |
| :--------------------: | :------------------------------- | :------------------------------------------------------- |
|          $S$           | "S"                              | The sample space (set of all possible outcomes)          |
|        $\|S\|$         | "cardinality of S"               | The total count of outcomes in the sample space          |
| $n_1, n_2, \dots, n_k$ | "n sub 1, n sub 2, ..., n sub k" | The number of options at each step of the experiment     |
|          $k$           | "k"                              | The total number of steps (components) in the experiment |

#### Examples

**Example 1** — Choosing a drink and a snack

At a snack bar you can choose **one drink** (Soda, Water, or Juice) and **one snack** (Chips or Cookies). List the full sample space and determine its cardinality.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Drinks: Soda, Water, Juice | Step 1 options |
> | Snacks: Chips, Cookies | Step 2 options |
> | $n_1 = 3$ | Number of drink choices |
> | $n_2 = 2$ | Number of snack choices |
> | Find: $S$ and $\|S\|$ | The sample space and its cardinality |

> **Step 1:** Write down the formula.
>
> $$|S| = n_1 \times n_2$$
>
> **Step 2:** Identify the values.
>
> Drink options: $n_1 = 3$ (Soda, Water, Juice)
> Snack options: $n_2 = 2$ (Chips, Cookies)
>
> **Step 3:** List the sample space.
>
> $S = \{(\text{Soda, Chips}), (\text{Soda, Cookies}), (\text{Water, Chips}), (\text{Water, Cookies}), (\text{Juice, Chips}), (\text{Juice, Cookies})\}$
>
> **Step 4:** Calculate the cardinality.
>
> $$|S| = 3 \times 2$$
>
> **Step 5:** Simplify.
>
> $$\boxed{|S| = 6}$$

**Example 2** — Creating a 4-digit PIN (digits 0–9)

A phone lock screen requires a **4-digit PIN** where each digit can be any number from 0 to 9. How many possible PINs are there?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | 4-digit PIN | The experiment (each digit is a step) |
> | Each digit can be 0–9 | 10 options per step |
> | $n_1 = n_2 = n_3 = n_4 = 10$ | Options at each of the 4 steps |
> | $k = 4$ | Number of steps |
> | Find: $\|S\|$ | Total number of possible PINs |

> **Step 1:** Write down the formula.
>
> $$|S| = n_1 \times n_2 \times n_3 \times n_4$$
>
> **Step 2:** Identify the values.
>
> Each digit has 10 possible values (0 through 9), and there are 4 digits.
>
> **Step 3:** Substitute into the formula.
>
> $$|S| = 10 \times 10 \times 10 \times 10$$
>
> **Step 4:** Simplify.
>
> $$|S| = 10^4$$
>
> **Step 5:** Calculate.
>
> $$\boxed{|S| = 10{,}000}$$

---

<p align="left">
  <a href="../session1/visualization.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./events.md"><b>Next →</b></a>
  </span>
</p>
