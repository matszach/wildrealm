from src.map_module.worldmap import WorldMap
from random import random
from math import sqrt


class StructureGenerator:

    def generate(self, wmap: WorldMap, possible_floor_ids: list, spawn_chance: float, min_range: int = 100):

        for x in range(wmap.x_size):
            for y in range(wmap.y_size):

                if wmap.floors[x, y] in possible_floor_ids:
                    if random() < spawn_chance:
                        if not self._similar_structure_in_range(x, y, min_range):
                            self._already_build.append((x, y))
                            self._build(wmap, x, y)

    """
    makes sure that no structures of the same have already been created nearby 
    :param x_origin, y_origin - central location of the structure
    :param min_range - minimum distance between the closest instance 
                       of the currently generated structure
    """
    def _similar_structure_in_range(self, x_origin: int, y_origin: int, min_range: int = 100):
        for structure in self._already_build:
            if sqrt((structure[0] - x_origin)**2 + (structure[1] - y_origin)**2) < min_range:
                return True
        return False

    """
    describes structure's creation algorithm
    :param wmap - map being worked on
    :param x_origin, y_origin - central location of the structure
    """
    def _build(self, wmap: WorldMap, x_origin: int, y_origin: int):
        pass

    """
    safe handles index errors when generating structures
    on the border of the map
    """
    @staticmethod
    def _place_wall(wmap: WorldMap, x: int, y: int, wall_id: int):
        try:
            wmap.walls[x, y] = wall_id
        except IndexError:
            pass

    @staticmethod
    def _place_floor(wmap: WorldMap, x: int, y: int, floor_id: int):
        try:
            wmap.floors[x, y] = floor_id
        except IndexError:
            pass

    def __init__(self):
        # holds origin points
        self._already_build = []
