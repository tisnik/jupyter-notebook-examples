
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


# In[69]:


# vytvoření kreslicího plátna
canvas = ipycanvas.Canvas(width=320, height=240)


# In[70]:


# vložení kreslicího plátna na plochu diáře
canvas


# In[73]:


gradient = canvas.create_linear_gradient(0, 0, 0, 240,
    [
        (0, 'red'),
        (1 / 6, 'orange'),
        (2 / 6, 'yellow'),
        (3 / 6, 'green'),
        (4 / 6, 'blue'),
        (5 / 6, '#4B0082'),
        (1, 'violet')
    ]
)


# In[74]:


# obdélník
canvas.fill_style = gradient
canvas.fill_rect(0, 0, 320, 240)

