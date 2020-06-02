'''
Box-Muller method in a Python code to produce 10,000 random numbers
====================================================================
Author: Avijit Maity
====================================================================
'''

import numpy as np
import matplotlib.pyplot as plt


def Gaussian_pdf(x):
	return (1.0/np.sqrt(2.0*np.pi))*np.exp(-x**2.0/2.0)
x=np.linspace(-5.0,5.0,200)

x1 = np.random.rand(100000)
x2 = np.random.rand(100000)
y1 = np.sqrt(-2*np.log(x1)) * np.cos(2*np.pi*x2)
y2 = np.sqrt(-2*np.log(x1)) * np.sin(2*np.pi*x2)

plt.suptitle("Box-Muller method to produce 10,000 random numbers",size=12)

plt.subplot(2,2,1)
plt.hist(x1,20,density = True,facecolor = 'green',ec='black',label = "Density Histogram")
plt.title("Distribution of x1",size = 15)
plt.xlabel("x1",size=13)
plt.ylabel("PDF(x1)",size=13)
plt.tight_layout()
plt.grid()
plt.legend()

plt.subplot(2,2,2)
plt.hist(x2,20,density = True,facecolor = 'red',ec='black',label = "Density Histogram")
plt.title("Distribution of x2",size = 15)
plt.xlabel("x2",size=13)
plt.ylabel("PDF(x2)",size=13)
plt.tight_layout()
plt.grid()
plt.legend()

plt.subplot(2,2,3)
plt.plot(x,Gaussian_pdf(x),color = 'black',label = "Gaussian Distribution")
plt.hist(y1,20,density = True,facecolor = 'yellow',ec='black',label = "Density Histogram")
plt.title("Distribution of y1",size = 15)
plt.xlabel("y1",size=13)
plt.ylabel("PDF(y1)",size=13)
plt.tight_layout()
plt.grid()
plt.legend(loc='upper left', frameon=False)

plt.subplot(2,2,4)
plt.plot(x,Gaussian_pdf(x),color = 'black',label = "Gaussian Distribution")
plt.hist(y2,20,density = True,facecolor = 'blue',ec='black',label = "Density Histogram")
plt.title("Distribution of y2",size = 15)
plt.xlabel("y2",size=13)
plt.ylabel("PDF(y2)",size=13)
plt.tight_layout()
plt.grid()
plt.legend(loc='upper left', frameon=False)

plt.show()