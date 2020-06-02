import numpy as np
import matplotlib.pyplot as plt

def f(x):
	if(3.0<x and x<7.0):
		return 1.0
	else:
		return 0.0


nsteps = 10000
sampled_points= np.zeros(nsteps,dtype = np.float64)
markov_chain = np.array([],dtype = np.float64)
step = np.array([],dtype = np.float64)

x = 4.0

for i in range(nsteps):
    x_prime = x + np.random.standard_normal()
    sampled_points[i]=x_prime
    r = np.random.rand()
    if f(x_prime)/f(x) > r:
            x = x_prime
            markov_chain = np.append(markov_chain, x_prime)
            step = np.append(step, i + 1)


plt.subplot(1,2,1)
plt.title(" Density Historgarm ",size = 15)
plt.hist(markov_chain,20,density = True,facecolor = 'orange',ec='black',label = 'Normalized Histogram')
plt.xlabel("x",size = 13)
plt.ylabel("p(x)",size = 13)
plt.grid()
plt.legend()

plt.subplot(1,2,2)
plt.title("Sampled points and Markov chain ",size = 14)
plt.scatter(np.linspace(1,nsteps,nsteps),sampled_points,marker = '.',color = 'red',label = "Sampled points")
plt.scatter(step,markov_chain,marker = 'x',label = 'Markov Chain')
plt.xlabel("step index",size = 13)
plt.ylabel("x value",size = 13)
plt.legend()
plt.grid()

plt.show()