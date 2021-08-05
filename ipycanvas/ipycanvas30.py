
# coding: utf-8

# In[1]:


# příprava knihovny určené pro instalaci
# dalších knihoven do prostředí prohlížeče
import micropip


# In[2]:


# instalace knihovny ipycanvas do prostředí prohlížeče
await micropip.install("ipycanvas")


# In[107]:


# nyní je již možné provést import nově nainstalované knihovny
import ipycanvas
import math


# In[146]:


# vytvoření kreslicího plátna
canvas = ipycanvas.RoughCanvas(width=320, height=240)


# In[147]:


# zvýraznění začátku a konce úseček
canvas.stroke_line(20, 20, 20, 220)
canvas.stroke_line(310, 20, 310, 220)


# In[148]:


# vložení kreslicího plátna na plochu diáře
canvas


# In[149]:


canvas.stroke_style = 'black'


# In[150]:


# vykreslení několika úseček na plochu plátna
for i in range(10):
    y = 30 + i * 20

    canvas.fill_text(str(i+1), 5, y+5)

    canvas.stroke_line(20, y, 310, y)

