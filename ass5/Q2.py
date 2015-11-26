import numpy as np
import numpy.linalg as linalg

def secant(shoot,alpha,N,f,s1,s0,threshhold):
    while(abs(shoot(alpha,s1,N,f))>threshhold):
        temp=s1
        s1=s1-(shoot(alpha,s1,N,f)*(s1-s0))/(shoot(alpha,s1,N,f)-shoot(alpha,s0,N,f))
        s0=temp
    return s1


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
            #print u,up    
        return u-beta
   
    alpha_p = secant(euleur_err,alpha,N,f,s1,s0,threshhold)
    print euleur_err(alpha,alpha_p,N,f)
main()
