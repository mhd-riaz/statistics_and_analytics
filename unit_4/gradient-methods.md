<p align="left">
  <a href="./optimization-foundations.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./index.md"><b>Next →</b></a>
  </span>
</p>

---

# Gradient Methods

```
Gradient Methods
├── 7. Gradient and Directional Change
│   ├── Gradient as steepest ascent direction
│   ├── Partial derivatives in multivariable functions
│   └── Directional interpretation for optimization
│
├── 8. Hessian Matrix
│   ├── Second-order partial derivatives
│   ├── Curvature and local shape
│   └── Classifying stationary points
│
├── 9. Gradient Descent
│   ├── Full-gradient update rule
│   ├── Learning rate effects
│   └── Convergence intuition
│
└── 10. Stochastic Gradient Descent
    ├── Sample-wise or mini-batch updates
    ├── Noisy but fast learning dynamics
    └── Scalability for large datasets
```

---

### 7. Gradient and Directional Change

For a multivariable function, the **gradient** collects all partial derivatives into a vector. It points in the direction of steepest increase of the function, while the negative gradient points in the direction of steepest decrease.

This makes the gradient the central object in machine learning optimization. Instead of checking every possible direction, we use the gradient to determine how the objective changes locally with respect to each variable.

```
  Contour (level-curve) view with gradient direction

        ┌──────────────────┐
        │    ╭──────────╮   │  f = 20
        │    │  ╭────╮  │   │
        │    │  │ •──►│  │   │  f = 10
        │    │  │  ∇f │  │   │
        │    │  ╰────╯  │   │  f = 5
        │    ╰──────────╯   │
        └──────────────────┘   f = 1

  • = current point
  ► = gradient direction (toward higher f)
  Descent = move opposite to ► (toward lower f)
  Contour lines = sets of equal function value
```

#### Gradient Interpretation

| Idea                              | Meaning                                                    |
| :-------------------------------- | :--------------------------------------------------------- |
| **Partial derivative**            | Change with respect to one variable while others are fixed |
| **Gradient vector**               | Collection of all partial derivatives                      |
| **Direction of steepest ascent**  | Gradient direction                                         |
| **Direction of steepest descent** | Negative gradient direction                                |
| **Zero gradient**                 | Possible stationary point                                  |

#### Real-World Use Cases

- **Machine Learning**: Model weights are updated using gradients of the loss function.
- **Economics**: Multivariable optimization uses partial derivatives to study response to price or demand changes.
- **Engineering Design**: Sensitivity of performance measures to several design parameters is read from the gradient.
- **Robotics and control**: Gradient information helps tune trajectories and controller parameters.
- **Caveat**: A zero gradient can indicate a minimum, maximum, or saddle point, so more analysis may be needed.

#### Steps

1. Write the multivariable function clearly.
2. Differentiate with respect to each variable separately.
3. Assemble the partial derivatives into the gradient vector.
4. Evaluate the gradient at the point of interest.
5. Use the gradient direction to interpret local increase or decrease.

#### Formula

For a function of two variables, the gradient is:

$$
\nabla f(x,y) = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)
$$

Where:
|             Symbol              | Pronunciation            | Meaning                               |
| :-----------------------------: | :----------------------- | :------------------------------------ |
|           $\nabla f$            | "gradient of f"          | Vector of partial derivatives         |
| $\frac{\partial f}{\partial x}$ | "partial f by partial x" | Change in $f$ with respect to $x$     |
| $\frac{\partial f}{\partial y}$ | "partial f by partial y" | Change in $f$ with respect to $y$     |
|             $(x,y)$             | "x y"                    | Point where the gradient is evaluated |

The directional change for minimization follows:

$$
\text{descent direction} = -\nabla f(x,y)
$$

Where:
|      Symbol      | Pronunciation            | Meaning                              |
| :--------------: | :----------------------- | :----------------------------------- |
| $-\nabla f(x,y)$ | "negative gradient of f" | Direction of steepest local decrease |
| $\nabla f(x,y)$  | "gradient of f"          | Direction of steepest local increase |

#### Examples

**Example 1 — Compute a gradient vector**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $f(x,y) = x^2 + 3y^2$ | Objective function |
> | Find: $\nabla f(x,y)$ | Gradient vector |
>
> **Step 1:** Differentiate with respect to $x$.
>
> $$\frac{\partial f}{\partial x} = 2x$$
>
> **Step 2:** Differentiate with respect to $y$.
>
> $$\frac{\partial f}{\partial y} = 6y$$
>
> **Step 3:** Assemble the gradient vector.
>
> $$\nabla f(x,y) = (2x, 6y)$$
>
> **Step 4:** Interpret the result.
>
> The function changes twice as fast in the $x$ direction and six times the current $y$ value in the $y$ direction.
>
> **Step 5:** Final answer.
>
> $$\boxed{\nabla f(x,y) = (2x, 6y)}$$

**Example 2 — Evaluate the gradient at a point and find the descent direction**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $g(x,y) = x^2 + y^2$ | Objective function |
> | $(x,y) = (2,-1)$ | Current point |
> | Find: gradient and descent direction | Determine local increase and decrease directions |
>
> **Step 1:** Compute the gradient formula.
>
> $$\nabla g(x,y) = (2x, 2y)$$
>
> **Step 2:** Substitute the point $(2,-1)$.
>
> $$\nabla g(2,-1) = (4,-2)$$
>
> **Step 3:** Identify the steepest ascent direction.
>
> The gradient $(4,-2)$ points in the direction of steepest increase.
>
> **Step 4:** Negate the gradient for descent.
>
> $$-\nabla g(2,-1) = (-4, 2)$$
>
> **Step 5:** Final answer.
>
> $$\boxed{\nabla g(2,-1) = (4,-2), \quad \text{descent direction} = (-4,2)}$$

---

### 8. Hessian Matrix

The **Hessian matrix** collects second-order partial derivatives of a multivariable function. While the gradient tells us slope, the Hessian tells us curvature. This helps determine whether a stationary point behaves like a bowl, a hill, or a saddle.

In optimization, the Hessian is useful for understanding local geometry. It is central to second-order methods and to classifying critical points more reliably than the gradient alone.

```
  Local shapes near a stationary point

  Bowl (minimum)        Hill (maximum)        Saddle point
         __                  /\                  ╲ ╱
       /    \              /    \                 ╳
      /      \            /      \              ╱ ╲
     /   __   \          ╱________╲           ╱     ╲
    /   /  \   \
   /___/    \___\

   f'' > 0 (all)        f'' < 0 (all)        f'' mixed signs
   Positive definite     Negative definite    Indefinite
```

```
  Hessian determinant test decision flowchart (2 variables)

              f'(x,y) = (0,0)
                    │
           Compute D = fxx·fyy − (fxy)²
                    │
           ┌────────┼────────┐
           │        │        │
         D > 0    D < 0    D = 0
           │        │        │
      ┌────┴────┐   │    Inconclusive
      │         │   │
   fxx > 0   fxx < 0
      │         │
  Local min  Local max
                    Saddle point
```

#### Hessian Interpretation

| Hessian behavior         | Interpretation                     |
| :----------------------- | :--------------------------------- |
| Positive definite        | Local minimum                      |
| Negative definite        | Local maximum                      |
| Mixed signs / indefinite | Saddle point                       |
| Zero or singular case    | Inconclusive without more analysis |

#### Real-World Use Cases

- **Machine Learning**: Curvature information helps diagnose flat regions, sharp minima, and conditioning issues.
- **Structural Engineering**: Second derivatives capture how responses bend around equilibrium points.
- **Economics**: Hessians help classify utility or cost function optima.
- **Numerical Optimization**: Newton-type methods use Hessians for faster convergence near a solution.
- **Caveat**: Computing the full Hessian is expensive for high-dimensional models.

#### Steps

1. Compute all first-order partial derivatives.
2. Differentiate again to obtain second-order partial derivatives.
3. Arrange them into the Hessian matrix.
4. Evaluate the Hessian at a stationary point.
5. Use curvature signs or definiteness to classify the point.

#### Formula

For a function $f(x,y)$, the Hessian is:

$$
H_f(x,y) = \begin{bmatrix}
\frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\
\frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2}
\end{bmatrix}
$$

Where:
|                    Symbol                    | Pronunciation                           | Meaning                                    |
| :------------------------------------------: | :-------------------------------------- | :----------------------------------------- |
|                  $H_f(x,y)$                  | "Hessian of f"                          | Matrix of second-order partial derivatives |
|     $\frac{\partial^2 f}{\partial x^2}$      | "second partial of f with respect to x" | Curvature in the $x$ direction             |
|     $\frac{\partial^2 f}{\partial y^2}$      | "second partial of f with respect to y" | Curvature in the $y$ direction             |
| $\frac{\partial^2 f}{\partial x \partial y}$ | "mixed partial"                         | Interaction curvature across variables     |

For two variables, the determinant test uses:

$$
D = f_{xx}f_{yy} - (f_{xy})^2
$$

Where:
|  Symbol  | Pronunciation | Meaning                                       |
| :------: | :------------ | :-------------------------------------------- |
|   $D$    | "D"           | Determinant of the Hessian in two variables   |
| $f_{xx}$ | "f double x"  | Second partial derivative with respect to $x$ |
| $f_{yy}$ | "f double y"  | Second partial derivative with respect to $y$ |
| $f_{xy}$ | "f x y"       | Mixed partial derivative                      |

#### Examples

**Example 1 — Build a Hessian matrix**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $f(x,y) = x^2 + 4xy + y^2$ | Objective function |
> | Find: $H_f(x,y)$ | Hessian matrix |
>
> **Step 1:** Compute the first partial derivatives.
>
> $$f_x = 2x + 4y$$
>
> $$f_y = 4x + 2y$$
>
> **Step 2:** Differentiate again.
>
> $$f_{xx} = 2, \qquad f_{xy} = 4$$
>
> $$f_{yx} = 4, \qquad f_{yy} = 2$$
>
> **Step 3:** Assemble the Hessian matrix.
>
> $$H_f(x,y) = \begin{bmatrix} 2 & 4 \\ 4 & 2 \end{bmatrix}$$
>
> **Step 4:** Interpret the result.
>
> The off-diagonal entries show strong interaction curvature between $x$ and $y$.
>
> **Step 5:** Final answer.
>
> $$\boxed{H_f(x,y) = \begin{bmatrix} 2 & 4 \\ 4 & 2 \end{bmatrix}}$$

**Example 2 — Classify a stationary point with the Hessian**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $g(x,y) = x^2 + y^2$ | Objective function |
> | $(0,0)$ | Stationary point |
> | Find: classify the point | Determine local behavior using the Hessian |
>
> **Step 1:** Compute second derivatives.
>
> $$g_{xx} = 2, \qquad g_{xy} = 0, \qquad g_{yy} = 2$$
>
> **Step 2:** Form the Hessian.
>
> $$H_g(0,0) = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}$$
>
> **Step 3:** Compute the determinant.
>
> $$D = (2)(2) - 0^2 = 4$$
>
> **Step 4:** Apply the test.
>
> Since $D > 0$ and $g_{xx} = 2 > 0$, the point is a **local minimum**.
>
> **Step 5:** Final answer.
>
> $$\boxed{(0,0) \text{ is a local minimum}}$$

---

### 9. Gradient Descent

**Gradient Descent** is an iterative minimization algorithm that updates parameters using the full gradient of the objective function. At each step, it moves opposite the gradient because that is the direction of steepest local decrease.

The method is simple and widely used, but its behavior depends heavily on the learning rate. If the learning rate is too large, updates can overshoot. If it is too small, convergence becomes slow.

```
  Full-gradient descent toward a minimum

  Loss
  ▲
  │         •
  │       •
  │     •
  │   •
  │ •
  └────────────────► iteration

  Objective value decreases over iterations
```

```
  Learning rate comparison

  η too small              η just right             η too large

  Loss                     Loss                     Loss
  ▲                        ▲                        ▲
  │•••••                   │•                       │•     •
  │     ••••               │  •                     │ •   • •
  │         •••            │    •                   │  • •   •
  │            •••         │      •                 │   •     •
  │               •        │        •               │          •
  └──────────────► k       └──────────► k           └──────────► k

  Slow convergence         Efficient descent        Oscillation/divergence
```

#### Learning Rate Effects

| Learning rate   | Behavior                  |
| :-------------- | :------------------------ |
| **Too small**   | Very slow progress        |
| **Well chosen** | Stable convergence        |
| **Too large**   | Oscillation or divergence |

#### Real-World Use Cases

- **Linear and logistic regression**: Gradient Descent is used when closed-form solutions are inconvenient or large-scale.
- **Deep learning**: Full-gradient updates illustrate the core logic behind more advanced optimizers.
- **Scientific computing**: Error minimization in fitted models often uses gradient-based descent.
- **Control tuning**: Parameter sets are improved iteratively by descending an error surface.
- **Caveat**: Computing the full gradient can be expensive on large datasets.

#### Steps

1. Initialize the parameter vector.
2. Compute the full gradient using all relevant data.
3. Update the parameter vector using the negative gradient.
4. Recompute the objective and repeat.
5. Stop when the gradient or objective change becomes sufficiently small.

#### Formula

The Gradient Descent update is:

$$
\mathbf{x}_{k+1} = \mathbf{x}_k - \eta \nabla f(\mathbf{x}_k)
$$

Where:
|          Symbol          | Pronunciation                     | Meaning                            |
| :----------------------: | :-------------------------------- | :--------------------------------- |
|      $\mathbf{x}_k$      | "x vector sub k"                  | Current parameter vector           |
|    $\mathbf{x}_{k+1}$    | "x vector sub k plus 1"           | Updated parameter vector           |
|          $\eta$          | "eta"                             | Learning rate                      |
| $\nabla f(\mathbf{x}_k)$ | "gradient of f at x vector sub k" | Full gradient at the current point |

The objective should ideally satisfy:

$$
f(\mathbf{x}_{k+1}) < f(\mathbf{x}_k)
$$

Where:
|        Symbol         | Pronunciation                | Meaning                           |
| :-------------------: | :--------------------------- | :-------------------------------- |
| $f(\mathbf{x}_{k+1})$ | "f at x vector sub k plus 1" | Objective value after the update  |
|   $f(\mathbf{x}_k)$   | "f at x vector sub k"        | Objective value before the update |

#### Examples

**Example 1 — One Gradient Descent update in two dimensions**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $f(x,y) = x^2 + y^2$ | Objective function |
> | $(x_0,y_0) = (2,1)$ | Initial point |
> | $\eta = 0.1$ | Learning rate |
> | Find: the next point | Apply one Gradient Descent step |
>
> **Step 1:** Compute the gradient.
>
> $$\nabla f(x,y) = (2x, 2y)$$
>
> **Step 2:** Evaluate the gradient at $(2,1)$.
>
> $$\nabla f(2,1) = (4,2)$$
>
> **Step 3:** Apply the update rule.
>
> $$(x_1,y_1) = (2,1) - 0.1(4,2)$$
>
> **Step 4:** Simplify.
>
> $$(x_1,y_1) = (1.6,0.8)$$
>
> **Step 5:** Final answer.
>
> $$\boxed{(x_1,y_1) = (1.6,0.8)}$$

**Example 2 — Show objective decrease after an update**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $f(x) = x^2$ | Objective function |
> | $x_0 = 4$ | Initial point |
> | $\eta = 0.25$ | Learning rate |
> | Find: $x_1$ and compare objective values | Show one descent step |
>
> **Step 1:** Differentiate the objective.
>
> $$f'(x) = 2x$$
>
> **Step 2:** Evaluate the slope at the current point.
>
> $$f'(4) = 8$$
>
> **Step 3:** Update the parameter.
>
> $$x_1 = 4 - 0.25(8) = 2$$
>
> **Step 4:** Compare objective values.
>
> $$f(4) = 16, \qquad f(2) = 4$$
>
> **Step 5:** Final answer.
>
> $$\boxed{x_1 = 2 \text{ and the objective decreases from } 16 \text{ to } 4}$$

---

### 10. Stochastic Gradient Descent

**Stochastic Gradient Descent (SGD)** updates parameters using one training example, or a very small mini-batch, at a time instead of the full dataset. This makes each update cheaper and often much faster in large-scale learning problems.

Because each update uses only part of the data, the gradient estimate is noisy. That noise can slow precise convergence, but it can also help the algorithm move through complex landscapes and escape shallow local structures.

```
  Noisy descent path

  Loss
  ▲
  │      •
  │    •  •
  │   •
  │  •   •
  │ •
  └────────────────► iteration

  Downward trend with noisy steps
```

#### Gradient Descent vs SGD

| Method               | Gradient source          | Per-step cost | Update behavior   |
| :------------------- | :----------------------- | :------------ | :---------------- |
| **Gradient Descent** | Full dataset             | High          | Stable and smooth |
| **SGD**              | One sample or mini-batch | Low           | Noisy but fast    |

#### Real-World Use Cases

- **Deep Learning**: Large datasets make full-gradient methods expensive, so SGD or mini-batch SGD is standard.
- **Online learning**: Models can update as new data arrives one example at a time.
- **Recommendation systems**: Massive training sets benefit from cheap frequent updates.
- **Streaming analytics**: SGD works well when data cannot all be stored or processed at once.
- **Caveat**: The noise in SGD can cause fluctuation around the minimum unless learning rates are controlled carefully.

#### Steps

1. Initialize the parameter vector.
2. Select one sample or a small mini-batch.
3. Compute the sample-based gradient estimate.
4. Update parameters using that estimated gradient.
5. Repeat across many samples and epochs.

#### Formula

An SGD update using sample $i$ is:

$$
\mathbf{x}_{k+1} = \mathbf{x}_k - \eta \nabla f_i(\mathbf{x}_k)
$$

Where:
|           Symbol           | Pronunciation               | Meaning                                         |
| :------------------------: | :-------------------------- | :---------------------------------------------- |
|       $\mathbf{x}_k$       | "x vector sub k"            | Current parameter vector                        |
|     $\mathbf{x}_{k+1}$     | "x vector sub k plus 1"     | Updated parameter vector                        |
|           $\eta$           | "eta"                       | Learning rate                                   |
| $\nabla f_i(\mathbf{x}_k)$ | "gradient of sample i loss" | Gradient estimate from one sample or mini-batch |

Across many steps, SGD aims for:

$$
\mathbb{E}[\nabla f_i(\mathbf{x})] \approx \nabla f(\mathbf{x})
$$

Where:
|          Symbol          | Pronunciation     | Meaning                              |
| :----------------------: | :---------------- | :----------------------------------- |
|       $\mathbb{E}$       | "expectation"     | Average over random sample choices   |
| $\nabla f_i(\mathbf{x})$ | "sample gradient" | Noisy gradient estimate              |
|  $\nabla f(\mathbf{x})$  | "full gradient"   | True gradient over the whole dataset |

#### Examples

**Example 1 — One SGD-style update from a single sample gradient**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | Current parameter $w_0 = 2$ | Starting weight |
> | Sample gradient $g_1 = 5$ | Gradient from one training example |
> | $\eta = 0.1$ | Learning rate |
> | Find: $w_1$ | Updated parameter after one SGD step |
>
> **Step 1:** Write the SGD update rule.
>
> $$w_1 = w_0 - \eta g_1$$
>
> **Step 2:** Substitute the given values.
>
> $$w_1 = 2 - 0.1(5)$$
>
> **Step 3:** Simplify.
>
> $$w_1 = 2 - 0.5 = 1.5$$
>
> **Step 4:** Interpret the result.
>
> The parameter moves in the direction opposite the sample gradient.
>
> **Step 5:** Final answer.
>
> $$\boxed{w_1 = 1.5}$$

**Example 2 — Compare two noisy SGD updates**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | Current parameter $w_0 = 1$ | Starting weight |
> | First sample gradient $g_1 = 2$ | Gradient from sample 1 |
> | Second sample gradient $g_2 = -1$ | Gradient from sample 2 |
> | $\eta = 0.2$ | Learning rate |
> | Find: $w_1$ and $w_2$ | Two successive SGD updates |
>
> **Step 1:** Apply the first update.
>
> $$w_1 = 1 - 0.2(2) = 0.6$$
>
> **Step 2:** Apply the second update using the new sample gradient.
>
> $$w_2 = 0.6 - 0.2(-1) = 0.8$$
>
> **Step 3:** Interpret the movement.
>
> The second sample gradient points in the opposite direction, so the update partially reverses the first step.
>
> **Step 4:** Relate this to SGD behavior.
>
> This illustrates why SGD follows a noisy path rather than a perfectly smooth one.
>
> **Step 5:** Final answer.
>
> $$\boxed{w_1 = 0.6, \quad w_2 = 0.8}$$

---

<p align="left">
  <a href="./optimization-foundations.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./index.md"><b>Next →</b></a>
  </span>
</p>
