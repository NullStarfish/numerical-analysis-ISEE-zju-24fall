import GaussSiedel
import Jacobi
import numpy as np
Aa = np.asarray([np.asarray([3, -1, 1], dtype=float), np.asarray([3, 6, 2], dtype=float), np.asarray([3, 3, 7], dtype=float)])
ba = np.asarray([1, 0, 4], dtype=float)
Ab = np.asarray([[10, -1, 0], [1, -2, -0.5], [0, 1, 2]], dtype=float)
bb = np.asarray([9, 7, 6], dtype=float)
print(Jacobi.Jacobi(Aa, ba, np.asarray([0, 0, 0], dtype=float), 0.001))
print(GaussSiedel.gaussSiedel(Aa, ba, np.asarray([0, 0, 0], dtype=float), 0.001))

print(Jacobi.Jacobi(Ab, bb, np.asarray([0, 0, 0], dtype=float), 0.001))
print(GaussSiedel.gaussSiedel(Ab, bb, np.asarray([0, 0, 0], dtype=float), 0.001))