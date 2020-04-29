
# coding: utf-8

# In[15]:


import numpy as np
from matplotlib import pyplot as plt


# In[16]:


raster = np.zeros(shape=(450, 450, 3), dtype=np.uint8)


# In[17]:


plt.figure(1, figsize=(8,6), dpi=100)
plt.imshow(raster)


# In[18]:


plt.show()

