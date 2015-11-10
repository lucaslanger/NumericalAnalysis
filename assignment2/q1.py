from math import exp
from math import log
import matplotlib.pyplot as plt


def compositeTrapezoidalApprox(f,n,a,b):
	h = float(b - a)/n
	s = f(a) + f(b)
	for k in range(1,n):	
		#print f(a+(k*h))
		s += 2*f(a+(k*h))
	return (h/2)*s

def richardsonApprox(f,n,a,b):
	x = [2*n,n]
	y = [compositeTrapezoidalApprox(f,i,a,b) for i in x]
	return (4.0/3)*y[0] - (1.0/3)*y[1]

a = 0
b = 1
f = lambda x: exp(-x)

#print compositeTrapezoidalApprox(f,4,a,b)
print "\n"
results = [0]*9
for i in range(0,9):
	n = (1 << i)
	results[i] = richardsonApprox(f,n,a,b)
	print "With h = " + str(1.0/n) + " the approximation is: " + str(results[i])

trueValue = richardsonApprox(f,10000,a,b)

log_errors = [log(abs(x-trueValue)) for x in results]
log_xaxis = [x for x in range(0,9)]

slope = (log_errors[-1] - log_errors[0])/(len(log_errors)-1)
print "\nThe degree of error was approximately: ", -1*slope

plt.plot(log_xaxis,log_errors)
plt.ylabel("Log value")
plt.show()


