from __future__ import division
'''
Created on Jan 5, 2013

@author: RAN
'''
from test.test_threading_local import target
"""A basic module for measuring distances in the graph."""

from graph import Graph
from sssp import SSSP
from closeness import Closeness


class Dist():

    def __init__(self, G):
        self._Gr = G
        self._closness = Closeness(G)
        
        
        pass

    def diameter(self):
        """
        Computes the diameter of a connected graph.
        """
        res = 0
        for v in self._closness._coupleDistances.keys():
            for (target, length) in self._closness._coupleDistances[v].iteritems():
                res = max(res, length)
        return res
                
            
    def characteristicPathLength(self):
        """
        Computes the average distance between two vertices in a connected graph.
        """
        sumOfAllDistances = 0
        allPairs = 0
        for v in self._closness._coupleDistances.keys():
            for (target, length) in self._closness._coupleDistances[v].iteritems():
                if target != v:
                    allPairs += 1
                    if length > 0:
                        sumOfAllDistances += int(length)
        return sumOfAllDistances/allPairs

    def localHopPlot(self, v):
        """
        Returns a list representing the vertex hop plot.
        CHANGED: hopPlot(v)[x] is the number of vertices at distance x from v.
        hopPlot(v)[x] is the number of vertices at distance at most x from v.
        """
        if v not in self._Gr.getVertices():
            return None
        
        v_distances = self._closness._coupleDistances[v]
        res = [0]*len(v_distances.keys())
        
        for (target, length) in v_distances.iteritems():
            if length >= 0:
                for i in range(length, len(res)):
                    res[i] += 1
                    
        return res                
                        

    def hopPlot(self):
        """
        Returns a list representing the graph.
        averageHopPlot()[x] is the number of pairs of vertices at distance x from each other.
        CAHNGED:
        averageHopPlot()[x] is the number of pairs of vertices at distance at most x from each other.
        """
        res = [0]*(self._closness.getMaxLength()+2)
        for v in self._closness._coupleDistances.keys():
            for (target, length) in self._closness._coupleDistances[v].iteritems():
                if length >= 0:
                    for i in range(length, len(res)):
                        res[i] += 1
                
        return res
