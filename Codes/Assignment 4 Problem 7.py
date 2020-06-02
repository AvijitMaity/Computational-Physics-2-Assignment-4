'''
Chi square test
====================================================================
Author: Avijit Maity
====================================================================
'''

import numpy as np
from scipy.stats import chi2


Y1=np.array([4,10,10,13,20,18,18,11,13,14,13]) #Observed counts 1
Y2=np.array([3,7,11,15,19,24,21,17,13,9,5]) #Observed counts 1
p=np.array([4,8,12,16,20,24,20,16,12,8,4]) #Expected counts 2

V1=np.sum((Y1-p)**2/p)
V2=np.sum((Y2-p)**2/p)


P1=100*(1.0-chi2.cdf(V1,10.0)) # In percentage
P2=100*(1.0-chi2.cdf(V2,10.0)) # In percentage

def criterion(v):
	x = 100*(1.0 - chi2.cdf(v,10.0)) # In percentage
	if(x<1):
		return "Not Sufficiently Random"
	elif(1<x and x<5):
 		return "Suspect"
	elif(5<x and x<1):
 		return"Almost Suspect"
	else:
 		return "Sufficiently Random"

print("Probability for V1 is",P1,"%")
print("Probability for V2 is",P2,"%")
print("The Test results for observed counts 1 :",criterion(V1))
print("The Test results for observed counts 2 :",criterion(V2))
