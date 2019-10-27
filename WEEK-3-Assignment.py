#!/usr/bin/env python
# coding: utf-8

# In[12]:



pip install wikipedia


# In[20]:


import pandas as pd
import wikipedia as wp
from bs4 import BeautifulSoup
html = wp.page("List of postal codes of Canada: M").html().encode("UTF-8")


# In[22]:


df = pd.read_html(html,header = 0)[0]
df = df[df.Borough!= 'Not assigned']
df = df.groupby(['Postcode', 'Borough'])['Neighbourhood'].apply(list).apply(lambda x:','.join(x)).to_frame().reset_index()


# In[24]:


for index, row in df.iterrows():
    if row['Neighbourhood']=='Not assigned':
        row['Neighbourhood'] = row['Borough']
        
df


# In[ ]:




