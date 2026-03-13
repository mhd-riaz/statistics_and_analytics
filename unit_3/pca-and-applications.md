<p align="left">
  <a href="./vector-spaces-and-eigen.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="../unit_4/index.md"><b>Next →</b></a>
  </span>
</p>

---

# Covariance Analysis & PCA

```
Covariance Analysis & PCA
├── 8. Covariance Matrices
│   ├── Review: covariance between two variables
│   ├── Constructing the covariance matrix
│   ├── Properties of covariance matrices
│   └── Correlation matrix as standardised covariance
│
├── 9. Principal Component Analysis (PCA)
│   ├── Motivation and intuition
│   ├── PCA via eigendecomposition
│   ├── Choosing the number of components
│   └── Interpreting principal components
│
└── 10. Applications of Linear Algebra in Engineering
    ├── Structural and mechanical engineering
    ├── Electrical engineering and signal processing
    ├── Machine learning and data science
    └── Computer graphics and image processing
```

---

### 8. Covariance Matrices

The **covariance matrix** (also called the _variance-covariance matrix_) generalises the concept of variance and covariance to multiple variables simultaneously. For a dataset with $p$ variables, the covariance matrix is a $p \times p$ symmetric matrix that captures all pairwise relationships.

```
Covariance Matrix Structure (3 variables):

         X₁        X₂        X₃
     ┌─────────┬─────────┬─────────┐
X₁   │ Var(X₁) │Cov(X₁,X₂)│Cov(X₁,X₃)│
     ├─────────┼─────────┼─────────┤
X₂   │Cov(X₂,X₁)│ Var(X₂) │Cov(X₂,X₃)│
     ├─────────┼─────────┼─────────┤
X₃   │Cov(X₃,X₁)│Cov(X₃,X₂)│ Var(X₃) │
     └─────────┴─────────┴─────────┘

Main diagonal  = variances (always ≥ 0)
Off-diagonal   = covariances (can be negative)
Symmetric:  Cov(Xᵢ,Xⱼ) = Cov(Xⱼ,Xᵢ)
```

#### Review: Covariance Between Two Variables

The **sample covariance** between variables $X$ and $Y$:

$$
\text{Cov}(X, Y) = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})
$$

Where:

|       Symbol       | Pronunciation           | Meaning                                   |
| :----------------: | :---------------------- | :---------------------------------------- |
| $\text{Cov}(X, Y)$ | "covariance of X and Y" | How much $X$ and $Y$ vary together        |
|     $x_i, y_i$     | "x sub i, y sub i"      | The $i$-th observation of each variable   |
| $\bar{x}, \bar{y}$ | "x bar, y bar"          | Sample means                              |
|      $n - 1$       | "n minus 1"             | Bessel's correction for sample covariance |

**Key identity:** $\text{Var}(X) = \text{Cov}(X, X)$

#### Constructing the Covariance Matrix

For $p$ variables measured on $n$ observations, the **sample covariance matrix** $S$ is:

$$
S = \frac{1}{n-1} (X_c)^T X_c
$$

Where $X_c$ is the **mean-centred** data matrix (each column has its mean subtracted):

$$
(X_c)_{ij} = x_{ij} - \bar{x}_j
$$

The entry at position $(i, j)$ of $S$ is $\text{Cov}(X_i, X_j)$.

Where:

|   Symbol    | Pronunciation | Meaning                                   |
| :---------: | :------------ | :---------------------------------------- |
|     $S$     | "S"           | The $p \times p$ sample covariance matrix |
|    $X_c$    | "X centred"   | The $n \times p$ mean-centred data matrix |
| $\bar{x}_j$ | "x bar sub j" | Mean of the $j$-th variable               |

#### Properties of Covariance Matrices

| Property                   | Description                                          |
| :------------------------- | :--------------------------------------------------- |
| **Symmetric**              | $S = S^T$ — covariance is commutative                |
| **Positive semi-definite** | All eigenvalues $\geq 0$                             |
| **Diagonal**               | Main diagonal entries are variances                  |
| **Dimension**              | $p \times p$ for $p$ variables, regardless of $n$    |
| **Related to correlation** | $r_{ij} = \frac{S_{ij}}{\sqrt{S_{ii} \cdot S_{jj}}}$ |

#### Correlation Matrix as Standardised Covariance

The **correlation matrix** $R$ is obtained by standardising the covariance matrix:

$$
R = D^{-1} S D^{-1}
$$

Where $D = \text{diag}(\sigma_1, \sigma_2, \ldots, \sigma_p)$ is the diagonal matrix of standard deviations.

| Covariance Matrix ($S$)         | Correlation Matrix ($R$)                 |
| :------------------------------ | :--------------------------------------- |
| Units depend on variables       | Unitless (always $-1$ to $+1$)           |
| Diagonal = variances            | Diagonal = 1s                            |
| Affected by scale               | Scale-invariant                          |
| Used when variables share units | Used when variables have different units |

#### Population vs Sample Notation

| Quantity           | Population Notation                          | Sample Notation                                    | Meaning                          |
| :----------------- | :------------------------------------------- | :------------------------------------------------- | :------------------------------- |
| Mean               | $\mu$                                        | $\bar{x}$                                          | Central value of a variable      |
| Variance           | $\sigma^2$                                   | $s^2$                                              | Average squared spread           |
| Standard deviation | $\sigma$                                     | $s$                                                | Spread in original units         |
| Size               | $N$                                          | $n$                                                | Number of observations           |
| Covariance         | $\operatorname{Cov}(X,Y)$ with $\frac{1}{N}$ | $s_{XY}$ or sample covariance with $\frac{1}{n-1}$ | Joint variation of two variables |

For sample covariance and sample variance, the denominator $n-1$ is **Bessel's correction**, which reduces the downward bias that appears when population parameters are estimated from a sample.

#### Real-World Use Cases

- **Finance (Portfolio Theory)**: The covariance matrix of asset returns determines portfolio risk; Markowitz optimisation minimises portfolio variance.
- **Machine Learning**: Covariance matrices are the input to PCA and Mahalanobis distance calculations.
- **Meteorology**: Covariance between temperature, pressure, and humidity across weather stations.
- **Quality Control**: Monitoring covariance structure detects when manufacturing processes drift.
- **Limitation**: Covariance only captures _linear_ relationships — nonlinear dependencies may not appear.

#### Steps

1. Arrange the dataset so each column represents one variable and each row one observation.
2. Compute the mean of each variable and centre the data by subtracting the corresponding column mean.
3. Use $n-1$ for sample covariance or $N$ for population covariance.
4. Compute every variance and covariance entry to form the full square covariance matrix.
5. If variables are on different scales, convert the covariance matrix to a correlation matrix for comparison.

#### Formula

For sample data, the covariance between two variables and the covariance matrix are:

$$
\operatorname{Cov}(X,Y) = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})
$$

$$
S = \frac{1}{n-1}(X_c)^T X_c
$$

Where:

|          Symbol           | Pronunciation           | Meaning                                           |
| :-----------------------: | :---------------------- | :------------------------------------------------ |
| $\operatorname{Cov}(X,Y)$ | "covariance of X and Y" | Pairwise covariance between variables $X$ and $Y$ |
|            $S$            | "S"                     | Sample covariance matrix                          |
|           $X_c$           | "X centred"             | Mean-centred data matrix                          |
|    $\bar{x}, \bar{y}$     | "x bar, y bar"          | Sample means                                      |
|           $n-1$           | "n minus 1"             | Bessel-corrected sample denominator               |

#### Examples

**Example 1 — Construct a 2×2 covariance matrix by hand**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $X = \{2, 4, 6, 8\}$ | Variable 1 observations |
> | $Y = \{1, 3, 2, 5\}$ | Variable 2 observations |
> | $n = 4$ | Number of observations |
> | Find: Covariance matrix $S$ | The $2 \times 2$ covariance matrix |
>
> **Step 1:** Compute the means.
>
> $\bar{x} = \frac{2+4+6+8}{4} = 5, \quad \bar{y} = \frac{1+3+2+5}{4} = 2.75$
>
> **Step 2:** Build the deviation table.
>
> | $i$ | $x_i$ | $y_i$ | $x_i - \bar{x}$ | $y_i - \bar{y}$ | $(x_i - \bar{x})^2$ | $(y_i - \bar{y})^2$ | $(x_i - \bar{x})(y_i - \bar{y})$ |
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> | 1 | 2 | 1 | $-3$ | $-1.75$ | 9 | 3.0625 | 5.25 |
> | 2 | 4 | 3 | $-1$ | $0.25$ | 1 | 0.0625 | $-0.25$ |
> | 3 | 6 | 2 | $1$ | $-0.75$ | 1 | 0.5625 | $-0.75$ |
> | 4 | 8 | 5 | $3$ | $2.25$ | 9 | 5.0625 | 6.75 |
> | **Sum** | | | | | **20** | **8.75** | **11** |
>
> **Step 3:** Compute each entry using $n - 1 = 3$.
>
> $$\text{Var}(X) = \frac{20}{3} = 6.67, \quad \text{Var}(Y) = \frac{8.75}{3} = 2.92, \quad \text{Cov}(X,Y) = \frac{11}{3} = 3.67$$
>
> **Step 4:** Assemble the covariance matrix.
>
> $$\boxed{S = \begin{bmatrix} 6.67 & 3.67 \\ 3.67 & 2.92 \end{bmatrix}}$$
>
> Positive covariance: $X$ and $Y$ tend to increase together.

**Example 2 — 3×3 covariance matrix + derive the correlation matrix**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | Covariance matrix $S = \begin{bmatrix} 4 & 2 & -1 \\ 2 & 9 & 3 \\ -1 & 3 & 16 \end{bmatrix}$ | Pre-computed $3 \times 3$ covariance matrix |
> | Find: Correlation matrix $R$ | Standardise $S$ to get correlations |
>
> **Step 1:** Extract standard deviations from the diagonal.
>
> $$\sigma_1 = \sqrt{4} = 2, \quad \sigma_2 = \sqrt{9} = 3, \quad \sigma_3 = \sqrt{16} = 4$$
>
> **Step 2:** Compute correlations using $r_{ij} = \frac{S_{ij}}{\sigma_i \cdot \sigma_j}$.
>
> | Pair | $S_{ij}$ | $\sigma_i \cdot \sigma_j$ | $r_{ij}$ |
> |:---:|:---:|:---:|:---:|
> | $(1,2)$ | 2 | $2 \times 3 = 6$ | $0.333$ |
> | $(1,3)$ | $-1$ | $2 \times 4 = 8$ | $-0.125$ |
> | $(2,3)$ | 3 | $3 \times 4 = 12$ | $0.250$ |
>
> **Step 3:** Assemble the correlation matrix.
>
> $$\boxed{R = \begin{bmatrix} 1 & 0.333 & -0.125 \\ 0.333 & 1 & 0.250 \\ -0.125 & 0.250 & 1 \end{bmatrix}}$$
>
> **Step 4:** Interpret.
>
> | Pair | Correlation | Strength | Direction |
> |:---:|:---:|:---|:---|
> | $X_1, X_2$ | $0.333$ | Weak | Positive |
> | $X_1, X_3$ | $-0.125$ | Very weak | Negative |
> | $X_2, X_3$ | $0.250$ | Weak | Positive |
>
> Interpretation scale: $|r| < 0.3$ weak, $0.3 \leq |r| < 0.7$ moderate, $|r| \geq 0.7$ strong.

---

### 9. Principal Component Analysis (PCA)

**Principal Component Analysis (PCA)** is a dimensionality reduction technique that transforms a set of possibly correlated variables into a set of linearly uncorrelated variables called **principal components**. It works by finding the directions (eigenvectors of the covariance matrix) along which the data varies the most.

```
PCA Intuition — Rotating to the Direction of Maximum Variance:

Original axes (X₁, X₂):          Principal components (PC₁, PC₂):
       ▲ X₂                              ▲ PC₂
       │    ·  ·                          │
       │  ·  ·  ·  ·                     │  ·
       │·  ·  ·  ·  ·                 ·  ·  ·  ·
       │  ·  ·  ·                     ·  ·  ·  ·  ·
       │ ·  ·                         ·  ·  ·  ·
       ┼──────────► X₁                ·  ·  ·
                                      ┼──────────────► PC₁
Correlated data                    Uncorrelated — variance
(elliptical cloud)                 is maximised along PC₁

PC₁ = direction of maximum variance (largest eigenvalue)
PC₂ = orthogonal to PC₁ (second largest eigenvalue)
```

#### Motivation

| Problem                     | How PCA Helps                                       |
| :-------------------------- | :-------------------------------------------------- |
| **High-dimensional data**   | Reduces dimensions while retaining most information |
| **Correlated features**     | Produces uncorrelated components                    |
| **Visualisation**           | Projects data to 2D/3D for plotting                 |
| **Noise reduction**         | Discards low-variance components (likely noise)     |
| **Curse of dimensionality** | Fewer dimensions → faster, more stable models       |

#### Real-World Use Cases

- **Image Compression**: Eigenfaces — representing faces as linear combinations of principal components.
- **Genomics**: Reducing thousands of gene expression variables to a few principal components that capture population structure.
- **Finance**: Reducing correlated asset returns to a few "market factors" (e.g., market risk, size, value).
- **Sensor Networks**: Combining readings from many correlated sensors into a few independent signals.
- **Limitation**: PCA captures only _linear_ relationships. For nonlinear data, use kernel PCA or t-SNE.
- **Limitation**: PCA is sensitive to the _scale_ of variables — always standardise first if variables have different units.

#### Steps

1. **Standardise** the data (subtract mean, divide by standard deviation) if variables have different units.
2. **Compute** the covariance matrix $S$ of the standardised data.
3. **Find** the eigenvalues $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_p$ and corresponding eigenvectors of $S$.
4. **Sort** eigenvectors by decreasing eigenvalue — these are the principal components.
5. **Choose** how many components $k$ to keep (using cumulative explained variance or a scree plot).
6. **Project** the data onto the $k$ principal components: $Z = X_c W_k$ where $W_k$ contains the top $k$ eigenvectors as columns.

#### Formula

**Explained variance ratio** for the $i$-th principal component:

$$
\text{EVR}_i = \frac{\lambda_i}{\sum_{j=1}^{p} \lambda_j}
$$

**Cumulative explained variance** for $k$ components:

$$
\text{CEV}_k = \frac{\sum_{i=1}^{k} \lambda_i}{\sum_{j=1}^{p} \lambda_j}
$$

**Projection** onto principal components:

$$
Z = X_c W_k
$$

Where:

|     Symbol     | Pronunciation                   | Meaning                                                     |
| :------------: | :------------------------------ | :---------------------------------------------------------- |
|  $\lambda_i$   | "lambda sub i"                  | The $i$-th eigenvalue (variance captured by PC $i$)         |
| $\text{EVR}_i$ | "explained variance ratio"      | Proportion of total variance explained by PC $i$            |
| $\text{CEV}_k$ | "cumulative explained variance" | Total proportion of variance retained by the first $k$ PCs  |
|     $X_c$      | "X centred"                     | The $n \times p$ mean-centred (or standardised) data matrix |
|     $W_k$      | "W sub k"                       | The $p \times k$ matrix of the top $k$ eigenvectors         |
|      $Z$       | "Z"                             | The $n \times k$ matrix of projected data (scores)          |

#### Choosing the Number of Components

| Method                  | Rule                                                                        |
| :---------------------- | :-------------------------------------------------------------------------- |
| **Cumulative variance** | Keep enough PCs to reach 80–95% of total variance                           |
| **Kaiser's rule**       | Keep PCs with eigenvalue $> 1$ (for correlation matrix PCA)                 |
| **Scree plot**          | Plot eigenvalues in order; look for an "elbow" and keep PCs before the drop |

```
Scree Plot:

Eigenvalue
λ  │
5 ─┤  ●
   │    ╲
4 ─┤     ╲
   │       ╲
3 ─┤        ●                 ← "Elbow" here
   │           ╲                 Keep PC₁ and PC₂
1 ─┤             ●──●──●──●
   │
0 ─┼──┬──┬──┬──┬──┬──┬──►
      PC₁ PC₂ PC₃ PC₄ PC₅ PC₆
```

#### Examples

**Example 1 — Full PCA on a 2D dataset**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | 5 observations, 2 variables | Small dataset |
> | Data: $(1,2), (2,3), (3,5), (4,4), (5,6)$ | Raw observations |
> | Find: Principal components | Full PCA procedure |
>
> **Step 1:** Compute means and centre the data.
>
> $\bar{x}_1 = 3, \quad \bar{x}_2 = 4$
>
> | $i$ | $x_1$ | $x_2$ | $x_1 - 3$ | $x_2 - 4$ |
> |:---:|:---:|:---:|:---:|:---:|
> | 1 | 1 | 2 | $-2$ | $-2$ |
> | 2 | 2 | 3 | $-1$ | $-1$ |
> | 3 | 3 | 5 | $0$ | $1$ |
> | 4 | 4 | 4 | $1$ | $0$ |
> | 5 | 5 | 6 | $2$ | $2$ |
>
> **Step 2:** Compute the covariance matrix.
>
> | Entry | Computation | Value |
> |:---:|:---|:---:|
> | $S_{11}$ | $\frac{(-2)^2+(-1)^2+0^2+1^2+2^2}{4} = \frac{10}{4}$ | $2.5$ |
> | $S_{22}$ | $\frac{(-2)^2+(-1)^2+1^2+0^2+2^2}{4} = \frac{10}{4}$ | $2.5$ |
> | $S_{12}$ | $\frac{(-2)(-2)+(-1)(-1)+(0)(1)+(1)(0)+(2)(2)}{4} = \frac{9}{4}$ | $2.25$ |
>
> $$S = \begin{bmatrix} 2.5 & 2.25 \\ 2.25 & 2.5 \end{bmatrix}$$
>
> **Step 3:** Find eigenvalues via the characteristic equation.
>
> $$\det(S - \lambda I) = (2.5 - \lambda)^2 - 2.25^2 = \lambda^2 - 5\lambda + 1.1875 = 0$$
>
> Using the quadratic formula:
>
> $$\lambda = \frac{5 \pm \sqrt{25 - 4.75}}{2} = \frac{5 \pm \sqrt{20.25}}{2} = \frac{5 \pm 4.5}{2}$$
>
> $$\lambda_1 = 4.75, \quad \lambda_2 = 0.25$$
>
> **Step 4:** Compute explained variance.
>
> | PC | Eigenvalue | EVR | Cumulative |
> |:---:|:---:|:---:|:---:|
> | PC₁ | $4.75$ | $\frac{4.75}{5} = 95\%$ | $95\%$ |
> | PC₂ | $0.25$ | $\frac{0.25}{5} = 5\%$ | $100\%$ |
>
> **Step 5:** Find eigenvector for $\lambda_1 = 4.75$.
>
> $(S - 4.75I)\mathbf{v} = \mathbf{0}$:
>
> $$\begin{bmatrix} -2.25 & 2.25 \\ 2.25 & -2.25 \end{bmatrix}\mathbf{v} = \mathbf{0} \implies v_1 = v_2$$
>
> Normalised: $\mathbf{w}_1 = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 \\ 1 \end{bmatrix} \approx \begin{bmatrix} 0.707 \\ 0.707 \end{bmatrix}$
>
> $$\boxed{\text{PC}_1 \text{ explains 95\% of variance, direction } \mathbf{w}_1 = \frac{1}{\sqrt{2}}(1, 1)^T}$$
>
> Reducing from 2D to 1D retains 95% of the information — only 5% lost.

**Example 2 — PCA decision using eigenvalues from a 4-variable dataset**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | Covariance matrix eigenvalues: $\lambda_1 = 8.2,\ \lambda_2 = 3.5,\ \lambda_3 = 0.8,\ \lambda_4 = 0.1$ | From a 4-variable dataset |
> | Total variance: $\sum \lambda = 12.6$ | Sum of all eigenvalues |
> | Find: How many components to retain? | Apply variance threshold and Kaiser's rule |
>
> **Step 1:** Compute the explained variance for each component.
>
> | PC | Eigenvalue $\lambda$ | EVR | Cumulative EVR |
> |:---:|:---:|:---:|:---:|
> | PC₁ | 8.2 | $\frac{8.2}{12.6} = 65.1\%$ | $65.1\%$ |
> | PC₂ | 3.5 | $\frac{3.5}{12.6} = 27.8\%$ | $92.9\%$ |
> | PC₃ | 0.8 | $\frac{0.8}{12.6} = 6.3\%$ | $99.2\%$ |
> | PC₄ | 0.1 | $\frac{0.1}{12.6} = 0.8\%$ | $100\%$ |
>
> **Step 2:** Apply selection criteria.
>
> | Criterion | Result | Components to Keep |
> |:---|:---|:---:|
> | **90% cumulative variance** | 92.9% reached at PC₂ | $k = 2$ |
> | **95% cumulative variance** | 99.2% reached at PC₃ | $k = 3$ |
> | **Kaiser's rule** ($\lambda > 1$) | $\lambda_1 = 8.2$, $\lambda_2 = 3.5$ qualify | $k = 2$ |
> | **Scree elbow** | Drop after $\lambda_2$ | $k = 2$ |
>
> **Step 3:** Recommendation.
>
> $$\boxed{k = 2 \text{ principal components — retains 92.9\% of variance, reduces from 4D to 2D}}$$
>
> By keeping only 2 components instead of 4, we reduce our feature space by 50% while losing only 7.1% of the information — a strong trade-off.

---

### 10. Applications of Linear Algebra in Engineering

Linear algebra is not an isolated mathematical discipline — it is the **computational engine** behind virtually every modern engineering and scientific application. This section surveys the key domains where the concepts from Sections 1–9 appear in practice.

```
Linear Algebra in the Engineering Pipeline:

Real-World Problem
     │
     ▼
┌──────────────────┐
│ Model as          │    Systems of equations (Sec 1)
│ Matrix Equation   │    Matrix operations (Sec 2)
│ Ax = b            │
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Solve / Analyse   │    RREF & Gaussian elim (Sec 4)
│ the System        │    Determinants (Sec 3)
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Understand         │    Eigenvalues (Sec 7)
│ System Behaviour   │    Vector spaces (Sec 5-6)
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Reduce & Optimise │    Covariance matrices (Sec 8)
│ High-Dim Data     │    PCA (Sec 9)
└──────────────────┘
```

#### Structural and Mechanical Engineering

| Application                     | Linear Algebra Concept      | Example                                                    |
| :------------------------------ | :-------------------------- | :--------------------------------------------------------- |
| **Truss analysis**              | Systems of equations        | Solving for unknown forces at each joint                   |
| **Finite Element Method (FEM)** | Large sparse matrix systems | Stiffness matrix $K\mathbf{u} = \mathbf{f}$                |
| **Vibration analysis**          | Eigenvalues & eigenvectors  | Natural frequencies = eigenvalues of mass-stiffness system |
| **Modal analysis**              | Eigendecomposition          | Mode shapes = eigenvectors                                 |
| **Stress/strain**               | Matrix operations           | Stress tensor is a $3 \times 3$ symmetric matrix           |

#### Electrical Engineering and Signal Processing

| Application           | Linear Algebra Concept | Example                                               |
| :-------------------- | :--------------------- | :---------------------------------------------------- |
| **Circuit analysis**  | Systems of equations   | Kirchhoff's laws → $A\mathbf{i} = \mathbf{v}$         |
| **Digital filters**   | Matrix multiplication  | Convolution = matrix-vector product (Toeplitz matrix) |
| **Fourier Transform** | Change of basis        | DFT matrix transforms time-domain to frequency-domain |
| **Control systems**   | Eigenvalues            | Stability determined by eigenvalues of system matrix  |
| **Antenna arrays**    | Eigenvectors           | Beamforming = finding the dominant eigenvector        |

#### Machine Learning and Data Science

| Application                            | Linear Algebra Concept           | Example                                                       |
| :------------------------------------- | :------------------------------- | :------------------------------------------------------------ |
| **Linear regression**                  | Matrix inverse, least squares    | $\hat{\beta} = (X^TX)^{-1}X^T\mathbf{y}$                      |
| **PCA**                                | Eigendecomposition of covariance | Dimensionality reduction                                      |
| **Neural networks**                    | Matrix multiplication            | Forward pass: $\mathbf{h} = \sigma(W\mathbf{x} + \mathbf{b})$ |
| **SVD (Singular Value Decomposition)** | Generalised eigendecomposition   | Recommendation systems, latent semantic analysis              |
| **Clustering (k-means)**               | Distance via matrix norms        | Computing centroids and distances                             |

#### Computer Graphics and Image Processing

| Application                 | Linear Algebra Concept   | Example                                                                                       |
| :-------------------------- | :----------------------- | :-------------------------------------------------------------------------------------------- |
| **Transformations**         | Matrix multiplication    | Rotation: $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ |
| **Projection**              | Projection matrices      | 3D → 2D perspective projection                                                                |
| **Image compression**       | SVD / PCA                | Low-rank approximation of image matrices                                                      |
| **Edge detection**          | Convolution (matrix ops) | Sobel filter = small matrix applied to pixel neighbourhood                                    |
| **Homogeneous coordinates** | Augmented matrices       | Combining rotation, scaling, and translation into one matrix                                  |

#### Real-World Use Cases

- **Aerospace**: Flutter analysis uses eigenvalue computations to determine critical flight speeds where structural vibrations become unstable.
- **Biomedical Engineering**: Brain imaging (fMRI) uses PCA to identify independent brain activity patterns from thousands of voxels.
- **Telecommunications**: MIMO antenna systems use eigenbeamforming (eigendecomposition) to maximise data throughput.
- **Finance**: Risk management uses covariance matrices and eigendecomposition to identify independent risk factors across portfolios.
- **Recommendation Systems**: Netflix/Spotify use matrix factorisation (a form of eigendecomposition) to predict user preferences.

#### Hands-On in Python

The teacher notes include practical linear algebra work in Python. These are the core functions worth knowing for classwork and exams:

| Task                       | Python Tool    | Typical Function or Operator             |
| :------------------------- | :------------- | :--------------------------------------- |
| Matrix creation            | `NumPy`        | `np.array(...)`                          |
| Matrix multiplication      | `NumPy`        | `A @ B` or `np.dot(A, B)`                |
| Determinant                | `NumPy`        | `np.linalg.det(A)`                       |
| Solve linear system        | `NumPy`        | `np.linalg.solve(A, b)`                  |
| Eigenvalues/eigenvectors   | `NumPy`        | `np.linalg.eig(A)`                       |
| QR decomposition (Q and R) | `NumPy`        | `np.linalg.qr(A)`                        |
| PCA from covariance matrix | `NumPy`        | `np.linalg.eig(np.cov(X, rowvar=False))` |
| Applied PCA workflow       | `scikit-learn` | `sklearn.decomposition.PCA`              |

#### Steps

1. Translate the engineering problem into a linear algebra object: vector, matrix, or linear transformation.
2. Choose the right operation: solve $A\mathbf{x}=\mathbf{b}$, compute an inverse, project onto a subspace, or use eigendecomposition.
3. Carry out the matrix computation carefully while checking dimensions and units.
4. Interpret the numerical result in the original engineering context.
5. Validate whether the result is physically meaningful, stable, or computationally efficient.

#### Formula

Many engineering applications reduce to one of these canonical forms:

$$
A\mathbf{x} = \mathbf{b}
$$

$$
\hat{\mathbf{x}} = (A^T A)^{-1}A^T\mathbf{b}
$$

$$
A = PDP^{-1}
$$

Where:

|       Symbol       | Pronunciation   | Meaning                                        |
| :----------------: | :-------------- | :--------------------------------------------- |
|        $A$         | "A"             | System, data, or transformation matrix         |
|    $\mathbf{x}$    | "x vector"      | Unknown state, parameter, or signal vector     |
|    $\mathbf{b}$    | "b vector"      | Observed output, forcing term, or measurements |
| $\hat{\mathbf{x}}$ | "x hat"         | Least-squares estimate                         |
|     $PDP^{-1}$     | "P D P inverse" | Eigendecomposition of a diagonalisable matrix  |

##### Key Formulas Summary

| Domain                 | Formula                                        | Meaning                                            |
| :--------------------- | :--------------------------------------------- | :------------------------------------------------- |
| **Least squares**      | $\hat{\beta} = (X^TX)^{-1}X^T\mathbf{y}$       | Best-fit line/plane through data                   |
| **Eigendecomposition** | $A = PDP^{-1}$                                 | Decompose matrix into eigenvalues and eigenvectors |
| **PCA projection**     | $Z = X_c W_k$                                  | Project data onto top $k$ principal components     |
| **SVD**                | $A = U\Sigma V^T$                              | Generalised decomposition for any matrix           |
| **FEM**                | $K\mathbf{u} = \mathbf{f}$                     | Stiffness × displacement = forces                  |
| **State-space**        | $\dot{\mathbf{x}} = A\mathbf{x} + B\mathbf{u}$ | Dynamic system model in control theory             |

#### Examples

**Example 1 — Circuit analysis as a system of linear equations**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $2i_1 + i_2 = 5$ | Loop equation 1 |
> | $i_1 - i_2 = 1$ | Loop equation 2 |
> | Find: $i_1, i_2$ | Unknown branch currents |
>
> **Step 1:** Write the matrix system.
>
> $$\begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix}\begin{bmatrix} i_1 \\ i_2 \end{bmatrix} = \begin{bmatrix} 5 \\ 1 \end{bmatrix}$$
>
> **Step 2:** Use elimination.
>
> From the second equation: $i_1 = 1 + i_2$
>
> Substitute into the first equation:
>
> $$2(1 + i_2) + i_2 = 5$$
>
> **Step 3:** Simplify.
>
> $$2 + 3i_2 = 5 \implies 3i_2 = 3 \implies i_2 = 1$$
>
> **Step 4:** Back-substitute.
>
> $$i_1 = 1 + i_2 = 2$$
>
> **Step 5:** Final answer.
>
> $$\boxed{i_1 = 2,\ i_2 = 1}$$

**Example 2 — Computer graphics rotation using a matrix transformation**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $R = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ | Rotation matrix for $90^\circ$ counterclockwise |
> | $\mathbf{p} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$ | Original point |
> | Find: $R\mathbf{p}$ | Rotated point |
>
> **Step 1:** Write the matrix-vector product.
>
> $$R\mathbf{p} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}\begin{bmatrix} 2 \\ 1 \end{bmatrix}$$
>
> **Step 2:** Multiply row-by-column.
>
> $$\begin{bmatrix} (0)(2) + (-1)(1) \\ (1)(2) + (0)(1) \end{bmatrix} = \begin{bmatrix} -1 \\ 2 \end{bmatrix}$$
>
> **Step 3:** Interpret the result.
>
> The point $(2,1)$ becomes $(-1,2)$ after a $90^\circ$ counterclockwise rotation.
>
> **Step 4:** Final answer.
>
> $$\boxed{R\mathbf{p} = \begin{bmatrix} -1 \\ 2 \end{bmatrix}}$$

---

<p align="left">
  <a href="./vector-spaces-and-eigen.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="../unit_4/index.md"><b>Next →</b></a>
  </span>
</p>
