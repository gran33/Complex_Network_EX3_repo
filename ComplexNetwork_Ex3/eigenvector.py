'''
Created on Jan 5, 2013

@author: RAN
'''
"""A basic module for measuring the eigenvector centrality."""

from graph import Graph

class EigenvectorCentrality():

    def __init__(self, G):
        self._Gr = G
        pass

    def eigenvectorCentrality(self, v):
        """
        Computes the Eigenvector Centrality of the vertex v.
        """
        raise NotImplementedError("Replace implementation of this method.")

