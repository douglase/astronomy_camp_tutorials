
# coding: utf-8

# In[3]:

get_ipython().magic('matplotlib inline')
from pylab import *
from astropy.modeling import models, fitting

d_June17th = array([#[32950,25],
            #[32651,11],
            #[32550,7.32],
            [32350,4.21],
            #[32150,10],
            [32450,5.99],
                   [32301,7.61]])

#define vectors to plot
x=d_June17th[:,0]
y=d_June17th[:,1]


# Find the best approximation of the data using a Parabola
g_init = models.Polynomial1D(2)
fit_g = fitting.LinearLSQFitter()
g = fit_g(g_init, x, y)

# Plot the data with the best-fit model
plt.figure(figsize=(8,5))
plt.plot(x, y, 'ko',label='data')
x_precise=np.arange(x.min()-200,x.max()+200)
plt.plot(x_precise, g(x_precise), label='parabola')
plt.xlabel('Position')
plt.ylabel('width')
plt.legend(loc=2)


# In[ ]:




# In[ ]:



