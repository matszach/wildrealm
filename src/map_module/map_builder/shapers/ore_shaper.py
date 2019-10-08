from src.map_module.map_builder.shapers._shaper import Shaper
from src.map_module.worldmap import WorldMap
from random import random


class OreShaper(Shaper):

    def shape(self, wmap: WorldMap, possible_wall_ids: list, step: float = 0.08, z_seed: float = 0,
              ore_id: int = 3, limit: float = -0.85, density: float = 0.8):

        for x in range(wmap.x_size):
            for y in range(wmap.y_size):

                # skip not possible walls
                if not wmap.walls[x, y] in possible_wall_ids:
                    continue

                v = self.noise_generator.noise3(x * step, y * step, z_seed)
                if v < limit:
                    if random() < density:
                        wmap.walls[x, y] = ore_id
