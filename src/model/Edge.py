
class Edge:
    """
    Edge class with direction

    attr:
    ----------------
    node1(obj)  : source node
    node2(obj)  : target node
    weight(int) : weight or capacity of edge
    """

    def __init__(self, node1, node2, weight = 0):
        self.__node1 = node1
        self.__node2 = node2
        self.__weight = weight

    def get_node1(self):
        return self.__node1

    def get_node2(self):
        return self.__node2

    def set_node(self, node, source = True):
        """
        Update the source node in the edge

        param:
        ----------------
        node(obj)   : Vertex which will be added
        source(bool): If it is True then setting the source node, otherwise setting the target node
        """

        if (node is not None and source):
            self.__node1 = node
        elif (node is not None and not source):
            self.__node2 = node
        else:
            raise ValueError("Vertex cannot be null")

    def update_edge(self, source, target):
        """
        Update the edge

        param:
        ----------------
        source(obj) : Source node
        target(obj) : Target node
        """

        if (source is not None and target is not None):
            self.__node1 = source
            self.__node2 = target
        else:
            raise ValueError("Vertex cannot be null")