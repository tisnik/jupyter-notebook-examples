
# coding: utf-8

# In[1]:


import micropip


# In[2]:


await micropip.install("ipywidgets")


# In[3]:


import ipywidgets


# In[4]:


import matplotlib.pyplot as plt
import numpy as np


# In[5]:


def plot(phase):
    x = np.arange(0, 6.28, 0.1)
    y = np.sin(x+phase)
    plt.plot(x,y)
    plt.show()


# In[6]:


w = ipywidgets.interactive(plot, phase=(0, 10, 0.1))


# In[8]:


display(w)

