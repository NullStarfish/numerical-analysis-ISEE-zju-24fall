import numpy as np
x = np.array([0, 2, 4, 5])
y = np.array([6, 8, 14, 20])

def linearLeast(x, y):
    assert len(x) == len(y)
    m = len(x)
    xSquareSum = sum([i ** 2 for i in x])
    xSum = sum(x)
    ySquareSum = sum([i**2 for i in y])
    ySum = sum(y)
    xydot = np.vdot(x, y)
    a0 = (xSquareSum * ySum - xydot * xSum) / (m * xSquareSum - xSum ** 2)
    a1 = (m * xydot - xSum * ySum) / (m * xSquareSum - xSum ** 2)
    return a0, a1


a0, a1 = linearLeast(x, y)
print("y = " + str(a0) + " + " + str(a1) + " x ")


f = lambda t: a0 + a1 * t

def E(x, y, f):
    result = sum([(y[i] - f(x[i])) ** 2 for i in range(0, len(x))])
    return result


print(E(x, y, f))
