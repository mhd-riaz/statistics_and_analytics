# Z-Score in Normal Distribution

## Definition
A Z-score (also known as a standard score) is a statistical measurement that describes a value's relationship to the mean (average) of a group of values. It is measured in terms of standard deviations from the mean. If a Z-score is 0, it indicates that the data point's score is identical to the mean score. A Z-score of 1.0 indicates a value that is one standard deviation from the mean. Z-scores can be positive or negative, with a positive value indicating the score is above the mean and a negative score indicating it is below the mean. 

Essentially, calculating a Z-score allows you to take any normal distribution and standardize it into a "Standard Normal Distribution," which always has a mean of 0 and a standard deviation of 1. 



## Formula
For a population:
$$Z = \frac{x - \mu}{\sigma}$$

For a sample:
$$Z = \frac{x - \bar{x}}{s}$$

**Explanation of formula**:
- $Z$: The standard score (Z-score) you are calculating, representing the number of standard deviations away from the mean.
- $x$: The specific individual data point or raw score you are evaluating.
- $\mu$: The population mean (the average of all data points in the population).
- $\sigma$: The population standard deviation (how spread out the population data is).
- $\bar{x}$: The sample mean (the average of the data points in a subset of the population).
- $s$: The sample standard deviation.

**Key concepts**:
- **Standardization**: The process of shifting and scaling your dataset so that it has a mean of 0 and a standard deviation of 1. This is what the Z-score formula does.
- **Comparability**: Z-scores allow you to compare scores from entirely different distributions. You can compare apples to oranges if both are converted to Z-scores.
- **The Empirical Rule (68-95-99.7 Rule)**: In a normal distribution, roughly 68% of the data falls between a Z-score of -1 and 1. About 95% falls between -2 and 2, and 99.7% falls between -3 and 3.
- **Outliers**: A data point with a Z-score less than -3 or greater than +3 is generally considered highly unusual or an outlier.

## Example 1
**Problem**: You are measuring the length of Cardinal Tetra fish in a 150-liter freshwater aquarium. Let's assume the lengths of adult Cardinal Tetras are normally distributed with a mean length of 3.5 cm and a standard deviation of 0.4 cm. You find a particularly large fish that measures 4.3 cm. What is the Z-score of this fish's length?

**Step-by-step Solution**:
1. **Identify the given variables**:
   - The specific data point ($x$) = 4.3 cm
   - The mean ($\mu$) = 3.5 cm
   - The standard deviation ($\sigma$) = 0.4 cm
2. **Apply the Z-score formula**:
   $$Z = \frac{x - \mu}{\sigma}$$
3. **Substitute the values into the formula**:
   $$Z = \frac{4.3 - 3.5}{0.4}$$
4. **Calculate the numerator (the difference from the mean)**:
   $$4.3 - 3.5 = 0.8$$
5. **Divide by the standard deviation**:
   $$Z = \frac{0.8}{0.4} = 2.0$$
**Conclusion**: The Z-score is 2.0. This means this specific Cardinal Tetra is exactly 2 standard deviations larger than the average Cardinal Tetra in the tank.

## Example 2
**Problem**: Students taking an M.Tech in Data Science entrance exam receive normally distributed scores. The average score on the exam is 72, with a standard deviation of 8. A student scores an 86 on the exam. What is their Z-score, and how did they perform relative to the class?

**Step-by-step Solution**:
1. **Identify the given variables**:
   - The student's score ($x$) = 86
   - The mean score ($\mu$) = 72
   - The standard deviation ($\sigma$) = 8
2. **Apply the Z-score formula**:
   $$Z = \frac{x - \mu}{\sigma}$$
3. **Substitute the values into the formula**:
   $$Z = \frac{86 - 72}{8}$$
4. **Calculate the numerator**:
   $$86 - 72 = 14$$
5. **Divide by the standard deviation**:
   $$Z = \frac{14}{8} = 1.75$$
**Conclusion**: The student's Z-score is 1.75. Because the Z-score is positive, they scored above the average. Specifically, their score is 1.75 standard deviations above the mean exam score, placing them well into the upper percentiles of the testing group.

## Example 3
**Problem**: Let's look at compensation in the tech industry. Suppose the annual salaries for full-stack developers with 4 years of experience in a specific region are normally distributed. The mean salary is 10.5 LPA (Lakhs Per Annum), and the standard deviation is 1.5 LPA. An engineer working in an IT company earns a salary of 12.9 LPA. What is the Z-score of this salary?

**Step-by-step Solution**:
1. **Identify the given variables**:
   - The specific salary ($x$) = 12.9 LPA
   - The mean salary ($\mu$) = 10.5 LPA
   - The standard deviation ($\sigma$) = 1.5 LPA
2. **Apply the Z-score formula**:
   $$Z = \frac{x - \mu}{\sigma}$$
3. **Substitute the values into the formula**:
   $$Z = \frac{12.9 - 10.5}{1.5}$$
4. **Calculate the numerator**:
   $$12.9 - 10.5 = 2.4$$
5. **Divide by the standard deviation**:
   $$Z = \frac{2.4}{1.5} = 1.6$$
**Conclusion**: The Z-score is 1.6. This means a salary of 12.9 LPA is 1.6 standard deviations above the average salary for that experience bracket, indicating a highly competitive compensation package.


---


# Cumulative Distribution Function (CDF)

## Definition
The Cumulative Distribution Function (CDF) is a fundamental concept in statistics that tells you the probability that a random variable $X$ will take on a value less than or equal to a specific value $x$. 

While a Probability Density Function (PDF) or Probability Mass Function (PMF) tells you the probability of landing *exactly* on a specific point, the CDF tells you the *total accumulated probability* up to that point. Because it accumulates probabilities, the CDF always starts at 0 and grows to 1 (or 100%) as you move from left to right across your possible values.



## Formula
The formula depends on whether your data is discrete (countable items, like whole numbers) or continuous (measurable items, like time or distance).

**For a discrete random variable:**
$$F(x) = P(X \le x) = \sum_{x_i \le x} P(X = x_i)$$

**For a continuous random variable:**
$$F(x) = P(X \le x) = \int_{-\infty}^{x} f(t) dt$$

**Explanation of formula**:
- $F(x)$: The Cumulative Distribution Function evaluated at the value $x$.
- $P(X \le x)$: The probability that the random variable $X$ is less than or equal to $x$.
- $\sum$: The summation symbol. For discrete data, you literally add up the probabilities of every outcome up to and including $x$.
- $x_i$: The individual discrete outcomes in your dataset.
- $\int$: The integral symbol. For continuous data, this represents calculating the area under the probability density curve from the lowest possible value up to $x$.
- $f(t)$: The Probability Density Function (PDF) for the continuous variable.
- $dt$: Represents a tiny slice of the variable $t$ (a dummy variable used for integration) over which you are accumulating the area.

**Key concepts**:
- **Monotonically Non-Decreasing**: A CDF can stay flat or go up, but it can *never* go down. As you move to larger values of $x$, you are only adding more probability.
- **Bounds**: The lowest possible value of a CDF is always 0 (0% chance), and the highest possible value is always 1 (100% chance). Mathematically, $\lim_{x \to -\infty} F(x) = 0$ and $\lim_{x \to \infty} F(x) = 1$.
- **Finding Ranges**: You can use the CDF to find the probability that a value falls within a specific range $(a, b]$. You do this by subtracting the CDF at the lower bound from the CDF at the upper bound: $P(a < X \le b) = F(b) - F(a)$.

---

## Example 1 (Grade 10 Level)
**Problem**: Let's look at the Assassin snails in a 150-liter freshwater aquarium. Suppose we observe the number of eggs a snail lays in a single week. The probability of laying 0, 1, 2, or 3 eggs is given by the following Probability Mass Function:
- $P(X=0) = 0.1$ (10% chance)
- $P(X=1) = 0.3$ (30% chance)
- $P(X=2) = 0.4$ (40% chance)
- $P(X=3) = 0.2$ (20% chance)

Calculate the Cumulative Distribution Function for $x = 2$, denoted as $F(2)$. What does it mean?

**Step-by-step Solution**:
1.  **Identify the goal**: We need to find $F(2)$, which is the same as $P(X \le 2)$. This means the probability that the snail lays 2 eggs *or fewer*.
2.  **Apply the discrete CDF formula**: We must sum all probabilities where the outcome $x_i$ is less than or equal to 2.
    $$F(2) = \sum_{x_i \le 2} P(X = x_i)$$
3.  **Expand the summation**: The outcomes less than or equal to 2 are 0, 1, and 2.
    $$F(2) = P(X=0) + P(X=1) + P(X=2)$$
4.  **Substitute the given probabilities**:
    $$F(2) = 0.1 + 0.3 + 0.4$$
5.  **Calculate the final sum**:
    $$F(2) = 0.8$$

**Conclusion**: $F(2) = 0.8$. There is an 80% cumulative probability that the Assassin snail will lay 2 or fewer eggs in a week.

---

## Example 2 (College Level)
**Problem**: Students in an M.Tech in Data Science program are assigned a complex data processing task in Python. The time ($X$, in hours) it takes for their Python scripts to run on a standard machine follows a continuous Uniform Distribution between 1 hour and 5 hours. 

For a continuous uniform distribution ranging from $a$ to $b$, the CDF formula is given by:
$$F(x) = \frac{x - a}{b - a}$$ for $a \le x \le b$.

Calculate the probability that a randomly selected student's Python script finishes running in 3.5 hours or less.

**Step-by-step Solution**:
1.  **Identify the given variables**:
    - Lower bound of time ($a$) = 1 hour
    - Upper bound of time ($b$) = 5 hours
    - The target time we are evaluating ($x$) = 3.5 hours
2.  **Define what we are solving for**: We want the probability that the time $X$ is less than or equal to 3.5. This is precisely the definition of the CDF evaluated at 3.5: $F(3.5)$.
3.  **Apply the specific uniform CDF formula**:
    $$F(x) = \frac{x - a}{b - a}$$
4.  **Substitute the values into the formula**:
    $$F(3.5) = \frac{3.5 - 1}{5 - 1}$$
5.  **Calculate the numerator and denominator**:
    - Numerator: $3.5 - 1 = 2.5$
    - Denominator: $5 - 1 = 4$
6.  **Divide to find the probability**:
    $$F(3.5) = \frac{2.5}{4} = 0.625$$

**Conclusion**: $F(3.5) = 0.625$. There is a 62.5% chance that the Python script will finish executing in 3.5 hours or less.

---

## Example 3 (Real World Level)
**Problem**: You are evaluating real estate opportunities and looking at 5 available plots of land in the Aikyas Brahmi layout near Mysuru. The asking prices for these 5 specific plots (in Lakhs) are: 24, 28, 30, 30, and 35. 

If you randomly select one of these available plots to view, what is the Cumulative Distribution Function evaluated at $x = 30$ Lakhs?

**Step-by-step Solution**:
1.  **Organize the data**: The dataset of prices (in Lakhs) is $[24, 28, 30, 30, 35]$. The total number of plots ($N$) is 5.
2.  **Identify the goal**: We want to find $F(30)$, which is the empirical probability that a randomly chosen plot costs 30 Lakhs *or less*.
3.  **Count the occurrences**: How many plots have a price $x_i \le 30$?
    - 24 is $\le 30$ (Count = 1)
    - 28 is $\le 30$ (Count = 2)
    - 30 is $\le 30$ (Count = 3)
    - 30 is $\le 30$ (Count = 4)
    - 35 is NOT $\le 30$
    There are exactly 4 plots that cost 30 Lakhs or less.
4.  **Calculate the empirical cumulative probability**: Divide the number of successful outcomes by the total number of outcomes.
    $$F(30) = \frac{\text{Number of plots } \le 30}{\text{Total number of plots}}$$
5.  **Substitute and solve**:
    $$F(30) = \frac{4}{5} = 0.80$$

**Conclusion**: $F(30) = 0.80$. If you pick a plot at random from this specific layout dataset, there is an 80% probability that the asking price will be 30 Lakhs or less.