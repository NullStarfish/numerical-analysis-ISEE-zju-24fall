import numpy as np

def Normp(vecx, p):
    sum = 0
    for x in vecx:
        sum += x ** p
    return np.pow(sum, 1 / p)

def NormInf(vecx):
    max = np.abs(vecx[0])
    for x in vecx:
        if max < abs(x):
            max = abs(x)
    return max

A1 = [[1, 2, 3], [2, 3, 4], [3, 4, 6]]
vecx1 = [0, -7, 5]
vecx1app = [-0.2, -7.5, 5.4]

print(NormInf(np.asarray(vecx1,dtype=float) - np.asarray(vecx1app, dtype=float)))

vecx2app = np.asarray([-0.33, -7.9, 5.8], dtype=float)

print(NormInf(np.matmul(A1, vecx2app) - np.asarray([1, -1, 2], dtype=float)))
