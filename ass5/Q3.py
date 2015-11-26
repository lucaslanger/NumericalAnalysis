import numpy as np
from scipy import linalg

def find_fixed_point(M,N,b,x_i,error_threshhold):
    prev = None
    def relative_error(x,x_approx):
        d = np.subtract(x,x_approx)
        return np.linalg.norm(d)/np.linalg.norm(x)
 
    def next_vector():
        prev = x_i
        x_i = np.linalg.solve(M,np.subtract(b,np.multiply(N,x_i)))
    
    while(prev!=None and relative_error(x_i,prev)>error_threshhold):
        next_vector()

    return x_i

def jacobi():
    M = np.array([2,0,0],[0,2,0],[0,0,2])
    N = np.array([0,-1,0],[-1,0,-1],[0,-1,0])
    x0 = np.array([1,0,0])
    b = np.array([1,2,3])
    threshhold = 10**(-10)
    return find_fixed_point(M,N,b,x0,threshhold)

def gauss_seidel():
    M = np.array([2,0,0],[-1,2,0],[0,-1,2])
    N = np.array([0,-1,0],[0,0,-1],[0,0,0])
    x0 = np.array([1,0,0])
    b = np.array([1,2,3])
    threshhold = 10**(-10)
    return find_fixed_point(M,N,b,x0,threshhold)

def runTest(method_name, f)
    print "Computing the solution with" + method_name+ "\n"
    f()
    print ""

def main():
    runTest("Richardsons", richardsons)
    runTest("Jacobi", jacobi))
    runTest("Gauss Seidel", gauss_seidel)
