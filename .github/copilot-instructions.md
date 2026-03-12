# Copilot Instructions — Statistics & Analytics Notes

These instructions define how concepts, formulas, and examples should be written across this workspace.

---

## 1. Topic Structure

When introducing a new topic or category, always start with a **tree diagram overview** using a code block before explaining each item in detail.

````markdown
```
Topic Name
├── Category A
│   ├── Sub-item 1
│   ├── Sub-item 2
│   └── Sub-item 3
│
└── Category B
    ├── Sub-item 4
    ├── Sub-item 5
    └── Sub-item 6
```
````

After the tree, use markdown heading hierarchy (`###`, `####`) to explain each category and its sub-items in detail.

---

## 2. Concept Explanation Hierarchy

Use this heading structure consistently:

```
## Topic Name
### N. Concept Name              ← numbered concept
#### Real-World Use Cases        ← practical applications
#### Steps                       ← how to solve it
#### Formula                     ← LaTeX formula + symbol table
#### Examples                    ← 2 worked examples
```

---

## 3. Formulas

### 3.1 LaTeX Format

All formulas must be written in LaTeX using `$$` block notation:

```markdown
$$
\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
$$
```

### 3.2 Symbol Explanation Table

Immediately after every formula, include a **"Where:"** table that explains each symbol with:

| Column            | Purpose                               |
| ----------------- | ------------------------------------- |
| **Symbol**        | The LaTeX-rendered math symbol        |
| **Pronunciation** | How to read/say the symbol in English |
| **Meaning**       | What the symbol represents in context |

Example:

```markdown
Where:
| Symbol | Pronunciation | Meaning |
|:---:|:---|:---|
| $\bar{x}$ | "x bar" | The mean (average) of the dataset |
| $\sum_{i=1}^{n}$ | "the sum from i equals 1 to n" | Add up all values from first to last |
| $x_i$ | "x sub i" | The i-th individual value in the dataset |
| $n$ | "n" | The total number of values in the dataset |
```

---

## 4. Examples

Every concept must include **exactly 2 worked examples**. Each example must follow this structure:

### 4.1 Given Block

Start every example with a **"Given:"** table inside a blockquote that extracts key values from the question:

```markdown
> **Given:**
>
> | Key Value                     | Description                           |
> | :---------------------------- | :------------------------------------ |
> | Dataset $= \{4, 8, 6, 5, 7\}$ | The set of observed values            |
> | $n = 5$                       | Total number of values in the dataset |
> | Find: $\bar{x}$               | The mean (average)                    |
```

### 4.2 Step-by-Step Solution

After the Given block, solve the problem **step by step inside a blockquote**, as a human would on paper:

1. **Write the formula** — restate the relevant formula.
2. **Identify / extract** — pull out values from the dataset.
3. **Substitute** — plug values into the formula.
4. **Simplify** — show intermediate arithmetic.
5. **Final answer** — box the result using `\boxed{}`.

```markdown
> **Step 1:** Write down the formula.
>
> $$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$
>
> **Step 2:** Identify the values and count them.
>
> Values: $x_1 = 4,\ x_2 = 8,\ x_3 = 6,\ x_4 = 5,\ x_5 = 7$
> Total number of values: $n = 5$
>
> **Step 3:** Substitute into the formula.
>
> $$\bar{x} = \frac{4 + 8 + 6 + 5 + 7}{5}$$
>
> **Step 4:** Simplify the numerator.
>
> $$\bar{x} = \frac{30}{5}$$
>
> **Step 5:** Divide.
>
> $$\boxed{\bar{x} = 6}$$
```

### 4.3 Example Variety

When applicable, the two examples should cover **different cases** to illustrate breadth:

- Odd vs even count (e.g., Median)
- Population vs sample (e.g., Variance, Standard Deviation)
- Unimodal vs multimodal (e.g., Mode)

---

## 5. General Formatting Rules

- Use **blockquotes** (`>`) for all example solutions to visually group them.
- Use **tables** for structured comparisons (deviations, frequencies, symbol meanings).
- Use **bold** for key terms on first mention.
- Use _italics_ for supplementary/related terms (e.g., _bell curve_, _asymptote_).
- Navigation links at the top and bottom of each page:
  ```html
  <p align="left">
    <a href="./previous.md"><b>← Previous</b></a>
    <span style="float:right">
      <a href="./next.md"><b>Next →</b></a>
    </span>
  </p>
  ```
- Separate major sections with `---` horizontal rules.

---

## 6. Steps Section

The "Steps" section should be a **numbered list** describing the human-readable procedure to solve the problem, written before the formula. Keep it concise — 3 to 6 steps.

```markdown
#### Steps

1. Sort the dataset in ascending order.
2. Count the total number of values ($n$).
3. If $n$ is **odd**, the median is the value at position $\frac{n+1}{2}$.
4. If $n$ is **even**, the median is the average of the values at positions $\frac{n}{2}$ and $\frac{n}{2}+1$.
```

---

## 7. Key Terms Section

When a topic has important related terminology, list them after the main explanation using italicized term names and a colon:

```markdown
- _Bell curve/normal distribution/gaussian distribution_: a symmetric, bell-shaped distribution...
- _Tail_: the part of a distribution that extends beyond the central part...
```

---

## 8. Real-World Use Cases Section

Every concept must include a **"Real-World Use Cases"** section placed **between the description and the Steps**. This section should list 3–5 bullet points showing where and why the concept is used in practice.

Include:

- **Domain-specific applications** (finance, healthcare, education, manufacturing, etc.)
- **Limitations or caveats** when relevant (e.g., sensitivity to outliers)
- **Advantages over related concepts** (e.g., why median is preferred over mean for skewed data)

```markdown
#### Real-World Use Cases

- **Finance**: Calculating the average monthly revenue of a business to assess overall performance.
- **Education**: Computing the average test score of a class to evaluate teaching effectiveness.
- **Healthcare**: Finding the average blood pressure of patients in a clinical trial.
- **Limitation**: Sensitive to outliers — e.g., a CEO's salary will drastically inflate the mean.
```

---

## 9. Visual Diagrams

Every concept should include an **ASCII visual diagram** placed between the description and the "Real-World Use Cases" section. Use code blocks (` ``` `) for all visuals.

Visuals should help the reader **see** the concept before reading the math. Use:

- **Number lines** for range, mean, standard deviation
- **Box diagrams** for quartile splits, IQR, and percentile divisions
- **Frequency bar charts** for mode (unimodal, bimodal)
- **Dot plots** for variance (high vs low vs zero)
- **Bell curve** ASCII art for standard deviation (empirical rule)
- **Sorted list with brackets** for median (odd vs even case)

### 9.1 Quartile / Percentile Splits

Use bordered box diagrams to show how data is divided:

````markdown
```
  ┌─────────┬─────────┬─────────┬─────────┐
  │   25%   │   25%   │   25%   │   25%   │
  └─────────┴─────────┴─────────┴─────────┘
            Q1        Q2        Q3
```
````

### 9.2 Box Plot / IQR

Show the full box-and-whisker structure with outlier bounds:

````markdown
```
  Outliers   Lower    Q1    Q2    Q3    Upper   Outliers
     ●       Bound     │     │     │    Bound      ●
  ◄──┼─────────┼───────┼─────┼─────┼───────┼──────┼──►
               │       ├─── IQR ───┤       │
          Q1-1.5×IQR                  Q3+1.5×IQR
```
````

### 9.3 Variance / Spread

Use dot plots on a number line to contrast high, low, and zero variance:

````markdown
```
  High variance:   ●       ●           ●   ●
  ◄────────────────────┼─────────────────────►
                       x̄

  Low variance:        ● ● ● ●
  ◄────────────────────┼─────────────────────►
                       x̄
```
````

### 9.4 Empirical Rule (Standard Deviation)

Show the 68-95-99.7 rule on a bell curve:

````markdown
```
               ┌──────── 99.7% ──────┐
               │  ┌───── 95% ─────┐  │
               │  │  ┌── 68% ──┐  │  │
               │  │  │    ██   │  │  │
               │  │  │   ████  │  │  │
               │  │  │  ██████ │  │  │
               │  │  │ ████████│  │  │
  ◄────────────┼──┼──┼────┼────┼──┼──┼────────────►
             -3σ -2σ -1σ  x̄  +1σ +2σ +3σ
```
````

---

## 10. Unit File Enrichment Workflow

This workspace contains **study material** organized in `unit_N/` folders, derived from raw lecture notes in `classNotes/sessionN/`. Enrichment means deepening shallow unit files to match classNotes depth.

### 10.1 Source Material Mapping

| Unit Folder | Primary ClassNotes Source                         | Fallback        |
| :---------- | :------------------------------------------------ | :-------------- |
| `unit_1/`   | `classNotes/session1/` and `classNotes/session2/` | Agent knowledge |
| `unit_2/`   | `classNotes/session3/`                            | Agent knowledge |
| `unit_3/`   | `classNotes/session4/`                            | Agent knowledge |
| `unit_4/`   | `classNotes/session5/`                            | Agent knowledge |

**If classNotes are missing or sparse for a topic** (the student missed class), use agent knowledge to produce the same depth and format. Do NOT produce shallow content just because classNotes are absent.

### 10.2 Enrichment Process

1. **Read ALL classNotes** for the relevant session(s) BEFORE writing anything. Build a gap list comparing classNotes content against the current unit file.
2. **Work file-by-file**, not all at once. Complete one `unit_N/*.md` file fully before moving to the next.
3. **Replace section-by-section** within each file:
   - Use `grep_search` for `^### [0-9]` to find section heading boundaries and line numbers.
   - Use `read_file` to capture the exact old content of ONE section (including its `---` separator).
   - Use `replace_string_in_file` to swap in the enriched version.
   - Move to the next section only after the previous replacement succeeds.
4. **Never replace the entire file at once** — token limits and match failures make whole-file replacement unreliable.

### 10.3 Depth Checklist

A section is NOT deep enough unless it includes **all applicable** items:

- [ ] Sub-concepts broken out as `####` subsections (e.g., Variance → Population vs Sample subsections)
- [ ] ASCII visual diagram BEFORE any formula (see Section 9)
- [ ] Comparison table when two related concepts exist (e.g., Variance vs CV, Population vs Sample notation)
- [ ] Interpretation scale with threshold values where applicable (e.g., correlation strength: weak < 0.5, moderate 0.5–0.8, strong > 0.8)
- [ ] Key identity relationships stated explicitly (e.g., $\operatorname{var}(X) = \operatorname{cov}(X,X)$)
- [ ] Deviation/computation tables inside worked examples (show the row-by-row work)
- [ ] Matrix notation where classNotes use it (covariance matrix, correlation matrix)
- [ ] Population ($\sigma^2$, $\mu$, $N$) vs Sample ($s^2$, $\bar{x}$, $n$) distinction wherever variance, standard deviation, or mean appears
- [ ] Bessel's correction explained when sample variance is introduced

### 10.4 Common First-Pass Gaps

These are consistently missing from first-draft content and trigger rework. Always include them proactively:

| Gap                                                             | Where It Applies                          |
| :-------------------------------------------------------------- | :---------------------------------------- |
| Population vs Sample notation table                             | Variance, Standard Deviation, Mean        |
| Strength/interpretation thresholds                              | Correlation, Coefficient of Determination |
| Analysis type taxonomy (univariate/bivariate/multivariate)      | Correlation, Regression                   |
| Bessel's correction ($n-1$ denominator)                         | Sample Variance, Sample Std Dev           |
| 5-number summary + box plot + 1.5×IQR outlier rule              | Dispersion / Quartiles                    |
| Skewness direction rules (mean vs median position)              | Central Tendency                          |
| Independent vs dependent variable convention (x-axis vs y-axis) | Correlation, Regression                   |

### 10.5 Example Differentiation Rules

The two required examples per concept must cover **meaningfully different cases**, not just different numbers:

| Concept Type       | Example 1 Case         | Example 2 Case                           |
| :----------------- | :--------------------- | :--------------------------------------- |
| Median             | Odd count dataset      | Even count dataset                       |
| Variance / Std Dev | Population ($N$)       | Sample ($n-1$)                           |
| Mode               | Unimodal               | Bimodal or no mode                       |
| Correlation        | Positive relationship  | Negative + build correlation matrix      |
| Probability        | Simple event           | Complement or conditional                |
| Distributions      | Specific parameter set | Different parameter set showing contrast |

The second example should always **demonstrate something extra** the first doesn't (e.g., outlier detection, matrix construction, edge case).

### 10.6 Project Progress Tracking

Track enrichment progress per unit. When resuming work, check the status below and continue from where the previous session left off.

#### Unit 1 (`unit_1/`)

| File                                    | Status                             |
| :-------------------------------------- | :--------------------------------- |
| `index.md`                              | ✅ Complete                        |
| `statistics-basics.md`                  | ✅ Fully enriched (all 3 sections) |
| `descriptive-statistics.md`             | ✅ Fully enriched (all 4 sections) |
| `probability-fundamentals.md`           | ⬜ Not yet enriched                |
| `random-variables-and-distributions.md` | ⬜ Not yet enriched                |

#### Units 2–4

| Unit      | Status         |
| :-------- | :------------- |
| `unit_2/` | ⬜ Not started |
| `unit_3/` | ⬜ Not started |
| `unit_4/` | ⬜ Not started |
