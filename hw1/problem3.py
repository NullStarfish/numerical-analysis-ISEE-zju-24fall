def exactly(x):
    return x

def chopping(x):
    x = x * 1000
    x = x // 1
    x = x / 1000
    return x

def rounding(x):
    return round(x, 3)

def absoluteError(exact, approx):
    return abs(exact - approx)

def relativeError(exact, approx):
    return absoluteError(exact, approx) / abs(exact)

#Test
a = 4 / 5 + 1 / 3
print("Exact: " + str(exactly(a)))
print("Chopping: " + str(chopping(a)))
print("Absolute error and relative error:" + str(absoluteError(a, chopping(a))) + "  " + str(relativeError(a, chopping(a))))
print("Rounding: " + str(rounding(a)))
print("Absolute error and relative error:" + str(absoluteError(a, rounding(a))) + "  " + str(relativeError(a, rounding(a))))


b = (1 / 3 + 3 / 11) - 3 / 20
print("Exact: " + str(exactly(b)))
print("Chopping: " + str(chopping(b)))
print("Absolute error and relative error:" + str(absoluteError(b, chopping(b))) + "  " + str(relativeError(b, chopping(b))))
print("Rounding: " + str(rounding(b)))
print("Absolute error and relative error:" + str(absoluteError(b, rounding(b))) + "  " + str(relativeError(b, rounding(b))))



