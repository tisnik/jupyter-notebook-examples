
# coding: utf-8

# In[2]:


import micropip


# In[3]:


await micropip.install("ipywidgets")


# In[4]:


import ipywidgets


# In[5]:


ipywidgets.IntSlider(
    value=7,
    min=-50,
    max=50,
    step=2,
    description='Second widget:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

