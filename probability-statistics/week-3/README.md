# Week 3

# Population and Sample

**Population** $(N)$ is the entire group of individuals or elements you want to study
which share a common behavior.

**Sample** $(n)$ is the subset of the population you use to draw conclusions about the
population as a whole.

Important properties for samples in order to make representative estimates of population:

- Random
- Independent (repetition allowed)
- Identically distributed

# Sample Mean

Given an actual mean of $\mu$, we define our first sample's mean as $\bar{x}_1$.

In general the larger the sample size, the better the estimate of population mean.

# Sample Proportion

Given an entire population, **population proportion** is

$$
p = \frac{\text{number of items with a given characteristic $(x)$}}{\text{population $(N)$}}
$$

Given a sample of the population, **sample proportion** is

$$
\hat{p} = \frac{\text{number of items with a given characteristic $(x)$}}{\text{sample $(n)$}}
$$

# Sample Variance

Recall that variance describes how much values in a dataset deviate from the mean.
**Population variance** is defined as


$$
\sigma^2 = \frac{1}{N} \sum (x - \mu)^2
$$

![sample-variance](images/sample-variance.png)

where $N$ is population size and $\mu$ is population mean. The question then is how to
estimate **sample variance** using a sample of the population?

The answer is that we divide not by the population size $N$, but 1 minus the sample size
$n$.

$$
Sample \space Var(x) = \frac{1}{n - 1} \sum (x - \bar{x})^2
$$

# Law of Large Numbers

As the sample size increases, the average of the sample will tend to get closer to the
average of the entire population.

- $n$: number of samples
- $X_i$: some estimate $X$ for sample $i$

As $n \rightarrow \infty$

$$
\frac{1}{n} \sum_{i=1}^n X_i \rightarrow \mathbb{E}[X] = \mu_X
$$

given certain conditions:

- Sample is randomly drawn
- Sample size must be sufficiently large
- Observations are independent (of each other)

# Central Limit Theorem

Given any distribution, no matter how skewed, take many samples, compute the mean and
plot them. Your resulting plot will have a normal/Gaussian distribution. This applies
to both discrete and continuous random variables.

![clt-1](images/clt-1.png)

As $n$ becomes sufficiently large we get a normal distribution where

$$
\bar x \approx \mu  = n p
$$

$$
\sigma^2 \approx n p (1 - p)
$$

$$
\mu_{\bar x} = \mu
$$

$$
\sigma_{\bar x}^2 = \frac{\sigma^2}{n}
$$

---

More formally, the Central Limit theorem states that that mean of sample means, when
standardized, has a standard normal distribution.

$$
\frac{\frac{1}{n} \sum_{i=1}^n X_i - \mathbb{E}[X]}{\sigma_X} \sqrt{n} \sim \mathcal{N}(0, 1)
$$


