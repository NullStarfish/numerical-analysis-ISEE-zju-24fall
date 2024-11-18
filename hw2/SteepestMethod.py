import NewtonMethod
import numpy as np
import math
def SteepestMethod(F, xv, recursionCount):
    g = getG(F)
    gGradient = myGradient(g, xv)

    def getalpha():
        '''h1 = (g2 - g1) * 2
        h2 = (g3 - g2) * 2
        h3 = (h2 - h1)'''
        def P(alpha):
            return g(xv- alpha * oneGradient())
        return np.argmin([P(i / 1000) for i in range(0, 1000)]) / 1000

    def oneGradient():
        return gGradient / math.sqrt(np.vdot(gGradient, gGradient))

    if recursionCount > 50:
        return "Failed after 50 times of iteraction"
    if g(xv) < 0.05:
        return xv
    else:
        next = xv - oneGradient() * getalpha()
        return SteepestMethod(F, next, recursionCount + 1)


def getG(F):
    def g(xv):
        result = 0
        for f in F.functionData:
            result += f(xv) ** 2
        return result
    return g

def myGradient(g, xv):
    result = []
    for i in range(0, len(xv)):
        result += [NewtonMethod.partialDifferent(g, xv, i)]
    return np.asarray(result, dtype=float)

