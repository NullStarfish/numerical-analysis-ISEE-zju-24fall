import matplotlib.pyplot as plt
import numpy as np



#L1 = 10
def F1(x, alpha, L1):
    assert x < 0.1
    return  L1 + x ** alpha

#L2 = 20
def F2(x, beta, L2):
    assert x < 0.1
    return L2 + x ** beta

def F(x, c1, c2, alpha, beta, L1, L2):
    return c1 * F1(x, alpha, L1) + c2 * F2(x, beta, L2)

def G(x, c1, c2, alpha, beta, L1, L2):
    return F1(c1 * x, alpha, L1) + F2(c2 * x, beta, L2)

def Fapproximate(x, L1, L2, alpha, beta, c1, c2):
    return c1 * L1 + c2 * L2 + x ** min(alpha, beta)

def Gapproximate(x, L1, L2, alpha, beta):
    return L1 + L2 + x ** min(alpha, beta)


#let L1 = 10, L2 = 20, c1 = 2, c2 = 3, alpha = 15, beta = 10
c1 = 2
c2 = 3
L1 = 0.001
L2 = 0.002
alpha = 2
beta = 3


xpoints = []
Fypoints = []
Fapproximateypoints = []
Gypoints = []
Gapproximateypoints = []

for k in range(0, 100):
    i = k / 10000
    xpoints += [i]
    Fypoints += [F(i, c1, c2, alpha, beta, L1, L2)]
    Fapproximateypoints += [Fapproximate(i, L1, L2, alpha, beta, c1, c2)]
    Gypoints += [G(i, c1, c2, alpha, beta, L1, L2)]
    Gapproximateypoints += [Gapproximate(i, L1, L2, alpha, beta)]



#plot 1: F(x):
x = np.array(xpoints)
y = np.array(Fypoints)

plt.subplot(2, 2, 1)
plt.plot(x,y)
plt.title("F(x)")

#plot 2 O(x ^ gamma):
x = np.array(xpoints)
y = np.array(Fapproximateypoints)

plt.subplot(2, 2, 2)
plt.plot(x,y)
plt.title("F approximate")

#plot 3:
x = np.array(xpoints)
y = np.array(Gypoints)

plt.subplot(2, 2, 3)
plt.plot(x,y)
plt.title("G(x)")

#plot 4:
x = np.array(xpoints)
y = np.array(Gapproximateypoints)

plt.subplot(2, 2, 4)
plt.plot(x,y)
plt.title("G approximate")

plt.suptitle("RUNOOB subplot Test")
plt.show()