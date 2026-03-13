<p align="left">
  <a href="./descriptive-statistics.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./random-variables-and-distributions.md"><b>Next →</b></a>
  </span>
</p>

---

# Probability Fundamentals

```
Probability Fundamentals
├── Basic Probability and Sample Space
│   ├── Probability Definition & Scale
│   ├── Experiment vs Trial
│   ├── P(A) vs P(E) Notation
│   ├── Sample Space & Cardinalities
│   └── Fundamental Counting Principle
│
├── Event Types and Relationships
│   ├── Event Type Taxonomy
│   │   ├── Simple Event
│   │   ├── Compound Event
│   │   ├── Complementary Event
│   │   ├── Mutually Exclusive (Disjoint) Event
│   │   ├── Independent Event
│   │   └── Dependent Event
│   ├── Disjoint ≠ Independent Caveat
│   └── Standard 52-Card Deck Reference
│
├── Probability Rules (Theorems)
│   ├── Addition Rule (OR)
│   │   ├── General Case (overlapping events)
│   │   └── Special Case (disjoint events)
│   └── Multiplication Rule (AND)
│       ├── Dependent Events
│       └── Independent Events
│
└── Conditional Reasoning
    ├── Conditional Probability
    │   └── "The given shrinks your world"
    ├── Law of Total Probability
    │   └── Partition-based decomposition
    └── Bayes' Theorem
        ├── Prior → Posterior update
        └── Key Terms (prior, posterior, likelihood, evidence)
```

---

## Probability Fundamentals

### 1. Basic Probability and Sample Space

**Probability** measures the likelihood of an event occurring. Every probability problem begins with an **experiment**, a **sample space** of all possible outcomes, and an **event** containing the favorable outcomes. Probability values always fall between 0 (impossible) and 1 (certain).

```
Probability Scale
Impossible         Unlikely       Even Chance       Likely          Certain
    0 ──────────── 0.25 ──────────── 0.5 ──────────── 0.75 ────────────  1
    │                                 │                                  │
 P(A)=0                            P(A)=0.5                          P(A)=1
 Event can                        Equally likely                    Event will
 never happen                     to happen or not                  always happen
```

#### Real-World Use Cases

- **Quality Control**: Compute the chance that a randomly chosen item from a production line is defective.
- **Weather Forecasting**: Express the chance of rain on a given day as a number between 0 and 1.
- **Finance**: Assess the likelihood of a positive return scenario based on historical frequencies.
- **Gaming**: Calculate odds in card games and dice games to guide strategy.
- **Limitation**: The classical model assumes all outcomes are equally likely, which does not hold in every real situation.

#### Steps

1. Define the experiment.
2. List the sample space $S$ (all possible outcomes).
3. Identify the event of interest $A$ (favorable outcomes).
4. Count favorable outcomes $n(A)$ and total outcomes $n(S)$.
5. Compute the probability $P(A) = n(A) / n(S)$.

#### Formula

$$
P(A) = \frac{n(A)}{n(S)}
$$

Where:
| Symbol | Pronunciation | Meaning                                      |
| :----: | :------------ | :------------------------------------------- |
| $P(A)$ | "P of A"      | Probability of event $A$                     |
| $n(A)$ | "n of A"      | Number of favorable outcomes (event $A$)     |
| $n(S)$ | "n of S"      | Total number of outcomes in the sample space |

#### Examples

**Example 1:** Rolling an even number on a die

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $S = \{1,2,3,4,5,6\}$ | Sample space |
> | $A = \{2,4,6\}$ | Event: even number |
> | Find: $P(A)$ | Probability of an even result |
>
> **Step 1:** Count the favorable outcomes.
>
> $$n(A) = 3$$
>
> **Step 2:** Count the total outcomes.
>
> $$n(S) = 6$$
>
> **Step 3:** Apply the formula.
>
> $$P(A) = \frac{3}{6}$$
>
> **Step 4:** Simplify.
>
> $$P(A) = \frac{1}{2}$$
>
> **Step 5:** State the answer.
>
> $$\boxed{P(A) = 0.5}$$

**Example 2:** Drawing a face card from a standard deck

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | Standard deck with 52 cards | Full sample space |
> | Face cards $= 12$ | J, Q, and K in four suits |
> | Find: $P(\text{face card})$ | Probability of drawing a face card |
>
> **Step 1:** Identify favorable outcomes.
>
> $$n(A) = 12$$
>
> **Step 2:** Identify total outcomes.
>
> $$n(S) = 52$$
>
> **Step 3:** Apply the formula.
>
> $$P(A) = \frac{12}{52}$$
>
> **Step 4:** Simplify.
>
> $$P(A) = \frac{3}{13}$$
>
> **Step 5:** State the result.
>
> $$\boxed{P(\text{face card}) = \frac{3}{13} \approx 0.231}$$

---

#### Experiment vs Trial

An **experiment** is the entire procedure of observing outcomes, while a **trial** is each individual repetition within that experiment. An experiment is the sum of all its trials.

```
Experiment: Test whether a coin is fair
┌──────────────────────────────────────────────────┐
│  Trial 1 → H    Trial 2 → T    Trial 3 → H       │
│  Trial 4 → H    Trial 5 → T    ...               │
│                                                  │
│  Experiment = Trial₁ + Trial₂ + ... + Trialₙ     │
└──────────────────────────────────────────────────┘
```

$$
\text{Experiment} = \sum_{i=1}^{n} \text{Trial}_i
$$

Where:
|      Symbol      | Pronunciation | Meaning                                             |
| :--------------: | :------------ | :-------------------------------------------------- |
| $\text{Trial}_i$ | "trial i"     | The $i$-th individual repetition of the observation |
|       $n$        | "n"           | Total number of trials in the experiment            |

**Example — Coin Fairness Test:**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | Experiment: Flip a coin 50 times | Full experiment |
> | Each flip is one trial | Single observation |
> | Find: relationship | How trials build an experiment |
>
> Each flip (trial) produces one outcome: $H$ or $T$. The full experiment collects all 50 results.
> If we observe 27 heads, we estimate $P(H) \approx 27/50 = 0.54$.

**Example — Battery Lifespan Test:**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | 3 brands of batteries | A, B, C |
> | 10 batteries per brand tested | 10 trials per brand |
> | Experiment: measure lifespan of all 30 batteries | Combined set of trials |
>
> Each battery measurement is a trial. The experiment is all 30 trials combined.

---

#### P(A) vs P(E) Notation

In different textbooks, you may see $P(A)$ or $P(E)$ used for the probability of an event. **They mean the same thing** — both represent the probability of an event occurring. The letter is just a label:

- $P(A)$ — labels the event as $A$
- $P(E)$ — labels the event as $E$

When multiple events exist, different letters distinguish them: $P(A)$, $P(B)$, $P(C)$, etc. Conditional probability notation like $P(A|B)$ reads as "probability of $A$ given $B$."

---

#### Sample Space and Cardinalities

The **sample space** $S$ is the set of **all possible outcomes**. The **cardinality** $|S|$ counts how many outcomes are in the sample space.

When an experiment has multiple stages, the **Fundamental Counting Principle** calculates the total number of outcomes:

$$
|S| = n_1 \times n_2 \times \ldots \times n_k
$$

Where:
|         Symbol          | Pronunciation            | Meaning                                      |
| :---------------------: | :----------------------- | :------------------------------------------- |
|         $\|S\|$         | "cardinality of S"       | Total number of outcomes in the sample space |
| $n_1, n_2, \ldots, n_k$ | "n one, n two, ..., n k" | Number of options at each stage              |
|           $k$           | "k"                      | Number of stages in the experiment           |

**Example 1 — Drink and Snack Combination:**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | 2 drink options: Tea, Coffee | Stage 1: $n_1 = 2$ |
> | 3 snack options: Chips, Cookie, Fruit | Stage 2: $n_2 = 3$ |
> | Find: $\|S\|$ | Total number of outcomes |
>
> **Step 1:** Apply the Fundamental Counting Principle.
>
> $$|S| = n_1 \times n_2 = 2 \times 3$$
>
> **Step 2:** Compute.
>
> $$\boxed{|S| = 6}$$
>
> The six outcomes: {(Tea, Chips), (Tea, Cookie), (Tea, Fruit), (Coffee, Chips), (Coffee, Cookie), (Coffee, Fruit)}

**Example 2 — 4-Digit PIN Code:**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | Each digit: 0–9 | 10 options per position |
> | 4 positions | $k = 4$ |
> | Repetition allowed | Digits can repeat |
> | Find: $\|S\|$ | Total number of possible PINs |
>
> **Step 1:** Apply the Fundamental Counting Principle.
>
> $$|S| = 10 \times 10 \times 10 \times 10 = 10^4$$
>
> **Step 2:** Compute.
>
> $$\boxed{|S| = 10{,}000}$$

---

### 2. Event Types and Relationships

An **event** is a subset of the sample space. Events can be classified into several types based on their structure (how many outcomes they contain) and their relationship to other events (whether they overlap, influence each other, or exhaust the space).

```
Event Type Taxonomy
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  By structure:    Simple Event ─── single outcome                │
│                   Compound Event ─ multiple outcomes              │
│                                                                  │
│  By relationship: Complementary ── A and A' cover all of S       │
│                   Mutually Exclusive (Disjoint) ── A ∩ B = ∅     │
│                   Independent ──── P(A ∩ B) = P(A)·P(B)          │
│                   Dependent ────── P(A ∩ B) = P(A)·P(B|A)        │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

Venn Diagrams:

Disjoint (Mutually Exclusive)          Non-Disjoint (Overlapping)
┌─────────────────────────┐            ┌─────────────────────────┐
│  ┌─────┐    ┌─────┐    │            │  ┌─────────────┐        │
│  │  A  │    │  B  │    │            │  │  A  ┌──┐ B  │        │
│  │     │    │     │    │            │  │     │AB│    │        │
│  └─────┘    └─────┘    │            │  │     └──┘    │        │
│        A ∩ B = ∅        │            │  └─────────────┘        │
└─────────────────────────┘            └─────────────────────────┘
```

#### Event Type Definitions

| Type                              | Definition                                                                   | Example                                            |
| :-------------------------------- | :--------------------------------------------------------------------------- | :------------------------------------------------- |
| **Simple Event**                  | An event with exactly one outcome                                            | Rolling a 3 on a die: $\{3\}$                      |
| **Compound Event**                | An event with more than one outcome                                          | Rolling an even number: $\{2,4,6\}$                |
| **Complementary Event**           | Everything in $S$ that is NOT in $A$; $A$ and $A'$ together cover all of $S$ | If $A = \{1,2\}$ then $A' = \{3,4,5,6\}$           |
| **Mutually Exclusive (Disjoint)** | Events that cannot happen at the same time: $A \cap B = \emptyset$           | Rolling an even and rolling an odd on the same die |
| **Independent Event**             | One event does not affect the probability of the other                       | Flipping a coin and rolling a die                  |
| **Dependent Event**               | One event changes the probability of the other                               | Drawing cards without replacement                  |

#### Standard 52-Card Deck Reference

Many probability examples use a standard deck. Keep this reference handy:

```
┌────────────────────────────────────────────────────────────────┐
│                    Standard 52-Card Deck                       │
├────────────┬───────────────────────────────────────────────────┤
│  4 Suits   │  ♠ Spades  ♥ Hearts  ♦ Diamonds  ♣ Clubs        │
├────────────┼───────────────────────────────────────────────────┤
│  13 Ranks  │  A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K        │
├────────────┼───────────────────────────────────────────────────┤
│  Total     │  4 × 13 = 52 cards                               │
├────────────┼───────────────────────────────────────────────────┤
│  Face cards│  J, Q, K × 4 suits = 12 cards                    │
│  Red cards │  ♥ + ♦ = 26 cards                                │
│  Black     │  ♠ + ♣ = 26 cards                                │
└────────────┴───────────────────────────────────────────────────┘
```

#### Real-World Use Cases

- **Medical Testing**: Positive and negative test outcomes are complements — if $P(\text{positive}) = 0.03$ then $P(\text{negative}) = 0.97$.
- **Card Games**: Drawing a King and drawing a Queen in a single draw are mutually exclusive — you cannot draw one card that is both.
- **Manufacturing QA**: Defective and non-defective items are complementary; tracking $P(\text{defect})$ automatically gives $P(\text{no defect})$.
- **Sensor Networks**: Independent sensors failing are modeled by multiplying individual failure probabilities.
- **Caveat**: Mutually exclusive events are **never** independent (unless one has probability 0). If $A \cap B = \emptyset$ with $P(A) > 0$ and $P(B) > 0$, then $P(A \cap B) = 0 \neq P(A) \cdot P(B)$.

> **⚠️ Disjoint ≠ Independent**
>
> A common mistake is confusing these two concepts:
> - **Disjoint (Mutually Exclusive)**: $A \cap B = \emptyset$ — they _cannot_ happen together.
> - **Independent**: $P(A \cap B) = P(A) \cdot P(B)$ — they _don't affect_ each other.
>
> If two events are disjoint and both have non-zero probability, knowing one occurred **guarantees** the other did not — so they are maximally _dependent_, not independent.

#### Steps

1. **Classify by structure**: Is the event simple (one outcome) or compound (multiple outcomes)?
2. **Classify by relationship**: Are the events complementary, mutually exclusive, independent, or dependent?
3. **Select the correct formula** based on the relationship type.
4. **Apply the formula** and interpret the result.

#### Formulas

**Complement Rule:**

$$
P(A') = 1 - P(A)
$$

**Independence Test:**

$$
\text{Events } A \text{ and } B \text{ are independent if and only if } P(A \cap B) = P(A) \cdot P(B)
$$

**Mutually Exclusive (Disjoint) Condition:**

$$
A \cap B = \emptyset \implies P(A \cap B) = 0
$$

Where:
|      Symbol       | Pronunciation               | Meaning                                                                            |
| :---------------: | :-------------------------- | :--------------------------------------------------------------------------------- |
|       $A'$        | "A prime" or "A complement" | The complement of event $A$ — all outcomes in $S$ not in $A$                       |
|      $P(A')$      | "P of A prime"              | Probability that event $A$ does **not** occur                                      |
|    $A \cap B$     | "A intersect B"             | The event that both $A$ and $B$ occur simultaneously                               |
|    $\emptyset$    | "empty set"                 | A set with no elements — no outcomes in common                                     |
| $P(A) \cdot P(B)$ | "P of A times P of B"       | Product of individual probabilities (equals joint probability only if independent) |

#### Examples

**Example 1:** Complement — probability of NOT rolling a 6

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | Experiment: Roll a fair six-sided die | Single roll |
> | $A = \{6\}$ | Event of rolling a 6 |
> | $S = \{1,2,3,4,5,6\}$ | Sample space |
> | $P(A) = \frac{1}{6}$ | Probability of rolling a 6 |
> | Find: $P(A')$ | Probability of NOT rolling a 6 |
>
> **Step 1:** Write the complement rule.
>
> $$P(A') = 1 - P(A)$$
>
> **Step 2:** Identify the complement event.
>
> $A' = \{1,2,3,4,5\}$ — all outcomes that are not 6.
>
> **Step 3:** Substitute.
>
> $$P(A') = 1 - \frac{1}{6}$$
>
> **Step 4:** Compute.
>
> $$P(A') = \frac{6}{6} - \frac{1}{6} = \frac{5}{6}$$
>
> **Step 5:** Interpret and state the answer.
>
> There is an $\frac{5}{6} \approx 83.3\%$ chance of NOT rolling a 6.
>
> $$\boxed{P(A') = \frac{5}{6} \approx 0.833}$$

**Example 2:** Mutually exclusive events — drawing a King or a Queen

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | Standard 52-card deck | Single draw |
> | $A$ = drawing a King | 4 Kings in the deck |
> | $B$ = drawing a Queen | 4 Queens in the deck |
> | $P(A) = \frac{4}{52}$ | Probability of King |
> | $P(B) = \frac{4}{52}$ | Probability of Queen |
> | Find: Are $A$ and $B$ mutually exclusive? What is $P(A \cup B)$? | |
>
> **Step 1:** Check if the events are mutually exclusive.
>
> Can a single card be _both_ a King and a Queen? **No.** A card has exactly one rank.
>
> $$A \cap B = \emptyset \quad \Rightarrow \quad P(A \cap B) = 0$$
>
> The events are **mutually exclusive (disjoint)**.
>
> **Step 2:** Since they are disjoint, use the special addition rule.
>
> $$P(A \cup B) = P(A) + P(B) \quad \text{(no overlap to subtract)}$$
>
> **Step 3:** Substitute.
>
> $$P(A \cup B) = \frac{4}{52} + \frac{4}{52} = \frac{8}{52}$$
>
> **Step 4:** Simplify.
>
> $$P(A \cup B) = \frac{8}{52} = \frac{2}{13}$$
>
> **Step 5:** Verify they are NOT independent (common misconception).
>
> If they were independent: $P(A) \cdot P(B) = \frac{4}{52} \cdot \frac{4}{52} = \frac{16}{2704} = \frac{1}{169} \neq 0 = P(A \cap B)$
>
> Since $P(A \cap B) \neq P(A) \cdot P(B)$, the events are **dependent** (not independent). This confirms: disjoint ≠ independent.
>
> $$\boxed{P(\text{King or Queen}) = \frac{2}{13} \approx 0.154}$$

---

### 3. Addition and Multiplication Rules

The **Addition Theorem** (OR Rule) calculates the probability that **at least one** of two events occurs. The **Multiplication Theorem** (AND Rule) calculates the probability that **both** events occur together. The main challenge is deciding whether events overlap (addition) or depend on each other (multiplication).

```
Addition Theorem (OR Rule)
──────────────────────────

Venn Diagram — why we subtract the overlap:

     P(A)                P(B)
┌─────────────┐    ┌─────────────┐
│             │    │             │
│    A only   │████│   B only    │
│             │████│             │
└─────────────┘    └─────────────┘
               ████
            P(A ∩ B)
         (counted TWICE
        if we just add —
        so subtract once)

P(A ∪ B) = P(A) + P(B) − P(A ∩ B)


Disjoint special case — no overlap, so nothing to subtract:

┌─────────────┐    ┌─────────────┐
│             │    │             │
│      A      │    │      B      │
│             │    │             │
└─────────────┘    └─────────────┘
     No overlap → P(A ∩ B) = 0

P(A ∪ B) = P(A) + P(B)


Multiplication Theorem (AND Rule)
─────────────────────────────────

DEPENDENT events (one affects the other):

Step 1                Step 2
┌──────────┐         ┌──────────┐
│  Pick 1  │───────► │  Pick 2  │
│  P(A)    │         │  P(B|A)  │   ← chances changed!
└──────────┘         └──────────┘
P(A ∩ B) = P(A) × P(B|A)


INDEPENDENT events (one does NOT affect the other):

Step 1                Step 2
┌──────────┐         ┌──────────┐
│  Flip 1  │         │  Flip 2  │
│  P(A)    │         │  P(B)    │   ← chances unchanged
└──────────┘         └──────────┘
P(A ∩ B) = P(A) × P(B)
```

#### Real-World Use Cases

- **Hiring**: Probability that a candidate has Python _or_ SQL skill (addition rule with overlap — many candidates have both).
- **Manufacturing**: Probability that two consecutive parts are _both_ defective (multiplication rule — sampling without replacement changes the odds).
- **Insurance**: Probability of either a home claim _or_ an auto claim in a given year (addition with overlap — some policyholders file both).
- **Medical Screening**: Probability two independent tests both return positive (multiplication rule with independence).
- **Limitation**: If overlap is ignored in addition, the result is **too high**. If dependence is ignored in multiplication, the result is **wrong**.

> **⚠️ Choosing the right rule:**
>
> | Question asks… | Key word | Rule | Formula |
> |:---|:---:|:---|:---|
> | _at least one_ of A, B | **or** | Addition | $P(A \cup B)$ |
> | _both_ A and B together | **and** | Multiplication | $P(A \cap B)$ |

#### Steps

1. Translate the English question: "or" → union ($\cup$), "and" → intersection ($\cap$).
2. Check the event relationship — are the events **disjoint** (no overlap) or **overlapping**? Are they **independent** or **dependent**?
3. Pick the correct formula variant (see formula table below).
4. Substitute known probabilities.
5. Compute and interpret the result.

#### Formula

**Addition Rule — General (overlapping events):**

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

**Addition Rule — Disjoint special case** ($A \cap B = \emptyset$):

$$
P(A \cup B) = P(A) + P(B)
$$

**Multiplication Rule — General (dependent events):**

$$
P(A \cap B) = P(A) \cdot P(B \mid A)
$$

**Multiplication Rule — Independent special case** ($P(B \mid A) = P(B)$):

$$
P(A \cap B) = P(A) \cdot P(B)
$$

Where:
|    Symbol     | Pronunciation    | Meaning                                       |
| :-----------: | :--------------- | :-------------------------------------------- |
|  $A \cup B$   | "A union B"      | Event that $A$ **or** $B$ (or both) occur     |
|  $A \cap B$   | "A intersect B"  | Event that **both** $A$ and $B$ occur         |
| $P(B \mid A)$ | "P of B given A" | Probability of $B$ after $A$ already occurred |
|  $\emptyset$  | "empty set"      | No outcomes in common — events are disjoint   |

> **How to tell if events are independent?**
>
> Check whether $P(A \cap B) = P(A) \cdot P(B)$. If this equality holds, the events are **independent**. If it does not hold, they are **dependent** and you must use $P(B \mid A)$.

#### Examples

##### Addition Theorem Examples

**Example 1:** Addition rule with overlap — 30 students surveyed about sports

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $n = 30$ | Total number of students surveyed |
> | Football players $= 15$ | Students who play football |
> | Basketball players $= 10$ | Students who play basketball |
> | Both $= 5$ | Students who play _both_ sports |
> | Find: $P(\text{Football} \cup \text{Basketball})$ | Probability a random student plays at least one sport |
>
> **Step 1:** Convert counts to probabilities.
>
> $$P(F) = \frac{15}{30} = \frac{1}{2}, \quad P(B) = \frac{10}{30} = \frac{1}{3}, \quad P(F \cap B) = \frac{5}{30} = \frac{1}{6}$$
>
> **Step 2:** Write the general addition rule.
>
> $$P(F \cup B) = P(F) + P(B) - P(F \cap B)$$
>
> **Step 3:** Substitute.
>
> $$P(F \cup B) = \frac{1}{2} + \frac{1}{3} - \frac{1}{6}$$
>
> **Step 4:** Find a common denominator and simplify.
>
> $$P(F \cup B) = \frac{3}{6} + \frac{2}{6} - \frac{1}{6} = \frac{4}{6} = \frac{2}{3}$$
>
> **Step 5:** Interpret.
>
> There is a $\frac{2}{3} \approx 66.7\%$ chance a randomly chosen student plays at least one of the two sports. Without subtracting the overlap, we would have counted the 5 students who play both **twice**.
>
> $$\boxed{P(F \cup B) = \frac{2}{3}}$$

**Example 2:** Addition rule for disjoint events — rolling a 1 or a 6 on a fair die

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Fair six-sided die | Equally likely outcomes $\{1,2,3,4,5,6\}$ |
> | $A$ = rolling a 1 | $P(A) = \frac{1}{6}$ |
> | $B$ = rolling a 6 | $P(B) = \frac{1}{6}$ |
> | $A \cap B = \emptyset$ | Cannot roll both 1 and 6 simultaneously — events are **disjoint** |
> | Find: $P(A \cup B)$ | Probability of rolling a 1 _or_ a 6 |
>
> **Step 1:** Verify the events are disjoint.
>
> A single die roll produces exactly one number, so rolling a 1 and rolling a 6 cannot happen at the same time: $P(A \cap B) = 0$.
>
> **Step 2:** Apply the disjoint addition rule.
>
> $$P(A \cup B) = P(A) + P(B)$$
>
> **Step 3:** Substitute.
>
> $$P(A \cup B) = \frac{1}{6} + \frac{1}{6} = \frac{2}{6} = \frac{1}{3}$$
>
> **Step 4:** Interpret.
>
> There is a $\frac{1}{3} \approx 33.3\%$ chance of rolling a 1 or a 6. Because the events are disjoint, no overlap adjustment is needed.
>
> $$\boxed{P(A \cup B) = \frac{1}{3}}$$

##### Multiplication Theorem Examples

**Example 3:** Multiplication rule for dependent events — drawing two Aces without replacement

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Standard 52-card deck | 4 Aces initially |
> | $A$ = first card is an Ace | First draw |
> | $B$ = second card is an Ace | Second draw, **without** replacement |
> | Find: $P(A \cap B)$ | Probability of drawing two Aces in a row |
>
> **Step 1:** Recognize this is a **dependent** situation — drawing the first Ace removes it from the deck, changing the odds for the second draw.
>
> **Step 2:** Write the general multiplication rule.
>
> $$P(A \cap B) = P(A) \cdot P(B \mid A)$$
>
> **Step 3:** Compute $P(A)$ — 4 Aces out of 52 cards.
>
> $$P(A) = \frac{4}{52} = \frac{1}{13}$$
>
> **Step 4:** Compute $P(B \mid A)$ — _one Ace is gone_, so 3 Aces remain out of 51 cards.
>
> $$P(B \mid A) = \frac{3}{51} = \frac{1}{17}$$
>
> **Step 5:** Multiply.
>
> $$P(A \cap B) = \frac{1}{13} \cdot \frac{1}{17} = \frac{1}{221}$$
>
> **Step 6:** Interpret.
>
> There is a $\frac{1}{221} \approx 0.45\%$ chance of drawing two Aces in a row from a full deck without replacement. The conditional probability $P(B \mid A) = \frac{3}{51}$ is _lower_ than $P(B) = \frac{4}{52}$ because removing an Ace making the second Ace less likely.
>
> $$\boxed{P(A \cap B) = \frac{1}{221}}$$

**Example 4:** Multiplication rule for independent events — flipping a coin and rolling a die

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Fair coin + fair six-sided die | Two separate experiments |
> | $A$ = Heads on the coin | $P(A) = \frac{1}{2}$ |
> | $B$ = rolling a 5 on the die | $P(B) = \frac{1}{6}$ |
> | Events are **independent** | The coin result does not affect the die result |
> | Find: $P(A \cap B)$ | Probability of getting Heads _and_ a 5 |
>
> **Step 1:** Verify independence — the coin and die are physically separate; the outcome of one cannot influence the other.
>
> **Step 2:** Apply the independent multiplication rule.
>
> $$P(A \cap B) = P(A) \cdot P(B)$$
>
> **Step 3:** Substitute.
>
> $$P(A \cap B) = \frac{1}{2} \cdot \frac{1}{6} = \frac{1}{12}$$
>
> **Step 4:** Interpret.
>
> There is a $\frac{1}{12} \approx 8.3\%$ chance of getting both Heads and a 5. We used $P(B)$ instead of $P(B \mid A)$ because the events are independent — the coin landing Heads does not change the die's probabilities.
>
> $$\boxed{P(A \cap B) = \frac{1}{12}}$$

---

### 4. Conditional Probability, Total Probability, and Bayes' Theorem

```
Conditional Probability, Total Probability & Bayes' Theorem
├── Conditional Probability
│   ├── "Shrinks your world" — new sample space = only cases where condition holds
│   ├── Formula: P(A|B) = P(A ∩ B) / P(B)
│   └── Direction: knows B happened → asks about A
│
├── Law of Total Probability
│   ├── Splits S into non-overlapping paths (partition)
│   ├── P(B) = Σ P(B|Aᵢ)·P(Aᵢ)
│   └── Provides the denominator for Bayes' Theorem
│
└── Bayes' Theorem
    ├── Reverses conditioning direction: P(A|B) from P(B|A)
    ├── P(A|B) = P(B|A)·P(A) / P(B)
    └── Updates Prior → Posterior with new evidence
```

**Conditional probability** answers the question _"What is the probability of A, given that B already happened?"_ It **shrinks your world** — instead of looking at every outcome in $S$, you zoom into only the outcomes where $B$ is true, then check how many of those also satisfy $A$.

**Analogy — Classroom:** Imagine a classroom with 30 students. 10 wear glasses, 18 are girls, and 6 are girls who wear glasses. If you already know the student picked **wears glasses** (your world shrinks from 30 to 10), what's the chance the student is a girl?

```
BEFORE condition (full sample space S = 30):

👦 👦 👦 👦 👦 👦 👧 👧 👧 👧
👧 👧 👧 👧 👧 👧 👧 👧 👧 👧
🤓 🤓 🤓 🤓 🤓 🤓 🤓 🤓 🤓 🤓   ← 10 wear glasses

AFTER condition — "given wears glasses" (world shrinks to 10):

┌──────────────────────────────────┐
│  🤓 🤓 🤓 🤓 🤓 🤓 🤓 🤓 🤓 🤓  │  only these 10 matter now
│  ↑  ↑  ↑  ↑  ↑  ↑               │
│  girls with glasses = 6          │  P(Girl | Glasses) = 6/10 = 0.60
└──────────────────────────────────┘
```

The **Law of Total Probability** splits the sample space into non-overlapping paths (a _partition_) and adds up the contributions of each path to compute an overall probability $P(B)$. It is the essential stepping stone for the denominator of Bayes' Theorem.

**Bayes' Theorem** _reverses_ a conditional probability. It converts $P(B|A)$ (how likely is the evidence if the hypothesis is true) into $P(A|B)$ (how likely is the hypothesis given the evidence). This is the foundation of _Bayesian statistics_ — updating beliefs as new data arrives.

```
The Bayesian Update Process:

┌──────────┐      New Evidence      ┌───────────┐
│  PRIOR   │  ──────────────────►   │ POSTERIOR  │
│  P(A)    │      (observed B)      │  P(A|B)   │
│          │                        │           │
│ "Initial │    Bayes' Theorem      │ "Updated  │
│  belief" │    does the update     │  belief"  │
└──────────┘                        └───────────┘

            P(B|A)  ×  P(A)
P(A|B)  = ─────────────────
                P(B)

Posterior = (Likelihood × Prior) / Evidence
```

#### Real-World Use Cases

**Conditional Probability:**
- **Medical Testing**: What is the probability a patient has COVID _given_ they tested positive?
- **Spam Filtering**: What is the probability an email is spam _given_ it contains the word "free"?
- **Insurance**: What is the probability of a claim _given_ the policyholder is under 25?
- **Quality Control**: What is the probability a product is defective _given_ it came from Machine A?
- **Limitation**: The condition must have $P(B) > 0$ — you cannot condition on an impossible event.

**Law of Total Probability:**
- **Manufacturing**: Finding the overall defect rate when products come from multiple machines with different defect rates.
- **Marketing**: Estimating total customer conversion rate across different age groups.
- **Insurance**: Determining overall claim probability by partitioning policyholders into risk categories (low, medium, high).
- **Advantage**: Essential stepping stone for Bayes' Theorem — you almost always need it to calculate the denominator $P(B)$.

**Bayes' Theorem:**
- **Medical Diagnosis**: Determining the probability of having a disease given a positive test result (accounting for false positives).
- **Legal Reasoning**: Assessing the probability of guilt given forensic evidence.
- **Machine Learning**: Naive Bayes classifiers use Bayes' Theorem to categorize text and images.
- **Advantage**: Lets you incorporate **prior knowledge** — you don't start from scratch each time.
- **Limitation**: Can be misleading if base rates (priors) are ignored — see _base rate neglect_.

> **Key Terms (Bayesian vocabulary):**
>
> | Term | Symbol | Meaning |
> |:---|:---:|:---|
> | **Prior** | $P(A)$ | Initial belief about hypothesis $A$ _before_ seeing evidence |
> | **Likelihood** | $P(B \mid A)$ | How probable the evidence is, _assuming_ $A$ is true |
> | **Evidence (Marginal)** | $P(B)$ | Overall probability of observing $B$ under all scenarios |
> | **Posterior** | $P(A \mid B)$ | Updated belief about $A$ _after_ seeing evidence $B$ |

#### Steps

**Conditional Probability — Steps:**

1. Identify the **condition** event $B$ (what is known to have happened).
2. Identify the **target** event $A$ (what you want the probability of).
3. Find $P(A \cap B)$ — the probability that both $A$ and $B$ occur together.
4. Find $P(B)$ — the probability of the condition.
5. Divide: $P(A|B) = \frac{P(A \cap B)}{P(B)}$.

**Law of Total Probability — Steps:**

1. Identify the event $B$ whose total probability you want.
2. Partition the sample space into mutually exclusive and exhaustive events $A_1, A_2, \dots, A_n$.
3. For each partition $A_i$, determine $P(A_i)$ and $P(B|A_i)$.
4. Multiply each pair: $P(B|A_i) \cdot P(A_i)$.
5. Sum all the products: $P(B) = \sum P(B|A_i) \cdot P(A_i)$.

**Bayes' Theorem — Steps:**

1. Identify the **hypothesis** ($A$) and the **evidence** ($B$).
2. Determine the **prior** $P(A)$.
3. Determine the **likelihood** $P(B|A)$.
4. Calculate the **evidence** $P(B)$ using the Law of Total Probability.
5. Apply Bayes' Theorem: $P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$.

#### Formula

**Conditional Probability:**

$$
P(A\mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0
$$

Where:
|    Symbol     | Pronunciation        | Meaning                                              |
| :-----------: | :------------------- | :--------------------------------------------------- |
| $P(A\mid B)$  | "P of A given B"     | Probability of $A$ after knowing $B$ occurred        |
| $P(A \cap B)$ | "P of A intersect B" | Probability that both $A$ and $B$ happen together    |
|    $P(B)$     | "P of B"             | Probability of the condition event (the new "world") |

> **Note:** $P(B|A)$ reverses the direction — it means "probability of $B$ given that $A$ occurred." In general, $P(A|B) \neq P(B|A)$.

**Law of Total Probability:**

$$
P(B) = \sum_{i=1}^{n} P(B\mid A_i) \cdot P(A_i)
$$

Or expanded:

$$
P(B) = P(B|A_1) \cdot P(A_1) + P(B|A_2) \cdot P(A_2) + \dots + P(B|A_n) \cdot P(A_n)
$$

Where:
|         Symbol         | Pronunciation             | Meaning                                                       |
| :--------------------: | :------------------------ | :------------------------------------------------------------ |
|         $P(B)$         | "P of B"                  | The total probability of event $B$ across all scenarios       |
| $A_1, A_2, \dots, A_n$ | "A sub 1 through A sub n" | A partition — mutually exclusive events that cover all of $S$ |
|        $P(A_i)$        | "P of A sub i"            | The probability of the $i$-th scenario                        |
|    $P(B \mid A_i)$     | "P of B given A sub i"    | The probability of $B$ within the $i$-th scenario             |

> **Partition requirement:** $A_1, A_2, \dots, A_n$ must be **mutually exclusive** ($A_i \cap A_j = \emptyset$) and **exhaustive** ($A_1 \cup \dots \cup A_n = S$).

```
Sample space split into partitions:

┌──────────┬──────────┬──────────┬──────────┐
│    A₁    │    A₂    │    A₃    │   ...Aₙ  │   ← Partition of S
│          │          │          │          │
│  B ∩ A₁  │  B ∩ A₂  │  B ∩ A₃  │  B ∩ Aₙ  │
└──────────┴──────────┴──────────┴──────────┘

P(B) = P(B ∩ A₁) + P(B ∩ A₂) + ... + P(B ∩ Aₙ)
     = P(B|A₁)·P(A₁) + P(B|A₂)·P(A₂) + ... + P(B|Aₙ)·P(Aₙ)
```

**Bayes' Theorem:**

$$
P(A\mid B) = \frac{P(B\mid A) \cdot P(A)}{P(B)}
$$

Where:
|    Symbol     | Pronunciation    | Meaning                                                         |
| :-----------: | :--------------- | :-------------------------------------------------------------- |
| $P(A \mid B)$ | "P of A given B" | **Posterior** — updated probability of $A$ after observing $B$  |
| $P(B \mid A)$ | "P of B given A" | **Likelihood** — probability of observing $B$ if $A$ is true    |
|    $P(A)$     | "P of A"         | **Prior** — initial probability of $A$ before new evidence      |
|    $P(B)$     | "P of B"         | **Evidence** — total probability of $B$ (use Law of Total Prob) |

> **Bayes in words:**
>
> $$\text{Posterior} = \frac{\text{Likelihood} \times \text{Prior}}{\text{Evidence}}$$

#### Examples

##### Conditional Probability Examples

**Example 1:** Die — probability of greater than 3 given even

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $S = \{1, 2, 3, 4, 5, 6\}$ | Full sample space of a fair die |
> | $B = \{2, 4, 6\}$ (even numbers) | The condition — we know the roll is even |
> | $A = \{4, 5, 6\}$ (greater than 3) | The target event |
> | $A \cap B = \{4, 6\}$ | Outcomes that are both >3 AND even |
> | Find: $P(A \mid B)$ | Probability of >3 given even |
>
> **Step 1:** Write the conditional probability formula.
>
> $$P(A|B) = \frac{P(A \cap B)}{P(B)}$$
>
> **Step 2:** The world shrinks to $B = \{2, 4, 6\}$, so $P(B) = \frac{3}{6} = \frac{1}{2}$.
>
> **Step 3:** Find $P(A \cap B)$. The outcomes in both $A$ and $B$ are $\{4, 6\}$, so $P(A \cap B) = \frac{2}{6} = \frac{1}{3}$.
>
> **Step 4:** Substitute into the formula.
>
> $$P(A|B) = \frac{\frac{1}{3}}{\frac{1}{2}} = \frac{1}{3} \times \frac{2}{1} = \frac{2}{3}$$
>
> **Step 5:** State the result.
>
> $$\boxed{P(A|B) = \frac{2}{3} \approx 0.667 \text{ or } 66.7\%}$$
>
> Out of the 3 even outcomes $\{2, 4, 6\}$, two of them $(4, 6)$ are greater than 3 — hence $\frac{2}{3}$.

**Example 2:** Cards — probability of King given face card

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Standard deck of 52 cards | Full sample space |
> | $B$ = face card (J, Q, K) | Condition — 12 face cards total |
> | $A$ = King | Target — 4 Kings in the deck |
> | $A \cap B$ = King (every King is a face card) | $A \subset B$, so $A \cap B = A$ |
> | Find: $P(A \mid B)$ | Probability of King given face card |
>
> **Step 1:** Write the formula.
>
> $$P(A|B) = \frac{P(A \cap B)}{P(B)}$$
>
> **Step 2:** Find $P(B)$. There are 12 face cards out of 52.
>
> $$P(B) = \frac{12}{52} = \frac{3}{13}$$
>
> **Step 3:** Find $P(A \cap B)$. Since every King is a face card, $A \cap B = A$.
>
> $$P(A \cap B) = \frac{4}{52} = \frac{1}{13}$$
>
> **Step 4:** Substitute.
>
> $$P(A|B) = \frac{\frac{1}{13}}{\frac{3}{13}} = \frac{1}{13} \times \frac{13}{3} = \frac{1}{3}$$
>
> **Step 5:** State the result.
>
> $$\boxed{P(A|B) = \frac{1}{3} \approx 0.333 \text{ or } 33.3\%}$$
>
> Among the 3 types of face cards (J, Q, K), each is equally likely, so the probability of King is $\frac{1}{3}$.

##### Law of Total Probability Examples

**Example 3:** Factory with two machines

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Machine A makes 60% of items | $P(A) = 0.60$ |
> | Machine B makes 40% of items | $P(B_m) = 0.40$ |
> | Defect rate from A is 3% | $P(D \mid A) = 0.03$ |
> | Defect rate from B is 5% | $P(D \mid B_m) = 0.05$ |
> | Find: $P(D)$ | Overall defect rate |
>
> **Step 1:** Write the total probability formula.
>
> $$P(D) = P(D \mid A) \cdot P(A) + P(D \mid B_m) \cdot P(B_m)$$
>
> **Step 2:** Substitute the values.
>
> $$P(D) = (0.03)(0.60) + (0.05)(0.40)$$
>
> **Step 3:** Multiply each contribution.
>
> | Source | $P(\text{Source})$ | $P(D \mid \text{Source})$ | Contribution |
> |:---:|:---:|:---:|:---:|
> | Machine A | 0.60 | 0.03 | $0.018$ |
> | Machine B | 0.40 | 0.05 | $0.020$ |
>
> **Step 4:** Add the contributions.
>
> $$P(D) = 0.018 + 0.020 = 0.038$$
>
> **Step 5:** State the result.
>
> $$\boxed{P(D) = 0.038 = 3.8\%}$$
>
> Even though Machine A has a lower defect rate (3%), it produces 60% of all items — so its contribution to the overall defect pool (0.018) is comparable to Machine B's (0.020).

**Example 4:** Transportation — 3 modes of commute

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | 50% commute by car | $P(C) = 0.50$ |
> | 30% commute by bus | $P(B) = 0.30$ |
> | 20% commute by bike | $P(K) = 0.20$ |
> | 5% late by car | $P(L \mid C) = 0.05$ |
> | 15% late by bus | $P(L \mid B) = 0.15$ |
> | 2% late by bike | $P(L \mid K) = 0.02$ |
> | Find: $P(L)$ | Overall probability of being late |
>
> **Step 1:** The 3 commute modes form a **partition** — mutually exclusive and exhaustive.
>
> $$P(C) + P(B) + P(K) = 0.50 + 0.30 + 0.20 = 1.00 \checkmark$$
>
> **Step 2:** Write the total probability formula.
>
> $$P(L) = P(L \mid C) \cdot P(C) + P(L \mid B) \cdot P(B) + P(L \mid K) \cdot P(K)$$
>
> **Step 3:** Substitute the values.
>
> $$P(L) = (0.05)(0.50) + (0.15)(0.30) + (0.02)(0.20)$$
>
> **Step 4:** Build the contribution table and add.
>
> | Mode | $P(\text{Mode})$ | $P(L \mid \text{Mode})$ | Contribution |
> |:---:|:---:|:---:|:---:|
> | Car | 0.50 | 0.05 | $0.025$ |
> | Bus | 0.30 | 0.15 | $0.045$ |
> | Bike | 0.20 | 0.02 | $0.004$ |
> | **Total** | | | **$0.074$** |
>
> **Step 5:** State the result.
>
> $$\boxed{P(L) = 0.074 = 7.4\%}$$
>
> Bus is the biggest contributor to lateness (0.045) despite only carrying 30% of commuters — its 15% late rate dominates. This shows how total probability pinpoints which source drives the overall rate.

##### Bayes' Theorem Examples

**Example 5:** School uniforms — who wears pants?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | 40% of students are boys | $P(\text{Boy}) = 0.40$ |
> | 60% of students are girls | $P(\text{Girl}) = 0.60$ |
> | 100% of boys wear pants | $P(\text{Pants} \mid \text{Boy}) = 1.00$ |
> | 50% of girls wear pants | $P(\text{Pants} \mid \text{Girl}) = 0.50$ |
> | A student wearing pants is selected at random | Observed evidence |
> | Find: $P(\text{Girl} \mid \text{Pants})$ | Update: is this student a girl? |
>
> **Step 1:** Identify prior, likelihood, and evidence.
>
> | Bayesian Term | Symbol | Value |
> |:---|:---:|:---:|
> | Prior | $P(\text{Girl})$ | 0.60 |
> | Likelihood | $P(\text{Pants} \mid \text{Girl})$ | 0.50 |
> | Evidence | $P(\text{Pants})$ | ? (need total probability) |
>
> **Step 2:** Compute the evidence using total probability.
>
> $$P(\text{Pants}) = P(\text{Pants} \mid \text{Boy}) \cdot P(\text{Boy}) + P(\text{Pants} \mid \text{Girl}) \cdot P(\text{Girl})$$
>
> $$P(\text{Pants}) = (1.00)(0.40) + (0.50)(0.60) = 0.40 + 0.30 = 0.70$$
>
> **Step 3:** Apply Bayes' formula.
>
> $$P(\text{Girl} \mid \text{Pants}) = \frac{P(\text{Pants} \mid \text{Girl}) \cdot P(\text{Girl})}{P(\text{Pants})}$$
>
> **Step 4:** Substitute values.
>
> $$P(\text{Girl} \mid \text{Pants}) = \frac{(0.50)(0.60)}{0.70} = \frac{0.30}{0.70} = \frac{3}{7}$$
>
> **Step 5:** State the result.
>
> $$\boxed{P(\text{Girl} \mid \text{Pants}) = \frac{3}{7} \approx 0.429 = 42.9\%}$$
>
> **Bayesian update:** The prior probability of Girl was 60%. After observing "wears pants", it dropped to 42.9% — because boys are guaranteed to wear pants, the evidence "pants" shifts probability _toward_ Boy.

**Example 6:** Medical testing — rare disease screening

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Disease prevalence $= 0.1\%$ | $P(D) = 0.001$ — very rare |
> | Healthy rate $= 99.9\%$ | $P(D') = 0.999$ |
> | Test correctly detects disease 99% of the time | $P(+ \mid D) = 0.99$ (sensitivity) |
> | Test correctly identifies healthy 99% of the time | $P(- \mid D') = 0.99$ (specificity) |
> | False positive rate 1% | $P(+ \mid D') = 0.01$ |
> | A patient tests positive | Observed evidence |
> | Find: $P(D \mid +)$ | Posterior probability of disease |
>
> **Step 1:** Identify Bayesian components.
>
> | Bayesian Term | Symbol | Value |
> |:---|:---:|:---:|
> | Prior | $P(D)$ | 0.001 |
> | Likelihood | $P(+ \mid D)$ | 0.99 |
> | Evidence | $P(+)$ | ? |
>
> **Step 2:** Compute $P(+)$ via total probability.
>
> $$P(+) = P(+ \mid D) \cdot P(D) + P(+ \mid D') \cdot P(D')$$
>
> | Group | $P(\text{Group})$ | $P(+ \mid \text{Group})$ | Contribution |
> |:---:|:---:|:---:|:---:|
> | Diseased | 0.001 | 0.99 | $0.00099$ |
> | Healthy | 0.999 | 0.01 | $0.00999$ |
> | **Total** | | | **$0.01098$** |
>
> **Step 3:** Apply Bayes' formula.
>
> $$P(D \mid +) = \frac{P(+ \mid D) \cdot P(D)}{P(+)} = \frac{(0.99)(0.001)}{0.01098}$$
>
> **Step 4:** Calculate.
>
> $$P(D \mid +) = \frac{0.00099}{0.01098} \approx 0.0902$$
>
> **Step 5:** State the result and interpret.
>
> $$\boxed{P(D \mid +) \approx 9.02\%}$$
>
> **Base rate neglect warning:** Despite a 99% accurate test, a positive result only means a ~9% chance of actually having the disease. Why? Because the disease is so rare ($0.1\%$) that the **false positives from the 99.9% healthy population** overwhelm the true positives. This is the most famous illustration of why **base rates matter** — and why Bayes' Theorem is essential in medical screening.
>
> | Before Test (Prior) | After Positive Test (Posterior) |
> |:---:|:---:|
> | $P(D) = 0.1\%$ | $P(D \mid +) = 9.02\%$ |
> | 1 in 1000 | ~1 in 11 |

---

<p align="left">
  <a href="./descriptive-statistics.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./random-variables-and-distributions.md"><b>Next →</b></a>
  </span>
</p>
