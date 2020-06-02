'''
Python code to compute volume of n dimensional sphere
====================================================================
Author: Avijit Maity
====================================================================
'''
# For circle with unit radius
import random
N1 = 100000

count = 0  # count will store the number of random points
          # that fell within the unit circle

for i in range(N1):
    x, y = random.random(), random.random()
    if x ** 2 + y ** 2 < 1:  # sqrt(1-x**2) < y
        count += 1

print("Area of circle is",4.0 * count / N1)


#the volume of a ten-dimensional unit sphere.

import numpy as np

def nSphereVolume(dim, N):
    count = 0   #count will store the number of random points
               #that fell within the unit circle


    for i in range(N):
        point = np.random.uniform(-1.0, 1.0, dim)
        distance = np.linalg.norm(point)
        if distance < 1.0:
            count += 1

    return np.power(2.0, dim) * (count / N)  #these points are uniformly distributed in the hypercube
                                             # of dimension dim. The volume of a hypercube is the product of its sides.
                                            #  Each side has length 2.0 so we can calculate the hypercube's volume
                                             #  with 2.0 power dim, or np.power(2.0, dim)

print("Volume of 2 dim sphere is", nSphereVolume(2, 100000))
print("Volume of 10 dim sphere is",nSphereVolume(10, 100000))