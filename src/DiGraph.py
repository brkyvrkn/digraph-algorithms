
class DiGraph():

    def __init__(self, vertices, edges):
        """
        G = (V,E)

        attributes:
        ----------------
        vertices    : type is list and store the all vertices
        edges       : type is list of tuples which stores the directionally edges (a,b) means 'a' -> 'b'
        """

        self.vertices=vertices
        self.edges=edges

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def isolated_nodes(self):
        """
        Determine the single nodes in graph
        
        params:
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
