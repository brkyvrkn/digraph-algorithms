
from src.DiGraphGenerator import specify_edges, specify_vertices
from src.DiGraph import DiGraph

def test_digraph(graph):
    vertices = specify_vertices(graph)
    edges = specify_edges(graph)
    digraph = DiGraph(vertices, edges)
    sp = digraph.shortest_path("buibuis","hotfoot")
    n = digraph.neighbours_of("hotfoot")
    iso = digraph.isolated_nodes()
    c = digraph.is_connected()
    print("A -> D : {0} \t Neighbours of A : {1} \t Isolated Nodes : {2} \t Is Connected : {3}".format(sp, n, iso, c))