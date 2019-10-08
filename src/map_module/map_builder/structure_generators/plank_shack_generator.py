from src.map_module.map_builder.structure_generators._structure_generator import StructureGenerator
from src.map_module.worldmap import WorldMap
from src.map_module.tile_types.wall_tiles.types import PlankWallTile, AirWallTile, WoodenTreasureChestWallTile
from src.map_module.tile_types.floor_tiles.types import PlankFloorTile
from random import randint, random


class PlankShackGenerator(StructureGenerator):

    def _build(self, wmap: WorldMap, x_origin: int, y_origin: int):

        # generating wall offsets from the origin point
        min_o = 2
        max_o = 4

        xl = randint(min_o, max_o)
        xr = randint(min_o, max_o)
        yl = randint(min_o, max_o)
        yr = randint(min_o, max_o)

        # placing the generated structure
        for x in range(x_origin - xl, x_origin + xr + 1):
            for y in range(y_origin - yl, y_origin + yr + 1):
                self._place_floor(wmap, x, y, PlankFloorTile.id)
                if x - x_origin in (-xl, xr) or y - y_origin in (-yl, yr):
                    self._place_wall(wmap, x, y, PlankWallTile.id)
                else:
                    self._place_wall(wmap, x, y, AirWallTile.id)

        # generating a chest with a 50% chance
        if random() > 0.5:
            self._place_wall(wmap, x_origin, y_origin, WoodenTreasureChestWallTile.id)





