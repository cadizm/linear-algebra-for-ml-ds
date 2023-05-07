# Week 1

One of the main uses of derivatives in machine learning is to optimize functions,
specifically minimizing and maximizing functions.

For example, a way to find a model that fits a dataset in an optimal way is to calculate
a loss function and minimizing it.

---

# Loss functions

- Square loss
- Log loss

---

# Machine learning  motivation

- Prediction for linear regression problems
- Sentiment analysis for classification problems

Math concepts used in model training:

- Gradients
- Derivatives
- Optimization
- Loss and Cost functions
- Gradient descent
- Linear regression
- Classification
- Neural networks

---

# Derivatives motivation

A derivative is the instantaneous rate of change of a function.

For example, if a function is distance over a given time period, its derivative is
velocity.

---

# Derivatives and tangents

The instantaneous rate of change at for a given point in a graph on a 2-d plane is
equivalent to the slope of the tangent line at that point in the graph.

More generally, the instantaneous rate of change is a measure of how fast the relationship
between 2 variables is changing at any point.

This instantaneous rate of change is also called the derivative.

More formally, the derivative of a function at a point is the slope of the tangent at
that point.

---

# Slopes, maxima and minima

The min and max points in a graph occur at points where the derivative is 0 (meaning
that the its slope is 0 and its tangent line is horizontal).

---

# Derivative notation

Given

$$
\begin{align*}
\text{slope} & = {\text{vertical change} \over \text{horizontal change}} \\
& = {\Delta y \over \Delta x}
\end{align*}
$$

The derivative is

$$
\text{slope at a point} = {dy \over dx}
$$

where $dy$ and $dx$ represent infinitesimal changes in the $y$ and $x$ directions.

Given a function $f$, let $y$ be a function of $x$

$$
y = f(x)
$$

The derivative of $f$ can be expressed as:

$$
f'(x)   \tag{Lagrange notation}
$$

$$
{dy \over dx} = {d \over dx} f(x)  \tag{Leibniz notation}
$$

---

# Common derivatives

In general,

$$
\text{slope} = f'(x) = \lim_{\Delta x \rightarrow 0} {\Delta f \over \Delta x}
$$

## Constants (horizontal lines with 0 slope)

$$
y = f(x) = c \\
$$

$$
f'(x) = 0
$$

The slope of the line is 0 and so the derivative $f'(x) = 0$

## Non-horizontal lines

$$
y = f(x) = ax + b \\
$$

$$
f'(x) = a
$$

The slope of tangent line at $x$ is $a$, equal to the slope of the line.

## Quadratics

$\Delta f$ is the change in $f$ (i.e. the change in $y$).

$$
{y = f(x) = x^2} \\
$$

$$
{{\Delta f} \over {\Delta x}} = {{f(x + \Delta x) - f(x)} \over {\Delta x}} \\
$$

$$
{{\Delta f} \over {\Delta x}} = {{(x + \Delta x)^2 - (x)^2} \over {\Delta x}} \\
$$

$$
{df \over dx} = f'(x) = 2x \text{  as  } \Delta x \rightarrow 0
$$

## Cubics

$$
y = f(x) = x^3 \\
$$

$$
f'(x) = 3x^2 \text{  as  } \Delta x \rightarrow 0
$$

## Power functions in general

$$
y = f(x) = x^{-1} = {1 \over x}
$$

$$
f'(x) = -x^{-2}
$$

---

$$
y = f(x) = x^n \\
$$

$$
f'(x) = nx^{n-1} \text{  as  } \Delta x \rightarrow 0
$$

---

$$
f(x) = {1 \over x} \\
$$

$$
{df \over dx} = -{1 \over x^2}
$$


# The inverse function and its derivative

If $g(x)$ and $f(x)$ are inverses of one another:

$$
g(x) = f^{-1}(x) \\
$$

$$
g(f(x)) = x \\
$$

$$
g'(y) = {1 \over f'(x)}
$$

The derivative of $g$ is the reciprocal of the derivative of $f$.

# Derivative of trigonometric functions

$$
f(x) = \sin(x) \\
$$

$$
{df \over dx} = \cos(x)
$$

---

$$
f(x) = \cos(x) \\
$$

$$
{df \over dx} = -\sin(x)
$$

# Euler's number $e$

$$
e = \lim_{n\rightarrow\infty} {\left(1 + {1 \over n}\right)}^{n} = 2.71828182...
$$

# Derivative of $e^x$

$$
f(x) = e^x \\
$$

$$
{df \over dx} = e^x
$$

# Derivative of $\ln(x)$

$$
e^{\ln(x)} = x
$$

$$
f(x) = e^x
$$

$$
f^{-1}(y) = \ln(y)
$$

---

$$
{d \over dy} ln(y) = {1 \over e^{\ln(y)}} = {1 \over y}
$$

# Existence of the derivative

For a function to be differentiable at a point, the derivative has to exist for that
point.

For a function to be differentiable at an interval, the derivative has to exist for
_every_ point in the interval.

---

Non-differentiable functions.

$$
f(x) = |x| \\
$$

$$
\begin{equation*}
{df \over dx} =
\begin{cases}
\text{1, if x > 0} \\
\text{-1, if x < 0} \\
\text{does not exist, if x = 0} \\
\end{cases}
\end{equation*}
$$

---

$$
f(x) = x^{1 \over 3} \\
$$

$$
\begin{equation*}
{df \over dx} =
\begin{cases}
{1 \over 3}x^{-{2 \over 3}} \text{, if x } \ne 0 \\
\text{does not exist, if x = 0} \\
\end{cases}
\end{equation*}
$$

In general, non-differentiable functions are any functions with a:

1. cusp or a corner
2. jump discontinuity
3. vertical tangent

# Properties of the derivative

## Multiplication by scalars

$$
f = c \cdot g \\
$$

$$
f' = c \cdot g'
$$

where $c$ is a constant.

## Sum rule

$$
f = g + h \\
$$

$$
f' = g' + h'
$$

## Product rule

$$
f = gh \\
$$

$$
f' = g'h + gh'
$$

## Chain rule

$$
{d \over dt} f(g(h(t))) \\
$$

$$
= {df \over dg} \cdot {dg \over dh} \cdot {dh \over dt} \tag{Leibniz notation}
$$

$$
= f'(g(h(t))) \cdot g'(h(t)) \cdot h'(t)  \tag{Lagrange notation}
$$

---

If $f(x) = e^{2x}$, then $f'(x) = 2e^{2x}$

The derivative of $2x$ is $2$ and $f(x) = g(2x)$ where $g(x) = e^x$.

# Introduction to optimization

The main application of derivatives in machine learning is for optimization, finding
the minimum or maximum value of a function.

We use this to find the model that best fits a dataset by minimizing a cost or error
function.

We need to make sure to consider the multiple min/max (local) that have slope 0 to find
the overall globally optimum point.

# Optimization of squared loss

Minimize

$$
(x - a_1)^2 + (x - a_2)^2 + \cdots + (x - a_n)^2
$$

Solution

$$
x = {{a_1 + a_2 + \cdots + a_n} \over n}
$$

# Optimization of log-loss

Why the logarithm?

1. Derivative of products is hard, derivative of sums is easy
2. Product of lots of tiny things is tiny, but the logarithm of a very small number is
   a very large negative number

The takeaway is that in ML, when we have a very complicated product, we can try using
logarithms to simplify things, especially when taking derivatives.
