#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mean


# In[25]:


data = pd.read_csv("http://www.dsi.uminho.pt/~pcortez/forestfires/forestfires.csv")
data.head()


# In[40]:


## Diferent ways to calculate mean
mean1 = data['temp'].mean()
mean2 = mean(data['temp'])
mean3 = np.mean(data['temp'])

print (f"{mean1}, {mean2}, {mean3}")


# In[55]:


## Diferent ways to compute mode
## !important: mode in statistics is taking Series as parameter
from statistics import mode
from scipy import stats

mode1 = data['temp'].mode()
mode2 = stats.mode(data['temp'])

print(f"MODE1\r\n{mode1}\r\n--------\r\nMODE2: {mode2}")


# In[60]:


## Calculate stdev - Standard Variation
## Document about Standard Variations: https://en.wikipedia.org/wiki/Standard_deviation

from statistics import stdev

stdev1 = data['temp'].std()
stdev2 = stdev(data['temp'])
stdev3 = np.std(data['temp'])

print(f"{stdev1}, {stdev2}, {stdev3}")


# In[64]:


## Calculate variation - 
## variance  = standard variation**2

from statistics import variance

variance1 = data['temp'].var()
variance2 = variance(data['temp'])
variance3 = np.var(data['temp'])

print (f"{variance1}, {variance2}, {variance3}")


# In[66]:


## Calculate skew

from scipy.stats import skew

skew1 = data['temp'].skew()
skew2 = skew(data['temp'])

print (f"{skew1}, {skew2}")


# In[67]:


## Kurtosis
from scipy.stats import kurtosis

kurtosis1 = data['temp'].kurt()
kurtosis2 = kurtosis(data['temp'])

print (f"{kurtosis1}, {kurtosis2}")


# In[68]:


## Display all
data.describe()


# In[89]:


## Draw chart
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)
sns.kdeplot(data['temp'], shade=True) # Add distribution
plt.axvline(data['temp'].mean(), 0, 1) # add x (vertical) line
plt.axvline(data['temp'].median(), 0, 1) # add x (vertical) line

## Display 25% and 75% vertical line
result = data['temp'].describe()
plt.axvline(result['25%'], 0, 1)
plt.axvline(result['75%'], 0, 1)


# In[90]:


result


# In[ ]:




