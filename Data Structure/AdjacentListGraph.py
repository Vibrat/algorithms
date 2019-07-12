#!/usr/bin/env python
# coding: utf-8

# In[29]:


"""
Implementation of Adjacent List Graph
"""
import abc
import numpy as np


# In[34]:


"""
Basic Abstract Graph Class
"""

class Graph(abc.ABC):
    
    @abc.abstractmethod
    def __init__(self, numVertices, directed  = False):
        self.numVertices = numVertices
        self.directed = False
    
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
    def display(self):
        pass


# In[38]:


"""
Node represent an linked list
"""
class Node:
    
    @abc.abstractmethod
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacent_set = set()
        
        
    @abc.abstractmethod    
    def add_edge(self, v, weight = 1):
        if v == self.vertexId:
            raise ValueError("Cannot add edge to itself on vertex %d" % v)
        
        self.adjacent_set.add(v)
       
    @abc.abstractmethod
    def get_adjacent_vertices(self):
        return sorted(self.adjacent_set)
    
    @abc.abstractmethod
    def display(self):
        print ("%d => %s" % (self.vertexId, self.adjacent_set))
        


# In[39]:


class AdjacentSetGraph(Graph):
    
    def __init__(self, numVertices, directed = False):      
        super(AdjacentSetGraph, self).__init__(numVertices, directed)
        
        self.dict_nodes = {}
        for i in range(numVertices):
            self.dict_nodes[i] = Node(i)
        
    
    def add_edge(self, v1, v2 , weight = 1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Cannot add edge  vertex %d and vertex %d" % (v1, v2))
        
        if weight < 1:
            raise ValueError("Weight should not be less than 1")
        
        self.dict_nodes[v1].add_edge(v2)
        
        if self.directed:
            self.dict_nodes[v2].add_edge(v1)
    
    
    def get_adjacent_vertices(self, v):
        return self.dict_nodes[v].get_adjacent_vertices
    
    
    
    def get_indegree(self, v):
        
        if v >= self.numVertices or v < 0:
            raise ValueError("Cannot acces vertex %d " % v )
        
        indegree = 0
        for i in self.dict_nodes:
            if v in self.dict_nodes[i].get_adjacent_vertices:
                indegree = indegree + 1
        
        return indegree
            
        
    def display(self):
        for i in self.dict_nodes:
            self.dict_nodes[i].display()


# In[40]:


sample_graph = AdjacentSetGraph(4)
sample_graph.add_edge(1, 2)
sample_graph.add_edge(2, 3)
sample_graph.add_edge(1, 3)
sample_graph.display()


# In[ ]:




