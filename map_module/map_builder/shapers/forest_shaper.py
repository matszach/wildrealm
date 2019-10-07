from map_module.map_builder.shapers._shaper import Shaper
from map_module.worldmap import WorldMap
from random import random
from map_module.tile_types.floor_tiles.types import GrassFloorTile
from map_module.tile_types.wall_tiles.types import TreeWallTile


class ForestShaper(Shaper):

    @staticmethod
    def get_message():
        return 'Shaping forests'

    def shape(self, wmap: WorldMap, step: float = 0.005, z_seed: float = 0,
              df_limit: float = -0.7, df_density: float = 0.3,
              sf_limit: float = 0.5, sf_density: float = 0.1,
              def_density: float = 0.01):

        for x in range(wmap.x_size):
            for y in range(wmap.y_size):

                # skip non grass floors
                if not wmap.floors[x, y] == GrassFloorTile.id:
                    continue

                v = self.noise_generator.noise3(x * step, y * step, z_seed)
                if v < df_limit:
                    if random() < df_density:
                        wmap.walls[x, y] = TreeWallTile.id
                elif v < sf_limit:
                    if random() < sf_density:
                        wmap.walls[x, y] = TreeWallTile.id
                else:
                    if random() < def_density:
                        wmap.walls[x, y] = TreeWallTile.id
