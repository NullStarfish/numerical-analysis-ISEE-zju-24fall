import NewtonMethod
import math
#question a
def absoluteError(f, x0):
    e = 5E-6
    return abs(NewtonMethod.different(f, x0) * e)

def relativeError(f, x0):
    return absoluteError(f, x0) / abs(f(x0))

#@Test
print(absoluteError(lambda x: x * x, 2))
print(relativeError(lambda x: x * x, 2))

#question b
#1:
print(absoluteError(lambda x: math.e ** x, 1))
print(relativeError(lambda x: math.e ** x, 1))

#2:
print(absoluteError(math.sin, 1))
print(relativeError(math.sin, 1))


#question 3
def q3absoluteError(f, x0):
    e = 5E-6 * x0
    return abs(NewtonMethod.different(f, x0) * e)

def q3relativeError(f, x0):
    return q3absoluteError(f, x0) / abs(f(x0))

#1:
print(q3absoluteError(lambda x: math.e ** x, 10))
print(q3relativeError(lambda x: math.e ** x, 10))

#2:
print(q3absoluteError(math.sin, 10))
print(q3relativeError(math.sin, 10))
