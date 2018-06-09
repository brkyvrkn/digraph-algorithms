
from src.DiGraphGenerator import specify_edges, specify_vertices
from src.DiGraph import DiGraph

def test_digraph(graph):
    vertices = specify_vertices(graph)
    edges = specify_edges(graph)
    digraph = DiGraph(vertices, edges)
    sp = digraph.shortest_path("a","d")
    n = digraph.neighbours_of("a")
    print(sp)
    print(n)