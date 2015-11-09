import math
import sys


def f(x): 
    return x**3.0 - (math.e)**(-x)

#g is used to find fixed points
def g(x):
    return ( math.e**(-x))** (1.0/3)
   
def fprime(x):
    return 3.0*(x**2.0) + math.e**(-x) 
    
def bisection(x0, x1):
    if f(x0)*f(x1) < 0:	
        if f(x0) > f(x1):
            highguess = x0
            lowguess = x1
        else:
            highguess = x1
            lowguess = x0
            
        c = 0
        while f(highguess) >= 10**-10  and -1*f(lowguess) >= 10**-10:
            newguess = (highguess+lowguess)/2.0 
	    v = f(newguess)
            c = c + 1
            if v > 0:
                highguess = newguess
            elif v < 0:
                lowguess = newguess
            else:
            	break
        
        print(c)
    else:
        print("Initial guesses don't satisfy requirements")

def testFixedPoint():
    x = 0.5
    c = 0 
    while( abs(g(x)-x) >= 10**(-10) ):
	x = g(x)
	c = c + 1
    print(c, x)

def testNewtons():
    x = 0.5 
    c = 0
    while( abs(g(x)-x) >= 10**(-10) ):
	slope = fprime(x)
	x = x - f(x)/slope
	c = c + 1
    print(c, x)

def testSecant():
    x = 0.5 
    c = 0
    while( abs(g(x)-x) >= 10**(-10) ):
	slope = (f(x+0.001) - f(x-0.001))/(2*0.001)
	x = x - f(x)/slope
	c = c + 1
    print(c, x)

def testBisection():
    g1 = 1 
    g2 = 0
    bisection(g1,g2)

t = sys.argv[1]
if t == "bisection":
    testBisection()
elif t == "fixedpoint":
    testFixedPoint()
elif t == "newtons":
    testNewtons()
elif t == "secant":
    testSecant()
