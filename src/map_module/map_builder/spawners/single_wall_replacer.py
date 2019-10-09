from src.map_module.worldmap import WorldMap
from random import random


class SingleWallReplacer:

    """
    Iterates over the map and randomly places a wall tile of given id
    :param wmap - the map being worked on
    :param wall_id - id of the wall tile spawned
    :param possible_wall_ids - ids of the walls that the new wall can replace
    :param spawn_chance - a chance that the wall will be placed on each valid floor tile
    """
    @staticmethod
    def spawn(wmap: WorldMap, wall_id: int, possible_walls_ids: list, spawn_chance: float):

        for x in range(wmap.x_size):
            for y in range(wmap.y_size):

                if wmap.walls[x, y] in possible_walls_ids:
                    if random() < spawn_chance:

                        wmap.walls[x, y] = wall_id
