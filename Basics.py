
# coding: utf-8

# Each gray box with 
# 
#     In []:
#     
# beside it is a bit of computer code and you run then by pressing the play button or pressing "Shift-Enter". 

# In[30]:

#this is a comment - the computer will remember it but not act on it.
print("this is a command or function, it tells the computer to print out the text")


# In[31]:

#try to display "hello world":


# In[32]:

#these commands setup our python environment for scientific programming and plotting
get_ipython().magic('pylab')
get_ipython().magic('matplotlib inline')
import astropy.io.fits as fits

rcParams['image.cmap'] = 'viridis' 
plt.xkcd()


# ## Just like algebra
# 
# We can assign a number to a variable and do math

# In[33]:


x = 2
a = 3.5
y = x + a

print(y)




# In[34]:

#you can skip a step and do math inside the print function:
print(y/x)


# ### The it remembered our variables from one box to the next --- spooky?

# ## Debugging

# In[35]:

print(z)
z=x*a


# # we can do lots of math at once
# 
# This is good -- astronomers are lazy

# In[ ]:


x=array([3,2,5,2,2,2,2,1])
a=array([5,5,5,5,5,5,5,5,])
SubtractedArrays=a-x
print(SubtractedArrays)


# In[ ]:

plot(SubtractedArrays)
plt.xlabel("location of number in arrays")
plt.ylabel("a-x")


# ## lets just like at the first four numbers

# In[36]:

plot(SubtractedArrays[:4])
plt.xlabel("location of number in arrays")
plt.ylabel("a-x")


# ## print the original array and see if it as has changed:

# In[ ]:




# ## Let's get some real data
# Last night we collected some images of the interacting galaxies NGC 6240
# 
# 

# In[37]:

image = fits.getdata("data/wiyn0_9/2016june18/NGC6240/c7558t0054o00.fits")


# In[38]:

#decrease the vmax until you can see the galaxies
figure(figsize=(10,10))
imshow(image,vmax=20000)
colorbar()


# ## more debugging -- getting help
# 

# In[39]:

#you can call a function with a ? to get help on it.
get_ipython().magic('pinfo fits.getdata')


# ## Removing Bias levels

# In[40]:

#calculate bias  1a.  compute mean value, M, of pixels in overscan columns 4100 - 4140
overscan=image[4100:4140,4100:4140] 
mean_bias=mean(overscan) #this is the average
image_without_bias = image - mean_bias


# In[41]:

figure(figsize=(12,10))
imshow(image_without_bias,vmax=9000,vmin=5000)
colorbar()


# In[42]:

#apply the flat field
flat =  fits.getdata("data/wiyn0_9/2016june18/c7558t0010f00.fits")
flat = flat-mean(flat[4100:4140,4100:4140] )
flat = flat/mean(flat)
image_flattened = image_without_bias/flat


# In[43]:

figure(figsize=(12,10))
imshow(image_flattened,vmax=9000,vmin=0)
colorbar()


# ## Look at just the pixels close to NGC 6240

# In[44]:

figure(figsize=(12,10))
#just like when we looked at the first four values in an array, look at pixels from 1800 to 2300, in both directions
imshow(image_flattened[1800:2300,1800:2300],vmax=7000,vmin=5000)
colorbar()


# ## why is the background still so high?
# 
# What was in the sky last night?

# ## TRY THIS AT HOME!
# 
# You can install  the Anaconda Scientific python platform on your (Windows/Mac/Linux) computer for free and run this  notebook in your web-browser or make your own:
# 
# https://www.continuum.io/downloads
# 
# Or you can use a webserver operated by a company to run it remotely. some examples are:
# https://cloud.sagemath.com/
# 
# A copy of this tutorial for refence:
# 

# In[ ]:



