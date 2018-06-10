
from time import time
import networkx as nx

from src.DiGraph import DiGraph
from src.model.Edge import Edge


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
    for node in graph.keys():
        vertices.append(node)
    return vertices

def specify_edges(graph):
    edges=[]
    for node in graph:
        for i in graph[node]:
            edges.append(Edge(node,i))
    return edges

def design_graph_object(graph, G = None):
    """
    Create the DiGraph object without creating a list

    param:
    ----------------
    graph(dict) : Dictionary graph format, 
    G(DiGraph)  : DiGraph object (It doesn't belong to Networkx library)

    return:
    ----------------
    G(DiGraph)  : Object returning
    """
    if (not G):
        G = DiGraph()
    for node in graph.keys():
        if (node not in G.get_vertices()):
            G.add_node(node)
        for ng in graph[node]:
            if (ng not in G.get_vertices()):
                G.add_node(ng)
            G.add_edge(node,ng)
    return G

def set_digraph_library(graph,G):
    """
    Design the graph object w.r.t dictionary

    param:
    ----------------
    graph(dict) : Dictionary format the graph
    G(nx.obj)   : DiGraph object

    return:
    ----------------
    G(nx.Digraph)
    """

    for nodes in graph.keys():
        G.add_node(nodes)
        for i in graph[nodes]:
            G.add_edge(nodes,i)
    return G