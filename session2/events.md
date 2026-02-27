<p align="left">
  <a href="./Probability.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./conditionalProbability.md"><b>Next →</b></a>
  </span>
</p>

# Events

```
Events
├── Events and Their Types
│   ├── Simple Event
│   ├── Compound Event
│   ├── Mutually Exclusive Events
│   ├── Independent Events
│   ├── Dependent Events
│   └── Complementary Events
│
└── Disjoint Events
    ├── Definition & Relationship to Mutually Exclusive
    ├── Addition Rule for Disjoint Events
    └── Worked Examples
```

---

## 1. Events and Their Types

In probability, an **event** is a specific outcome or a collection of outcomes resulting from an experiment. It is a subset of the sample space ($S$). Events can be categorized based on how they relate to one another or how many outcomes they contain.

```
  Sample Space S (all possible outcomes)
  ┌─────────────────────────────────────────────┐
  │                                             │
  │   ┌─── Event A ───┐   ┌─── Event B ───┐     │
  │   │  {outcome 1}  │   │  {outcome 3}  │     │
  │   │  {outcome 2}  │   │  {outcome 4}  │     │
  │   └───────────────┘   └───────────────┘     │
  │                                             │
  │         {outcome 5}   {outcome 6}           │
  │       (not in any defined event)            │
  └─────────────────────────────────────────────┘

  Types at a glance:
  ● Simple       →  one outcome only       →  {4}
  ● Compound     →  multiple outcomes      →  {2, 4, 6}
  ● Mutually Exclusive → cannot co-occur   →  A ∩ B = ∅
  ● Independent  →  one doesn't affect other
  ● Dependent    →  one changes the other
  ● Complementary → everything NOT in A    →  P(A) + P(A') = 1
```

#### Real-World Use Cases

- **Quality Control**: Classifying defects as simple events (one specific flaw) vs. compound events (any flaw from a set) to assess product failure rates.
- **Medical Diagnosis**: Treating test outcomes as complementary events — a patient either tests positive ($A$) or negative ($A'$).
- **Card Games / Gambling**: Identifying mutually exclusive events (a single card cannot be both a King and a Queen) to calculate winning probabilities.
- **Risk Assessment**: Determining whether failure modes are independent or dependent to model cascading system failures.
- **Limitation**: Misclassifying dependent events as independent (or vice versa) leads to incorrect probability calculations.

#### Steps

1. Identify the **experiment** and its **sample space** ($S$).
2. Define the **event(s)** of interest as subsets of $S$.
3. Classify each event by type (simple, compound, mutually exclusive, independent, dependent, or complementary).
4. Apply the appropriate probability formula based on the event type.

#### Formula

$$
P(E) = \frac{n(E)}{n(S)}
$$

Where:

| Symbol | Pronunciation | Meaning                                          |
| :----: | :------------ | :----------------------------------------------- |
| $P(E)$ | "P of E"      | The probability of event E occurring             |
| $n(E)$ | "n of E"      | The number of outcomes in event E                |
| $n(S)$ | "n of S"      | The total number of outcomes in the sample space |

#### Key Concepts

- _Simple Event_: An event with exactly **one** outcome. E.g., rolling a 4 on a die: $E = \{4\}$.
- _Compound Event_: An event with **more than one** outcome. E.g., rolling an even number: $E = \{2, 4, 6\}$.
- _Mutually Exclusive Events_: Events that **cannot happen at the same time**. If one occurs, the other cannot. E.g., turning left and turning right at the same intersection.
- _Independent Events_: The occurrence of one event **does not affect** the probability of the other. E.g., flipping a coin and rolling a die.
- _Dependent Events_: The occurrence of one event **changes** the probability of the other. E.g., drawing a card without replacement — the total outcomes shrink.
- _Complementary Events_: The event that includes all outcomes **not** in the original event. $P(A) + P(A') = 1$.

**CARDS**:

A standard deck of cards has 52 cards split into 4 suits of 13 cards each:
```
Standard Deck of 52 Cards
├── ♠ Spades   (13 cards) ── BLACK
├── ♣ Clubs    (13 cards) ── BLACK
├── ♥ Hearts   (13 cards) ── RED
└── ♦ Diamonds (13 cards) ── RED

Each suit contains 13 cards:
  A  2  3  4  5  6  7  8  9  10  J  Q  K
 (Ace)                            (Jack Queen King)
                                  └─ Face cards ──┘
```

#### Examples

**Example 1** — Identifying event types with a deck of cards

A standard deck has **52 cards**. Classify each of the following as a specific event type: <br>(a) drawing the Ace of Spades, <br>(b) drawing any red card, <br>(c) drawing a King vs. drawing a Queen in a single draw, <br>(d) if event $A$ is drawing a Heart, what is $A'$?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Standard deck of 52 cards | The experiment |
> | $n(S) = 52$ | Total possible outcomes |
> | (a) Ace of Spades | Single specific card |
> | (b) Red cards | Hearts + Diamonds = 26 cards |
> | (c) King vs. Queen | Two events in one draw |
> | (d) $A$ = Heart, find $A'$ | Complementary event |
> | Find: Event type for each | Classify each scenario |

> **Step 1:** Classify (a) — Drawing the Ace of Spades.
>
> Only **one** outcome satisfies this: $E = \{\text{Ace of Spades}\}$
> This is a **Simple Event**.
>
> **Step 2:** Classify (b) — Drawing any red card.
>
> There are **26** red cards (13 Hearts + 13 Diamonds): $E = \{R_1, R_2, \dots, R_{26}\}$
> This is a **Compound Event** (more than one outcome).
>
> **Step 3:** Classify (c) — Drawing a King vs. drawing a Queen in a single draw.
>
> A single card cannot be both a King **and** a Queen simultaneously.
> These are **Mutually Exclusive Events** ($\text{King} \cap \text{Queen} = \emptyset$).
>
> **Step 4:** Classify (d) — Complement of drawing a Heart.
>
> $A = \text{Heart}$ (13 cards), so $A' = \text{everything NOT a Heart}$ (Clubs, Spades, Diamonds = 39 cards).
> $P(A) + P(A') = \frac{13}{52} + \frac{39}{52} = 1$
>
> $$\boxed{A' = \{\text{Clubs, Spades, Diamonds}\},\quad P(A') = \frac{39}{52} = 0.75}$$

**Example 2** — Independent vs. dependent events

You flip a fair coin and then roll a standard 6-sided die. Are these events independent or dependent? Then, you draw 2 cards from a deck **without replacement**. Are these draws independent or dependent?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Scenario 1: Coin flip + die roll | Two separate actions |
> | Scenario 2: Draw 2 cards without replacement | Sequential draws from the same deck |
> | Find: Independent or dependent? | Classify each scenario |

> **Step 1:** Analyze Scenario 1 — Coin flip then die roll.
>
> The coin landing on Heads or Tails has **no effect** on which number the die shows.
> The sample space of the die remains $\{1,2,3,4,5,6\}$ regardless of the coin result.
> These are **Independent Events**.
>
> **Step 2:** Analyze Scenario 2 — Drawing 2 cards without replacement.
>
> On the 1st draw: $n(S) = 52$ cards.
> After drawing one card (and not replacing it): $n(S) = 51$ cards for the 2nd draw.
> The probability of the 2nd draw **changes** based on what was drawn first.
> These are **Dependent Events**.
>
> $$\boxed{\text{Scenario 1: Independent} \quad | \quad \text{Scenario 2: Dependent}}$$

---

## 2. Disjoint Events

**Disjoint events** (also known as **Mutually Exclusive events**) are two or more events that cannot happen at the same time. If one event occurs, the other cannot. In terms of sets, their intersection is empty ($\emptyset$), meaning they have no outcomes in common.

```
  Disjoint (Mutually Exclusive):         Non-Disjoint (Overlapping):

  ┌───────┐     ┌───────┐               ┌───────┐
  │   A   │     │   B   │               │   A ┌─┼───────┐
  │       │     │       │               │     │ │   B   │
  │{2,4,6}│     │{1,3,5}│               │     │ │       │
  └───────┘     └───────┘               └─────┼─┘       │
                                              └─────────┘
     A ∩ B = ∅                              A ∩ B ≠ ∅
     No shared outcomes                     Some shared outcomes
```

#### Real-World Use Cases

- **Coin Toss**: The result is either Heads or Tails — these are disjoint; it cannot be both.
- **Blood Type Classification**: A person's blood type is A, B, AB, or O — each is mutually exclusive.
- **Election Outcomes**: A candidate either wins or loses a specific seat — disjoint outcomes.
- **Scheduling**: Two meetings scheduled at the exact same time in the same room are mutually exclusive events.
- **Caveat**: Disjoint events are actually **highly dependent** — if you know $A$ happened, then $P(B) = 0$. Do not confuse disjoint with independent.

#### Steps

1. Define the two (or more) events and list their outcomes.
2. Check if they share **any** common outcomes ($A \cap B$).
3. If $A \cap B = \emptyset$, the events are **disjoint**.
4. Use the **Addition Rule** for disjoint events: $P(A \cup B) = P(A) + P(B)$.

#### Formula

$$
P(A \cap B) = 0
$$

$$
P(A \cup B) = P(A) + P(B)
$$

Where:

|    Symbol     | Pronunciation        | Meaning                                              |
| :-----------: | :------------------- | :--------------------------------------------------- |
| $P(A \cap B)$ | "P of A intersect B" | Probability of both A and B occurring simultaneously |
| $P(A \cup B)$ | "P of A union B"     | Probability of either A or B (or both) occurring     |
|    $P(A)$     | "P of A"             | Probability of event A                               |
|    $P(B)$     | "P of B"             | Probability of event B                               |
|  $\emptyset$  | "empty set"          | A set with no elements — no shared outcomes          |

#### Examples

**Example 1** — Rolling even vs. odd on a die

You roll a standard 6-sided die once. Let $A$ = rolling an **even** number and $B$ = rolling an **odd** number. Are $A$ and $B$ disjoint? What is $P(A \cup B)$?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Standard 6-sided die | The experiment |
> | $S = \{1, 2, 3, 4, 5, 6\}$ | Sample space |
> | $A = \{2, 4, 6\}$ | Event: rolling an even number |
> | $B = \{1, 3, 5\}$ | Event: rolling an odd number |
> | $n(S) = 6$ | Total possible outcomes |
> | Find: Are $A$ and $B$ disjoint? Find $P(A \cup B)$ | Classify and calculate |

> **Step 1:** List the outcomes for each event.
>
> $A = \{2, 4, 6\}$ and $B = \{1, 3, 5\}$
>
> **Step 2:** Check for common outcomes.
>
> $A \cap B = \{2, 4, 6\} \cap \{1, 3, 5\} = \emptyset$
> No number is both even and odd, so $P(A \cap B) = 0$.
>
> **Step 3:** Determine if they are disjoint.
>
> Since $A \cap B = \emptyset$, the events are **disjoint** (mutually exclusive).
>
> **Step 4:** Apply the Addition Rule for disjoint events.
>
> $$P(A \cup B) = P(A) + P(B) = \frac{3}{6} + \frac{3}{6}$$
>
> **Step 5:** Simplify.
>
> $$\boxed{P(A \cup B) = 0.5 + 0.5 = 1.0}$$
>
> Every roll is either even or odd, so the probability is 100%.

**Example 2** — Drawing a King vs. drawing a Queen from a deck

You draw **one card** from a standard 52-card deck. Let $A$ = drawing a King and $B$ = drawing a Queen. Are these events disjoint? What is the probability of drawing a King **or** a Queen?

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Standard 52-card deck | The experiment |
> | $A = \{\text{K♠, K♥, K♦, K♣}\}$ | Event: drawing a King |
> | $B = \{\text{Q♠, Q♥, Q♦, Q♣}\}$ | Event: drawing a Queen |
> | $n(A) = 4$ | Number of Kings |
> | $n(B) = 4$ | Number of Queens |
> | $n(S) = 52$ | Total cards in the deck |
> | Find: Are $A$ and $B$ disjoint? Find $P(A \cup B)$ | Classify and calculate |

> **Step 1:** List the outcomes for each event.
>
> $A = \{\text{K♠, K♥, K♦, K♣}\}$ and $B = \{\text{Q♠, Q♥, Q♦, Q♣}\}$
>
> **Step 2:** Check for common outcomes.
>
> $A \cap B = \emptyset$ — a single card cannot be both a King and a Queen.
> So $P(A \cap B) = 0$.
>
> **Step 3:** Determine if they are disjoint.
>
> Since $A \cap B = \emptyset$, the events are **disjoint**.
>
> **Step 4:** Calculate individual probabilities.
>
> $$P(A) = \frac{4}{52} = \frac{1}{13}, \quad P(B) = \frac{4}{52} = \frac{1}{13}$$
>
> **Step 5:** Apply the Addition Rule for disjoint events.
>
> $$P(A \cup B) = P(A) + P(B) = \frac{4}{52} + \frac{4}{52} = \frac{8}{52}$$
>
> **Step 6:** Simplify.
>
> $$\boxed{P(A \cup B) = \frac{2}{13} \approx 0.154 \text{ or } 15.4\%}$$

---

<p align="left">
  <a href="./Probability.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./conditionalProbability.md"><b>Next →</b></a>
  </span>
</p>