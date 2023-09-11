#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
import pandas as pd
import re


# In[25]:


data_path ="D:\codegym3\\"
data_name = "OnlineRetail.xlsx"

df= pd.read_excel(data_path+data_name)
df.head()


# In[26]:


df.shape


# In[27]:


df.dtypes


# In[28]:


df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'])


# In[29]:


df.dtypes


# Tạo cột mới có tên quý –  ‘Previous’ nhận giá trị 1 nếu ngày lập hóa đơn nằm trong các tháng 1,2,3; nhận giá trị 2 nếu ngày lập hóa đơn nằm trong các tháng 4,5,6; nhận giá trị 3 nếu ngày lập hóa đơn nằm trong các tháng 7,8,9;  nhận giá trị 4 nếu ngày lập hóa đơn nằm trong các tháng 10,11,12;

# In[31]:


def map_to_quarter(month):
    if month in [1,2,3]:
        return 1
    elif month in [4,5,6]:
        return 2
    elif month in [7,8,9]:
        return 3
    else:
        return 4
    
df['Previous']= df['InvoiceDate'].apply(lambda x : map_to_quarter(x.month))

df


# Tạo một cột mới có tên ‘Amount’ có giá trị bằng Quantity * UnitPrice

# In[32]:


df['Amount'] = df['Quantity']*df['UnitPrice']

df.head(3)


# Tạo cột mới ‘Discount’ nhận giá trị 10% nếu Country là ‘United Kingdom’ và thuộc quý 4, 5% nếu là ‘France’ ngược lại là 0%.
# 

# In[34]:


def calculate_dis(row):
    if row['Country']=='United Kingdom' and row['Previous'] == 4:
        return 0.1
    elif row['Country'] == 'France':
        return 0.05
    else:
        return 0
    
df['Discount'] = df.apply(calculate_dis, axis= 1)

df


# Tạo cột mới ‘Total’ nhận giá trị bằng: Amount – Discount.

# In[35]:


df['Total'] = df['Amount']- df['Discount']

df

