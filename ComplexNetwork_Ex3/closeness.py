from __future__ import division
'''
Created on Jan 5, 2013

@author: RAN
'''
"""A basic module for measuring closeness in the graph."""

from graph import Graph
from sssp import SSSP

class Closeness():

    def __init__(self, G):
        self._Gr = G
        self._coupleDistances = {}
        
        for v in self._Gr.getVertices():
            v_sssp = SSSP(self._Gr)
            v_sssp.run(v)
            self._coupleDistances[v] = v_sssp.getDistances()
#        theLongest = 0
#        for (source, length) in self._coupleDistances.iteritems():
#                if length > theLongest:
#                    theLongest =  length
        

    def closeness(self, v):
        """Computes the sum of reciprocal distances of v from every other vertex in the graph."""
        sum = 0
        if v not in self._Gr.getVertices():
            return None
        
        for (target, length) in self._coupleDistances[v].iteritems():
            if(length > 0):
                sum += 1/length
        if sum == 0:
            return 0
        return sum
        

    def groupCloseness(self, group):
        """Computes the sum of reciprocal distances of all non group members from the closest group member."""
        relevantGroup = []
        for v in group:
            if (v in self._Gr.getVertices()) and (v not in relevantGroup):
                relevantGroup.append(v)
        res = 0
        for v in self._Gr.getVertices():
            if v not in relevantGroup:
                closestDistanceFromGroup = 1000
                for (target, length) in self._coupleDistances[v].iteritems():
                    if(length > 0) and (target in relevantGroup):
                        closestDistanceFromGroup = min(closestDistanceFromGroup, length)
                if closestDistanceFromGroup < 1000:
                    res += closestDistanceFromGroup
        if res == 0:
            return 'inf'
        
                
        return 1/res
            
            
    def closenessDistribution(self):
        """
        Return a list representing the closeness distribution.
        closenessDistribution()[k] is the number of vertices having closeness larger or equal to k.
        """
        res = [0]*((int)(self.getMaxCloseness())+2)
        for v in self._coupleDistances:
            tmp_closeness = (int)(self.closeness(v))
            for i in range(0,tmp_closeness+1):
                res[i]+=1
        return res
    
    
    def getMaxCloseness(self):
        res = 0
        for v in self._coupleDistances.keys():
            res = max(res, self.closeness(v)) 
            
        return res
    
    def getMaxLength(self):
        res = 0
        for v in self._coupleDistances.keys():
            for (target, length) in self._coupleDistances[v].iteritems():
                res = max(res, length)
                
        return res
            
            
        
        
        
        
        
        
        
        
        
        

