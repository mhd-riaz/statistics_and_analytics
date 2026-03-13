<p align="left">
  <a href="./hypothesis-testing.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="../unit_3/index.md"><b>Next →</b></a>
  </span>
</p>

---

## Analysis of Variance (ANOVA)

**Analysis of Variance (ANOVA)** is a statistical method for comparing the means of **three or more groups** to determine if at least one group mean differs significantly from the others. While a t-test compares two groups, ANOVA generalizes this to $k$ groups without inflating the Type I error rate that would come from running multiple pairwise t-tests.

```
Analysis of Variance (ANOVA)
├── 13. One-Way ANOVA
│   ├── Between-Group Variation (SSB)
│   ├── Within-Group Variation (SSW)
│   ├── F-Statistic and F-Distribution
│   └── ANOVA Summary Table
│
├── 14. Two-Way ANOVA
│   ├── Two Factors (Rows and Columns)
│   ├── Main Effects (Factor A, Factor B)
│   ├── Interaction Effect (A × B)
│   └── Two-Way ANOVA Table
│
└── 15. Applications in Engineering Research
    ├── Experimental Design
    ├── Choosing the Right Test
    └── End-to-End Workflow
```

---

### 13. One-Way ANOVA

**One-Way ANOVA** tests whether the means of $k$ independent groups (levels of one factor) are all equal, or if at least one differs. It works by partitioning the total variability in the data into two components: variation _between_ groups and variation _within_ groups.

```
  The Logic of ANOVA — Partitioning Variation

  Total Variation (SST)
  ┌──────────────────────────────────────────┐
  │                                          │
  │  ┌─────────────────┐  ┌───────────────┐  │
  │  │ Between Groups  │  │ Within Groups │  │
  │  │     (SSB)       │  │    (SSW)      │  │
  │  │                 │  │               │  │
  │  │ Due to factor   │  │ Due to random │  │
  │  │ (real effect?)  │  │ variation     │  │
  │  └─────────────────┘  └───────────────┘  │
  │                                          │
  └──────────────────────────────────────────┘

  F = SSB / (k−1)   =  MSB
      ─────────────     ───
      SSW / (N−k)       MSW

  If F is large → group means differ significantly
  If F ≈ 1      → variation between groups ≈ random noise
```

**Key Concepts:**

| Term                   | Symbol | Meaning                                                         |
| :--------------------- | :----: | :-------------------------------------------------------------- |
| Sum of Squares Between | $SSB$  | Variation due to differences _between_ group means              |
| Sum of Squares Within  | $SSW$  | Variation due to differences _within_ each group (random error) |
| Sum of Squares Total   | $SST$  | Total variation in all data ($SST = SSB + SSW$)                 |
| Mean Square Between    | $MSB$  | $SSB / (k - 1)$ — average between-group variation               |
| Mean Square Within     | $MSW$  | $SSW / (N - k)$ — average within-group variation                |
| F-Statistic            |  $F$   | $MSB / MSW$ — ratio of between-group to within-group variation  |

**Why Not Just Run Multiple t-Tests?**

If you have 4 groups and compare all pairs with t-tests, that's $\binom{4}{2} = 6$ comparisons. Each at $\alpha = 0.05$ gives a combined Type I error rate of roughly $1 - (1 - 0.05)^6 \approx 0.26$ — a 26% chance of a false positive! ANOVA controls this by testing all groups simultaneously at a single $\alpha$.

**Assumptions:**

1. Each group is drawn from a **normally distributed** population.
2. The groups have **equal variances** (_homogeneity of variance_).
3. Observations are **independent**.

#### Real-World Use Cases

- **Manufacturing**: Comparing the tensile strength of parts produced by 4 different machines to see if machine choice matters.
- **Agriculture**: Testing whether 3 types of fertilizer produce different average crop yields.
- **Education**: Comparing average test scores across 5 teaching methods.
- **Limitation**: ANOVA tells you _that_ at least one mean differs, but not _which_ one. You need **post-hoc tests** (e.g., Tukey's HSD) to find which pairs are different.

#### Steps

1. State $H_0$: all group means are equal ($\mu_1 = \mu_2 = \cdots = \mu_k$).
2. State $H_1$: at least one mean differs.
3. Choose $\alpha$ (typically 0.05).
4. Compute the group means ($\bar{x}_j$) and the overall mean ($\bar{\bar{x}}$).
5. Compute $SSB$, $SSW$, and $SST$.
6. Compute the degrees of freedom: $df_B = k - 1$, $df_W = N - k$.
7. Compute $MSB = SSB / df_B$ and $MSW = SSW / df_W$.
8. Compute $F = MSB / MSW$.
9. Compare $F$ to $F_{\text{critical}}$ (or find the p-value). If $F \geq F_{\text{critical}}$, reject $H_0$.

#### Formula

$$
F = \frac{MSB}{MSW} = \frac{SSB \,/\, (k-1)}{SSW \,/\, (N-k)}
$$

Where:

$$
SSB = \sum_{j=1}^{k} n_j (\bar{x}_j - \bar{\bar{x}})^2
$$

$$
SSW = \sum_{j=1}^{k} \sum_{i=1}^{n_j} (x_{ij} - \bar{x}_j)^2
$$

$$
SST = SSB + SSW
$$

Where:

|     Symbol      | Pronunciation         | Meaning                                                |
| :-------------: | :-------------------- | :----------------------------------------------------- |
|       $F$       | "F"                   | The F-statistic (ratio of between to within variation) |
|       $k$       | "k"                   | Number of groups                                       |
|       $N$       | "capital N"           | Total number of observations across all groups         |
|      $n_j$      | "n sub j"             | Number of observations in group $j$                    |
|   $\bar{x}_j$   | "x bar sub j"         | Mean of group $j$                                      |
| $\bar{\bar{x}}$ | "x double bar"        | Grand mean (mean of all observations)                  |
|    $x_{ij}$     | "x sub i j"           | The $i$-th observation in group $j$                    |
|      $MSB$      | "mean square between" | $SSB / (k-1)$                                          |
|      $MSW$      | "mean square within"  | $SSW / (N-k)$                                          |

**ANOVA Summary Table Template:**

| Source         |  SS   |   df    |        MS         |       F       |
| :------------- | :---: | :-----: | :---------------: | :-----------: |
| Between Groups | $SSB$ | $k - 1$ | $MSB = SSB/(k-1)$ | $F = MSB/MSW$ |
| Within Groups  | $SSW$ | $N - k$ | $MSW = SSW/(N-k)$ |               |
| **Total**      | $SST$ | $N - 1$ |                   |               |

#### Examples

---

##### Example 1 — One-Way ANOVA (3 Groups, Equal Size)

An engineer tests 3 different alloys for tensile strength (in MPa). Each alloy is tested 4 times:

| Alloy A | Alloy B | Alloy C |
| :-----: | :-----: | :-----: |
|   45    |   55    |   50    |
|   42    |   58    |   48    |
|   48    |   52    |   53    |
|   41    |   51    |   49    |

Test at $\alpha = 0.05$ whether the alloys have different mean tensile strengths.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $k = 3$ | Number of groups (alloys) |
> | $n_j = 4$ per group | Sample size per group |
> | $N = 12$ | Total observations |
> | $df_B = k - 1 = 2$ | Between-group degrees of freedom |
> | $df_W = N - k = 9$ | Within-group degrees of freedom |
> | $\alpha = 0.05$ | Significance level |
> | $F_{\text{critical}} = 4.256$ | From F-table: $df_1=2$, $df_2=9$, $\alpha=0.05$ |
> | Find: Reject or fail to reject $H_0$? | |

> **Step 1:** State the hypotheses.
>
> $$H_0: \mu_A = \mu_B = \mu_C \qquad H_1: \text{At least one mean differs}$$
>
> **Step 2:** Compute group means and grand mean.
>
> $$\bar{x}_A = \frac{45+42+48+41}{4} = \frac{176}{4} = 44$$
>
> $$\bar{x}_B = \frac{55+58+52+51}{4} = \frac{216}{4} = 54$$
>
> $$\bar{x}_C = \frac{50+48+53+49}{4} = \frac{200}{4} = 50$$
>
> $$\bar{\bar{x}} = \frac{176 + 216 + 200}{12} = \frac{592}{12} = 49.33$$
>
> **Step 3:** Compute $SSB$.
>
> $$SSB = \sum n_j(\bar{x}_j - \bar{\bar{x}})^2$$
> $$= 4(44 - 49.33)^2 + 4(54 - 49.33)^2 + 4(50 - 49.33)^2$$
> $$= 4(28.41) + 4(21.81) + 4(0.45)$$
> $$= 113.64 + 87.24 + 1.80 = 202.68$$
>
> **Step 4:** Compute $SSW$.
>
> | Group | Values | Deviations from $\bar{x}_j$ | Squared deviations |
> |:---|:---|:---|:---|
> | A ($\bar{x}=44$) | 45, 42, 48, 41 | 1, −2, 4, −3 | 1, 4, 16, 9 → sum = 30 |
> | B ($\bar{x}=54$) | 55, 58, 52, 51 | 1, 4, −2, −3 | 1, 16, 4, 9 → sum = 30 |
> | C ($\bar{x}=50$) | 50, 48, 53, 49 | 0, −2, 3, −1 | 0, 4, 9, 1 → sum = 14 |
>
> $$SSW = 30 + 30 + 14 = 74$$
>
> **Step 5:** Build the ANOVA table.
>
> | Source | SS | df | MS | F |
> |:---|:---:|:---:|:---:|:---:|
> | Between | 202.68 | 2 | 101.34 | **12.34** |
> | Within | 74.00 | 9 | 8.22 | |
> | **Total** | 276.68 | 11 | | |
>
> $$F = \frac{MSB}{MSW} = \frac{101.34}{8.22} = 12.34$$
>
> **Step 6:** Compare to critical value.
>
> $$F = 12.34 > F_{\text{critical}} = 4.256$$
>
> **Step 7:** Decision.
>
> $$\boxed{\text{Reject } H_0}$$
>
> **Interpretation:** At the 5% significance level, there **is** sufficient evidence that the three alloys have different mean tensile strengths. A post-hoc test (e.g., Tukey's HSD) would be needed to determine _which_ alloys differ.

---

##### Example 2 — One-Way ANOVA (Unequal Group Sizes)

A school district compares homework hours per week across 3 grade levels:

- **Grade 9** ($n_1 = 3$): 5, 7, 6
- **Grade 10** ($n_2 = 4$): 8, 10, 9, 11
- **Grade 11** ($n_3 = 3$): 12, 14, 13

Test at $\alpha = 0.05$.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $k = 3$ | Number of groups |
> | $n_1 = 3,\ n_2 = 4,\ n_3 = 3$ | Group sizes |
> | $N = 10$ | Total observations |
> | $df_B = 2$, $df_W = 7$ | Degrees of freedom |
> | $\alpha = 0.05$ | Significance level |
> | $F_{\text{critical}} = 4.737$ | From F-table: $df_1=2$, $df_2=7$, $\alpha=0.05$ |
> | Find: Reject or fail to reject $H_0$? | |

> **Step 1:** State the hypotheses.
>
> $$H_0: \mu_9 = \mu_{10} = \mu_{11} \qquad H_1: \text{At least one mean differs}$$
>
> **Step 2:** Compute group means and grand mean.
>
> $$\bar{x}_9 = \frac{5+7+6}{3} = 6 \qquad \bar{x}_{10} = \frac{8+10+9+11}{4} = 9.5 \qquad \bar{x}_{11} = \frac{12+14+13}{3} = 13$$
>
> $$\bar{\bar{x}} = \frac{18 + 38 + 39}{10} = \frac{95}{10} = 9.5$$
>
> **Step 3:** Compute $SSB$.
>
> $$SSB = 3(6-9.5)^2 + 4(9.5-9.5)^2 + 3(13-9.5)^2$$
> $$= 3(12.25) + 4(0) + 3(12.25)$$
> $$= 36.75 + 0 + 36.75 = 73.50$$
>
> **Step 4:** Compute $SSW$.
>
> | Group | Values | Deviations | Squared & Summed |
> |:---|:---|:---|:---|
> | Gr 9 ($\bar{x}=6$) | 5,7,6 | −1, 1, 0 | 1+1+0 = 2 |
> | Gr 10 ($\bar{x}=9.5$) | 8,10,9,11 | −1.5, 0.5, −0.5, 1.5 | 2.25+0.25+0.25+2.25 = 5 |
> | Gr 11 ($\bar{x}=13$) | 12,14,13 | −1, 1, 0 | 1+1+0 = 2 |
>
> $$SSW = 2 + 5 + 2 = 9$$
>
> **Step 5:** Build the ANOVA table.
>
> | Source | SS | df | MS | F |
> |:---|:---:|:---:|:---:|:---:|
> | Between | 73.50 | 2 | 36.75 | **28.58** |
> | Within | 9.00 | 7 | 1.286 | |
> | **Total** | 82.50 | 9 | | |
>
> $$F = \frac{36.75}{1.286} = 28.58$$
>
> **Step 6:** Compare.
>
> $$F = 28.58 > F_{\text{critical}} = 4.737$$
>
> **Step 7:** Decision.
>
> $$\boxed{\text{Reject } H_0}$$
>
> **Interpretation:** At the 5% significance level, homework hours differ significantly across grade levels. The large F-value suggests very strong evidence of real differences.

---

### 14. Two-Way ANOVA

**Two-Way ANOVA** extends one-way ANOVA by examining the effect of **two factors** simultaneously on a response variable. It can also detect whether the two factors **interact** — that is, whether the effect of one factor depends on the level of the other.

```
  Two-Way ANOVA — Sources of Variation

  Total Variation (SST)
  ┌─────────────────────────────────────────────────────┐
  │                                                     │
  │  ┌──────────┐  ┌──────────┐  ┌────────────┐  ┌───┐ │
  │  │ Factor A │  │ Factor B │  │ Interaction│  │ E │ │
  │  │  (SSA)   │  │  (SSB)   │  │  (SSAB)    │  │   │ │
  │  │          │  │          │  │            │  │SSE│ │
  │  │ Row      │  │ Column   │  │ A × B      │  │   │ │
  │  │ effect   │  │ effect   │  │ combined   │  │   │ │
  │  └──────────┘  └──────────┘  └────────────┘  └───┘ │
  │                                                     │
  └─────────────────────────────────────────────────────┘

  SST = SSA + SSB + SSAB + SSE
```

**One-Way vs Two-Way ANOVA:**

| Feature               | One-Way ANOVA         | Two-Way ANOVA                                             |
| :-------------------- | :-------------------- | :-------------------------------------------------------- |
| **Number of factors** | 1                     | 2                                                         |
| **Tests**             | Effect of one factor  | Main effect A, main effect B, interaction A×B             |
| **Design**            | $k$ groups            | $a \times b$ cells (rows × columns)                       |
| **Interaction**       | Not applicable        | Yes — can test whether factors combine in unexpected ways |
| **Example**           | 3 fertilizers → yield | 3 fertilizers × 2 soil types → yield                      |

**Three hypotheses tested simultaneously:**

1. $H_{0A}$: Factor A has no effect on the mean ($\mu_{1\cdot} = \mu_{2\cdot} = \cdots$)
2. $H_{0B}$: Factor B has no effect on the mean ($\mu_{\cdot1} = \mu_{\cdot2} = \cdots$)
3. $H_{0AB}$: There is no interaction between Factor A and Factor B

#### Real-World Use Cases

- **Manufacturing**: Testing the effect of _temperature_ (Factor A: 3 levels) and _pressure_ (Factor B: 2 levels) on product strength simultaneously.
- **Medicine**: Studying how _drug type_ (3 drugs) and _dosage level_ (low/high) affect patient recovery time — and whether the drug effect changes at different dosages (interaction).
- **Agriculture**: Examining _fertilizer type_ and _irrigation method_ on crop yield — an interaction would mean a specific fertilizer works especially well with a specific irrigation method.
- **Key Advantage**: More efficient than running two separate one-way ANOVAs because it uses fewer total observations and can detect interactions.

#### Steps

1. Organize data into a table with Factor A as rows and Factor B as columns.
2. State three sets of hypotheses (main effect A, main effect B, interaction).
3. Compute group means: row means ($\bar{x}_{i\cdot}$), column means ($\bar{x}_{\cdot j}$), cell means ($\bar{x}_{ij}$), and grand mean ($\bar{\bar{x}}$).
4. Compute $SSA$, $SSB$, $SSAB$, $SSE$, and $SST$.
5. Compute degrees of freedom for each source.
6. Compute mean squares ($MSA$, $MSB$, $MSAB$, $MSE$).
7. Compute F-statistics: $F_A = MSA/MSE$, $F_B = MSB/MSE$, $F_{AB} = MSAB/MSE$.
8. Compare each F to its critical value. Reject the corresponding $H_0$ if $F \geq F_{\text{critical}}$.

#### Formula

$$
F_A = \frac{MSA}{MSE}, \quad F_B = \frac{MSB}{MSE}, \quad F_{AB} = \frac{MSAB}{MSE}
$$

Where:

$$
SSA = bn \sum_{i=1}^{a} (\bar{x}_{i\cdot} - \bar{\bar{x}})^2
$$

$$
SSB = an \sum_{j=1}^{b} (\bar{x}_{\cdot j} - \bar{\bar{x}})^2
$$

$$
SSAB = n \sum_{i=1}^{a} \sum_{j=1}^{b} (\bar{x}_{ij} - \bar{x}_{i\cdot} - \bar{x}_{\cdot j} + \bar{\bar{x}})^2
$$

$$
SSE = \sum_{i} \sum_{j} \sum_{l} (x_{ijl} - \bar{x}_{ij})^2
$$

|       Symbol        | Pronunciation          | Meaning                              |
| :-----------------: | :--------------------- | :----------------------------------- |
|         $a$         | "a"                    | Number of levels of Factor A         |
|         $b$         | "b"                    | Number of levels of Factor B         |
|         $n$         | "n"                    | Number of replicates per cell        |
| $\bar{x}_{i\cdot}$  | "x bar i dot"          | Mean of row $i$ (across all columns) |
| $\bar{x}_{\cdot j}$ | "x bar dot j"          | Mean of column $j$ (across all rows) |
|   $\bar{x}_{ij}$    | "x bar i j"            | Cell mean (row $i$, column $j$)      |
|   $\bar{\bar{x}}$   | "x double bar"         | Grand mean                           |
|        $SSA$        | "sum of squares A"     | Variation due to Factor A            |
|        $SSB$        | "sum of squares B"     | Variation due to Factor B            |
|       $SSAB$        | "sum of squares A B"   | Variation due to the interaction     |
|        $SSE$        | "sum of squares error" | Residual (unexplained) variation     |

**Two-Way ANOVA Summary Table:**

| Source            |   SS   |      df      |   MS   |          F          |
| :---------------- | :----: | :----------: | :----: | :-----------------: |
| Factor A          | $SSA$  |   $a - 1$    | $MSA$  |   $F_A = MSA/MSE$   |
| Factor B          | $SSB$  |   $b - 1$    | $MSB$  |   $F_B = MSB/MSE$   |
| Interaction (A×B) | $SSAB$ | $(a-1)(b-1)$ | $MSAB$ | $F_{AB} = MSAB/MSE$ |
| Error             | $SSE$  |  $ab(n-1)$   | $MSE$  |                     |
| **Total**         | $SST$  |  $abn - 1$   |        |                     |

#### Examples

---

##### Example 1 — Two-Way ANOVA (No Interaction)

An engineer tests 2 materials (Factor A: Steel, Aluminum) at 2 temperatures (Factor B: 100°C, 200°C). Each combination is tested 3 times. Response: tensile strength (MPa).

|              |   100°C    |   200°C    |
| :----------- | :--------: | :--------: |
| **Steel**    | 50, 52, 48 | 60, 58, 62 |
| **Aluminum** | 40, 42, 38 | 45, 47, 43 |

Test all three hypotheses at $\alpha = 0.05$.

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $a = 2$ (Steel, Aluminum) | Levels of Factor A |
> | $b = 2$ (100°C, 200°C) | Levels of Factor B |
> | $n = 3$ | Replicates per cell |
> | $N = abn = 12$ | Total observations |
> | $\alpha = 0.05$ | Significance level |
> | Find: Which effects are significant? | |

> **Step 1:** Compute cell means, row means, column means, and grand mean.
>
> | | 100°C | 200°C | Row Mean |
> |:---|:---:|:---:|:---:|
> | Steel | $\bar{x}_{11}=50$ | $\bar{x}_{12}=60$ | $\bar{x}_{1\cdot}=55$ |
> | Aluminum | $\bar{x}_{21}=40$ | $\bar{x}_{22}=45$ | $\bar{x}_{2\cdot}=42.5$ |
> | **Col Mean** | $\bar{x}_{\cdot1}=45$ | $\bar{x}_{\cdot2}=52.5$ | $\bar{\bar{x}}=48.75$ |
>
> **Step 2:** Compute $SSA$ (Factor A: Material).
>
> $$SSA = bn \sum_{i=1}^{a}(\bar{x}_{i\cdot} - \bar{\bar{x}})^2 = (2)(3)[(55-48.75)^2 + (42.5-48.75)^2]$$
> $$= 6[39.0625 + 39.0625] = 6(78.125) = 468.75$$
>
> **Step 3:** Compute $SSB$ (Factor B: Temperature).
>
> $$SSB = an \sum_{j=1}^{b}(\bar{x}_{\cdot j} - \bar{\bar{x}})^2 = (2)(3)[(45-48.75)^2 + (52.5-48.75)^2]$$
> $$= 6[14.0625 + 14.0625] = 6(28.125) = 168.75$$
>
> **Step 4:** Compute $SSAB$ (Interaction).
>
> $$SSAB = n \sum_{i}\sum_{j}(\bar{x}_{ij} - \bar{x}_{i\cdot} - \bar{x}_{\cdot j} + \bar{\bar{x}})^2$$
>
> | Cell | $\bar{x}_{ij} - \bar{x}_{i\cdot} - \bar{x}_{\cdot j} + \bar{\bar{x}}$ | Squared |
> |:---|:---:|:---:|
> | Steel, 100°C | $50 - 55 - 45 + 48.75 = -1.25$ | 1.5625 |
> | Steel, 200°C | $60 - 55 - 52.5 + 48.75 = 1.25$ | 1.5625 |
> | Alum, 100°C | $40 - 42.5 - 45 + 48.75 = 1.25$ | 1.5625 |
> | Alum, 200°C | $45 - 42.5 - 52.5 + 48.75 = -1.25$ | 1.5625 |
>
> $$SSAB = 3(1.5625 + 1.5625 + 1.5625 + 1.5625) = 3(6.25) = 18.75$$
>
> **Step 5:** Compute $SSE$.
>
> | Cell | Values | Deviations from cell mean | Squared & summed |
> |:---|:---|:---|:---|
> | Steel, 100°C ($\bar{x}=50$) | 50,52,48 | 0,2,−2 | 0+4+4=8 |
> | Steel, 200°C ($\bar{x}=60$) | 60,58,62 | 0,−2,2 | 0+4+4=8 |
> | Alum, 100°C ($\bar{x}=40$) | 40,42,38 | 0,2,−2 | 0+4+4=8 |
> | Alum, 200°C ($\bar{x}=45$) | 45,47,43 | 0,2,−2 | 0+4+4=8 |
>
> $$SSE = 8+8+8+8 = 32$$
>
> **Step 6:** Build the ANOVA table.
>
> | Source | SS | df | MS | F |
> |:---|:---:|:---:|:---:|:---:|
> | Material (A) | 468.75 | 1 | 468.75 | **117.19** |
> | Temperature (B) | 168.75 | 1 | 168.75 | **42.19** |
> | Interaction (A×B) | 18.75 | 1 | 18.75 | **4.69** |
> | Error | 32.00 | 8 | 4.00 | |
> | **Total** | 688.25 | 11 | | |
>
> Critical values ($\alpha = 0.05$, $df_1=1$, $df_2=8$): $F_{\text{critical}} = 5.318$
>
> **Step 7:** Decisions.
>
> | Effect | F | $F_{\text{critical}}$ | Decision |
> |:---|:---:|:---:|:---|
> | Material (A) | 117.19 | 5.318 | $\boxed{\text{Reject } H_{0A}}$ — Material has a significant effect |
> | Temperature (B) | 42.19 | 5.318 | $\boxed{\text{Reject } H_{0B}}$ — Temperature has a significant effect |
> | Interaction (A×B) | 4.69 | 5.318 | $\text{Fail to reject } H_{0AB}$ — No significant interaction |
>
> **Interpretation:** Both material type and temperature significantly affect tensile strength. However, there is no significant interaction — the temperature effect is similar for both materials.

---

##### Example 2 — Two-Way ANOVA (With Interaction)

A food scientist tests 2 cooking methods (Factor A: Baked, Fried) and 2 seasonings (Factor B: Salt, Pepper) on taste ratings (1–10 scale). Each combination tested twice ($n=2$).

|           | Salt  | Pepper |
| :-------- | :---: | :----: |
| **Baked** | 6, 8  |  4, 5  |
| **Fried** | 5, 7  |  8, 9  |

> **Given:**
>
> | Key Value | Description |
> |:---|:---|
> | $a = 2$, $b = 2$, $n = 2$ | Design: 2×2 with 2 replicates |
> | $N = 8$ | Total observations |
> | $\alpha = 0.05$ | Significance level |
> | Find: Which effects are significant? | |

> **Step 1:** Compute means.
>
> | | Salt | Pepper | Row Mean |
> |:---|:---:|:---:|:---:|
> | Baked | $\bar{x}_{11}=7$ | $\bar{x}_{12}=4.5$ | $\bar{x}_{1\cdot}=5.75$ |
> | Fried | $\bar{x}_{21}=6$ | $\bar{x}_{22}=8.5$ | $\bar{x}_{2\cdot}=7.25$ |
> | **Col Mean** | $\bar{x}_{\cdot1}=6.5$ | $\bar{x}_{\cdot2}=6.5$ | $\bar{\bar{x}}=6.5$ |
>
> **Step 2:** Compute sums of squares.
>
> $$SSA = bn\sum(\bar{x}_{i\cdot}-\bar{\bar{x}})^2 = (2)(2)[(5.75-6.5)^2+(7.25-6.5)^2]$$
> $$= 4[0.5625+0.5625] = 4.50$$
>
> $$SSB = an\sum(\bar{x}_{\cdot j}-\bar{\bar{x}})^2 = (2)(2)[(6.5-6.5)^2+(6.5-6.5)^2] = 0$$
>
> Interaction terms:
>
> | Cell | $\bar{x}_{ij}-\bar{x}_{i\cdot}-\bar{x}_{\cdot j}+\bar{\bar{x}}$ | Squared |
> |:---|:---:|:---:|
> | Baked, Salt | $7-5.75-6.5+6.5 = 1.25$ | 1.5625 |
> | Baked, Pepper | $4.5-5.75-6.5+6.5 = -1.25$ | 1.5625 |
> | Fried, Salt | $6-7.25-6.5+6.5 = -1.25$ | 1.5625 |
> | Fried, Pepper | $8.5-7.25-6.5+6.5 = 1.25$ | 1.5625 |
>
> $$SSAB = 2(1.5625 \times 4) = 12.50$$
>
> $SSE$ (within-cell variation):
>
> | Cell | Values | Dev from cell mean | Squared sum |
> |:---|:---|:---|:---|
> | Baked, Salt ($\bar{x}=7$) | 6, 8 | −1, 1 | 2 |
> | Baked, Pepper ($\bar{x}=4.5$) | 4, 5 | −0.5, 0.5 | 0.5 |
> | Fried, Salt ($\bar{x}=6$) | 5, 7 | −1, 1 | 2 |
> | Fried, Pepper ($\bar{x}=8.5$) | 8, 9 | −0.5, 0.5 | 0.5 |
>
> $$SSE = 2 + 0.5 + 2 + 0.5 = 5.00$$
>
> **Step 3:** ANOVA table.
>
> | Source | SS | df | MS | F |
> |:---|:---:|:---:|:---:|:---:|
> | Cooking (A) | 4.50 | 1 | 4.50 | **3.60** |
> | Seasoning (B) | 0.00 | 1 | 0.00 | **0.00** |
> | Interaction (A×B) | 12.50 | 1 | 12.50 | **10.00** |
> | Error | 5.00 | 4 | 1.25 | |
> | **Total** | 22.00 | 7 | | |
>
> Critical value ($\alpha = 0.05$, $df_1=1$, $df_2=4$): $F_{\text{critical}} = 7.709$
>
> **Step 4:** Decisions.
>
> | Effect | F | $F_{\text{critical}}$ | Decision |
> |:---|:---:|:---:|:---|
> | Cooking (A) | 3.60 | 7.709 | Fail to reject $H_{0A}$ — Cooking method alone is not significant |
> | Seasoning (B) | 0.00 | 7.709 | Fail to reject $H_{0B}$ — Seasoning alone is not significant |
> | Interaction (A×B) | 10.00 | 7.709 | $\boxed{\text{Reject } H_{0AB}}$ — Significant interaction |
>
> **Interpretation:** Neither cooking method nor seasoning alone significantly affects taste ratings. However, the **interaction is significant** — this means the best seasoning depends on which cooking method is used. Baked food tastes better with salt (7 vs 4.5), while fried food tastes better with pepper (8.5 vs 6). This is a classic _crossover interaction_.

---

### 15. Applications in Engineering Research

This section ties together all the statistical methods covered in this unit into a practical **decision framework** for engineering research and design.

#### Choosing the Right Test — Decision Flowchart

```
  What Are You Trying to Do?
  │
  ├── Estimate a parameter? ─── → Estimation & Confidence Intervals (Sections 7–9)
  │
  └── Test a claim about a population?
      │
      ├── How many groups?
      │   ├── 1 group ─── → Z-test or t-test (Section 11)
      │   ├── 2 groups ─── → Two-sample t-test or Mann-Whitney U (Sections 11–12)
      │   └── 3+ groups ─── → ANOVA (Sections 13–14)
      │
      ├── How many factors?
      │   ├── 1 factor ─── → One-Way ANOVA (Section 13)
      │   └── 2 factors ─── → Two-Way ANOVA (Section 14)
      │
      └── Is data normal?
          ├── YES ─── → Parametric tests
          └── NO ──── → Non-parametric tests (Section 12)
```

#### Quick Reference — Choosing the Right Test

| Scenario                            | Data Requirements                   | Test           | Section |
| :---------------------------------- | :---------------------------------- | :------------- | :-----: |
| One sample, known $\sigma$          | Continuous, normal (or $n \geq 30$) | Z-test         |   11    |
| One sample, unknown $\sigma$        | Continuous, approximately normal    | t-test         |   11    |
| Comparing frequencies to expected   | Categorical counts                  | Chi-Square     |   12    |
| Comparing 2 groups, non-normal data | Ordinal or non-normal               | Mann-Whitney U |   12    |
| Comparing 3+ groups, 1 factor       | Continuous, normal, equal variances | One-Way ANOVA  |   13    |
| Comparing groups across 2 factors   | Continuous, normal, equal variances | Two-Way ANOVA  |   14    |

#### End-to-End Workflow for Engineering Research

```
  Engineering Research Statistical Workflow

  Step 1: Define the Research Question
  ┌──────────────────────────────────┐
  │ "Does temperature affect the     │
  │  tensile strength of alloy X?"   │
  └─────────────┬────────────────────┘
                │
  Step 2: Design the Experiment
  ┌─────────────▼────────────────────┐
  │ Choose factors, levels, sample   │
  │ sizes, and randomization method  │
  └─────────────┬────────────────────┘
                │
  Step 3: Collect Data
  ┌─────────────▼────────────────────┐
  │ Run experiments, record results  │
  └─────────────┬────────────────────┘
                │
  Step 4: Check Assumptions
  ┌─────────────▼────────────────────┐
  │ Normality? Equal variances?      │
  │ → Choose parametric or           │
  │   non-parametric test            │
  └─────────────┬────────────────────┘
                │
  Step 5: Perform the Test
  ┌─────────────▼────────────────────┐
  │ Compute test statistic, p-value  │
  │ Compare to α                     │
  └─────────────┬────────────────────┘
                │
  Step 6: Interpret & Report
  ┌─────────────▼────────────────────┐
  │ State conclusion in context      │
  │ Include confidence intervals     │
  │ Discuss practical significance   │
  └──────────────────────────────────┘
```

#### Key Reminders for Engineering Applications

- **Statistical significance ≠ practical significance**: A p-value of 0.04 means the result is unlikely under $H_0$, but the actual difference might be too small to matter in engineering. Always report **effect sizes** alongside p-values.
- **Sample size matters**: Power analysis _before_ the experiment helps ensure you have enough observations to detect a meaningful effect.
- **Assumptions come first**: Always check normality and equal variances before choosing a test. Violating assumptions can invalidate results.
- **Reproducibility**: Document your experimental procedure, analysis method, and significance level chosen _before_ collecting data to avoid p-hacking.

---

<p align="left">
  <a href="./hypothesis-testing.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="../unit_3/index.md"><b>Next →</b></a>
  </span>
</p>
