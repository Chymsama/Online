#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import re


# In[5]:


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


# In[11]:


selected_columns = df[['Description', 'Quantity']]
selected_columns.to_csv("D:\codegym3\OnlineReatail2.txt", index=False)


# In[19]:


selected_rows = df.head(1000)
selected_rows.to_excel("D:\codegym3\OnlineRetail.xlsx", index=False, engine='openpyxl')


# In[27]:


selected_data = df.loc[1000:2000, ['Quantity', 'InvoiceDate', 'UnitPrice']]
selected_data.to_json("D:\codegym3\OnlineRetail.json", orient='records')


# In[31]:


filtered_data = df[df['InvoiceNo'] == '536365']
filtered_data.to_html("D:\codegym3\OnlineRetail.html", index=False)

