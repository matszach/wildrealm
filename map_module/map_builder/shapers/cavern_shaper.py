from map_module.worldmap import WorldMap
from map_module.map_builder.shapers._shaper import Shaper


class CavernShaper(Shaper):

    @staticmethod
    def get_message():
        return 'Shaping cavern systems'

    def shape(self, wmap: WorldMap, step: float = 0.07, z_seed: float = 0,
              st_limit: float = 0.4):

        for x in range(wmap.x_size):
            for y in range(wmap.y_size):

                if wmap.floors[x, y] == 4:
                    v = self.noise_generator.noise3(x*step, y*step, z_seed)
                    if v < st_limit:
                        wmap.walls[x, y] = 2
                elif wmap.floors[x, y] == 5:
                    v = self.noise_generator.noise3(x*step, y*step, z_seed)
                    if v < st_limit:
                        wmap.walls[x, y] = 3





