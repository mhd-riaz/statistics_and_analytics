# Random Variable

## Definition
A **Random Variable** is a numerical description of the outcome of a statistical experiment. It is a mapping or a function that assigns a real number to each possible outcome in the sample space of a random process. Instead of looking at "Heads" or "Tails," a random variable allows us to work with numbers like "1" or "0."



## Formula
While there isn't a single "formula" for a random variable, it is typically denoted by an uppercase letter (like $X$) and defined as:
$$X: S \to \mathbb{R}$$

**Explanation of formula**:
- **$X$**: The Random Variable.
- **$S$**: The Sample Space (all possible outcomes).
- **$\to$**: Maps to.
- **$\mathbb{R}$**: The set of Real Numbers.

**Key concepts**:
- **Discrete Random Variable**: A variable that can take on only a countable number of distinct values (e.g., number of children, goals scored).
- **Continuous Random Variable**: A variable that can take any value within a range or interval (e.g., height, temperature, time).
- **Not "Random"**: Despite the name, the *function* itself is deterministic; the randomness comes from the underlying process that produces the outcome.
- **Probability Distribution**: A table or formula that tells us the probability for each possible value of the random variable.

## Example
Consider the experiment of **flipping a fair coin twice**. 

We want to define a random variable **$X$** as **the number of Heads** obtained.

**Step-by-Step Solution**:

1.  **List the Sample Space ($S$)**:
    * Possible outcomes: {TT, TH, HT, HH} (where T = Tails, H = Heads).

2.  **Assign Numerical Values to $X$**:
    * If the outcome is **TT**: $X = 0$ (Zero heads)
    * If the outcome is **TH**: $X = 1$ (One head)
    * If the outcome is **HT**: $X = 1$ (One head)
    * If the outcome is **HH**: $X = 2$ (Two heads)

3.  **Determine the Probability Distribution**:
    * $P(X = 0)$: There is 1 "TT" out of 4 outcomes. $P = 1/4 = 0.25$.
    * $P(X = 1)$: There are 2 outcomes ("TH", "HT") out of 4. $P = 2/4 = 0.50$.
    * $P(X = 2)$: There is 1 "HH" out of 4 outcomes. $P = 1/4 = 0.25$.

**Conclusion**: Our random variable $X$ can take the values {0, 1, 2}. By converting the coin flips into these numbers, we can now calculate the average (mean) or the spread (variance) of the results using math.