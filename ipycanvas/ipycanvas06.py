
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


# In[58]:


# vytvoření kreslicího plátna
canvas = ipycanvas.Canvas(width=320, height=240)


# In[59]:


# vložení kreslicího plátna na plochu diáře
canvas


# In[60]:


# změna stylu vykreslování 2D entit
canvas.line_width = 5
# vykreslení základních entit - úseček
canvas.stroke_line(0, 0, 319, 239)


# In[61]:


# oblouk a kružnice
canvas.global_alpha = 0.8
canvas.fill_style = 'lightblue'
canvas.fill_arc(160, 120, 50, 0, 3.14)

canvas.global_alpha = 0.5
canvas.stroke_style = '#4e6393'
canvas.stroke_circle(160, 120, 40)


# In[62]:


# obdélník
canvas.global_alpha = 0.1
canvas.fill_style = 'red'
canvas.fill_rect(0, 0, 320, 240)

