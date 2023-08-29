#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import re


# In[3]:


data_path = 'D:\\codegym3\\'
data_name = 'OnlineRetail.csv'

df = pd.read_csv(data_path+data_name, encoding= 'unicode_escape')


# In[4]:


df.head(5)


# In[5]:


df.info()


# In[9]:


df['Country'].nunique()


# In[18]:


df['total']= df['Quantity']*df['UnitPrice']

df.head(2)

t = df['total'].sum()

print(str(t.size))
print(t.sum())


# In[24]:


q = df.groupby(['StockCode'])['Description'].sum().reset_index()

top_10_q= q.sort_values(by='StockCode', ascending=False).head(10)


print(top_10_q)


# In[19]:


df.head(2)

