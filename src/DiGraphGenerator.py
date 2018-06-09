from DiGraph import *
from Writer import *
import time
import networkx as nx
import random

def text_to_dict(filename):
    in_file=open(filename,"r")
    lines=in_file.read()
    in_file.close()
    open_bracket=lines.index("{")       # find the point which will begin dictionary
    close_bracket=lines.index("}")      # similarly, end point of dict
    graph = eval(lines[open_bracket:close_bracket+1])       # evaluating string to available type
    return graph

def specify_vertices(graph):
    vertices=[]
    for nodes in graph.keys():      #keys of dictionary is our verteices
        vertices.append(nodes)
    return vertices

def specify_edges(graph):
    edges=[]
    for node in graph:
        for i in graph[node]:           # assign keys to value
            edges.append((node,i))          # concat as tuple similar like G=(V,E)
    return edges

def set_digraph_library(filename,obj):
    graph=text_to_dict(filename)
    for nodes in graph.keys():      #keys of dictionary is our vertices
        obj.add_node(nodes)
        for i in graph[nodes]:           # assign keys to value
            obj.add_edge(nodes,i)

file=open("datas.txt","w")      #the file store the datas of elapsed time each #of vertices 
graph_creating=Writer()		 #to create new graph, call Writer class
name_of_graph_files=["sample1.txt","sample2.txt","sample3.txt","sample4.txt","sample5.txt","sample6.txt","sample7.txt","sample8.txt","sample9.txt","sample10.txt"]
counter=0
for x in range(500,5500,500):               #the loop creates graph dictionary with 500 to 5000 vertices
    graph_creating.write_to(name_of_graph_files[counter],x)         #graph is created via Writer class

    graph=text_to_dict(name_of_graph_files[counter])            #graph prepearing for DiGraph class
    vertices = specify_vertices(graph)
    edges = specify_edges(graph)
    directed_graph = DiGraph(vertices, edges)           #vertices and edges are sent to class

    di_graph_lib = nx.DiGraph()             #Object creates from library
    set_digraph_library(name_of_graph_files[counter], di_graph_lib)     #graph creates from helper function in library
    file.write("\nFor " + str(x) + "vertices:\n")
    for x in range(5):
        vertex1 = random.choice(graph.keys())           #random vertex1
        vertex2 = random.choice(graph.keys())           #random vertex which are searched any path from vertex1
        start_lib = time.clock()
        temp_path = nx.shortest_path(di_graph_lib, vertex1, vertex2)
        file.writelines("%s to %s is %s ====> Elapsed time is %ssecond with library\n" % (vertex1, vertex2, str(temp_path), str(time.clock() - start_lib)))
        start_class = time.clock()
        file.writelines("%s to %s is %s ====> Elapsed time is %ssecond with class\n" % (vertex1, vertex2, str(directed_graph.find_shortest_path(vertex1, vertex2, [])), str(time.clock() - start_class)))
    counter+=1
file.close()
