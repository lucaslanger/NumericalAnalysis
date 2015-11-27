import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt

def secant(shoot,alpha,N,f,s1,s0,threshhold):
    sa = [s0,s1]
    while(abs(shoot(alpha,s1,N,f))>threshhold):
        temp=s1
        s1=s1-(shoot(alpha,s1,N,f)*(s1-s0))/(shoot(alpha,s1,N,f)-shoot(alpha,s0,N,f))
        s0=temp
        sa.append(s1)
    return sa

def main():
    alpha=0
    beta=0
    s0=0
    s1=10**(-3)   
    N=100
    threshhold=10**(-10)

    def f(x):
        return 5*x*(1-x)
    
    def euleur_err(u,u_p,N,f):
        for i in range(N):
            x = (float(i)/N)
            u += (1.0/N)*u_p*(x)
            u_p += (1.0/N)*(-1)*f(x)*((1+(u_p**2))**(1.5))
        return u-beta
   
    sg=secant(euleur_err,alpha,N,f,s1,s0,threshhold)
    errors=[abs(euleur_err(alpha,a_p,N,f)) for a_p in sg]
    print "\nSlopes guesses: ", sg
    print "\nErrors:", errors 
    print "\nNumber of iterations:", len(sg)

    plt.plot(sg,errors,marker='o', linestyle='--', color='b')

    plt.xlabel("slope_i")
    plt.ylabel("error_i")
    plt.title("Error as a function of successive initial slope guesses")
    plt.grid(True)
    plt.show()
main()
