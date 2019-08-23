#!/usr/bin/env python
# coding: utf-8

# In[123]:


import pandas as pd
import numpy as np


# In[124]:


data = pd.read_csv('./data/prices.csv')


# In[125]:


data.head()


# In[126]:


data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')


# In[127]:


## Sort data
data = data.sort_values(['date'], ascending=[True])


# In[128]:


data['intercept'] = 1


# In[129]:


pivot_data = pd.pivot_table(data, index="date" ,values="open", columns="symbol")


# In[130]:


stockNames = data['symbol'].unique()
stockNames


# In[131]:


pivot_data.head()


# In[136]:


stock_frame = pivot_data.iloc[:, 1:]
stock_frame['intercept'] = 1
weights = np.array([1.0 / len(stockNames)] * len(stockNames))


# In[138]:


portfolio_variance = np.dot(np.dot(weights, stock_frame.cov()), weights.T)


# In[140]:


portfolio_variance


# In[ ]:




