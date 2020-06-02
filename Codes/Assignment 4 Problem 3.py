import numpy as np
import matplotlib.pyplot as plt
import time

# Time for problem 1
n=10000
a=12367
c=301345698
x=0.3
m=1

results = []

start1 = time.time() # here we will start our clock to compute the time taken by the code
for i in range(n):
     x = (a*x+c) % m
     results.append(x)

print(f'Time taken using Linear congruential random number generator: {time.time() - start1}') #Time taken to produce 10,000 uniform deviates

# Time for problem 2
start2 = time.time() # here we will start our clock to compute the time taken by the code

x = np.random.rand(10000)
print(f'Time taken using np.random.rand : {time.time() - start2}') #Time taken to produce 10,000 uniform deviates
