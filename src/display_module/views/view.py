
class View:

    """
    stops all active gui nodes
    """
    def close(self):
        for n in self.nodes:
            n.deactivate()

    """
    initiates view's nodes
    """
    def initiate(self):
        pass

    # constructor
    def __init__(self):

        # list of view's gui nodes
        self.nodes: list = []

        self.initiate()
