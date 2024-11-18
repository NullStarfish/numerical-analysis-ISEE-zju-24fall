import GaussSiedel
import Norms
import numpy as np
def Jacobihelper(A, b, vecx, TOL, recursionCount):
    if recursionCount > 50:
        return "Failed after 50 times of iteration"
    if Norms.NormInf(np.matmul(A, vecx) - b) < TOL:
        return vecx
    else:
        nextvec = np.matmul(np.matmul(np.linalg.inv(GaussSiedel.diagonly(A)), GaussSiedel.matrixL(A) + GaussSiedel.matrixU(A)), vecx) + np.matmul(np.linalg.inv(GaussSiedel.diagonly(A)), b)
        return Jacobihelper(A, b, nextvec, TOL, recursionCount + 1)
    
def Jacobi(A, b, vecx, TOL):
    return Jacobihelper(A, b, vecx, TOL, 0)

def JacobiforProblem4(A, b, vecx, recursionCount):
    if recursionCount > 2:
        return []
    else:
        nextvec = np.matmul(np.matmul(np.linalg.inv(GaussSiedel.diagonly(A)), GaussSiedel.matrixL(A) + GaussSiedel.matrixU(A)), vecx) + np.matmul(np.linalg.inv(GaussSiedel.diagonly(A)), b)
        return [nextvec] + JacobiforProblem4(A, b, nextvec, recursionCount + 1)