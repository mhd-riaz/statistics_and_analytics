<p align="left">
  <a href="./events.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./conditionalProbability.md"><b>Next →</b></a>
  </span>
</p>

# Probability Theorems

```
Probability Theorems
├── Addition Theorem (OR Rule)
│   ├── Definition & Intuition
│   ├── Formula: P(A ∪ B)
│   ├── Special Case: Disjoint Events
│   └── Worked Examples
│
└── Multiplication Theorem (AND Rule)
    ├── Definition & Intuition
    ├── Formula: P(A ∩ B)
    ├── Special Case: Independent Events
    └── Worked Examples
```

---

## 1. Addition Theorem (The OR Rule)

The **Addition Theorem** (also called the **Probability Addition Rule**) calculates the probability that **at least one** of two events occurs — i.e., the probability of $A$ **or** $B$ (or both). The key idea: if two events overlap, you'll double-count the overlap when you add their individual probabilities, so you **subtract it once** to correct.

**Analogy:** Imagine a pizza menu. 15 pizzas have **cheese** and 10 have **mushrooms**. But 5 pizzas have **both**. If you ask "how many have cheese OR mushrooms?", you can't just say $15 + 10 = 25$ — you'd count those 5 overlap pizzas twice. So: $15 + 10 - 5 = 20$.

```
  Venn Diagram — why we subtract the overlap:

       P(A)                P(B)
  ┌─────────────┐    ┌─────────────┐
  │             │    │             │
  │    A only   │████│   B only    │
  │             │████│             │
  │             │    │             │
  └─────────────┘    └─────────────┘
                 ████
              P(A ∩ B)
           (counted TWICE
          if we just add —
          so subtract once)

  P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

  Special case — if A and B are DISJOINT (no overlap):

  ┌─────────────┐    ┌─────────────┐
  │             │    │             │
  │      A      │    │      B      │
  │             │    │             │
  └─────────────┘    └─────────────┘
       No overlap → P(A ∩ B) = 0

  P(A ∪ B) = P(A) + P(B)
```

#### Real-World Use Cases

- **Insurance**: Probability of a client filing a home insurance claim OR a car insurance claim.
- **Hiring**: Probability a candidate has a degree in CS OR experience in Python (some have both).
- **Healthcare**: Probability a patient has diabetes OR hypertension (comorbidity = overlap).
- **Quality Control**: Probability a product has a cosmetic defect OR a functional defect.
- **Limitation**: Only works for two events at a time in this form. For 3+ events, the inclusion-exclusion formula grows more complex.

#### Steps

1. Identify the two events $A$ and $B$.
2. Calculate $P(A)$ and $P(B)$ individually.
3. Determine $P(A \cap B)$ — the probability **both** events occur together.
4. If $A$ and $B$ are **disjoint** (mutually exclusive), then $P(A \cap B) = 0$.
5. Apply: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.

#### Formula

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

Where:

|    Symbol     | Pronunciation        | Meaning                                                          |
| :-----------: | :------------------- | :--------------------------------------------------------------- |
| $P(A \cup B)$ | "P of A union B"     | Probability of A **or** B (or both) occurring                    |
|    $P(A)$     | "P of A"             | Probability of event A occurring                                 |
|    $P(B)$     | "P of B"             | Probability of event B occurring                                 |
| $P(A \cap B)$ | "P of A intersect B" | Probability of both A **and** B occurring together (the overlap) |

> **Special case:** If $A$ and $B$ are **disjoint** (mutually exclusive), then $P(A \cap B) = 0$, and the formula simplifies to:
> $$P(A \cup B) = P(A) + P(B)$$

#### Examples

**Example 1** — Students playing sports (overlapping events)

In a class of **30 students**, **15** play Football, **10** play Basketball, and **5** play **both**. If you pick a student at random, what is the probability they play Football **or** Basketball?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Total students $= 30$ | Sample space |
> | $n(\text{Football}) = 15$ | Students who play Football |
> | $n(\text{Basketball}) = 10$ | Students who play Basketball |
> | $n(\text{Football} \cap \text{Basketball}) = 5$ | Students who play both |
> | Find: $P(\text{Football} \cup \text{Basketball})$ | Probability of playing at least one sport |

> **Step 1:** Write down the formula.
>
> $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
>
> **Step 2:** Calculate each probability.
>
> $P(\text{Football}) = \frac{15}{30} = \frac{1}{2}$
>
> $P(\text{Basketball}) = \frac{10}{30} = \frac{1}{3}$
>
> $P(\text{Football} \cap \text{Basketball}) = \frac{5}{30} = \frac{1}{6}$
>
> **Step 3:** Substitute into the formula.
>
> $$P(F \cup B) = \frac{1}{2} + \frac{1}{3} - \frac{1}{6}$$
>
> **Step 4:** Find a common denominator (6) and simplify.
>
> $$P(F \cup B) = \frac{3}{6} + \frac{2}{6} - \frac{1}{6} = \frac{4}{6}$$
>
> **Step 5:** Simplify.
>
> $$\boxed{P(F \cup B) = \frac{2}{3} \approx 0.667 \text{ or } 66.7\%}$$
>
> Note: If we had just added $\frac{15 + 10}{30} = \frac{25}{30}$, we'd overcount by 5 students — the ones playing both sports.

**Example 2** — Rolling a die (disjoint events)

You roll a standard 6-sided die. What is the probability of rolling a **1** or a **6**?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $S = \{1, 2, 3, 4, 5, 6\}$ | Sample space |
> | $A = \{1\}$ | Event: rolling a 1 |
> | $B = \{6\}$ | Event: rolling a 6 |
> | $A \cap B = \emptyset$ | Cannot roll both 1 and 6 simultaneously (disjoint) |
> | Find: $P(A \cup B)$ | Probability of rolling 1 or 6 |

> **Step 1:** Write down the formula (disjoint case).
>
> Since $A$ and $B$ are disjoint: $P(A \cup B) = P(A) + P(B)$
>
> **Step 2:** Calculate each probability.
>
> $P(A) = \frac{1}{6}$, $\quad P(B) = \frac{1}{6}$
>
> **Step 3:** Substitute into the formula.
>
> $$P(A \cup B) = \frac{1}{6} + \frac{1}{6}$$
>
> **Step 4:** Simplify.
>
> $$\boxed{P(A \cup B) = \frac{2}{6} = \frac{1}{3} \approx 0.333 \text{ or } 33.3\%}$$
>
> Because rolling a 1 and rolling a 6 can never happen at the same time on one die, there's no overlap to subtract.

---

## 2. Multiplication Theorem (The AND Rule)

The **Multiplication Theorem** calculates the probability that **both** events $A$ and $B$ occur together. It is derived from conditional probability — the chance of both happening equals the chance of the first one happening, **times** the chance of the second one happening *given the first already did*.

**Analogy:** Imagine picking 2 socks from a drawer in the dark. The first pick has some probability. But for the second pick, **one sock is already gone** — the chances have changed. The Multiplication Theorem accounts for this chain of events.

```
  Two cases:

  DEPENDENT events (one affects the other):

  Step 1                Step 2
  ┌──────────┐         ┌──────────┐
  │  Pick 1  │───────► │  Pick 2  │
  │  P(A)    │         │  P(B|A)  │   ← chances changed!
  └──────────┘         └──────────┘
  P(A ∩ B) = P(A) × P(B|A)

  Example: Drawing cards WITHOUT replacement
  1st draw: 4/52 chance of Ace
  2nd draw: 3/51 chance of Ace (one Ace gone, one card gone)


  INDEPENDENT events (one does NOT affect the other):

  Step 1                Step 2
  ┌──────────┐         ┌──────────┐
  │  Flip 1  │         │  Flip 2  │
  │  P(A)    │         │  P(B)    │   ← chances unchanged
  └──────────┘         └──────────┘
  P(A ∩ B) = P(A) × P(B)

  Example: Flipping a coin twice
  1st flip: 1/2 chance of Heads
  2nd flip: 1/2 chance of Heads (unaffected by 1st)
```

#### Real-World Use Cases

- **Security**: Probability of guessing both a username AND a password correctly.
- **Genetics**: Probability of a child inheriting gene A from the mother AND gene B from the father.
- **Manufacturing**: Probability that part 1 passes inspection AND part 2 passes inspection.
- **Reliability Engineering**: Probability that component A works AND component B works in a system where both are needed.
- **Limitation**: For dependent events, you must know or calculate the conditional probability $P(B|A)$, which isn't always straightforward.

#### Steps

1. Identify the two events $A$ and $B$.
2. Determine if the events are **independent** or **dependent**.
3. If **dependent**: find $P(A)$ and $P(B|A)$ — the probability of B given A already occurred.
4. If **independent**: find $P(A)$ and $P(B)$ — they don't affect each other.
5. Multiply the appropriate probabilities.

#### Formula

**General case (any two events):**

$$
P(A \cap B) = P(A) \cdot P(B|A)
$$

**Special case (independent events):**

$$
P(A \cap B) = P(A) \cdot P(B)
$$

Where:

|    Symbol     | Pronunciation        | Meaning                                                                |
| :-----------: | :------------------- | :--------------------------------------------------------------------- |
| $P(A \cap B)$ | "P of A intersect B" | Probability of both A **and** B occurring                              |
|    $P(A)$     | "P of A"             | Probability of the first event occurring                               |
| $P(B \mid A)$ | "P of B given A"     | Probability of B occurring, **knowing A already happened** (dependent) |
|    $P(B)$     | "P of B"             | Probability of B occurring on its own (independent case)               |

> **How to tell if events are independent?** If knowing that $A$ happened does **not** change the probability of $B$, they are independent: $P(B|A) = P(B)$.

#### Examples

**Example 1** — Drawing two Aces without replacement (dependent events)

You draw **two cards** one after another from a standard 52-card deck **without replacement**. What is the probability that **both cards are Aces**?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $n(S) = 52$ | Total cards in the deck |
> | 4 Aces in the deck | Favorable cards for each draw |
> | Without replacement | Cards are NOT put back (dependent) |
> | $A$ = first card is an Ace | First event |
> | $B$ = second card is an Ace | Second event |
> | Find: $P(A \cap B)$ | Probability both cards are Aces |

> **Step 1:** Write down the formula (dependent case).
>
> $$P(A \cap B) = P(A) \cdot P(B|A)$$
>
> **Step 2:** Calculate $P(A)$ — probability the first card is an Ace.
>
> $P(A) = \frac{4}{52} = \frac{1}{13}$
>
> **Step 3:** Calculate $P(B|A)$ — probability the second card is an Ace, given the first was an Ace.
>
> After removing one Ace: 3 Aces remain out of 51 cards.
>
> $P(B|A) = \frac{3}{51} = \frac{1}{17}$
>
> **Step 4:** Substitute into the formula.
>
> $$P(A \cap B) = \frac{1}{13} \times \frac{1}{17}$$
>
> **Step 5:** Multiply.
>
> $$\boxed{P(A \cap B) = \frac{1}{221} \approx 0.0045 \text{ or } 0.45\%}$$
>
> Very unlikely — less than half a percent. The first draw reduces the Aces available, making the second draw even harder.

**Example 2** — Flipping a coin and rolling a die (independent events)

You flip a fair coin and roll a standard 6-sided die. What is the probability of getting **Heads** on the coin **and** a **5** on the die?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Coin: $S_1 = \{H, T\}$ | Coin sample space |
> | Die: $S_2 = \{1, 2, 3, 4, 5, 6\}$ | Die sample space |
> | $A$ = Heads | Coin event |
> | $B$ = rolling a 5 | Die event |
> | Events are **independent** | Coin does not affect the die |
> | Find: $P(A \cap B)$ | Probability of Heads AND 5 |

> **Step 1:** Write down the formula (independent case).
>
> $$P(A \cap B) = P(A) \cdot P(B)$$
>
> **Step 2:** Calculate $P(A)$.
>
> $P(A) = P(\text{Heads}) = \frac{1}{2}$
>
> **Step 3:** Calculate $P(B)$.
>
> $P(B) = P(\text{rolling a 5}) = \frac{1}{6}$
>
> **Step 4:** Substitute into the formula.
>
> $$P(A \cap B) = \frac{1}{2} \times \frac{1}{6}$$
>
> **Step 5:** Multiply.
>
> $$\boxed{P(A \cap B) = \frac{1}{12} \approx 0.083 \text{ or } 8.3\%}$$
>
> The coin and die don't affect each other, so we simply multiply their individual probabilities.

---

<p align="left">
  <a href="./events.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./conditionalProbability.md"><b>Next →</b></a>
  </span>
</p>