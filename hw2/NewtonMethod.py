import numpy as np

def NewtonMethodhelper(f, x, rescursionCount):
    if rescursionCount > 50:
        return "Failed after 50 times of iteration"
    if abs(f(x)) < 0.0001:
        return x
    else:
        next = x - f(x)/different(f, x)
        return NewtonMethod(f, next)

def NewtonMethod(f, x):
    return NewtonMethodhelper(f, x, 0)

def different(f, x):
    deltax = x + 0.0001
    return (f(deltax) - f(x)) / (deltax - x)

def diffFunc(f):
    def diff(x):
        return different(f, x)
    return diff


#F return an array
#fv is an array

class Fv:
    def __init__(self, fv):
        self.functionData = []
        for f in fv:
            self.functionData += [f]

    def value(self, xv):
        result = []
        for i in range(0, len(self.functionData)):
            result += [self.functionData[i](xv)]
        return np.asarray(result, dtype=float)

#F is Fv
def NewtonMethodMatrix(F, xk, recursionCount, limit):
    if recursionCount >= limit:
        return xk
    if all([abs(x) < 0.00001 for x in F.value(xk)]):
        return xk
    else:
        next = xk - np.dot(matrixInverse(Jaccobi(F, xk)), F.value(xk))
        return NewtonMethodMatrix(F, next, recursionCount + 1, limit)
    
def Jaccobi(F, xv):
    assert len(F.functionData) == len(xv)
    result = []
    for i in range(0, len(F.functionData)):
        for j in range(0, len(xv)):
            result += [partialDifferent(F.functionData[i], xv, j)]
    return np.asarray(result, dtype=float).reshape(len(F.functionData), len(xv))

def matrixInverse(M):
    return np.linalg.inv(M)
    


def partialDifferent(f, xv, index):
    TOL = 0.0001
    xdelta = xv.copy()
    xdelta[index] += TOL
    return (f(xdelta) - f(xv)) / TOL

def f1(xv):
    return xv[0] * xv[1] * xv[2]
def f2(xv):
    return xv[0] + xv[1] + xv[2]
def f3(xv):
    return xv[0] + xv[1] * xv[2]

'''
fv = [f1, f2, f3]
F = Fv(fv)
xv = np.asarray([1, 2, 3], dtype=float)
print(Jaccobi(F, xv))
print(matrixInverse(Jaccobi(F, xv)))
print(NewtonMethodMatrix(F, xv, 0))
'''