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