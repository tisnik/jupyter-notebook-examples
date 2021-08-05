
# coding: utf-8

# In[1]:


# příprava knihovny určené pro instalaci
# dalších knihoven do prostředí prohlížeče
import micropip


# In[2]:


# instalace knihovny ipycanvas do prostředí prohlížeče
await micropip.install("ipycanvas")


# In[3]:


# nyní je již možné provést import nově nainstalované knihovny
import ipycanvas


# In[49]:


# vytvoření kreslicího plátna
canvas = ipycanvas.Canvas(width=320, height=240)


# In[50]:


# zvýraznění začátku a konce úseček
canvas.line_width = 1
canvas.stroke_line(20, 20, 20, 220)
canvas.stroke_line(310, 20, 310, 220)


# In[51]:


# vložení kreslicího plátna na plochu diáře
canvas


# In[52]:


# vzorek použitý pro vykreslení čar
line_dash = [20, 20]


# In[53]:


# vykreslení několika úseček na plochu plátna
canvas.line_width = 2

# nastavení vzorku
canvas.set_line_dash(line_dash)
 
canvas.stroke_style = "black"
 
for i in range(0,10):
    y = 30 + i * 20
 
    canvas.fill_text(str(i+1), 5, y+5)
    canvas.line_dash_offset = i*2
    canvas.begin_path()
    canvas.move_to(20, y)
    canvas.line_to(310, y)
    canvas.stroke()

