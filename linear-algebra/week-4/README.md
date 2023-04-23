# Week 4

[Principal component analysis](https://en.wikipedia.org/wiki/Principal_component_analysis)

PCA is a technique for reducing datasets of high-dimensionality to lower dimensionality,
while preserving the maximum amount of information.

This is used to aid in the visualization of multi-dimensional data.

---

# Singularity and rank of linear transformations

When a matrix is singular the image of its corresponding linear transformation does not
cover the entire plane in its new basis.

Another way to calculate the rank of a matrix is the rank of the image of its linear
transformation.

---

# Determinant as an area

The determinant of a matrix is equivalent to the area of image of the fundamental basis
formed by the basis unit square (the fundamental square).

---

# Determinant of a product of matrices

```
3  1  *   1  1  =   1  4
1  2     -2  1     -3  3

det = 5   det = 3   det = 15
```

Notice that `5 * 3 = 15`

In general

```
det(A * B) = det(A) * det(B)
```

# Determinants of inverses

$$
\begin{bmatrix}
3 & 1 \\
1 & 2 \\
\end{bmatrix}^{-1} =
\begin{bmatrix}
0.4 & -0.2 \\
-0.2 & 0.6 \\
\end{bmatrix}
$$

$$
det \begin{bmatrix}
3 & 1 \\
1 & 2 \\
\end{bmatrix}^{-1} = 5
$$

$$
det \begin{bmatrix}
0.4 & -0.2 \\
-0.2 & 0.6 \\
\end{bmatrix} = 0.2
$$

$$
5^{-1} = 0.2
$$

In general, for invertible matrices:

$$
det(A^{-1}) = \frac{1}{det(A)}
$$

---

# Basis in Linear Algebra

The main property of a basis is that every point in the vector space can be expressed as
a linear combination of the elements in the basis.

# Span in Linear Algebra

The span of a set of vectors is the set of points that can be reached by walking in the
direction of the vectors in any combination.

---

By definition, a basis is a _minimal_ spanning set.

The number of elements in the basis is equivalent to the dimensionality of the space.

# Eigenbasis

`Eigen`, derived from German means "characteristic", "proper", or literally "own".

```
2  1
0  3

(1, 0) -> (2, 0)
(0, 1) -> (1, 3)
```

The linear transformation of a set of basis vectors to its image vectors is called a
change of basis.

A basis with linear transformation consisting only of a scaling of its basis vectors
is called an eigenbasis.

The vectors in the eigenbasis are `eigenvectors` and the scaling factors (coefficients)
are the `eigenvalues`.

The use of eigenvectors and eigenvalues simplifies linear algebra calculations.

---

# Finding eigenvalues

```
2  1     |     3  0
0  3     |     0  3
```

```
2  1  x  =  3  0  x
0  3  y     0  3  y
```

$$
\begin{pmatrix}
\begin{bmatrix}
2 & 1 \\
0 & 3
\end{bmatrix} -
\begin{bmatrix}
3 & 0 \\
0 & 3
\end{bmatrix}
\end{pmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix} =
\begin{bmatrix}
0 \\
0
\end{bmatrix}
$$

$$
\begin{bmatrix}
-1 & 1 \\
0 & 0
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix} =
\begin{bmatrix}
0 \\
0
\end{bmatrix}
$$

$$
det \begin{bmatrix}
-1 & 1 \\
0 & 0
\end{bmatrix} = 0
$$

If $\lambda$ is an eigenvalue:

$$
\begin{bmatrix}
2 & 1 \\
0 & 3
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix} =
\begin{bmatrix}
\lambda & 0 \\
0 & \lambda
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

For infinitely many $(x, y)$

$$
\begin{bmatrix}
2 - \lambda & 1 \\
0 & 3 - \lambda
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix} =
\begin{bmatrix}
0 \\
0
\end{bmatrix}
$$

has infinitely many solutions.

$$
det \begin{bmatrix}
2 - \lambda & 1 \\
0 & 3 - \lambda
\end{bmatrix} = 0
$$

And the `characteristic polynomial` is

$$
(2 - \lambda)(3 - \lambda) - (1 \cdot 0) = 0
$$

So the eigenvalues are

$$
\lambda = 2, \lambda = 3
$$

# Finding eigenvectors

The eigenvectors are the vectors that satisfy the equation:

$$
\text{matrix * vector = eigenvalue * vector}
$$

Which gives the equations

$$
\begin{array}{l l l}
\begin{bmatrix}
2 & 1 \\
0 & 3
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix} =
2
\begin{bmatrix}
x \\
y
\end{bmatrix}
& , &
\begin{bmatrix}
2 & 1 \\
0 & 3
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix} =
3
\begin{bmatrix}
x \\
y
\end{bmatrix}
\end{array}
$$

which is equivalent to

$$
\begin{matrix}
2x + y = 2x & , & 2x + y = 3x \\
0x + 3y = 2y & , & 0x + 3y = 3y
\end{matrix}
$$

Solving for $x$ and $y$

$$
\begin{matrix}
x = 1 & , & x = 1 \\
y = 0 & , & y = 1
\end{matrix}
$$

gives

$$
\begin{bmatrix}1 \\
0
\end{bmatrix}
,
\begin{bmatrix}1 \\
1
\end{bmatrix}
$$

as eigenvectors. Note that any scaled multiple of these vectors is also an eigenvector.


# Supplemental videos

- [Eigenvectors and Generalized Eigenspaces](https://www.youtube.com/watch?v=ajXb3N6QEqc)
- [Principal Component Analysis (PCA)](https://www.youtube.com/watch?v=g-Hb26agBFg)
