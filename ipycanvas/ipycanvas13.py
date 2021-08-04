
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


# In[23]:


# vytvoření kreslicího plátna
canvas = ipycanvas.Canvas(width=200, height=200)


# In[24]:


# vložení kreslicího plátna na plochu diáře
canvas


# In[25]:


# definice cesty
path1 = ipycanvas.Path2D('M 50 150 h 100 l -100 -100 v 100 l 100 -100 h -100 l 50 -50 l 50 50 v 100')


# In[26]:


# vykreslení cesty
canvas.fill_style = 'orange'
canvas.stroke_style = 'black'

canvas.fill(path1)

