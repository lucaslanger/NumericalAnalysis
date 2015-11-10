import math
import matplotlib.pyplot as plt

T=20
y0=0.1
h=0.03
N=500

def newtons(f, guess):
	x = guess
    	while( abs(g(x)-x)/x >= 10**(-10) ):
		slope = fprime(x)
		x = x - f(x)/slope
	return x
    

def trapezoidal(T,h,y_init):
	def trap(T):
		step_size = h
		y = y_init
		yield y
		while True:
			y = y + step_size*(y**2)*(1-(step_size*y))
			yield y 

def euleurs(T,h,y_init):
	def eul(T):
		step_size = h
		y = y_init
		yield y
		while True:
			c = y + (step_size/2)*(y**2)*(1-(step_size*y)) 
			y = newtons(lambda y: y - C + (step_size/2)*(y**2)*(1-(step_size*y)), C*2) #For initial guess, we use newtons and then we solve the implicit equation with rootfinding
			yield y
	return eul
