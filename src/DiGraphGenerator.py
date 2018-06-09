
from time import time
import networkx as nx

def text_to_dict(filename):
    """
    Read from given file and converts to the dictionary format

    params:
    ----------------
    filename    : String format FILE PATH!

    return:
    ----------------
    graph       : graph in dictionary type
    """
    in_file=open(filename,"r")
    lines=in_file.read()
    in_file.close()
    open_bracket=lines.index("{")
    close_bracket=lines.index("}")
    graph = eval(lines[open_bracket:close_bracket+1])
    return graph

def specify_vertices(graph):
    vertices=[]
    for nodes in graph.keys():
        vertices.append(nodes)
    return vertices

def specify_edges(graph):
    edges=[]
    for node in graph:
        for i in graph[node]:
            edges.append((node,i))
    return edges

def set_digraph_library(graph,G):
    for nodes in graph.keys():
        G.add_node(nodes)
        for i in graph[nodes]:
            G.add_edge(nodes,i)