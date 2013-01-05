'''
Created on Jan 5, 2013

@author: RAN
'''
from pickle import NONE
"""A parser class for graph files of different types.

You should expand the parser by adding more types to the GraphParser
class, writing handlers for these types, and adding these types-to-handlers
mapping in the parsers dictionary defined in the class' __init__ constructor.

The example code executed when running this module uses the supplied
as4.net file, in Pajek format. Your code should behave similarly."""

"""import networkx as nx"""
import re
from graph import *
from sssp import *

class GraphParser():

    TYPE_PAJEK = "TYPE_PAJEK"
    
    def pajekHandler(self,filename):
        graph = Graph()
        f = open(filename)
        lines = f.readlines()
        f.close()
        
        i = 0
        st = lines[i]
        stop = len(lines)
        
        while i < stop:
            st = lines[i]
            
            if('*Vertices' in st):
                i+=1   
                while ('*Arcs' not in st and i < stop):
                    st = lines[i]
                    graph.addVertex(st.split()[0])
                    i+=1
                    if i < stop:
                        st = lines[i]
                   
            if('*Arcs' in st or '*Edges' in st):
                i+=1
                while (i < stop):
                    st = lines[i]
                    toAdd = st.split()
                    if('*Edges' in toAdd):
                        i+=1
                        continue
                    
                    toAddLen = len(toAdd)
                    if toAddLen >= 2:
                        graph.addEdge(toAdd[0], toAdd[1], None)

                    i+=1
                    if i < stop:
                        st = lines[i]
            i+=1
            
        return graph
    
    def __init__(self):
        self.parsers = {
            GraphParser.TYPE_PAJEK : self.pajekHandler
        }

    def loadGraphFromFile(self,filename,type):
        parser = self.parsers.get(type,None)

        if parser is None:
            print 'ERRORRRRRRRRRRRRR'
            raise ValueError("Unknown type.")
        else:
            return parser(filename)

#if __name__ == "__main__":
#    graphParser = GraphParser()
#    g = graphParser.loadGraphFromFile('as4.net',GraphParser.TYPE_PAJEK)
#    #print g.getNumberOfVertices()
#    bfs = SSSP(g)
#    
#    bfs.run('11')
    #240526  169170 100315
    
    #    for e in g.getEdges():
#        assert(e,Edge)
#        print e.toString() 
    #print g.getVertexWeight('137') 
    #print [x for x in g.getVertices()]
    #print g.getNumberOfEdges()
    #print g.getVertices() is set
