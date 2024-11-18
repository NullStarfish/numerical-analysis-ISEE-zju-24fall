import numpy as np
import GaussianElimination as gaus
Aa = np.asarray([[0.03, 58.9], [5.31, -6.10]], dtype=float)
ba = np.asarray([59.2, 47.0], dtype=float)
print(gaus.gaussionElimination(Aa, ba))


Ab = np.asarray([[3.03, -12.1, 14], [-3.03, 12.1, -7], [6.11, -14.2, 21]])
bb = np.asarray([-119, 120, -139], dtype=float)
print(gaus.gaussionElimination(Ab, bb))