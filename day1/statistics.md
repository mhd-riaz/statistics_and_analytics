# Statistics

Is a tool that will be used to perform computation on dataset inorder to get meaningful insights.

could be classified into two categories

| descripitive statistics | inferential statistics    |
| :---------------------- | :------------------------ |
| used to understand data | helps in making decisions |


Population: represents entire group, represented with `N`
sample: a subset of a group, represented with `n`, should have min of 30 (cox of central limit theorem)

## descriptive statistics
```
Types
├── measures of central tendancy
│   ├── Mean/Avg
│   ├── Median
│   └── Mode
│
└── measure of variation/spread
    ├── Range
    ├── Quantile
    ├── IQR
    ├── Variance
    └── Standard Deviation
```

### measures of central tendancy
**Mean**: tells you about averge 
(sum of all values / n) 
(x bar) for avg of sample set
(meu) for avg of population set

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$


**Median**: a single measure cannont represent the whole group, coz outliers might impact the average result, thats where median comes into play.
e.g. a company salary's avg cannot tell whole employee's common salary, as some might earn more like CEO, some might earn very low, causing outliers

How to do median?
1. sort data
2. count number of obervations
3. find middle value
4. then take average of middle values

$$\text{Median} = \left(\frac{n+1}{2}\right)^{\text{th}} \text{ value}$$

**Mode**: most frequently occuring value

### measure of variation/spread
```
Types
├── Range
├── Quantile
├── IQR
├── Variance
└── Standard Deviation
```

$$\text{Median} = \frac{\left(\frac{n}{2}\right)^{\text{th}} + \left(\frac{n}{2} + 1\right)^{\text{th}}}{2}$$


**Range**:
uses min and max

$$
\text{Range} = [\min(x), \max(x)]
$$

**Variance**:

- uses all values, and compares with mean value

- high variance - diverse dataset; low variance - low diversification; zero variance - means dataset with single value, no useful information can be extracted

- sampling variation, depends on the dataset we choose

- confidence interval, help in finding the range of values

- bezels correction: which is used to keep sample set lower than population set, that why the n-1 in the variance formula

$$s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$$

**Standard Deviation**

- measures how spread out data points are from their average (mean)

- a low SD means data clusters near the mean, indicating consistency, while a high SD shows data spread over a wider range suggesting greater variability or dispersion

- often using the Greek letter sigma (σ) for population or 's' for samples

$$\sigma^2 = \frac{\sum (X - \mu)}{n}$$

## Types of data

1. **Numerical data**
   a. Also called quantitative data
   b. can be classsified into
      1. **Discrete** - anything that is countable (e.g. how many people, entered show at this time?)
      2. **Continious** - tho, represented as whole number, but they have infinite values inbetween them, e.g. timeseries or Keyword: **proportion**, **length**

2. **Non-numerical data**
   a. Aslo called qualitative/categorical data
   b. can be classsified into
      1. **Nominal** - some repeated value, cannot be ordered e.g. fav food in a class group
      2. **Ordinal** - where you can order it, ratings (bad < good < better < best)
      3. words - 
      4. open-ended(using sentiments)

interval:  cannot compare with other value, absolute zero value does not exists, comparison does not make sense
ratio: comparison is meaning full in ratios, zero exists