from src.map_module.worldmap import WorldMap
from random import random
from src.map_module.tile_types.wall_tiles.types import AirWallTile


class SingleWallSpawner:

    """
    Iterates over the map and randomly places a wall tile of given id
    :param wmap - the map being worked on
    :param wall_id - id of the wall tile spawned
    :param possible_floors - ids of the floors that the wall can be placed on
    :param spawn_chance - a chance that the wall will be placed on each valid floor tile
    """
    @staticmethod
    def spawn(wmap: WorldMap, wall_id: int, possible_floor_ids: list, spawn_chance: float):

        for x in range(wmap.x_size):
            for y in range(wmap.y_size):

                # skip not empty tiles
                if not wmap.walls[x, y] == AirWallTile.id:
                    continue

                if wmap.floors[x, y] in possible_floor_ids:
                    if random() < spawn_chance:

                        wmap.walls[x, y] = wall_id
