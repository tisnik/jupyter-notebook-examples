
# coding: utf-8

# In[1]:


import micropip


# In[2]:


await micropip.install("ipywidgets")


# In[3]:


import ipywidgets


# In[35]:


button = ipywidgets.Button(description="Click Me!")
output = ipywidgets.Output()

display(button, output)

@output.capture()
def on_button_clicked(b):
    print(type(b))
    print("Button clicked.")
    b.icon="warning"

button.on_click(on_button_clicked)

