<p align="left">
  <a href="./linear-equations-and-matrices.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./pca-and-applications.md"><b>Next →</b></a>
  </span>
</p>

---

# Vector Spaces & Eigenanalysis

```
Vector Spaces & Eigenanalysis
├── 5. Vector Spaces and Subspaces
│   ├── Definition and axioms
│   ├── Common examples (ℝⁿ, function spaces)
│   ├── Subspaces (null space, column space, row space)
│   └── Span of a set of vectors
│
├── 6. Linear Independence and Basis
│   ├── Linearly dependent vs independent
│   ├── Basis and dimension
│   ├── Finding a basis via RREF
│   └── Rank-Nullity Theorem
│
└── 7. Eigenvalues and Eigenvectors
    ├── Definition and geometric interpretation
    ├── Characteristic equation
    ├── Computing eigenvalues and eigenvectors
    └── Diagonalisation
```

---

### 5. Vector Spaces and Subspaces

A **vector space** $V$ over $\mathbb{R}$ is a set of objects (vectors) equipped with two operations — **addition** and **scalar multiplication** — that satisfy a specific list of axioms. Vector spaces provide the abstract framework for all of linear algebra.

```
  ℝ² as a Vector Space:

        ▲ y
        │
   v₂ = │─── (1,2) ●
  (1,2)  │         ╱
        │       ╱     v₁ + v₂ = (4, 3)
        │     ╱              ●
   v₁ = │───╱──── (3,1) ●
  (3,1)  │ ╱
        │╱
        ┼───────────────► x

  Closure: v₁ + v₂ stays in ℝ²
  Scalar:  2·v₁ = (6, 2) stays in ℝ²
```

#### Vector Space Axioms

For all $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ and scalars $c, d \in \mathbb{R}$:

|   #   | Axiom                  | Statement                                                                                             |
| :---: | :--------------------- | :---------------------------------------------------------------------------------------------------- |
|   1   | Closure (addition)     | $\mathbf{u} + \mathbf{v} \in V$                                                                       |
|   2   | Closure (scalar mult.) | $c\mathbf{u} \in V$                                                                                   |
|   3   | Commutativity          | $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$                                                   |
|   4   | Associativity (add.)   | $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$                     |
|   5   | Zero vector            | There exists $\mathbf{0} \in V$ such that $\mathbf{u} + \mathbf{0} = \mathbf{u}$                      |
|   6   | Additive inverse       | For each $\mathbf{u}$, there exists $-\mathbf{u}$ such that $\mathbf{u} + (-\mathbf{u}) = \mathbf{0}$ |
|   7   | Scalar distributivity  | $c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$                                              |
|   8   | Vector distributivity  | $(c + d)\mathbf{u} = c\mathbf{u} + d\mathbf{u}$                                                       |
|   9   | Associativity (scalar) | $c(d\mathbf{u}) = (cd)\mathbf{u}$                                                                     |
|  10   | Identity (scalar)      | $1\mathbf{u} = \mathbf{u}$                                                                            |

#### Common Vector Spaces

| Space                     | Description                                      |
| :------------------------ | :----------------------------------------------- |
| $\mathbb{R}^n$            | All $n$-tuples of real numbers (the most common) |
| $\mathbb{R}^{m \times n}$ | All $m \times n$ matrices                        |
| $P_n$                     | All polynomials of degree $\leq n$               |
| $C[a,b]$                  | All continuous functions on $[a, b]$             |

#### Subspaces

A **subspace** $W$ of $V$ is a non-empty subset of $V$ that is itself a vector space under the same operations. To verify, check three conditions:

1. $\mathbf{0} \in W$ (contains the zero vector).
2. If $\mathbf{u}, \mathbf{v} \in W$, then $\mathbf{u} + \mathbf{v} \in W$ (closed under addition).
3. If $\mathbf{u} \in W$ and $c \in \mathbb{R}$, then $c\mathbf{u} \in W$ (closed under scalar multiplication).

**Key subspaces associated with a matrix $A$ ($m \times n$):**

| Subspace                         | Definition                                                                  | Lives in       |
| :------------------------------- | :-------------------------------------------------------------------------- | :------------- |
| **Column space** $\text{Col}(A)$ | All vectors $\mathbf{b}$ such that $A\mathbf{x} = \mathbf{b}$ is consistent | $\mathbb{R}^m$ |
| **Null space** $\text{Nul}(A)$   | All solutions $\mathbf{x}$ to $A\mathbf{x} = \mathbf{0}$                    | $\mathbb{R}^n$ |
| **Row space** $\text{Row}(A)$    | Span of the rows of $A$ = $\text{Col}(A^T)$                                 | $\mathbb{R}^n$ |

#### Real-World Use Cases

- **Signal Processing**: Signals live in function spaces; filtering is projection onto subspaces.
- **Machine Learning**: Feature spaces are vector spaces; models operate in subspaces of the full feature space.
- **Quantum Mechanics**: Quantum states are vectors in a complex vector space (Hilbert space).
- **Data Compression**: The null space identifies redundant information that can be discarded.
- **Limitation**: Not all sets with "vector-like" elements form vector spaces — the axioms must all hold.

#### Steps

1. Identify the set of vectors or objects being tested.
2. Check whether the zero vector is included when verifying a subspace.
3. Test closure under addition and scalar multiplication.
4. If working with spanning sets, express a general linear combination and describe all vectors it can generate.
5. Conclude whether the set is a vector space, subspace, or spanning set.

#### Formula

A subset $W$ of a vector space $V$ is a subspace when:

$$
\mathbf{0} \in W, \quad \mathbf{u} + \mathbf{v} \in W, \quad c\mathbf{u} \in W
$$

Where:

|          Symbol          | Pronunciation | Meaning                    |
| :----------------------: | :------------ | :------------------------- |
|           $W$            | "W"           | Candidate subset           |
|           $V$            | "V"           | Ambient vector space       |
|       $\mathbf{0}$       | "zero vector" | Required identity element  |
| $\mathbf{u}, \mathbf{v}$ | "u, v"        | Arbitrary vectors from $W$ |
|           $c$            | "c"           | Any real scalar            |

##### Span

The **span** of a set of vectors $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_k\}$ is the set of all linear combinations:

$$
\text{Span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\} = \{c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k \mid c_i \in \mathbb{R}\}
$$

Where:

|         Symbol          | Pronunciation | Meaning                                     |
| :---------------------: | :------------ | :------------------------------------------ |
| $\text{Span}\{\ldots\}$ | "span of"     | The set of all possible linear combinations |
|          $c_i$          | "c sub i"     | Scalar weights (can be any real number)     |
|     $\mathbf{v}_i$      | "v sub i"     | The $i$-th vector in the spanning set       |

#### Examples

**Example 1 — Verify a subspace**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $W = \{(x, y, z) \in \mathbb{R}^3 \mid x + y + z = 0\}$ | A subset of $\mathbb{R}^3$ |
> | Find: Is $W$ a subspace of $\mathbb{R}^3$? | Check the three subspace conditions |
>
> **Step 1:** Check if $\mathbf{0} \in W$.
>
> $(0, 0, 0)$: $0 + 0 + 0 = 0$ ✓
>
> **Step 2:** Check closure under addition.
>
> Let $\mathbf{u} = (u_1, u_2, u_3)$ and $\mathbf{v} = (v_1, v_2, v_3)$ with $u_1 + u_2 + u_3 = 0$ and $v_1 + v_2 + v_3 = 0$.
>
> $\mathbf{u} + \mathbf{v} = (u_1 + v_1,\ u_2 + v_2,\ u_3 + v_3)$
>
> Sum: $(u_1 + v_1) + (u_2 + v_2) + (u_3 + v_3) = (u_1 + u_2 + u_3) + (v_1 + v_2 + v_3) = 0 + 0 = 0$ ✓
>
> **Step 3:** Check closure under scalar multiplication.
>
> $c\mathbf{u} = (cu_1, cu_2, cu_3)$
>
> Sum: $cu_1 + cu_2 + cu_3 = c(u_1 + u_2 + u_3) = c \cdot 0 = 0$ ✓
>
> **Step 4:** Conclude.
>
> $$\boxed{W \text{ is a subspace of } \mathbb{R}^3}$$
>
> Geometrically, $W$ is a **plane** through the origin in $\mathbb{R}^3$.

**Example 2 — Not a subspace (fails zero vector test)**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $W = \{(x, y) \in \mathbb{R}^2 \mid x + y = 1\}$ | A subset of $\mathbb{R}^2$ |
> | Find: Is $W$ a subspace of $\mathbb{R}^2$? | Check subspace conditions |
>
> **Step 1:** Check if $\mathbf{0} \in W$.
>
> $(0, 0)$: $0 + 0 = 0 \neq 1$ ✗
>
> **Step 2:** Conclude immediately.
>
> The zero vector $(0, 0)$ is **not** in $W$, so $W$ fails the first subspace condition.
>
> $$\boxed{W \text{ is NOT a subspace of } \mathbb{R}^2}$$
>
> Geometrically, $W$ is a **line** in $\mathbb{R}^2$ that does _not_ pass through the origin. Any subspace must contain the origin.

---

### 6. Linear Independence and Basis

A set of vectors is **linearly independent** if no vector in the set can be written as a linear combination of the others. **Linear independence** is the key property that distinguishes a _minimal_ spanning set (a **basis**) from a redundant one.

```
  Linearly Independent (2 vectors in ℝ²):

        ▲ y            v₂ = (1, 2)
        │            ╱
        │          ╱      These two vectors
        │        ●         span ALL of ℝ²
        │      ╱           (neither is a scalar
        │    ╱              multiple of the other)
        │  ╱
        ┼───────●────────► x
              v₁ = (3, 1)

  Linearly Dependent (3 vectors in ℝ²):

        ▲ y
        │   v₃ = v₁ + v₂
        │       ●
        │     ╱   ╲
        │   ●       ●     3 vectors in ℝ²
        │  v₂      v₁     are ALWAYS dependent
        ┼──────────────► x
```

#### Steps

1. Set up the equation $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \mathbf{0}$.
2. Form a matrix with the vectors as columns.
3. Row reduce to RREF.
4. If the **only** solution is $c_1 = c_2 = \cdots = c_k = 0$ (trivial solution), the vectors are **linearly independent**.
5. If a nontrivial solution exists (free variables), they are **linearly dependent**.

#### Formula

The set $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ is **linearly independent** if and only if:

$$
c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k = \mathbf{0} \implies c_1 = c_2 = \cdots = c_k = 0
$$

Where:

|     Symbol     | Pronunciation | Meaning                                       |
| :------------: | :------------ | :-------------------------------------------- |
|     $c_i$      | "c sub i"     | Scalar coefficients in the linear combination |
| $\mathbf{v}_i$ | "v sub i"     | The $i$-th vector being tested                |
|  $\mathbf{0}$  | "zero vector" | The vector of all zeros                       |

#### Basis and Dimension

A **basis** for a vector space $V$ is a set of vectors that is:

1. **Linearly independent**, and
2. **Spans** $V$.

The **dimension** of $V$ is the number of vectors in any basis for $V$.

| Concept            | Definition                                             | Example in $\mathbb{R}^3$                 |
| :----------------- | :----------------------------------------------------- | :---------------------------------------- |
| **Standard basis** | $\{\mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n\}$ | $\{(1,0,0), (0,1,0), (0,0,1)\}$           |
| **Dimension**      | Number of vectors in a basis                           | $\dim(\mathbb{R}^3) = 3$                  |
| **Rank**           | Dimension of the column space                          | $\text{rank}(A) = \dim(\text{Col}(A))$    |
| **Nullity**        | Dimension of the null space                            | $\text{nullity}(A) = \dim(\text{Nul}(A))$ |

#### Rank-Nullity Theorem

For an $m \times n$ matrix $A$:

$$
\text{rank}(A) + \text{nullity}(A) = n
$$

Where:

|       Symbol        | Pronunciation  | Meaning                                       |
| :-----------------: | :------------- | :-------------------------------------------- |
|  $\text{rank}(A)$   | "rank of A"    | Number of pivot columns in RREF of $A$        |
| $\text{nullity}(A)$ | "nullity of A" | Number of free variables (non-pivot columns)  |
|         $n$         | "n"            | Number of columns of $A$ (number of unknowns) |

#### Real-World Use Cases

- **Data Science**: Features in a dataset should be linearly independent; redundant features waste computation and can cause multicollinearity in regression.
- **Signal Processing**: Orthogonal bases (Fourier basis) decompose signals into independent frequency components.
- **Robotics**: Degrees of freedom = dimension of the configuration space; dependent joints reduce effective DOF.
- **Compression**: Finding a compact basis for data (PCA) — the basis vectors capture the maximum variance.
- **Limitation**: Checking independence by RREF is $O(n^3)$; for massive datasets, approximate methods are preferred.

#### Examples

**Example 1 — Test linear independence (independent case)**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix}$, $\mathbf{v}_2 = \begin{bmatrix} 0 \\ 1 \\ 3 \end{bmatrix}$, $\mathbf{v}_3 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$ | Three vectors in $\mathbb{R}^3$ |
> | Find: Are they linearly independent? | Check if only the trivial solution exists |
>
> **Step 1:** Form the matrix with vectors as columns.
>
> $$A = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 2 & 3 & 0 \end{bmatrix}$$
>
> **Step 2:** Row reduce to RREF.
>
> $R_3 \leftarrow R_3 - 2R_1$:
>
> $$\begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 3 & -2 \end{bmatrix}$$
>
> $R_3 \leftarrow R_3 - 3R_2$:
>
> $$\begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & -5 \end{bmatrix}$$
>
> $R_3 \leftarrow -\frac{1}{5}R_3$:
>
> $$\begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}$$
>
> Continue to RREF: $R_1 \leftarrow R_1 - R_3$, $R_2 \leftarrow R_2 - R_3$:
>
> $$\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = I_3$$
>
> **Step 3:** Interpret.
>
> Three pivots, zero free variables → the only solution to $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3 = \mathbf{0}$ is $c_1 = c_2 = c_3 = 0$.
>
> $$\boxed{\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\} \text{ is linearly independent — it forms a basis for } \mathbb{R}^3}$$

**Example 2 — Test linear independence (dependent case) + apply Rank-Nullity**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$, $\mathbf{v}_2 = \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}$, $\mathbf{v}_3 = \begin{bmatrix} 5 \\ 7 \\ 9 \end{bmatrix}$ | Three vectors in $\mathbb{R}^3$ |
> | Note: $\mathbf{v}_3 = \mathbf{v}_1 + \mathbf{v}_2$ | Potential dependency |
> | Find: Independence? Rank? Nullity? | Full analysis |
>
> **Step 1:** Form the matrix and row reduce.
>
> $$A = \begin{bmatrix} 1 & 4 & 5 \\ 2 & 5 & 7 \\ 3 & 6 & 9 \end{bmatrix}$$
>
> $R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - 3R_1$:
>
> $$\begin{bmatrix} 1 & 4 & 5 \\ 0 & -3 & -3 \\ 0 & -6 & -6 \end{bmatrix}$$
>
> $R_3 \leftarrow R_3 - 2R_2$:
>
> $$\begin{bmatrix} 1 & 4 & 5 \\ 0 & -3 & -3 \\ 0 & 0 & 0 \end{bmatrix}$$
>
> $R_2 \leftarrow -\frac{1}{3}R_2$:
>
> $$\begin{bmatrix} 1 & 4 & 5 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}$$
>
> $R_1 \leftarrow R_1 - 4R_2$:
>
> $$\begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}$$
>
> **Step 2:** Identify pivots and free variables.
>
> | Column | Type |
> |:---:|:---|
> | 1 | Pivot |
> | 2 | Pivot |
> | 3 | **Free** |
>
> **Step 3:** Apply Rank-Nullity.
>
> $$\text{rank}(A) = 2, \quad \text{nullity}(A) = 1, \quad 2 + 1 = 3 = n \quad \checkmark$$
>
> **Step 4:** Find the dependency relation. Let $c_3 = t$:
>
> From RREF: $c_1 + c_3 = 0 \implies c_1 = -t$, $c_2 + c_3 = 0 \implies c_2 = -t$.
>
> Setting $t = 1$: $-\mathbf{v}_1 - \mathbf{v}_2 + \mathbf{v}_3 = \mathbf{0}$, confirming $\mathbf{v}_3 = \mathbf{v}_1 + \mathbf{v}_2$.
>
> $$\boxed{\text{Linearly dependent. Rank} = 2, \text{ Nullity} = 1}$$

---

### 7. Eigenvalues and Eigenvectors

An **eigenvector** of a square matrix $A$ is a nonzero vector $\mathbf{v}$ that, when multiplied by $A$, only gets _scaled_ (not rotated). The scaling factor is the **eigenvalue** $\lambda$.

```
  Geometric Interpretation:

  Regular vector:                 Eigenvector:
  A changes direction AND length  A only changes length

      ╱ Av                            Av = λv
    ╱                                   ↑
  ●───► v                         ●────────► v
                                  │
                                  │ Same direction,
                                  │ scaled by λ

  λ > 1  → stretches the eigenvector
  0 < λ < 1 → shrinks the eigenvector
  λ < 0  → reverses direction
  λ = 0  → collapses to zero (singular)
  λ = 1  → eigenvector is unchanged
```

#### Real-World Use Cases

- **Structural Engineering**: Eigenvalues = natural frequencies of vibration; eigenvectors = mode shapes of a structure.
- **Google PageRank**: The dominant eigenvector of the web's link matrix determines page rankings.
- **PCA (Dimensionality Reduction)**: Eigenvectors of the covariance matrix define the principal components; eigenvalues measure the variance captured.
- **Stability Analysis**: System stability depends on eigenvalues of the system matrix — all eigenvalues inside the unit circle → stable.
- **Quantum Mechanics**: Observable quantities are eigenvalues of Hermitian operators.
- **Limitation**: Not every matrix is diagonalisable — defective matrices require Jordan normal form.

#### Steps

1. Set up the **characteristic equation**: $\det(A - \lambda I) = 0$.
2. Expand the determinant to get a polynomial in $\lambda$ (the **characteristic polynomial**).
3. Solve for $\lambda$ — these are the **eigenvalues**.
4. For each eigenvalue $\lambda_i$, solve $(A - \lambda_i I)\mathbf{v} = \mathbf{0}$ to find the **eigenvectors**.

#### Formula

The **characteristic equation**:

$$
\det(A - \lambda I) = 0
$$

The **eigenvalue equation**:

$$
A\mathbf{v} = \lambda\mathbf{v}
$$

Where:

|        Symbol         | Pronunciation                     | Meaning                          |
| :-------------------: | :-------------------------------- | :------------------------------- |
|          $A$          | "A"                               | An $n \times n$ square matrix    |
|       $\lambda$       | "lambda"                          | An eigenvalue (scalar)           |
|     $\mathbf{v}$      | "v"                               | An eigenvector (nonzero vector)  |
|          $I$          | "identity"                        | The $n \times n$ identity matrix |
| $\det(A - \lambda I)$ | "determinant of A minus lambda I" | The characteristic polynomial    |

#### Key Properties of Eigenvalues

| Property                    | Statement                                                                    |
| :-------------------------- | :--------------------------------------------------------------------------- |
| **Sum**                     | $\lambda_1 + \lambda_2 + \cdots + \lambda_n = \text{trace}(A) = \sum a_{ii}$ |
| **Product**                 | $\lambda_1 \cdot \lambda_2 \cdots \lambda_n = \det(A)$                       |
| **Invertibility**           | $A$ is invertible $\iff$ no eigenvalue is $0$                                |
| **Symmetric matrices**      | All eigenvalues are **real**                                                 |
| **Eigenvalues of $A^{-1}$** | $\frac{1}{\lambda}$ for each eigenvalue $\lambda$ of $A$                     |
| **Eigenvalues of $A^k$**    | $\lambda^k$ for each eigenvalue $\lambda$ of $A$                             |

#### Diagonalisation

If $A$ has $n$ linearly independent eigenvectors, then:

$$
A = PDP^{-1}
$$

Where:

|  Symbol  | Pronunciation | Meaning                                          |
| :------: | :------------ | :----------------------------------------------- |
|   $P$    | "P"           | Matrix whose columns are the eigenvectors of $A$ |
|   $D$    | "D"           | Diagonal matrix with eigenvalues on the diagonal |
| $P^{-1}$ | "P inverse"   | Inverse of the eigenvector matrix                |

This is useful because $A^k = PD^kP^{-1}$, which makes computing powers of $A$ trivial.

#### Examples

**Example 1 — 2×2 eigenvalue/eigenvector computation**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}$ | A $2 \times 2$ matrix |
> | Find: Eigenvalues and eigenvectors | Using the characteristic equation |
>
> **Step 1:** Set up $\det(A - \lambda I) = 0$.
>
> $$A - \lambda I = \begin{bmatrix} 4 - \lambda & 1 \\ 2 & 3 - \lambda \end{bmatrix}$$
>
> **Step 2:** Compute the characteristic polynomial.
>
> $$\det(A - \lambda I) = (4 - \lambda)(3 - \lambda) - (1)(2) = \lambda^2 - 7\lambda + 10$$
>
> **Step 3:** Solve for $\lambda$.
>
> $$\lambda^2 - 7\lambda + 10 = 0 \implies (\lambda - 5)(\lambda - 2) = 0$$
>
> $$\lambda_1 = 5, \quad \lambda_2 = 2$$
>
> **Verify:** $\lambda_1 + \lambda_2 = 7 = \text{trace}(A) = 4 + 3$ ✓ and $\lambda_1 \cdot \lambda_2 = 10 = \det(A) = 12 - 2$ ✓
>
> **Step 4:** Find eigenvectors for $\lambda_1 = 5$.
>
> $$(A - 5I)\mathbf{v} = \mathbf{0}: \quad \begin{bmatrix} -1 & 1 \\ 2 & -2 \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
>
> Row 1: $-v_1 + v_2 = 0 \implies v_2 = v_1$. Let $v_1 = 1$:
>
> $$\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$
>
> **Step 5:** Find eigenvectors for $\lambda_2 = 2$.
>
> $$(A - 2I)\mathbf{v} = \mathbf{0}: \quad \begin{bmatrix} 2 & 1 \\ 2 & 1 \end{bmatrix}\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
>
> Row 1: $2v_1 + v_2 = 0 \implies v_2 = -2v_1$. Let $v_1 = 1$:
>
> $$\mathbf{v}_2 = \begin{bmatrix} 1 \\ -2 \end{bmatrix}$$
>
> $$\boxed{\lambda_1 = 5,\ \mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}; \quad \lambda_2 = 2,\ \mathbf{v}_2 = \begin{bmatrix} 1 \\ -2 \end{bmatrix}}$$

**Example 2 — 3×3 eigenvalues + diagonalisation check**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $A = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 5 \end{bmatrix}$ | A diagonal $3 \times 3$ matrix |
> | Find: Eigenvalues, eigenvectors, and $A^3$ | Full eigenanalysis |
>
> **Step 1:** For a diagonal matrix, eigenvalues are the diagonal entries.
>
> $$\lambda_1 = 2, \quad \lambda_2 = 3, \quad \lambda_3 = 5$$
>
> **Verify:** $\text{trace}(A) = 2 + 3 + 5 = 10 = \lambda_1 + \lambda_2 + \lambda_3$ ✓
>
> $\det(A) = 2 \times 3 \times 5 = 30 = \lambda_1 \cdot \lambda_2 \cdot \lambda_3$ ✓
>
> **Step 2:** Eigenvectors are the standard basis vectors.
>
> | Eigenvalue | Eigenvector | Reason |
> |:---:|:---:|:---|
> | $\lambda_1 = 2$ | $\mathbf{e}_1 = (1,0,0)^T$ | $A\mathbf{e}_1 = (2,0,0)^T = 2\mathbf{e}_1$ |
> | $\lambda_2 = 3$ | $\mathbf{e}_2 = (0,1,0)^T$ | $A\mathbf{e}_2 = (0,3,0)^T = 3\mathbf{e}_2$ |
> | $\lambda_3 = 5$ | $\mathbf{e}_3 = (0,0,1)^T$ | $A\mathbf{e}_3 = (0,0,5)^T = 5\mathbf{e}_3$ |
>
> **Step 3:** Diagonalisation.
>
> Since $A$ is already diagonal: $P = I$, $D = A$, so $A = IDI^{-1} = A$.
>
> **Step 4:** Compute $A^3$ using the diagonal property.
>
> $$A^3 = \begin{bmatrix} 2^3 & 0 & 0 \\ 0 & 3^3 & 0 \\ 0 & 0 & 5^3 \end{bmatrix} = \begin{bmatrix} 8 & 0 & 0 \\ 0 & 27 & 0 \\ 0 & 0 & 125 \end{bmatrix}$$
>
> $$\boxed{A^3 = \begin{bmatrix} 8 & 0 & 0 \\ 0 & 27 & 0 \\ 0 & 0 & 125 \end{bmatrix}}$$
>
> _Key insight:_ A diagonal matrix is already diagonalised. Powers of diagonal matrices just raise each diagonal entry to that power — this is why diagonalisation makes matrix powers computationally trivial.

---

<p align="left">
  <a href="./linear-equations-and-matrices.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./pca-and-applications.md"><b>Next →</b></a>
  </span>
</p>
