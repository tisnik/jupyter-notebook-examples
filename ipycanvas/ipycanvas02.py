
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


# In[10]:


# vytvoření kreslicího plátna
canvas = ipycanvas.Canvas(width=320, height=240)


# In[11]:


# vložení kreslicího plátna na plochu diáře
canvas

