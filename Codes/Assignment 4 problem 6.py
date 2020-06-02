'''
Rejection Method in Python
====================================================================
Author: Avijit Maity
====================================================================
'''

import numpy as np
from matplotlib import pyplot as plt

def f(x): #Distribution function
 	return np.sqrt(2.0/np.pi)*np.exp(-0.5*x**2.0)

def g(x): # Enclosing function
 	return 1.5*np.exp(-x)
X=np.linspace(0,10,1000) # x values for plotting f(x), g(x)

x = np.random.rand(10000)
x = -np.log(x)
y =np.random.rand(10000)*g(x) #for each x, let us get a value y that is uniformly random
                              #between 0 and g(x):
X1=[]
Y1=[]

for i in range(len(x)):
	if(y[i]<f(x[i])):
		X1.append(x[i])
		Y1.append(y[i])


plt.plot(X,f(X),color = "red",label = "Given Distribution in the problem")
plt.plot(X,g(X),color = 'black',label = "Enveloping function")
plt.hist(X1,20,density = True,facecolor = 'blue',ec='black',label = 'Density Histogram')
plt.xlabel("x",size = 13)
plt.ylabel("PDF(x)",size = 13)
plt.title(" Rejection Method",size = 16)
plt.legend()
plt.grid()
plt.show()
