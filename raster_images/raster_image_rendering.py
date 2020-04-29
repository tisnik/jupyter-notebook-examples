
# coding: utf-8

# In[27]:


import numpy as np
from matplotlib import pyplot as plt


# In[28]:


WIDTH = 256
HEIGHT = 256
raster = np.zeros(shape=(HEIGHT, WIDTH, 3), dtype=np.uint8)


# In[29]:


for y in range(HEIGHT):
    for x in range(WIDTH):
        raster[y][x][0] = x
        raster[y][x][1] = 255
        raster[y][x][2] = y


# In[30]:


plt.figure(1, figsize=(8,6), dpi=100)
plt.imshow(raster)


# In[31]:


plt.show()

