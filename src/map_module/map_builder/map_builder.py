from src.map_module.worldmap import WorldMap
from src.map_module.map_builder.shapers.floor_shaper import FloorShaper
from src.map_module.map_builder.shapers.cavern_shaper import CavernShaper
from src.map_module.map_builder.shapers.forest_shaper import ForestShaper
from src.map_module.map_builder.shapers.ore_shaper import OreShaper
from random import random
from perlin import SimplexNoise
from src.map_module.tile_types.wall_tiles.types import \
    SurfaceRockWallTile, DeepRockWallTile, \
    CopperVeinWallTile, IronVeinWallTile, \
    SilverVeinWallTile, GoldVeinWallTile


# builds a map_module map
class MapBuilder:

    @staticmethod
    def get_z_seed() -> float:
        return random() * 1000000

    def build(self, x_size: int = 1024, y_size: int = 1024):

        # initialisation
        m = WorldMap(x_size=x_size, y_size=y_size)

        # terrain
        print(self.floor_shaper.get_message())
        self.floor_shaper.shape(m, z_seed=self.get_z_seed())

        # caves and ores
        print(self.cavern_shaper.get_message())
        self.cavern_shaper.shape(m, z_seed=self.get_z_seed())
        print(self.ore_shaper.get_message())
        self.ore_shaper.shape(m, z_seed=self.get_z_seed(), ore_id=CopperVeinWallTile.id,
                              possible_wall_ids=[SurfaceRockWallTile.id, DeepRockWallTile.id])
        self.ore_shaper.shape(m, z_seed=self.get_z_seed(), ore_id=IronVeinWallTile.id,
                              possible_wall_ids=[SurfaceRockWallTile.id, DeepRockWallTile.id])
        self.ore_shaper.shape(m, z_seed=self.get_z_seed(), ore_id=SilverVeinWallTile.id,
                              possible_wall_ids=[DeepRockWallTile.id])
        self.ore_shaper.shape(m, z_seed=self.get_z_seed(), ore_id=GoldVeinWallTile.id,
                              possible_wall_ids=[DeepRockWallTile.id])

        # forests and plants
        print(self.forest_shaper.get_message())
        self.forest_shaper.shape(m, z_seed=self.get_z_seed())

        # finalisation
        return m

    # constructor
    def __init__(self):

        noise_generator = SimplexNoise()
        self.floor_shaper = FloorShaper(noise_generator)
        self.cavern_shaper = CavernShaper(noise_generator)
        self.forest_shaper = ForestShaper(noise_generator)
        self.ore_shaper = OreShaper(noise_generator)

