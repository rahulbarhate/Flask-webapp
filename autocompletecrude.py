
# coding: utf-8

# In[1]:


import requests


# In[2]:


url = "http://suggestqueries.google.com/complete/search"


# In[3]:


params = {
    "client": "firefox",
    "q": "sal",
    "hl": "en"
}


# In[4]:


r = requests.get(url, params = params)


# In[5]:


#print(r.text)


# In[6]:


print(r.json())

