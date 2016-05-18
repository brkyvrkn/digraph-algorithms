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
