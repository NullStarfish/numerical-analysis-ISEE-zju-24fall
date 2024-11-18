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