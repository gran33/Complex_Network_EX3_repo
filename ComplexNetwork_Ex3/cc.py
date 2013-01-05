from __future__ import division
'''
Created on Jan 5, 2013

@author: RAN
'''
import math
"""A basic module for measuring clustering coefficient in the graph."""

from graph import Graph

class UndirectedClusteringCoefficient():

    def __init__(self, G):
        self._Gr = G

    def clusteringCoefficient(self):
        """
        Computes clustering coefficient of the graph.
        Two vertices are connected w.r.t. undirected clustering coefficient if an edge exists between them in either direction
        """
        triangelsInTheGraph = 0
        
        for v in self._Gr.getVertices():
            v_neighbors = self._Gr.getNeighbors(v)
            for u1 in v_neighbors:
                for u2 in v_neighbors:
                    if (u1 != u2) and (u1 != v) and (u2 != v) and (self._Gr.isEdge(u1,u2) or self._Gr.isEdge(u2,u1)):
                        triangelsInTheGraph += 1
        return (triangelsInTheGraph/6)/self.NchooseK(len(self._Gr.getVertices()), 3)

    def localClusteringCoefficient(self, v):
        """
        Computes the local clustering coefficient of the vertex v.
        Two vertices are connected w.r.t. undirected clustering coefficient if an edge exists between them in either direction
        """
        if v not in self._Gr.getVertices():
            return 'ERROR: there is not vertex like ', v, ' in the graph!'
        ConnectedNeighorsTupels = []
        v_neighbors = self._Gr.getNeighbors(v)
        v_neighbors_length = len(v_neighbors)
        if v_neighbors_length <= 1:
            return 0
        for u1 in v_neighbors:
            for u2 in v_neighbors:
                tup = (u1,u2)
                tup2 = (u2,u1)
                if (u1 != u2) and (u1 != v) and (u2 != v) and \
                    (tup not in ConnectedNeighorsTupels) and \
                    (tup2 not in ConnectedNeighorsTupels) and\
                    (self._Gr.isEdge(u1,u2) or self._Gr.isEdge(u2,u1)):
                    
                    ConnectedNeighorsTupels.append(tup)
        return (len(ConnectedNeighorsTupels))/(v_neighbors_length*(v_neighbors_length-1))
            
    
    def NchooseK(self,n,k):
        return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
