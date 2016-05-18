from DiGraph import *

def text_to_dict(filename):
    in_file=open(filename,"r")
    lines=in_file.read()
    in_file.close()
    open_bracket=lines.index("{")       # find the point which will begin dictionary
    close_bracket=lines.index("}")      # similarly, end point of dict
    graph = eval(lines[open_bracket:close_bracket+1])       # evaluating string to available type
    return graph

def specify_vertices(filename):
    vertices=[]
    graph=text_to_dict(filename)       # call dictionary
    for nodes in graph.keys():      #keys of dictionary is our verteices
        vertices.append(nodes)
    return vertices

def specify_edges(filename):
    edges=[]
    graph=text_to_dict(filename)
    for node in graph:
        for i in graph[node]:           # assign keys to value
            edges.append((node,i))          # concat as tuple similar like G=(V,E)
    return edges

vertices=specify_vertices("graph.txt")
edges=specify_edges("graph.txt")
graphviz=DiGraph(vertices, edges)
print "Vertices of digraph are\n" , graphviz.get_vertices()
print "Edges of digraph are\n" , graphviz.get_edges()
print "Isolated Nodes of digraph are\n" , graphviz.isolated_nodes()
graphviz.toDotFormat("Digraph.dot")
