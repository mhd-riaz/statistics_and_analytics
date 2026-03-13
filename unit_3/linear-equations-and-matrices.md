<p align="left">
  <a href="./index.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./vector-spaces-and-eigen.md"><b>Next →</b></a>
  </span>
</p>

---

# Linear Equations & Matrices

```
Linear Equations & Matrices
├── 1. Systems of Linear Equations
│   ├── Definition and geometric interpretation
│   ├── Consistent vs inconsistent systems
│   └── Augmented matrix representation
│
├── 2. Matrices and Matrix Operations
│   ├── Matrix notation and types
│   ├── Addition, scalar multiplication, transposition
│   ├── Matrix multiplication
│   └── Inverse of a matrix
│
├── 3. Determinants and Their Properties
│   ├── Definition and computation (2×2, 3×3)
│   ├── Cofactor expansion
│   ├── Properties of determinants
│   └── Cramer's Rule
│
└── 4. Row Reduced Echelon Form (RREF)
    ├── Elementary row operations
    ├── Row echelon form vs RREF
    ├── Gaussian elimination algorithm
    └── Classifying solutions (unique, infinite, none)
```

---

### 1. Systems of Linear Equations

A **system of linear equations** is a collection of two or more linear equations involving the same set of variables. The goal is to find the values of the variables that satisfy _all_ equations simultaneously.

```
System with 2 equations, 2 unknowns:

      y ▲
        │      L₁: x + y = 3
   3 ── │╲                          ● Intersection = Solution
        │  ╲         ╱                (1, 2)
   2 ── │───●──────╱──
        │    ╲   ╱
   1 ── │     ╲╱
        │    ╱ ╲    L₂: 2x − y = 0
        │  ╱    ╲
   0 ──┬┴──┬──┬──┬──► x
        0   1  2  3

One intersection → Unique solution
Parallel lines → No solution (inconsistent)
Same line → Infinitely many solutions
```

A system can be written in **matrix form** as:

$$
A\mathbf{x} = \mathbf{b}
$$

Where:

|    Symbol    | Pronunciation | Meaning                                                             |
| :----------: | :------------ | :------------------------------------------------------------------ |
|     $A$      | "A"           | The coefficient matrix (contains the coefficients of the variables) |
| $\mathbf{x}$ | "x vector"    | The column vector of unknowns                                       |
| $\mathbf{b}$ | "b vector"    | The column vector of constants (right-hand side)                    |

#### Classification of Systems

| Type                         | Description               | Geometric Meaning                                |
| :--------------------------- | :------------------------ | :----------------------------------------------- |
| **Consistent & Independent** | Exactly one solution      | Lines/planes intersect at a single point         |
| **Consistent & Dependent**   | Infinitely many solutions | Lines/planes overlap (identical or share a line) |
| **Inconsistent**             | No solution               | Lines/planes are parallel (never intersect)      |

#### Real-World Use Cases

- **Electrical Engineering**: Solving circuit equations using Kirchhoff's laws — each loop/node equation is a linear equation in unknown currents.
- **Structural Engineering**: Computing forces and moments at joints in truss structures.
- **Economics**: Input-output models (Leontief model) where industries' production depends on each other.
- **Computer Graphics**: Transformations (rotation, scaling, translation) expressed as matrix-vector equations.
- **Limitation**: Only applicable to _linear_ relationships — nonlinear systems require different techniques.

#### Steps

1. Write each equation in standard form ($a_1x_1 + a_2x_2 + \cdots + a_nx_n = b$).
2. Construct the **augmented matrix** $[A \mid \mathbf{b}]$ by placing coefficients and constants into a matrix.
3. Apply **row operations** to reduce the augmented matrix (see Section 4: RREF).
4. Read the solution from the reduced matrix.

#### Formula

The **augmented matrix** for a system of $m$ equations in $n$ unknowns:

$$
[A \mid \mathbf{b}] = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} & \mid & b_1 \\ a_{21} & a_{22} & \cdots & a_{2n} & \mid & b_2 \\ \vdots & \vdots & \ddots & \vdots & \mid & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} & \mid & b_m \end{bmatrix}
$$

Where:

|  Symbol  | Pronunciation | Meaning                                                   |
| :------: | :------------ | :-------------------------------------------------------- |
| $a_{ij}$ | "a sub i j"   | Coefficient of the $j$-th variable in the $i$-th equation |
|  $b_i$   | "b sub i"     | Constant on the right-hand side of the $i$-th equation    |
|   $m$    | "m"           | Number of equations                                       |
|   $n$    | "n"           | Number of unknowns                                        |

#### Examples

**Example 1 — Unique solution (2×2 system)**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $x + y = 5$ | First equation |
> | $2x - y = 1$ | Second equation |
> | Find: $x, y$ | Values satisfying both equations |
>
> **Step 1:** Write the augmented matrix.
>
> $$[A \mid \mathbf{b}] = \begin{bmatrix} 1 & 1 & \mid & 5 \\ 2 & -1 & \mid & 1 \end{bmatrix}$$
>
> **Step 2:** Eliminate $x$ from the second row: $R_2 \leftarrow R_2 - 2R_1$.
>
> $$\begin{bmatrix} 1 & 1 & \mid & 5 \\ 0 & -3 & \mid & -9 \end{bmatrix}$$
>
> **Step 3:** Solve for $y$ from Row 2.
>
> $$-3y = -9 \implies y = 3$$
>
> **Step 4:** Back-substitute into Row 1.
>
> $$x + 3 = 5 \implies x = 2$$
>
> **Step 5:** Final answer.
>
> $$\boxed{x = 2,\ y = 3}$$

**Example 2 — Inconsistent system (no solution)**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $x + 2y = 4$ | First equation |
> | $2x + 4y = 5$ | Second equation |
> | Find: $x, y$ | Values satisfying both equations |
>
> **Step 1:** Write the augmented matrix.
>
> $$[A \mid \mathbf{b}] = \begin{bmatrix} 1 & 2 & \mid & 4 \\ 2 & 4 & \mid & 5 \end{bmatrix}$$
>
> **Step 2:** Eliminate $x$ from Row 2: $R_2 \leftarrow R_2 - 2R_1$.
>
> $$\begin{bmatrix} 1 & 2 & \mid & 4 \\ 0 & 0 & \mid & -3 \end{bmatrix}$$
>
> **Step 3:** Interpret Row 2.
>
> Row 2 reads: $0x + 0y = -3$, which simplifies to $0 = -3$.
>
> This is a **contradiction** — no values of $x$ and $y$ can satisfy this.
>
> **Step 4:** Classify the system.
>
> The second equation $2x + 4y = 5$ is a scalar multiple of the first ($2x + 4y = 8$) with a _different_ constant. The lines are **parallel** and never intersect.
>
> $$\boxed{\text{No solution — inconsistent system}}$$

---

### 2. Matrices and Matrix Operations

A **matrix** is a rectangular array of numbers arranged in rows and columns. Matrices provide a compact way to represent and manipulate systems of linear equations, transformations, and data.

```
Matrix A (2×3):                Matrix B (3×2):
┌─────────────────┐            ┌───────────┐
│  a₁₁  a₁₂  a₁₃  │            │  b₁₁  b₁₂ │
│  a₂₁  a₂₂  a₂₃  │            │  b₂₁  b₂₂ │
└─────────────────┘            │  b₃₁  b₃₂ │
 2 rows × 3 columns            └───────────┘
                                3 rows × 2 columns

Product A × B → Result is 2×2
┌─────────┐
│ c₁₁ c₁₂│   where c₁₁ = a₁₁b₁₁ + a₁₂b₂₁ + a₁₃b₃₁
│ c₂₁ c₂₂│         (row of A) · (column of B)
└─────────┘
```

#### Types of Matrices

| Type                      | Notation     | Description                                          |
| :------------------------ | :----------- | :--------------------------------------------------- |
| **Row matrix**            | $1 \times n$ | Single row                                           |
| **Column matrix**         | $m \times 1$ | Single column                                        |
| **Square matrix**         | $n \times n$ | Same number of rows and columns                      |
| **Rectangular matrix**    | $m \times n$ | Different numbers of rows and columns                |
| **Zero matrix**           | $O$          | All entries are 0                                    |
| **Identity matrix**       | $I_n$        | Square matrix with 1s on the diagonal, 0s elsewhere  |
| **Diagonal matrix**       | $D$          | Square, non-zero entries only on the main diagonal   |
| **Scalar matrix**         | $kI$         | Diagonal matrix with the same scalar on the diagonal |
| **Symmetric matrix**      | $A = A^T$    | Equal to its own transpose                           |
| **Skew-symmetric matrix** | $A^T = -A$   | Transpose equals the negative of the matrix          |
| **Orthogonal matrix**     | $Q^TQ = I$   | Columns and rows are orthonormal                     |
| **Upper triangular**      | $U$          | All entries below the main diagonal are 0            |
| **Lower triangular**      | $L$          | All entries above the main diagonal are 0            |
| **Sparse matrix**         | —            | Most entries are 0                                   |
| **Dense matrix**          | —            | Most entries are non-zero                            |

#### Real-World Use Cases

- **Machine Learning**: Datasets are stored as matrices (rows = observations, columns = features); weight matrices in neural networks.
- **Image Processing**: Images are pixel matrices; filters (kernels) are small matrices applied via convolution.
- **Control Systems**: State-space models use matrices to describe system dynamics ($\dot{x} = Ax + Bu$).
- **Network Analysis**: Adjacency matrices represent connections between nodes in a graph.
- **Limitation**: Matrix multiplication is **not commutative** — $AB \neq BA$ in general.

#### Steps

1. Identify the dimensions of the matrix or matrices involved.
2. Check whether the requested operation is valid: same dimensions for addition, matching inner dimensions for multiplication, square and non-singular for inversion.
3. Apply the corresponding matrix rule entry-by-entry or row-by-column.
4. Simplify the result and verify the dimension of the output matrix.

#### Formula

##### Addition and Scalar Multiplication

Matrices of the **same dimensions** can be added element-wise. Scalar multiplication multiplies every entry by a constant.

$$
A + B = [a_{ij} + b_{ij}], \qquad kA = [k \cdot a_{ij}]
$$

##### Transpose

The **transpose** of an $m \times n$ matrix $A$ is the $n \times m$ matrix $A^T$ obtained by swapping rows and columns.

$$
(A^T)_{ij} = A_{ji}
$$

Where:

|  Symbol  | Pronunciation | Meaning                                                 |
| :------: | :------------ | :------------------------------------------------------ |
|  $A^T$   | "A transpose" | Matrix with rows and columns swapped                    |
| $A_{ji}$ | "A sub j i"   | The entry in row $j$, column $i$ of the original matrix |

**Key properties of transpose:**

| Property         | Formula                 |
| :--------------- | :---------------------- |
| Double transpose | $(A^T)^T = A$           |
| Sum              | $(A + B)^T = A^T + B^T$ |
| Scalar           | $(kA)^T = kA^T$         |
| Product          | $(AB)^T = B^T A^T$      |

##### Matrix Multiplication

For $A$ ($m \times n$) and $B$ ($n \times p$), the product $C = AB$ is an $m \times p$ matrix where:

$$
c_{ij} = \sum_{k=1}^{n} a_{ik} \cdot b_{kj}
$$

Where:

|  Symbol  | Pronunciation | Meaning                                            |
| :------: | :------------ | :------------------------------------------------- |
| $c_{ij}$ | "c sub i j"   | Entry in row $i$, column $j$ of the product matrix |
| $a_{ik}$ | "a sub i k"   | Entry from row $i$ of $A$                          |
| $b_{kj}$ | "b sub k j"   | Entry from column $j$ of $B$                       |
|   $n$    | "n"           | Number of columns in $A$ = number of rows in $B$   |

> **Rule**: $A_{m \times n} \cdot B_{n \times p} = C_{m \times p}$ — the inner dimensions must match.

##### Inverse of a Matrix

A square matrix $A$ is **invertible** (nonsingular) if there exists a matrix $A^{-1}$ such that:

$$
AA^{-1} = A^{-1}A = I
$$

For a $2 \times 2$ matrix:

$$
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}, \qquad A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
$$

Where:

|  Symbol   | Pronunciation     | Meaning                                        |
| :-------: | :---------------- | :--------------------------------------------- |
| $A^{-1}$  | "A inverse"       | The matrix that "undoes" multiplication by $A$ |
| $ad - bc$ | "a d minus b c"   | The determinant of $A$ (must be $\neq 0$)      |
|    $I$    | "identity matrix" | The multiplicative identity for matrices       |

#### Examples

**Example 1 — Matrix multiplication**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ | A $2 \times 2$ matrix |
> | $B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}$ | A $2 \times 2$ matrix |
> | Find: $AB$ | The product of $A$ and $B$ |
>
> **Step 1:** Write the multiplication formula.
>
> $$c_{ij} = \sum_{k=1}^{2} a_{ik} \cdot b_{kj}$$
>
> **Step 2:** Compute each entry of $C = AB$.
>
> | Entry | Computation | Result |
> |:---:|:---|:---:|
> | $c_{11}$ | $(1)(5) + (2)(7) = 5 + 14$ | $19$ |
> | $c_{12}$ | $(1)(6) + (2)(8) = 6 + 16$ | $22$ |
> | $c_{21}$ | $(3)(5) + (4)(7) = 15 + 28$ | $43$ |
> | $c_{22}$ | $(3)(6) + (4)(8) = 18 + 32$ | $50$ |
>
> **Step 3:** Assemble the result.
>
> $$\boxed{AB = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}}$$

**Example 2 — Finding the inverse of a 2×2 matrix**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $A = \begin{bmatrix} 4 & 7 \\ 2 & 6 \end{bmatrix}$ | A $2 \times 2$ matrix |
> | Find: $A^{-1}$ | The inverse of matrix $A$ |
>
> **Step 1:** Compute the determinant.
>
> $$\det(A) = ad - bc = (4)(6) - (7)(2) = 24 - 14 = 10$$
>
> **Step 2:** Check invertibility.
>
> Since $\det(A) = 10 \neq 0$, the matrix is invertible.
>
> **Step 3:** Apply the $2 \times 2$ inverse formula.
>
> $$A^{-1} = \frac{1}{10} \begin{bmatrix} 6 & -7 \\ -2 & 4 \end{bmatrix}$$
>
> **Step 4:** Simplify.
>
> $$\boxed{A^{-1} = \begin{bmatrix} 0.6 & -0.7 \\ -0.2 & 0.4 \end{bmatrix}}$$
>
> **Verification:** $AA^{-1} = \begin{bmatrix} 4 & 7 \\ 2 & 6 \end{bmatrix}\begin{bmatrix} 0.6 & -0.7 \\ -0.2 & 0.4 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I$ ✓

---

### 3. Determinants and Their Properties

The **determinant** is a scalar value that can be computed from the entries of a square matrix. It encodes important information about the matrix: whether it is invertible, how it scales volumes, and the nature of solutions to the associated system of equations.

```
2×2 Determinant — Geometric Meaning:

The determinant of a 2×2 matrix equals the
signed area of the parallelogram formed by
its column vectors.

      ▲ y
      │        ╱(a+c, b+d)
      │      ╱  ╱
      │    ╱  ╱
 (c,d)│  ╱  ╱
      │╱  ╱
      ┼─╱──────────► x
     ╱(a,b)

Area = |ad − bc| = |det(A)|

det > 0 → preserves orientation
det < 0 → reverses orientation
det = 0 → collapses to a line (singular)
```

#### Real-World Use Cases

- **Engineering**: Determining whether a system of equations has a unique solution (non-zero determinant).
- **Physics**: Computing cross products and volumes of parallelepipeds in 3D.
- **Computer Graphics**: Checking whether transformations preserve orientation (positive determinant).
- **Stability Analysis**: The sign and magnitude of determinants in Jacobian matrices indicate system stability.
- **Limitation**: Computing determinants for large matrices ($n > 4$) via cofactor expansion is expensive — $O(n!)$ complexity.

#### Steps

1. For a $2 \times 2$ matrix, apply the formula $ad - bc$ directly.
2. For a $3 \times 3$ matrix, choose a row or column and expand along it using **cofactor expansion**.
3. Compute the minor (determinant of the submatrix) for each entry in the chosen row/column.
4. Apply the **checkerboard sign pattern** ($+, -, +, -, \ldots$).
5. Sum the signed products: entry × cofactor.

#### Formula

**2×2 Determinant:**

$$
\det\begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc
$$

**3×3 Determinant (cofactor expansion along Row 1):**

$$
\det(A) = a_{11}(a_{22}a_{33} - a_{23}a_{32}) - a_{12}(a_{21}a_{33} - a_{23}a_{31}) + a_{13}(a_{21}a_{32} - a_{22}a_{31})
$$

Where:

|           Symbol            | Pronunciation           | Meaning                                                                |
| :-------------------------: | :---------------------- | :--------------------------------------------------------------------- |
|          $\det(A)$          | "determinant of A"      | The scalar value computed from the matrix entries                      |
|          $a_{ij}$           | "a sub i j"             | Entry in row $i$, column $j$                                           |
|          $M_{ij}$           | "M sub i j" (minor)     | Determinant of the submatrix formed by deleting row $i$ and column $j$ |
| $C_{ij} = (-1)^{i+j}M_{ij}$ | "cofactor of a sub i j" | Signed minor                                                           |

**Checkerboard sign pattern (3×3):**

$$
\begin{bmatrix} + & - & + \\ - & + & - \\ + & - & + \end{bmatrix}
$$

#### Properties of Determinants

| Property          | Statement                                                               |
| :---------------- | :---------------------------------------------------------------------- |
| **Identity**      | $\det(I) = 1$                                                           |
| **Transpose**     | $\det(A^T) = \det(A)$                                                   |
| **Product**       | $\det(AB) = \det(A) \cdot \det(B)$                                      |
| **Inverse**       | $\det(A^{-1}) = \frac{1}{\det(A)}$                                      |
| **Scalar**        | $\det(kA) = k^n \det(A)$ for an $n \times n$ matrix                     |
| **Row swap**      | Swapping two rows changes the sign of the determinant                   |
| **Row scaling**   | Multiplying a row by $k$ multiplies the determinant by $k$              |
| **Row addition**  | Adding a multiple of one row to another does not change the determinant |
| **Singular test** | $\det(A) = 0 \iff A$ is not invertible                                  |

#### Cramer's Rule

For a system $A\mathbf{x} = \mathbf{b}$ where $\det(A) \neq 0$, each unknown can be found by:

$$
x_i = \frac{\det(A_i)}{\det(A)}
$$

Where $A_i$ is the matrix formed by replacing the $i$-th column of $A$ with $\mathbf{b}$.

#### Examples

**Example 1 — 2×2 determinant**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $A = \begin{bmatrix} 3 & 8 \\ 4 & 6 \end{bmatrix}$ | A $2 \times 2$ matrix |
> | Find: $\det(A)$ | The determinant |
>
> **Step 1:** Apply the formula $ad - bc$.
>
> $$\det(A) = (3)(6) - (8)(4) = 18 - 32$$
>
> **Step 2:** Compute the result.
>
> $$\boxed{\det(A) = -14}$$
>
> Since $\det(A) \neq 0$, the matrix is **invertible**.

**Example 2 — 3×3 determinant with cofactor expansion**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $A = \begin{bmatrix} 2 & 1 & 3 \\ 0 & 4 & 5 \\ 1 & 0 & 2 \end{bmatrix}$ | A $3 \times 3$ matrix |
> | Find: $\det(A)$ | The determinant using cofactor expansion along Row 1 |
>
> **Step 1:** Write the cofactor expansion along Row 1.
>
> $$\det(A) = a_{11} \cdot C_{11} + a_{12} \cdot C_{12} + a_{13} \cdot C_{13}$$
>
> **Step 2:** Compute each cofactor.
>
> | Term | Entry | Sign | Minor | Cofactor |
> |:---:|:---:|:---:|:---|:---|
> | $a_{11} \cdot C_{11}$ | $2$ | $+$ | $\det\begin{bmatrix} 4 & 5 \\ 0 & 2 \end{bmatrix} = 8 - 0 = 8$ | $+2 \times 8 = 16$ |
> | $a_{12} \cdot C_{12}$ | $1$ | $-$ | $\det\begin{bmatrix} 0 & 5 \\ 1 & 2 \end{bmatrix} = 0 - 5 = -5$ | $-1 \times (-5) = 5$ |
> | $a_{13} \cdot C_{13}$ | $3$ | $+$ | $\det\begin{bmatrix} 0 & 4 \\ 1 & 0 \end{bmatrix} = 0 - 4 = -4$ | $+3 \times (-4) = -12$ |
>
> **Step 3:** Sum the cofactors.
>
> $$\det(A) = 16 + 5 + (-12) = 9$$
>
> $$\boxed{\det(A) = 9}$$
>
> Since $\det(A) = 9 \neq 0$, the matrix is invertible and the system $A\mathbf{x} = \mathbf{b}$ has a **unique solution** for any $\mathbf{b}$.

---

### 4. Row Reduced Echelon Form (RREF)

**Row Reduced Echelon Form (RREF)** is the fully simplified form of an augmented matrix, achieved by applying elementary row operations. It is the systematic way to solve any system of linear equations — known as **Gaussian elimination** (or Gauss-Jordan elimination for RREF).

```
Reduction Pipeline:

Original System         Augmented Matrix         REF               RREF
┌──────────────┐        ┌────────────┐        ┌────────────┐     ┌────────────┐
│ 2x + y = 5   │   →    │ 2  1 │ 5  │   →    │ 1  ½ │ 5/2│  →  │ 1  0 │ 2  │
│ 4x − y = 1   │        │ 4 −1 │ 1  │        │ 0 −3 │ −9 │     │ 0  1 │ 3  │
└──────────────┘        └────────────┘        └────────────┘     └────────────┘
                                                                  x=2, y=3
Row Echelon Form (REF):          RREF (fully reduced):
• Leading 1 in each row           • All REF conditions +
• Each leading 1 is to the        • Leading 1 is the ONLY
  right of the one above            nonzero entry in its column
• Zeros below each leading 1      • Zeros above AND below
```

#### Real-World Use Cases

- **Engineering Analysis**: Systematically solving large systems of equations in circuit analysis, structural mechanics, and fluid flow.
- **Linear Programming**: The simplex method uses pivot operations similar to RREF.
- **Rank Determination**: RREF reveals the rank of a matrix (number of non-zero rows), which tells us the dimension of the solution space.
- **Basis Finding**: RREF identifies pivot and free variables, directly giving a basis for the column space and null space.
- **Advantage over Cramer's Rule**: RREF is computationally efficient — $O(n^3)$ vs $O(n!)$ for determinant-based methods.

#### Steps

1. Write the system as an **augmented matrix** $[A \mid \mathbf{b}]$.
2. Start with the leftmost column and select a nonzero pivot entry.
3. Use row swaps if needed, then scale the pivot row so the leading entry becomes 1.
4. Eliminate entries below the pivot to create REF.
5. Continue column by column until every pivot has a staircase position.
6. Eliminate entries above each pivot to obtain RREF.
7. Read the solution type directly from the reduced matrix.

#### Formula

##### Elementary Row Operations

| Operation           | Notation                    | Description                              |
| :------------------ | :-------------------------- | :--------------------------------------- |
| **Row swap**        | $R_i \leftrightarrow R_j$   | Interchange two rows                     |
| **Row scaling**     | $R_i \leftarrow kR_i$       | Multiply a row by a nonzero constant $k$ |
| **Row replacement** | $R_i \leftarrow R_i + kR_j$ | Add $k$ times row $j$ to row $i$         |

These operations **do not change the solution set** of the system.

The action of an elementary row operation can be written as:

$$
E[A \mid \mathbf{b}] = [EA \mid E\mathbf{b}]
$$

Where:

|    Symbol    | Pronunciation       | Meaning                                     |
| :----------: | :------------------ | :------------------------------------------ |
|     $E$      | "elementary matrix" | A matrix representing one row operation     |
|     $A$      | "A"                 | The coefficient matrix                      |
| $\mathbf{b}$ | "b vector"          | The constants column                        |
|     $EA$     | "E A"               | The matrix after applying the row operation |

In RREF, each pivot entry is 1 and is the only nonzero entry in its column.

#### Comparison: REF vs RREF

| Feature       | Row Echelon Form (REF)        | Reduced Row Echelon Form (RREF) |
| :------------ | :---------------------------- | :------------------------------ |
| Leading entry | Leading 1 in each nonzero row | Leading 1 in each nonzero row   |
| Below pivot   | All zeros                     | All zeros                       |
| Above pivot   | May be nonzero                | **All zeros**                   |
| Uniqueness    | Not unique                    | **Unique** for any given matrix |
| Solve by      | Back-substitution needed      | Read solution directly          |

#### Solution Classification from RREF

| RREF Pattern                                             | Solution Type          | Meaning                                 |
| :------------------------------------------------------- | :--------------------- | :-------------------------------------- |
| Every column has a pivot                                 | **Unique solution**    | Each variable is determined             |
| Fewer pivots than variables                              | **Infinite solutions** | Free variables parametrise the solution |
| Row of form $[0\ 0\ \cdots\ 0\ \mid\ c]$ with $c \neq 0$ | **No solution**        | Contradiction → inconsistent            |

#### Examples

**Example 1 — RREF yielding a unique solution (3×3)**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $x + y + z = 6$ | Equation 1 |
> | $2x + 3y + z = 10$ | Equation 2 |
> | $x + 2y + 2z = 10$ | Equation 3 |
> | Find: $x, y, z$ | Solve by reducing to RREF |
>
> **Step 1:** Write the augmented matrix.
>
> $$\begin{bmatrix} 1 & 1 & 1 & \mid & 6 \\ 2 & 3 & 1 & \mid & 10 \\ 1 & 2 & 2 & \mid & 10 \end{bmatrix}$$
>
> **Step 2:** Eliminate below the first pivot.
>
> $R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - R_1$:
>
> $$\begin{bmatrix} 1 & 1 & 1 & \mid & 6 \\ 0 & 1 & -1 & \mid & -2 \\ 0 & 1 & 1 & \mid & 4 \end{bmatrix}$$
>
> **Step 3:** Eliminate below the second pivot.
>
> $R_3 \leftarrow R_3 - R_2$:
>
> $$\begin{bmatrix} 1 & 1 & 1 & \mid & 6 \\ 0 & 1 & -1 & \mid & -2 \\ 0 & 0 & 2 & \mid & 6 \end{bmatrix}$$
>
> **Step 4:** Scale Row 3: $R_3 \leftarrow \frac{1}{2}R_3$.
>
> $$\begin{bmatrix} 1 & 1 & 1 & \mid & 6 \\ 0 & 1 & -1 & \mid & -2 \\ 0 & 0 & 1 & \mid & 3 \end{bmatrix}$$
>
> **Step 5:** Eliminate above (RREF).
>
> $R_2 \leftarrow R_2 + R_3$, $R_1 \leftarrow R_1 - R_3$:
>
> $$\begin{bmatrix} 1 & 1 & 0 & \mid & 3 \\ 0 & 1 & 0 & \mid & 1 \\ 0 & 0 & 1 & \mid & 3 \end{bmatrix}$$
>
> $R_1 \leftarrow R_1 - R_2$:
>
> $$\begin{bmatrix} 1 & 0 & 0 & \mid & 2 \\ 0 & 1 & 0 & \mid & 1 \\ 0 & 0 & 1 & \mid & 3 \end{bmatrix}$$
>
> **Step 6:** Read the solution directly.
>
> $$\boxed{x = 2,\ y = 1,\ z = 3}$$

**Example 2 — RREF yielding infinitely many solutions (free variable)**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $x + 2y + z = 3$ | Equation 1 |
> | $2x + 4y + 2z = 6$ | Equation 2 |
> | Find: $x, y, z$ | Solve by reducing to RREF |
>
> **Step 1:** Write the augmented matrix.
>
> $$\begin{bmatrix} 1 & 2 & 1 & \mid & 3 \\ 2 & 4 & 2 & \mid & 6 \end{bmatrix}$$
>
> **Step 2:** Eliminate below the first pivot: $R_2 \leftarrow R_2 - 2R_1$.
>
> $$\begin{bmatrix} 1 & 2 & 1 & \mid & 3 \\ 0 & 0 & 0 & \mid & 0 \end{bmatrix}$$
>
> **Step 3:** Identify pivot and free variables.
>
> | Variable | Type | Reason |
> |:---:|:---|:---|
> | $x$ | **Pivot** | Column 1 has a leading 1 |
> | $y$ | **Free** | Column 2 has no pivot |
> | $z$ | **Free** | Column 3 has no pivot |
>
> **Step 4:** Express the pivot variable in terms of free variables.
>
> From Row 1: $x + 2y + z = 3 \implies x = 3 - 2y - z$
>
> Let $y = s$ and $z = t$ (free parameters):
>
> $$\boxed{\begin{cases} x = 3 - 2s - t \\ y = s \\ z = t \end{cases}, \quad s, t \in \mathbb{R}}$$
>
> The system has **infinitely many solutions** parametrised by two free variables — geometrically, the solution is a **plane** in $\mathbb{R}^3$.

---

<p align="left">
  <a href="./index.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./vector-spaces-and-eigen.md"><b>Next →</b></a>
  </span>
</p>
