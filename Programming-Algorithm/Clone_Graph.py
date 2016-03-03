# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 09:44:12 2015

@author: ZSHU
"""
 class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
 
 node0=UndirectedGraphNode(0)
 node1=UndirectedGraphNode(1)
 node2=UndirectedGraphNode(2)
 
 node0.neighbors=[node1,node2]
 node1.neighbors=[node2]
 node2.neighbors=[node2]
 
 class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        
         def clone(node, visited):
             if node in visited:
                 return visited[node]
             else:
                 cloned=UndirectedGraphNode(node.label)
                 visited[node]=cloned
                 for neighbor in node.neighbors:
                     cloned.neighbors+=[clone(neighbor, visited)]
                 return cloned
         
         if node==None: return None 
         else:
             visited={}
             return clone(node, visited)