
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


# In[11]:


def plot(amplitude, phase, phase2):
    x = np.arange(0, 6.28, 0.1)
    y1 = np.sin(amplitude*x+phase)
    plt.plot(x,y1)
    y2 = np.sin(amplitude*x+phase2)
    plt.plot(x,y2)
    plt.show()


# In[12]:


w = ipywidgets.interactive(plot, amplitude=(0.5, 2.0, 0.1), phase=(0, 10, 0.1), phase2=(0, 10, 0.1))


# In[14]:


display(w)

