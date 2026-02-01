# Probability

## Definition 
Probability is the branch of mathematics that quantifies uncertainty. It measures the likelihood of an event occurring, expressed as a number between 0 and 1, where 0 indicates impossibility and 1 indicates certainty.

## Formula (Human readable formula)
> $P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}$

- **$P(A)$**: The probability of event A occurring.
- **Favorable outcomes**: The specific results you are looking for.
- **Total outcomes**: The set of all possible results (the sample space).

## Fundamentals

### 1. Sample Space ($S$)
The set of all possible outcomes of an experiment. For a coin toss, $S = \{Heads, Tails\}$.

### 2. Events ($E$)
A subset of the sample space. For example, rolling an even number on a die is an event: $E = \{2, 4, 6\}$.

### 3. Complementary Events
The probability that an event does *not* occur. 
> $P(A') = 1 - P(A)$

### 4. Independent vs. Dependent Events
* **Independent**: The outcome of one event does not affect the other (e.g., tossing two separate coins).
* **Dependent**: The outcome of one event affects the likelihood of the next (e.g., drawing a card from a deck and not replacing it before drawing a second).

## Example
Imagine you have a bag containing **10 marbles**: 3 are red, 5 are blue, and 2 are green. If you reach in and grab one marble without looking, what is the probability of picking a red one?

* **Favorable outcomes**: 3 (the red marbles).
* **Total outcomes**: 10 (all the marbles in the bag).

Using the formula:
$$P(\text{Red}) = \frac{3}{10} = 0.3 \text{ or } 30\%$$

This means there is a 30% chance you will pick a red marble.




# Experiment vs. Trial

## Definition
In statistics, an **experiment** is a structured process or investigation intended to discover, verify, or demonstrate a particular fact. A **trial** is a single performance or observation within that experiment. Think of the experiment as the "whole project" and the trial as "one single attempt."

## Formula

> $\text{Experiment} = \sum_{i=1}^{n} \text{Trial}_i$
  
    - **Experiment**: The total collection of all repeated attempts.
    - **Trial**: A single, individual iteration (represented by $i$).
    - **$n$**: The total number of times the trial is repeated.

## Example
Imagine you want to test if a coin is fair. You decide to flip the coin **50 times**.

* **The Experiment**: The entire process of flipping the coin 50 times and recording the results to see if it lands on heads about half the time.
* **The Trial**: Every single time you flip the coin. The 1st flip is a trial, the 2nd flip is a trial, and so on, until the 50th trial.

If you are a grade 10 student doing a science fair project on which brand of battery lasts longest, the entire project is your **experiment**, while testing one specific battery until it dies is a single **trial**.





# P(A) vs. P(E)

## Definition
In probability notation, **P(A)** and **P(E)** are functionally the same thing. They both represent the probability of a specific outcome occurring. The letter inside the parentheses is simply a label or a "placeholder" for an event. Traditionally, **"E"** is used to stand for **Event**, while **"A"** (along with B and C) is used as a generic variable to distinguish between different specific events in the same problem.

## Formula (Human readable formula)
> $P(A) = P(E) = \frac{n}{N}$

- **$P$**: Probability function.
- **$A$ or $E$**: The specific event or outcome we are measuring.
- **$n$**: Number of successful outcomes for that specific label.
- **$N$**: Total possible outcomes in the sample space.

## Example
Imagine you are rolling a standard six-sided die.

* **Using P(E):** You might say, "Let **E** be the event of rolling an even number." 
    Since the even numbers are $\{2, 4, 6\}$, $P(E) = \frac{3}{6} = 0.5$.
    
* **Using P(A):** You might say, "Let **A** be the event of rolling a 5."
    Since there is only one 5, $P(A) = \frac{1}{6} \approx 0.167$.

If a math problem asks for $P(A)$ and $P(B)$, it is simply asking you to calculate the probability for two different scenarios within the same experiment.


# Sample Space and Cardinalities

## Definition
The **Sample Space** ($S$) is the set of all possible outcomes of a random experiment. **Cardinality**, denoted as $|S|$ or $n(S)$, is the total number of elements or outcomes contained within that sample space. It tells you "how many" possible results exist.

## Formula (Human readable formula)
> $|S| = n_1 \times n_2 \times \dots \times n_k$

- **$S$**: The Sample Space (the set of outcomes).
- **$|S|$**: The Cardinality (the count of outcomes).
- **$n$**: The number of options for each individual step in the experiment (Fundamental Counting Principle).

## Key Concepts

### 1. Identifying the Sample Space
To find the sample space, you list every possible unique result. 
* For a single coin flip: $S = \{H, T\}$
* For a single 6-sided die: $S = \{1, 2, 3, 4, 5, 6\}$

### 2. Determining Cardinality
Once the set is defined, you simply count the members.
* If $S = \{H, T\}$, then $|S| = 2$.
* If $S = \{1, 2, 3, 4, 5, 6\}$, then $|S| = 6$.

### 3. The Fundamental Counting Principle
If an experiment has multiple steps, you multiply the cardinality of each step to find the total cardinality.
* **Example**: If you flip a coin ($2$ outcomes) AND roll a die ($6$ outcomes), the total cardinality is $2 \times 6 = 12$.

## Example
Imagine you are at a snack bar. You can choose **one drink** (Soda, Water, or Juice) and **one snack** (Chips or Cookies).

**The Sample Space ($S$):**
$S = \{(Soda, Chips), (Soda, Cookies), (Water, Chips), (Water, Cookies), (Juice, Chips), (Juice, Cookies)\}$

**The Cardinality ($|S|$):**
You can count them manually, or use the formula:
* Drink options ($n_1$) = 3
* Snack options ($n_2$) = 2
* $|S| = 3 \times 2 = 6$

There are **6** possible combinations in your sample space.
