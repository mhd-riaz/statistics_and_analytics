<p align="left">
  <a href="./functions-and-calculus.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./gradient-methods.md"><b>Next →</b></a>
  </span>
</p>

---

# Optimization Foundations

```
Optimization Foundations
├── 4. Introduction to Optimization
│   ├── Objective function, variables, and constraints
│   ├── Minimization vs maximization
│   └── Feasible region and optimal solution
│
├── 5. Maxima and Minima
│   ├── Critical points
│   ├── First derivative and second derivative tests
│   └── Local vs global optima
│
└── 6. First-Order Optimization Algorithms
    ├── Gradient-based update logic
    ├── Learning rate and convergence behavior
    └── Iterative improvement of objective values
```

---

### 4. Introduction to Optimization

**Optimization** is the process of choosing values of decision variables so that an objective function is made as small as possible or as large as possible, while respecting any constraints. In machine learning, the objective is often a loss function; in engineering, it may be cost, weight, energy, or error.

Every optimization problem has three core ingredients: decision variables, an objective function, and optionally a set of constraints. The solution must lie inside the feasible region and achieve the best attainable objective value there.

```
  Feasible region and best point

  y
  ▲
  │        feasible region
  │      /-----------\
  │     /      *      \
  │    /   optimal      \
  │   /      point       \
  │  /---------------------\
  └──────────────────────────► x

  Best value is chosen inside the allowed region
```

#### Core Components of an Optimization Problem

| Component              | Meaning                                      | Example                                        |
| :--------------------- | :------------------------------------------- | :--------------------------------------------- |
| **Decision variable**  | Quantity we are free to choose               | Learning rate, batch size, production quantity |
| **Objective function** | Quantity to minimize or maximize             | Loss, cost, profit, efficiency                 |
| **Constraint**         | Restriction on allowed values                | Budget, capacity, non-negativity               |
| **Feasible region**    | Set of all values satisfying constraints     | All valid parameter combinations               |
| **Optimal solution**   | Feasible point with the best objective value | Lowest cost or highest profit                  |

#### Real-World Use Cases

- **Machine Learning**: Training a model means minimizing loss over model parameters.
- **Manufacturing**: Production schedules are optimized to reduce waste or maximize throughput.
- **Transportation**: Routing problems minimize time, distance, or fuel usage under capacity limits.
- **Finance**: Portfolio selection balances expected return and risk under budget constraints.
- **Caveat**: A mathematically optimal solution can still be impractical if the model omits real-world constraints.

#### Steps

1. Define the decision variables clearly.
2. Write the objective function that measures performance.
3. State any constraints on the variables.
4. Determine the feasible region.
5. Search for the feasible point that gives the best objective value.

#### Formula

A general constrained optimization problem is written as:

$$
\min_{x \in \mathcal{F}} f(x)
$$

Where:
|    Symbol     | Pronunciation | Meaning                                  |
| :-----------: | :------------ | :--------------------------------------- |
|    $\min$     | "minimize"    | Seek the smallest objective value        |
|      $x$      | "x"           | Decision variable or vector of variables |
| $\mathcal{F}$ | "script F"    | Feasible set satisfying all constraints  |
|    $f(x)$     | "f of x"      | Objective function                       |

For maximization problems, the form is:

$$
\max_{x \in \mathcal{F}} f(x)
$$

Where:
|    Symbol     | Pronunciation | Meaning                                  |
| :-----------: | :------------ | :--------------------------------------- |
|    $\max$     | "maximize"    | Seek the largest objective value         |
|      $x$      | "x"           | Decision variable or vector of variables |
| $\mathcal{F}$ | "script F"    | Feasible set satisfying all constraints  |
|    $f(x)$     | "f of x"      | Objective function                       |

#### Examples

**Example 1 — Identify a minimization problem**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $f(x) = (x - 2)^2 + 1$ | Objective function |
> | No explicit constraints | Any real value of $x$ is allowed |
> | Find: optimization type and best value | Determine whether it is a minimization problem and find the minimum |
>
> **Step 1:** Inspect the objective function.
>
> $$f(x) = (x - 2)^2 + 1$$
>
> **Step 2:** Note that the squared term is never negative.
>
> $$(x - 2)^2 \ge 0$$
>
> **Step 3:** Find the smallest possible value of the squared term.
>
> The minimum occurs when $(x - 2)^2 = 0$, so $x = 2$.
>
> **Step 4:** Substitute into the objective.
>
> $$f(2) = (2 - 2)^2 + 1 = 1$$
>
> **Step 5:** Final answer.
>
> $$\boxed{\text{Minimum value } = 1 \text{ at } x = 2}$$

**Example 2 — Identify a maximization problem with a feasible interval**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $P(q) = -q^2 + 8q$ | Profit function |
> | $0 \le q \le 10$ | Feasible production interval |
> | Find: maximum profit on the feasible set | Determine the best feasible output level |
>
> **Step 1:** Recognize the objective.
>
> $$P(q) = -q^2 + 8q$$
>
> **Step 2:** Note that the coefficient of $q^2$ is negative.
>
> The parabola opens downward, so it has a maximum.
>
> **Step 3:** Use the vertex formula.
>
> $$q^* = -\frac{b}{2a} = -\frac{8}{2(-1)} = 4$$
>
> **Step 4:** Check that $q = 4$ is feasible and evaluate the profit.
>
> $$P(4) = -(4)^2 + 8(4) = -16 + 32 = 16$$
>
> **Step 5:** Final answer.
>
> $$\boxed{\text{Maximum profit } = 16 \text{ at } q = 4}$$

---

### 5. Maxima and Minima

A **maximum** is a point where the function value is higher than nearby points, and a **minimum** is a point where the function value is lower than nearby points. These may be **local** or **global** depending on whether the comparison is made near the point or over the entire domain.

Critical points occur where the first derivative is zero or undefined. The first derivative test and second derivative test help classify those points.

```
  Local maximum       Local minimum        Saddle-like flat point

      *                   *                     *
    *   *               *   *                 *   *
  *       *           *       *             *       *
            \       /
             \     /
              *   *

  Peak                Valley               Not every flat point is best
```

```
  Local vs Global optima on a single function

  f(x)
  ▲
  │  *             local max
  │ * *
  │*   *          *
  │     *       * * ← local min (not the best)
  │      *    *    *
  │       *  *      *
  │        **        *
  │     global min    *
  └──────────────────────► x

  A local minimum has the lowest nearby value.
  The global minimum has the lowest value everywhere.
  Optimization algorithms can get stuck at a local minimum.
```

#### Classification Guide

| Situation      | Interpretation                                   |
| :------------- | :----------------------------------------------- |
| $f'(x)=0$      | Candidate critical point                         |
| $f''(x) > 0$   | Local minimum                                    |
| $f''(x) < 0$   | Local maximum                                    |
| $f''(x) = 0$   | Test is inconclusive; further analysis is needed |
| Boundary value | Must also be checked in constrained problems     |

#### Real-World Use Cases

- **Engineering Design**: Minimize material weight while maintaining structural performance.
- **Economics**: Maximize revenue or profit with respect to price or production level.
- **Machine Learning**: Minimize training loss and avoid poor stationary points.
- **Operations Research**: Optimize staffing, scheduling, or energy usage.
- **Caveat**: A local optimum is not always the best solution globally.

#### Steps

1. Differentiate the objective function.
2. Solve $f'(x)=0$ to locate critical points.
3. Compute the second derivative if available.
4. Classify each critical point using the sign of $f''(x)$ or another test.
5. Compare values if a global optimum is required.

#### Formula

Critical points are found by solving:

$$
f'(x) = 0
$$

Where:
| Symbol  | Pronunciation  | Meaning                           |
| :-----: | :------------- | :-------------------------------- |
| $f'(x)$ | "f prime of x" | First derivative of the objective |
|   $0$   | "zero"         | Stationary slope condition        |
|   $x$   | "x"            | Candidate point for an optimum    |

The second derivative test uses:

$$
f''(x) \begin{cases} > 0 & \text{local minimum} \\ < 0 & \text{local maximum} \end{cases}
$$

Where:
|  Symbol  | Pronunciation         | Meaning                               |
| :------: | :-------------------- | :------------------------------------ |
| $f''(x)$ | "f double prime of x" | Second derivative measuring curvature |
|  $> 0$   | "greater than zero"   | Curve bends upward near the point     |
|  $< 0$   | "less than zero"      | Curve bends downward near the point   |

#### Examples

**Example 1 — Find a local minimum**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $f(x) = x^2 - 6x + 10$ | Objective function |
> | Find: critical point and classify it | Determine whether the point is a maximum or minimum |
>
> **Step 1:** Differentiate the function.
>
> $$f'(x) = 2x - 6$$
>
> **Step 2:** Set the derivative equal to zero.
>
> $$2x - 6 = 0$$
>
> $$x = 3$$
>
> **Step 3:** Compute the second derivative.
>
> $$f''(x) = 2$$
>
> **Step 4:** Classify the point.
>
> Since $f''(3) = 2 > 0$, the point is a **local minimum**.
>
> **Step 5:** Evaluate the function value.
>
> $$f(3) = 3^2 - 6(3) + 10 = 1$$
>
> $$\boxed{\text{Local minimum } = 1 \text{ at } x = 3}$$

**Example 2 — Find a local maximum**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $g(x) = -x^2 + 4x + 1$ | Objective function |
> | Find: critical point and classify it | Determine whether the point is a maximum or minimum |
>
> **Step 1:** Differentiate the function.
>
> $$g'(x) = -2x + 4$$
>
> **Step 2:** Set the derivative equal to zero.
>
> $$-2x + 4 = 0$$
>
> $$x = 2$$
>
> **Step 3:** Compute the second derivative.
>
> $$g''(x) = -2$$
>
> **Step 4:** Classify the point.
>
> Since $g''(2) = -2 < 0$, the point is a **local maximum**.
>
> **Step 5:** Evaluate the function value.
>
> $$g(2) = -(2)^2 + 4(2) + 1 = 5$$
>
> $$\boxed{\text{Local maximum } = 5 \text{ at } x = 2}$$

---

### 6. First-Order Optimization Algorithms

**First-order optimization algorithms** use first-derivative information to improve an objective function iteratively. They do not require curvature information from second derivatives, which makes them more practical for large machine learning models.

These methods follow the slope: for minimization, move against the gradient; for maximization, move with the gradient. The step size, often called the learning rate, controls how aggressively the algorithm moves.

```
  Iterative descent on a loss curve

  Loss
  ▲
  │         • x0
  │       /
  │     • x1
  │    /
  │  • x2
  │ /
  │• x3
  └────────────────► parameter

  Each step moves toward lower objective value
```

#### Key Ideas

| Idea                   | Meaning                        | Practical effect                                         |
| :--------------------- | :----------------------------- | :------------------------------------------------------- |
| **Gradient**           | Direction of steepest increase | Use the negative gradient for minimization               |
| **Learning rate**      | Step size per update           | Too large can diverge; too small can be slow             |
| **Iteration**          | Repeated update step           | Improves the objective progressively                     |
| **Stopping criterion** | Rule for ending updates        | Based on small gradient, small change, or max iterations |

#### Real-World Use Cases

- **Machine Learning**: Neural networks and regression models are trained with first-order updates.
- **Signal Processing**: Adaptive filters update coefficients using error gradients.
- **Control Systems**: Online tuning can be framed as repeated first-order improvement.
- **Operations**: Iterative methods are used when closed-form optimization is unavailable.
- **Caveat**: Performance depends strongly on step size selection and problem scaling.

#### Steps

1. Choose an initial point for the decision variable.
2. Compute the first derivative or gradient at the current point.
3. Update the variable in the direction that improves the objective.
4. Recompute the objective and repeat the update.
5. Stop when the updates become small or a preset iteration limit is reached.

#### Formula

For minimization, a generic first-order update is:

$$
x_{k+1} = x_k - \eta f'(x_k)
$$

Where:
|  Symbol   | Pronunciation        | Meaning                    |
| :-------: | :------------------- | :------------------------- |
|   $x_k$   | "x sub k"            | Current iterate            |
| $x_{k+1}$ | "x sub k plus 1"     | Next iterate               |
|  $\eta$   | "eta"                | Learning rate or step size |
| $f'(x_k)$ | "f prime at x sub k" | Slope at the current point |

In multiple dimensions, the update becomes:

$$
\mathbf{x}_{k+1} = \mathbf{x}_k - \eta \nabla f(\mathbf{x}_k)
$$

Where:
|          Symbol          | Pronunciation                     | Meaning                       |
| :----------------------: | :-------------------------------- | :---------------------------- |
|      $\mathbf{x}_k$      | "x vector sub k"                  | Current parameter vector      |
| $\nabla f(\mathbf{x}_k)$ | "gradient of f at x vector sub k" | Vector of partial derivatives |
|          $\eta$          | "eta"                             | Learning rate or step size    |

#### Examples

**Example 1 — One first-order update in one dimension**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $f(x) = x^2$ | Objective function |
> | $x_0 = 3$ | Initial point |
> | $\eta = 0.1$ | Learning rate |
> | Find: $x_1$ | One update step for minimization |
>
> **Step 1:** Differentiate the objective.
>
> $$f'(x) = 2x$$
>
> **Step 2:** Evaluate the derivative at the current point.
>
> $$f'(3) = 6$$
>
> **Step 3:** Apply the update rule.
>
> $$x_1 = x_0 - \eta f'(x_0)$$
>
> $$x_1 = 3 - 0.1(6)$$
>
> **Step 4:** Simplify.
>
> $$x_1 = 3 - 0.6 = 2.4$$
>
> **Step 5:** Final answer.
>
> $$\boxed{x_1 = 2.4}$$

**Example 2 — Two first-order updates show iterative improvement**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $f(x) = (x - 1)^2$ | Objective function |
> | $x_0 = 5$ | Initial point |
> | $\eta = 0.25$ | Learning rate |
> | Find: $x_1$ and $x_2$ | Two update steps |
>
> **Step 1:** Differentiate the objective.
>
> $$f'(x) = 2(x - 1)$$
>
> **Step 2:** Compute the first update.
>
> $$f'(5) = 2(5 - 1) = 8$$
>
> $$x_1 = 5 - 0.25(8) = 3$$
>
> **Step 3:** Compute the second update.
>
> $$f'(3) = 2(3 - 1) = 4$$
>
> $$x_2 = 3 - 0.25(4) = 2$$
>
> **Step 4:** Compare objective values.
>
> $$f(5) = 16, \qquad f(3) = 4, \qquad f(2) = 1$$
>
> **Step 5:** Final answer.
>
> $$\boxed{x_1 = 3, \; x_2 = 2, \text{ and the objective decreases each step}}$$

---

<p align="left">
  <a href="./functions-and-calculus.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./gradient-methods.md"><b>Next →</b></a>
  </span>
</p>
