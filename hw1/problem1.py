import NewtonMethod
def getMedium(f, a, b, x1, x2):
    assert x1 >= a and x1 <= b and x2 >= a and x2 <= b and a < b
    def g(x):
        return f(x) - f(x1) / 2 - f(x2) / 2
    return NewtonMethod.NewtonMethod(g, 0)


def getMediumplus(f, a, b, x1 ,x2, c1, c2):
    assert x1 >= a and x1 <= b and x2 >= a and x2 <= b and a < b
    assert c1 > 0 and c2 > 0
    def g(x):
        return f(x) - f(x1) / (c1 + c2) * c1 - f(x2) / (c1 + c2) * c2
    result = NewtonMethod.NewtonMethod(g, 0)
    assert result >= a and result <= b
    return result


def getMediumWithNolimitation(f, a, b, x1, x2, c1, c2):
    def g(x):
        return f(x) - f(x1) / (c1 + c2) * c1 - f(x2) / (c1 + c2) * c2
    result = NewtonMethod.NewtonMethod(g, 0)
    assert result >= a and result <= b
    return result
    
#Test (a)
epsilong = getMedium(lambda x: x, 0, 1, 0, 1)
print(epsilong)

#Test(b)
epsilong = getMediumplus(lambda x: x, 0, 1, 0, 1, 1, 2)
print(epsilong)


#Test c
epislong = getMediumWithNolimitation(lambda x: x, 0, 1, 0, 1, 1, -2) #throw an exception
print(epislong)
