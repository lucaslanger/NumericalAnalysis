import numpy as np
import math

def jacF(x,y):
   t11 = 2*x  
   t12 = 2*y
   t21 = 1 + y*math.cos(x*y)
   t22 = x*math.cos(x*y) - 1
   return np.array([[t11,t12],
		    [t21,t22]])

def f(x,y):
    t1 = x**2.0 + y**2.0 - 4
    t2 = x + math.sin(x*y) - y
    return np.array([t1, t2])

def newtons():
    v = np.array( [1.,1.] )
    c = 0 
    while np.linalg.norm( f(v[0],v[1]) ) >= 10**(-8):
   	dFe = jacF( v[0], v[1] )
        fe = f( v[0], v[1] )
	t = np.linalg.solve( dFe, fe ) # solves the equation dFe*t = fe
        v = v - t
	c = c + 1
        print(v)
    print(c)

newtons()

