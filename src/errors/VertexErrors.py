
class VertexErrors(Error):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    