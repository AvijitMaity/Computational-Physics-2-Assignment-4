'''
Linear congruential random number generator in Python
====================================================================
Author: Avijit Maity
====================================================================
'''

import numpy as np
import matplotlib.pyplot as plt
import time

n=10000
a=12367
c=301345698
x=0.3
m=1

results = []

start = time.time() # here we will start our clock to compute the time taken by the code
for i in range(n):
     x = (a*x+c) % m
     results.append(x)

print(f'Time: {time.time() - start}') #Time taken to produce 10,000 uniform deviates


plt.plot(np.linspace(0,1,2),np.ones(2),color = 'black',label = "True Uniform Distribution")
plt.hist(results,20,density = True,facecolor = 'green',ec='black',label = "Density Histogram")
plt.xticks( np.arange(0, 1.05, step=0.05))
plt.title("Linear congruential random number generator in Python",size = 14)
plt.xlabel("x")
plt.ylabel("PDF")
plt.grid()
plt.legend()
plt.show()