
# coding: utf-8

# In[1]:


# příprava knihovny určené pro instalaci dalších knihoven do prostředí prohlížeče
import micropip


# In[2]:


# instalace knihovny ipycanvas do prostředí prohlížeče
await micropip.install("ipycanvas")


# In[3]:


# nyní je již možné provést import nově nainstalované knihovny
import ipycanvas


# In[4]:


# vytvoření kreslicího plátna
canvas = ipycanvas.Canvas(width=200, height=200)


# In[5]:


# vložení kreslicího plátna na plochu diáře
canvas

