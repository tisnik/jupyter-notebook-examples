
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


# In[124]:


# vytvoření kreslicího plátna
canvas = ipycanvas.Canvas(width=320, height=240)


# In[125]:


# zvýraznění začátku a konce úseček
canvas.stroke_line(20, 20, 20, 220)
canvas.stroke_line(310, 20, 310, 220)


# In[126]:


# vložení kreslicího plátna na plochu diáře
canvas


# In[127]:


# vzorek použitý pro vykreslení čar
line_dash = [20, 20]


# In[128]:


# vykreslení několika úseček na plochu plátna
canvas.line_width = 5

# nastavení vzorku
canvas.set_line_dash(line_dash)
 
canvas.stroke_style = "black"
 
for i in range(0,20):
    angle = i * 2 * math.pi/20.0
    canvas.fill_text(str(i+1), 5, y+5)
    canvas.line_dash_offset = i*2
    canvas.begin_path()
    canvas.move_to(160+10*math.sin(angle), 120+10*math.cos(angle))
    canvas.line_to(160+100*math.sin(angle), 120+100*math.cos(angle))
    canvas.stroke()

