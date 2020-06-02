import numpy as np
import matplotlib.pyplot as plt

y1=np.loadtxt("Assignment 4 Problem 4.txt",usecols=0)

def f(x): # Exponential pdf
 	return 2*np.exp(-x/0.5)
x=np.linspace(0,5,1000) # x values for plotting f(x)


plt.hist(y1,20,density = True,facecolor = 'blue',ec='black',label = 'Density Histogram')
plt.plot(x,f(x),color = "red",label = "Given Distribution in the problem")
plt.title("Transformation method in a C code to produce 10,000 random numbers",size=15)
plt.xlabel("x",size = 13)
plt.ylabel("PDF(x)",size = 13)
plt.legend()
plt.grid()
plt.show()
