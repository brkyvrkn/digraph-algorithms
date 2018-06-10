
from src.model.Edge import Edge

class DiGraph:
    """
    Directed Graph with unweighted

    attributes:
    ----------------
    vertices(list)  : type is list and store the all vertices
    edges(list)     : type is list of tuples which stores the directionally edges (a,b) means 'a' -> 'b'
    isolated(list)  : stores the single nodes (which has no edge)
    size(int)       : specify the number of vertex
    volume(int)     : specify the number of edge
    """

    def __init__(self, vertices = [], edges = []):
        """
        G = (V,E)
        """

        self.vertices = vertices
        self.edges = edges
        self.isolated = self.isolated_nodes()
        self.size = len(vertices)
        self.volume = len(edges)

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def set_vertices(self, vertices):
        """
        Add node list to class, which has the type of list of objects

        param:
        ----------------
        vertices    : list of whole vertices

        return:
        ----------------
        (void)
        """

        if (vertices is not None):
            self.vertices = vertices
        else:
            raise IOError("Node list is empty")

    def set_edges(self, edges):
        """
        Set the edge list in the class

        param:
        ----------------
        edges   : list of tuples that contain (a,b) as a->b
        """

        if (edges is not None):
            self.edges = edges
        else:
            raise IOError("Edge list is empty")

    def __str__(self):
        return "\nDiGraph has {0} vertices and {1} edges which are \nNodes:\t{2}\nEdges:\t{3}\n".format(len(self.vertices), len(self.edges), self.vertices, [str(e) for e in self.edges])

    def get_vertex_from_label(self, label):
        for v in self.vertices:
            if (label == v.get_label()):
                return v
        return None
    
    def add_node(self, label, weight = 0):
        """
        Add node if it does not exist

        param:
        ----------------
        node    : node which will be added
        w       : weight of node which is default as 0
        """
        if label not in self.vertices:
            self.vertices.append(label)
            self.isolated.append(label)
            self.size += 1
        else:
            raise DeprecationWarning("Node has already existed.")

    def add_edge(self, node1, node2, weight = 1, bidirectional = False):
        """
        Create edge between node1 and node2. If bidirectional is True then create an edge also node2 to node1

        param:
        ----------------
        node1   : Source vertex
        node2   : Target vertex
        bidirectional(bool)   : Determine the direction
        """

        if (node1 in self.vertices and node2 in self.vertices):
            e1 = Edge(node1, node2, weight=weight)
            e2 = Edge(node1, node2, weight=weight)
            if (node1 in self.isolated):    self.isolated.remove(node1)
            if (node2 in self.isolated):    self.isolated.remove(node2)
            if (bidirectional):
                self.edges.extend([e1,e2])
            else:
                self.edges.append(e1)
            self.volume += 1
        else:
            raise IOError("Given vertex is not in graph.")

    def __isolated_recursive(self, nodes, iso=[]):
        """
        Proceed on the noeighbours
        If a node has no neighbour then append to isolateds
        """
        #FIXME
        if(len(nodes) == 0):
            return iso
        else:
            active = nodes[0]
            neigh = self.neighbours_of(active)[1]   #1st level neighbour
            if (len(neigh) == 0):
                iso.append(active)
            visited = set([active] + neigh)
            return self.__isolated_recursive(list(set(nodes) - visited),iso)

    def isolated_nodes(self):
        """
        Determine the single nodes in graph
        
        param:
        ----------------
        null

        return:
        ----------------
        single_vertices : which stores the single nodes as in the type of 1D list
        """
        nodes = self.vertices[:]
        return self.__isolated_recursive(nodes, iso = [])

    def adjacency_matrix(self):
        """
        Get the adjacency matrix as row-based
        i.e. element in 3rd row, 4th column correspondings to adj[3][4]
        """
        #TODO: arrange it
        encoding = enumerate([v for v in self.vertices])
        dim = len(self.vertices)
        adj = [[0] * dim] * dim
        
        for key, value in encoding:
            for i in range(dim):
                pass

    def to_dot_format(self,dotfile):
        """
        Converts the graph to .dot format for illustrating in the graphviz

        params:
        ----------------
        dotfile : name of file in the string format

        return:
        ----------------
        (void)
        """
        dot_file=open(dotfile,"w")
        dot_file.write("Digraph {\n")
        for i in self.edges:
            dot_file.writelines(i.get_node1() + "->" + i.get_node2() + "\n")
        for j in self.isolated_nodes():
            dot_file.writelines(j + "\n")     #single vertices write to end
        dot_file.write("}")
        dot_file.close()

    def shortest_path(self, start_vertex, end_vertex, path=[]):
        """
        Finds the shortest path by using Breath First Search(BFS) algorithm
        With recursive iterative method
        If path duplicate then send the empty list as an argument, List stores as a reference in python!

        params:
        ----------------
        start_vertex    : source node
        end_vertex      : target node
        path            : by default is empty list which will stores the edges in the type of list of tuples

        return:
        ----------------
        path            : list of tuples which define the directional edges
        """
        if (start_vertex==end_vertex):
            return path[::-1]
        Queue=[start_vertex]
        visited=[]
        while (Queue):
            active_node=Queue.pop(0)
            visited.append(active_node)
            for searching_edge in self.edges:
                if (searching_edge.get_node1()==active_node) and (searching_edge.get_node2() not in Queue) and (searching_edge.get_node2() not in visited):
                    Queue.append(searching_edge.get_node2())     #vertex coloring
                    if (searching_edge.get_node2()==end_vertex):
                        path.append((active_node,searching_edge.get_node2()))
                        return self.shortest_path(start_vertex, active_node, path)

    def neighbours_of(self,root,level=1):
        """
        Get the neighbours of given node as root with the level

        param:
        ----------------
        root    : node what you search its neighbours
        level   : how many neighbour will take

        return:
        ----------------
        tree    : of neighbours stores in the dictionary type
        """
        tree={}
        tree[0]=[root]      #TODO: should not be necessary to assign 0.th element root itself.
        visited=[root,]
        level_counter=1
        while (level_counter <= level):
            tree[level_counter]=[]
            for node in tree[level_counter-1]:          #active node traverses in previous neighbours
                for edge in self.edges:
                    if (edge.get_node1()==node) and (edge.get_node2() not in visited):
                        tree[level_counter]+=[edge.get_node2()]            #children adding to tree as multiple value by list
                        visited.append(edge.get_node2())
            level_counter+=1
        del tree[0]
        return tree

    def is_connected(self):
        # TODO: Take the more efficient algorithm to determine whether graph is conencted or not
        # return len(self.isolated_nodes())==0
        return (len(self.isolated) == 0)
