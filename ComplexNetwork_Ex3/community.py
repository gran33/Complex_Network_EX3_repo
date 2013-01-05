'''
Created on Jan 5, 2013

@author: RAN
'''
"""A basic module for detecting community structure in graphs."""

from graph import Graph

class GirvanNewman():
    """
Splits the graph into a set of communities. 

@article{girvan2002community,
  title={Community structure in social and biological networks},
  author={Girvan, M. and Newman, M.E.J.},
  journal={Proceedings of the National Academy of Sciences},
  volume={99},
  number={12},
  pages={7821--7826},
  year={2002},
  publisher={National Acad Sciences},
  URL={http://www.santafe.edu/media/workingpapers/01-12-077.pdf}
}

    """

    def __init__(self, G):
        self._G = G
        pass

    def getCommunities(self, k):
        """
        Returns a set of communities detected by removal of k edges with
        maximal betweenness centrality. 
        @Invariant: all([all([self._G.isVertex(v) for v in C]) for C in self.getCommunities()])


        """
        raise NotImplementedError("Replace implementation of this method.")


class LabelPropagation():
    """
Splits the graph into a set of communities. 

@article{raghavan2007near,
  title={Near linear time algorithm to detect community structures in large-scale networks},
  author={Raghavan, U.N. and Albert, R. and Kumara, S.},
  journal={Physical Review E},
  volume={76},
  number={3},
  pages={036106},
  year={2007},
  publisher={APS},
  URL={http://arxiv.org/abs/0709.2938}
}
    """

    def __init__(self, G):
        self._G = G
        pass

    def getCommunities(self):
        """
        Returns a collection of sets.
        @Invariant: all([all([self._G.isVertex(v) for v in C]) for C in self.getCommunities()])
        """
        raise NotImplementedError("Replace implementation of this method.")



