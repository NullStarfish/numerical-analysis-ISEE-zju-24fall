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


