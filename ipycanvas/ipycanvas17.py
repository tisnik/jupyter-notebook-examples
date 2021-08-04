
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


# In[35]:


# vytvoření kreslicího plátna
canvas = ipycanvas.Canvas(width=320, height=240)


# In[36]:


# zvýraznění okrajů plátna
canvas.stroke_style = "gray"
canvas.stroke_rect(0, 0, 319, 239)


# In[37]:


# vložení kreslicího plátna na plochu diáře
canvas


# In[38]:


# vykreslení několika úseček na plochu plátna
for i in range(10):
    y = 30 + i * 20

    canvas.fill_text(str(i+1), 5, y+5)

    canvas.begin_path()
    canvas.move_to(20, y)
    canvas.line_to(310, y)
    canvas.stroke()

