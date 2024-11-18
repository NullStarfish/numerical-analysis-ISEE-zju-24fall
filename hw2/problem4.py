import NewtonMethod
import SteepestMethod
import numpy as np
f11 = lambda xv: 15 * xv[0] * xv[1] ** 2 - 4 * xv[2] - 13
f12 = lambda xv: xv[0] ** 2 + 10 * xv[1] - xv[2] - 11
f13 = lambda xv: xv[1] ** 3 - 25 * xv[2] + 22
fv1 = [f11, f12, f13]
Fv1 = NewtonMethod.Fv(fv1)

print(SteepestMethod.SteepestMethod(Fv1, np.asarray([0, 0, 0], dtype=float), 0))


f21 = lambda xv: 10 * xv[0] - 2 * xv[1] ** 2 + xv[1] - 2 * xv[2] - 5
f22 = lambda xv: 8 * xv[1] ** 2 + 4 * xv[2] ** 2 - 9
f23 = lambda xv: 8 * xv[1] * xv[2] + 4
fv2 = [f21, f22, f23]
Fv2 = NewtonMethod.Fv(fv2)

print(SteepestMethod.SteepestMethod(Fv2, np.asarray([0, 0, 0], dtype=float), 0))

