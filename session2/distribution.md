# Probability Distribution

## Definition
A **Probability Distribution** is a mathematical function or a table that describes the likelihood of obtaining the possible values that a random variable can take. It maps every possible outcome of a random process to its corresponding probability of occurrence. Essentially, it tells you how the total probability (which is always 1) is "distributed" across the sample space.



## Types of distribution:
The formula depends on the type of random variable:


### For Discrete
1. Bernoulli distribution: used if it has one of the two favourable outcomes, boolean choice
2. Binomial distribution: sequence of bernoulli, when you have more than 1 choice, more than two favourable outcomes
3. Poisson distribution: 

### For Continious
4. Normal Distribution



# Bernoulli Distribution

## Definition
The **Bernoulli Distribution** is the simplest discrete probability distribution. It represents a single experiment that has exactly two possible outcomes: **"Success"** (usually represented by 1) and **"Failure"** (usually represented by 0). The probability of success is denoted by $p$, and the probability of failure is $q = 1 - p$.



## Formula
For a random variable $X$:
$$P(X = x) = p^x (1 - p)^{1 - x}$$
where $x \in \{0, 1\}$.

**Explanation of formula**:
- **$X$**: The Bernoulli random variable.
- **$x$**: The outcome (1 for success, 0 for failure).
- **$p$**: The probability of success ($0 \le p \le 1$).
- **$1 - p$**: The probability of failure (often written as $q$).
- **If $x=1$**: The formula becomes $p^1(1-p)^0 = p$.
- **If $x=0$**: The formula becomes $p^0(1-p)^1 = 1-p$.

**Key concepts**:
- **Single Trial**: It only models one single event (one flip, one check, one trial).
- **Mutually Exclusive**: You cannot have both success and failure at the same time.
- **Mean ($\mu$)**: The expected value is simply $p$.
- **Variance ($\sigma^2$)**: The spread is $p(1 - p)$.

## Example 1
**Scenario**: Tossing a biased coin where the probability of getting **Heads** is 0.7.
Let $X = 1$ if it is Heads (Success) and $X = 0$ if it is Tails (Failure).

**Step-by-Step**:
1.  **Identify $p$**: $p = 0.7$.
2.  **Identify $q$**: $q = 1 - 0.7 = 0.3$.
3.  **Distribution**: 
    * $P(X=1) = 0.7$
    * $P(X=0) = 0.3$
4.  **Conclusion**: This is a Bernoulli trial with parameter $p = 0.7$.

## Example 2
**Scenario**: A student takes a single "True or False" question on a college entrance exam by guessing randomly.

**Step-by-Step**:
1.  **Define Success**: Getting the answer right ($X=1$).
2.  **Determine $p$**: Since there are 2 choices and only one is correct, $p = 0.5$.
3.  **Apply Mean Formula**: The expected number of correct answers for this one question is $E[X] = p = 0.5$.
4.  **Apply Variance Formula**: $Var(X) = 0.5(1 - 0.5) = 0.25$.
5.  **Conclusion**: Random guessing on a binary choice is a Bernoulli trial with $p=0.5$.

## Example 3
**Scenario**: In your **Golang backend**, you are implementing a health check for a microservice. The service is either **Up (1)** or **Down (0)**.

**Step-by-Step**:
1.  **Problem**: You want to model the reliability of the service. Based on logs, the service has an uptime of 99.9%.
2.  **Data**: $p = 0.999$ (Success/Up), $q = 0.001$ (Failure/Down).
3.  **Implementation**: Every time your React frontend pings the backend, it encounters a Bernoulli trial. 
4.  **Simulation**: If you were writing a load test script, you would use a Bernoulli distribution to simulate service failures.
5.  **Conclusion**: A single "Health Check" is a real-world application of the Bernoulli distribution.



# Bernoulli Distribution

## Definition
The **Bernoulli Distribution** is the simplest discrete probability distribution. It models a single experiment—called a **Bernoulli Trial**—that has exactly two possible outcomes: **"Success"** (represented by the value 1) and **"Failure"** (represented by the value 0). 



## Formula
For a random variable $X$:
$$P(X = x) = p^x (1 - p)^{1 - x}$$
where $x \in \{0, 1\}$.

**Explanation of formula**:
- **$X$**: The Bernoulli random variable.
- **$x$**: The outcome, which can only be 1 or 0.
- **$p$**: The probability of success ($P(X=1)$).
- **$1 - p$**: The probability of failure ($P(X=0)$), often denoted as $q$.
- **If $x=1$**: The formula simplifies to $p^1(1-p)^0 = p$.
- **If $x=0$**: The formula simplifies to $p^0(1-p)^1 = 1-p$.

**Key concepts**:
- **Single Trial**: It represents only one instance of an event (e.g., one flip, one click).
- **Binary Outcome**: The outcomes must be mutually exclusive and exhaustive (Success vs. Failure).
- **Mean ($\mu$)**: The expected value is always $p$.
- **Variance ($\sigma^2$ )**: The spread of the distribution is calculated as $p(1 - p)$.

## Example 1
**Scenario**: Flipping a coin where you win if it's **Heads**.
Assuming the coin is fair, the probability of Heads is 0.5.

**Step-by-Step Solution**:
1.  **Define Success**: Heads ($X=1$).
2.  **Define Probability**: $p = 0.5$.
3.  **Find Failure Probability**: $q = 1 - 0.5 = 0.5$.
4.  **Distribution**: 
    * $P(X=1) = 0.5$
    * $P(X=0) = 0.5$
5.  **Conclusion**: This is a classic Bernoulli trial with $p=0.5$.

## Example 2
**Scenario**: A student guesses the answer to a single **Multiple Choice Question** that has 4 options (A, B, C, D).

**Step-by-Step Solution**:
1.  **Identify Success**: Picking the one correct option.
2.  **Calculate $p$**: Since there is 1 correct option out of 4, $p = 1/4 = 0.25$.
3.  **Calculate $q$**: $1 - 0.25 = 0.75$.
4.  **Calculate Mean**: $E[X] = p = 0.25$.
5.  **Calculate Variance**: $Var(X) = 0.25 \times 0.75 = 0.1875$.
6.  **Conclusion**: The "guessed question" follows a Bernoulli distribution with $p=0.25$.

## Example 3
**Scenario**: In your **Golang backend**, you are checking if a user is "Premium" or "Free" to determine which UI components to render in **React**.

**Step-by-Step Solution**:
1.  **Context**: You have 10,000 users, and 1,500 of them are Premium.
2.  **Define $p$**: The probability that a randomly logged-in user is Premium is $1500/10000 = 0.15$.
3.  **Real-World Application**: When a request hits your backend, you can model the "Premium status" of that single user as a Bernoulli trial where $p=0.15$. 
4.  **Analysis**: If you want to simulate 100 random users hitting your server to see how many Premium features are loaded, you would be moving from a Bernoulli distribution to a **Binomial distribution** (multiple Bernoulli trials).
5.  **Conclusion**: Any Boolean flag in your code (`is_active`, `is_paid`, `has_error`) essentially represents a Bernoulli random variable.





# Poisson Distribution

## Definition
The **Poisson Distribution** is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space. It is used for events that occur with a known constant mean rate and independently of the time since the last event.



## Formula
$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

**Explanation of formula**:
- **$P(X = k)$**: The probability of observing exactly $k$ events.
- **$\lambda$ (Lambda)**: The average number of events in the given interval (mean rate).
- **$e$**: Euler's number (approximately 2.71828).
- **$k$**: The number of occurrences ($k = 0, 1, 2, ...$).
- **$k!$**: The factorial of $k$.

**Key concepts**:
- **Independence**: The occurrence of one event does not affect the probability of another event occurring.
- **Constant Rate**: The average number of events per unit of time/space is assumed to be constant.
- **Discrete Outcomes**: You can have 1, 2, or 3 events, but not 2.5 events.
- **Mean and Variance**: Uniquely, for a Poisson distribution, the **Mean** and the **Variance** are both equal to $\lambda$.

## Example 1
**Scenario**: A small bakery receives an average of **3 customers per hour**. What is the probability that exactly **2 customers** will arrive in the next hour?

**Step-by-Step Solution**:
1.  **Identify parameters**: $\lambda = 3$ (average customers), $k = 2$ (desired customers).
2.  **Apply the formula**:
    * $P(X = 2) = \frac{3^2 \cdot e^{-3}}{2!}$
3.  **Calculate values**:
    * $3^2 = 9$
    * $e^{-3} \approx 0.0498$
    * $2! = 2 \cdot 1 = 2$
4.  **Final Calculation**:
    * $P(X = 2) = \frac{9 \cdot 0.0498}{2} = \frac{0.4482}{2} = 0.2241$

**Conclusion**: There is a **22.41%** chance that exactly 2 customers will arrive.

## Example 2
**Scenario**: A book has an average of **0.5 typos per page**. What is the probability that a randomly selected page has **no typos**?

**Step-by-Step Solution**:
1.  **Identify parameters**: $\lambda = 0.5$, $k = 0$.
2.  **Apply the formula**:
    * $P(X = 0) = \frac{0.5^0 \cdot e^{-0.5}}{0!}$
3.  **Calculate values**:
    * $0.5^0 = 1$
    * $e^{-0.5} \approx 0.6065$
    * $0! = 1$
4.  **Final Calculation**:
    * $P(X = 0) = \frac{1 \cdot 0.6065}{1} = 0.6065$

**Conclusion**: There is a **60.65%** chance that a page will be perfectly free of typos.

## Example 3
**Scenario**: In your **Golang backend**, you are tracking the number of **API requests** per second to your home server. Your logs show an average of **10 requests/sec**. You want to know the probability of a "burst" of **15 requests/sec** to prepare for potential latency in your **React** frontend.

**Step-by-Step Solution**:
1.  **Identify parameters**: $\lambda = 10$, $k = 15$.
2.  **Apply the formula**:
    * $P(X = 15) = \frac{10^{15} \cdot e^{-10}}{15!}$
3.  **Real-World Logic**: In a production environment, you would use a library (like `math` in Go) to calculate this.
    * $10^{15}$ is a massive number, and $15!$ is also huge ($1,307,674,368,000$).
    * $P(X = 15) \approx 0.0347$.
4.  **Conclusion**: There is only a **3.47%** chance of hitting exactly 15 requests in a single second. This helps you realize that while a burst of 15 is possible, it is relatively rare, allowing you to set appropriate rate-limiting thresholds.





# Normal Distribution

## Definition
The **Normal Distribution** (also known as the **Gaussian Distribution**) is the most important continuous probability distribution in statistics. It describes a symmetrical, bell-shaped curve where most of the observations cluster around the central peak (the mean), and the probabilities for values further away from the mean taper off equally in both directions.



## Formula
The Probability Density Function (PDF) is:
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$

**Explanation of formula**:
- **$f(x)$**: The probability density at point $x$.
- **$\mu$ (Mu)**: The mean or expectation of the distribution (the center of the bell).
- **$\sigma$ (Sigma)**: The standard deviation, which determines the width or "spread" of the bell.
- **$e$**: Euler's number ($\approx 2.71828$).
- **$\pi$**: Archimedes' constant ($\approx 3.14159$).

**Key concepts**:
- **Symmetry**: The left half is a mirror image of the right half. Mean, Median, and Mode are all equal at the center.
- **The 68-95-99.7 Rule**: 
    - **68%** of data falls within $1\sigma$ of the mean.
    - **95%** of data falls within $2\sigma$ of the mean.
    - **99.7%** of data falls within $3\sigma$ of the mean.
- **Central Limit Theorem**: This distribution is crucial because the sum of many independent random variables tends toward a normal distribution, regardless of the original distribution.

## Example 1
**Scenario**: The weights of a specific breed of **freshwater fish** in your 150-liter aquarium follow a normal distribution.
The average weight ($\mu$) is **5 grams** with a standard deviation ($\sigma$) of **1 gram**.

**Step-by-Step Solution**:
1.  **Identify the Mean**: $\mu = 5$.
2.  **Apply the Rule**: What is the probability a fish weighs between 4g and 6g?
3.  **Calculate**: Since 4g and 6g are exactly $1\sigma$ away from the mean ($5-1$ and $5+1$):
    * According to the 68-95-99.7 rule, the probability is **0.68**.
4.  **Conclusion**: There is a **68% chance** that a randomly picked fish weighs between 4 and 6 grams.

## Example 2
**Scenario**: A college entrance exam has scores that are normally distributed with a **mean of 70** and a **standard deviation of 10**. A student scores an **85**.

**Step-by-Step Solution**:
1.  **Find the Z-score**: This tells us how many standard deviations the score is from the mean.
    * $Z = \frac{x - \mu}{\sigma} = \frac{85 - 70}{10} = 1.5$
2.  **Look up the Z-table**: A Z-score of 1.5 corresponds to a cumulative probability of approximately **0.9332**.
3.  **Interpret**: This means the student performed better than **93.32%** of all test-takers.
4.  **Conclusion**: The student is in the top 7% of the class.

## Example 3
**Scenario**: You are measuring the **latency (response time)** of your **Golang API** that serves your **React** frontend.
The latency is normally distributed with $\mu = 200ms$ and $\sigma = 20ms$.

**Step-by-Step Solution**:
1.  **Problem**: You want to set a timeout in your React code so that only **2.5%** of requests fail.
2.  **Analysis**: In a normal distribution, the top 2.5% starts at approximately $+2\sigma$ from the mean.
3.  **Calculation**:
    * $Timeout = \mu + 2\sigma$
    * $Timeout = 200ms + 2(20ms) = 240ms$
4.  **Implementation**: You set your frontend timeout to **240ms**.
5.  **Conclusion**: By understanding the normal distribution of your server's performance, you can mathematically ensure that **97.5%** of your users experience a successful request without waiting too long.



# Summary of Key Probability Distributions

Here is a summarized comparison of the four distributions we discussed. This table highlights their primary use cases, whether they are discrete or continuous, and their core mathematical properties.

| Distribution  | Type       | Key Parameter(s)                 | Typical Use Case                                                                         | Main Characteristic                                                                              |
| :------------ | :--------- | :------------------------------- | :--------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| **Bernoulli** | Discrete   | $p$ (Success probability)        | A single Yes/No trial (e.g., Is a user "Premium"?)                                       | Only two outcomes (0 or 1).                                                                      |
| **Binomial*** | Discrete   | $n$ (Trials), $p$ (Probability)  | Number of successes in $n$ independent Bernoulli trials                                  | Sum of multiple Bernoulli events.                                                                |
| **Poisson**   | Discrete   | $\lambda$ (Mean rate)            | Number of events in a fixed time/space (e.g., API requests/ sec)                         | Mean and Variance are equal ($\lambda$). (Keyword - **event, avg, in a specific range of time**) |
| **Normal**    | Continuous | $\mu$ (Mean), $\sigma$ (Std Dev) | Natural measurements and errors (e.g.,  **Time**, Human **height/weight**, Sensor noise) | Symmetrical "Bell Curve" shape.                                                                  |

> **Note**: While we focused on the first three in detail, the **Binomial** distribution is the natural "next step" after Bernoulli, representing the total count of successes over multiple trials.

---

# formula quick reference table

| Distribution  | Mean ($E[X]$) | Variance ($Var(X)$) | Standard Deviation ($SD$) | PMF / PDF Formula                                                                  |
| :------------ | :------------ | :------------------ | :------------------------ | :--------------------------------------------------------------------------------- |
| **Bernoulli** | $p$           | $p(1 - p)$          | $\sqrt{p(1 - p)}$         | $p^x(1-p)^{1-x}$                                                                   |
| **Binomial**  | $np$          | $np(1 - p)$         | $\sqrt{np(1 - p)}$        | $\binom{n}{x} p^x (1-p)^{n-x}$                                                     |
| **Poisson**   | $\lambda$     | $\lambda$           | $\sqrt{\lambda}$          | $\frac{\lambda^x e^{-\lambda}}{x!}$                                                |
| **Normal**    | $\mu$         | $\sigma^2$          | $\sigma$                  | $\frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$ |

**Quick Note on the Formulas:**
* **$n$**: The total number of identical trials.
* **$p$**: The probability of success on any single given trial.
* **$x$**: Represents the specific outcome or value you are calculating the probability for.
* **$\binom{n}{x}$**: Read as "n choose x", this represents the combinations formula. It calculates the total number of distinct ways to get exactly $x$ successes out of $n$ trials.
* **$e$**: Euler's number (approximately $2.71828$).
* **$\pi$**: Pi (approximately $3.14159$).
* **$x!$**: Factorial of $x$ (e.g., $3! = 3 \times 2 \times 1$).
