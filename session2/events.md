



# Events and its Types

## Definition
In probability, an **event** is a specific outcome or a collection of outcomes resulting from an experiment. It is a subset of the sample space. Events can be categorized based on how they relate to one another or how many outcomes they contain.

## Formula (Human readable formula)

> $P(E) = \frac{\text{Outcomes in Event } E}{\text{Total Outcomes in Sample Space } S}$

- **$E$**: The specific event or set of outcomes.
- **$S$**: The sample space (every possible outcome).
- **$P(E)$**: The likelihood that the event $E$ occurs.

## Types of Events

### 1. Simple Event
An event that consists of only one single outcome.
* **Example**: Rolling a 4 on a six-sided die.

### 2. Compound Event
An event that includes more than one outcome from the sample space.
* **Example**: Rolling an "even number" on a die (includes 2, 4, and 6).

### 3. Mutually Exclusive Events
Events that cannot happen at the same time. If one happens, the other cannot.
* **Example**: Turning left and turning right at the same intersection simultaneously.

### 4. Independent Events
The occurrence of one event does not affect the probability of the other event happening.
* **Example**: Flipping a coin and then rolling a die. The coin result doesn't change the die's odds.

### 5. Dependent Events
The occurrence of the first event changes the probability of the second event.
* **Example**: Drawing a sock from a drawer and not putting it back. The "total outcomes" for the next draw has changed.

### 6. Complementary Events
The event that includes all outcomes in the sample space that are *not* part of the original event.
* **Formula**: $P(A) + P(A') = 1$

## Example
Imagine you are a grade 10 student playing with a standard deck of 52 cards.

* **Simple Event**: Drawing specifically the "Ace of Spades."
* **Compound Event**: Drawing any "Red Card" (there are 26 possible outcomes: all hearts and diamonds).
* **Mutually Exclusive**: You cannot draw a card that is both a "King" and a "Queen" at the exact same time.
* **Complementary**: If event **A** is drawing a "Heart," the complementary event **A'** is drawing "anything that is not a Heart" (Clubs, Spades, or Diamonds).




# Disjoint Events

## Definition
**Disjoint events** (also known as **Mutually Exclusive events**) are two or more events that cannot happen at the same time. If one event occurs, the other cannot. In terms of sets, their intersection is empty, meaning they have no outcomes in common.



## Formula
$$P(A \cap B) = 0$$

**Addition Rule for Disjoint Events**:
$$P(A \cup B) = P(A) + P(B)$$

**Explanation of formula**:
- **$P(A \cap B) = 0$**: The probability of both event **A** and event **B** happening at the same time is zero.
- **$P(A \cup B)$**: The probability of either event **A** OR event **B** occurring.
- **$P(A) + P(B)$**: Because there is no overlap to subtract, you simply add the individual probabilities together.

**Key concepts**:
- **Mutual Exclusivity**: This is just another name for disjoint. They "exclude" each other.
- **No Overlap**: On a Venn diagram, the circles for disjoint events do not touch or overlap.
- **Difference from Independence**: Disjoint events are actually highly dependent. If you know event A happened, the probability of B happening becomes 0%.

## Example
Consider a single roll of a standard **6-sided die**. 

Let's define two events:
- **Event A**: Rolling an **Even** number (2, 4, 6).
- **Event B**: Rolling an **Odd** number (1, 3, 5).

**Step-by-Step Solution**:

1.  **List the outcomes for each event**:
    * Outcomes for A: {2, 4, 6}
    * Outcomes for B: {1, 3, 5}

2.  **Check for common outcomes**:
    * Look at both lists. Is there any number that appears in both? 
    * No. There is no number that is both even and odd.

3.  **Determine if they are disjoint**:
    * Since $A \cap B = \emptyset$ (an empty set), the events are **disjoint**.

4.  **Calculate the probability of rolling an Even OR an Odd number**:
    * $P(A) = \frac{3}{6} = 0.5$
    * $P(B) = \frac{3}{6} = 0.5$
    * $P(A \cup B) = P(A) + P(B) = 0.5 + 0.5 = 1.0$

**Conclusion**: Since the events are disjoint, the probability of one or the other happening is 100%, which makes sense because every number on a die is either even or odd.