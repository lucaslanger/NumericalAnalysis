import math
import matplotlib.pyplot as plt

def secant(f, x):
	dx = 0.001
    	while( abs(f(x)) >= 10**(-6) ):
		slope = (f(x+dx)-f(x-dx))/(2*dx)
		x = x - f(x)/slope
	return x
    
def euleurs(h,y,eps):
	yield y
	while True:
		y = y + h*(y**2)*(1-(eps*y))
		yield y 

def trapezoidal(h,y,eps):
	yield y
	while True:
		c = y + (h/2)*(y**2)*(1-(eps*h*y)) 
		guess = y + h*(y**2)*(1-(eps*h*y)) 
		y = secant(lambda y: y-c-(h/2)*(y**2)*(1-(eps*y)), guess) 
		yield y
	#For initial guess, we use newtons and then we solve the implicit equation with rootfinding
	#yn+1 = yn+(h/2)*f(yn+1)+(h/2)*f(yn)

T=20.0
N=250
h=T/N

y0=0.1
eps=0.03

plt.figure(1)
xaxis = [i for i in range(N)]

plt.subplot(211)
euler_iter = euleurs(h,y0,eps)
euler_values = [euler_iter.next() for i in range(N)]
plt.plot(xaxis,euler_values)

plt.subplot(212)
trap_iter = trapezoidal(h,y0,eps)
trap_values = [trap_iter.next() for i in range(N)]
plt.plot(xaxis,trap_values)

plt.show()

