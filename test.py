
from src.di_graph_generator import specify_edges, specify_vertices, design_graph_object
from src.DiGraph import DiGraph

def test_digraph(graph):
    vertices = specify_vertices(graph)
    edges = specify_edges(graph)
    digraph = DiGraph(vertices, edges)
    print(digraph)
    digraph.adjacency_matrix()
    sp = digraph.shortest_path("a","d",path=[])
    n = digraph.neighbours_of("a")
    iso = digraph.isolated_nodes()
    c = digraph.is_connected()
    print("A -> D : {0} \t Neighbours of A : {1} \t Isolated Nodes : {2} \t Is Connected : {3}".format(sp, n, [str(i) for i in iso], c))

def test_design(graph):
    G = design_graph_object(graph, DiGraph())
    print(G)
    sp = G.shortest_path("a","d",path = [])
    n = G.neighbours_of("a")
    iso = G.isolated_nodes()
    c = G.is_connected()
    print("A -> D : {0} \t Neighbours of A : {1} \t Isolated Nodes : {2} \t Is Connected : {3}".format(sp, n, iso, c))