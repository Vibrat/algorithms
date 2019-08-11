#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


np.random.seed(0)
mu, sigma = 0, 1

data = np.random.normal(mu, sigma, 1000) 


# In[12]:


p = sns.distplot(data, kde=True, color="b", bins=50)


# In[13]:


kdeplot = sns.kdeplot(data, color="b", shade=True)


# In[31]:


boxplot = sns.boxplot(data)


# In[32]:


violin = sns.violinplot(data)


# In[36]:


violin = plt.violinplot(data, vert=False, showmeans=True, showmedians=True)


# In[41]:


## jitter represent stripping level
strip = sns.stripplot(x= data, jitter=1) 


# In[42]:


swarm = sns.swarmplot(x=data)


# In[ ]:




