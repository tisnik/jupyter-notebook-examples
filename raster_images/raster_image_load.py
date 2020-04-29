
# coding: utf-8

# In[32]:


import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


# In[33]:


filename="house.png"
img = Image.open(filename)


# In[34]:


plt.figure(1, figsize=(6,6), dpi=100)
plt.imshow(img)


# In[35]:


plt.show()

