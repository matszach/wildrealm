from src.map_module.worldmap import WorldMap
from random import random
from perlin import SimplexNoise
from src.map_module.tile_types.wall_tiles.types import *
from src.map_module.tile_types.floor_tiles.types import *
from src.map_module.map_builder.shapers.floor_shaper import FloorShaper
from src.map_module.map_builder.shapers.cavern_shaper import CavernShaper
from src.map_module.map_builder.shapers.forest_shaper import ForestShaper
from src.map_module.map_builder.shapers.ore_shaper import OreShaper
from src.map_module.map_builder.spawners.single_wall_spawner import SingleWallSpawner
from src.map_module.map_builder.spawners.single_wall_replacer import SingleWallReplacer
from src.map_module.map_builder.structure_generators.plank_shack_generator import PlankShackGenerator
from src.map_module.map_builder.structure_generators.mountain_fortress_generator import MountainFortressGenerator
from src.threading_module.thread_manager import ThreadManager


# builds a map_module map
class MapBuilder:

    @staticmethod
    def get_z_seed() -> float:
        return random() * 1000000

    def build(self, x_size: int = 1024, y_size: int = 1024):
        ThreadManager.start_daemon(self._construct_new_map, (x_size, y_size))

    def _construct_new_map(self, x_size: int = 1024, y_size: int = 1024):

        # initialisation
        self.map_ready = False
        self.completion = 0
        self.wmap = WorldMap(x_size=x_size, y_size=y_size)

        # terrain
        self.message = 'Generating terrain ...'
        self.floor_shaper.shape(self.wmap, z_seed=self.get_z_seed())
        self.completion = 10
        self.single_wall_spawner.spawn(self.wmap, SurfaceRockWallTile.id, [SurfaceStoneFloorTile.id], 0.01)
        self.completion = 20
        self.single_wall_spawner.spawn(self.wmap, DeepRockWallTile.id, [DeepStoneFloorTile.id], 0.02)
        self.completion = 30

        # caves and ores
        self.message = 'Generating caverns ...'
        self.cavern_shaper.shape(self.wmap, z_seed=self.get_z_seed())
        self.completion = 40

        self.message = 'Placing ores ...'
        self.ore_shaper.shape(self.wmap, z_seed=self.get_z_seed(), ore_id=CopperVeinWallTile.id,
                              possible_wall_ids=[SurfaceRockWallTile.id, DeepRockWallTile.id])
        self.completion = 45
        self.ore_shaper.shape(self.wmap, z_seed=self.get_z_seed(), ore_id=IronVeinWallTile.id,
                              possible_wall_ids=[SurfaceRockWallTile.id, DeepRockWallTile.id])
        self.completion = 50
        self.ore_shaper.shape(self.wmap, z_seed=self.get_z_seed(), ore_id=SilverVeinWallTile.id,
                              possible_wall_ids=[DeepRockWallTile.id])
        self.completion = 55
        self.ore_shaper.shape(self.wmap, z_seed=self.get_z_seed(), ore_id=GoldVeinWallTile.id,
                              possible_wall_ids=[DeepRockWallTile.id])
        self.completion = 60

        # forests and plants
        self.message = 'Generating forests ...'
        self.forest_shaper.shape(self.wmap, z_seed=self.get_z_seed())
        self.completion = 70

        self.message = 'Placing plants ...'
        self.single_wall_spawner.spawn(self.wmap, SeaweedWallTile.id, [ShallowWaterFloorTile.id], 0.01)
        self.completion = 75
        self.single_wall_replacer.spawn(self.wmap, BerryBushWallTile.id, [TreeWallTile.id], 0.02)
        self.completion = 80

        # structures
        self.message = 'Generating structures ...'
        self.plank_shack_generator.generate(self.wmap, [GrassFloorTile.id], 0.001, 100)
        self.completion = 85
        self.mountain_fortress_generator.generate(self.wmap, [SurfaceStoneFloorTile.id], 0.0005, 300)
        self.completion = 90

        # treasure chests
        self.message = 'Placing treasures ...'
        self.single_wall_spawner.spawn(self.wmap, WoodenTreasureChestWallTile.id,
                                       [GrassFloorTile.id], 0.0005)
        self.single_wall_spawner.spawn(self.wmap, WoodenTreasureChestWallTile.id,
                                       [SurfaceStoneFloorTile.id, DeepStoneFloorTile.id], 0.003)
        self.completion = 95
        self.single_wall_spawner.spawn(self.wmap, WaterTreasureChestWallTile.id,
                                       [SandFloorTile.id, ShallowWaterFloorTile.id], 0.0005)
        self.single_wall_spawner.spawn(self.wmap, MagicTreasureChestWallTile.id,
                                       [DeepStoneFloorTile.id], 0.003)

        # finalisation
        self.message = 'New World created!'
        self.map_ready = True
        self.completion = 100

    # constructor
    def __init__(self):

        # current builder state message
        self.message: str = ''
        self.completion: int = 0  # out of 100%

        # current map status
        self.map_ready: bool = False

        # map being worked on
        self.wmap: WorldMap = None

        # map builder tools
        noise_generator = SimplexNoise()
        self.floor_shaper = FloorShaper(noise_generator)
        self.cavern_shaper = CavernShaper(noise_generator)
        self.forest_shaper = ForestShaper(noise_generator)
        self.ore_shaper = OreShaper(noise_generator)

        self.single_wall_spawner = SingleWallSpawner()
        self.single_wall_replacer = SingleWallReplacer()

        self.plank_shack_generator = PlankShackGenerator()
        self.mountain_fortress_generator = MountainFortressGenerator()
