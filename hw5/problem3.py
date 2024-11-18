
import math
f1 = lambda x: math.cos(x) ** 2
a1 = -0.25
b1 = 0.25

f2 = lambda x: x * math.log(x + 1)
a2 = -0.5
b2 = 0

f3 = lambda x: math.sin(x) ** 2 - 2 * x * math.sin(x) + 1
a3 = 0.75
b3 = 1.3

f4 = lambda x: 1 / x / math.log(x)
a4 = math.e
b4 = math.e + 1

def Trapezoidal(f, a, b):
    h = b - a
    return h / 2 * (f(b) + f(a))

def Simpson(f, a, b):
    x0 = a
    x1 = (a + b) / 2
    x2 = b
    h = x1 - x0
    return h * (f(x0) + 4 * f(x1) + f(x2)) / 3

print(Trapezoidal(f1, a1, b1))
print(Simpson(f1, a1, b1))
print(" ")


print(Trapezoidal(f2, a2, b2))
print(Simpson(f2, a2, b2))
print(" ")

print(Trapezoidal(f3, a3, b3))
print(Simpson(f3, a3, b3))
print(" ")

print(Trapezoidal(f4, a4, b4))
print(Simpson(f4, a4, b4))
print(" ")
