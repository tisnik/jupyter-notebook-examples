
# coding: utf-8

# In[22]:


# příprava knihovny určené pro instalaci dalších knihoven do prostředí prohlížeče
import micropip


# In[23]:


# instalace knihovny ipycanvas do prostředí prohlížeče
await micropip.install("ipycanvas")


# In[24]:


# nyní je již možné provést import nově nainstalované knihovny
import ipycanvas


# In[58]:


# vytvoření kreslicího plátna
canvas = ipycanvas.Canvas(width=320, height=240)


# In[59]:


# zvýraznění okrajů plátna
canvas.stroke_style = "gray"
canvas.stroke_rect(0, 0, 319, 239)


# In[60]:


# vložení kreslicího plátna na plochu diáře
canvas


# In[61]:


# zvýraznění začátku a konce úseček
canvas.line_width = 1
canvas.stroke_line(20, 20, 20, 220)
canvas.stroke_line(310, 20, 310, 220)


# In[66]:


# vykreslení několika úseček na plochu plátna
canvas.line_cap = "butt"

canvas.stroke_style = "black"

for i in range(10):
    y = 30 + i * 20

    canvas.fill_text(str(i+1), 5, y+5)

    canvas.line_width = i
    canvas.begin_path()
    canvas.move_to(20, y)
    canvas.line_to(310, y)
    canvas.stroke()

