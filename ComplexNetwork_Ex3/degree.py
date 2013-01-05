'''
Created on Jan 5, 2013

@author: RAN
'''
"""A basic module for measuring degrees in the graph."""

from graph import Graph

class Degree():

    def __init__(self, G):
        self._Gr = G

    def degree(self, v):
        """
        In graph G, return the degree of a certain vertex v.
        """
        if v not in self._Gr.getVertices():
            return None
        
        return len(self._Gr.getNeighbors(v))

    def groupDegree(self, group):
        """
        In graph G, return the group degree of a certain set of vertices group.
        """
        groupNeighbor = []
        for v in group:
            if v not in self._Gr.getVertices():
                continue
            for v_neibour in  self._Gr.getNeighbors(v):
                if v_neibour not in group:
                    groupNeighbor.append(v_neibour)
                
        return len(set(groupNeighbor))


    def degreeDistribution(self):
        """
        Return a list representing the degree distribution.
        degreeDistribution()[k] is the number of vertices having k neighbors or more.
        """
        return self.degreeCalculatorHelper('degree')

    def inDegreeDistribution(self):
        """
        Return a list representing the in-degree distribution.
        inDegreeDistribution()[k] is the number of vertices having in-degree at least k.
        """
        return self.degreeCalculatorHelper('in')

    def outDegreeDistribution(self):
        """
        Return a list representing the out-degree distribution.
        outDegreeDistribution()[k] is the number of vertices having out-degree at least k.
        """
        return self.degreeCalculatorHelper('out')
    
    def degreeCalculatorHelper(self, fun):
        res = [0]*(self._Gr.getMaxDegree()+2)
        for target in self._Gr.getVertices():
            if fun == 'in':
                v_degree = len(self._Gr.getVertexInNeightbours(target))
            elif fun == 'out':
                v_degree = len(self._Gr.getVertexOutNeightbours(target))
            elif fun == 'degree':
                v_degree = len(self._Gr.getNeighbors(target))
            else:
                break
            for i in range(0, v_degree+1):
                res[i]+=1
        return res
            
        
        
        
        
        
        
    
