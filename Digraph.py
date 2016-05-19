#Forever Freshcoders

class Queue:
    def __init__(self):
        self._items = []        #protected queue that stored vertices based on BFS algorithm

    def is_empty(self):
        return self._items == []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

class DiGraph(Queue):

    def __init__(self, vertices, edges,):
        Queue.__init__(self)
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

    def __bfs(self,root,term):		#private method that only execute in Digraph not in main function
        Q=Queue()
        Q.enqueue(root)			#enqueue the rooted vertex by application of BFS algorithm
        visited=[]
        tree=[[root]]           #appending all visited nodes according to its level
        counter=0

        while (Q.is_empty() is False):
            node=Q.dequeue()
            visited.append(node)

            for edge in self.edges:
                if (edge[term]==node) and (edge[1-term] not in visited) and (edge[1-term] not in Q._items):		#if the node already searching, then not go in that statement
                    Q.enqueue(edge[1-term])

            if (len(visited)==1):		#the vertex which contain in level 1
                counter+=Q.size()
                tree.append([x for x in Q._items])

            elif (len(visited) - counter == 1):			#the other level of vertices checking
                tree.append([x for x in Q._items])
                counter+=Q.size()

        return visited,tree[:-1]		#get rid of extra list at the end of the 2D tree list

    def neighbours_of(self,vertex,level=1,term="out"):         #default level of neighbourhood is 1 it means that default parameter is nearest neighbours also default term of neighbourhood is out-neighbourhood
        if (term=="in"):           #if term is in-neighbours
            k=1           #according to algorithm, if in-neighbour then it'll look at 1. index of edges
        else:          #if term is out-neighbours
            k=0              #according to algorithm, if out-neighbour then it'll look at 0. index of edges

        traversing_vertices,tree_of_root=self.__bfs(vertex,k)        #bfs algorithm helps us to find the neighbours both 'out' and 'in'
        to_str_neighbours=""

        for i in range(1,level+1):
            if i<=len(tree_of_root)-2:
                to_str_neighbours+= str(i) + ". level " + term + "-neighbour(s) of vertex " + vertex + " is/are " + str([ x for x in tree_of_root[i] ]) + "\n"
            elif i>len(tree_of_root)-2:           #if entering the level is greater than the height of tree, then getting out of loop
                to_str_neighbours+= "The vertex " + vertex + " hasn't got any neighbour in " + str(i) + ". level\n"

        return to_str_neighbours

    def connectivity(self,vertex):          #any vertex can be given as parameter.
        return len(self.vertices)==len(self.__bfs(vertex,"out"))

    def shortest_path(self,vertex1,vertex2):
        pass


