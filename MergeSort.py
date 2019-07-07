#!/usr/bin/env python
# coding: utf-8

# In[94]:


import math
data = [ 1 , 3, 2, 6 , 11, 11, 2300, 42  ]


# In[95]:


def merge_sort(data):
    ## print (len(data))
    if len(data) < 2:
        return data
    else: 
        middle  = math.floor((len(data)) / 2)  
        left_data = data[0:middle]
        right_data = data[middle:]

        ## print (left_data)
        return merge(merge_sort(left_data), merge_sort(right_data))
    
def merge(array_left, array_right):
    result = []
    left_index, right_index = 0 , 0 
    
    while left_index < len(array_left) and right_index < len(array_right):
        if array_left[left_index] < array_right[right_index]:
            result.append(array_left[left_index])
            left_index += 1
        else:
            result.append(array_right[right_index])
            right_index += 1
    
    print ("Result", result)
    
    if array_left:
        print ("index", left_index, "array left", array_left)
        result.extend(array_left[left_index:])
        
    if array_right:
        print ("index", right_index, "array right",  array_right)
        result.extend(array_right[right_index:])
    
    print ("Result", result)
    
    return result
        


# In[96]:


result = merge_sort(data)
print (result)


# In[ ]:





# In[ ]:




