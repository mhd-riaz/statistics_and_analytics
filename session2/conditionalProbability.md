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