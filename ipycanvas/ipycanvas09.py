
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


# In[95]:


# vytvoření kreslicího plátna
canvas = ipycanvas.Canvas(width=320, height=240)


# In[96]:


# vložení kreslicího plátna na plochu diáře
canvas


# In[97]:


radial_gradient = canvas.create_radial_gradient(
    160, 120, 10,
    160, 120, 100,
    [
        (0, 'yellow'),
        (1, 'white'),
    ]
)


# In[98]:


# obdélník
canvas.fill_style = radial_gradient
canvas.fill_circle(160, 120, 200)

