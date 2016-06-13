#Forever Freshcoders

class DiGraph():

    def __init__(self, vertices, edges):
        self.vertices=vertices
        self.edges=edges

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def isolated_nodes(self):
        single_vertices=[]
        temp_list=[]
        for adjacents in self.edges:
            temp_list.append(adjacents[0])
        [single_vertices.append( k ) for k in self.vertices if (k not in temp_list)]        # concatenating the single vertex to list
        return single_vertices

    def toDotFormat(self,dotfile):
        dot_file=open(dotfile,"w")
        dot_file.write("Digraph {\n")
        for i in self.edges:
            dot_file.writelines(i[0] + "->" + i[1] + "\n")
        for j in self.isolated_nodes():
            dot_file.writelines(j + "\n")     #single vertices write to end
        dot_file.write("}")
        dot_file.close()

    def find_shortest_path(self, start_vertex, end_vertex, path=[]):
        if (start_vertex==end_vertex):          #base case
            return path[::-1]
        Queue=[start_vertex]            #breath first queue
        visited=[]          #visiting nodes stored in
        while (Queue):
            active_node=Queue.pop(0)        #according to BFS algorithm, we must have active node
            visited.append(active_node)
            for searching_edge in self.edges:
                if (searching_edge[0]==active_node) and (searching_edge[1] not in Queue) and (searching_edge[1] not in visited):    #the vertex which are not already coloring go in the statement
                    Queue.append(searching_edge[1])
                    if (searching_edge[1]==end_vertex):             #any vertex are adjacent with end vertex, new end_vertex be that also last edge of shortest path
                        path.append((active_node,searching_edge[1]))
                        return self.find_shortest_path(start_vertex, active_node, path)       #recursively call

    def neighbours_of(self,root,level=1):
        tree={}             #stored in neighbours in terms of distance to root vertex
        tree[0]=[root]            #0. level is the root itself
        visited=[root,]
        level_counter=1         #each distance counting with
        while (level_counter <= level):
            tree[level_counter]=[]          #multiple values stored in specifying keys
            for node in tree[level_counter-1]:          #active node traverse in previous neighbours
                for edge in self.edges:
                    if (edge[0]==node) and (edge[1] not in visited):
                        tree[level_counter]+=[edge[1]]            #children adding to tree as multiple value by list
                        visited.append(edge[1])
            if (tree[level_counter]==[]):           #Before arrived specifying level, to prevent extra memory break out the method if it has no other neighbour
                del tree[level_counter]         #deleting empty list to save the memory
                return tree                #break out and return level tree
            level_counter+=1
        return tree

    def is_connected(self):
        return len(self.isolated_nodes())==0
