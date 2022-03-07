#!/usr/bin/env python
# coding: utf-8

# In[15]:


import requests
from bs4 import BeautifulSoup
url='https://check.torproject.org/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title.text.replace("browser is configured to use", "system is connected to"))
#By 4K5H4Y 4RJUN ^_+


# In[ ]:





# In[ ]:




