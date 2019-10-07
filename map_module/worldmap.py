import numpy


# map_module's field map and field state
class WorldMap:

    def __init__(self, x_size=512, y_size=512):

        # map sizes
        self.x_size = x_size
        self.y_size = y_size

        # floor tile ids
        self.floors = numpy.zeros((self.x_size, self.y_size))

        # wall tile ids
        self.walls = numpy.zeros((self.x_size, self.y_size))
