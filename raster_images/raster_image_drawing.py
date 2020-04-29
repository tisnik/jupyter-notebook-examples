
# coding: utf-8

# In[1]:


import numpy as np
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt


# In[56]:


filename="house.png"
img = Image.open(filename)


# In[57]:


draw = ImageDraw.Draw(img)
width, height = img.size[0], img.size[1]


# In[58]:


for x in range(0, width, 16):
    draw.line((x, 0, x, height-1), fill=(255, 255, 255))

for y in range(0, height, 16):
    draw.line((0, y, width-1, y), fill=(255, 255, 255))


# In[59]:


size = 2*width/72
plt.figure(1, figsize=(size,size), dpi=100)
plt.imshow(img, interpolation="none")


# In[60]:


plt.show()

