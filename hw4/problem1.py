import math
def L(n, k, xpoints):
    assert n == len(xpoints) - 1
    def f(x):
            fact1 = 1
            for xk in xpoints:
                  if (xk != x):
                        fact1 *= x - xk
            fact2 = 1
            for xk in xpoints:
                  if (xk != xpoints[k]):
                        fact2 *= xpoints[k] - xk
            return fact1 / fact2
    return f

def PLangr(xpoints, f):
      def private(x):
            sum = 0
            for k in range(0, len(xpoints)):
                  sum += L(len(xpoints) - 1, k, xpoints)(x) * f(xpoints[k])
            return sum
      return private

                 
                     
            


f1 = lambda x: math.exp(2 * x) * math.cos(3 * x)
f2 = lambda x: math.sin(math.log(x))

xpoints1 = [0, 0.3, 0.6]
xpoints2 = [2.0, 2.4, 2.6]

max1 = max([PLangr(xpoints1, f1)(xpoints1[0] + x * (xpoints1[2] - xpoints1[0]) / 100) for x in range(0, 101)])
min1 = min([PLangr(xpoints1, f1)(xpoints1[0] + x * (xpoints1[2] - xpoints1[0]) / 100) for x in range(0, 101)])

max2 = max([PLangr(xpoints2, f2)(xpoints2[0] + x * (xpoints2[2] - xpoints2[0]) / 100) for x in range(0, 101)])
min2 = min([PLangr(xpoints2, f2)(xpoints2[0] + x * (xpoints2[2] - xpoints2[0]) / 100) for x in range(0, 101)])


print(str(max1) + " " + str(min1))
print(str(max2) + " " + str(min2))