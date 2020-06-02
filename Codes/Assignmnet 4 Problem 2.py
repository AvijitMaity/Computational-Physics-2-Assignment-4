'''
Random number using  np.random.rand()
====================================================================
Author: Avijit Maity
====================================================================
'''
import numpy as np
import matplotlib.pyplot as plt
import time

start = time.time() # here we will start our clock to compute the time taken by the code

x = np.random.rand(10000)
print(f'Time: {time.time() - start}') # #Time taken to produce 10,000 uniform deviates


plt.plot(np.linspace(0,1,2),np.ones(2),color = 'black',label = "True Uniform Distribution") # Here we will plot our true uniform pdf
plt.hist(x,20,density = True,facecolor = 'green',ec='black',label = "Density Histogram")
plt. xticks(np.arange(0, 1.05, step=0.05))
plt.title("Random number using  np.random.rand()",size = 16)
plt.xlabel("x",size=14)
plt.ylabel("PDF",size=14)
plt.grid()
plt.legend()
plt.show()