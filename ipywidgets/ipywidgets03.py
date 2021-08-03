
# coding: utf-8

# In[1]:


import micropip


# In[2]:


await micropip.install("ipywidgets")


# In[3]:


import ipywidgets


# In[5]:


slider = ipywidgets.IntSlider()


# In[6]:


slider


# In[7]:


slider.value


# In[8]:


slider.value = 10


# In[9]:


slider.orientation


# In[10]:


slider.description="a slider"


# In[11]:


slider.orientation='vertical'

