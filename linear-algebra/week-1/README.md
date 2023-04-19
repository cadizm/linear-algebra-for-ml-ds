# Week 1

A system is `singular`, if it is redundant or contradictory.

A system is `non-singular`, if it is complete.

Completeness is defined as carrying the same number of pieces of information as
number of sentences.

---

```
a + b = 10
a + (2 * b) = 12
=>
a = 10 - b
10 - b + (2 * b) = 12
-b + (2 * b) = 2
b = 2
=>
a = 8
```

---

# Complete & Non-singular
Systems of equations that are complete (non-singular) have one unique solution.

# Redundant & Singular
Systems of equations that are redundant have infinitely many solutions.

# Contradictory & Singular
Systems of equations that have contradictory information have no solutions.

---

# Visualizing systems of linear equations

Systems of equations that are complete (non-singular) have one unique solution; where
the lines intersect.

Systems of equations that are redundant have infinitely many solutions; where the lines
all the same, and all points on the lines are solutions to the system of equations.

Systems of equations that have contradictory information have no solutions; where the
lines never intersect (are parallel)

---

# Singular vs non-singular geometric interpretation

We can ignore the constants in systems of linear to more easily determine if the system
is non-singular. When we set the constants to 0 in each equation, each line will pass
through the origin. If they all intersect, they are non-singular. Else the system is
singular.

---

# Systems of equations as matrices

```

a +  b = 0             |    a +  b = 0
a + 2b = 0             |   2a + 2b = 0
                       |
1 1                    |   1 1
1 2                    |   2 2
                       |
non-singular matrix    |   singular matrix
unique solution        |   infinitely many solutions
linearly independent   |   linearly dependent (second matrix row is multiple of first)
```

---

# The determinant

By definition, a matrix must be a "square matrix" (same number of row and columns) in
order to compute its determinant.

After computing the determinant of a matrix M:
  if `det(M)` is non-zero, the matrix is non-singular

```
 a +  b = 0
2a + 2b = 0

 a    b
 c    d

Matrix is singular if

[a b] * k = [c d]

ak = c
bk = d

c/a = d/b = k

ad = bc

ad - bc = 0

det(M) = ad - bc
```

`ad` is the product of the numbers in the "main diagonal"
`bc` is the product of the numbers in the "main anti-diagonal"

---

# NumPy

`ndarray` object encapsulates n-dimensional arrays of homogeneous data types.

Vectorized element-by-element operations are the "default mode" for `ndarray`'s.

Broadcasting is the term used to describe the implicit element-by-element behavior
of operations.

In NumPy, dimensions are called _axes_.

```python
# 3d array with shape (2, 3, 4)
np.arange(24).reshape(2, 3, 4)

[
  [
    [ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]
  ]

  [
    [12 13 14 15]
    [16 17 18 19]
    [20 21 22 23]
  ]
]
```

---

# Systems of Linear Equations

```
a +  b +  c = 10
a + 2b +  c = 15  -> b = 5
a +  b + 2c = 12  -> c = 2
                  -> a = 3
-> non-singular
```

```
a +  b +  c = 10
a +  b + 2c = 15  -> c = 5
a +  b + 3c = 20  -> 2c = 10
                  -> c = 5
-> singular and redundant, infinitely many solutions
```

```
a +  b +  c = 10
a +  b + 2c = 15  -> c = 5
a +  b + 3c = 18  -> 2c = 8
                  -> c = 4
-> singular and contradictory, no solutions
```

```
 a +  b +  c = 10
2a + 2b + 2c = 20
3a + 3b + 3c = 30

-> singular and redundant, infinitely many solutions
```

---

# Linear dependence and independence

```
1  0  1
0  1  0
3  2  3

-> 3row1 + 2row2 = row3
-> linearly dependent rows, singular
```

# 3x3 Determinants

```
1  0  1
0  1  0
3  3  3

((1*1*3) + (0*0*3) + (1*3*0)) - ((1*1*3) + (0*0*3) + (1*3*0))
det = 3 - 3 = 0
-> singular
```

```
1  1   1
1  1   2
0  0  -1

((1*1*-1) + (1*2*1) + (1*1*0)) - ((1*1*0) + (1*1*-1) + (1*2*0))
det = -1 + 2 - -1 = 0
-> singular
```

```
1  1  1
0  2  2
0  0  3
((1*2*3) + (1*2*0) + (1*0*0)) - ((1*2*0) + (1*0*3) + (1*2*0))
det = 6 - 0 = 6
-> non-singular
```

```
1  2   5
0  3  -2
2  4  10
((1*3*10) + (2*-2*2) + (5*0*4)) - ((5*3*2) + (2*0*10) + (1*-2*4))
det = (30 + -8) - (30 + -8) = 0
-> singular
```

---

# Row Echelon Form

A matrix is in Row Echelon form if it has the following properties:

1. Any row consisting entirely of zeros occurs at the bottom of the matrix.
2. For each row that does not contain entirely zeros, the first non-zero entry
   is 1 (called a leading 1).
3. For two successive (non-zero) rows, the leading 1 in the higher row is
   further left than the leading one in the lower row.

# Matrix Rank

Matrix rank is then number of "unique" rows in the matrix.

A matrix is Full Rank if its rank is the highest possible for a matrix of the
same size.

---

# Quiz 1

```
2b +  m + 5c = 20
 b + 2m +  c = 10
2b +  m + 3c = 15
```

```
2  1  5
1  2  1
2  1  3

((2*2*3) + (1*1*2) + (5*1*1)) - ((5*2*2) + (1*1*3) + (2*1*1))
det = (12 + 2 + 5) - (20 + 3 + 2)
    = 19 - 25 = -6
```

```
2  1  5   |   2  1  5   |   2  1  5
1  2  1   |   1  2  1   |   1  2  1
1  3  3   |   3  3  6   |   1  2  3
det = 9   |   det = 0   |   det =
```

```
1  2  3
0  2  2
1  4  5

(10 + 4 + 0) - (6 + 0 + 8)
det = 14 - 14 = 0
```
