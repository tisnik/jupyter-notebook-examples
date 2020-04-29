
# coding: utf-8

# In[2]:


import numpy as np
from PIL import Image, ImageFilter
from matplotlib import pyplot as plt


# In[3]:


filename="house.png"
img = Image.open(filename)


# In[5]:


edges = img.filter(ImageFilter.FIND_EDGES)


# In[10]:


plt.figure(1, figsize=(6,6), dpi=100)
plt.imshow(edges)


# In[11]:


plt.show()

