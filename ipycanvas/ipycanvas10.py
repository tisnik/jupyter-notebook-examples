
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


# In[106]:


# vytvoření kreslicího plátna
canvas = ipycanvas.Canvas(width=320, height=240)


# In[107]:


# vložení kreslicího plátna na plochu diáře
canvas


# In[108]:


# parametry vykreslovaného textu
canvas.font = '32px serif'

# výpis textu
canvas.fill_text('www.root.cz', 10, 120)

