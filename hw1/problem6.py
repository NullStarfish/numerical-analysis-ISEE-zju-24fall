import math

class problem6Solution:
    failed = ()
    def fixedPoindMethod(f, p, recursionTimes, sel):
        def g1(x):
            return f(x) + x
        def g2(x):
            return x - f(x)
        def gsuitf2(x):
            return math.log(3 * x * x)
        def gsuitf22(x):
            return math.sqrt(math.e ** x / 3)
        def gsuitf23(x):
            return math.sqrt((math.e ** x + x * x) / 4)
        def gsuitf1(x):
            return math.sqrt(2 - 2 * math.cos(2 * math.pi * x))

        if sel == 1:
            g = g1
        elif sel == 2:
            g = g2
        elif sel == 3:
            g = gsuitf2
        elif sel == 4:
            g = gsuitf22
        elif sel == 5:
            g = gsuitf23
        elif sel == 6:
            g = gsuitf1

        if recursionTimes > 50:
            yield problem6Solution.failed
        else:
            try:
                if abs(g(p) - p) < 0.01:
                    yield p
                else:
                    yield p
                    yield from problem6Solution.fixedPoindMethod(f, g(p), recursionTimes + 1, sel)
            except OverflowError:
                yield ()



def fixedPointMethodFinal(f, p0):
    result = list(problem6Solution.fixedPoindMethod(f, p0, 0, 1))
    if result[len(result) - 1] is problem6Solution.failed:
        result = list(problem6Solution.fixedPoindMethod(f, p0, 0, 2))
        if result[len(result) - 1] is problem6Solution.failed:
            return "failed after 50 times of iterations"
        else:
            return result
    else:
        return result
    

fa = lambda x: 2 * math.sin(math.pi * x) + x
fb = lambda x: 3 * x * x - math.e ** x


print(list(problem6Solution.fixedPoindMethod(fa, 1, 0, 6)))
print(list(problem6Solution.fixedPoindMethod(fb, 0, 0, 4)))
print(list(problem6Solution.fixedPoindMethod(fb, 1, 0, 3)))
print(list(problem6Solution.fixedPoindMethod(fb, -0.01, 0, 5)))

