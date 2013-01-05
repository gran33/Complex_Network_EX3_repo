'''
Created on Jan 5, 2013

@author: RAN
'''
"""A basic module for measuring betweenness in the graph."""

from graph import Graph

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
        #you can add code here if you want
        pass

    def getBetweenness(self, v):
        """Returns the BC of v in G
           @precondition: method run() was executed. 
        """
        #you can add code here if you want
        return self._BC[v]

    def run(self):
        raise NotImplementedError("Replace implementation of this method.")


class GroupBetweenness():
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
        self._G = G
        self._GBC = 0
        #you can add code here if you want
        pass

    def getGroupBetweenness(self):
        """Returns the GBC of M in G
           @precondition: method run() was executed. 
        """
        #you can add code here if you want
        return self._GBC

    def run(self, M):
        raise NotImplementedError("Replace implementation of this method.")

class EdgeBetweenness():
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
        self._G = G
        self._BC = {}
        #you can add code here if you want
        pass

    def getBetweenness(self,u,v):
        """Returns the GBC of M in G
           @precondition: method run() was executed. 
        """
        #you can add code here if you want
        return self._BC[u,v]

    def run(self):
        raise NotImplementedError("Replace implementation of this method.")


