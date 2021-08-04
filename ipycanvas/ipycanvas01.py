
# coding: utf-8

# In[4]:


# příprava knihovny určené pro instalaci dalších knihoven do prostředí prohlížeče
import micropip


# In[5]:


# instalace knihovny ipycanvas do prostředí prohlížeče
await micropip.install("ipycanvas")


# In[8]:


# nyní je již možné provést import nově nainstalované knihovny
import ipycanvas


# In[9]:


# zobrazení nápovědy k naimportované knihovně
help(ipycanvas)

