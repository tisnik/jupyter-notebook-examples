
# coding: utf-8

# In[14]:


import numpy as np
from PIL import Image, ImageFilter
from matplotlib import pyplot as plt


# In[15]:


filename="house.png"
img = Image.open(filename)


# In[16]:


blurred = img.filter(ImageFilter.BLUR)


# In[19]:


plt.figure(1, figsize=(8,6), dpi=100)
plt.imshow(blurred)


# In[20]:


plt.show()

