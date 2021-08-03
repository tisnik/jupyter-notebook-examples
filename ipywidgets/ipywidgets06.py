
# coding: utf-8

# In[1]:


import micropip


# In[2]:


await micropip.install("ipywidgets")


# In[3]:


import ipywidgets


# In[4]:


def callbackFunction(x):
    return 2*x


# In[5]:


ipywidgets.interact(callbackFunction, x=10)

