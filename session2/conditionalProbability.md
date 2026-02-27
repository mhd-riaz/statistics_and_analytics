<p align="left">
  <a href="./events.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./theorems.md"><b>Next →</b></a>
  </span>
</p>

# Conditional Probability & Bayes' Theorem

```
Conditional Probability & Bayes' Theorem
├── Conditional Probability
│   ├── Definition & Intuition
│   ├── Formula: P(A|B)
│   └── Worked Examples
│
└── Bayes' Theorem
    ├── Definition (Prior → Posterior)
    ├── Formula: P(A|B) = P(B|A)·P(A) / P(B)
    ├── Key Terms (Prior, Likelihood, Evidence, Posterior)
    └── Worked Examples
```

---

## 1. Conditional Probability

**Conditional probability** is the probability of an event occurring **given that** another event has already occurred. The notation $P(A|B)$ is read as "the probability of A given B" — it answers: *now that we know B happened, how likely is A?*

**Analogy:** Imagine a classroom of 30 students. 10 wear glasses. 6 of those 10 are girls.
- *Normal question:* "Pick a random student — what's the chance they're a girl who wears glasses?" → You look at **all 30** students.
- *Conditional question:* "I've already picked someone with glasses — what's the chance they're a girl?" → You **only** look at the **10 glasses-wearers**. Answer: 6 out of 10.

That's the key idea: **the "given" shrinks your world**.

```
  BEFORE the condition (full classroom):

  All 30 students
  ┌──────────────────────────────────────────┐
  │  👦 👦 👧 👧 👦 👧 👦 👧 👦 👧          │  20 students
  │  👦 👧 👦 👧 👦 👧 👦 👧 👦 👧          │  WITHOUT glasses
  │──────────────────────────────────────────│
  │  🤓 🤓 🧒 🧒 🤓                        │  10 students
  │  🧒 🧒 🧒 🤓 🧒                        │  WITH glasses
  └──────────────────────────────────────────┘
       🤓 = boy with glasses (4)
       🧒 = girl with glasses (6)

  P(Girl with glasses) = 6/30      ← denominator is ALL 30

  AFTER the condition "wears glasses" (shrunk world):

  Only the 10 glasses-wearers
  ┌──────────────────────────────────────────┐
  │  🤓 🤓 🧒 🧒 🤓                        │
  │  🧒 🧒 🧒 🤓 🧒                        │
  └──────────────────────────────────────────┘
  P(Girl | glasses) = 6/10        ← denominator is only the 10

  The "given" (glasses) becomes your NEW total.
```

#### Real-World Use Cases

- **Medical Testing**: What is the probability a patient has a disease **given** they tested positive?
- **Spam Filtering**: What is the probability an email is spam **given** it contains certain keywords?
- **Insurance**: What is the probability of a car accident **given** the driver is under 25?
- **Quality Control**: What is the probability a product is defective **given** it came from Machine A?
- **Limitation**: Conditional probability requires knowing or estimating $P(A \cap B)$ and $P(B)$, which may not always be directly available — this is where Bayes' Theorem helps.

#### Steps

1. Identify which event has **already occurred** (the "given" event, $B$).
2. Identify the event whose probability you want to find ($A$).
3. Determine $P(A \cap B)$ — the probability that **both** events occur.
4. Determine $P(B)$ — the probability of the given event.
5. Divide: $P(A|B) = \frac{P(A \cap B)}{P(B)}$.

#### Formula

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad \text{where } P(B) > 0
$$

Where:

|    Symbol     | Pronunciation        | Meaning                                            |
| :-----------: | :------------------- | :------------------------------------------------- |
| $P(A \mid B)$ | "P of A given B"     | Probability of A occurring, knowing B has occurred |
| $P(A \cap B)$ | "P of A intersect B" | Probability of both A and B occurring together     |
|    $P(B)$     | "P of B"             | Probability of the given (conditioning) event B    |

> **Note:** Similarly, $P(B|A) = \frac{P(B \cap A)}{P(A)}$, where $A$ has already occurred.

#### Examples

**Example 1** — Rolling a die with a condition

You roll a standard 6-sided die. You are told the result is an **even number**. What is the probability that the result is **greater than 3**, given it is even?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $S = \{1, 2, 3, 4, 5, 6\}$ | Sample space |
> | $B = \{2, 4, 6\}$ | Event: result is even (already occurred) |
> | $A = \{4, 5, 6\}$ | Event: result is greater than 3 |
> | $A \cap B = \{4, 6\}$ | Both even AND greater than 3 |
> | Find: $P(A \mid B)$ | Probability of > 3 given even |

> **Step 1:** Write down the formula.
>
> $$P(A|B) = \frac{P(A \cap B)}{P(B)}$$
>
> **Step 2:** Calculate $P(A \cap B)$.
>
> $A \cap B = \{4, 6\}$, so $P(A \cap B) = \frac{2}{6} = \frac{1}{3}$
>
> **Step 3:** Calculate $P(B)$.
>
> $B = \{2, 4, 6\}$, so $P(B) = \frac{3}{6} = \frac{1}{2}$
>
> **Step 4:** Substitute into the formula.
>
> $$P(A|B) = \frac{\frac{1}{3}}{\frac{1}{2}} = \frac{1}{3} \times \frac{2}{1}$$
>
> **Step 5:** Simplify.
>
> $$\boxed{P(A|B) = \frac{2}{3} \approx 0.667 \text{ or } 66.7\%}$$

**Example 2** — Drawing cards with a condition

You draw one card from a standard 52-card deck. You are told the card is a **face card** (J, Q, or K). What is the probability that it is a **King**, given it is a face card?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $n(S) = 52$ | Total cards in the deck |
> | $B$ = face card (J, Q, K of each suit) | The given event |
> | $n(B) = 12$ | 4 Jacks + 4 Queens + 4 Kings |
> | $A$ = King | The event of interest |
> | $n(A) = 4$ | 4 Kings in the deck |
> | $A \cap B = A = \{$K♠, K♥, K♦, K♣$\}$ | All Kings are face cards |
> | Find: $P(A \mid B)$ | Probability of King given face card |

> **Step 1:** Write down the formula.
>
> $$P(A|B) = \frac{P(A \cap B)}{P(B)}$$
>
> **Step 2:** Calculate $P(A \cap B)$.
>
> Every King is a face card, so $A \cap B = A$: $P(A \cap B) = \frac{4}{52} = \frac{1}{13}$
>
> **Step 3:** Calculate $P(B)$.
>
> $P(B) = \frac{12}{52} = \frac{3}{13}$
>
> **Step 4:** Substitute into the formula.
>
> $$P(A|B) = \frac{\frac{1}{13}}{\frac{3}{13}} = \frac{1}{13} \times \frac{13}{3}$$
>
> **Step 5:** Simplify.
>
> $$\boxed{P(A|B) = \frac{1}{3} \approx 0.333 \text{ or } 33.3\%}$$
>
> This makes sense — among the 3 types of face cards (J, Q, K), each is equally likely, so the chance of King is $\frac{1}{3}$.

---

## 2. Bayes' Theorem

**Bayes' Theorem** is a formula that **reverses** a conditional probability. It lets you go from knowing $P(B|A)$ (how likely is the evidence given the hypothesis) to finding $P(A|B)$ (how likely is the hypothesis given the evidence). It is the foundation of _Bayesian statistics_, allowing us to **update** our beliefs as new data arrives.

```
  The Bayesian Update Process:

  ┌──────────┐      New Evidence      ┌───────────┐
  │  PRIOR   │  ──────────────────►   │ POSTERIOR │
  │  P(A)    │      (observed B)      │  P(A|B)   │
  │          │                        │           │
  │ "Initial │    Bayes' Theorem      │ "Updated  │
  │  belief" │    does the update     │  belief"  │
  └──────────┘                        └───────────┘

  Formula flow:

              P(B|A)  ×  P(A)
  P(A|B)  = ─────────────────
                  P(B)

  Posterior = (Likelihood × Prior) / Evidence
```

#### Real-World Use Cases

- **Medical Diagnosis**: Determining the probability of having a disease given a positive test result (accounting for false positives).
- **Spam Detection**: Updating the probability an email is spam given that it contains the word "free."
- **Legal Reasoning**: Assessing the probability of guilt given forensic evidence.
- **Machine Learning**: Naive Bayes classifiers use Bayes' Theorem to categorize text, images, etc.
- **Advantage**: Bayes' Theorem lets you incorporate **prior knowledge** — you don't start from scratch each time.

#### Steps

1. Identify the **hypothesis** ($A$) and the **evidence** ($B$).
2. Determine the **prior** $P(A)$ — initial probability of the hypothesis.
3. Determine the **likelihood** $P(B|A)$ — probability of seeing the evidence if the hypothesis is true.
4. Calculate the **evidence** $P(B)$ using the Law of Total Probability:
   $P(B) = P(B|A) \cdot P(A) + P(B|A') \cdot P(A')$
5. Apply Bayes' Theorem: $P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$.

#### Formula

$$
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
$$

Where:

|    Symbol     | Pronunciation    | Meaning                                                    |
| :-----------: | :--------------- | :--------------------------------------------------------- |
| $P(A \mid B)$ | "P of A given B" | **Posterior** — updated probability of A after observing B |
| $P(B \mid A)$ | "P of B given A" | **Likelihood** — probability of observing B if A is true   |
|    $P(A)$     | "P of A"         | **Prior** — initial probability of A before new evidence   |
|    $P(B)$     | "P of B"         | **Evidence** — total probability of B under all scenarios  |

- _Prior probability_: What you believed **before** seeing new data.
- _Posterior probability_: Your **updated** belief after seeing new data.
- _Likelihood_: How probable the evidence is, **assuming** the hypothesis is true.
- _Evidence (marginal)_: The overall probability of observing B, calculated via the _Law of Total Probability_.

#### Examples

**Example 1** — School uniform problem

At a school, **40% of students are boys** and **60% are girls**. All the boys wear pants. Half of the girls wear pants and the other half wear skirts. If you see a student from a distance wearing **pants**, what is the probability the student is a **girl**?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $P(\text{Girl}) = 0.60$ | Prior — proportion of girls |
> | $P(\text{Boy}) = 0.40$ | Proportion of boys |
> | $P(\text{Pants} \mid \text{Girl}) = 0.50$ | Likelihood — half the girls wear pants |
> | $P(\text{Pants} \mid \text{Boy}) = 1.00$ | All boys wear pants |
> | Find: $P(\text{Girl} \mid \text{Pants})$ | Posterior — probability of girl given pants |

> **Step 1:** Write down Bayes' Theorem.
>
> $$P(\text{Girl}|\text{Pants}) = \frac{P(\text{Pants}|\text{Girl}) \cdot P(\text{Girl})}{P(\text{Pants})}$$
>
> **Step 2:** Calculate $P(\text{Pants})$ using the Law of Total Probability.
>
> $$P(\text{Pants}) = P(\text{Pants}|\text{Girl}) \cdot P(\text{Girl}) + P(\text{Pants}|\text{Boy}) \cdot P(\text{Boy})$$
>
> $$P(\text{Pants}) = (0.50 \times 0.60) + (1.00 \times 0.40)$$
>
> $$P(\text{Pants}) = 0.30 + 0.40 = 0.70$$
>
> **Step 3:** Substitute into Bayes' Theorem.
>
> $$P(\text{Girl}|\text{Pants}) = \frac{0.50 \times 0.60}{0.70}$$
>
> **Step 4:** Simplify the numerator.
>
> $$P(\text{Girl}|\text{Pants}) = \frac{0.30}{0.70}$$
>
> **Step 5:** Divide.
>
> $$\boxed{P(\text{Girl}|\text{Pants}) = \frac{3}{7} \approx 0.429 \text{ or } 42.9\%}$$
>
> Even though there are more girls (60%), the fact that **all** boys wear pants shifts the probability. A random pants-wearer is more likely to be a boy (57.1%) than a girl (42.9%).

**Example 2** — Medical test accuracy

A disease affects **1 in 1,000 people** ($0.1\%$). A test for the disease is **99% accurate** — it correctly identifies a sick person 99% of the time ($P(\text{Positive}|\text{Disease}) = 0.99$) and correctly identifies a healthy person 99% of the time ($P(\text{Negative}|\text{No Disease}) = 0.99$), meaning the false positive rate is 1%. If a person tests **positive**, what is the probability they actually have the disease?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $P(\text{Disease}) = 0.001$ | Prior — 1 in 1,000 have the disease |
> | $P(\text{No Disease}) = 0.999$ | Complement of the prior |
> | $P(\text{Pos} \mid \text{Disease}) = 0.99$ | Likelihood — true positive rate |
> | $P(\text{Pos} \mid \text{No Disease}) = 0.01$ | False positive rate |
> | Find: $P(\text{Disease} \mid \text{Pos})$ | Posterior — probability of disease given positive test |

> **Step 1:** Write down Bayes' Theorem.
>
> $$P(\text{Disease}|\text{Pos}) = \frac{P(\text{Pos}|\text{Disease}) \cdot P(\text{Disease})}{P(\text{Pos})}$$
>
> **Step 2:** Calculate $P(\text{Pos})$ using the Law of Total Probability.
>
> $$P(\text{Pos}) = P(\text{Pos}|\text{Disease}) \cdot P(\text{Disease}) + P(\text{Pos}|\text{No Disease}) \cdot P(\text{No Disease})$$
>
> $$P(\text{Pos}) = (0.99 \times 0.001) + (0.01 \times 0.999)$$
>
> $$P(\text{Pos}) = 0.00099 + 0.00999 = 0.01098$$
>
> **Step 3:** Substitute into Bayes' Theorem.
>
> $$P(\text{Disease}|\text{Pos}) = \frac{0.99 \times 0.001}{0.01098}$$
>
> **Step 4:** Simplify the numerator.
>
> $$P(\text{Disease}|\text{Pos}) = \frac{0.00099}{0.01098}$$
>
> **Step 5:** Divide.
>
> $$\boxed{P(\text{Disease}|\text{Pos}) \approx 0.0902 \text{ or } 9.02\%}$$
>
> Despite a 99%-accurate test, a positive result only means a ~9% chance of actually having the disease. This is because the disease is so rare that **false positives** vastly outnumber **true positives** — a famous and counter-intuitive result of Bayes' Theorem.

---

<p align="left">
  <a href="./events.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./theorems.md"><b>Next →</b></a>
  </span>
</p>