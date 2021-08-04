
# coding: utf-8

# In[7]:


# příprava knihovny určené pro instalaci dalších knihoven do prostředí prohlížeče
import micropip


# In[8]:


# instalace knihovny ipycanvas do prostředí prohlížeče
await micropip.install("ipycanvas")


# In[9]:


# nyní je již možné provést import nově nainstalované knihovny
import ipycanvas


# In[16]:


# vytvoření kreslicího plátna
canvas = ipycanvas.Canvas(width=320, height=240)


# In[ ]:


# 


# In[17]:


# vložení kreslicího plátna na plochu diáře
canvas

