import numpy as np
from scipy import linalg

def find_fixed_point(M,N,b,x_i,error_threshhold,sor):
    def relative_error(x,x_approx):
        d = np.subtract(x,x_approx)
        return np.linalg.norm(d)/np.linalg.norm(x)
 
    def next_vector(x_i):
        tempv = np.subtract(b,np.dot(N,x_i))
        return np.dot(np.linalg.inv(M), tempv)
    
    prev = x_i
    x_i = next_vector(x_i)
    iterations = 1

    while(relative_error(x_i,prev) > error_threshhold):
        prev = x_i  
        x_i = np.subtract(np.multiply(sor,next_vector(x_i)), np.multiply(1-sor,prev) )
        iterations = iterations + 1


    return {"x":x_i,"iterations":iterations}


def jacobi():
    M = np.array([[2,0,0],[0,2,0],[0,0,2]])
    N = np.array([[0,-1,0],[-1,0,-1],[0,-1,0]])
    x0 = np.transpose(np.array([1,0,0]))
    b = np.transpose(np.array([1,2,3]))
    threshhold = 10**(-10)
    sor = 1.0
    return find_fixed_point(M,N,b,x0,threshhold,sor)

def gauss_seidel():
    M = np.array([[2,0,0],[-1,2,0],[0,-1,2]])
    N = np.array([[0,-1,0],[0,0,-1],[0,0,0]])
    x0 = np.transpose(np.array([1,0,0]))
    b = np.transpose(np.array([1,2,3]))
    threshhold = 10**(-10)
    sor = 1.0
    return find_fixed_point(M,N,b,x0,threshhold,sor)

def runTest(method_name, f):
    print "Computing the solution with " + method_name
    print "Iterations: " +  str(f()["iterations"])
    print ""

def main():
    #runTest("Richardsons", richardsons)
    runTest("Jacobi", jacobi)
    runTest("Gauss Seidel", gauss_seidel)
main()
