import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import corner


x=np.loadtxt("data.txt",usecols=[1],delimiter="&")
y= np.loadtxt("data.txt",usecols=[2],delimiter="&")
yerr=np.loadtxt("data.txt",usecols=[3],delimiter="&")

#Let us begin by coding up our lnL function
def log_likelihood(theta, x, y, yerr):
    a, b,c = theta
    model = a*x**2 + b*x + c
    sigma2 = yerr**2
    # actually negative ln L
    return 0.5 * np.sum((y - model) ** 2 / sigma2 + np.log(2 * np.pi * sigma2))

#Now the prior distribution p(m; bjI).
#We are a priori ignorant about the parameters so we choose a uniform prior:
def log_prior(theta):
    a, b,c = theta
    if -500.0 < a< 500 and 0.0 < b < 1000.0 and -100<c<100:
        return 0.0
    return -np.inf

#With the prior and likelihood coded up, we can now code our posterior PDF:
def log_probability(theta, x, y, yerr):
     lp = log_prior(theta)
     if not np.isfinite(lp):
         return -np.inf
     return lp - log_likelihood(theta, x, y, yerr)

#Now we can sample our posterior PDF using MCMC.
#Let us use 50 Markov chains.
# a common idea to initialise them is to start near the optimum of the likelihood.
guess = (1.0, 1.0,1.0)
soln = minimize(log_likelihood,guess,args=(x, y, yerr))

#We now initialise each of our 50 Markov chains near the
#optimum reported by the minimize function.
nwalkers, ndim = 50, 3
pos = soln.x + 1e-4 * np.random.randn(nwalkers, ndim)

#We now use the emcee library to do the MCMC so that each
#Markov chain takes 5,000 steps.
import emcee
sampler = emcee.EnsembleSampler(nwalkers,ndim,log_probability,args=(x, y, yerr))
sampler.run_mcmc(pos, 4000)

#We can look at the chains by plotting them:
samples = sampler.get_chain()
plt.suptitle("Plotting MCMC chains of the parameters")
plt.subplot(3,1,1)
plt.plot(samples[:, :, 0])
plt.xlabel("Step number")
plt.ylabel("MCMC chains of a")
plt.tight_layout()

plt.subplot(3,1,2)
plt.plot(samples[:, :, 1])
plt.xlabel("Step number")
plt.ylabel("MCMC chains of b")
plt.tight_layout()

plt.subplot(3,1,3)
plt.plot(samples[:, :, 2])
plt.xlabel("Step number")
plt.ylabel("MCMC chains of c")
plt.tight_layout()

plt.show()


# computing Medians for true values
medians = np.median(samples, axis=0)

a_true, b_true, c_true = np.average(medians,axis=0)  # computing the the value of the parameters by averaging over the 50 chains

data = np.zeros([4000 * 50, 3])

for i in range(3):
    data[:, i] = np.hstack(samples[:, :, i])

# We can plot the posterior PDF using the corner library.

fig = corner.corner(samples.reshape(40 * 5000, 3), labels=["a", "b", "c"], quantiles=[0.16, 0.5, 0.84],
                    truths=[a_true, b_true, c_true], show_titles=True)
plt.show()

X = np.linspace(0, 300, 1000)

for i in range(200):
    r = np.random.randint(0, high=4000 * 50)
    a = data[r, 0]
    b = data[r, 1]
    c = data[r, 2]
    plt.plot(X, a * X ** 2 + b * X + c)

x = np.sort(x)
plt.plot(X, a_true * X ** 2 + b_true * X + c_true,color = 'black',lw = 2,label = "True Model")
plt.errorbar(x, y, yerr=yerr,fmt = 'o',ecolor = 'black',elinewidth = 0.75,lolims = True,uplims = True,label = "Data with error bars")
plt.xlabel("x data")
plt.ylabel("y data")
plt.title("Data with Model and Candidate Models",size = 14)
plt.legend()
plt.show()


