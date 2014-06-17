from graph import Graph

def is_complete(g):
    keys = g.nodes.keys()
    complete = True
    for key in keys:
        nodes = set(keys)
        nodes.remove(key)
        if(not(g.nodes[key] == nodes)):
            complete = False
    return complete

def main():
    edges_complete = [(0, 1), (1, 0), (1, 2), (2, 1), (0, 2), (2, 0)]
    edges_incomplete = [(1, 0), (1, 2), (2, 1), (0, 2), (2, 0)]
    print edges_complete, is_complete(Graph(edges_complete))
    print edges_incomplete, is_complete(Graph(edges_incomplete))

if(__name__ == '__main__'):
    main()
