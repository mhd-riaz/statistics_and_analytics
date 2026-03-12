<p align="left">
  <a href="./index.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./descriptive-statistics.md"><b>Next →</b></a>
  </span>
</p>

---

# Statistics Basics

```
Statistics Basics
├── Statistical Thinking
│   ├── Descriptive vs Inferential Statistics
│   ├── Population, Sample, Parameter, Statistic
│   ├── The Statistical Problem (Observed → Non-observed)
│   ├── Estimates
│   └── Big Data and Modern Statistics
│
├── Data Fundamentals
│   ├── Data Sources (Primary vs Secondary)
│   ├── Qualitative Data (Nominal, Binary, Ordinal)
│   ├── Quantitative Data (Interval, Ratio)
│   ├── Types of Datasets
│   └── Measurement Scale Summary
│
└── Sampling Methods
    ├── Sampling Fraction
    ├── Random Sampling
    │   ├── Simple Random Sampling
    │   ├── Stratified Sampling
    │   ├── Cluster Sampling
    │   └── Systematic Sampling
    │
    └── Non-Random Sampling
        ├── Snowball Sampling
        ├── Convenience Sampling
        └── Judgmental Sampling
```

---

## Statistics Basics

### 1. Statistical Thinking

**Statistics** is the discipline of learning from data — a tool used to perform computation on datasets in order to get meaningful insights. At the foundation of statistics is a workflow: describe the data you observed, then use that evidence to say something about a larger group you care about.

Statistics can be classified into two broad categories:

| Descriptive Statistics              | Inferential Statistics                                    |
| :---------------------------------- | :-------------------------------------------------------- |
| Used to understand / summarize data | Helps in making decisions                                 |
| Refers to what has already happened | Refers to what might / is about to happen                 |
| Concerned with data summarization   | Uses sample summaries to talk about population parameters |

**Descriptive statistics** summarizes what is already observed — tables, charts, measures of center and spread. **Inferential statistics** uses a sample summary to estimate or test something about a population — hypothesis tests, confidence intervals, regression.

#### Terminologies

Think of it from a data perspective. Let the data you have now be `dataNow` — it contains records that have already been collected. You want to apply conclusions from this past data to future events, i.e. `futureData`. But the data you have is only **partly related** to the future. In machine learning this partly related data is known as **test data**.

> **Test Dataset** helps us evaluate how well a model generalizes to new, unseen data, ensuring its effectiveness in real-world applications.

Future data is different from the data we have, but both come from the **same place** — the **population**.

```
  ┌───────────────────────────────── Population ──────────────────────────────────┐
  │                 (universe of all possible data for a specified object)         │
  │                                                                               │
  │    Past Data        Present Data        Future Data                           │
  │   (collected)       (observable)        (not yet seen)                        │
  │       │                  │                   │                                │
  │       └──── dataNow ─────┘                   │                                │
  │              (sample)                    futureData                            │
  │                  │                       (unknown)                             │
  │                  ▼                                                             │
  │             Statistic ──────── estimates ──────► Parameter                     │
  │           (computed)                           (true but unknown)              │
  └───────────────────────────────────────────────────────────────────────────────┘
```

1. **Population**:
   - The universe of all possible data for a specified object — the sum of past, present, and future data.
   - Theoretically it is possible to observe a full population at once, but not practically. With advancements in technology we can now deliberately observe populations (e.g. census).
   - _Example_: All people who have visited or will visit my website.

2. **Parameter**:
   - A numerical value associated with the **population** — the thing we are truly interested in.
   - _Example_: The average time people spend on my website (across all visitors ever).
   - This is generally **not directly observed** — just like the population itself.
   - Notation: population mean $\mu$, population proportion $p$.

3. **Sample**:
   - A selected subset (observed part) of the population.
   - _Example_: People who visited the website on a specific day.
   - This **is** observed — you can compute on it.
   - But it does **not** represent the whole population, and the exact same sample will not recur.

4. **Statistic**:
   - A numerical value computed from an observed sample.
   - _Example_: The average time people spent on the website on a specific day.
   - Notation: sample mean $\bar{x}$, sample proportion $\hat{p}$.

| Population Symbol | Sample Symbol | Meaning            |
| :---------------: | :-----------: | :----------------- |
|       $\mu$       |   $\bar{x}$   | Mean (average)     |
|        $p$        |   $\hat{p}$   | Proportion         |
|    $\sigma^2$     |     $s^2$     | Variance           |
|     $\sigma$      |      $s$      | Standard deviation |

#### The Statistical Problem (Observed → Non-observed)

The core statistical problem is to go **from the observed to the non-observed** — from the sample to the population — because the object we are interested in is not the statistic but the **parameter**, and the universe we are interested in is the **population**.

```
  Observed World                        Non-observed World
  ┌──────────────────┐    inference     ┌──────────────────┐
  │     Sample       │ ──────────────►  │   Population     │
  │   Statistic (x̄)  │                  │  Parameter (μ)   │
  └──────────────────┘                  └──────────────────┘
```

This notion of a sample drawn from a population has defined the subject of statistics for many years — and is still being challenged today with **big data** that appears to be a population, not a sample.

> Even if you can see all your customers in the big data you have today, your results will still have to **infer** what those customers will do in the **future**. So even if you can see the entire population, that extraction will apply to elements that are **still not in the population**.
>
> If you think you are working with the population, think twice — the actual population might have changed while you were cleaning or processing your data. It is considered good practice to treat your dataset as a **sample** rather than a population.

#### Estimates

**Estimation** is the process of using sample data to infer unknown population parameters.

```
  Sample ──► Compute Statistic ──► Use as Estimate of Parameter

  x̄  ≈  μ     (sample mean estimates population mean)
  p̂  ≈  p     (sample proportion estimates population proportion)
  s² ≈  σ²    (sample variance estimates population variance)
```

#### Real-World Use Cases

- **Manufacturing**: Measure 40 bolts from a production line and use the sample average to estimate the line's true average diameter.
- **Healthcare**: Summarize patient blood pressure readings, then infer the typical blood pressure for the broader target group.
- **Education**: Compute the mean quiz score of a class and use it to judge likely performance of the full batch.
- **Limitation**: A poor sample leads to weak inference, even if the calculations are correct.

#### Steps

1. Define the **population** you care about.
2. Collect a **sample** from that population.
3. Compute a **statistic** from the sample.
4. Use the statistic as an **estimate** of the unknown **parameter**.

#### Formula

$$
\hat{\theta} = g(x_1, x_2, \dots, x_n)
$$

Where:
|         Symbol         | Pronunciation       | Meaning                                                   |
| :--------------------: | :------------------ | :-------------------------------------------------------- |
|     $\hat{\theta}$     | "theta hat"         | A sample-based estimate of an unknown population quantity |
|       $g(\cdot)$       | "g of"              | The rule used to turn raw sample values into an estimate  |
| $x_1, x_2, \dots, x_n$ | "x one through x n" | The observed values in the sample                         |
|          $n$           | "n"                 | The sample size                                           |

#### Examples

**Example 1 — Estimating average battery life**

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Sample battery lives $= \{9, 11, 10, 12, 8\}$ hours | Observed battery durations |
> | $n = 5$ | Number of sampled batteries |
> | Find: statistic and parameter | Identify the observed summary and the unknown target |
>
> **Step 1:** Identify the population idea.
>
> The population is **all batteries** produced by the process.
>
> **Step 2:** Identify the sample.
>
> The five observed batteries form the sample.
>
> **Step 3:** Compute a sample statistic.
>
> $$\bar{x} = \frac{9 + 11 + 10 + 12 + 8}{5} = \frac{50}{5} = 10$$
>
> **Step 4:** Interpret the result.
>
> The sample mean $\bar{x} = 10$ hours is the **statistic**.
>
> **Step 5:** State the inferential meaning.
>
> $$\boxed{\bar{x} = 10 \text{ hours is used to estimate the population mean } \mu}$$

**Example 2 — Estimating a defect rate**

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Defective items $= 6$ | Number of defective items found |
> | Sample size $n = 50$ | Number of inspected items |
> | Find: sample proportion and target parameter | Identify the sample estimate |
>
> **Step 1:** Identify the population idea.
>
> The population is **all items** produced in the process.
>
> **Step 2:** Identify the statistic to use.
>
> For a defect rate, use the sample proportion.
>
> **Step 3:** Compute the statistic.
>
> $$\hat{p} = \frac{6}{50} = 0.12$$
>
> **Step 4:** Interpret the result.
>
> The sample statistic says 12% of the sampled items are defective.
>
> **Step 5:** State the inferential meaning.
>
> $$\boxed{\hat{p} = 0.12 \text{ estimates the unknown population proportion } p}$$

---

### 1b. Big Data and Modern Statistics

**Big Data** is a set of data that cannot be managed, processed, or analyzed with traditional software or algorithms within a reasonable amount of time. It is characterized by the **5 V's**:

```
  Big Data
  ├── Volume    — massive quantities of data
  ├── Velocity  — speed at which data is generated and processed
  ├── Variety   — many different formats (text, images, logs, …)
  ├── Value     — actionable insight that can be extracted
  └── Veracity  — trustworthiness and accuracy of the data
```

_Example_: Walmart handles over 1 million purchase transactions per hour.

#### Need for Statistics

Statistics was invented to solve numerical problems such as:
- If I put this amount of fertilizer, what yield will I get?
- Did the medicine actually improve the cure rate?

**Statistical methods** have been used to simply describe what was observed. These methods now adapt to standards driven by technology events:
- Social networks generating massive behavioral data
- Automated data collection from IoT devices
- Modern computing power for complex calculations
- Scalable data storage and processing pipelines

> The **design phase** in a project or experiment is the most crucial step for statistical planning — a well-designed study prevents most analytical headaches.

---

### 2. Data Fundamentals

**Data** is a collection of facts, measurements, or observations — numbers, words, images, etc. Before choosing any formula, you must understand what kind of data you have.

**Attributes** are the characteristics or properties of data that can be used to describe, analyze, and understand it. They help in categorizing, organizing, and interpreting data.

#### Data Sources

| **Primary Data**                                                              | **Secondary Data**                                                   |
| :---------------------------------------------------------------------------- | :------------------------------------------------------------------- |
| Data that is collected continuously / in real-time                            | Data that has already been collected, stored as archive or published |
| Fresh, collected for specific analysis, ingested by a computer during runtime | A bit old, as it was collected and stored already                    |

During older times, the rule of thumb was to use secondary data as collection of primary data was not feasible. But due to automation and technological advancement, it is now much easier to collect real-time (primary) data.

#### Types of Data

```
  Data
  ├── Qualitative (Categorical)
  │   ├── Nominal   → labels with no order
  │   ├── Binary    → only two outcomes
  │   │   ├── Symmetric   (both outcomes equally important)
  │   │   └── Asymmetric  (one outcome more important)
  │   └── Ordinal   → ordered categories, gaps not meaningful
  │
  └── Quantitative (Numerical)
      ├── Discrete  → integer values (counted)
      └── Continuous → real numbers (measured)
          ├── Interval → equal gaps, no true zero
          └── Ratio    → equal gaps, true zero
```

##### Qualitative Data (Categorical)

1. **Nominal**
   - Pure categorical data, no inherent order.
   - _Examples_: Hair colour {black, grey, white, blond}, marital status {married, single, divorced}, ID number, zip code.
   - **NOTE**: Even though ID numbers and zip codes contain digits, arithmetic operations on them make no sense (e.g. squaring a zip code or adding two IDs) — such data is still nominal.

2. **Binary**
   - A special case of nominal data with exactly **two** outcomes (yes/no, 0/1, true/false).
   - **Symmetric binary**: Both outcomes are equally important.
     - _Example_: Gender (male, female).
   - **Asymmetric binary**: Outcomes are not equally important.
     - _Example_: Medical test result (positive or negative).
     - _Best practice_: Assign the value `1` (true) to the more important / rarer outcome (e.g. HIV positive = 1).

3. **Ordinal**
   - Values have a meaningful **order** (ranking), but the gaps between ranks are not necessarily equal or measurable.
   - _Examples_: {small, medium, large}, army ranking, letter grades {A, B, C, D, F}.

##### Quantitative Data (Numerical)

Values can be **integer** (1, 2, 3, …) or **real** (175 cm, 175.6 cm, 175.65 cm).

1. **Interval**
   - Measured on a scale of equal-sized units.
   - Values have order but **no true zero point**.
   - _Example_: Temperature in °C — 0°C does not mean "no temperature". Calendar dates — the birth of an individual is not on year 0.

2. **Ratio**
   - Measured on a scale of equal-sized units with a **true zero**.
   - Ratios between values are meaningful.
   - _Examples_: Weight (0 kg = no weight), runtime in hours (0 hours = no runtime), income.

#### Types of Datasets

```
  Datasets
  ├── Records
  │   ├── Relational records
  │   ├── Data matrix (numerical matrix, cross-tabs)
  │   ├── Document data (text)
  │   └── Transactional data
  │
  ├── Graph and Network
  │   ├── World Wide Web
  │   ├── Social / information networks
  │   └── Molecular structures
  │
  ├── Ordered
  │   ├── Video data (sequence of images)
  │   ├── Temporal data (time-series)
  │   ├── Sequential data (transaction sequences)
  │   └── Genetic sequence data
  │
  └── Spatial, Image, and Multimedia
      ├── Spatial data (maps)
      ├── Image data
      └── Video data
```

#### Measurement Scale Summary

| Scale    | Order? | Equal gaps? | True zero? | Example                        |
| :------- | :----: | :---------: | :--------: | :----------------------------- |
| Nominal  |   ✗    |      ✗      |     ✗      | Blood group, colour, ID        |
| Ordinal  |   ✓    |      ✗      |     ✗      | Grades, satisfaction level     |
| Interval |   ✓    |      ✓      |     ✗      | Temperature °C, calendar dates |
| Ratio    |   ✓    |      ✓      |     ✓      | Weight, height, runtime        |

#### Real-World Use Cases

- **Survey Design**: Choose mode for nominal responses such as department or blood group.
- **Education**: Treat letter grades as ordinal because order matters but gaps are not numerically equal.
- **Engineering**: Use ratio scale for weight, length, and time because zero is meaningful.
- **Medical Research**: Binary asymmetric classification for disease positive/negative, where the positive case is the important outcome.
- **Limitation**: Misclassifying a variable can lead to meaningless arithmetic, such as averaging ID numbers.

#### Steps

1. Check whether the variable is a **category** or a **measurement**.
2. If categorical, decide whether the categories are **ordered** (ordinal) or **unordered** (nominal).
3. If categorical with two outcomes, determine whether it is **symmetric** or **asymmetric** binary.
4. If numerical, decide whether zero is **arbitrary** (interval) or a **true absence** (ratio).
5. Match the data to the correct scale before choosing analysis methods.

#### Formula

$$
\text{Data} = \text{Qualitative} \cup \text{Quantitative}
$$

Where:
|        Symbol         | Pronunciation  | Meaning                                              |
| :-------------------: | :------------- | :--------------------------------------------------- |
|     $\text{Data}$     | "data"         | The full collection of observed values               |
| $\text{Qualitative}$  | "qualitative"  | Non-numeric category-based values                    |
| $\text{Quantitative}$ | "quantitative" | Numeric measured or counted values                   |
|        $\cup$         | "union"        | Combined categories that make up the full data space |

#### Examples

**Example 1 — Classify student variables**

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Blood group | Medical category |
> | Satisfaction level $= \{$low, medium, high$\}$ | Ordered feedback category |
> | HIV test result $= \{$positive, negative$\}$ | Binary medical test |
> | Find: data type | Classify each variable |
>
> **Step 1:** Inspect blood group.
>
> Blood group has categories such as A, B, AB, and O.
>
> **Step 2:** Check whether order exists.
>
> Blood groups have **no natural order** → **qualitative nominal**.
>
> **Step 3:** Inspect satisfaction level.
>
> Low, medium, and high are categories with an obvious order → **qualitative ordinal**.
>
> **Step 4:** Inspect HIV test result.
>
> Only two outcomes. The positive result is rarer and more important → **asymmetric binary** (code positive = 1).
>
> **Step 5:** State the final classification.
>
> $$\boxed{\text{Blood group: nominal | Satisfaction: ordinal | HIV test: asymmetric binary}}$$

**Example 2 — Classify engineering measurements**

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Temperature in $^\circ C$ | A numerical scale |
> | Machine runtime in hours | A measured duration |
> | Product ID numbers | Numerical labels |
> | Find: measurement scale | Decide the correct classification |
>
> **Step 1:** Inspect temperature in Celsius.
>
> Celsius has equal gaps, but 0°C does **not** mean no temperature → **interval**.
>
> **Step 2:** Inspect runtime in hours.
>
> Runtime has equal gaps, and 0 hours means no runtime → **ratio**.
>
> **Step 3:** Inspect product ID numbers.
>
> IDs are digits used as labels. Adding or averaging them is meaningless → **nominal** (despite containing numbers).
>
> **Step 4:** State the final classification.
>
> $$\boxed{\text{Temperature: interval | Runtime: ratio | Product ID: nominal}}$$

---

### 3. Sampling Methods

Because observing an entire population is often expensive or impossible, statistics relies on **sampling**. The goal is to collect a sample that represents the population as fairly as possible.

Sampling techniques fall into two broad categories:

```
  Sampling Methods
  ├── Random (Probability-Based)
  │   ├── Simple Random Sampling   → every member has equal chance
  │   ├── Stratified Sampling      → divide into subgroups, sample each
  │   ├── Cluster Sampling         → pick whole clusters, survey all inside
  │   └── Systematic Sampling      → pick every k-th member from a list
  │
  └── Non-Random (Non-Probability)
      ├── Snowball Sampling        → existing subjects recruit more
      ├── Convenience Sampling     → whoever is easiest to reach
      └── Judgmental Sampling      → researcher picks "typical" members
```

#### Random (Probability-Based) Sampling

Each member of the population has a **known, non-zero probability** of being selected. This is the foundation for valid statistical inference.

| Method            | How it works                                                                                                                                            | Best when                                                                                         |
| :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------ |
| **Simple Random** | Assign numbers to every member, draw $n$ at random (e.g. lottery, random number generator)                                                              | A complete list of the population exists                                                          |
| **Stratified**    | Divide the population into non-overlapping subgroups (strata) by a key attribute, then take a random sample from **each** stratum                       | The population has important subgroups (e.g. age, income) that must be proportionally represented |
| **Cluster**       | Divide the population into naturally occurring groups (clusters), randomly select a few clusters, then include **all** members of the selected clusters | Subjects are naturally grouped (e.g. regions, schools) and individual listing is impractical      |
| **Systematic**    | From an ordered list, pick a random starting point, then select every $k$-th member where $k = N/n$                                                     | A physical or ordered list is available and the population has no hidden periodic pattern         |

#### Non-Random (Non-Probability) Sampling

Members are **not selected by a random mechanism**. These methods are useful when random sampling is impractical, but they carry a higher risk of bias.

| Method                     | How it works                                                                                                       | Typical use                                                                           |
| :------------------------- | :----------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------ |
| **Snowball**               | Start with a few known subjects; each subject refers others who meet the criteria. The sample "snowballs" outward. | Hard-to-reach populations: drug users, undocumented immigrants, rare disease patients |
| **Convenience**            | Sample whoever is easiest to access — volunteers, passers-by, online responders                                    | Pilot studies, quick exploratory surveys                                              |
| **Judgmental (Purposive)** | The researcher deliberately hand-picks subjects believed to be representative                                      | Expert panels, case studies, qualitative research                                     |

> **Important**: Non-random methods do not support formal statistical inference (confidence intervals, hypothesis tests) because the selection probability is unknown. Results may still be informative but cannot be generalized to the population with known precision.

#### Real-World Use Cases

- **Market Research**: Use stratified sampling to ensure age groups are proportionally represented.
- **Manufacturing**: Use systematic sampling to inspect every 20th item on a production line.
- **Public Health**: Use cluster sampling when households are naturally grouped by region.
- **Epidemiology**: Use snowball sampling to study populations that are difficult to identify (e.g. rare genetic condition carriers).
- **Limitation**: Convenience sampling is fast but often biased and weak for inference — it should only be used for exploratory work.

#### Steps

1. Define the population size $N$ and required sample size $n$.
2. Compute the sampling fraction $f = n / N$ if needed.
3. Choose a sampling method based on population structure and accessibility.
4. If random: draw the sample using the chosen method without bias.
5. If non-random: document the selection criteria and acknowledge the limitation on generalizability.

#### Formula

$$
f = \frac{n}{N}
\qquad
k = \frac{N}{n}
$$

Where:
| Symbol | Pronunciation | Meaning                                                               |
| :----: | :------------ | :-------------------------------------------------------------------- |
|  $f$   | "f"           | Sampling fraction, the share of the population included in the sample |
|  $n$   | "n"           | Sample size                                                           |
|  $N$   | "N"           | Population size                                                       |
|  $k$   | "k"           | Systematic sampling interval                                          |

#### Examples

**Example 1 — Compute the sampling fraction**

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Population size $N = 1000$ | Total number of products |
> | Sample size $n = 80$ | Number of products inspected |
> | Find: $f$ | Sampling fraction |
>
> **Step 1:** Write the formula.
>
> $$f = \frac{n}{N}$$
>
> **Step 2:** Substitute the values.
>
> $$f = \frac{80}{1000}$$
>
> **Step 3:** Simplify.
>
> $$f = 0.08$$
>
> **Step 4:** Convert to percentage.
>
> $$f = 8\%$$
>
> **Step 5:** State the final answer.
>
> $$\boxed{f = 0.08 = 8\%}$$

**Example 2 — Systematic sampling interval**

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | Population size $N = 600$ | Total students on the list |
> | Desired sample size $n = 30$ | Students to select |
> | Find: $k$ and method | Determine the sampling interval |
>
> **Step 1:** Write the systematic interval formula.
>
> $$k = \frac{N}{n}$$
>
> **Step 2:** Substitute the values.
>
> $$k = \frac{600}{30}$$
>
> **Step 3:** Calculate the interval.
>
> $$k = 20$$
>
> **Step 4:** Interpret the result.
>
> Start from a random position between 1 and 20, then pick every 20th student from the ordered list.
>
> **Step 5:** State the final answer.
>
> $$\boxed{k = 20 \text{, so systematic sampling selects every 20th student}}$$

---

<p align="left">
  <a href="./index.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./descriptive-statistics.md"><b>Next →</b></a>
  </span>
</p>