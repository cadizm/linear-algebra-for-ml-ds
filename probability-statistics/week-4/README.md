# Week 4

# Z Distribution

A **confidence interval** describes some degree of certainty for sample means.

$$
\text{lower limit} < \bar{x} < \text{upper limit}
$$

$\alpha$ is the significance level and $1 - \alpha$ gives a confidence level.

![confidence-interval](images/confidence-interval.png)
![confidence-interval-2](images/confidence-interval-2.png)
![confidence-interval-3](images/confidence-interval-3.png)

As the sample size increases, the confidence interval shrinks.

[Transcript](./z-distribution.txt)

# Margin of Error

![margin-of-error](images/margin-of-error.png)

[Transcript](./margin-of-error.txt)

# Calculation Steps

![confidence-interval-calculation](images/confidence-interval-calculation.png)

[Transcript](./confidence-interval-calculation.txt)

# Calculating Sample Size

What is the smallest sample size necessary to obtain a desired margin of error?

$$
\text{margin of error} = Z_{\frac{\alpha}{2}} \cdot \frac{\sigma}{\sqrt{n}}
$$

The necessary sample size $n$ for margin of error $MOE$ is

$$
n \ge \left( \frac{Z_{\frac{\alpha}{2}} \cdot \sigma}{MOE} \right)^2
$$

# Difference Between Confidence and Probability

![population-mean](images/population-mean.png)
![confidence-and-probability](images/confidence-and-probability.png)

[Transcript](./difference-between-confidence-and-probability.txt)

# Unknown Standard Deviation

![unknown-sigma](./images/unknown-sigma.png)
![t-distribution](./images/t-distribution.png)

[Transcript](./unknown-standard-deviation.txt)

# Unknown Mean and Standard Deviation

Given

- $\overline{X}$: sample mean
- $t_{\alpha / 2}$: student t
- $s$: sample standard deviation
- $n$: sample size

The confidence interval is:

$$
\left( \overline{X} - t_{\alpha / 2} \cdot \frac{s}{\sqrt{n}}, \overline{X} + t_{\alpha / 2} \cdot \frac{s}{\sqrt{n}} \right)
$$


# Confidence Interval for Proportions

How do you calculate a confidence interval for a given sample proportion?

![confidence-interval-proportions](images/confidence-interval-proportions.png)
![confidence-interval-proportions-example](images/confidence-interval-for-proportions-example.png)

[Transcript](./confidence-interval-for-proportion.txt)

# Defining Hypothesis

Null hypothesis $H_0$ and alternative hypothesis $H_1$ must be mutually exclusive and
have a true/false answer.

[Transcript](./defining-hypothesis.txt)

# Type I and Type II Errors

- Type I error (false positive)
    - you reject $H_0$ when it was actually true.
- Type II ( false negative)
    - you don't reject $H_0$ and the hypothesis was actually false

![type-i-type-ii-errors](./images/type-i-type-ii-errors.png)

Type I errors are more severe than Type II errors. What is the greatest probability
of Type I error you are willing to tolerate? This is called the **Significance level**
($\alpha$).

![significance-level](images/significance-level.png)

# Right-Tailed, Left-Tailed, and Two-Tailed Tests

![data-quality](./images/data-quality.png)
![test-statistic](./images/test-statistic.png)
![three-hypotheses](./images/three-hypotheses.png)

[Transcript](./right-left-two-tailed-tests.txt)

# p-Value

A **p-value** is the probability, assuming $H_0$ is true, that the test statistic takes
on a value as extreme as or more extreme than the value observed.

This means that from the observed value you moved the direction of $H_1$.

- If p-value is less than $\alpha$ reject $H_0$ and accept $H_1$ as true.
- If p-value is greater than $\alpha$ don't reject $H_0$.

![p-values](images/p-values.png)
![z-statistic](images/z-statistic.png)

[Transcript](./p-value.txt)

# Critical Values

- You can define the critical value in advance
- For a given sample, using p-value and critical value will lead to the same conclusion
- Defining a test in terms of critical values makes possible determining Type II error
- probabilities for the decision rule

![p-value-vs-critical-value](images/p-value-vs-critical-value.png)
![compute-critical-value](images/compute-critical-value.png)
![critical-value-decision-rules](images/critical-value-decision-rules.png)

[Transcript](./critical-values.txt)

# Power of the Test

![finding-type-ii-error-probabilities](images/finding-type-ii-error-probabilities.png)
![power-of-the-test](images/power-of-the-test.png)

[Transcript](./power-of-the-test.txt)

# Interpreting Results

![steps-hypothesis-testing](images/steps-hypothesis-testing.png)
![interpreting-tests-1](images/interpreting-tests-1.png)
![interpreting-tests-2](images/interpreting-tests-2.png)

[Transcript](./interpreting-results.txt)

# t-Distribution

![t-distribution](images/t-distribution-2.png)
![t-statistic](images/t-statistic.png)

[Transcript](./t-distribution.txt)

# t-Tests

![t-test-right-tail](images/t-test-right-tail.png)
![t-test-two-tail](images/t-test-two-tail.png)
![t-test-left-tail](images/t-test-left-tail.png)

[Transcript](./t-tests.txt)

# Test for Proportions

[Test for Proportions](./test-for-proportions.md)

# Two Sample t-Test

![two-sample-t-test-assumptions](images/two-sample-t-test-assumptions.png)
![two-sample-t-test-statistic](images/two-sample-t-test-statistic.png)

[Transcript](./two-sample-t-test.txt)

# Two Sample Test for Proportions

[Two Sample Test for Proportions](./two-sample-tests-for-proportions.md)

# Paired t-Test

![paired-t-test](images/paired-t-test.png)
![paired-t-test-statistic](images/paired-t-test-statistic.png)
![paired-t-test-right-tailed-test](images/paired-t-test-right-tailed-test.png)

[Transcript](./paired-t-test.txt)

# ML Application: A/B Testing

[Transcript](./a-b-testing.txt)
