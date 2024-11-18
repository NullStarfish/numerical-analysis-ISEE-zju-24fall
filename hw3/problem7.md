let the diagonal elements be positive

for an $n * n$ matrix

a11 a12 a13 .......

a21 a22 a23

        a33

for the first step of gaussian elimination

the diagonal elements:

$a_{22} -> a_{22} - \frac{a_{12}}{a_{11}} * a_{21}$

$a_{33} -> a_{33} - \frac{a_{13}}{a_{11}} * a_{31}$

$\frac{a_{1j}}{a11} < 1$

the the determinant is the product of the eigenvalue of a diagonly matrix

because a11 > 0, the rest of the diagon elements is still strictly diagonly dominant

recursively, Q. T. E.