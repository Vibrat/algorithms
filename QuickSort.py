#!/usr/bin/env python
# coding: utf-8

# In[61]:


import math

data = [1, 8, 4, 2, 6, 7, 3, 4, 5]


# In[62]:


def quick_sort(data):
    """
    Quick Sort Implementation

    - Time Complexity O(Nlog(N)) on average, and O(N2) for worst case
    - Space Complexity (Log(N))
    """

    length = len(data)
    return quick_sort_processing(data, 0, length -1)
    
def quick_sort_processing(data, left, right):
    index = patrition(data, left, right)
    
    if left < index - 1:
        quick_sort_processing(data, 0, index)
        
    if right > index:
        quick_sort_processing(data, index, right)
    
    return data
        

def patrition(data, left, right):
    middle = math.ceil((left + right)/2)
    
    while data[left] <= data[middle]:
        if left == middle:
            break
        else: 
            left += 1
    
    while data[right] >= data[middle]:
        if right == middle:
            break
        else:
            right -= 1
    
    if left < right:
        temp = data[left]
        data[left]  = data[right]
        data[right] = temp
    
    return left


# In[63]:


print (data)
output = quick_sort(data)
print (output)


# In[ ]:




