
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


# In[25]:


# vytvoření kreslicího plátna
canvas = ipycanvas.RoughCanvas(width=320, height=240)


# In[26]:


# vložení kreslicího plátna na plochu diáře
canvas


# In[27]:


# definice cesty
path1 = ipycanvas.Path2D('M 0 100 Q 50 0 100 100 T 200 100')


# In[28]:


# vykreslení cesty
canvas.fill_style = 'gray'
canvas.stroke_style = 'black'

canvas.fill(path1)


# In[29]:


# vykreslení obdélníku
canvas.stroke_rect(0, 0, 319, 239)


# In[30]:


canvas.stroke_circle(160, 60, 40)


# In[31]:


canvas.fill_circle(260, 180, 40)


# In[32]:


canvas.stroke_line(10, 200, 200, 200)

