import math
ft = lambda x: math.sin(x)
at = 0
bt = math.pi


f1 = lambda x: math.cos(x) ** 2
a1 = -1
b1 = 1

f2 = lambda x: x * math.log(x + 1)
a2 = -0.75
b2 = 0.75

f3 = lambda x: math.sin(x) ** 2 - 2 * x * math.sin(x) + 1
a3 = 1
b3 = 4

f4 = lambda x: 1 / x / math.log(x)
a4 = math.e
b4 = math.e * 2

def R(x, y, a, b, f):
    if y == 1:
        h = (b - a) * (2 ** (1 - x))
        sum = 0
        for i in [2 * f(a + h * t) for t in range(0, 2 ** (x - 1) + 1)]:
            sum += i
        sum -= (f(a) + f(b))
        return h / 2 * sum
    else:
        return R(x, y - 1, a, b, f) + 1 / 3 * (R(x, y - 1, a, b, f) - R(x - 1, y - 1, a, b, f))
    
f = [f1, f2, f3, f4]
a = [a1, a2, a3, a4]
b = [b1, b2, b3, b4]
for i in range(0, 4):
    print(R(3, 3, a[i], b[i], f[i]))



