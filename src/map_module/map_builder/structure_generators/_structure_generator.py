from src.map_module.worldmap import WorldMap
from random import random


class StructureGenerator:

    @staticmethod
    def generate(wmap: WorldMap, possible_floor_ids: list, spawn_chance: float):

        for x in range(wmap.x_size):
            for y in range(wmap.y_size):

                if wmap.floors[x, y] in possible_floor_ids:
                    if random() < spawn_chance:

                        StructureGenerator._build(wmap, x, y)

    """
    describes structure's creation algorithm
    :param wmap - map being worked on
    :param x_origin, y_origin - central location of the structure
    """
    @staticmethod
    def _build(wmap: WorldMap, x_origin: int, y_origin: int):
        pass
