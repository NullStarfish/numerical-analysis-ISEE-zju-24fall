from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
samples = np.array([[1, 3], [2, 3.72], [4.53, 4], [6, 4.5],[7.5, 6.55], [11, 8.5], [14, 7.5], [17, 5], [19, 7.45], [20, 8], [22, 8.43], [23, 7.95], [24.7, 5.9], [26, 6.1]
                    ,[28.0, 4.55], [30.5, 3.0], [29, 1.55], #圆弧三点
                    [28, 1.55], [24.5, 1.12], [18, 1.9], 
                    [15.5, 1.75], [13.5, 2.15], [10, 1.5],  
                    [9.2, 2], [9.4, 3], [9.3, 3.8],  
                    [8, 2.55], [5, 2.6], 
                    [2, 2.73], [1, 3] ])
diffs = [[2, 0.15], [0.15, 0.23], [1.5, -1], [2, -0.1], [-0.1, -2], [100, -100], [0, 0.3], [0, 0], [-30, -20], [-0.05, -0.05], [-1, -0.05]]
xd = samples[:, 0]
yd = samples[:, 1]


def xy2circle(position):
    l = np.sqrt(position[0] ** 2 + position[1] ** 2)
    theta = np.angle(complex(position[0], position[1]), deg=False)
    return [theta, l]

def circle2xy(position):
    return [position[1] * np.cos(position[0]), position[1] * np.sin(position[0])]


def cmp(k):
    return k[0]

class interResults:

    def __init__(self, data, diff, circle=0):
        self.length = len(data)
        if circle:
            data = np.array([xy2circle(k) for k in data])
            self.isXy = 0
        else:
            self.isXy = 1

        dataSorted = list(data)
        dataSorted.sort(key=cmp)
        dataSorted = np.array(dataSorted)

		#we assume x is simply increasing or decreasing
        tempx = dataSorted[:, 0]
        tempy = dataSorted[:, 1]


        self.x = data[:, 0]
        y = data[:, 1]
        
        self.funciton = CubicSpline(tempx, tempy, bc_type=((1, diff[0]), (1, diff[1])))
        

    def getDots(self):
        xs = np.linspace(self.x[0], self.x[self.length - 1], 100)
        ys = self.funciton(xs)
        if self.isXy == 1:
            return [xs, ys]
        else:
            dots = np.array([circle2xy([xs[k], ys[k]]) for k in range(0, len(xs))])
            return [dots[:, 0], dots[:, 1]]



functions = []
functions += [interResults(samples[0:2], diffs[0]), interResults(samples[1:4],diffs[1]), interResults(samples[3:8], diffs[2]), interResults(samples[7:11], diffs[3]), interResults(samples[10:15], diffs[4]), interResults(samples[14:17], diffs[5], circle=1),
				interResults(samples[16:20], diffs[6]), interResults(samples[19:23], diffs[7]),  
				interResults(samples[22:26], diffs[8], circle=1), 
				interResults(samples[25: 28], diffs[9]), 
				interResults(samples[27: 30], diffs[10])]



xs = np.array([])
ys = np.array([])
for i in functions:
        xs = np.append(xs, i.getDots()[0])
        ys = np.append(ys, i.getDots()[1])

plt.plot(xs, ys)
#plt.scatter(xd, yd)
plt.axis([0, 40, 0, 10])
plt.show()
