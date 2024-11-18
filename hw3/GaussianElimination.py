import numpy as np

def gaussionElimination(A, b):
    for diagon in range(0, len(A[0]) - 1):
        maxIndex = findmaxI(A, diagon)

        temp = np.copy(A[diagon])
        A[diagon] = A[maxIndex]
        A[maxIndex] = temp
        if A[diagon][diagon] == 0:
            return "There is no unique solution"

        temp = b[diagon]
        b[diagon] = b[maxIndex]
        b[maxIndex] = temp

        for row in range(diagon + 1, len(A)):
            m = A[row][diagon] / A[diagon][diagon]
            A[row] = A[row] - m * A[diagon]
            b[row] = b[row] - m * b[diagon]
    
    result = [0 for _ in range(0, len(A))]
    for valIndex in range(len(A) - 1, -1, -1):
        xval = (b[valIndex] - np.dot(result, A[valIndex])) / A[valIndex][valIndex]
        result[valIndex] = xval

    return result



def getSi(A):
    result = []
    for x in range(0, len(A)):
        si = max([abs(a) for a in A[x]])
        result += [si]
    return result

def findmaxI(A, diagon):
    buff = []
    for x in range(diagon, len(A)):
        buff += [abs(A[x][diagon] / getSi(A)[x])]
    return buff.index(max(buff))

'''
A = np.asarray([np.asarray([0, 1], dtype=float), np.asarray([1, 0], dtype=float)])
b = np.asarray([1, 1], dtype=float)
print(gaussionElimination(A, b))
'''