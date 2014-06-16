#!/usr/bin/python

"""
Graph abstract data type implemented as an adjacency list.
Directed unweighted graph.
@author Madhav Murthy
"""

"""
Graph represents a mutable directed, unweighted graph object.
"""
class Graph(object):
    def __init__(self, edges=[]):
        self.nodes = {}
        for edge in edges:
            self.add(edge[0], edge[1])

    """
    param: a vertex x in the graph
    param: a vertex y in the graph
    returns: if x and y are adjacent
    """
    def adjacent(self, x, y):
        if(not(self.exists(x))):
            return False
        for node in self.nodes[x]:
            if(node == y):
                return True
        return False

    """
    param: a vertex x in the graph
    returns: list of all vertices y such that there is an edge from x to y
    """
    def neighbors(self, x):
        if(not(self.exists(x))):
            return set()
        return self.nodes[x]

    """
    param: a vertex x in the graph
    param: a vertex y in the graph
    effects: a new edge from x to y; if x or y are not in the graph a new vertex is created
    """
    def add(self, x, y):
        if(not(self.exists(x))):
            self.nodes[x] = set()
        self.nodes[x].add(y)

    """
    param: a vertex x in the graph
    param: a vertex y in the graph
    effects: deletes the edge from x to y
    """
    def delete(self, x, y):
        if(self.exists(x)):
            self.nodes[x].remove(y)
            if(len(self.nodes[x]) == 0):
                del self.nodes[x]

    """
    param: a vertex x in the graph
    returns: whether or not x is in the graph
    """
    def exists(self, x):
        for node in self.nodes.keys():
            if (node == x):
                return True
        return False

def main():
    edges = [(0, 1), (1, 0), (1, 2), (3, 4), (2, 3), (3, 5),(3, 4)]
    g = Graph(edges)
    print g.nodes
    g.add(3, 7)
    g.delete(0, 1)
    print g.nodes
    print g.neighbors(1)
    print g.adjacent(2, 3)

if(__name__ == '__main__'):
    main()
