# Week 3

---

# Vectors

A vector is a tuple of numbers.

2-d vector: (4, 3)
3-d vector: (4, 3, 1)

Vectors in a space have both `magnitude` and `direction`.

"Taxi-cab" distance using L1-norm vs "helicopter" distance using L2-norm. This is also
known as Manhattan distance and Euclidean distance respectively.

The norm of a vector `v` an be defined as (length, magnitude) and denoted `|v|`.

The L1-norm that is calculated as the sum of the absolute values of the vector.
The L2-norm that is calculated as the square root of the sum of the squared vector values.

Distances between vectors computed using the L1 or L2 norms/distances can be used to
measure similarities between vectors.

The distance between 2 vectors is the square root of the sum of squared differences of
the components of the vector.

The magnitude of the vector from 1 vector to another is the distance between the 2
vectors.

The sum of 2 vectors is the diagonal in the parallelogram formed by the 2 vectors.

# Dot product

```
Quantities       Prices      Total price
----------------------------------------
2 apples         $3          2 * 3 =  6
4 bananas        $5          4 * 5 = 20
1 cherry         $2          1 * 2 =  2
```

```
2                 3
4                 5          28
1                 2
```

```
          3
2 4  1 *  5 = 28
          2
```

We can define the L2-norm of a vector `u` in terms of the dot product operation.

The L2-norm of a vector is the square root of the dot product of the vector and itself:

```
L2-norm(u) = sqrt(dot_product(u, u))
```

This also means that the dot product of a vector is the L2-norm squared.

# Geometric dot product

Two vectors are orthogonal (perpendicular) iff their dot product is 0.

# Matrix multiplication by vector

Using what we know so far, we can define a linear system of equations as by a vector as
the combination of the dot products of each of the equations in the system.

```
a +  b +  c = 10    |    1  1  1   a   10
a + 2b +  c = 15    |    1  2  1 * b = 15
a +  b + 2c = 12    |    1  1  2   c   12
```

# Matrices as linear transformations

The following example is in 2 dimensions, but higher dimensions follow similarly.

```
3  1  x
1  2  y
```

For the point `(x, y) = (0, 0)`, the 2x2 matrix performs a linear transformation which
results in the point `(0, 0)`

```
(0, 0) -> (0, 0)
(1, 0) -> (3, 1)
(0, 1) -> (1, 2)
(1, 1) -> (4, 3)
```

The points to the left of `->` and the points to the right of `->` form what is called
a `basis`.

An important property of a basis is that it can describe the entire plane.

# Linear transformations as matrices

```
(0, 0) -> (0,  0)
(1, 0) -> (3, -1)
(0, 1) -> (2,  3)
(1, 1) -> (5,  2)
```

In this case, we actually only need `(1, 0)` and `(0, 1)`

```
(1, 0) -> (3, -1)
(0, 1) -> (2,  3)

 3  2  * [1  0] = [3  -1]
-1  3

 3  2  * [0  1] = [2  3]
-1  3

->
3  -1
2   3
```

# Matrix multiplication

Matrix multiplication can be thought of as combining 2 linear transformations into a
3rd new linear transformation.

```
3  1   1   ->  3
1  2   0       1

3  1   0   ->  1
1  2   1       2
```

```
2  -1   3   ->  5
0   2   1       2

2  -1   1   ->  0
0   2   2       4
```

```
2  -1  *  3  1  =  5  0
0   2     1  2     2  4
```

# Identity matrix

1's in the diagonal and 0's everywhere else.

```
1  0  0  0     a     a
0  1  0  0  *  b  =  b
0  0  1  0     c     c
0  0  0  1     d     d
```

```
(0, 0) -> (0, 0)
(1, 0) -> (1, 0)
(0, 1) -> (0, 1)
(1, 1) -> (1, 1)
```

---

# Matrix inverse

The inverse of a number is the number that yields 1 when it is multiplied by the
original number.

The inverse of 2 is 1/2.

```
2 * 1/2 = 1
```

The same idea can be applied to matrices.

```
3  1  *  a  b  =  1  0
1  2     c  d     0  1
```

To find the inverse:

```
3  *  a  c  =  1      |     3a + 1c = 1
1                     |
                      |
3  *  b  d  =  0      |     3b + 1d = 0
1                     |
                      |
1  *  a  c  =  0      |     1a + 2c = 0
2                     |
                      |
1  *  b  d  =  1      |     1b + 2d = 1
2                     |
```

---

# Which matrices have an inverse?

Just like numbers (such as 0), some matrices have no inverse.

Looking at a few examples, we might be able to infer that a matrix has an inverse iff
it is non-singular. That is, singular matrices have no inverse.

We call matrices that have an inverse, `invertible`. And matrices that have no inverse,
`non-invertible`.

Because an invertible matrix is non-singular, its determinant is non-zero.  And the
determinant of a singular matrix is zero.

---

# Neural networks and matrices

Classifier example

A 1-layer neural network can be seen as a matrix product followed by a threshold check
(the activation).

Another name for a 1-layer neural network is a perceptron.
