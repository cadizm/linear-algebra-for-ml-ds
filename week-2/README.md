# Week 2

Processes for transforming a system of linear equations into a "solved system."

- Swapping equations
- Adding equations
- Multiplying equations by a constant

---

# Solving non-singular systems of equations

```
2a + 5b = 46
8a +  b = 32

8a + 20b = 184
8a +   b =  32

     19b = 152
b = 8

8a + 8 = 32
8a = 24
a = 3
```

---

# Solving singular systems of equations (redundant)

```
 a +  b = 10
2a + 2b = 20

 a +  b = 10
 a +  b = 10

0 = 0
```

In this case, the solved system is the single equation:

```
 a +  b = 10

a = x
b = 10 - x
```

Here, we say the solved system has one "degree of freedom `x`"

---

# Solving singular systems of equations (contradictory)

```
 a +  b = 10
2a + 2b = 24

 a +  b = 10
 a +  b = 12

0 = 2

-> contradiction
```

---

```
 5a +  b = 11
10a + 2b = 22

10a + 2b = 22
10a + 2b = 22

0 = 0

-> infinitely many solutions
```

---

# Solving systems of equations with more variables

## Elimination method

1. Manipulate equations so that all have a single variable with coefficient `1`
2. Now a single variable has been "isolated" and a system of 2 equations w/ 2
   unknowns remains
2. Continue isolating variables one by one and solve as previously described

---

# Matrix row-reduction

Also called `Gaussian elimination`

```
5a +  b = 17       |     5  1       |
4a - 3b =  6       |     4  3       |
                   |                |
a + 0.2b = 3.4     |     1  0.2     |   Row echelon form
       b = 2       |     0  1       |
                   |                |
a = 3              |     1  0       |   Reduced row echelon form
b = 2              |     0  1       |
```

# Row echelon form

Main diagonal starts with 1's, can be followed by 0's. 0's under main diagonal.

```
1 * * * *
0 1 * * *
0 0 0 * *
0 0 0 0 *
0 0 0 0 0
```

# Matrix row operations

Matrix row operations "preserve singularity". This means that when applying row
operations to a singular matrix, the resulting matrix is also a singular matrix.
And applying row operations to a non-singular matrix results in a non-singular matrix.

1. Switching rows
   - Determinant of new matrix is negative of original
2. Multiplying row by non-zero scalar
   - Determinant of new matrix is similarly scaled
3. Adding a row to another row
   - Determinant remains the same

---

# Practice quiz

Luis went yesterday to the bank to find out the interest rate of three different
financial instruments. He received the following information:

```
Financial Instrument            Annual interest
-----------------------------------------------
Savings account                 2%
Certificate of Deposit (CD)     3%
Bonds                           4%
```

He wants to invest his USD $10,000 savings in these three accounts. By doing so, he knows
that after a year he would receive a total of US $ 260 in interest if he put twice as
much money in the savings account as in the CDs, and "z" money in bonds.

Calculate the value of "z", in USD, using the elimination method explained in the
lectures.

```
x + y + z = 10_000
.02x + .03y + .04z = 260
x = 2y

 x +  y +  z = 10_000
2x + 3y + 4z = 26_000
 x - 2y      =      0

Gaussian elimination

1   1  1   10_000
2   3  4   26_000  multiply row 1 by -2 and add
1  -2  0        0  multiply row 1 by -1 and add

1   1   1  10_000
0   1   2   6_000
0  -3  -1 -10_000  multiply row 2 by 3 and add

1   1   1  10_000
0   1   2   6_000
0   0   5   8_000

->
x + y +  z = 10_000
    y + 2z =  6_000
        5z =  8_000

->
z = 1600
```

---

# Rank of a matrix

In systems of information, the rank is the number of pieces of information each sentence
carries.

The definition can be used similarly in systems of linear equations.

A matrix is non-singular iff it has full rank (rank equal to the number of rows).

This is the same as saying that each equation in the system of linear equations is
linearly independent.

# Row echelon form

```
Original matrix  |   Row echelon form
 5   1           |   1  0.2
 4  -3           |   0  1.

 5   1           |   1  1
10   2           |   0  0

0    0           |   0  0
0    0           |   0  0
```

The rank of a matrix is the number of non-zero numbers in the main diagonal of the matrix
in its row echelon form.

A matrix is non-singular iff the row echelon form has non-zero numbers in the main
diagonal.

Define the `pivot` of a matrix's row as the leftmost non-zero entry. Every pivot
must be the right of pivots in rows above it.

Another way to say this is, given a row, rows above it must have pivots to the left of
the given row.

The rank of a matrix is equal to the number of pivots in the matrix in row echelon form.

---

# Reduced row echelon form

A matrix is in reduced row echelon form if

1. It is in row echelon form
2. Each pivot is a 1
3. All numbers above a pivot are 0

---
