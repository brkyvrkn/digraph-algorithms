

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

    def add_node(self, node):
        """
        Add node if it does not exist

        param:
        ----------------
        node    : node which will be added
        """

        if node not in self.vertices:
            self.vertices.append(node)
            self.isolated_nodes.append(node)
            self.size += 1
        else:
            raise DeprecationWarning("Node has already existed.")

    def add_edge(self, node1, node2, bidirectional = False):
        """
        Create edge between node1 and node2. If bidirectional is True then create an edge also node2 to node1

        param:
        ----------------
        node1   : Source vertex
        node2   : Target vertex
        bidirectional(bool)   : Determine the direction
        """

        if (node1 in self.vertices and node2 in self.vertices):
            if (node1 in self.isolated):
                self.isolated.remove(node1)
            elif (node2 in self.isolated):
                self.isolated.remove(node2)
            else:
                e1 = (node1, node2)
                e2 = (node2, node1)
                if (bidirectional):
                    self.edges.extend([e1,e2])
                else:
                    self.edges.append(e1)
                self.volume += 1
        else:
            raise IOError("Given vertex is not in graph.")

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
        single_vertices=[]
        temp_list=[]
        for adjacents in self.edges:
            temp_list.append(adjacents[0])
        [single_vertices.append( k ) for k in self.vertices if (k not in temp_list)]
        return single_vertices

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
            dot_file.writelines(i[0] + "->" + i[1] + "\n")
        for j in self.isolated_nodes():
            dot_file.writelines(j + "\n")     #single vertices write to end
        dot_file.write("}")
        dot_file.close()

    def shortest_path(self, start_vertex, end_vertex, path=[]):
        """
        Finds the shortest path by using Breath First Search(BFS) algorithm
        With recursive iterative method

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
                if (searching_edge[0]==active_node) and (searching_edge[1] not in Queue) and (searching_edge[1] not in visited):
                    Queue.append(searching_edge[1])     #vertex coloring
                    if (searching_edge[1]==end_vertex):
                        path.append((active_node,searching_edge[1]))
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
                    if (edge[0]==node) and (edge[1] not in visited):
                        tree[level_counter]+=[edge[1]]            #children adding to tree as multiple value by list
                        visited.append(edge[1])
            level_counter+=1
        del tree[0]
        return tree

    def is_connected(self):
        # TODO: Take the more efficient algorithm to determine whether graph is conencted or not
        return len(self.isolated_nodes())==0
