import math

class problem5Solution:
    failed = ()
    def BisectionMethod(f, a, b, recursionCount):
        assert a <= b
        if recursionCount > 100:
            yield problem5Solution.failed
        else:
            p = (a + b) / 2
            if abs(f(p)) < 1E-5:
                yield p
            else:
                yield p
                if f(p) * f(a) < 0:
                    yield from problem5Solution.BisectionMethod(f, a, p, recursionCount + 1)
                else:
                    yield from problem5Solution.BisectionMethod(f, p, b, recursionCount + 1)
                
                        
def BisectionFinal(f, a, b):
    result = list(problem5Solution.BisectionMethod(f, a, b, 0))
    if result[len(result) - 1] is problem5Solution.failed:
        return "failed after 100 iterations"
    else:
        return result


f1 = lambda x: math.e ** x - x * x + 3 * x - 2
f2 = lambda x: x * math.cos(x) - 2 * x ** 2 + 3 * x - 1

print("for the first question:")
print(BisectionFinal(f1, 0, 1))

print("for the second:")
print("for the first section:" + str(BisectionFinal(f2, 0.2, 0.3)))
print("for the second section: " + str(BisectionFinal(f2, 1.2, 1.3)))

                    
                