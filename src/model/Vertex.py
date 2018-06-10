
class Vertex:
    """
    Simple Node class
    """

    def __init__(self, data, weight = 0):
        self.data = data
        self.weight = weight

    def get_data(self):
        return self.data

    def get_weight(self):
        return self.weight

    def update_data(self, data):
        """
        Update the data whose belong to the node

        param:
        ----------------
        data(obj)   : It can be string, int etc..
        """

        if (data is not None):
            self.data = data
        else:
            raise ValueError("Data cannot be empty")

    def update_weight(self, weight):
        """
        Re-weight the node

        param:
        ----------------
        weight(int) : Weight or capacity of node
        """

        try:
            i = int(weight)
            f = float(weight)
            self.weight = weight
        except :
            raise TypeError("Invalid weight type")
