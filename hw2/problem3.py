import math
import numpy
import NewtonMethod
f11 = lambda xv: 3 * xv[0] - math.cos(xv[1] * xv[2]) - 0.5
f12 = lambda xv: 4 * xv[0] ** 2 - 625 * xv[1] ** 2 + 2 * xv[1] - 1
f13 = lambda xv: math.e ** (-1 * xv[0] * xv[1]) + 20 * xv[2] + (10 * math.pi - 3) / 3
fv1 = [f11, f12, f13]
F1 = NewtonMethod.Fv(fv1)
xv1 = [0, 0, 0]

f21 = lambda xv: xv[0] ** 2 + xv[1] - 37
f22 = lambda xv: xv[0] - xv[1] ** 2 - 5
f23 = lambda xv: xv[0] + xv[1] + xv[2] - 3
fv2 = [f21, f22, f23]
F2 = NewtonMethod.Fv(fv2)
xv2 = [0, 0, 0]


print(NewtonMethod.NewtonMethodMatrix(F1, xv1, 0, 2))
print(NewtonMethod.NewtonMethodMatrix(F2, xv2, 0, 2))