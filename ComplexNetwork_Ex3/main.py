'''
Created on Jan 5, 2013

@author: RAN
'''
#!/usr/bin/env python
from __future__ import division
import sys
import random
#from graphParser import *
from graph import *
from degree import Degree
from sssp import SSSP
from dist import Dist
from cc import UndirectedClusteringCoefficient
from closeness import Closeness
from graphParser import GraphParser
from betweenness import *




def main():
    #parser = GraphParser()        
    #g = parser.loadGraphFromFile('football.net','TYPE_PAJEK')
#    g = Graph()
#    g.addEdge('1', '2', 1)
#    g.addEdge('2', '3', 1)
#    g.addEdge('3', '4', 1)
#    g.addEdge('4', '5', 1)
#    g.addEdge('5', '6', 1)
#    g.addEdge('6', '1', 1)
#    g.addEdge('1', '4', 1)
##    g.addEdge('e', 'c', 1)
##    g.addEdge('a', 'd', 1)
##    g.addEdge('a', 'b', 1)
##    g.addEdge('a', 'e', 1)
##    g.addEdge('b', 'e', 1)
#    
#    bwns = Betweenness(g)
#
#"""addVertex, addEdge, getNumberOfVertices, getNumberOfEdges"""
    g=Graph()
    NumberOfVertices = g.getNumberOfVertices()    
    print "number of vertices: %d \n" % NumberOfVertices
    print "number of links: %d \n" % g.getNumberOfEdges()    
    g.addVertex(2)
    g.addVertex(1)
    g.addVertex(4)
    g.addVertex(3)
    # g.addVertex(5)
    g.addEdge(1,2)
    g.addEdge(2,1)
    g.addEdge(1,3)
    g.addEdge(3,1)
    g.addEdge(2,3)
    g.addEdge(3,2)
    g.addEdge(3,4)
    g.addEdge(4,3)    
    #Betweeness
    g.addVertex(5)
    g.addEdge(2,5)
    g.addEdge(5,2)
    g.addEdge(3,5)
    g.addEdge(5,3)    
    b = Betweenness(g)
    b.run()
    print "Betweenness \n"    
    print "b.getBetweenness(1) expected 0\n"
    print (b.getBetweenness(1))
    print "b.getBetweenness(2) expected 1\n"
    print (b.getBetweenness(2))
    print "b.getBetweenness(3) expected 7\n"
    print (b.getBetweenness(3))
    print "b.getBetweenness(4) expected 0\n"
    print (b.getBetweenness(4))
    print "b.getBetweenness(5) expected 0\n"
    print (b.getBetweenness(5))
    
    #EdgeBetweeness
    eb = EdgeBetweenness(g)
    eb.run()
    print "Edge Betweenness \n"    
    print "eb.getBetweenness(3,4) expected 4\n"
    print (eb.getBetweenness(3,4))
    print "eb.getBetweenness(4,3) expected 4\n"
    print (eb.getBetweenness(4,3))

    print "eb.getBetweenness(5,3) expected 2.5\n"
    print (eb.getBetweenness(5,3))
    print "eb.getBetweenness(3,5) expected 2.5\n"
    print (eb.getBetweenness(3,5))

    print "eb.getBetweenness(5,2) expected 1.5\n"
    print (eb.getBetweenness(5,2))
    print "eb.getBetweenness(2,5) expected 1.5\n"
    print (eb.getBetweenness(2,5))

    print "eb.getBetweenness(2,3) expected 2\n"
    print (eb.getBetweenness(2,3))
    print "eb.getBetweenness(3,2) expected 2\n"
    print (eb.getBetweenness(3,2))

    print "eb.getBetweenness(1,3) expected 2.5\n"
    print (eb.getBetweenness(1,3))
    print "eb.getBetweenness(3,1) expected 2.5\n"
    print (eb.getBetweenness(3,1))

    print "eb.getBetweenness(1,2) expected 1.5\n"
    print (eb.getBetweenness(1,2))
    print "eb.getBetweenness(2,1) expected 1.5\n"   
    print (eb.getBetweenness(2,1))

    #GroupBetweeness
    gb = GroupBetweenness(g)
    M = set()
    M.add(3)
    gb.run(M)
    print "Group Betweenness \n"
    print "M=[3] expected: "
    print (b.getBetweenness(3))
    print (gb.getGroupBetweenness())
    print "M=[2,3] expected 8: "
    M.add(2)
    gb.run(M);
    print (gb.getGroupBetweenness())
    print "M=[1,5] expected 0: "
    M=set()
    M.add(1)
    M.add(5)
    gb.run(M);    
    print (gb.getGroupBetweenness())
    print "M=[1,5,4] expected 0: "    
    M.add(4)
    gb.run(M);    
    print (gb.getGroupBetweenness())
    print "M=[1,5,3] expected "
    print (b.getBetweenness(3))    
    M.add(3)
    gb.run(M);    
    print (gb.getGroupBetweenness())
   
   # print bwns.getBetweenness('a')
    
    
#    dist = Dist(g)
#    close = Closeness(g)
#    deg = Degree(g)
#    group = ['93']
#    sssp = SSSP(g)
#    print g.getNeighbors('v1')
#    print sssp.getDistances()
#    print 'deg.outDegreeDistribution()=' ,deg.outDegreeDistribution()
#    print 'deg.inDegreeDistribution()=',deg.inDegreeDistribution()
#    print 'deg.degreeDistribution()=',deg.degreeDistribution()
#    print 'deg.groupDegree([1,2,3])=',deg.groupDegree([1,2,3])
#    print 'deg.degree(9)=',deg.degree('v1')
#    print close.closeness('v1')
#    print 'close.closeness=', close.closeness('v1')
#    print 'close.groupCloseness(group)=',close.groupCloseness(group)
#    print 'close.closenessDistribution()=',close.closenessDistribution()
#    print 'dist.characteristicPathLength()=' , dist.characteristicPathLength()
#    print 'dist.localHopPlot(v)=' , dist.localHopPlot('v1')
#    print 'dist.hopPlot()=' , dist.hopPlot()
#    print 'dist.diameter()' , dist.diameter()    

if __name__ == "__main__":
    main()