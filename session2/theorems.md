# Bayes' Theorem

## Definition
**Bayes' Theorem** is a mathematical formula used to determine the **conditional probability** of an event based on prior knowledge of conditions that might be related to the event. In simpler terms, it provides a way to update the probability of a hypothesis as more evidence or information becomes available. It is the foundation of Bayesian statistics, allowing us to move from "What is the probability of the evidence given a hypothesis?" to "What is the probability of the hypothesis given the evidence?"

## Formula
$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

**Explanation of formula**:
- **$P(A|B)$ (Posterior)**: The probability of event $A$ occurring given that $B$ has already occurred. This is what we want to find.
- **$P(B|A)$ (Likelihood)**: The probability of event $B$ occurring given that $A$ is true.
- **$P(A)$ (Prior)**: The initial probability of event $A$ before considering the new evidence $B$.
- **$P(B)$ (Evidence)**: The total probability of event $B$ occurring under all possible scenarios.

**Key concepts**:
- **Conditional Probability**: The likelihood of an event happening based on the occurrence of a previous event.
- **Prior Probability**: What you believed before seeing the new data.
- **Posterior Probability**: Your updated belief after seeing the new data.
- **Evidence**: The data or observation that triggers the update of your belief.

---

## Example
Imagine you are at a school where **40% of the students are boys** and **60% are girls**. 
- All the **boys wear pants**.
- Half of the **girls wear pants** (50%) and the other half wear skirts.

If you see a student from a distance wearing **pants**, what is the probability that the student is a **girl**?



### Step-by-Step Solution:

**1. Identify the known values:**
* $P(Girl)$ (Prior): $0.60$
* $P(Boy)$: $0.40$
* $P(Pants|Girl)$ (Likelihood): $0.50$ (Since half the girls wear pants)
* $P(Pants|Boy)$: $1.00$ (Since all boys wear pants)

**2. Calculate $P(Pants)$ (Total Evidence):**
To find the total probability of someone wearing pants, we add the probability of a boy wearing pants and a girl wearing pants:
* $P(Pants) = (P(Pants|Girl) \cdot P(Girl)) + (P(Pants|Boy) \cdot P(Boy))$
* $P(Pants) = (0.50 \cdot 0.60) + (1.00 \cdot 0.40)$
* $P(Pants) = 0.30 + 0.40 = 0.70$

**3. Apply Bayes' Theorem to find $P(Girl|Pants)$:**
We want to find the probability that the student is a girl, given we know they are wearing pants.
* $P(Girl|Pants) = \frac{P(Pants|Girl) \cdot P(Girl)}{P(Pants)}$
* $P(Girl|Pants) = \frac{0.50 \cdot 0.60}{0.70}$
* $P(Girl|Pants) = \frac{0.30}{0.70}$
* $P(Girl|Pants) = \frac{3}{7} \approx 0.428$

**Result:**
There is approximately a **42.8%** chance that the student wearing pants is a girl. Even though there are more girls in the school, the fact that all boys wear pants makes it slightly more likely that a random person in pants is a boy.





# Total Probability Theorem

## Definition
The **Total Probability Theorem** is a fundamental rule that allows us to find the overall probability of an event by breaking it down into several distinct scenarios or "partitions." If we know the likelihood of an event happening under different conditions, we can sum those parts to find the total likelihood of that event occurring.



## Formula
$$P(B) = \sum_{i=1}^{n} P(B|A_i)P(A_i)$$

**Explanation of formula**:
- **$P(B)$**: The total probability of the event we are interested in.
- **$P(A_i)$**: The probability of each specific scenario or partition $i$.
- **$P(B|A_i)$**: The probability of event **B** occurring, given that scenario $A_i$ happened.
- **$\sum$**: The summation symbol, meaning we add up the results for every possible scenario from $1$ to $n$.

**Key concepts**:
- **Partitioning**: The sample space must be divided into scenarios ($A_1, A_2, ... A_n$) that are **disjoint** (cannot happen at the same time) and **exhaustive** (cover all possibilities).
- **Weighted Average**: You can think of this theorem as a weighted average of the conditional probabilities, where the weights are the probabilities of each scenario.
- **Foundation for Bayes**: This theorem is the "denominator" used in Bayes' Theorem to normalize probabilities.

## Example
A tech company has three servers: **Server 1**, **Server 2**, and **Server 3**. 
- **Server 1** handles **50%** of the traffic and has a **1%** error rate.
- **Server 2** handles **30%** of the traffic and has a **2%** error rate.
- **Server 3** handles **20%** of the traffic and has a **5%** error rate.

If a random request is made, what is the **total probability** that it results in an error?

**Step-by-Step Solution**:

1.  **Identify the scenarios (Partitions)**:
    * $P(A_1)$ (Server 1): 0.50
    * $P(A_2)$ (Server 2): 0.30
    * $P(A_3)$ (Server 3): 0.20

2.  **Identify the conditional probabilities (Error rates)**:
    * $P(Error|A_1)$: 0.01
    * $P(Error|A_2)$: 0.02
    * $P(Error|A_3)$: 0.05

3.  **Apply the Total Probability Theorem**:
    * $P(Error) = [P(Error|A_1) \times P(A_1)] + [P(Error|A_2) \times P(A_2)] + [P(Error|A_3) \times P(A_3)]$
    * $P(Error) = [0.01 \times 0.50] + [0.02 \times 0.30] + [0.05 \times 0.20]$

4.  **Calculate the values**:
    * $P(Error) = 0.005 + 0.006 + 0.010$
    * $P(Error) = 0.021$

**Conclusion**: The total probability of a request resulting in an error across all servers is **2.1%**.



# Addition Theorem

## Definition
The **Addition Theorem** (also known as the **Probability Addition Rule**) provides a way to calculate the probability that at least one of two events occurs. It accounts for the fact that if two events are not disjoint, they might happen simultaneously, and we must avoid double-counting that overlapping probability.



## Formula
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**Explanation of formula**:
- **$P(A \cup B)$**: The probability that event **A** OR event **B** (or both) occurs.
- **$P(A)$**: The individual probability of event **A**.
- **$P(B)$**: The individual probability of event **B**.
- **$P(A \cap B)$**: The probability that both **A** and **B** occur at the same time (the intersection). This is subtracted to ensure the overlap is only counted once.

**Key concepts**:
- **The "OR" Rule**: Whenever you see "Probability of A or B," you should think of the Addition Theorem.
- **Inclusion-Exclusion**: This is a simple form of the Principle of Inclusion-Exclusion. We include the probabilities of A and B, then exclude the part where they overlap.
- **Special Case (Disjoint)**: If the events cannot happen together, $P(A \cap B) = 0$, and the formula simplifies to $P(A) + P(B)$.

## Example
In a class of **30 students**:
- **15 students** play **Football**.
- **10 students** play **Basketball**.
- **5 students** play **both** Football and Basketball.

If you pick one student at random, what is the probability that they play **either** Football or Basketball?

**Step-by-Step Solution**:

1.  **Identify the individual probabilities**:
    * Total students = 30.
    * $P(Football) = \frac{15}{30} = 0.5$
    * $P(Basketball) = \frac{10}{30} \approx 0.333$

2.  **Identify the intersection (the overlap)**:
    * Students playing both = 5.
    * $P(Football \cap Basketball) = \frac{5}{30} \approx 0.167$

3.  **Apply the Addition Theorem**:
    * $P(Football \cup Basketball) = P(Football) + P(Basketball) - P(Football \cap Basketball)$
    * $P(Football \cup Basketball) = \frac{15}{30} + \frac{10}{30} - \frac{5}{30}$

4.  **Calculate the final result**:
    * $P(Football \cup Basketball) = \frac{20}{30}$
    * $P(Football \cup Basketball) = \frac{2}{3} \approx 0.667$ (or **66.7%**)

**Conclusion**: There is a **66.7%** chance that a randomly selected student plays at least one of the two sports.s


# Multiplication Theorem

## Definition
The **Multiplication Theorem** (also known as the **Probability Multiplication Rule**) is used to find the probability that two events, Event **A** and Event **B**, both occur. It is derived from the definition of conditional probability and describes the likelihood of the intersection of two events.






## Formula
For any two events:
$$P(A \cap B) = P(A) \cdot P(B|A)$$

If the events are **independent**:
$$P(A \cap B) = P(A) \cdot P(B)$$

**Explanation of formula**:
- **$P(A \cap B)$**: The probability that both event **A** and event **B** happen.
- **$P(A)$**: The probability of the first event occurring.
- **$P(B|A)$**: The probability of event **B** occurring *given* that **A** has already happened.
- **$\cdot$**: Represents multiplication.

**Key concepts**:
- **The "AND" Rule**: When you want to find the probability of one event AND another event happening in sequence or together, you multiply.
- **Dependence**: If the outcome of the first event changes the chances of the second event (like picking a card and not putting it back), you must use the conditional probability $P(B|A)$.
- **Independence**: If the first event doesn't affect the second (like flipping a coin twice), you simply multiply the two individual probabilities.

## Example
Imagine you have a deck of **52 playing cards**. You draw **two cards** one after the other **without replacement** (meaning you don't put the first card back). 

What is the probability that **both cards are Aces**?

**Step-by-Step Solution**:

1.  **Identify the first event ($A$)**:
    * Event A: The first card is an Ace.
    * There are 4 Aces in a deck of 52.
    * $P(A) = \frac{4}{52} = \frac{1}{13}$

2.  **Identify the second event ($B|A$)**:
    * Event B|A: The second card is an Ace, given the first was an Ace.
    * Since we didn't put the first Ace back, there are now **3 Aces** left in a deck of **51 cards**.
    * $P(B|A) = \frac{3}{51} = \frac{1}{17}$

3.  **Apply the Multiplication Theorem**:
    * $P(A \cap B) = P(A) \cdot P(B|A)$
    * $P(A \cap B) = \frac{4}{52} \cdot \frac{3}{51}$

4.  **Calculate the result**:
    * $P(A \cap B) = \frac{1}{13} \cdot \frac{1}{17}$
    * $P(A \cap B) = \frac{1}{221} \approx 0.0045$ (or **0.45%**)

**Conclusion**: The chance of drawing two Aces in a row without replacing the first card is very low—about **0.45%**.