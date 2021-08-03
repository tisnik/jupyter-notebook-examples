
# coding: utf-8

# In[4]:


# Inicializace knihovny `ipywidgets` v Jupyter Notebooku Lite


# In[5]:


import micropip


# In[6]:


await micropip.install('ipywidgets')


# In[8]:


import ipywidgets


# In[9]:


pprint.pprint(ipywidgets.__dir__())

