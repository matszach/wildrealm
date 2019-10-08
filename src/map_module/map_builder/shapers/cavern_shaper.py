from src.map_module.worldmap import WorldMap
from src.map_module.map_builder.shapers._shaper import Shaper
from src.map_module.tile_types.wall_tiles.types import SurfaceRockWallTile, DeepRockWallTile
from src.map_module.tile_types.floor_tiles.types import SurfaceStoneFloorTile, DeepStoneFloorTile


class CavernShaper(Shaper):

    def shape(self, wmap: WorldMap, step: float = 0.07, z_seed: float = 0,
              st_limit: float = 0.4):

        for x in range(wmap.x_size):
            for y in range(wmap.y_size):

                if wmap.floors[x, y] == SurfaceStoneFloorTile.id:
                    v = self.noise_generator.noise3(x*step, y*step, z_seed)
                    if v < st_limit:
                        wmap.walls[x, y] = SurfaceRockWallTile.id
                elif wmap.floors[x, y] == DeepStoneFloorTile.id:
                    v = self.noise_generator.noise3(x*step, y*step, z_seed)
                    if v < st_limit:
                        wmap.walls[x, y] = DeepRockWallTile.id





