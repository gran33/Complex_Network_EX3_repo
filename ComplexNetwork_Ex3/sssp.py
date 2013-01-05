'''
Created on Jan 5, 2013

@author: RAN
'''
"""SSSP - Single-Source Shortest Path algorithm implementation.

This module contains class SSSP, which is initialized with a given Graph
instance G. Upon initialization, a dictionary of distances is also initialized.
When the run(s) method is invoked with a certain source vertex, your
implementation should calculate the distances from s to every other vertex.

The implementation should also support the following queries:
getNumberOfDiscovered - how many vertices were discovered?
getNumberOfRediscovered - how many vertices were re-discovered during search?
getNumberOfExpanded - how many vertices were expanded during search?
resetCounters - zeroes the dicovered, rediscovered, and expanded counters.

We strongly recommed you would use implement BFS as your SSSP algorithm.
The supplied implementation is partial and relies on networkx."""

from Queue import Queue
from graph import Graph

class SSSP():
    def __init__(self, G):
        self._Gr = G
        self._distances = {}
        self._pi = {}

        self._discovered = 0
        self._reDiscovered = 0
        self._expended = 0
        
        #self._vertexColors = {}
        #self._queue = Queue(len(self._Gr.getVertices()))
        #for v in self._Gr.getVertices():
        #    self._vertexColors[v] = 'white'

    def bfs(self, s):
        queue = Queue(len(self._Gr.getVertices()))
        vertexColors = {}
        for v in self._Gr.getVertices():
            vertexColors[v] = 'white'
            self._distances[v] = -1
            self._pi[v] = None
        vertexColors[s] = 'gray'
        self._distances[s] = 0
        queue.put_nowait(s)
        while not queue.empty():
            u = queue.get_nowait()
            self._expended+=1
            for v in self._Gr.getVertexOutNeightbours(u):
                if vertexColors[v] == 'white':
                    self._discovered+=1
                    vertexColors[v] = 'gray'
                    self._distances[v] = self._distances[u] + 1
                    self._pi[v] = u
                    queue.put_nowait(v)      
                else:
                    self._reDiscovered+=1                
                vertexColors[u] = 'black'

    def run(self, s):
        """
        Executes the algorithm.
        """
        if s not in self._Gr.getVertices():
            return None
        self.bfs(s)
                    
    def getDistances(self):
        """
        Returns a collection of distances from s indexed by vertex.
        mySSSP.getDistances()[v]==mySSSP.getDistance(v) is the distance of v from s.
        """
        return self._distances

    def getDistance(self, v):
        """
        Returns the distance of v from s.
        mySSSP.getDistances()[v]==mySSSP.getDistance(v) is the distance of v from s.
        """
        if v not in self._Gr.getVertices():
            return -1
            
        return self._distances[v]

    def getNumberOfDiscovered(self):
        """
        Returns the number of vertices discovered during run(...)
        """
        return self._discovered               

    def getNumberOfRediscovered(self):
        """
        Returns the number of vertices discovered during run(...)
        """
        return self._reDiscovered

    def getNumberOfExpanded(self):
        """
        Returns the number of vertices rediscovered during run(...)
        """
        return self._expended

    def resetCounters(self):
        self._discovered = 0
        self._expended = 0
        self._reDiscovered = 0
    

