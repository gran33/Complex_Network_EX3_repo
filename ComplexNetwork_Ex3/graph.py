'''
Created on Jan 5, 2013

@author: RAN
'''
"""A proxy to networkx.

Current version delegates to networkx.XGraph with integer nodes (vertices).
An internal dictionary is maintained to support vertex weights.
Edge weights are supported by networkx.XGraph.

You should write an implementation of your own, independant from networkx."""

import copy #"Generic (shallow and deep) copying operations" package.
import re


            

class Graph():
    """An implementation of a Graph ADT. While this implementation
    delegates everything to networkx, you should write your own
    implementations."""
    
    def __init__(self,copyFrom = None):
        """
        Creates and empty graph object.
        """
        self._Gr = {}
        self._vertexWeights = {}


#        if isinstance(copyFrom,Graph):
#            self._vertexWeights = copyFrom._vertexWeights
#            self._Gr = copyFrom._Gr

        if isinstance(copyFrom,Graph):
            for v in copyFrom._Gr:
                self.addVertex(v, copyFrom._vertexWeights[v])
                for v2 in copyFrom._Gr[v]:
                    self.addEdge(v, v2[0], v2[1])                 
            

    def addVertex(self,index,weight = None):
        """
        Adds a new vertex to the graph.
        If the vertex already exists in the graph then the vertex is ignored. Implementations may replace vertex weight in this case with a new weight.
        If the optional weight argument is given then it is associated with the vertex and can be retrieved with getVertexWeight.
        """
        if weight is None:
            weight = 0
            
        if index not in self._Gr:
            self._Gr[index] = []
    
        self._vertexWeights[index] = weight


    def addEdge(self,v1,v2,weight = None):
        """
        Adds a new directed edge to the graph.
        If the edge already exists in the graph then no edge is added. Implementations may replace edge weight with a new weight.
        If the optional weight argument is given then it is associated with the edge and can be retrieved with getEdgeWeight.
        """
        if weight is None:        
            weight = 0

        #if self.isEdge(v1, v2) is None:
        self.addVertex(v1)
        self.addVertex(v2)         
        self._Gr[v1].append((v2,weight))
            

    def deleteEdge(self,e):
        assert isinstance(e,tuple)
        neighbors = self._Gr[e[0]]
        for i in range(0,neighbors.__len__()):
            if(neighbors[i][0] == e[1]):
                del neighbors[i]
                break
            
        
       
        #self._Gr[e[0]].remove(e[1], self.getEdgeWeight(e[0],e[1]))

    def getNumberOfVertices(self):
        """
        Returns the number of vertices
        """
        return len(self._Gr.keys())

    def getNumberOfEdges(self):
        """
        Returns the number of _edges
        """
        res = 0
        for k in self._Gr.keys():
            res+=len(self._Gr[k])
        return res

    def getVertexWeight(self,index):
        """
        Returns the weight object previousely associated with the vertex or None if no weight was provided.
        """
        return self._vertexWeights[index]

    def getVertices(self):
        """
        Returns an iterable object representing the collection of vertices.
        The order of vertices may be arbitrary.
        Invariant: all([g.isVertex(v) for v in g.getVertices()])
        """
        return self._Gr.keys()

    def isEdge(self,v1,v2):
        """
        Returns true if v1 is connected to v2.
        isEdge(v1,v2) might not be equal to isEdge(v2,v1)
        """
        if  v1 in self.getVertices():
            for target in self._Gr[v1]:
                if target[0] == v2:
                    return target
        else:
            return None
        

    def getEdge(self,v1,v2):
        return self.isEdge(v1, v2)
        
        
    
    def getEdges(self):
        """
        **CHANGED**
        Returns an iterable object representing the collection of directed tuples where first element of
        each entry is source vertex of an edge and the second element is the target vertex.
        Invariant: all([g.isEdge(*e[:2]) for e in g.getEdges()])
        """
        res = []
        for source in self.getVertices():
            for target in self._Gr[source]:
                res.append((source, target[0]))
        return res

    def getNeighbors(self, v):
        """
        This methos is calculate the neightbours which are the vertex that a access from v and 
        the  vertex which v is access from them
        """
        if v not in self.getVertices():
            return None
        res = self.getVertexOutNeightbours(v)
        res.extend(self.getVertexInNeightbours(v))
        return set(res)
    
    def isVertex(self, v):
        """
        Returns true if v is a vertex in the graph and false otherwise.
        Invariant: all([g.isVertex(v) for v in g.getVertices()])
        """
        return v in self.getVertices()

    def getEdgeWeight(self,v1,v2):
        """
        Returns the weight object previousely associated with the edge or None if no weight was provided.
        """
        resEdge = self.isEdge(v1, v2)
        if resEdge is None:
            return None
        else:       
            return resEdge[1]
    
    def getVertexInNeightbours(self, v):
        res = []
    
        if v not in self.getVertices():
            return None
        
        for source in self.getVertices():
            if (source not in res) and (self.isEdge(source, v) != None):
                res.append(source)
        return res
        
    def getVertexOutNeightbours(self, v):
        if v not in self.getVertices():
            return None
        res = []
        for target in self._Gr[v]:
            if target not in res:
                res.append(target[0])
        return res
    
    def getMaxDegree(self):
        res = 0
        for v in self.getVertices():
            res = max(res,len(self.getNeighbors(v)))
        
        return res
    

            
    
            
            
            
            
            