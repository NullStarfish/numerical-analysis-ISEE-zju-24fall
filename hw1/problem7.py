import NewtonMethod
import math
def isDiverges(delta, p, g):
    x = getTestPoints(p, delta)
    for i in range(0, len(x)):
        x[i] = abs(x[i] - p) < abs(g(x[i]) - p)
    return all(x)

def getTestPoints(p, delta):
    x = []
    for i in range(0, 101):
        x += [p + (i - 50) / 100 * delta]
    x.remove(p)#get 100 test points
    return x


def getDelta(g, p, delta):
    assert validg(g, p)
    x = getTestPoints(p, delta)

    valid = True
    for i in x:
        if abs(NewtonMethod.different(g, i)) <= 1:
            valid = False
    
    if valid:
        return delta
    else:
        return getDelta(g, p, delta / 2)

def validg(g, p):
    return g(p) == p and abs(NewtonMethod.different(g, p)) > 1



g = lambda x: 3 * x - 2
g = lambda x: math.e ** x - math.e + 1 
delta = getDelta(g, 1, 1)
print(delta)
print(isDiverges(delta, 1, g))