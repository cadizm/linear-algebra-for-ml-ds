# Week 2

We now consider functions of more than a single variable.

Given $f(x, y) = x^2 + y^2$

If we treat $y$ as a constant, we now have a function of a single variable, $x$.

The slope of this function with respect to $x$ and $y$ fixed is partial derivative.

$$
f(x, y) = x^2 + y^2
$$

$$
{\partial f \over \partial x} = 2x + 0
$$

We can take the partial derivative with respect to each variable.

$$
f(x, y)
$$

$$
\begin{array}{lll}
f_x = {\partial f \over \partial x} & , & f_y = {\partial f \over \partial y} \\
\end{array}
$$

Partial derivative of $f$ with respect to $x$, and partial derivative of $f$ with respect
to $y$.

---

An example

$$
f(x, y) = 3x^2y^3
$$

$$
{\partial f \over \partial x} = 6xy^3
$$

$$
{\partial f \over \partial y} = 9x^2y^2
$$

# Gradients

Given $f(x, y) = x^2 + y^2$, ${\partial f \over \partial x} = 2x$ and
${\partial f \over \partial y} = 2y$.

The gradient is the vector containing the 2 partial derivatives

$$
\begin{bmatrix}
2x \\
2y
\end{bmatrix}
$$

In general we denote the gradient using the "nabla" symbol, which is a vector of all the
partial derivatives with respect to all of the variables in the function.

$$
\nabla f =
\begin{bmatrix}
\frac{\partial f}{\partial x} \\
\frac{\partial f}{\partial y}
\end{bmatrix}
$$

---

Let $f(x, y) = x^2 + y^2$, calculate the gradient $f$, $\nabla f$, at $(2, 3)$

$$
\begin{equation}
\begin{bmatrix}
2 \cdot 2 \\
2 \cdot 3
\end{bmatrix} =
\begin{bmatrix}
4 \\
6
\end{bmatrix}
\end{equation}
$$

---

# Gradients and maxima/minima

The gradient is useful in minimizing functions of 2 or more variables in the same way
as the derivative is useful minimizing functions of a single variable.

The minimum a function $f$ occurs when the slopes of all the tangent lines given by the
partial derivatives are $0$.

In general, set all the partial derivatives to $0$, and solve that system of equations.

---

For example, to find the **minimum value** (not point) that the function
$f(x, y) = x^2 + 2y^2 + 8y$ can output: compute the gradient given by

$$
\nabla f(x, y) = \left({\partial f \over \partial x}, {\partial f \over \partial y}\right)
$$

and find all points such that $\nabla f(x, y) = (0, 0)$

$$
\left({\partial f \over \partial x}, {\partial f \over \partial y}\right) = (2x, 4y + 8)
$$

Solving for $x$ and $y$

$$
\begin{array}{ll}
x = 0 \\
y = -2
\end{array}
$$

Substituting back into the original equation

$$
\begin{align*}
f(0, -2) & = 0^2 + 2(-2)^2 + 8(-2) \\
& = -8
\end{align*}
$$

# Linear Regression

$$
E(m, b) = 14m^2 + 3b^2 + 38 + 12mb - 42m - 20b
$$

$$
{\partial E \over \partial m} = 28m + 12b - 42 = 0
$$

$$
{\partial E \over \partial b} = 6b + 12m - 20 = 0
$$

Solving for $m$ and $b$

$$
\begin{array}{ccc}
12b + 24m - 40 = 0 \\
4m - 2 = 0 \\
m = {2 \over 4} = 0.5
\end{array}
$$

$$
\begin{array}{ccc}
6b + 12(0.5) - 20 = 0 \\
6b + 6 - 20 = 0 \\
b =  {14 \over 6} = {7 \over 3}
\end{array}
$$

This example only required solving an equation with 2 variables and 2 unknowns.

But imagine a problem with many unknowns. In general, solving an $m \cdot n$ system of equations can be compute intensive and performance can be improved upon using gradient
descent.

# Gradient Descent

Motivation: hard to optimize functions.

$$
f(x) = e^x - \log(x)
$$

$$
f'(x) = e^x - \frac{1}{x}
$$

Find minimum by setting equation to $0$ and solving

$$
f'(x) = e^x - \frac{1}{x} = 0 \\
$$

$$
e^x = \frac{1}{x}
$$

Solving analytically this is not so straightforward. The solution is $x = 0.5671...$,
also known as the Omega constant.

We can try a "binary search" method for finding the minimum by choosing a point, then
checking in both directions (left and right), if the new points are closer than the
current point. We terminate when both points are further from the minimum than the
current point.

One way we can try to improve upon this method is to use the function itself for hints
on which direction to choose for the next point and the distance to move from the current
point.

We can use derivative (slope) of the current point and if it is positive, move left. And
if it is negative, move right.

$$
\text{new point} = \text{old point} - \text{slope} \\
$$

$$
x_1 = x_0 - f'(x_0)
$$

When the slope of the current point is very steep, the derivative is very large which will
lead to a  large next step, which can be chaotic and cause the algorithm to oscillate
between 2 points.

We introduce a learning rate, denoted $\alpha$, to ensure that the steps used are small
enough so that the algorithm can converge to the minimum.

$$
x_1 = x_0 - \alpha f'(x_0)
$$

The method we have just described is called Gradient Descent and it proceeds iteratively
to converge at the minimum using the following steps:

Function: $f(x)$ \
Goal: find minimum of $f(x)$

- Step 1:
    - Define a learning rate $\alpha$
    - Choose a starting point $x_0$
- Step 2:
    - Update $x_k = x_{k-1} - \alpha f'(x_{k-1})$
- Step 3:
    - Repeat Step 2 until you are close enough to the true minimum (you can tell when
      you are close to the true minimum when your steps don't change much from the
      current location)

Notice that we never need to solve the _equation_ for the derivative equaling $0$, we
only need to apply the derivative in order to find the next point for consideration.

---

Challenges with gradient descent

- Finding a good learning rate
    - too big: may never converge
    - too small: take a very long time to converge
- Converges to a local minima instead of a global minima
    - Run the algorithm several times with several different starting points

## Gradient descent in two variables

Initial position: $(x_0, y_0)$ \
Direction of greatest ascent: $\nabla f$ \
Direction of greatest descent: $-\nabla f$ \
Updated position: $(x_1, y_1) = (x_0, y_0) - \alpha \nabla f$

This are the same steps as gradient descent in 1 variable, except instead of using the
_derivative_, we use the _gradient_ (the partial derivatives with respect to each
variable).

Function: $f(x, y)$ \
Goal: find minimum of $f(x, y)$

- Step 1:
    - Define a learning rate $\alpha$
    - Choose a starting point $(x_0, y_0)$
- Step 2:
    - Update

$$
\begin{bmatrix}x_k \\
y_k\end{bmatrix} =
\begin{bmatrix}x_{k-1} \\
y_{k-1}\end{bmatrix} - \alpha \nabla f(x_{k-1}, y_{k-1})
$$

- Step 3:
    - Repeat Step 2 until you are close enough to the true minimum (you can tell when
      you are close to the true minimum when your steps don't change much from the
      current location)

# Links

* [Difference between linear regression and gradient descent](https://stackoverflow.com/questions/68722976/difference-between-linear-regression-and-gradient-descent)
* [Analytical vs Gradient Descent methods of solving linear regression](https://atmamani.github.io/projects/ml/coursera-linear-regression-analytical-solution/)
