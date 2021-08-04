
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


# In[115]:


# vytvoření kreslicího plátna
canvas = ipycanvas.Canvas(width=320, height=240)


# In[116]:


# vložení kreslicího plátna na plochu diáře
canvas


# In[117]:


# parametry vykreslovaného textu
canvas.font = '32px serif'

# vycentrování textu okolo zadaného bodu
canvas.text_align = 'center'

# vertikální umístění textu na základní čáru
canvas.text_baseline = 'middle'

# výpis textu
canvas.fill_text('www.root.cz', 160, 120)

