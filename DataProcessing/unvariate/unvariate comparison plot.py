#!/usr/bin/env python
# coding: utf-8

# In[4]:


import seaborn as sns
import pandas as pd
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


data_tips = sns.load_dataset('tips')


# In[6]:


data_tips.describe()


# In[7]:


data_tips.head()


# In[8]:


## Create barplot using seaborn
barplot_dist = sns.barplot('size', y='total_bill', data=data_tips, errwidth=0)


# In[9]:


# barplot using matplotlib
x_data = ['A', 'B', 'C', 'D']
y_data = [0, 1, 2, 3]

sns_barplot = plt.bar(x_data, y_data) 


# In[28]:


## LinePlot using Seaborn

line_plot  = sns.lineplot(x='size', y='total_bill', data=data_tips, color="r")
line_plot2 = sns.lineplot(x='size', y='tip', data=data_tips, color="b")

## line plot by matplotlib

data = [4, 8, 9 , 15 , 3 , 2,2 ,3 ,4 ,5 ]
line_plot3 = plt.plot(range(len(data)), data, color='y')

# fill color in the area under line plot
plt.fill_between(range(len(data)), data, color="y", alpha=0.2)


# In[11]:


## Lag plot
data_prep = data_tips['tip']
pd.plotting.lag_plot(data_prep, lag = 1, c="r")


# In[29]:


## Angles Area
angles = [a/4 * 2 * np.pi for a in range(4)]
angles.append(angles[0])
angles


# In[51]:


# Circular Area Plot

plt.subplot(111, polar=True)
plt.plot(angles, [3, 4 , 2 , 1, 3], 'r')
plt.plot(angles, [3, 6 , 4 , 5, 3], 'b')
plt.fill(angles, [3, 6 , 4 , 5, 3], 'b', alpha=0.2)
plt.fill(angles, [3, 4 , 2 , 1, 3], 'r', alpha=0.2)


# In[54]:


## Cartogram
get_ipython().system('pip install geopandas')
import geopandas
import geoplot

path = geopandas.datasets.get_path('naturalearth_lowers')
df = feopandas.read_file(path)
df['gdp_pp'] =df['gdp_nd_eat'] / df['pop_eat']

df.head()


# In[ ]:


geoplot.choropleth(df, hue='gdp_pp')

