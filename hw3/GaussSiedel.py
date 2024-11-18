import numpy as np
import Norms
import numpy.matlib as matlib

def gaussSiedelhelper(A, b, vecx, recursionCount, TOL):
    if recursionCount > 50:
        return "Failed after 50 times of iterations"
    if Norms.NormInf(np.matmul(A, vecx) - b) < TOL:
        return vecx
    else:
        nextvec = np.matmul(np.matmul(np.linalg.inv(diagonly(A) - matrixL(A)), matrixU(A)), vecx) + np.matmul(np.linalg.inv(diagonly(A) - matrixL(A)), b)
        return gaussSiedelhelper(A, b, nextvec, recursionCount + 1, TOL)

def gaussSiedel(A, b, vecx, TOL):
    return gaussSiedelhelper(A, b, vecx, 0, TOL)

def matrixU(A):
    result = []
    for y in range(0, len(A)):
        serialBuff = []
        for x in range(0, len(A[0])):
            if x > y:
                serialBuff += [-A[y][x]]
            else:
                serialBuff += [0]
        result += [serialBuff]
    return np.asarray(result, dtype=float)


def diagonly(A):
    result = np.asarray(matlib.zeros((len(A[0]), len(A))), dtype=float)
    for x in range(0, len(A[0])):
        result[x][x] = A[x][x]
    return result

def matrixL(A):
    result = []
    for y in range(0, len(A)):
        serialBuff = []
        for x in range(0, len(A[0])):
            if x < y:
                serialBuff += [-A[y][x]]
            else:
                serialBuff += [0]
        result += [serialBuff]
    return np.asarray(result, dtype=float)

