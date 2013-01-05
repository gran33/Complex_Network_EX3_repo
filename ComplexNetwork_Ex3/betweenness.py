from __future__ import division
'''

Created on Jan 5, 2013

@author: RAN
'''
from copy import deepcopy
"""A basic module for measuring betweenness in the graph."""

from graph import Graph
from Queue import Queue

class Betweenness():
    """
Computes the betweenness centrality of all vertices. 
Implements Brandes' algortithm 

@article{brandes2001faster,
  title={A faster algorithm for betweenness centrality},
  author={Brandes, U.},
  journal={Journal of Mathematical Sociology},
  volume={25},
  number={2},
  pages={163--177},
  year={2001},
  publisher={Taylor \& Francis},
  URL={http://www.inf.uni-konstanz.de/algo/publications/b-fabc-01.pdf}
}
@article{bc-variants,
    author={U. Brandes},
    title={On variants of shortest-path betweenness centrality and their generic computation},
    journal={Social Networks},
    volume={30},
    number={2},
    pages={136-145},
    year={2008},
    URL={http://www.inf.uni-konstanz.de/algo/publications/b-vspbc-08.pdf}
}

    """

    def __init__(self, G):
        self._G = G
        self._BC = {}
        
        for s in self._G.getVertices():
            self._BC[s] = 0

        

    def getBetweenness(self, v):
        """Returns the BC of v in G
           @precondition: method run() was executed. 
        """
        #you can add code here if you want
        if v not in self._BC:
            raise NameError("There is no vertex like that")
        else:
            return self._BC[v]

    

    def run(self):
        for s in self._G.getVertices():
            stack = []
            Pred = {}
            sigma = {}
            d = {}
            Q = Queue()
            Q.put(s)
            delta = {}
            for init_s in self._G.getVertices():
                Pred[init_s] = []
                delta[init_s] = 0
                sigma[init_s] = 0
                d[init_s] = -1
            
            sigma[s] = 1
            d[s] = 0
                    
            while not (Q.empty()):
                v = Q.get()
                stack.append(v)
                for w in self._G.getNeighbors(v):
                    if d[w] < 0:
                        Q.put(w)
                        d[w] = d[v] + 1
                    if d[w] == d[v] + 1 :
                        sigma[w] += sigma[v]
                        Pred[w].append(v)
            self.accumulation(delta, stack, Pred, sigma, s)
        
    
    def accumulation(self, delta, stack, Pred, sigma, s):
        for u in delta.items():
            delta[u] = 0
                        
        while stack.__len__() > 0:
            w = stack.pop()
            for v in Pred[w]:
                delta[v] += (((sigma[v])/(sigma[w])) * (1 + delta[w]))
                if w != s:
                    self._BC[w] += delta[w]
        
        
        

class GroupBetweenness(Betweenness):
    #you can modify class declaration (e.g. extend Betweenness)
    """
Computes the group betweenness centrality of all vertices. 

@article{bc-variants,
    author={U. Brandes},
    title={On variants of shortest-path betweenness centrality and their generic computation},
    journal={Social Networks},
    volume={30},
    number={2},
    pages={136-145},
    year={2008},
    URL={http://www.inf.uni-konstanz.de/algo/publications/b-vspbc-08.pdf}
}

@article{dana-anonimity,
author={R. Puzis and D. Yagil and Y. Elovici and D. Braha},
title={Collaborative Attack on Internet Users' Anonymity},
journal={Internet Research},
volume={19},
number={1},
pages={60--77}
year={2009},
URL={http://necsi.edu/affiliates/braha/Internet_Research_Anonimity.pdf}
}
    """

    def __init__(self, G):
        Betweenness.__init__(self, G)
        self._M = []
        self._GBC = 0
        #you can add code here if you want


    def getGroupBetweenness(self):
        """Returns the GBC of M in G
           @precondition: method run() was executed. 
        """
        #you can add code here if you want
        vertx = self._G.getVertices()
        for v in self._M:
            if v not in vertx:
                raise NameError("One of the vertices isn't in your supplied Gragh")
        return self._GBC

    def run(self, M):
        self._GBC = 0
        self._M = M
        Betweenness.run(self)
        
    def accumulation(self, delta, stack, Pred, sigma, s):
        for u in delta.items():
            delta[u] = 0
        while stack.__len__() > 0:
            w = stack.pop()
            for v in Pred[w]:
                if w in self._M:
                    i = 0
                else:
                    i = delta[w]
                delta[v] += ((sigma[v]/sigma[w]) * (1 + i))
            M_tmp = deepcopy(self._M)
            if s in M_tmp:
                M_tmp.remove(s)
            if w in M_tmp:
                self._GBC += delta[w]
                         
        

class EdgeBetweenness(Betweenness):
    #you can modify class declaration (e.g. extend Betweenness)
    """
Computes the group betweenness centrality of all vertices. 

@article{bc-variants,
    author={U. Brandes},
    title={On variants of shortest-path betweenness centrality and their generic computation},
    journal={Social Networks},
    volume={30},
    number={2},
    pages={136-145},
    year={2008},
    URL={http://www.inf.uni-konstanz.de/algo/publications/b-vspbc-08.pdf}
}

    """

    def __init__(self, G):
        Betweenness.__init__(self, G)
        self._BC_Edges = {}
        
        for e in self._G.getEdges():
            self._BC_Edges[e] = 0
       
    def getBetweenness(self,u,v):
        """Returns the GBC of M in G
           @precondition: method run() was executed. 
        """
        if not self._G.isEdge(u,v):
            raise NameError("There is no edge like that")
        #you can add code here if you want
        return self._BC_Edges[(u,v)]

    def run(self):
        Betweenness.run(self)
        
            
    def accumulation(self, delta, stack, Pred, sigma, s):
        for u in delta.items():
                delta[u] = 0
                        
        while stack.__len__() > 0:
            w = stack.pop()
            for v in Pred[w]:
                c = (sigma[v]/sigma[w])*(1+delta[w])
                
                self._BC_Edges[(v,w)] += c
                delta[v] += c
            if w != s:
                self._BC[w] += delta[w]





