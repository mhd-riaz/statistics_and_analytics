# Population vs Sample

| Population                                                            | Statistics                                                    |
| :-------------------------------------------------------------------- | :------------------------------------------------------------ |
| Population is referred with $\mu$                                     | Sample is referred with $\bar{x}$                             |
| Parameter - **characteristics of a population**, represented with $p$ | Statistics - summary about sample, represented with $\hat{p}$ |

---

| Co-variance | Cor-relation |
| :---------- | :----------- |
| cov(x,y)    |              |

Co-variance Forumla: 

$\text{cov}(x,y)^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{n-1}$


Variance Formula:

$\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}$


then var(x) can be written as `var(x) = cov(x,x)`

**Covariance Matrix**:

A Covariance Matrix is a square, symmetric matrix that summarizes the relationships between multiple variables in a dataset, showing how they vary together; its diagonal elements are the variances (spread) of each variable, while the off-diagonal elements show the covariance (direction and strength of linear relationship) between different pairs of variables, with positive values meaning they tend to rise/fall together and negative values meaning they move in opposite directions, crucial in statistics, machine learning (like PCA), and finance. 

- can be positive, negative, zero
- increase in x, increases y also, then its related
- if increase in x, decrease in y, then indirectly propertional
- this just tell about the direction of relation, but if you want to measure the strength then use co-relation
- is associate with units

**Co-relation Matrix**:

A correlation matrix is a table that displays the correlation coefficients between multiple variables, showing the strength and direction of their linear relationships in a single view, with values from -1 (perfect negative) to +1 (perfect positive), and 0 meaning no correlation; it's a key tool in data analysis to spot patterns, summarize data, and inform advanced modeling. 

- for sample $r$
- for population $\hat{r}$

```
ρ(x, y) = Cov(x, y) / (σₓ * σᵧ)
```
$$
\\rho_{X,Y} = \\frac{\\text{cov}(X,Y)}{\\sigma_X \\sigma_Y}
$$

$$
\\rho_{X,Y} = \\frac{\\sum_{i=1}^{n} (X_i - \\bar{X})(Y_i - \\bar{Y})}{\\sqrt{\\sum_{i=1}^{n} (X_i - \\bar{X})^2 \\sum_{i=1}^{n} (Y_i - \\bar{Y})^2}}
$$


where:
- xᵢ, yᵢ: Individual data points.
- x̄, ȳ: Mean (average) of x and y.
- n: Number of data points. 


$$
\mathbf{R} = \begin{bmatrix}
r_{11} & r_{12} & \cdots & r_{1n} \\
r_{21} & r_{22} & \cdots & r_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
r_{n1} & r_{n2} & \cdots & r_{nn}
\end{bmatrix}
= \begin{bmatrix}
1 & r_{12} & \cdots & r_{1n} \\
r_{21} & 1 & \cdots & r_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
r_{n1} & r_{n2} & \cdots & 1
\end{bmatrix}
$$


Pearson Corelation co-efficient

$
r_{ij} = \frac{\text{cov}(X_i, X_j)}{\sigma_{X_i} \sigma_{X_j}}
$


weakly related < 0.5

strongly related > 0.8


The same thing can be done with scatter plot, but the mathematical way is to first find co-relation and co-variance


any analysis with two variables is called bi variate analysis
1 variable - uni variate analysis
3 or more - multi variate analysis


NOTE:
always use independant variable in x axis & in y axis use dependant variable

if `mean ~= median ~= mode` then data is symentrically distributed
- if `mean > median` then it is right/positively skewed
- if `mean < median` then its left/negatively skewed
- if `mean ~= median ~= mode` then symentric distribution



# Sampling techniques

- Random sampling techniques
  - probability
  - Types:
    1. **Simple Random Sampling** : just random
    2. **Stratified Sampling**: picking up groups then making a sample
    3. **Cluster Sampling**: categorize as clusters then sample it
    4. **Systematic Sampling** : select every 10th student in a set of 1000 student list if i want 100 samples, but randomly pick 1st number, but proceed with n increments, where n is the systematic plan
- Non random sampling techniques
  - non-probability
  - Types:
    1. **Snow ball**: where initial participants refer other potential subjects from their social networks, allowing the sample to grow like a rolling snowball
    2. **Convenience**: based on our convenience 
    3. **Judgemental**: domain knowledge plays a role on selecting  