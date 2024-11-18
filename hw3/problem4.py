import numpy as np
import Jacobi

Aa = np.asarray([[4, 1, -1], [-1, 3, 1], [2, 2, 5]], dtype=float)
ba = np.asarray([5, -4, 1], dtype=float)

print(Jacobi.JacobiforProblem4(Aa, ba, np.asarray([0, 0, 0], dtype=float), 0))

Ab = np.asarray([[-2, 1, 0.5], [1, -2, -0.5], [0, 1, 2]], dtype=float)
bb = np.asarray([4, -4, 0], dtype=float)

print(Jacobi.JacobiforProblem4(Ab, bb, np.asarray([0, 0, 0], dtype=float), 0))