<p align="left">
  <a href="./statistics-basics.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./probability-fundamentals.md"><b>Next →</b></a>
  </span>
</p>

---

# Descriptive Statistics

```
Descriptive Statistics
├── Measures of Central Tendency
│   ├── Mean (Average)
│   ├── Median
│   ├── Mode
│   └── Skewness and Shape
│
├── Measures of Dispersion
│   ├── Range
│   ├── Quantiles (Quartiles & Percentiles)
│   ├── Interquartile Range (IQR)
│   ├── 5-Number Summary & Box Plot
│   ├── Variance (Population σ² vs Sample s²)
│   └── Standard Deviation
│
├── Relative Variability and Distribution Rules
│   ├── Coefficient of Variation (CV)
│   ├── Variance vs CV Comparison
│   ├── Empirical Rule (68-95-99.7)
│   └── Chebyshev's Theorem
│
└── Measures of Relationship
    ├── Covariance & Covariance Matrix
    ├── Correlation & Correlation Matrix
    ├── Pearson Correlation Coefficient
    └── Analysis Types (Univariate, Bivariate, Multivariate)
```

---

## Descriptive Statistics

### 1. Measures of Central Tendency

Measures of central tendency describe the **center** of a dataset — a single value that attempts to represent the "typical" value. The three most common measures are the **mean**, **median**, and **mode**. They answer different questions: the mean uses every value, the median identifies the middle, and the mode highlights the most frequent value.

Each measure uses a different symbol depending on whether the data represents a **population** or a **sample**:

| Measure            | Population Symbol |    Sample Symbol    |
| :----------------- | :---------------: | :-----------------: |
| Mean               |   $\mu$ ("mu")    | $\bar{x}$ ("x bar") |
| Proportion         |        $p$        | $\hat{p}$ ("p hat") |
| Variance           |    $\sigma^2$     |        $s^2$        |
| Standard Deviation |     $\sigma$      |         $s$         |

```
Sorted data:   2   4   [4]   6   9
                │   │    │    │   │
Mean   → (2+4+4+6+9) / 5 = 5.0
Median → middle value      = [4]
Mode   → most frequent     = 4 (appears twice)
```

#### Mean (Average)

The **mean** is the sum of all values divided by the total number of values. It is the most commonly used measure of center and incorporates every data point in the calculation.

```
Values:   3    7    5    9    6
          │    │    │    │    │
          └──┬─┴──┬─┴──┬─┘
             ▼    ▼    ▼
        Sum = 3 + 7 + 5 + 9 + 6 = 30
        n   = 5
             ┌─────────┐
        x̄  = │ 30 / 5  │ = 6
             └─────────┘
```

- For a **population**: $\mu = \frac{\sum_{i=1}^{N} x_i}{N}$
- For a **sample**: $\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$

**Key property**: The mean is sensitive to **outliers** — a single extreme value can significantly shift the mean away from the typical center. For example, adding a value of 1000 to the dataset $\{3, 7, 5, 9, 6\}$ would change the mean from 6 to 171.7.

#### Median

The **median** is the middle value when data is sorted in ascending (or descending) order. It divides the dataset into two equal halves. Because the median only depends on position, it is **robust to outliers** and preferred for skewed distributions.

```
Odd count (n=5):   Sorted:   2   4   [5]   7   9
                                      ↑
                             Median = 5 (position 3)

Even count (n=6):  Sorted:   2   4   [5   6]   8   10
                                      ↑   ↑
                         Median = (5+6)/2 = 5.5
```

- If $n$ is **odd**, the median is the value at position $\frac{n+1}{2}$
- If $n$ is **even**, the median is the average of values at positions $\frac{n}{2}$ and $\frac{n}{2} + 1$

#### Mode

The **mode** is the value that appears most frequently in a dataset. Unlike mean and median, the mode can be used with **categorical (qualitative)** data as well.

```
Unimodal:     1  2  [3  3  3]  4  5       → Mode = 3

Bimodal:      1  [2  2]  3  [5  5]  6     → Mode = 2 and 5

No Mode:      1  2  3  4  5               → No mode (all unique)
```

- **Unimodal**: One mode (single most frequent value)
- **Bimodal**: Two modes (two values share the highest frequency)
- **Multimodal**: More than two modes
- **No mode**: All values appear with equal frequency

#### Skewness and Shape

The relationship between mean, median, and mode reveals the **shape** of the distribution:

```
Left (Negative) Skew         Symmetric            Right (Positive) Skew

        ▄▄                     ▄▄▄▄                            ▄▄
      ▄▄██▄▄                 ▄▄████▄▄                       ▄▄██▄▄
    ▄▄██████▄▄            ▄▄████████▄▄                   ▄▄██████▄▄
◄────┼────┼──────►   ◄──────┼──────────►   ◄──────┼────┼──────────►
   Mean  Median         Mean=Med=Mode           Median  Mean

Mean < Median           Mean ≈ Med ≈ Mode        Mean > Median
```

| Condition                                               | Shape              | Skew Direction            |
| :------------------------------------------------------ | :----------------- | :------------------------ |
| $\text{Mean} \approx \text{Median} \approx \text{Mode}$ | Symmetric          | No skew                   |
| $\text{Mean} > \text{Median}$                           | Tail extends right | Right / Positively skewed |
| $\text{Mean} < \text{Median}$                           | Tail extends left  | Left / Negatively skewed  |

#### Real-World Use Cases

- **Finance**: Mean monthly revenue gives an overall average; median income is preferred for skewed salary distributions where CEO pay inflates the mean.
- **Education**: Median test score describes the middle performer in a class, unaffected by a few very high or very low scores.
- **Retail**: Mode identifies the most commonly purchased product size or category — useful for inventory decisions.
- **Healthcare**: Mean blood pressure in a clinical trial gives an aggregate picture; median is used when a few extreme readings would distort the average.
- **Limitation**: The mean is sensitive to outliers. The mode may not exist (all unique values) or may not be unique (multimodal). The median ignores the actual magnitudes of values.

#### Steps

1. Sort the dataset in ascending order.
2. Compute the **mean**: divide the sum of all values by the count $n$.
3. Find the **median**: if $n$ is odd, take the middle value; if $n$ is even, average the two middle values.
4. Find the **mode**: identify the value(s) with the highest frequency.
5. Compare mean and median to determine **skewness**: if mean > median → right-skewed; if mean < median → left-skewed; if approximately equal → symmetric.

#### Formula

$$
\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
$$

$$
\text{Median} =
\begin{cases}
x_{\frac{n+1}{2}}, & n \text{ odd} \\[6pt]
\frac{x_{\frac{n}{2}} + x_{\frac{n}{2}+1}}{2}, & n \text{ even}
\end{cases}
$$

$$
\text{Mode} = \text{value(s) with highest frequency}
$$

Where:
|                 Symbol                 | Pronunciation          | Meaning                                        |
| :------------------------------------: | :--------------------- | :--------------------------------------------- |
|               $\bar{x}$                | "x bar"                | The sample mean (average) of the dataset       |
|                 $\mu$                  | "mu"                   | The population mean                            |
|                 $x_i$                  | "x sub i"              | The $i$-th individual value in the dataset     |
|                  $n$                   | "n"                    | Total number of observations in the sample     |
|                  $N$                   | "capital N"            | Total number of observations in the population |
|          $x_{\frac{n+1}{2}}$           | "x at n plus 1 over 2" | The middle value when $n$ is odd               |
| $x_{\frac{n}{2}}$, $x_{\frac{n}{2}+1}$ | "x at n over 2"        | The two middle values when $n$ is even         |

#### Examples

**Example 1:** Find mean, median, mode, and skewness for an odd-count dataset with an outlier

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Dataset $= \{12, 15, 15, 18, 40\}$ | Five observed values (sorted) |
> | $n = 5$ | Number of values (odd) |
> | Find: $\bar{x}$, Median, Mode, skewness | All central tendency measures + shape |
>
> **Step 1:** Compute the mean.
>
> $$\bar{x} = \frac{12 + 15 + 15 + 18 + 40}{5} = \frac{100}{5} = 20$$
>
> **Step 2:** Find the median.
>
> $n = 5$ (odd), so the median is at position $\frac{5+1}{2} = 3$.
>
> $$\text{Median} = x_3 = 15$$
>
> **Step 3:** Find the mode.
>
> The value 15 appears twice (more than any other value).
>
> $$\text{Mode} = 15$$
>
> **Step 4:** Determine skewness.
>
> $\bar{x} = 20 > \text{Median} = 15$, so the distribution is **right-skewed** (the outlier 40 pulls the mean to the right).
>
> **Step 5:** State the results.
>
> $$\boxed{\bar{x} = 20,\ \text{Median} = 15,\ \text{Mode} = 15,\ \text{Right-skewed}}$$

**Example 2:** Find mean, median, mode, and skewness for an even-count bimodal dataset

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Dataset $= \{2, 4, 4, 6, 6, 8\}$ | Six observed values (sorted) |
> | $n = 6$ | Number of values (even) |
> | Find: $\bar{x}$, Median, Mode, skewness | All central tendency measures + shape |
>
> **Step 1:** Compute the mean.
>
> $$\bar{x} = \frac{2 + 4 + 4 + 6 + 6 + 8}{6} = \frac{30}{6} = 5$$
>
> **Step 2:** Find the median.
>
> $n = 6$ (even), so the median is the average of positions $\frac{6}{2} = 3$ and $\frac{6}{2}+1 = 4$.
>
> $$\text{Median} = \frac{x_3 + x_4}{2} = \frac{4 + 6}{2} = 5$$
>
> **Step 3:** Find the mode.
>
> Both 4 and 6 appear twice — the dataset is **bimodal**.
>
> $$\text{Mode} = 4 \text{ and } 6$$
>
> **Step 4:** Determine skewness.
>
> $\bar{x} = 5 = \text{Median} = 5$, so the distribution is approximately **symmetric**.
>
> **Step 5:** State the results.
>
> $$\boxed{\bar{x} = 5,\ \text{Median} = 5,\ \text{Mode} = 4 \text{ and } 6,\ \text{Symmetric}}$$

---

### 2. Measures of Dispersion

Measures of dispersion show **how spread out** the data is. Two datasets can have the same mean but very different variability. Important measures include the **range**, **quantiles**, **interquartile range (IQR)**, **5-number summary**, **variance**, and **standard deviation**.

```
Low spread:        ● ● ● ●
◄────────────────────┼────────────────────►
                     x̄

High spread:   ●       ●           ●   ●
◄────────────────────┼────────────────────►
                     x̄

Zero variance:       ● ● ● ● (all identical)
◄────────────────────┼────────────────────►
                     x̄
```

#### Range

The **range** is the simplest measure of dispersion — the difference between the largest and smallest values. It uses only two data points and is highly sensitive to outliers.

$$
\text{Range} = x_{\max} - x_{\min}
$$

#### Quantiles (Quartiles & Percentiles)

**Quantiles** split sorted data into equal-sized groups. The most common are:

- **Quartiles** split data into **4 equal parts** ($Q_1, Q_2, Q_3$):

```
┌─────────┬─────────┬─────────┬─────────┐
│   25%   │   25%   │   25%   │   25%   │
└─────────┴─────────┴─────────┴─────────┘
Min      Q1        Q2        Q3        Max
                (Median)
```

- **Percentiles** split data into **100 equal parts** (e.g., the 90th percentile means 90% of data is at or below that value)

| Quartile | Equivalent Percentile | Meaning                           |
| :------: | :-------------------: | :-------------------------------- |
|  $Q_1$   |    25th percentile    | 25% of data is below this value   |
|  $Q_2$   |    50th percentile    | The median — 50% of data is below |
|  $Q_3$   |    75th percentile    | 75% of data is below this value   |

#### Interquartile Range (IQR)

The **IQR** is the range of the middle 50% of data — the distance between the first and third quartiles. It is **robust to outliers** because it ignores the extremes.

$$
\text{IQR} = Q_3 - Q_1
$$

#### 5-Number Summary & Box Plot

The **5-number summary** provides a complete picture of the data spread using five key values:

1. **Minimum** ($x_{\min}$)
2. **First Quartile** ($Q_1$)
3. **Median** ($Q_2$)
4. **Third Quartile** ($Q_3$)
5. **Maximum** ($x_{\max}$)

The **box plot** (or _box-and-whisker plot_) is a visual representation of the 5-number summary that also identifies **outliers** using the 1.5×IQR rule:

```
Outliers   Lower    Q1    Q2    Q3    Upper   Outliers
   ●       Bound     │     │     │    Bound      ●
◄──┼─────────┼───────┼─────┼─────┼───────┼──────┼──►
             │       ├─── IQR ───┤       │
        Q1-1.5×IQR                  Q3+1.5×IQR
```

- **Lower Bound** = $Q_1 - 1.5 \times \text{IQR}$
- **Upper Bound** = $Q_3 + 1.5 \times \text{IQR}$
- Any value below the lower bound or above the upper bound is considered an **outlier**

#### Variance (Population vs Sample)

**Variance** measures the average of the squared deviations from the mean. The key difference between population and sample variance is the **denominator**:

| Aspect      |         Population Variance         |            Sample Variance             |
| :---------- | :---------------------------------: | :------------------------------------: |
| Symbol      |             $\sigma^2$              |                 $s^2$                  |
| Denominator |       $N$ (total population)        |     $n - 1$ (Bessel's correction)      |
| Formula     |   $\frac{\sum (x_i - \mu)^2}{N}$    | $\frac{\sum (x_i - \bar{x})^2}{n - 1}$ |
| Use case    | When you have the entire population |       When working with a sample       |

The sample variance divides by $n - 1$ instead of $n$ to correct for the bias in estimating the population variance from a sample (_Bessel's correction_).

#### Standard Deviation

The **standard deviation** is the square root of the variance. It returns the measure of spread to the **same units** as the original data, making it more interpretable than variance.

- Population: $\sigma = \sqrt{\sigma^2}$
- Sample: $s = \sqrt{s^2}$

#### Real-World Use Cases

- **Manufacturing**: Standard deviation shows how tightly product dimensions stay around the target specification.
- **Healthcare**: IQR is useful when a few extreme patient values (outliers) would distort the range.
- **Finance**: Variance and standard deviation summarize volatility in stock returns.
- **Education**: The 5-number summary and box plot quickly reveal the distribution shape and outliers in a class's test scores.
- **Limitation**: The range is highly sensitive to outliers. Variance uses squared units, making it harder to interpret than standard deviation.

#### Steps

1. Sort the data in ascending order.
2. Find the **minimum** and **maximum** to compute the range.
3. Find $Q_1$, $Q_2$ (median), and $Q_3$ to build the quartile structure.
4. Compute $\text{IQR} = Q_3 - Q_1$.
5. Determine outlier bounds: $Q_1 - 1.5 \times \text{IQR}$ and $Q_3 + 1.5 \times \text{IQR}$.
6. Compute the mean.
7. Find deviations from the mean, square them, divide by $N$ (population) or $n - 1$ (sample) to get variance.
8. Take the square root of variance to get standard deviation.

#### Formula

$$
\text{Range} = x_{\max} - x_{\min}
$$

$$
\text{IQR} = Q_3 - Q_1
$$

$$
\sigma^2 = \frac{\sum_{i=1}^{N}(x_i - \mu)^2}{N} \qquad \text{(population)}
$$

$$
s^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1} \qquad \text{(sample)}
$$

$$
\sigma = \sqrt{\sigma^2} \qquad s = \sqrt{s^2}
$$

Where:
|    Symbol    | Pronunciation   | Meaning                                    |
| :----------: | :-------------- | :----------------------------------------- |
|  $x_{\max}$  | "x max"         | Largest observed value                     |
|  $x_{\min}$  | "x min"         | Smallest observed value                    |
|    $Q_1$     | "Q one"         | First quartile (25th percentile)           |
|    $Q_2$     | "Q two"         | Second quartile (median / 50th percentile) |
|    $Q_3$     | "Q three"       | Third quartile (75th percentile)           |
| $\text{IQR}$ | "I Q R"         | Interquartile range (middle 50% spread)    |
|  $\sigma^2$  | "sigma squared" | Population variance                        |
|    $s^2$     | "s squared"     | Sample variance                            |
|   $\sigma$   | "sigma"         | Population standard deviation              |
|     $s$      | "s"             | Sample standard deviation                  |
|    $\mu$     | "mu"            | Population mean                            |
|  $\bar{x}$   | "x bar"         | Sample mean                                |
|     $N$      | "capital N"     | Population size                            |
|     $n$      | "n"             | Sample size                                |

#### Examples

**Example 1:** Complete dispersion analysis — Range, Quartiles, IQR, 5-Number Summary, and Outlier Detection

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Dataset $= \{2, 4, 5, 7, 8, 10, 12\}$ | Sorted data |
> | $n = 7$ | Number of values |
> | Find: Range, $Q_1$, $Q_2$, $Q_3$, IQR, outlier bounds | Full dispersion summary |
>
> **Step 1:** Compute the range.
>
> $$\text{Range} = 12 - 2 = 10$$
>
> **Step 2:** Find the median ($Q_2$).
>
> With $n = 7$ (odd), the middle value is at position 4.
>
> $$Q_2 = 7$$
>
> **Step 3:** Find $Q_1$ and $Q_3$.
>
> Lower half (below median): $\{2, 4, 5\}$ → $Q_1 = 4$ (middle of lower half)
>
> Upper half (above median): $\{8, 10, 12\}$ → $Q_3 = 10$ (middle of upper half)
>
> **Step 4:** Compute the IQR.
>
> $$\text{IQR} = Q_3 - Q_1 = 10 - 4 = 6$$
>
> **Step 5:** Determine outlier bounds.
>
> $$\text{Lower Bound} = Q_1 - 1.5 \times \text{IQR} = 4 - 9 = -5$$
>
> $$\text{Upper Bound} = Q_3 + 1.5 \times \text{IQR} = 10 + 9 = 19$$
>
> All values fall within $[-5, 19]$, so there are **no outliers**.
>
> **5-Number Summary:**
>
> | Min | $Q_1$ | Median ($Q_2$) | $Q_3$ | Max |
> |:---:|:---:|:---:|:---:|:---:|
> | 2 | 4 | 7 | 10 | 12 |
>
> $$\boxed{\text{Range} = 10,\ Q_1 = 4,\ Q_2 = 7,\ Q_3 = 10,\ \text{IQR} = 6,\ \text{No outliers}}$$

**Example 2:** Population variance vs Sample variance

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Dataset $= \{4, 6, 8\}$ | Three observations |
> | Compute both $\sigma^2$ and $s^2$ | Population and sample variance |
>
> **Step 1:** Compute the mean.
>
> $$\mu = \bar{x} = \frac{4 + 6 + 8}{3} = 6$$
>
> **Step 2:** Compute squared deviations.
>
> | $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
> |:---:|:---:|:---:|
> | 4 | $-2$ | 4 |
> | 6 | 0 | 0 |
> | 8 | 2 | 4 |
>
> $$\sum (x_i - \bar{x})^2 = 8$$
>
> **Step 3:** Compute population variance (divide by $N$).
>
> $$\sigma^2 = \frac{8}{3} \approx 2.67$$
>
> **Step 4:** Compute sample variance (divide by $n - 1$).
>
> $$s^2 = \frac{8}{3 - 1} = \frac{8}{2} = 4$$
>
> **Step 5:** Compute standard deviations.
>
> $$\sigma = \sqrt{2.67} \approx 1.63 \qquad s = \sqrt{4} = 2$$
>
> $$\boxed{\sigma^2 \approx 2.67,\ s^2 = 4,\ \sigma \approx 1.63,\ s = 2}$$

---

### 3. Relative Variability and Distribution Rules

Sometimes absolute spread is not enough. The **coefficient of variation (CV)** compares spread relative to the size of the mean. Distribution rules such as the **Empirical Rule** and **Chebyshev's Theorem** help interpret how much data lies within a certain number of standard deviations.

#### Coefficient of Variation (CV)

The **CV** expresses the standard deviation as a percentage of the mean. This makes it useful for comparing variability across datasets with different units or magnitudes.

$$
CV = \frac{s}{\bar{x}} \times 100\%
$$

#### Variance vs CV Comparison

| Aspect                | Variance ($s^2$ / $\sigma^2$)            | Coefficient of Variation (CV)                                   |
| :-------------------- | :--------------------------------------- | :-------------------------------------------------------------- |
| **What it measures**  | Average squared deviation from the mean  | Relative variability as a percentage of the mean                |
| **Units**             | Squared units of the original data       | Unitless (percentage)                                           |
| **Formula**           | $\frac{\sum(x_i - \bar{x})^2}{n-1}$      | $\frac{s}{\bar{x}} \times 100\%$                                |
| **Use case**          | Comparing spread within the same dataset | Comparing spread across datasets with different units or scales |
| **Example**           | Variance of test scores $= 25$ marks²    | CV of test scores $= 10\%$                                      |
| **Depends on scale?** | Yes — larger values → larger variance    | No — normalized by the mean                                     |

#### Empirical Rule (68-95-99.7)

For data that follows a **normal distribution** (_bell curve_), the Empirical Rule states:

```
             ┌──────── 99.7% ──────┐
             │  ┌───── 95% ─────┐  │
             │  │  ┌── 68% ──┐  │  │
             │  │  │    ██    │  │  │
             │  │  │   ████   │  │  │
             │  │  │  ██████  │  │  │
             │  │  │ ████████ │  │  │
◄────────────┼──┼──┼────┼────┼──┼──┼────────────►
           -3σ -2σ -1σ  μ  +1σ +2σ +3σ
```

- **68%** of data falls within $\mu \pm 1\sigma$
- **95%** of data falls within $\mu \pm 2\sigma$
- **99.7%** of data falls within $\mu \pm 3\sigma$

#### Chebyshev's Theorem

For **any distribution** (regardless of shape), Chebyshev's Theorem guarantees:

$$
\text{At least } 1 - \frac{1}{k^2} \text{ of data falls within } k \text{ standard deviations of the mean}
$$

|  $k$  | Minimum proportion                        |
| :---: | :---------------------------------------- |
|   2   | At least $1 - \frac{1}{4} = 75\%$         |
|   3   | At least $1 - \frac{1}{9} \approx 88.9\%$ |
|   4   | At least $1 - \frac{1}{16} = 93.75\%$     |

This is weaker than the Empirical Rule but applies universally — no normality assumption required.

#### Real-World Use Cases

- **Quality Comparison**: CV helps compare the stability of processes measured in different units (e.g., temperature in °C vs pressure in PSI).
- **Exam Analysis**: The Empirical Rule estimates how many students fall near the mean in a normally distributed set of scores.
- **Risk Assessment**: Chebyshev's Theorem gives a guaranteed lower bound for any distribution — useful when normality cannot be assumed.
- **Limitation**: The Empirical Rule applies **only** to approximately normal (bell-shaped) data. Chebyshev gives conservative (weaker) bounds.

#### Steps

1. Compute the mean ($\bar{x}$) and standard deviation ($s$).
2. Compute $CV = \frac{s}{\bar{x}} \times 100\%$ when comparing relative spread.
3. For normal data, use the **Empirical Rule** (68-95-99.7).
4. For any distribution, use **Chebyshev's Theorem**: at least $1 - \frac{1}{k^2}$ within $k$ standard deviations.

#### Formula

$$
CV = \frac{s}{\bar{x}} \times 100\%
$$

$$
\text{Chebyshev: at least } 1 - \frac{1}{k^2} \text{ within } k \text{ standard deviations}
$$

Where:
|  Symbol   | Pronunciation | Meaning                                     |
| :-------: | :------------ | :------------------------------------------ |
|   $CV$    | "C V"         | Coefficient of variation                    |
|    $s$    | "s"           | Sample standard deviation                   |
| $\bar{x}$ | "x bar"       | Sample mean                                 |
|    $k$    | "k"           | Number of standard deviations from the mean |
| $\sigma$  | "sigma"       | Population standard deviation               |
|   $\mu$   | "mu"          | Population mean                             |

#### Examples

**Example 1:** Compare relative spread using CV — Variance vs CV distinction

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Process A: mean $= 100$, SD $= 5$ | Manufacturing process A |
> | Process B: mean $= 20$, SD $= 4$ | Manufacturing process B |
> | Find: which process is more variable | Compare using both variance and CV |
>
> **Step 1:** Compare using variance (absolute spread).
>
> $$s_A^2 = 5^2 = 25, \qquad s_B^2 = 4^2 = 16$$
>
> By variance alone, Process A appears more variable ($25 > 16$).
>
> **Step 2:** Compute the CV for Process A (relative spread).
>
> $$CV_A = \frac{5}{100} \times 100\% = 5\%$$
>
> **Step 3:** Compute the CV for Process B.
>
> $$CV_B = \frac{4}{20} \times 100\% = 20\%$$
>
> **Step 4:** Compare and interpret.
>
> Process B has the larger CV ($20\% > 5\%$) — it is more variable **relative to its mean**, even though its absolute variance is smaller.
>
> **Step 5:** State the final answer.
>
> $$\boxed{\text{By variance: A is more spread. By CV: B is relatively more variable.}}$$

**Example 2:** Use the Empirical Rule and Chebyshev's Theorem

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Normal dataset with mean $\mu = 50$ | Center of the distribution |
> | Standard deviation $\sigma = 4$ | Spread of the distribution |
> | Find: proportion within $2\sigma$ and Chebyshev bound for $k=2$ | Interpret spread |
>
> **Step 1:** Apply the Empirical Rule (normal distribution assumed).
>
> For a normal distribution, about **95%** of values lie within $\mu \pm 2\sigma$.
>
> **Step 2:** Compute the interval.
>
> $$50 \pm 2(4) = 50 \pm 8$$
>
> So the interval is **42 to 58**.
>
> **Step 3:** Apply Chebyshev's Theorem with $k = 2$ (no normality required).
>
> $$1 - \frac{1}{2^2} = 1 - \frac{1}{4} = \frac{3}{4} = 75\%$$
>
> **Step 4:** Compare the two results.
>
> | Method | Assumption | Proportion within $\mu \pm 2\sigma$ |
> |:---|:---|:---|
> | Empirical Rule | Normal distribution | ~95% |
> | Chebyshev's Theorem | Any distribution | At least 75% |
>
> The Empirical Rule is stronger because it assumes normality; Chebyshev is weaker but universally applicable.
>
> **Step 5:** State the final answer.
>
> $$\boxed{\text{Empirical Rule: } \approx 95\% \text{ in } [42, 58],\ \text{Chebyshev: at least } 75\%}$$

---

### 4. Measures of Relationship

When two variables move together, descriptive statistics uses **covariance** and **correlation** to describe that relationship. Covariance shows direction, while correlation standardizes the result so it always stays between $-1$ and $+1$. The most common correlation measure is the **Pearson correlation coefficient** ($r$).

#### Covariance

**Covariance** measures how two variables change together. A positive covariance indicates they move in the same direction; negative means they move in opposite directions.

```
Positive covariance:     Negative covariance:     Zero covariance:
Y                        Y                         Y
│        ●               │  ●                      │  ●     ●
│      ●                 │    ●                    │    ●
│    ●                   │      ●                  │  ●   ●
│  ●                     │        ●                │    ●
└──────── X              └──────── X               └──────── X
As X ↑, Y ↑             As X ↑, Y ↓              No linear pattern
```

$$
\operatorname{cov}(X,Y) = \frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{n-1}
$$

**Key relationship**: The variance of a variable is the covariance of that variable with itself:

$$
\operatorname{var}(X) = \operatorname{cov}(X, X)
$$

#### Covariance Matrix

When working with multiple variables, covariances are organized into a **covariance matrix**:

$$
\Sigma = \begin{bmatrix}
\operatorname{cov}(X,X) & \operatorname{cov}(X,Y) \\
\operatorname{cov}(Y,X) & \operatorname{cov}(Y,Y)
\end{bmatrix}
= \begin{bmatrix}
\operatorname{var}(X) & \operatorname{cov}(X,Y) \\
\operatorname{cov}(Y,X) & \operatorname{var}(Y)
\end{bmatrix}
$$

The diagonal contains **variances**, and the off-diagonal elements are **covariances** between pairs of variables.

#### Correlation & Pearson Correlation Coefficient

The **Pearson correlation coefficient** ($r$) standardizes covariance by dividing by the product of the standard deviations, producing a value between $-1$ and $+1$:

$$
r = \frac{\operatorname{cov}(X,Y)}{s_X \cdot s_Y} = \frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i-\bar{x})^2 \cdot \sum_{i=1}^{n}(y_i-\bar{y})^2}}
$$

**Interpreting $r$:**

```
◄───────┬──────────┬───────────┬──────────┬───────►
-1     -0.8       -0.5         0        +0.5      +0.8     +1
│ Strong │ Moderate │   Weak    │   Weak   │ Moderate │ Strong │
│  Neg   │   Neg    │  Neg/Pos  │  Pos/Neg │   Pos    │  Pos   │
```

| $r$ value         | Interpretation                       |
| :---------------- | :----------------------------------- |
| $r = +1$          | Perfect positive linear relationship |
| $r > +0.8$        | Strong positive correlation          |
| $+0.5 < r < +0.8$ | Moderate positive correlation        |
| $0 < r < +0.5$    | Weak positive correlation            |
| $r = 0$           | No linear relationship               |
| $-0.5 < r < 0$    | Weak negative correlation            |
| $-0.8 < r < -0.5$ | Moderate negative correlation        |
| $r < -0.8$        | Strong negative correlation          |
| $r = -1$          | Perfect negative linear relationship |

#### Correlation Matrix

Like the covariance matrix, correlations between multiple variables are organized into a **correlation matrix**:

$$
R = \begin{bmatrix}
1 & r_{XY} \\
r_{YX} & 1
\end{bmatrix}
$$

The diagonal is always 1 (a variable perfectly correlates with itself), and $r_{XY} = r_{YX}$ (the matrix is symmetric).

#### Analysis Types

The number of variables involved determines the type of analysis:

| Type             | Variables | Example                                                      |
| :--------------- | :-------: | :----------------------------------------------------------- |
| **Univariate**   |     1     | Analyzing test scores of a class                             |
| **Bivariate**    |     2     | Studying the relationship between study hours and exam score |
| **Multivariate** |    3+     | Predicting house price from area, location, and age          |

For bivariate analysis:
- The **independent variable** (cause/predictor) goes on the **x-axis**
- The **dependent variable** (effect/outcome) goes on the **y-axis**

#### Real-World Use Cases

- **Finance**: Measure whether two assets tend to move together (positive correlation) or in opposite directions (negative) for portfolio diversification.
- **Engineering**: Check whether pressure rises as temperature rises in a process using the Pearson coefficient.
- **Analytics**: A correlation matrix gives a quick overview of linear associations across all variable pairs.
- **Healthcare**: Covariance matrices are used in multivariate analysis of patient data (e.g., blood pressure, cholesterol, weight).
- **Limitation**: Correlation does **not** prove causation. Correlation only captures **linear** relationships — two variables with a strong non-linear relationship may show $r \approx 0$.

#### Steps

1. Compute the mean of each variable ($\bar{x}$, $\bar{y}$).
2. Find paired deviations from the means for each observation.
3. Multiply paired deviations and sum them.
4. Divide by $n - 1$ to get **covariance**.
5. Divide covariance by the product of the two standard deviations to get the **Pearson correlation coefficient** ($r$).
6. Interpret $r$: direction (positive/negative) and strength (weak/moderate/strong).

#### Formula

$$
\operatorname{cov}(X,Y) = \frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{n-1}
$$

$$
r = \frac{\operatorname{cov}(X,Y)}{s_X \cdot s_Y} = \frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i-\bar{x})^2 \cdot \sum_{i=1}^{n}(y_i-\bar{y})^2}}
$$

Where:
|          Symbol           | Pronunciation           | Meaning                                                    |
| :-----------------------: | :---------------------- | :--------------------------------------------------------- |
| $\operatorname{cov}(X,Y)$ | "covariance of X and Y" | Average paired movement of two variables                   |
|            $r$            | "r"                     | Pearson correlation coefficient (ranges from $-1$ to $+1$) |
|        $x_i, y_i$         | "x sub i, y sub i"      | Paired observations of two variables                       |
|    $\bar{x}, \bar{y}$     | "x bar, y bar"          | Means of the two variables                                 |
|        $s_X, s_Y$         | "s sub X, s sub Y"      | Standard deviations of each variable                       |
|  $\operatorname{var}(X)$  | "variance of X"         | $= \operatorname{cov}(X, X)$                               |
|         $\Sigma$          | "sigma (capital)"       | Covariance matrix                                          |
|            $R$            | "R"                     | Correlation matrix                                         |

#### Examples

**Example 1:** Positive relationship — Covariance, Correlation, and Interpretation

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $X = \{1, 2, 3\}$ | Hours studied |
> | $Y = \{2, 4, 6\}$ | Exam score |
> | $n = 3$ | Number of paired observations |
> | Find: $\operatorname{cov}(X,Y)$, $r$, and interpretation | Relationship direction and strength |
>
> **Step 1:** Compute the means.
>
> $$\bar{x} = \frac{1+2+3}{3} = 2, \qquad \bar{y} = \frac{2+4+6}{3} = 4$$
>
> **Step 2:** Compute paired deviations and their products.
>
> | $x_i$ | $y_i$ | $x_i - \bar{x}$ | $y_i - \bar{y}$ | $(x_i - \bar{x})(y_i - \bar{y})$ |
> |:---:|:---:|:---:|:---:|:---:|
> | 1 | 2 | $-1$ | $-2$ | 2 |
> | 2 | 4 | 0 | 0 | 0 |
> | 3 | 6 | 1 | 2 | 2 |
>
> $$\sum (x_i-\bar{x})(y_i-\bar{y}) = 4$$
>
> **Step 3:** Compute covariance.
>
> $$\operatorname{cov}(X,Y) = \frac{4}{3-1} = 2$$
>
> **Step 4:** Compute standard deviations and correlation.
>
> $$s_X = \sqrt{\frac{(1-2)^2+(2-2)^2+(3-2)^2}{2}} = \sqrt{\frac{2}{2}} = 1$$
>
> $$s_Y = \sqrt{\frac{(2-4)^2+(4-4)^2+(6-4)^2}{2}} = \sqrt{\frac{8}{2}} = 2$$
>
> $$r = \frac{2}{1 \times 2} = 1$$
>
> **Step 5:** Interpret the result.
>
> $r = +1$ indicates a **perfect positive linear relationship**. As study hours increase, exam scores increase proportionally.
>
> $$\boxed{\operatorname{cov}(X,Y) = 2,\ r = +1,\ \text{Perfect positive correlation}}$$

**Example 2:** Negative relationship — Covariance, Correlation, and Correlation Matrix

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $X = \{1, 2, 3\}$ | Temperature setting |
> | $Y = \{6, 4, 2\}$ | Energy saved |
> | $n = 3$ | Number of paired observations |
> | Find: $\operatorname{cov}(X,Y)$, $r$, and correlation matrix | Full relationship analysis |
>
> **Step 1:** Compute the means.
>
> $$\bar{x} = 2, \qquad \bar{y} = 4$$
>
> **Step 2:** Compute paired deviations and their products.
>
> | $x_i$ | $y_i$ | $x_i - \bar{x}$ | $y_i - \bar{y}$ | $(x_i - \bar{x})(y_i - \bar{y})$ |
> |:---:|:---:|:---:|:---:|:---:|
> | 1 | 6 | $-1$ | 2 | $-2$ |
> | 2 | 4 | 0 | 0 | 0 |
> | 3 | 2 | 1 | $-2$ | $-2$ |
>
> $$\sum (x_i-\bar{x})(y_i-\bar{y}) = -4$$
>
> **Step 3:** Compute covariance.
>
> $$\operatorname{cov}(X,Y) = \frac{-4}{2} = -2$$
>
> **Step 4:** Compute correlation.
>
> Using $s_X = 1$ and $s_Y = 2$ (same computation as Example 1):
>
> $$r = \frac{-2}{1 \times 2} = -1$$
>
> **Step 5:** Build the correlation matrix and interpret.
>
> $$R = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$$
>
> $r = -1$ indicates a **perfect negative linear relationship**. As temperature setting increases, energy saved decreases proportionally.
>
> $$\boxed{\operatorname{cov}(X,Y) = -2,\ r = -1,\ \text{Perfect negative correlation}}$$

---

<p align="left">
  <a href="./statistics-basics.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./probability-fundamentals.md"><b>Next →</b></a>
  </span>
</p>
