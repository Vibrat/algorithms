#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Graph Data Inplimentation
"""

import abc
import numpy as np


# In[4]:


########################################
#
# Base Class Implementation for Graph
#
########################################


class Graph(abc.ABC):
    
    def __init__(self, numVertices, directed = False):
        self.numVertices = numVertices
        self.directed = directed
    
    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass
    
    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass
    
    @abc.abstractmethod
    def get_indegree(self, v):
        pass
    
    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass
    
    @abc.abstractmethod
    def display(self):
        pass 


# In[23]:


########################################
#
# AdjacencyMatrixGraph
#
########################################

class AdjacencyMatrixGraph(Graph):
    
    def __init__(self, numVertices, directed = False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)
        
        self.matrix = np.zeros((numVertices, numVertices))
    
    def add_edge(self, v1, v2, weight = 1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))
        
        if weight < 1:
            raise ValueError("An edge cannot have weigth < 1")
            
        self.matrix[v1][v2] = weight
        
        if self.directed:
            self.matrix[v2][v1] = weight
            
    def get_adjacent_vertices(self, v):
        
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot acces vertex %d" % v)
        
        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i]:
                adjacent_vertices.append(i)
        
        return adjacent_vertices
    
    def get_indegree(self, v):
        
        if v >= self.numVertices or v < 0: 
            raise ValueError("Cannot access  vertex %d " % v)
        
        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                indegree = indegree + 1
        
        return indegree
    
    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]
    
    def display(self):
        for i1 in range(self.numVertices):
            for i2 in self.get_adjacent_vertices(i1):
                print ("Vertex %d => %d" % (i1, i2))
        


# In[24]:


graph_sample = AdjacencyMatrixGraph(4)
graph_sample.add_edge(1, 2)
graph_sample.add_edge(2, 3)
graph_sample.add_edge(2, 1)

graph_sample.display()


# In[ ]:





# In[ ]:




