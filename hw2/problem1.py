import NewtonMethod as lib
import math
f = lambda x: - x ** 3 - math.cos(x) 
g = lambda x: x - f(x) / lib.different(f, -1)

p2 = g(g(-1))
print("p2: " + str(p2))

print(lib.NewtonMethod(f, 0))
