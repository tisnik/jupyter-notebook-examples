
# coding: utf-8

# In[1]:


# příprava knihovny určené pro instalaci dalších knihoven do prostředí prohlížeče
import micropip


# In[2]:


# instalace knihovny ipycanvas do prostředí prohlížeče
await micropip.install("ipycanvas")


# In[15]:


# nyní je již možné provést import nově nainstalované knihovny
import ipycanvas


# In[128]:


# vytvoření kreslicího plátna
canvas = ipycanvas.Canvas(width=320, height=320)


# In[129]:


# vložení kreslicího plátna na plochu diáře
canvas


# In[130]:


# definice čtveřice cest
path1 = ipycanvas.Path2D('M80 80 A 45 45, 0, 0, 0, 125 125 L 125 80 Z')
path2 = ipycanvas.Path2D('M230 80 A 45 45, 0, 1, 0, 275 125 L 275 80 Z')
path3 = ipycanvas.Path2D('M80 230 A 45 45, 0, 0, 1, 125 275 L 125 230 Z')
path4 = ipycanvas.Path2D('M230 230 A 45 45, 0, 1, 1, 275 275 L 275 230 Z')


# In[131]:


# vykreslení čtveřice cest
canvas.fill_style = 'green'
canvas.fill(path1)

canvas.fill_style = 'purple'
canvas.fill(path2)

canvas.fill_style = 'red'
canvas.fill(path3)

canvas.fill_style = 'blue'
canvas.fill(path4)

