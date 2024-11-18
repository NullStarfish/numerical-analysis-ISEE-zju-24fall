f1 = lambda t, y: y / t - (y / t) ** 2
h1 = 0.1
a1 = 1
b1 = 2
ya1 = 1

f2 = lambda t, y: 1 + y / t + (y / t) ** 2
h2 = 0.2
a2 = 1
b2 = 3
ya2 = 0

ft = lambda t, y: y - t ** 2 + 1
at = 0
bt = 2
ht = 0.5
yat = 0.5


def Eulers(currentW, step, currentX, StopX, f):
    while currentX < StopX:
        currentW = currentW + step * f(currentX, currentW)
        currentX += step
    return currentW


print(Eulers(ya1, h1, a1, b1, f1))
print(Eulers(ya2, h2, a2, b2, f2))



