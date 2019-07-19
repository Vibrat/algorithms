#!/usr/bin/env python
# coding: utf-8

# In[38]:


from numpy import zeros
from queue import Queue
get_ipython().run_line_magic('run', 'AdjacentListGraph.ipynb')

data = sample_graph


# In[45]:



def breadth_first(graph, start = 0):
    queue = Queue()
    queue.put(start)
    
    graph_matrix = zeros(graph.numVertices)
    
    while not queue.empty():
        vertex = queue.get()
        
        if graph_matrix[vertex] == 1:
            continue
            
        print ("visit %d" % (vertex))
        for item in graph.get_adjacent_vertices(vertex):
            if graph_matrix[item] != 1:
                queue.put(item)
        
    


# In[46]:


breadth_first(data, 2)



