<p align="left">
  <a href="./index.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./optimization-foundations.md"><b>Next →</b></a>
  </span>
</p>

---

# Functions and Calculus

```
Functions and Calculus
├── 1. Linear and Nonlinear Functions
│   ├── Function notation and input-output mapping
│   ├── Linear form, slope, and intercept
│   ├── Nonlinear behavior and curvature
│   └── Comparing graph shapes and rates of change
│
├── 2. Function Differentiation and Rules of Derivatives
│   ├── Derivative as slope and instantaneous rate of change
│   ├── Power, product, quotient, and chain rules
│   └── Local sensitivity in engineering and ML
│
└── 3. Function Integration
    ├── Antiderivatives and indefinite integrals
    ├── Definite integrals as accumulation
    └── Area interpretation and total change
```

---

### 1. Linear and Nonlinear Functions

A **function** maps each allowed input to exactly one output. In engineering and machine learning, functions describe relationships such as force versus displacement, cost versus output, probability versus input features, and loss versus model parameters.

A **linear function** has a constant rate of change, so its graph is a straight line. A **nonlinear function** has a changing rate of change, so its graph bends, curves, oscillates, or grows unevenly.

```
Linear function                    Nonlinear function

y                                  y
▲                                  ▲
│       /                          │         *
│     /                            │      *
│   /                              │    *
│ /                                │  *
└──────────► x                     └──────────► x

Straight line                      Curved graph
Constant slope                     Changing slope
```

#### Linear vs Nonlinear Comparison

| Feature            | Linear Function                              | Nonlinear Function                                     |
| :----------------- | :------------------------------------------- | :----------------------------------------------------- |
| **Graph shape**    | Straight line                                | Curve or changing shape                                |
| **Rate of change** | Constant                                     | Variable                                               |
| **Typical form**   | $f(x) = mx + c$                              | $f(x) = ax^2 + bx + c$, $e^x$, $\frac{1}{x}$, $\tan x$ |
| **Modeling use**   | Simple trend approximation                   | Curvature, growth, decay, saturation, oscillation      |
| **Interpretation** | Equal input steps cause equal output changes | Equal input steps may produce different output changes |

#### Real-World Use Cases

- **Manufacturing**: Material cost is often approximated linearly when each additional unit requires the same amount of raw material.
- **Transportation**: Distance traveled at constant speed follows the linear relationship $d = vt$.
- **Machine Learning**: Linear regression captures straight-line trends, while neural networks are designed to approximate nonlinear behavior.
- **Reliability and population studies**: Exponential or logistic nonlinear functions model growth, decay, and saturation.
- **Caveat**: Linear models are interpretable, but they can underfit systems whose behavior changes with operating conditions.

#### Steps

1. Identify the independent variable and the dependent variable.
2. Examine whether the output changes by a constant amount when the input changes by one unit.
3. Write the algebraic form of the function and inspect powers, ratios, or transcendental terms.
4. Classify the function as linear or nonlinear.
5. Interpret what the form means in the application context.

#### Formula

For a linear function:

$$
f(x) = mx + c
$$

Where:
| Symbol | Pronunciation | Meaning                                 |
| :----: | :------------ | :-------------------------------------- |
| $f(x)$ | "f of x"      | Output value corresponding to input $x$ |
|  $m$   | "m"           | Slope or constant rate of change        |
|  $x$   | "x"           | Input or independent variable           |
|  $c$   | "c"           | Intercept, the output when $x = 0$      |

For a common nonlinear function:

$$
f(x) = ax^2 + bx + c
$$

Where:
| Symbol | Pronunciation | Meaning                           |
| :----: | :------------ | :-------------------------------- |
|  $a$   | "a"           | Coefficient controlling curvature |
|  $b$   | "b"           | Coefficient of the linear term    |
|  $c$   | "c"           | Constant term or intercept        |
|  $x$   | "x"           | Input or independent variable     |

#### Examples

**Example 1 — Classifying and evaluating a linear function**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $f(x) = 3x + 2$ | Function relating input to output |
> | $x = 4$ | Input value |
> | Find: function type and $f(4)$ | Determine whether the function is linear and compute the output |
>
> **Step 1:** Write down the linear form.
>
> $$f(x) = mx + c$$
>
> **Step 2:** Compare the given function with the linear form.
>
> $$f(x) = 3x + 2$$
>
> So, $m = 3$ and $c = 2$.
>
> **Step 3:** Classify the function.
>
> The variable $x$ appears only to the first power, so the rate of change is constant. The function is **linear**.
>
> **Step 4:** Substitute $x = 4$.
>
> $$f(4) = 3(4) + 2$$
>
> **Step 5:** Simplify and state the result.
>
> $$f(4) = 12 + 2 = 14$$
>
> $$\boxed{\text{Linear function and } f(4) = 14}$$

**Example 2 — Classifying and evaluating a nonlinear function**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $g(x) = x^2 - 4x + 1$ | Function relating input to output |
> | $x = 3$ | Input value |
> | Find: function type and $g(3)$ | Determine whether the function is nonlinear and compute the output |
>
> **Step 1:** Write the given function.
>
> $$g(x) = x^2 - 4x + 1$$
>
> **Step 2:** Inspect the structure of the function.
>
> The term $x^2$ means the input is raised to a power greater than 1.
>
> **Step 3:** Classify the function.
>
> Because the slope changes with $x$, the function is **nonlinear**.
>
> **Step 4:** Substitute $x = 3$.
>
> $$g(3) = 3^2 - 4(3) + 1$$
>
> **Step 5:** Simplify and state the result.
>
> $$g(3) = 9 - 12 + 1 = -2$$
>
> $$\boxed{\text{Nonlinear function and } g(3) = -2}$$

---

### 2. Function Differentiation and Rules of Derivatives

A **derivative** measures the instantaneous rate of change of a function. Geometrically, it is the slope of the tangent line at a specific point. In machine learning, derivatives quantify how sensitive a loss function is to parameter changes.

Differentiation converts a function into another function describing local behavior. This is central to optimization because gradient-based methods rely on derivatives to decide update direction and step tendency.

```
From secant line to tangent line (the limit idea)

y
▲
│             curve
│          *
│       *
│    *   • P ─────── secant through P and Q
│  *    /    •Q
│     /   (Q slides toward P)
│   /
└──────────────────► x

As Q → P, the secant line → tangent line
Derivative at P = slope of tangent line = lim of secant slope

Secant slope:   Δy/Δx  =  [f(x+h) − f(x)] / h
Tangent slope:  lim h→0  [f(x+h) − f(x)] / h  =  f'(x)
```

#### Common Derivative Rules

| Rule              | Formula                                                                             | Use                        |
| :---------------- | :---------------------------------------------------------------------------------- | :------------------------- |
| **Constant rule** | $\frac{d}{dx}(k) = 0$                                                               | Differentiate constants    |
| **Power rule**    | $\frac{d}{dx}(x^n) = nx^{n-1}$                                                      | Polynomial terms           |
| **Sum rule**      | $\frac{d}{dx}[f(x)+g(x)] = f'(x)+g'(x)$                                             | Differentiate term-by-term |
| **Product rule**  | $\frac{d}{dx}[f(x)g(x)] = f'(x)g(x)+f(x)g'(x)$                                      | Product of two functions   |
| **Quotient rule** | $\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x)-f(x)g'(x)}{[g(x)]^2}$ | Ratio of two functions     |
| **Chain rule**    | $\frac{d}{dx}[f(g(x))] = f'(g(x))g'(x)$                                             | Composite functions        |

#### Real-World Use Cases

- **Machine Learning**: Model parameters are updated using derivatives of the loss function.
- **Physics**: Velocity is the derivative of position, and acceleration is the derivative of velocity.
- **Economics**: Marginal cost and marginal revenue are found using derivatives.
- **Control Engineering**: Local sensitivity and response tuning use derivative information.
- **Caveat**: A derivative describes local behavior; it does not automatically guarantee global improvement.

#### Steps

1. Rewrite the function clearly and identify whether it is a sum, product, quotient, or composite function.
2. Select the appropriate derivative rule or combination of rules.
3. Differentiate each part carefully.
4. Simplify the resulting expression.
5. If needed, evaluate the derivative at a specific point to get the local slope.

#### Formula

The derivative is defined by the limit of the difference quotient:

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

Where:
|         Symbol          | Pronunciation                | Meaning                                      |
| :---------------------: | :--------------------------- | :------------------------------------------- |
|         $f'(x)$         | "f prime of x"               | Derivative of $f(x)$ with respect to $x$     |
|           $h$           | "h"                          | Small input change tending to zero           |
|      $f(x+h)-f(x)$      | "f of x plus h minus f of x" | Change in output                             |
| $\frac{f(x+h)-f(x)}{h}$ | "difference quotient"        | Average rate of change over a small interval |

For polynomial terms, the most used rule is:

$$
\frac{d}{dx}(x^n) = nx^{n-1}
$$

Where:
|     Symbol     | Pronunciation                | Meaning                           |
| :------------: | :--------------------------- | :-------------------------------- |
| $\frac{d}{dx}$ | "dee by dee x"               | Differentiate with respect to $x$ |
|     $x^n$      | "x to the power n"           | Power term                        |
|      $n$       | "n"                          | Exponent                          |
|   $nx^{n-1}$   | "n x to the power n minus 1" | Result after differentiation      |

#### Examples

**Example 1 — Differentiate a polynomial**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $f(x) = 4x^3 - 2x^2 + 7x - 5$ | Polynomial function |
> | Find: $f'(x)$ | Derivative of the function |
>
> **Step 1:** Write the power rule.
>
> $$\frac{d}{dx}(x^n) = nx^{n-1}$$
>
> **Step 2:** Differentiate each term.
>
> $$\frac{d}{dx}(4x^3) = 12x^2$$
>
> $$\frac{d}{dx}(-2x^2) = -4x$$
>
> $$\frac{d}{dx}(7x) = 7$$
>
> $$\frac{d}{dx}(-5) = 0$$
>
> **Step 3:** Add the results.
>
> $$f'(x) = 12x^2 - 4x + 7$$
>
> **Step 4:** Simplify.
>
> The derivative is already simplified.
>
> **Step 5:** Final answer.
>
> $$\boxed{f'(x) = 12x^2 - 4x + 7}$$

**Example 2 — Differentiate a composite function using the chain rule**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $g(x) = (3x^2 + 1)^5$ | Composite function |
> | Find: $g'(x)$ | Derivative of the function |
>
> **Step 1:** Identify the inner and outer functions.
>
> Inner function: $u = 3x^2 + 1$
>
> Outer function: $u^5$
>
> **Step 2:** Differentiate the outer function.
>
> $$\frac{d}{du}(u^5) = 5u^4$$
>
> **Step 3:** Differentiate the inner function.
>
> $$\frac{d}{dx}(3x^2 + 1) = 6x$$
>
> **Step 4:** Apply the chain rule.
>
> $$g'(x) = 5(3x^2 + 1)^4 \cdot 6x$$
>
> **Step 5:** Simplify and state the result.
>
> $$\boxed{g'(x) = 30x(3x^2 + 1)^4}$$

---

### 3. Function Integration

An **integral** reverses differentiation and measures accumulation. An **indefinite integral** gives a family of antiderivatives, while a **definite integral** gives a numerical value representing total accumulated change over an interval.

In engineering and machine learning, integration is used for total quantity calculations, area under curves, probability accumulation, and linking rate functions back to original state functions.

```
Area under a curve from a to b

y
▲
│           curve
│         *
│       *   *
│     *██████*
│   *██████████*
│ *██████████████*
└──a────────────b──► x

Definite integral = accumulated area/change
```

#### Key Identity — Fundamental Theorem of Calculus

Differentiation and integration are inverse operations. The **Fundamental Theorem of Calculus** connects them:

$$
\frac{d}{dx}\int_a^x f(t)\,dt = f(x)
$$

This means: if you integrate a function and then differentiate the result, you recover the original function. Conversely, a definite integral can be evaluated by finding any antiderivative.

---

#### Indefinite vs Definite Integrals

| Type                    | Notation                     | Meaning                                            |
| :---------------------- | :--------------------------- | :------------------------------------------------- |
| **Indefinite integral** | $\int f(x)\,dx$              | Family of antiderivatives plus constant $C$        |
| **Definite integral**   | $\int_a^b f(x)\,dx$          | Net accumulated value from $x=a$ to $x=b$          |
| **Output**              | Expression or number         | Function for indefinite, scalar value for definite |
| **Use**                 | Recovering original function | Computing area, total quantity, accumulated change |

#### Real-World Use Cases

- **Physics**: Integrating velocity gives displacement; integrating acceleration gives velocity.
- **Probability**: Continuous probability over an interval is found using a definite integral of a density function.
- **Economics**: Accumulated revenue or total production can be obtained by integrating rate functions.
- **Signal and systems engineering**: Integration is used to compute total energy and accumulated response.
- **Caveat**: A definite integral gives net signed area, so regions below the axis contribute negatively.

#### Steps

1. Determine whether the problem asks for an antiderivative or an accumulated value over an interval.
2. Rewrite the integrand into a form that matches known integration rules.
3. Apply the antiderivative rule term-by-term.
4. Add the constant of integration for indefinite integrals, or apply upper and lower bounds for definite integrals.
5. Simplify and interpret the result in context.

#### Formula

For an indefinite integral:

$$
\int x^n\,dx = \frac{x^{n+1}}{n+1} + C, \qquad n \ne -1
$$

Where:
| Symbol | Pronunciation      | Meaning                                   |
| :----: | :----------------- | :---------------------------------------- |
| $\int$ | "integral"         | Integration operator                      |
| $x^n$  | "x to the power n" | Integrand term                            |
|  $dx$  | "dee x"            | Indicates integration with respect to $x$ |
|  $C$   | "C"                | Constant of integration                   |
|  $n$   | "n"                | Exponent, not equal to $-1$               |

For a definite integral:

$$
\int_a^b f(x)\,dx = F(b) - F(a)
$$

Where:
|   Symbol    | Pronunciation         | Meaning                                 |
| :---------: | :-------------------- | :-------------------------------------- |
|     $a$     | "a"                   | Lower limit of integration              |
|     $b$     | "b"                   | Upper limit of integration              |
|   $f(x)$    | "f of x"              | Integrand or rate function              |
|   $F(x)$    | "F of x"              | An antiderivative of $f(x)$             |
| $F(b)-F(a)$ | "F of b minus F of a" | Net accumulated value over the interval |

#### Examples

**Example 1 — Find an indefinite integral**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $\int (6x^2 - 4x + 3)\,dx$ | Indefinite integral |
> | Find: antiderivative | Recover the original family of functions |
>
> **Step 1:** Write the integration power rule.
>
> $$\int x^n\,dx = \frac{x^{n+1}}{n+1} + C$$
>
> **Step 2:** Integrate each term separately.
>
> $$\int 6x^2\,dx = 6 \cdot \frac{x^3}{3} = 2x^3$$
>
> $$\int (-4x)\,dx = -4 \cdot \frac{x^2}{2} = -2x^2$$
>
> $$\int 3\,dx = 3x$$
>
> **Step 3:** Combine the antiderivatives.
>
> $$\int (6x^2 - 4x + 3)\,dx = 2x^3 - 2x^2 + 3x + C$$
>
> **Step 4:** Include the constant of integration.
>
> The constant $C$ is required because many functions have the same derivative.
>
> **Step 5:** Final answer.
>
> $$\boxed{2x^3 - 2x^2 + 3x + C}$$

**Example 2 — Evaluate a definite integral**

> **Given:**
>
> | Key Value | Description |
> | :--- | :--- |
> | $\int_1^3 (2x + 1)\,dx$ | Definite integral |
> | Find: accumulated value from $x=1$ to $x=3$ | Compute total change over the interval |
>
> **Step 1:** Find an antiderivative of the integrand.
>
> $$F(x) = \int (2x + 1)\,dx = x^2 + x$$
>
> **Step 2:** Apply the Fundamental Theorem of Calculus.
>
> $$\int_1^3 (2x + 1)\,dx = F(3) - F(1)$$
>
> **Step 3:** Evaluate at the upper limit.
>
> $$F(3) = 3^2 + 3 = 12$$
>
> **Step 4:** Evaluate at the lower limit.
>
> $$F(1) = 1^2 + 1 = 2$$
>
> **Step 5:** Subtract and state the result.
>
> $$\int_1^3 (2x + 1)\,dx = 12 - 2 = 10$$
>
> $$\boxed{10}$$

---

<p align="left">
  <a href="./index.md"><b>← Previous</b></a>
  <span style="float:right">
    <a href="./optimization-foundations.md"><b>Next →</b></a>
  </span>
</p>
